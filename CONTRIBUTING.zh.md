## 🤝 贡献指南

我们欢迎您的补充和改进！

### 📝 如何添加新论文

1. **获取 BibTeX**  
   访问 [Google Scholar](https://scholar.google.com)，找到论文，点击引号 📖 图标，复制 **BibTeX**。

2. **添加额外字段**  
   请完善 BibTeX，添加以下字段：

   - `link` – DOI 或论文网址（如果有）。  
     _示例_：  

     ```bibtex
     link = {https://doi.org/10.1145/1234567.1234568},
     ```

   - `keywords` – 自定义关键词列表（逗号分隔）。  
     _示例_：  

     ```bibtex
     keywords = {auto-tuning, LLVM, reinforcement learning},
     ```

   - `abstract` – 复制并粘贴论文摘要。

3. **保存条目**  
   将完善后的 BibTeX 条目添加到 `bib/` 目录中对应类别文件的**末尾**。  
   例如，若论文主题为代码优化，则添加到 `bib/code_optimization.bib`。

4. **Fork 并克隆仓库**  
   点击本仓库右上角的“Fork”，然后执行：

   ```bash
   git clone https://github.com/YOUR_USERNAME/AI4Compiler-Collection.git
   cd AI4Compiler-Collection
   ```

5. **创建新分支**

   使用有意义的分支名称，如 patch-001 或 add-paper-transformer23：

   ```bash
   git checkout -b patch-001
   ```
   
   然后添加一些 bib 内容...

6. **生成网站内容**

   完成后执行：

   ```bash
   cd scripts
   python 01-bib2md.py    # 将 bib 转换为 papers/*.md
   python 02-bib2json.py  # 更新 index.json
   cd ..
   ```

7. **预览网站（可选）**

   ```bash
   npm install -g serve
   serve scripts
   ```

   然后在浏览器打开对应网址（例如：http://localhost:3000）。

8. **提交并推送更改**

   ```bash
   git add .
   git commit -m "Add paper on XYZ (2023)"
   git push origin patch-001
   ```

9. **发起 Pull Request**

   1. 进入您 Fork 的 GitHub 仓库（`https://github.com/YOUR_USERNAME/AI4Compiler-Collection`）。
   2. 点击分支名称旁的 **Compare & pull request** 按钮。
   3. 确认基础仓库为 `YOUR_USERNAME/AI4Compiler-Collection` → `main`（或 `master`），源仓库为您的分支。
   4. PR 标题请简洁描述：  
      `Add paper: <论文标题> (年份)`。
   5. PR 描述中请说明：
      - 您添加或修改了什么内容。
      - BibTeX 条目和目标类别路径（例如 `bib/code_optimization.bib`）。
      - 相关的 GitHub issue（如 `Fixes #123`）。
   6. 分配至少一名审阅者（可选但推荐），并添加相关标签（如 `enhancement`，`documentation`）。
   7. 点击 **Create pull request** 提交。
   8. 等待持续集成（CI）检查完成。  
      - 若 CI 失败（如脚本错误），请更新分支修复问题。
   9. 根据审阅意见推送额外提交进行修改。
   10. 审核通过后，您的 PR 将被合并！

   ---

   PR 审核通过后，将合并到主仓库。

   感谢您为 AI4Compiler-Collection 做出的贡献！🌟
