# 📚 ArXiv 每日论文精选

> 每日自动抓取 arXiv 计算机科学领域最新论文，聚焦大模型相关研究

## 📋 项目简介

本项目每日自动抓取 arXiv 上 CS 相关领域的新提交论文，通过 AI 分析进行分类，筛选出与大模型相关的研究，生成结构化日报。

### 分类体系

| 级别 | 类别 | 说明 | 关键词 |
|------|------|------|--------|
| 🔐 **Level 1** | 大模型安全相关研究 | 直接讨论大模型安全问题 | safety、security、attack、jailbreak、alignment、privacy |
| 🧠 **Level 2** | 大模型内生能力研究 | 探索模型各方面能力 | reasoning、planning、knowledge、in-context learning |
| 🔬 **Level 3** | 大模型相关研究 | 与大模型相关的技术 | LLM、transformer、training、fine-tuning、RAG |
| 📄 **Level 4** | 其他研究 | 不属于大模型领域 | 传统 ML、CV、NLP 非 LLM |

---

## 📅 每日报告索引

| 日期 | 论文数量 | 报告链接 |
|------|----------|----------|
| 2026-04-04 | 127 篇 | [查看详情](./papers/2026-04-04.md) |

---

## 🔧 数据来源

- **arXiv Categories**: cs.AI, cs.CL, cs.CV, cs.LG, cs.MA, cs.RO
- **抓取内容**: New Submissions + Cross Submissions
- **更新频率**: 每日自动更新

---

## 📊 统计信息

- **总论文数**: 127 篇（截至 2026-04-04）
- **大模型相关**: ~60% 的论文与大模型研究相关
- **安全研究**: ~15% 聚焦大模型安全

---

## 🚀 使用说明

### 查看今日论文
```bash
# 查看最新报告
cat papers/$(date +%Y-%m-%d).md
```

### 搜索特定主题
```bash
# 在报告中搜索关键词
grep -r "safety" papers/
```

---

## 📁 项目结构

```
.
├── README.md              # 项目主页（本文件）
├── papers/                # 每日论文报告
│   ├── 2026-04-04.md
│   └── ...
├── daily/                 # 原始数据（JSON）
│   └── 2026-04-04.json
├── reports/               # 生成的报告
├── scripts/               # 自动化脚本
├── config/                # 配置文件
└── analysis/              # 分析规则
```

---

## 🔗 相关链接

- [arXiv 官网](https://arxiv.org/)
- [GitHub 仓库](https://github.com/shuita2333/Arxiv-daily-paper)

---

## 📝 更新日志

| 日期 | 更新内容 |
|------|----------|
| 2026-04-04 | 项目初始化，首份日报生成 |

---

> 🌟 **Star** 本仓库以获取每日最新大模型研究动态！
