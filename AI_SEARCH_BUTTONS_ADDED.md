# ✅ AI SEARCH BUTTONS ADDED TO EXPLANATION EDITOR

## What Was Added

You can now search for explanations using multiple AI tools directly from the explanation editor modal!

## Changes Made to practice.html

### 1. AI Search Buttons Added to Modal

In the explanation editor modal, four AI search buttons now appear:

```
🔍 Perplexity  |  🤖 ChatGPT  |  🧠 Claude  |  ✨ Gemini
```

Each button:
- Opens the AI tool in a **new tab**
- Searches for the **current question** automatically
- Lets you read the AI explanation while keeping the modal open
- You can then **copy-paste** the explanation back into the textarea

### 2. How It Works

**User Flow:**
1. Click ✏️ **Edit Explanation** button
2. Modal opens with the question and AI buttons
3. Click any AI button (e.g., 🔍 Perplexity)
4. New tab opens with AI already searching your question
5. Read the explanation on the AI site
6. Copy the text
7. Switch back to the modal
8. Paste the explanation into textarea
9. Click **Save Changes**

### 3. AI Search URLs

The buttons automatically create search links for:

- **Perplexity:** `https://www.perplexity.ai/search?q=[question]`
- **ChatGPT:** `https://chatgpt.com/?q=[question]`
- **Claude:** `https://claude.ai/?q=[question]`
- **Google Gemini:** `https://gemini.google.com/app?q=[question]`

### 4. JavaScript Updated

The `openExpModal()` function now:
- Extracts the question text
- Creates URLs for all 4 AI tools
- Sets the href on all buttons
- Opens them in new tabs (target="_blank")

```javascript
const searchQuery = encodeURIComponent(q.question_text || '');
document.getElementById('searchPerplexity').href = 'https://www.perplexity.ai/search?q=' + searchQuery;
document.getElementById('searchChatGPT').href = 'https://chatgpt.com/?q=' + searchQuery;
// ... etc for Claude and Gemini
```

## Visual Layout

```
✏️ Edit Explanation
─────────────────────
Question ID: 12345

Search on AI (to get explanation):
[🔍 Perplexity] [🤖 ChatGPT] [🧠 Claude] [✨ Gemini]

[Large textarea for pasting explanation]

[💾 Save Changes] [Cancel]
```

## Testing

1. **Hard refresh:** `Ctrl+Shift+R`
2. **Go to AP_HC Practice**
3. **Click ✏️ Edit Explanation**
4. **See the 4 AI buttons** at the top
5. **Click one** (opens in new tab)
6. **Read explanation** on AI site
7. **Copy-paste** back to modal
8. **Save Changes**

## Benefits

✅ No need to manually search on different AI sites  
✅ Question text auto-fills in search  
✅ All 4 major AI tools available  
✅ Workflow stays in one modal  
✅ Copy-paste seamlessly  

## Files Modified

- ✅ `templates/practice.html`
  - Added HTML for 4 AI search buttons
  - Updated `openExpModal()` function with dynamic URLs

---

Now when practicing AP_HC questions, you have quick access to multiple AI tools to generate explanations! 🚀
