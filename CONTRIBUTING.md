## 🤝 Contributing

We welcome additions and improvements!

### 📝 How to Add a New Paper

1. **Get the BibTeX**  
   Go to [Google Scholar](https://scholar.google.com), find the paper, click the quotation mark 📖 icon, and copy the **BibTeX**.

2. **Add Extra Fields**  
   Please improve the BibTeX with the following fields:

   - `link` – The DOI or paper URL (if available).  
     _Example_:  

     ```bibtex
     link = {https://doi.org/10.1145/1234567.1234568},
     ```

   - `keywords` – A list of your own chosen keywords (comma-separated).  
     _Example_:  

     ```bibtex
     keywords = {auto-tuning, LLVM, reinforcement learning},
     ```

   - `abstract` – Copy and paste the abstract of the paper.

3. **Save the Entry**  
   Place the enhanced BibTeX entry at the **end of the appropriate category file** in the `bib/` directory.  
   For example, if the paper is about code optimization, add it to `bib/code_optimization.bib`.

4. **Fork & Clone the Repo**  
   Click “Fork” in the top right corner of this repository, then:

   ```bash
   git clone https://github.com/YOUR_USERNAME/AI4Compiler-Collection.git
   cd AI4Compiler-Collection
   ```

5. **Create a New Branch**

   Use a meaningful branch name such as patch-001 or add-paper-transformer23:

   ```bash
   git checkout -b patch-001
   ```
   
   Then add some bib contents...

6. **Generate the Website Content**

   When all done...

   ```bash
   cd scripts
   python 01-bib2md.py    # converts bib to papers/*.md
   python 02-bib2json.py  # updates index.json
   cd ..
   ```

7. **Preview the Site (Optional)**

   ```bash
   npm install -g serve
   serve scripts
   ```

   Then open the URL (e.g., http://localhost:3000) in your browser.

8. **Commit & Push Your Changes**

   ```bash
   git add .
   git commit -m "Add paper on XYZ (2023)"
   git push origin patch-001
   ```

9. **Open a Pull Request**

   1. Go to your fork on GitHub (`https://github.com/YOUR_USERNAME/AI4Compiler-Collection`).
   2. Click the **Compare & pull request** button next to your branch name.
   3. Ensure the base repository is `YOUR_USERNAME/AI4Compiler-Collection` → `main` (or `master` if used), and the head repository is your branch.
   4. In the PR title, use a concise, descriptive format:  
      `Add paper: <Paper Title> (Year)`.
   5. In the PR description:
      - Briefly explain what you added or changed.
      - Link to the BibTeX entry and target category (e.g., `bib/code_optimization.bib`).
      - Mention any related GitHub issues (e.g., `Fixes #123`).
   6. Assign at least one reviewer (optional but appreciated) and add relevant labels (e.g., `enhancement`, `documentation`).
   7. Click **Create pull request** to submit.
   8. Wait for continuous integration (CI) checks to complete.  
      - If CI fails (e.g., script errors), update your branch to fix issues.
   9. Respond to any review comments by pushing additional commits to your branch.
   10. Once approved, your PR will be merged!

   ---

   Once your PR is reviewed and approved, it will be merged into the main repository.

   Thank you for contributing to AI4Compiler-Collection! 🌟


