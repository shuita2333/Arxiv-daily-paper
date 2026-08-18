# 🧠 大模型相关研究 | 2026年08月19日

> 本类共 **358** 篇论文：已确认 **337** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-358**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-358**

---

### 351. [StreamOPD: A Post-Training Recipe with Spatio-Temporal Cue Gating for Streaming Video Understanding](https://arxiv.org/abs/2608.16320)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Keming Wu, Baoyi Wang, Kaichen Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding demands direct responses from the causally observed prefix of an unfolding video. Existing systems add inference-time memory, retrieval, and compression, yet a training-free sliding-window baseline already matches them. We therefore fix a memory-free recent-window protocol and ask how far post-training alone can go. Reinforcement learning with verifiable rewards fits this regime poorly, encouraging long ``think-then-answer'' generations, while on-policy distillation (OPD) supplies dense token-level teacher supervision on student trajectories but is stable only when both models train in thinking mode. These observations lead to \textsc{StreamOPD}, a recipe combining verifiable streaming-video data, thinking-mode OPD, and instruct-mode deployment. It raises StreamingBench from $77.9\%$ to $83.9\%$---within $0.3$ points of the 9B teacher---and improves OVO-Bench excluding its hallucination-detection subtask (HLD) by $9.1$ points under unchanged inference. As a teacher-privilege extension, \emph{Spatio-Temporal CueGate (ST-CueGate)} aggregates cue-versus-no-cue teacher likelihood ratios into a group-relative response score that reweights OPD. It reaches $71.9\%$ on OVO-Bench (excluding HLD) and $64.9\%$ on Video-MME, and is the only variant that stays above the base model on all four benchmarks. Replacing the teacher with a frozen copy of the student's initial policy---on-policy self-distillation---retains most of these gains and lifts HLD to $57.0\%$, above both the untrained student and the 9B teacher, so abstention loss is not intrinsic to the recipe. We provide a transparent and reproducible reference for open-source streaming-video research.

---


### 352. [Self-Routed Tensor Adapters for Parameter-Efficient Universal Visual Adaptation](https://arxiv.org/abs/2608.16384)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Suraj Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Universal visual representations require adaptation mechanisms that adapt across heterogeneous domains without fragmenting knowledge into domain-specific modules. Parameter-efficient fine-tuning adapts frozen visual foundation models efficiently, but standard low-rank adapters use a fixed subspace for all inputs, which can be restrictive when domains differ in style, background, and semantic context. MoE-based adapters improve specialization through multiple expert pathways, but often rely on external routers and large expert banks, adding parameters and separating routing from adaptation. We propose \textbf{Self-Routed Tensor Adapters}, a compact framework for multi-domain visual adaptation. SRTA projects each input into a low-rank space, computes routing weights from this representation using a learnable domain matrix, and uses these weights to blend slices of a shared Tucker core. This produces a sample-specific adaptation matrix without an external gating network, allowing shared visual factors to be reused while supporting domain-aware specialization. To strengthen pathway learning, we introduce a progressive depth-weighted routing objective that supervises routing decisions across adapter layers. Across five heterogeneous multi-domain visual classification benchmarks, SRTA achieves competitive or slightly stronger average accuracy than MoE-style PEFT baselines while using substantially fewer trainable parameters. At rank 64, SRTA uses 2.77M parameters in the 4-domain setting compared with 9.52M for MoLoRA, and 3.00M in the 6-domain setting compared with 14.31M. Overall, SRTA offers an effective accuracy-parameter trade-off for adapting visual foundation models toward universal multi-domain representations. \href{this https URL}{GitHub}

---


