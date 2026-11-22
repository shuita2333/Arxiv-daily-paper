# 🧠 大模型相关研究 | 2026年11月22日

> 本类共 **265** 篇论文：已确认 **245** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-265**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-265**

---

### 251. [LingSante MedGuard Technical Report](https://arxiv.org/abs/2611.25509)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** LingSante MedGuard Team  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As medical AI is increasingly used for patient consultation and clinical decision support, identifying harmful, non-compliant, or ethically problematic responses is essential for responsible deployment. Assessing these risks requires checking clinical claims against relevant evidence, verifying calculations, and applying medical requirements under their intended conditions. We introduce LingSante MedGuard, a capability-enhanced guardrail that integrates supervision from a medical guardrail teacher model and six specialized medical capability experts into a unified model. The guardrail teacher supervises risk decisions and explanations across medical safety, compliance, and ethics, while the capability experts support medical rule understanding, numerical reasoning, multimodal hallucination detection, agentic safety verification, risk localization, and multimodal entity understanding. We consolidate these sources of supervision through offline supervised fine-tuning on teacher-generated demonstrations, followed by multi-teacher on-policy distillation using feedback on student-generated responses. We further introduce LingSante MedGuardBench, a benchmark comprising 11 risk-detection subsets spanning medical safety, compliance, and ethics. At 4B, 9B, and 27B scales, LingSante MedGuard achieves mean benchmark F1 scores of 82.3%, 82.4%, and 87.4%, respectively. The 4B model also achieves 73.9% mean accuracy across MedHallu and MedHALT-NOTA under retrieval-enabled evaluation. Additional evaluations of the verification components show improvements in evidence-supported consistency, source traceability, and rule-guided rationale quality across model scales. These results support the integration of specialized medical capabilities into a unified guardrail for medical risk assessment and evidence-based medical safety verification.

---


### 252. [Don't Lose the Future: Latent-Aware 4-Bit Quantization of World Action Models](https://arxiv.org/abs/2611.25614)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yichen Guo, Yanlong Chen, Xinyue Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) predict how a scene will evolve and condition their actions on this predicted future. Deploying them on a robot's onboard computer calls for 4-bit weights, activations and key-value caches (W4A4KV4). Existing 4-bit quantizers for WAMs preserve the generated action, and estimate sensitivity one denoising step at a time. However, they fail to preserve the fidelity of the predicted future: once the action pathway is protected, the remaining action error enters mostly through a degraded future that none of them deliberately protects. We propose LAQ, a latent-aware quantization framework that preserves the predicted future where it is written, stored and read. Specifically, we introduce a reader metric, which measures future error by its effect on the action, and a read count, which weights each rounding error by the number of denoising steps that read it. Together they give the allocation of precision over activations and caches a closed-form solution. We further develop gaze-guided refinement, which gives the tokens the action attends to a second 4-bit pass in the denoising loop and in the cache. All weights stay at 4 bits, with no high-precision branch and no per-task recalibration. On the LIBERO-Plus benchmark, LAQ reaches 76.4% and 83.3% average success on Fast-WAM and Cosmos-Policy, within 1.2 percentage points of the 16-bit models and all above the baselines with 16-bit KV caches. It compresses the model by 3.8x, reduces the peak GPU memory of the whole policy by 2.3x, and runs 1.66x faster than the 16-bit model. On a real AgileX PiPER arm, it reaches 47.0% average success over three tasks, against 52.0% for the 16-bit model and 30.0% higher than QuaRot.

---


### 253. [Erasing the Wrong Thing: Conditional Attribute Leakage and Concept Erasure in Shared Foundation-Model Embeddings](https://arxiv.org/abs/2611.25640)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haijun He, Fei Li, Donghong Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Medical-image embeddings are increasingly shared in place of raw images for authorized downstream tasks, yet they may reveal sensitive attributes. Standard concept-erasure methods target population-level guardedness. However, we prove that, when binary task and sensitive labels are associated, global and task-conditional linear guardedness cannot both hold while a nonzero linear task signal is preserved, so global erasure must either eliminate that signal or retain task-conditional linear leakage. We further show how global erasure affects linear readers' discrimination between positive and negative samples with different sensitive attributes, deriving an approximate closed-form prediction of its utility cost from pre-erasure statistics. Motivated by this conflict, we introduce Task-Conditional LEACE (TC-LEACE), a closed-form variant of LEACE that enforces linear guardedness within each task stratum of its fitting data. We evaluate four vision foundation models on 85 CelebA attribute pairs spanning a broad range of associations. After LEACE, conditional leakage persists across all four encoders, the discrepancy between marginal and conditional audits increases with association strength, and predicted utility costs track observed losses. We then examine hospital chest radiographs using three foundation models, including two biomedical models, in which chest-tube status is strongly associated with diagnosis. Although a marginal attack on LEACE-erased embeddings underperforms a diagnosis-only reference, chest-tube status remains detectable within diagnosis strata. TC-LEACE recovers most of LEACE's linear task-utility loss while keeping task-conditional leakage within a prespecified margin of LEACE's.

