# 🧠 大模型相关研究 | 2026年09月24日

> 本类共 **206** 篇论文：已确认 **192** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-206**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-206**

---

### 201. [Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models](https://arxiv.org/abs/2609.25980)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jinmyeong Choi, Jinkwan Jang, Seul Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic time series foundation models (TSFMs) provide coordinate-wise predictive distributions, but these marginals do not determine a joint distribution over multivariate future trajectories. We study training-free coupling of frozen TSFM marginals into multivariate forecast sample paths. Our primary evaluation fixes the empirical marginal sample multiset at every channel--horizon coordinate across methods, isolating the effect of coupling alone. Historical temporal and channel relations substantially improve their corresponding dependence diagnostics. The same pattern persists when the fixed-marginal constraint is removed and paths are sampled directly, and remains present under native multivariate backbone inference. These results support treating dependence reconstruction as a distinct post-processing problem for probabilistic TSFMs.

---


### 202. [Cellular-Communication-Level Interpretability for Pathology Foundation Models via Graph Distillation on Microenvironment](https://arxiv.org/abs/2609.26073)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuxiang Xiao, Zhiwei Chen, Dan Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models (PFMs) provide strong tile-level representations but remain difficult to interpret at the cellular and microenvironmental scales that underpin clinical reasoning. We introduce Graph-Interpreter (G-Interp), a graph-distillation framework that equips a frozen PFM teacher with a cellular-communication-level "plug-in" interpreter, without modifying the teacher. For each tile, we segment cells as graph nodes and construct a microenvironment graph based on spatial adjacency. Graph neural network (GNN) students distil the PFM embedding, whilst learning attention-based message passing that yields node- and edge-level importances. We interpret these importances as cell-cell communication evidence, providing fine-grained explanations of how PFMs encode microenvironmental context. To stabilise distillation when graph abstraction is imperfect, we employ a lightweight auxiliary student to supply complementary visual cues and condition graph message passing, while keeping the primary interpretability signal graph-derived. We evaluate explanation faithfulness by mapping graph-selected evidence back to the image using instance masks and measuring teacher sensitivity under targeted vs non-target occlusions. Across multiple histopathology tasks, G-Interp produces highly scalable, microenvironment-aware explanations, while maintaining competitive predictive performance.

---


### 203. [HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing](https://arxiv.org/abs/2609.26368)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jianyu Wei, Yizhao Gao, Qihao Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon and multi-turn agents typically generate short actions and process long observations from tools and environments. This growing context demands efficient prefill, compact KV-cache storage, and accurate long-context retrieval. To meet these demands, we introduce HySparse2, a hybrid sparse attention architecture with two-level KV sharing. At the outer level, KV Bridging adopts a YOCO-style self-decoder and cross-decoder structure, but bridges only full-attention layers. The self-decoder uses hybrid sliding-window attention (SWA), while the cross-decoder uses hybrid sparse attention. The KV caches for full-attention layers in the cross-decoder are generated from the hidden states of full-attention layers in the self-decoder. At the inner level, HySparse2 retains HySparse's core KV Reuse design with two refinements. First, it replaces block-level sparsity with token-level sparsity for finer long-context retrieval. Second, it removes the separate SWA branch from sparse layers and instead forces a sliding window of recent tokens into the sparse selection. This two-level KV sharing allows all cross-decoder KV caches to be constructed from self-decoder hidden states. Prefill can therefore exit after the self-decoder, skipping all cross-decoder layers. On an 80B-A3B MoE model, HySparse2 outperforms HySparse and Hybrid SWA on long-context retrieval and multi-turn agentic tasks, while substantially reducing prefill computation and KV-cache storage.

---


