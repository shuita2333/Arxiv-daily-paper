# 📦 其他研究 | 2026年08月14日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-202**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-202**

---

### 201. [Redistribution-based Cost Inference Improves Sparse Safe Offline RL](https://arxiv.org/abs/2608.12306)

**<font color=#1a73e8>作者：</font>** Ebenezer Gelo, Geraud Nangue Tasse, Steven James 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe offline RL typically assumes access to dense per-step cost annotations, but in practice supervisors provide only trajectory-level stop-feedback: a binary signal at the first unsafe transition, with no per-step attribution. We frame this as a temporal credit assignment problem and propose the Redistribution-based Cost Inference (RCI) framework, which converts sparse stop-feedback into dense per-step costs via return decomposition, then trains a constrained offline policy on the augmented dataset. We show that return-equivalent redistribution preserves the feasible policy set and the optimal Lagrangian in a CMDP, establishing that the transformation is lossless in theory while yielding better-conditioned cost critic learning in practice. Experiments on highway driving and robotic manipulation demonstrate substantially lower violation rates than sparse and classifier-based baselines, with robustness to heterogeneous dataset compositions and label noise.

---


### 202. [AVA-Encoder: Towards Agent-Native Video Representation Learning](https://arxiv.org/abs/2608.12313)

**<font color=#1a73e8>作者：</font>** Chuyue Li, Jinpeng Yu, Haozhe Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creative agents still lack an effective way to learn from high-quality human films, limiting their ability to produce cinematic-grade videos. A key challenge is the absence of a structured video representation that is both faithful to film content and directly usable for agentic reasoning and manipulation. To address the challenge, we propose the Agentic Video Auto-Encoder (AVA-Encoder), a framework for learning agent-native video representations via agentic auto-encoding.
AVA-Encoder transforms a video into a knowledge graph (KG) representation and then reconstructs it back into video. Its hierarchy and state nodes store structured text, while a linked asset layer holds generated images, audio, and video. Typed edges preserve the relations between these text descriptions and assets in a form that agents can easily understand, query, and edit. The video reconstruction differences drive a textual-gradient optimization framework, which expresses evaluation feedback as natural-language update directions for Data-Independent Encoding Policy Pseudo-Training in the outer loop and optional Data-Dependent KG Representation Refinement in the test-time inner loop.
Extensive experiments show that AVA-Encoder improves by 20.7 percentage points over the strongest external baseline. In the controlled policy-only setting, its pseudo-trained shot-level Agentic Video Encoder policy also outperforms a carefully human-tuned policy while using 74.3% fewer system-prompt tokens. We release the complete AVA-Encoder framework, a reliable agentic video reconstruction benchmark, and the first dataset of high-quality film KG representations.

---


> [!TIP]
> 当前位于：**201-202**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-202**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