---


### 254. [MatVerse: A Foundation Model for Materials Science](https://arxiv.org/abs/2611.25651)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xuanyu Zhu, Qian Tan, Bo Chen 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Materials science involves highly heterogeneous scientific information, including textual knowledge, molecular and crystal structures, experimental characterization data, microscopy images, and structure-property relationships. Developing a general-purpose foundation model capable of understanding and reasoning over these diverse materials representations remains challenging. In this technical report, we introduce MatVerse, a materials foundation model built upon Intern-S2-Preview and further specialized through large-scale materials-domain post-training. We construct a large-scale multimodal training corpus covering materials knowledge, scientific reasoning, quantitative problem solving, structural understanding, and multimodal scientific interpretation. To improve domain adaptation, we develop a unified data construction pipeline combining teacher-guided reasoning distillation, scientific problem synthesis, consistency-based filtering, and retrieval-based multimodal data construction. We evaluate MatVerse on three representative materials-science benchmarks: our human-calibrated OmniMatBench, MatSciBench, and MaCBench. Results demonstrate consistent improvements after materials-specific post-training over the base model on all three benchmarks, alongside improved inference efficiency on calculation-intensive problems. These results show that targeted domain-specific post-training can effectively enhance scientific reasoning, materials knowledge understanding, and multimodal scientific capabilities of foundation models. MatVerse provides a unified language-and-vision interface for materials science and serves as a foundation for future AI-assisted materials research workflows.

---


### 255. [CGM: Chaos-Guided Graph Attention and Expert Routing for Autism Stereotypy Detection](https://arxiv.org/abs/2611.25730)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hafsa Aslam, Yue Li, Saba Aslam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton graph attention for autism video analysis weights joints by content alone, giving an erratic wrist the same standing as a still one. Stereotypy, however, is defined by how unpredictably movement unfolds rather than how much of it occurs: in our cohort, every amplitude-based kinematic descriptor falls in stereotyped clips, while windowed Sample Entropy of angular velocity alone rises (Hedges' g = +1.05). We compute this irregularity as a per-joint, per-frame tensor that structurally drives computation. The proposed chaos-guided graph attention and mixture-of-experts model (CGM) couples two mechanisms. First, a learned pairwise term added to the graph-attention logit concentrates attention on irregular joints and re-ranks the remaining edge weight toward jointly irregular pairs; its unconstrained coefficient neither vanishes nor inverts, and zeroing the tensor realigns attention in 94% of clips. Second, a gate conditioned on the same signal routes each frame to two of four experts, whose weights track frame-level irregularity. Under subject-grouped five-fold cross-validation on 116 clips, CGM reaches 0.930 balanced accuracy, exceeding the graph-attention baseline by +0.187; the component ordering replicates on the public MMASD dataset, and on held-out Panoptic Studio sessions, CGM keeps 0.86 specificity without retraining, against at most 0.35 for chaos-free baselines. In ablation, routing without irregularity yields no reliable gain, whereas chaos modulation alone contributes +0.132. A severity index from the same tensor reaches 0.87 split-half reliability, separates the cohorts with Hedges' g = +1.08, and stays consistent within children across therapy recordings, supporting video-only monitoring of stereotypy during intervention.

---


### 256. [AdaptReg: Skip-level FiLM Adapter for Task-Specific Adaptation of a Frozen Registration Foundation Model](https://arxiv.org/abs/2611.25761)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shuyue Shi, Rong Yuan, Lin Tian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Longitudinal PSMA-PET/CT registration is a key step in assessing treatment response in prostate cancer, and it requires more than generic alignment accuracy: the deformation must preserve lesion volume, so that measured changes in metabolic tumor volume (MTV) and total lesion glycolysis (TLG) reflect treatment response rather than registration artifacts. We propose AdaptReg, which adapts a frozen registration foundation model to such task-specific requirements through a lightweight trainable adapter branch with identity-preserving initialization. Keeping uniGradICON fully frozen, we apply FiLM-style per-voxel affine modulation ($\gamma$, $\beta$) to its decoder skip connections; the modulation is generated from anatomical semantic features of a frozen TotalSegmentator encoder and supervised by a lesion volume-preservation loss. On the official Codabench validation set (20 pairs), AdaptReg achieves DSC 0.7585, HD95 6.33 mm, MTV/TLG errors of 1.68%/2.11%, and 0.0022% non-diffeomorphic voxels, improving on the uniGradICON + instance optimization baseline by $+0.05$ DSC and reducing the MTV/TLG errors by 70.9%/67.7%. On the hidden official test set (160 pairs), AdaptReg achieves CT DSC 0.816, PET DSC 0.598, and MTV/TLG errors of 4.02%/3.46%, ranking fourth among 16 teams in the final PSMAReg evaluation. Code: this https URL

