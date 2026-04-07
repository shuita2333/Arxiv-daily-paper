# ArXiv Daily Report

## 固定流程

### 一键执行

```bash
bash ~/Documents/arxiv每日阅读/scripts/daily_complete.sh [YYYY-MM-DD]
```

默认流程：
1. 抓取 arXiv 论文
2. 相关性分类
3. 生成 Markdown 日报
4. 上传日报到 GitHub 仓库 `shuita2333/Arxiv-daily-paper`

## 当前规则

### 抓取规则

只抓取：
- **New submissions**

不抓取：
- Cross submissions
- Replacement submissions

### 分类策略

当前采用：
- **纯规则打分 + 降级分类补位**

规则负责：
- 给每篇论文做 1 / 2 / 4 三类竞争打分
- 直接判定明显样本
- 对边界样本做降级归类

降级补位规则：
- 1 / 2 中间态 → 归为 2
- 2 / 4 中间态 → 归为 3

当前不再调用 GLM 参与分类。

### 分类标签

| 等级 | 名称 | 说明 |
|------|------|------|
| 1 | 大模型安全相关研究 | 安全、对齐、鲁棒性、隐私等 |
| 2 | 大模型相关研究 | 能力、架构、训练、优化、agent、multimodal 等 |
| 3 | 中间态相关研究 | 边界样本通过降级补位后的展示类别 |
| 4 | 其他研究（内部） | 内部判断用，不进入最终日报展示 |

### 报告字段

每篇论文保留：
- 标题（带链接）
- 作者
- arXiv所属领域
- 摘要

已删除字段：
- 类型

## 主要文件

```text
~/Documents/arxiv每日阅读/
├── config/
│   └── sources.json
├── daily/
│   └── YYYY-MM-DD.json
├── analysis/
│   └── rules.json
├── papers/
│   └── YYYY-MM-DD.md
└── scripts/
    ├── fetch_papers.py
    ├── analyze_papers.py
    ├── generate_report.py
    ├── git_upload.sh
    └── daily_complete.sh
```

## GitHub 发布

目标仓库：
`https://github.com/shuita2333/Arxiv-daily-paper`

本地仓库：
`~/Documents/arxiv每日阅读`

发布路径：
`papers/YYYY-MM-DD.md`

README 索引格式：
`- [YYYY-MM-DD 日报](papers/YYYY-MM-DD.md)`

上传限制：
- 只允许上传 `papers/` 目录中的日报文件
- 以及根目录 `README.md`
- 其他内容禁止进入在线 Git 仓库

## 已废弃功能

以下发布路径不再属于固定流程：
- 邮件发送
- Notion
- 飞书
- 知乎

## 日报目录

- [2026-04-07 日报](papers/2026-04-07.md)