### 204. [KwaiMind Technical Report](https://arxiv.org/abs/2609.26375)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junlong Wu, Zijun Li, Yuting Hu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Commercial image editing requires product identity preservation, accurate text rendering, and user appeal alongside general editing quality. We present KwaiMind, an image editing system combining general capabilities with e-commerce specialization. An agent-based data engine maintains approximately 1.8 million high-quality editing pairs. Built on a multimodal diffusion transformer, KwaiMind undergoes continued pre-training and supervised fine-tuning, followed by preference optimization and online reinforcement learning. A general-purpose vision-language judge and specialized rewards for click-through rate (CTR), text rendering, and product consistency guide specialized policies, which are consolidated through on-policy distillation. We introduce Ecom-Bench, covering 11 commercial editing tasks with task-specific visual evaluation and CTR-based ranking. KwaiMind achieves the strongest overall scores among evaluated open-source editors on ImgEdit, GEdit, both language splits of REDEdit, and Ecom-Bench visual quality, and the highest aggregate CTR ranking score among compared systems. Offline, CTR-guided optimization increases the proportion of generated images whose predicted CTR exceeds that of the original product image from 12.16% to 37.41%. In an online A/B experiment, CTR-based selection of product main images yields an approximately 2.44% relative increase in actual CTR. These results demonstrate the value of domain-specific data and reward-driven alignment for commercial image editing.

---


### 205. [Vision Foundation Models with Synthetic-Only Training for Monocular Spacecraft Pose Estimation](https://arxiv.org/abs/2609.26561)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** John Church, Vazghen Nikolian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present an improvement on previous spacecraft pose estimation architectures that results in the lowest published mean rotation errors we know of on the SPEED+ lightbox and sunlamp test sets for a known, non-cooperative spacecraft. By using a previously established heatmap-based pose estimation architecture and adapting a large self-supervised ViT foundation model (DINOv3) in place of the smaller convolutional and ViT encoders of previous work, we show that pose estimation accuracy improves from 300M to 840M parameters with no saturation yet observed. We also evaluate our 840M model on a Jetson Orin NX 16GB, measuring single-pass network inference at 133.8 ms per crop with a board draw of 32.0 W. These measurements demonstrate embedded inference feasibility on a processor family with orbital flight heritage. Our resulting model outperforms previous models across lightbox and sunlamp domains while training only on synthetic data. Our best model, using DINOv3 840M adapted with LoRA as the encoder (rank 64, three-seed ensemble with four-rotation test-time augmentation), results in $1.56^\circ$ mean rotation error on sunlamp and $1.17^\circ$ on lightbox, compared to the previous best mean rotation errors we know of on these test sets, $2.66^\circ$ and $1.75^\circ$ by EagerNet.

---


### 206. [Foundation model embeddings capture pre-diagnostic changes on screening mammograms](https://arxiv.org/abs/2609.26605)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kalina P. Slavkova, Eric Brattain, Aditya Gowd 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation model embeddings of screening mammograms may encode pre-diagnostic tissue change without task-specific adaptation. We tested whether embeddings move faster along a data-derived "cancer direction" in women later biopsied for cancer than in matched screen-negative controls, and whether this depends on pretraining domain. We studied 1,773 biopsied women (785 malignant, 988 biopsy-negative) and 1,773 matched controls, each with at least two annual screening exams before their index exam. An identical pipeline was applied to four 2D models: Mammo-CLIP (MC, out-of-distribution mammography), HOPPR (in-distribution mammography), MedImageInsight (MII, general medical imaging), and BiomedCLIP (biomedical vision-language pretraining on literature figures). Breast-level embeddings quantified longitudinal movement along the cancer direction. We compared cases and controls using a between-patient design with complementary mixed-effects analysis, and biopsied versus healthy contralateral breasts within patients. Under matched modality in MII embedding space, malignant cases drifted significantly faster than controls in the first two screening intervals preceding the index exam; biopsy-negative cases showed significance only in the first. MC differences were significant in the first interval for both biopsy groups. Within-patient comparisons showed a broadly similar pattern, with MC significance extending to the second interval in both groups and HOPPR showing significance at interval 1. BiomedCLIP showed no significant differences in either design or biopsy group. Overall, directional embedding velocity emerges as a property of clinically grounded rather than general biomedical pretraining, showing that foundation model embeddings can encode pre-diagnostic mammographic change without task-specific adaptation.

---


> [!TIP]
> 当前位于：**201-206**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-206**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