---


### 257. [System-One RSI: Building Muscle Memory for Interactive Agents through Guided Practice](https://arxiv.org/abs/2611.26007)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qingxu Fu, Xuanfa Jin, Ziqian Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning models provide strong multimodal task understanding but struggle with sub-second control because deliberation increases decision latency. Fast decision models can meet the response window, yet prompting and few-shot examples do not readily provide the fine-grained experience required by a new task. Inspired by coached motor learning, this paper presents System-One Recursive Self-Improvement (System-One RSI), which couples two loops. The high-frequency online inner loop is an Observe, Orient, Decide, Act (OODA) cycle: a decision model maps each visual observation and task question to structured judgments, and a decision tree converts them into timed actions without invoking a reasoning model. The offline outer loop is a recursive improvement cycle carried out by a team of reasoning agents. The team revises the decision-model prompt and decision tree, captures interaction records, derives supervision from those records, and trains or deploys updated model parameters. The improved system then returns to the environment and generates the experience for the next round, consolidating learned distinctions as external muscle memory. The framework operates with a small number of real episodes, without expert demonstrations, environment modification, sandboxing, or parallel simulation. Experiments in Snake, Zenless Zone Zero, and Black Myth: Wukong use a 27B decision model. Mean Snake score increases from 1.30 to 7.35. In an evaluated scenario of Zenless Zone Zero, median completion time decreases by 8.4%. In an evaluated combat scenario of Black Myth: Wukong, the evasive policy achieves 11 times the mean survival time of a stationary reference, while the offensive policy win rate rises from 0% to 66.7% across the evaluated configurations.

---


### 258. [When Foundation Models Disagree: Representational Heterogeneity for Calibrated Uncertainty in Whole-Slide Image Classification](https://arxiv.org/abs/2611.26159)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yekai Shen, Yuqian Wang, Zishun Liao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models supply strong representations for whole-slide image classification, yet the confidence attached to their predictions remains hard to trust. Prevailing uncertainty estimators act within a single feature space and thereby overlook the uncertainty that the choice of foundation-model representation itself induces. This work introduces CALIFUSE, a calibration-oriented framework that fuses several pathology foundation models for the specific purpose of uncertainty estimation. Departing from accuracy-driven fusion, CALIFUSE reads representational heterogeneity across encoders as an explicit confidence cue. Slide-level decision consensus is coupled with chunk-level evidence agreement quantified through Jensen-Shannon divergence, so that both prediction stability and fine-grained evidence consistency inform the estimate. Foundation-model encoders stay frozen. A task-specific nnMIL classifier is still trained for each FM; CALIFUSE then estimates confidence at inference without training an extra fusion module. Evaluated on seven WSI classification tasks under several foundation-model combinations, the framework sharpens calibration, misclassification detection, and selective prediction relative to both the strongest single-encoder baseline and naive ensemble averaging, all while preserving competitive balanced accuracy.

---


### 259. [Physics-Informed Feature Representations and Pretrained Tabular Foundation Models for Generalizable Melt Pool Geometry Prediction](https://arxiv.org/abs/2611.26235)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rafid Enayet, Imtiaz Ahmed, Md Habibor Rahman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developing generalizable, data-efficient machine learning (ML) models for advanced manufacturing remains challenging because experimental datasets are limited and process-property relationships vary across materials and operating conditions. In laser powder bed fusion (LPBF), melt pool width, depth, and melting mode (conduction, transition, or keyhole) govern process stability and defect formation. Conventional ML models typically use dimensional process parameters, which represent laser-material interactions only implicitly and may limit cross-material transfer. This study evaluates whether two physics-informed dimensionless features, normalized enthalpy and Peclet number, combining laser processing conditions with material thermophysical properties, improve melt pool prediction over raw process parameters. We systematically benchmark seven models: four classical ML methods (Gaussian process, support vector machine, random forest, and XGBoost) and three pretrained tabular foundation models (TabPFN, TabDPT, and TabICLv2). Experiments span 316L stainless steel, IN625, IN718, and combined-material datasets, covering regression of melt pool width and depth and classification of melting modes. Dimensionless features yield comparable or superior predictive performance in most settings, with the largest gains in cross-material depth prediction (R^2 = 0.96). Tabular foundation models generally achieve stronger classification performance than classical baselines, particularly for multi-material datasets. These findings indicate that combining physically meaningful dimensionless representations with pretrained tabular models can improve data-efficient melt pool modeling and support more transferable process-window identification in LPBF.