### 353. [ParaTempo: Efficient Parallel Reasoning via Temporal Confidence](https://arxiv.org/abs/2608.16425)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xuteng Zhang, Wenhao Zeng, Xiaodong Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parallel reasoning improves the accuracy and robustness of large reasoning models by exploring multiple solution paths, but its computational cost grows with reasoning depth and branch count. Existing methods for managing these parallel paths typically rely on final-answer consensus, local token confidence, or isolated intermediate probes. However, these signals are often delayed, weakly tied to actual reasoning progress, or too noisy for dynamic, branch-level control. To address these limitations, we introduce ParaTempo, a training-free asynchronous parallel reasoning framework. ParaTempo is driven by temporal confidence, a branch-local measure of answer-space convergence. Each branch is periodically probed for a tentative answer probability distribution, and temporal confidence quantifies how sharply the recent intermediate probes concentrate on a dominant answer. Once sufficient evidence has accumulated, ParaTempo drives its entire control process from this single signal: low-confidence branches are pruned, branches that persistently commit to their dominant answer are retired early, freed computation is reallocated by forking new branches, and generation stops globally once the confidence-weighted vote concentrates. Without requiring synchronization among reasoning trajectories, ParaTempo adaptively allocates computation based on branch-level convergence. Experiments on challenging mathematical and scientific reasoning benchmarks show that ParaTempo reduces average latency by 21.8-32.2% and total token usage by 18.1-30.3% while maintaining competitive accuracy. Moreover, temporal confidence exhibits stronger temporal stability and predictive power for future branch convergence than token-level and instantaneous signals.

---


### 354. [Beyond Accuracy: Assessing Calibration of Geospatial Foundation Models and Their Sensitivity to Distribution Shifts](https://arxiv.org/abs/2608.16614)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nils Lehmann, Jakob Gawlikowski, Burak Ekim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial Foundation Models (GeoFMs) are most commonly ranked and selected by accuracy on standard benchmark conditions via averaged ranks. We show that this protocol is too narrow: the promised deployment in critical EO tasks requires further angles of analysis, mainly calibration, the agreement between a model's confidence and its correctness. Across 16 frozen encoders, four classification and five segmentation datasets, and two orthogonal stress axes, every encoder degrades as corruption intensifies, and the ranking changes as well. Across the four classification benchmarks, EO-pretrained and ImageNet-pretrained encoders are indistinguishable on clean accuracy and clean calibration, and EO pretraining provides no more stability under shift than ImageNet pretraining. Under shift the GeoFMs drift further into overconfidence than the ImageNet-pretrained encoders, at every grade and in every corruption family. A centered kernel alignment (CKA) analysis ties this to representational rigidity: EO-pretrained embeddings move less under corruption while losing just as much task information and remaining overconfident. We apply three commonly explored uncertainty quantification methods and find that temperature scaling and deep ensembles cannot counteract the degradation, while a Gaussian-process probe roughly halves ECE under severe cloud only by tripling it on clean data. In selective prediction experiments, we find that confidence-based abstention cannot defer around confidently wrong predictions, and advocate that benchmark rankings and evaluations should therefore operate across a multitude of conditions and metrics to more holistically evaluate model development progress and close the gap to real world deployment scenarios.

---


### 355. [The Ethical Decision Head: Operationalizing Normative Ethics in Autonomous Vehicles via Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2608.16710)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Thomas Mbrice, Ammar Ali, Sami Mian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As autonomous vehicles (AVs) approach Level 4 and Level 5 operational capability [SAE International, 2018], their on- board decision systems must handle not only safety-critical locomotion but also their subsequent moral weight. This paper details the Ethical Decision Head (EDH), a deep re- inforcement learning (RL) framework that encodes ethical reasoning as a differentiable reward signal, enabling a pol- icy gradient agent to learn morally-aligned driving behavior in scenarios whose state representation is aligned with the CARLA simulation environment [Dosovitskiy et al., 2017]. Two normative frameworks are instantiated and evaluated: a Utilitarian framework minimizing total casualties and a Kan- tian framework enforcing course maintenance as a categori- cal imperative. The EDH is trained via Proximal Policy Op- timization (PPO) [Schulman et al., 2017] against a Bradley- Terry reward model [Bradley and Terry, 1952] learned from pairwise human preference annotations over 200 collision- imminent scenarios. Results reveal an asymmetry in the learnability of normative ethical frameworks under human su- pervision. The Kantian condition, which reduces to a con- stant prediction task under the codebook, serves as a pipeline control: it confirms training stability and rules out infrastruc- ture failure as an explanation for the utilitarian result. The Utilitarian agent learned something more unsettling: human raters rewarded self-sacrifice over casualty minimization, and the model learned that preference faithfully. This divergence between what humans prescribe in theory and what they re- ward in practice suggests that RLHF does not learn ethics as philosophers define it, but as humans live it.