---


### 260. [Actor-Predictor Architecture for Reinforcement Learning with Formal Specification Objectives](https://arxiv.org/abs/2611.26313)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Josef Brozovich, Qining Zhang, Lei Ying  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> One fundamental challenge in reinforcement learning (RL) is enforcing temporal safety constraints, such as satisfying formal specifications. Existing methods often transform logic formulas into automata for state augmentation and reward shaping. However, this approach assumes that automaton construction is both feasible and tractable, which limits its applicability to small specifications and linear temporal logic (LTL). This paper proposes Actor-Predictor, a framework that learns a surrogate representation of logic progress without explicitly constructing an automaton. The predictor continuously estimates whether a partial trajectory will satisfy the formal specification in a later step, and its learned features are provided as auxiliary inputs to the actor, which is then optimized using GRPO and RWR. We show theoretically that, under sufficient predictive accuracy, the learned representation is equivalent to the automaton state. Experiments on grid world and robotic tasks in Isaac Lab demonstrate that Actor-Predictor outperforms automaton-based baselines on LTL-constrained tasks. It also performs well on non-regular formal specifications, such as $(a^n b^n)$, for which finite-automaton-based approaches are not applicable.

---


### 261. [C-LiTE: A Lightweight Foundation Model for Cellular feature learning in Histopathology](https://arxiv.org/abs/2611.26316)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Esha Sadia Nasir, Jiaqi Lv, Gozde N. Gunesli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Characterising individual cells is fundamental to computational pathology, as cellular morphology informs tasks such as tumour grading, mitotic assessment and immune profiling. However, most pathology foundation models are trained on tissue patches and capture cellular features only implicitly, while existing cell-level models are either restricted to specific cell populations or rely on computationally expensive architectures with hundreds of millions of parameters. Applying ViTs directly to small cellular crops also presents an architectural challenge: upsampling increases computational cost without adding morphological information and may introduce interpolation artefacts. To address these limitations, we introduce C-LiTE, a lightweight foundation model for cellular representation learning in H&E-stained histopathology, with only 22 million parameters. C-LiTE employs a native-resolution tokenisation strategy tailored to cellular inputs, processing 64 x 64 px cell-centred crops using a 4 x 4 patch embedding to produce a 16 x 16 token grid without image upsampling. To transfer visual knowledge from large-scale pre-training, we adapt the patch embedding weights of a pre-trained ViT-5-S using a pseudoinverse-based transformation, enabling weight initialisation at the finer patch resolution. We further assemble a pre-training dataset of 60 million cell-centred crops from TCGA, balanced across 19 cancer types and 16 tissue types. To our knowledge, this represents the largest public dataset for self-supervised pre-training on H&E images at the cellular level. We evaluate C-LiTE on seven public datasets spanning mitotic figure recognition, nucleus and cell-type classification, and immune cell phenotyping. Under frozen-feature evaluation, C-LiTE achieves a mean macro-F1 of 0.670, approaching CytoFormer (0.682) with approximately 30x fewer parameters.

---


### 262. [Beam Model Technical Report](https://arxiv.org/abs/2611.26358)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Reflection Team, Adam Abdulhamid, Osama Abuelsorour 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Beam is a sparse Mixture-of-Experts (MoE) model with 501.3B total parameters and 23.4B active parameters, specifically built and optimized for coding, reasoning, and agentic workloads. Beam delivers frontier level reasoning, while requiring 3-4x less inference compute than many models of its class. Pretrained on 23.8T diverse, curated, high-quality tokens, Beam features a 1M-token context window achieved through a novel two-stage midtraining phase, built on verifiable, correctness-anchored data. Post-training leveraged a large-scale, fully asynchronous reinforcement learning (RL) campaign across 10.5K GB300 GPUs, generating over 100M rollouts over 4 weeks of training. We believe this is one of the largest scale RL runs conducted by any open lab to date. Across our evaluation suite, capabilities continued to improve as we increased RL compute, with no sign of a plateau. Supported by deep hardware-model co-design, FP8/NVFP4 quantization, and a 1.93B-parameter speculative decoding drafter (DFlash 2), Beam maximizes serving throughput with efficient, flexible deployment. Averaged across conversation turns and harm categories, Beam refuses or pivots on 88.9% of harmful requests while complying with 81.5% of harmless requests, achieving the highest refusal/pivot rate on harmful requests among open-weight models on the Pareto frontier.

---


### 263. [AURA: AUdio-dRiven streaming Avatar](https://arxiv.org/abs/2611.26540)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nathaniel Cohen, Nicolas Dufour, Amélie Royer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current audio-driven video diffusion models can synthesize realistic talking-head videos but generally require dozens of diffusion denoising steps over multi-second video chunks, making them unsuitable for streaming applications such as voice assistants and virtual avatars, where low-latency and online causal generation are required properties. AURA generates video chunk by chunk with a rolling KV cache, requiring only the audio of the current chunk to start generating, rather than a multi-second audio look-ahead like bidirectional models. It comes in two sizes: AURA 1.3B streams 576p video in real time on a single GPU (20.7 fps for a 16 Hz playback rate), making it suited to interactive avatar applications, and AURA 5B streams 720p video at 9.7 fps. Our two-stage distillation pipeline first aligns the causal student with the teacher, by training it to match the teacher's trajectories with fewer diffusion steps and a chunk-wise sliding window causal attention mask, then applies Distribution Matching Distillation (DMD) with backward simulation to close the remaining quality gap. On standard talking-head benchmarks, AURA 1.3B runs 23x faster than its own bidirectional teacher and reaches a quality comparable to TalkVerse at a lower resolution, and AURA 5B matches its TalkVerse teacher at 720p while running 17x faster. To support reproducibility and further research on streaming avatar generation, we release the weights of both models along with a dataset of 30K synthetic videos and their precomputed teacher trajectories.

---


### 264. [Multi-institutional grading of Barrett's esophagus dysplasia without stain normalization using a pathology foundation model and multiple instance learning](https://arxiv.org/abs/2611.26562)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Amirali Khosravi, Jaidip M. Jagtap, D. Chamil Codipilly 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Barrett's esophagus dysplasia grading suffers substantial inter-observer variability, particularly for low-grade dysplasia, complicating clinical decision-making. We conducted a retrospective multi-institutional diagnostic accuracy study of a foundation model-based deep learning system for dysplasia grading, using 969 H\&E-stained whole slide images from four institutions. Patch-level classifiers trained on expert annotations identified diagnostically relevant regions, followed by attribute-aware multiple instance learning for slide-level classification as non-dysplastic Barrett's esophagus (NDBE), low-grade dysplasia, or high-grade dysplasia. On a held-out test set (n = 130), macro-averaged AUC was 0.96 (95\% CI 0.93--0.98). For binary dysplasia detection, sensitivity was 98\% (80/82) and specificity 81\% (39/48), with a negative likelihood ratio of 0.030 and quadratic-weighted \kap{} of 0.83 against expert consensus. No high-grade dysplasia case was misclassified as NDBE. Performance was consistent across institutions without stain normalization, indicating that stain-robust foundation-model representations may remove the site-specific preprocessing that has constrained prior systems to institution-specific deployment.

---


### 265. [ScaleWorld: High-Resolution World Generation through Shared Prediction and Refinement](https://arxiv.org/abs/2611.26615)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yansong Qu, Wesker Zheng, Quanjian Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution generation enables video world models to render fine-grained scene structures and textures, but directly generating high-resolution video incurs substantial computational and memory costs. We present ScaleWorld, a causal video model that unifies low-resolution world prediction and high-resolution refinement within a single shared backbone. By refining its own predictions, ScaleWorld produces high-resolution world videos without requiring a separate refinement model. For each video chunk, the shared backbone first completes a low-resolution prediction and then performs one-step high-resolution refinement conditioned on that prediction. To support efficient streaming generation, we maintain separate causal states with a long low-resolution history for prediction and a short high-resolution history for refinement. To address task interference during distillation, we separate specialist optimization from capability consolidation and introduce task-asymmetric on-policy distillation (TA-OPD). This procedure transfers prediction and refinement behaviors from specialized teachers into a shared student through local velocity matching under their respective sampling and history policies. {Extensive experiments demonstrate that ScaleWorld achieves high-quality world generation with improved computational and memory efficiency.

---


> [!TIP]
> 当前位于：**251-265**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-265**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