---


### 356. [CytoFormer: A Molecularly Supervised Cell Foundation Model for Histopathology Cell Classification](https://arxiv.org/abs/2608.16718)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jialu Yao, Songhao Li, Alina Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identifying cell types directly from routine haematoxylin and eosin (H&E) histology would enable single-cell analysis at scale, but training such models has relied on manual pathologist annotations, which are slow, expensive and unreliable for many cell types. We instead supervise morphology with molecules. Imaging-based spatial transcriptomics profiles individual cells in situ on a section that can afterwards be stained with H&E, so that molecular identity and morphology are observed for the same physical cell. We assembled 81 such paired Xenium sections spanning 16 organs, derived per-cell labels by clustering, marker-gene annotation, organ-wise human review and quality control, and mapped them onto the cell types commonly reported in each organ. This yielded 15.4 million cells, each with a paired H&E image patch and one of 23 cell types, on which we trained CytoFormer, a cell foundation model with a multi-task, per-organ classification head. On spatially held-out tissue CytoFormer reached an accuracy of 0.85 and a macro-F1 of 0.78 across all 16 organs, and its predictions reproduced the tissue architecture of an entire held-out section. The representation also transfers: with the encoder frozen, a linear head on CytoFormer features performed better than six pathology foundation models on four expert-annotated benchmarks, including on organs and cell types that were not part of pretraining. Finally, in an interactive active-learning setting, CytoFormer's embeddings are markedly more label-efficient than existing pathology foundation models, detecting normal epithelium amid look-alike tumour with an F1 of 0.82 from only a few annotations and leading the strongest baseline by 0.13 in F1. CytoFormer turns paired H&E and spatial transcriptomics into a reusable, label-efficient representation for cell-level analysis of routine histology.

---


### 357. [VicEdit: Learning to Edit Videos from Visual In-Context Examples](https://arxiv.org/abs/2608.16745)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuji Wang, Teng Hu, Yuheng Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite progress in instruction-based video editing, unimodal textual instructions inherently struggle to convey fine-grained textures and complex dynamics. To bridge this perceptual gap, we propose Visual In-context Editing, a new paradigm elevating video editing from textual instructions to multi-modal visual guidance encompassing single image, image pair, and video pair. To facilitate this paradigm, we curate VicEdit-400K, the first large-scale dataset for visual in-context video editing. We develop an automated pipeline to generate 400K high-quality samples across ten task types, ensuring superior visual fidelity and semantic consistency through multi-dimensional filtering. Leveraging this foundation, we introduce VicEdit, a unified framework to bridge visual and textual contexts. To adaptively extract editing semantics from heterogeneous references, we design Modality-Adaptive Semantic Distillation, which produces modality-specific semantic tokens from visual references. These tokens are then synergistically integrated with textual instructions through Dual-Context Injection, enabling the generation process to benefit from both visual and textual signals. Extensive evaluations on VicEditBench demonstrate that VicEdit achieves state-of-the-art performance across both basic instruction editing and visual in-context editing tasks, establishing visual in-context learning as a powerful and controllable paradigm for video editing.

---


### 358. [Model Hypnosis: Strong control of AI via additive subliminal effects](https://arxiv.org/abs/2608.16834)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Enric Boix-Adsera, Benedict Tessler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We demonstrate that AI models are broadly susceptible to a phenomenon we call model hypnosis, in which individually weak and seemingly irrelevant cues in the prompt can be systematically combined to strongly control model behavior. Model hypnosis occurs across model families and scales, including in frontier reasoning models, and hypnotic prompts can transfer between models. Because the model is controlled by inconspicuous textual choices, such as paraphrases and typos, model hypnosis presents new challenges and avenues for AI safety, and is a major hurdle for AI interpretability.

---


> [!TIP]
> 当前位于：**351-358**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-358**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
