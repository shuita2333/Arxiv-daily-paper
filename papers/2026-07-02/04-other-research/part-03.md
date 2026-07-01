# 📦 其他研究 | 2026年07月02日

> 本类共 **274** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-274](./part-06.md)

---

### 101. [PPT-Eval: A Benchmark for Computer-Use Agents on PowerPoint Tasks](https://arxiv.org/abs/2606.31154)

**<font color=#1a73e8>作者：</font>** Apurva Gandhi, Vishwas Suryanarayanan, Raja Hasnain Anwar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Creating and editing slides is a rich, multimodal activity that is ubiquitous in professional and educational settings, making it an ideal testbed for real-world computer-use agents. Microsoft PowerPoint is among the most widely adopted and feature-rich environments for presentation creation. We introduce PPT-Eval, a benchmark of 120 PowerPoint tasks across 12 files that cover both content creation and presentation editing scenarios, organized by difficulty. A central challenge in this domain is evaluation: tasks are complex, multimodal, and often admit many valid solutions. Moreover, today's agents frequently make only partial progress, which binary success metrics fail to capture. To address this, we design a robust evaluation framework to help create task-specific rubrics for PowerPoint tasks, taking inspiration from and building on past works for rubric-based evaluation. These rubrics award partial credit for intermediate steps, penalize unnecessary changes and poor aesthetics, and provide natural language feedback. This nuanced approach proves highly effective, achieving a Kendall's {\tau}-b correlation of 0.77 with human judgments. We find that existing frontier agents still struggle with solving PowerPoint tasks, with strong models like Claude-4.5-Opus achieving only a 45% success rate and an average partial score of 57%. The benchmark is located at: this https URL.

---


### 102. [Reasoning-aware Speculative Decoding for Efficient Vision-Language-Action Models in Autonomous Driving](https://arxiv.org/abs/2606.31160)

**<font color=#1a73e8>作者：</font>** Anh Dung Dinh, Simon Khan, Flora Salim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Vision-Language-Action (VLA) planners for autonomous driving emit a chain-of-causation (CoC) reasoning step \emph{before} producing a trajectory. The reasoning is autoregressive and dominates inference latency, while the trajectory head is parallel and cheap. Latency is an operational constraint in autonomous driving, so accelerating the reasoning step is the central problem we address. We observe that CoC reasoning has two qualitatively different needs: most tokens continue routine setup that follows naturally from the ego-trajectory history, and a small fraction encode commitments that require fresh visual evidence about an unexpected situation. We split this reasoning into two specialized paths: a \emph{routine reasoner} that handles the predictable continuation by attending to trajectory history, and a \emph{deliberative reasoner} (the unmodified VLA target) that handles novel cases by attending to current visual evidence, using the speculative decoding framework as the architectural template for how the two paths cooperate. Unlike standard speculative decoding, our routine reasoner is not a smaller replica of the target; the two reasoners are deliberately specialized to read different parts of the prompt. We propose two techniques to realize this. First, we introduce \textbf{FlatRoPE}, a 1D rotary positional embedding in the draft that breaks the rotational symmetry of the target's 3D M-RoPE, redirecting attention away from visual tokens and onto trajectory-history tokens. Second, we introduce \textbf{Action-aware RL (AARL)}, a post-training stage that uses an action-quality reward together with a static-reference KL anchor. Together, our two-reasoner system reduces the reasoning-step running time by approximately $4\times$ relative to the original Alpamayo planner.

---


### 103. [Seeing Through the Weights: Privacy Leakage in Scene Coordinate Regression](https://arxiv.org/abs/2606.31164)

**<font color=#1a73e8>作者：</font>** Oleksii Nasypanyi, Jaemin Cho, Utku Ozbulak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene Coordinate Regression (SCR) methods are increasingly adopted for visual localization. In these approaches, the scene is implicitly encoded within a neural network that regresses a 3D world coordinate for each image pixel. Because the scene is represented only through the network parameters and not stored explicitly as images or maps, such methods are often assumed to be privacy-preserving. In this work, we show that this assumption is incorrect in practice.
Specifically, we introduce a query-based attack that reconstructs the 3D geometry of the training environment from an SCR model under different levels of model access. To do so, we repeatedly query the model with batches of proxy images unrelated to the target scene to obtain dense pixel-wise 3D coordinates. Reliable points are identified through their stability under small input perturbations and can be further refined in a white-box setting. These stable points are accumulated across independent query batches to recover the scene geometry. From the recovered 3D representation, we also invert the network features to synthesize images from arbitrary viewpoints, revealing additional appearance information.
Experiments on indoor and outdoor datasets demonstrate that substantial portions of training environments can be reconstructed with high geometric fidelity. Beyond geometry, we also recover an approximate color appearance, which exposes recognizable layout and potentially sensitive scene elements. This directly contradicts claims in the literature that SCR representations are privacy-preserving by design, and reveals a real risk when such systems are deployed in private or security-critical spaces. The project page is available at this https URL.

---


### 104. [Probe Choice Changes Canary-Memorization Verdicts: Three Post-Hoc Disagreement Case Studies in a Text-Dominant LoRA-Tuned Autoregressive Testbed](https://arxiv.org/abs/2606.31168)

**<font color=#1a73e8>作者：</font>** Zhichao Fan, Zexin Zhuang, Yanhang Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We audit a fixed prefix-window mean-NLL memorization probe (K=20) on a Qwen2.5-VL-7B canary testbed and report three post-hoc cases where it disagrees with full-span secret NLL or greedy exact-recall. C3 (false negative, window truncation): damage lands on hex tokens outside K=20; the probe stays flat while hit@1 drops. C4 (false positive, non-secret drift): the probe moves, but approximately 99% sits on non-secret preamble; the secret span and hit@1 are unchanged. C5 (ambiguous in-window drop): the probe falls on an undertrained baseline while full-span hex is positive and hit@1=0. Recommendation: report (i) full-span secret NLL, (ii) a span-localised decomposition, (iii) behavioural exact-recall at k>=4, and (iv) decoy probes before asserting secret-specificity. Evidence is on controlled canaries in one backbone; magnitudes are testbed-specific.

---


### 105. [Cross-Domain Feature Expansion for Tabular Medical Data via Knowledge Graphs Injection](https://arxiv.org/abs/2606.31171)

**<font color=#1a73e8>作者：</font>** Mengying Zhou, Yongjie Yin, Haoyan Xin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Acquiring comprehensive cross-domain biomedical profiles is often costly and time-consuming, resulting in severe data scarcity in medical research. To address this challenge, we propose MedKGTab, a knowledge-injected framework specifically engineered for cross-domain feature expansion in tabular medical data. MedKGTab seeks to infer uncollected biomedical features from available ones by exploiting their inherent statistical dependencies and established medical correlations. By employing a row-column dual-attention mechanism, MedKGTab operates directly on raw structured tabular data, inherently capturing exact numerical distributions without the structural loss caused by tokenization. Crucially, MedKGTab integrates data-driven statistical priors with the SPOKE biomedical knowledge graph, achieving an optimal synergy between the data and knowledge channels. Within this synergy, the representations derived from the data channel are modulated by the injected biomedical knowledge, ensuring the final generated data are grounded in empirical medical research. Experimental results demonstrate that MedKGTab achieves high data fidelity and realistic data representation in cross-domain feature expansion. It outperforms both SOTA medical large models (e.g., Baichuan M3-plus) and specialized tabular models designed for medical data generation. Furthermore, MedKGTab consistently delivers superior performance across various data generation scenarios, whether inferring missing features within the same dataset or generalizing across different medical cohorts.

---


### 106. [HSDF-Lane: Height-Aligned Signed Distance Field with Semantic Lane Prior for 3D Lane Detection](https://arxiv.org/abs/2606.31172)

**<font color=#1a73e8>作者：</font>** Jiyong Boo, Byeongin Joung, Hyemin Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular 3D lane detection plays a critical role in autonomous driving, yet recovering reliable 3D geometry from a single image remains challenging due to inherent depth ambiguity. Prior methods project image features into Bird's-Eye-View (BEV) space under a flat-ground assumption, causing geometric distortion on real-world roads. Recent methods instead predict explicit height maps to capture non-planar surfaces, but still rely on sparse anchor-based regression and exploit the recovered geometry merely for spatial transformation rather than semantic understanding. To overcome these limitations, we propose HSDF-Lane, which implicitly models the road surface as a Height-aligned Signed Distance Field (HSDF) over a densely sampled 3D feature volume. Through differentiable rendering, the HSDF jointly produces an accurate height map and surface-aligned features. We further introduce Lane-aware Semantic Positional Encoding (LSPE), which injects a lane-existence prior derived from the surface-aligned features into the transformer queries, coupling geometric structure with semantic guidance. Extensive experiments on the OpenLane benchmark show that HSDF-Lane achieves state-of-the-art performance in both 3D lane detection and height map estimation.

---


### 107. [ClawArena-Team: Benchmarking Subagent Orchestration and Dynamic Workflows in Language-Model Agents](https://arxiv.org/abs/2606.31174)

**<font color=#1a73e8>作者：</font>** Kaiwen Xiong, Haonian Ji, Shi Qiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production large language-model (LLM) agents are increasingly deployed not as lone problem-solvers but as managers: a main model creates specialized subagents, delegates work, and orchestrates their parallel, asynchronous returns through dynamic workflows. Whether one model can actually run such a team is largely unmeasured: existing benchmarks score a policy's own task-solving or a fixed multi-agent system's emergent behavior, but none isolate the management ability of the single LLM acting as leader. We introduce ClawArena-Team, a benchmark of 41 multi-turn, multimodal, multi-directory scenarios spanning 258 evaluation rounds and 72 staged updates that measures this management ability. The main agent is deliberately constrained: it natively perceives only text and directly accesses only part of the workspace. It commands a fixed, locally served subagent pool, so score differences reflect management skill, not raw capability. All scoring is execution-based with no LLM judge: an overall score -- the Subagent-Management Score (SMS) -- multiplies task correctness by a least-privilege and modality-routing factor. Across twelve proprietary, community-hosted, and self-hosted models, experiments show that the management bottleneck is privilege granting rather than perception (no model exceeds 50% workspace-permission precision); that cost and management quality are decoupled (API cost spans over 100 times while the overall score spans under 4 times, with the cheapest open models on the Pareto frontier); and that most leaderboard scores cluster within a 9.9-point band while orchestration behaviors diverge by more than an order of magnitude. Code and data will be released.

---


### 108. [GaussianMap: Learning Gaussian Representation for Multi-Sensor Online HD Map Construction](https://arxiv.org/abs/2606.31177)

**<font color=#1a73e8>作者：</font>** Hongyu Lyu, Julie Stephany Berrio Perez, Mao Shan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving systems benefit from high-definition (HD) maps that provide critical information about road infrastructure. The online construction of HD maps offers a scalable approach to generate local vectorized maps from onboard sensor observations. Existing methods commonly adopt bird's-eye-view (BEV) features as the intermediate scene representation, encoding the surrounding space with fixed-resolution dense grids. However, map elements are spatially sparse yet require fine-grained geometric localization, making uniformly allocated BEV representations redundant and less effective for vectorized map prediction. In this work, we propose GaussianMap, an online HD map construction framework that learns an adaptive Gaussian representation of the surrounding scene. This representation consists of a set of Gaussian primitives on the BEV plane, each encoding a flexible local region with geometric properties and a feature vector, allowing the model to allocate representational capacity to map-relevant regions. To generate such a representation from sensor observations, we introduce a feed-forward Gaussian encoder that progressively refines these primitives through Gaussian interaction modeling and multi-sensor feature aggregation. The refined Gaussian representation is then splatted into a BEV feature map and decoded into vectorized map predictions. Extensive experiments on nuScenes and Argoverse 2 datasets demonstrate that GaussianMap achieves state-of-the-art performance in both camera-only and camera-LiDAR fusion settings. Our code will be made publicly available.

---


### 109. [AETDICE: Unified Framework and Offline Optimization for Nonlinear Multi-Objective RL](https://arxiv.org/abs/2606.31178)

**<font color=#1a73e8>作者：</font>** Woosung Kim, Youngjun Suh, Jinho Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing nonlinear preferences in multi-objective reinforcement learning (MORL) is essential for capturing complex trade-offs like risk aversion or fairness. However, such non-linearity has historically bifurcated nonlinear MORL objectives into two distinct paradigms: Scalarized Expected Return (SER) and Expected Scalarized Return (ESR). While SER requires global-level optimization and ESR requires non-Markovian policies, leading to fragmented optimization strategies, we bridge this divide through the Aggregation-Expectation-Transformation (AET) framework. By unifying both criteria through a tripartite decomposition of scalarization, AET provides a principled foundation for general nonlinear MORL. Building on this framework, we propose AETDICE, a tractable offline RL algorithm for AET objectives. By utilizing DICE-style density-ratio estimation in an augmented state space, AETDICE enables sample-based optimization from static datasets. Our framework resolves long-standing barriers and captures respective trade-offs induced by AET framework, which existing methods fail to address.

---


### 110. [AI-Assisted Discovery of Convex Relaxations via Dual Agents](https://arxiv.org/abs/2606.31182)

**<font color=#1a73e8>作者：</font>** Sungyoon Kim, Mert Pilanci  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work shows that LLM agents can improve sharp-constant inequalities by searching for extremal constructions, which yield upper bounds. We address the complementary side: a lower bound holds for every admissible function and follows from a convex relaxation of the nonconvex problem, with tighter relaxations giving stronger bounds. We instantiate the autoresearch paradigm to discover such relaxations: a coding agent proposes valid tightening constraints, a theory agent verifies each one and searches for counterexamples, and every reported bound is certified by an explicit dual-feasible point checked in rigorous interval arithmetic. On two optimization constants studied by \citet{tao2025alphaevolve} - the first autocorrelation inequality ($C_{6.2}$) and the Erdős minimum-overlap constant ($C_{6.5}$) - we improve the certified lower bounds from $1.28$ to $1.2937$ and from $0.379005$ to $0.37912$, respectively.

---


### 111. [Transformers as Bayesian In-Context Experimenters: Smoothness-Adaptive Efficient ATE Estimation](https://arxiv.org/abs/2606.31184)

**<font color=#1a73e8>作者：</font>** Jiachun Li, David Simchi-Levi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive experiments for average treatment effects (ATE) require randomized allocations balancing valid inference with statistical efficiency. The oracle design is a covariate-dependent Neyman rule governed by unknown arm-conditional outcome variances. We investigate whether this sequential variance-estimation and allocation process can be amortized via in-context learning. We introduce Bayesian in-context experimenters: transformer policies trained to imitate a Bayesian posterior Neyman teacher. The teacher updates nonparametric beliefs over potential outcomes using experimental history to assign posterior Neyman treatment probabilities. This design converges to the oracle rule, supporting efficient ATE inference. Transformers constructively implement this mapping through attention-based sufficient statistics and projected gradient descent, imitating Bayesian updating for Gaussian-series priors. To address unknown outcome smoothness, we combine smoothness-indexed experimenters using a mixture-of-experts transformer. The gate acts as a hierarchical posterior over smoothness classes, concentrating on near-oracle experts. By bounding the complexity of the transformer class, we prove this amortized policy can be learned via empirical risk minimization using supervised pretraining. Experiments confirm accurate teacher imitation, adaptive allocation, and improved ATE precision over baselines.

---


### 112. [Gated Multi-Graph Fusion via Graph Attention Networks for Alzheimer's Disease Detection](https://arxiv.org/abs/2606.31186)

**<font color=#1a73e8>作者：</font>** Jinyu Li, Xiao Wei, Bin Wen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spontaneous speech is a vital non-invasive biomarker for Alzheimer's Disease (AD), yet many systems overlook non-linear structural disruptions and clinical heterogeneity in pathological language. We propose a Multi-View Gated Graph Attention Network that transcribes audio via Automatic Speech Recognition (ASR) to construct semantic, dependency, and co-occurrence graphs, characterizing speech through a "content-structure-flow" framework. Notably, the co-occurrence graph leverages Pointwise Mutual Information (PMI) from a normative corpus to quantify narrative logic and linguistic deviation. To address symptomatic diversity, an adaptive gated fusion mechanism dynamically integrates these views. Evaluated on the ADReSSo dataset, our model achieves 90.00% accuracy. Ablation results confirm that the PMI-based graph and heterogeneity-aware gating are essential for robust classification across diverse clinical populations. Our source code is publicly available at this https URL.

---


### 113. [ISM:Self-Improving Strategy Memory for Continual Mathematical Reasoning](https://arxiv.org/abs/2606.31191)

**<font color=#1a73e8>作者：</font>** Prakhar Dixit, Tim Oates  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Intelligent Schema Memory (ISM), a self-evolving memory-augmented system that improves mathematical reasoning for a frozen LLM under continual learning with hard episodic resets. ISM maintains a compact, self-refined bank of strategy schemas learned from both successful and failed episodes, with symbolic tools that check intermediate steps and certify this http URL updating model parameters, ISM outperforms passive, retrieval, and reflection baselines on MATH-Hard and OlympiadBench, using 64% and 86% fewer schemas respectively than the strongest passive baseline. These results show that small, actively maintained, and verified strategy memories can support reliable continual mathematical reasoning under strict episodic isolation.

---


### 114. [Distilling Temporal Coherence into 2D Networks for Transrectal Ultrasound Prostate Video Segmentation](https://arxiv.org/abs/2606.31198)

**<font color=#1a73e8>作者：</font>** Dong Yeong Kim, JunGyu Lee, Jaewon Choi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time video segmentation of the prostate in Transrectal Ultrasound (TRUS) is essential for image-guided interventions. While conventional 2D methods suffer from inter-frame inconsistencies by disregarding temporal context, 3D architectures incur prohibitive latency. To resolve this dilemma, we present a Temporally Consistent Learning Framework that distills temporal coherence into a 2D network during training, preserving single-frame inference efficiency. Our design is driven by a key clinical observation: the prostate exhibits geometric stability, whereas the surrounding acoustic environment fluctuates due to physiological motion and transducer pressure. Because conventional temporal constraints propagate erroneous gradients from these unstable regions, we introduce a Confidence-Weighted Temporal Consistency objective derived from optical flow warping residuals, selectively attenuating contributions from unreliable regions. Complementing this pixel-wise constraint, a Dual-scale Prototype Alignment Module enforces semantic coherence through contrastive optimization of local boundary and global semantic features. Furthermore, to eliminate the need for dense per-frame video annotations, we employ geometric equivariance-based pseudo-labeling with knowledge distillation from a pretrained teacher. Extensive experiments on SUN-SEG and our newly introduced TRUS-V benchmark (2,679 frames) demonstrate state-of-the-art accuracy and temporal consistency at real-time speed. Code and dataset are available at this https URL.

---


### 115. [ExPLoRe: Expert Patch-Level Loss Routing for Multi-Objective Masked Image Modeling](https://arxiv.org/abs/2606.31201)

**<font color=#1a73e8>作者：</font>** Konstantinos Georgiou, Maofeng Tang, Hairong Qi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-objective masked image modeling (MIM) combines complementary learning signals (token distillation, CLS alignment, and pixel reconstruction) but existing methods weight these objectives with global scalars, ignoring spatial heterogeneity across patches. We present ExPLoRe (Expert Patch-Level Loss Routing), which repurposes Soft Mixture of Experts (MoE) dispatch weights as learned, per-patch loss coefficients. The key mechanism is loss-coupling: allowing loss gradients to flow through dispatch weights to the router enables content-dependent specialization, where different patches receive different emphases across objectives. A detach ablation confirms loss-coupling as the core mechanism, degrading performance by 1.6% when gradients are blocked. On ImageNet-1K with ViT-Base, ExPLoRe improves over non-MoE baselines on two objective combinations (Token+CLS: +0.5% k-NN, +4.4% linear probe; Token+Pixel: +2.2% k-NN), achieving 80.6% linear probe and 85.3% finetuning accuracy, competitive with published methods. For downstream transfer, we develop adaptation recipes (Freeze Routing, Expert Dropout, and Freeze Attention) that improve MoE finetuning by +1.5% over the vanilla MoE, and close a 2.5--2.9 mIoU segmentation gap so that MoE models match or exceed non-MoE baselines on ADE20K.

---


### 116. [AC3S: Adaptive Conditioning for 3D-Aware Synthetic Data Generation](https://arxiv.org/abs/2606.31204)

**<font color=#1a73e8>作者：</font>** Eric Ji, Qiran Hu, Wufei Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic data generation has emerged as a powerful tool for improving data scalability in computer vision. Recent diffusion-based pipelines have demonstrated strong photorealism. However, how to enforce precise 3D structure and pose consistency in generated images remains challenging. Existing methods leverage visual prompts such as edge maps to guide diffusion models, but often suffer from over-conditioning artifacts that degrade image realism and limit dataset quality. In this paper, we present a diffusion-based image generation framework that enforces 3D structural alignment while preserving photorealism through adaptive conditioning. Our framework, Adaptive Conditioning for 3D-Aware Synthetic Data Generation (AC3S), introduces a self-supervised visual prompt modulator that dynamically adjusts the strength of ControlNet conditioning, preventing over-conditioning and enabling the diffusion model to retain its generative expressiveness. To further enhance diversity and semantic consistency, we develop a multi-agent vision language model framework that composes detailed and 3D-aware prompts aligned with the underlying geometric structure. Together, these components enable the scalable generation of high-quality synthetic datasets with accurate 2D and 3D annotations. Extensive experiments demonstrate that our method significantly improves image quality and downstream utility.

---


### 117. [Towards Inclusive Mobility Modeling: Characterizing and Evaluating Elderly Trajectory Patterns in Urban Systems](https://arxiv.org/abs/2606.31207)

**<font color=#1a73e8>作者：</font>** Zhengxuan Wang, Haohan He, Mengying Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid advance of smart cities increasingly depends on trajectory data mining, yet underrepresented demographic groups, particularly the elderly, are often sparsely represented in public mobility datasets. This underrepresentation can introduce systematic bias into mobility modeling and downstream urban planning. Using the 2016-2020 Jersey City subset of the Citi Bike System Data, this study quantitatively examines how the absence of underrepresented subgroups' mobility signatures affects mobility modeling, using synthetic trajectory generation as a case study. The analysis reveals that elderly riders exhibit a structurally distinct mobility signature, including localized activity spaces (958 m vs. 1,189 m for young riders), lower mobility entropy (1.82 vs. 4.15), and asymmetric off-peak temporal patterns. To demonstrate that relying on majority-dominated training data yields biased synthetic outcomes, we further evaluate both a first-order Markov chain and a Qwen3-4B model fine-tuned with QLoRA across three demographic training settings: the full population, young riders only, and elderly riders only. Results show that models trained on majority-dominated populations systematically misrepresent elderly mobility behavior, particularly for spatial mobility metrics. The Markov model trained on the full population overestimates elderly step length by 4.5% and dwell time by 8.9%, whereas the elderly-specific model achieves substantially lower errors across most metrics. Comparisons between the Markov and LLM-based frameworks further show that higher-capability models do not necessarily improve subgroup-level fidelity under limited demographic data. These findings underscore the importance of demographic representation in mobility modeling and its downstream applications for underrepresented populations.

---


### 118. [CooperScene: Multi-Modal Cooperative Autonomy Benchmark with C-V2X Communication Characterization](https://arxiv.org/abs/2606.31219)

**<font color=#1a73e8>作者：</font>** Bo Wu, Ruoshen Mo, Justin Yue 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cellular vehicle-to-everything (C-V2X) enables cooperative perception, prediction, and planning beyond the field of view of individual agents. However, existing datasets often overlook the complexities of real-world deployment, such as limited communication bandwidth and its dynamics, heterogeneous sensing modalities, and scalability beyond a single cooperative partner. In this paper, we introduce CooperScene, a high-fidelity cooperative autonomy dataset with real-world C-V2X communication characterization. The dataset is organized into diverse scenes, including intersections, highway ramps, and parking lots. These scenes involve three connected and autonomous vehicles (CAVs) and one infrastructure roadside unit (RSU), all equipped with multi-modal sensors and commercial off-the-shelf C-V2X communication radios. All scenes are annotated with globally consistent 3D labels at 10 Hz, totaling 344K objects across 59K frames, underpinned by tight sensor- and agent-synchronization, centimeter-level localization and spatial alignment, precise cross-modality calibration, and 3GPP-standard-compliant C-V2X communication. CooperScene establishes a rigorous benchmark for evaluating multi-agent scaling and actual performance in real-world deployable settings. Project website for data and benchmark: this https URL

---


### 119. [Thinking Before Retrieving: Robust Zero-Shot Composed Image Retrieval via Strategic Planning and Self-Criticism](https://arxiv.org/abs/2606.31222)

**<font color=#1a73e8>作者：</font>** Gunho Jung, Jeong-Woo Park, Seon Bin Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Composed image retrieval requires identifying a target image from a gallery by integrating a reference image with a textual modification instruction. In a training-free zero-shot setting, this task relies on constructing a retrieval-oriented textual query within a frozen vision--language embedding space at inference time. Existing approaches predominantly rely on a single-pass generation strategy that fuses the reference context and modification text into a unified description. This strategy makes it difficult to detect or correct semantic distortions and omissions during generation. Consequently, the preservation of reference attributes and the integration of textual requirements interfere with each other, which degrades retrieval precision. To address these challenges, we introduce PEC-CIR, a training-free framework that structures query construction as a multi-stage reasoning pipeline. The framework operates through a Planner--Executor--Critic architecture where the Planner extracts explicit constraints, the Executor generates multiple candidate target descriptions, and the Critic evaluates these candidates based on constraint compliance. By reframing query construction as a staged inference process instead of a single-pass output, PEC-CIR reduces the propagation of generative errors by explicitly evaluating candidate queries before retrieval, thereby improving retrieval stability.

---


### 120. [ForgeDrive: Bidirectional Cross-Conditioning for Unified Visual-Action Generation in Autonomous Driving](https://arxiv.org/abs/2606.31226)

**<font color=#1a73e8>作者：</font>** Xuchang Zhong, He Zheng, Chenxu Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-model-based autonomous driving endows the model with the ability to understand scene evolution. Yet this promise is undermined by the prevailing imagine-then-act paradigm, which allows errors from the more challenging visual generation stage to cascade into action planning. We introduce ForgeDrive, a unified autoregressive diffusion framework with visual-action cross-conditioning that closes this gap through act-then-imagine paradigm. ForgeDrive factorizes the future as a sequence of per-timestep frame-action pairs, intertwining each action with its corresponding visual observation. During training, we decouple the diffusion timesteps of the two modalities and introduce a UniDiffuser-style noise scheduler to get the ability to infer either modality from its counterpart and deepen understanding of relationships between images and actions. At inference, we propose a novel act-then-imagine inference paradigm, and find that at each step, action generation is a capability internalized during training, requiring no clean future frame as a prerequisite at inference time; instead, the generated action can improve the accuracy of future frame generation, which in turn enhances the quality of the next action. Additionally, we augment each step with future ego-status prediction, further sharpening planning ability. Extensive experiments on NAVSIM demonstrate that ForgeDrive not only unifies driving simulation, planning, and visual odometry into a single model, but also outperforms existing strong planners without any post-training strategy.

---


### 121. [Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming](https://arxiv.org/abs/2606.31227)

**<font color=#1a73e8>作者：</font>** Yong Yang, Xing Zheng, Huiyu Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The fast growth of open-source AI infrastructure, from model serving engines and agent platforms to the Model Context Protocol (MCP) ecosystem and the language models themselves, has outpaced the security tooling available to defend it. We present AI-Infra-Guard, an open-source framework that organizes AI red teaming around a single observation: the attack surface of an AI agent is stratified across layers (infrastructure, protocol/tool, agent behavior, and model), and no single detection paradigm fits all of them. The framework therefore matches a paradigm to each layer, from deterministic rule matching over 75+ AI components and 1{,}400+ vulnerability rules, through LLM-driven agentic auditing of MCP servers and agent-skill packages and multi-turn black-box agent red teaming, to a jailbreak harness with 26+ attack operators over sixteen datasets. To our knowledge it is the only open-source framework to span all of these, including supply-chain auditing of the agent skills that increasingly extend AI agents. We release AI-Infra-Guard as open source so that \emph{layer-paradigm matching} can serve as a practical foundation for agent security and a shared base for the community to build on.

---


### 122. [Learning Gaussian Graphical Models from a Glauber Trajectory Without Mixing](https://arxiv.org/abs/2606.31230)

**<font color=#1a73e8>作者：</font>** Eric Shen, Tony Wu, Mahbod Majid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the task of learning the structure of a $d$-sparse Gaussian graphical model on $n$ variables from a single trajectory of Glauber dynamics. Beyond algorithmic considerations, many applications present temporally correlated observations rather than i.i.d.\ samples. In the classical i.i.d.\ setting, under comparably general sparsity and minimum edge-strength assumptions, sublinear-in-$n$ sample guarantees are known, but achieving them in polynomial-time remains open. Motivated in part by this gap, we give a polynomial-time algorithm that recovers the conditional-independence graph from a single Glauber trajectory, with a trajectory-length guarantee that does not depend on the mixing time.
Technically, our algorithm has three components. First, we estimate the conditional variances and rescale the trajectory to reduce to the unit-diagonal case, without changing the underlying graph. Second, we design a local edge test that extracts adjacency information from short update windows by isolating pairwise influence. Third, we aggregate these local statistics using a robust median-based estimator, and prove accuracy despite temporal dependence arising from a single trajectory.

---


### 123. [UHD-MFF: Shattering Barriers in Multi-Focus Ultra-High-Definition Image Fusion via Learnable Lookup Tables](https://arxiv.org/abs/2606.31242)

**<font color=#1a73e8>作者：</font>** Yibing Zhang, Xunpeng Yi, Qinglong Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the advancement of imaging technology, ultra-high-definition images have become increasingly essential in modern visual applications. However, existing multi-focus image fusion remains largely confined to low-resolution images and faces three major barriers in UHD scenarios, namely data availability, model adaptability, and deployment feasibility, which severely hinder its practical application. To shatter these barriers, first, we propose the UHD-MFF dataset, the first large-scale ultra-high-resolution multi-focus fusion dataset. Second, we propose a scale-specialized lookup-table framework tailored for ultra-high-resolution images, termed as UMF-LUT. It consists of Coarse-Region Lookup Table (C-LUT) and Detail-Edge Lookup Table (D-LUT). Specifically, C-LUT performs joint queries of multiple gradient cues and semantic cues at low-resolution scales to enable region-level decision-making. Also, D-LUT operates at high-resolution scales, leveraging efficient Laplacian cues to provide complementary edge-level decision information. Such a design makes the model particularly well-suited for ultra-high-resolution multi-focus image fusion. Finally, it offers strong deployability with minimal computational overhead, enabling real-time 4K multi-focus fusion and showing promising potential for smartphone. Extensive experiments demonstrate that it outperforms SOTA methods in both visual fidelity and quantitative metrics. It effectively advances the development of multi-focus image fusion toward ultra-high-resolution imaging scenarios. The code is available at this https URL.

---


### 124. [Rethinking the Role of Feature Engineering and Learning Strategies in Few-Shot Hidden Emotion Recognition](https://arxiv.org/abs/2606.31249)

**<font color=#1a73e8>作者：</font>** Xiaochuan Guo, Jihao Gu, Haixu Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we present the solution developed by our team, XInsight Lab, which achieved first place in Track 3 of the 4th EI-MIGA-IJCAI Challenge with a test accuracy of 0.76923. To address the challenge of weak and sparse implicit emotion evidence in long videos, this paper extends the winning solution from the previous competition and proposes a compact multi-modal temporal modeling framework. The framework integrates and evaluates the effects of multi-source features, including 2D/3D skeletons, facial expression Blendshapes, DINOv2/v3 vision foundation models, X-CLIP video features, and Gemini semantic priors. Architecturally, we propose a cross-attention mechanism that utilizes static pose features, denoted as Base, as the Query and dynamic micro-motion differential features, denoted as Offset, as the Key and Value. By capturing local relative velocities, this mechanism eliminates static biases related to individual body shape and identity. Concurrently, an adaptive pooling method based on Multiple Instance Learning is employed to extract instantaneous emotions while suppressing background noise in long sequences. Finally, the paper reveals the representation collapse phenomenon of general vision foundation models in micro-dynamic tasks, and analyzes the underlying mechanisms where networks fall into public-leaderboard-driven pseudo-generalization due to shortcut learning and rote memorization.

---


### 125. [Decodable Is Not Grounded: A Vision-Ablation Arbiter for VLM Spatial Reasoning](https://arxiv.org/abs/2606.31257)

**<font color=#1a73e8>作者：</font>** Chih-Ting Liao, Fei Shen, Xin Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The standard way to read latent knowledge out of a model, a linear probe confirmed by a steering recovery, can systematically overstate what a vision-language model (VLM) actually grounds in the image. We show this on spatial reasoning, where the error is invisible to both probing and steering yet exposed by a one-line causal control: replacing the image with a gray blank. Probes decode the within-axis answer at 73--97% across axes, and a training-free projection lifts a near-chance axis from 59% to 79%, exactly the signature of unlocking latent knowledge. The blank-image arbiter refutes it, revealing three grounding regimes that probing conflates: an axis can be grounded (vision-dependent, correct), a prior (vision-independent, with its decode and its apparent recovery a directional default rather than perception), or, surprisingly, inverted: decodable, causally controllable, but deployed with the wrong sign, so the model scores below chance and the error requires looking. The taxonomy holds across the studied VLMs: in fourteen models spanning six language-model families and 2B--27B, horizontal is grounded, vertical is a prior, and depth is inverted, with the inversion emerging at scale within families. The decode-versus-deploy inversion replicates on seven of eight models across five families, and the minimal edit that re-deploys it varies with geometry: a training-free rotation matches a trained edit on the cleanest model, while distributed inversions need a trained low-rank edit, tracing a per-model correction-complexity spectrum. The cheap, self-calibrating arbiter cleanly separates grounded perception, inverted perception, and prior substitution; we argue it should be a default control for latent-knowledge and steering claims in VLMs.

---


### 126. [WarpHammer: Densifying Scene Warps with 3D Object Priors for Extreme View Synthesis](https://arxiv.org/abs/2606.31258)

**<font color=#1a73e8>作者：</font>** Michael Green, Gavriel Habib, Dvir Samuel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Projection-conditioned novel view synthesis (NVS) warps an explicit 3D reconstruction of the input view into the target camera and conditions a generator on the warped rendering. This works well for small viewpoint changes but degrades sharply under large orbital motion: the warp becomes sparse around the orbited object, where hidden surfaces dominate the new view and mirror-like artifacts emerge, causing the generator to lose both pixel content and the implicit camera cue carried by the warp. We introduce WarpHammer, a training-free framework that resolves this failure mode by augmenting the warped scene with an explicit 3D reconstruction of the object obtained from a native 3D generative prior (e.g., SAM3D). The reconstructed object adds missing foreground surfaces and occludes background points that should no longer be visible, restoring both appearance and camera cues without fine-tuning the base model. The same explicit object representation further unlocks a capability current NVS pipelines do not support: incorporating auxiliary views of the object from sources outside the target scene, for example, a casual snapshot of a car paired with a manufacturer studio shot of the same model. We process the reference and auxiliary images jointly with a pretrained multi-view geometry foundation model, which predicts a unified point cloud that we fuse into the 3D object reconstruction. This yields substantially more faithful geometry than single-image reconstruction, without requiring user-provided camera poses for the auxiliary views. On five benchmarks, WarpHammer produces stable novel views at viewpoint deviations where strong baselines collapse, and is the first scene-level NVS method that can naturally fuse auxiliary, pose-unknown object views from an external source.

---


### 127. [TDGT: A Tabular Data Generation Toolkit supporting adaptive GPU-accelerated Bayesian mixture models, diffusion-based models, and latent-space generative modeling](https://arxiv.org/abs/2606.31268)

**<font color=#1a73e8>作者：</font>** Vasileios C. Pezoulas, Nikolaos S. Tachos, Eleni Georga 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing demand for privacy-preserving data sharing has positioned synthetic data generation as a critical component of responsible AI workflows. Despite notable advances in generative modeling, existing solutions often lack integration of adaptive generation strategies, multi-metric evaluation, and accessible end-to-end generators within a unified web-based toolkit. In this work, we introduce TDGT (Tabular Data Generation Toolkit), a web-based toolkit for synthetic tabular data generation and fidelity assessment. TDGT introduces the Adaptive Bayesian Mixture Synthesizer (ABMS), a novel algorithm that autonomously determines the optimal number of mixture components through iterative cluster quality optimization, eliminating the need for manual hyperparameter configuration. Building upon ABMS, we further propose VAE-ABMS, a hybrid architecture that couples Variational Autoencoder-based latent space learning with adaptive Bayesian mixture synthesis, enabling high-fidelity generation of complex, nonlinear tabular distributions. For large-scale scenarios, TDGT provides a GPU-accelerated variant of ABMS leveraging CUDA-based k-means clustering and Gaussian mixture fitting. Synthetic data fidelity is assessed through eleven statistical fidelity metrics spanning distributional divergence, structural correlation, and sample-level similarity, complemented by privacy risk indicators including k-anonymity scoring and disclosure rate estimation. The web-based toolkit supports a real-time streaming interface with interactive Plotly-based visualizations. TDGT is assessed across datasets from healthcare, socioeconomic modeling, and cybersecurity domains, demonstrating consistent generation fidelity and statistical coherence across heterogeneous feature types and data scales.

---


### 128. [The Decomposition Is the Fingerprint: Per-Component Identity for Agent Skills](https://arxiv.org/abs/2606.31272)

**<font color=#1a73e8>作者：</font>** Hongliang Liu, Yuhao Wu, Tung-Ling Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly acquire and execute skills at runtime: bundles of prompt instructions, executable code, and tool declarations fetched from marketplaces and other agents. Governing them needs a stable notion of skill identity, yet cryptographic hashing is engineered to destroy the very similarity we need, as a one-character edit scrambles the digest. We present a compact, locality-sensitive fingerprint that embeds each component of a skill and projects it to bits with a multi-bank SimHash, giving a fixed 120-byte signature compared in constant time by Hamming distance. Our central claim is that keeping the fingerprint as a per-component triple (prompt, code, tools), rather than a single score, is what makes it useful: the triple recovers skill-family identity through paraphrase, renaming, refactoring, and controlled code translation when another component remains shared, while independent multilingual reimplementation is not recovered; it also localizes which component carries the reuse. We claim lineage, not behavioral equivalence: identity supplies the structural axis of a registry and leaves safety to behavioral verification. The fingerprint reaches an area under the ROC curve (AUC) of 0.974 (95% CI [0.956, 0.994]) over 4,950 pairwise comparisons while using 77x fewer bits than the embedding it approximates, with ranking preserved in expectation and finite-bit concentration; the per-component split turns one number into relationship classification, families, novelty, and a portable "SkillBOM" for a skill registry. On a 906-skill injection benchmark the fingerprint recognizes injected skills as tampered copies of a known base and localizes the change, but recognition is not trust: it remains, by design, an identity signal complementary to behavioral verification rather than a safety verdict.

---


### 129. [The Calibration Turn in AI-Assisted Research: A Conceptual and Methodological Framework for Evidence-Licensed Claims](https://arxiv.org/abs/2606.31273)

**<font color=#1a73e8>作者：</font>** Hongmin Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI-assisted research has entered a stage in which the central question is not only whether systems can generate hypotheses, run experiments, or produce manuscripts, but whether their scientific claims are calibrated to the evidence that supports them. This Perspective-style paper develops a conceptual and methodological framework for evidence-licensed claims in AI-assisted research. Motivated by representative routes including specialized scientific foundation models, LLM research assistants, multi-agent co-scientists, AI Scientist pipelines, mathematical discovery agents, and self-driving laboratories, it represents AI-assisted research as five operators: hypothesis generation, model-mediated consequence derivation, external validation, belief update, and claim calibration. The central claim is that calibration is not merely cautious wording but a mechanism for managing scientific assertion rights: evidence licenses some forms of speech and withholds others. The paper distinguishes linguistic, consequence-based, interventional, and evidence-licensed semantics; defines the claim-evidence gap and epistemic debt; and treats minimal structural reconstruction across heterogeneous outputs as an upward form of claim calibration. AISim-Cal is included as an illustrative synthetic dynamics exercise, not as an empirical forecast or benchmark. The resulting principles are: no claim without license, validation does not determine claim level, and automation amplifies the need for calibration. Reliable AI-assisted research is therefore evaluated as a loop that generates hypotheses, derives testable consequences, accepts independent adjudication, updates beliefs, and outputs only evidence-licensed claims.

---


### 130. [CLIMB: Centroid-Based Hierarchical Memory for Online Continual Self-Supervised Learning](https://arxiv.org/abs/2606.31275)

**<font color=#1a73e8>作者：</font>** Julien Lefebvre, Stefan Duffner, Mathieu Lefort  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online Continual Self-Supervised Learning (OCSSL) aims to learn representations from a continuous stream of unlabeled data, without knowledge of task boundaries and under memory constraints. Existing methods rely either on replay buffers that exploit latent space structure, or on regularization alone. We present CLIMB (Continual Learning with Intelligent Memory Bank), which combines both simultaneously. Our method introduces a hierarchical centroid-based memory, bounded in total number of stored images, combined with knowledge distillation on replayed examples to limit representation drift. The memory groups similar images into centroids, providing hard-to-discriminate examples for contrastive learning while covering the diversity of observed distributions. Experiments on Split CIFAR-100 and Split ImageNet-100, on standard benchmarks from the state-of-the-art as well as a new protocol with irregular task distributions show that CLIMB outperforms state-of-the-art OCSSL methods.

---


### 131. [Editing Everything Everywhere All at Once](https://arxiv.org/abs/2606.31278)

**<font color=#1a73e8>作者：</font>** Fabio Quattrini, Carmine Zaccagnino, Enis Simsar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Editing multiple elements of an image in a single forward pass is a practical alternative to multi-turn image manipulation, offering improved efficiency and potentially better harmonization. However, when several instructions target different regions, semantic interference often leads to attribute leakage and poor edit disentanglement, especially as the number of edits increases. In this work, we propose MICE (Multi-Instance Concurrent Editing), a training-free strategy for scalable multi-instance image editing with Multimodal Diffusion Transformers. MICE modifies the additive bias of joint attention to regulate interactions between instance-specific edit instructions, latent, and context tokens identified via user-provided segmentation masks. Specifically, MICE allows intra-instance attention, penalizes interactions between neighboring region tokens, and suppresses unrelated cross-instance attention. As a result, our method enforces attribute binding while preserving global visual consistency. We evaluate MICE on LoMOE-Bench and introduce MICE-Bench, a more challenging benchmark with an average of 8.5 concurrent edits per image. The experiments demonstrate that our approach outperforms strong baselines and recent competitors in terms of visual quality preservation and faithfulness to the editing instructions.

---


### 132. [Revisiting the Volume Hypothesis](https://arxiv.org/abs/2606.31282)

**<font color=#1a73e8>作者：</font>** Ari Pakman, Lior Kreimer, Yakir Berchenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep neural networks often contain far more parameters than needed to fit their training data, yet they achieve impressive generalization. A common explanation for this success is the implicit bias of stochastic gradient descent (SGD). An alternative volume hypothesis posits that, within low training-loss regions, loss-landscape basins leading to strong generalization occupy much larger regions of weight space than basins that generalize poorly, and therefore SGD is simply more likely to land in the former. Recent experimental explorations of this idea present seemingly contradictory results. While in one set of experiments randomly sampling the network weights until achieving zero training error yielded poor generalization, molecular dynamics density estimates supported the volume hypothesis. We observe that these experiments were performed at different dataset size regimes, and explore an intermediate regime using the Replica Exchange Wang-Landau algorithm to estimate the joint density of states over training and test accuracies in binary networks. Across several architectures and datasets, we show that the generalization advantage of gradient learning over random sampling training generally diminishes as the training data size grows, suggesting a resolution of the paradox.

---


### 133. [Sequential sparse Gaussian process quantile regression](https://arxiv.org/abs/2606.31284)

**<font color=#1a73e8>作者：</font>** Hugo Nicolas, Olivier Le Maître  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantile regression aims to estimate the conditional quantiles of a response variable from observed data. In a Bayesian setting, Gaussian process quantile regression provides uncertainty quantification but faces significant computational challenges due to the nonconjugacy of the asymmetric Laplace likelihood and the cost of posterior inference. We develop a sparse Gaussian process framework in which the quantile function is represented through a reduced set of inducing variables and posterior inference is performed using a Laplace approximation. A decomposition of the predictive uncertainty into conditional-prior and posterior-induced variance components is then exploited to drive two complementary adaptive mechanisms: inducing-input infilling and data acquisition. These mechanisms are combined within a sequential algorithm that allocates computational effort toward the dominant source of predictive uncertainty and adaptively controls model complexity. Numerical experiments on benchmark problems demonstrate the accuracy of the Laplace approximation, the benefits of variance-based inducing-input placement, and the effectiveness of the proposed sequential enrichment strategy compared with predefined data-acquisition strategies.

---


### 134. [Probabilistic Inversion with Flow Matching](https://arxiv.org/abs/2606.31288)

**<font color=#1a73e8>作者：</font>** Baldur Paulwitz, Stefan Buske  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We demonstrate the application of Flow Matching, a technique originating from generative Artificial Intelligence, to probabilistic inversion in geophysical settings, such as seismic Full-Waveform inversion. We adapt the well-established mathematical theory of Flow Matching from generative Artificial Intelligence to the context of probabilistic inversion. We evaluate the approach with two case studies: a simple 2D velocity model to illustrate the general features of the method, and the OpenFWI dataset to show its capabilities for probabilistic inversion of more complex seismic velocity models.

---


### 135. [Patch-PODiff-ViT: Structured Latent Diffusion with Patchwise POD for Super-Resolution and Uncertainty Quantification](https://arxiv.org/abs/2606.31290)

**<font color=#1a73e8>作者：</font>** Onkar Jadhav, Tim French, Matthew Rayson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models enable probabilistic super-resolution and conditional generation, but pixel-space methods are computationally expensive and learned latent spaces often lack interpretable uncertainty quantification. We introduce Patch-PODiff-ViT, a structured latent diffusion framework in which the latent space is defined by patchwise Proper Orthogonal Decomposition (POD), a fixed linear orthonormal basis over local patches, rather than learned by a nonlinear autoencoder. This yields low-dimensional, variance-ordered tokens that preserve spatial structure and enable efficient diffusion in a structured low-dimensional latent space with a Vision Transformer. Because the decoder is fixed, linear, and orthonormal, latent coefficient uncertainty can be propagated directly to physical-space predictive variance, enabling analytic propagation of predictive variance through the linear decoder without Monte Carlo estimation in pixel space. Across sea surface temperature, medical imaging, and natural images, the method achieves strong reconstruction with fewer parameters and lower memory, while producing well-calibrated spatial uncertainty that closely matches empirical ensembles.

---


### 136. [Deep Reinforcement Learning for Spacecraft Attitude Control During Atmospheric Re-Entry](https://arxiv.org/abs/2606.31291)

**<font color=#1a73e8>作者：</font>** Alexander Fabisch, Melvin Laux, Mariela De Lucas Álvarez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning has the potential to solve attitude control problems more adaptively, precisely, and robustly by handling nonlinear dynamics, uncertainties, and failure cases more effectively than traditional attitude control approaches. We explore reinforcement learning (RL) for attitude control in spacecraft re-entry. An industry-standard proportional-integral-derivative controller with gain scheduling serves as a strong baseline for model-free RL and hybrid controllers that combine these two approaches. We formalize the application in the RL framework to apply continuous, off-policy RL. State-of-the-art RL achieves comparable performance to traditional control approaches in this domain. However, its out-of-distribution generalization is not sufficient. Hence, we use dynamics randomization to introduce challenging task variations during training and enforce generalization in a predefined operational envelope. Finally, we assess the best obtained RL-based controllers with application-specific metrics to show superior performance in comparison to traditional controllers in the operational envelope, that is, hybrid controllers are able to track the angle of attack better and are more robust under variations of mass, inertia tensor, and flap actuator bandwidth.

---


### 137. [Deep Spectral Models for Robust Dental Shape Generation](https://arxiv.org/abs/2606.31293)

**<font color=#1a73e8>作者：</font>** Tibor Kubík, François Guibault, Michal Španěl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate modeling of dental crown morphology is fundamental for diagnosis, orthodontic planning, and computer-aided restoration design. However, datasets suitable for training such models are typically limited in size. We present ToothForge, a deep spectral generative framework that models dental crown geometries from compact, intrinsic representations. By operating in the spectral domain, ToothForge learns a latent manifold of 3D tooth shapes through synchronized spectral embeddings, ensuring consistent modeling across samples with varying connectivity. Spectral synchronization mitigates the instability of Laplace-Beltrami eigenbases and enables efficient learning in a low-dimensional space. The framework is thoroughly evaluated through robustness analysis, ablation studies, and benchmarking against PCA-based statistical shape models and point-based generative frameworks. Results show that synchronized spectral modeling achieves reconstruction and generative performance comparable to or exceeding spatial approaches, while maintaining compactness and geometric interpretability. Together, the compact synchronized coefficients and low-dimensional learning space make the framework particularly suitable for limited datasets, as often encountered in dental and medical domains, and applicable in real-world scenarios where guaranteeing consistent connectivity across shapes from various clinics is unrealistic.

---


### 138. [From Idea to Prototype in an Afternoon: Scaffolded, AI-Assisted Rapid VA Prototyping](https://arxiv.org/abs/2606.31311)

**<font color=#1a73e8>作者：</font>** Gennady Andrienko, Natalia Andrienko  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Testing a new visual-analytics idea usually takes months: one needs to find a realistic data set, clean it, and implement an interactive prototype. We describe a case where a workflow language and an AI assistant reduced this effort to one afternoon. The idea under test: relax the Pareto frontier with a tolerance and group the surviving options into recurring types -- ``constellations'' on a ``soft sky''. Using the Artifact--Transform Workflow Language (ATWL) as a scaffold, we obtained a consistent workflow in minutes and a running prototype in a few hours. We derive three lessons. The scaffold matters: without ATWL the assistant produced a naive workflow. The scaffold alone is not enough: the first implementation was only average, and expert knowledge injection was needed to reach state-of-the-art quality. Finally, the way the scaffold is used matters: controlled experiments show that a language definition and a library of examples support different aspects of the task, that providing both at once reduces quality because template following displaces creative content, and that scaffolds work best when introduced after an initial unconstrained design pass. We argue that the field needs a typology of human knowledge injection, in a form that is both human-editable and machine-accessible.

---


### 139. [BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding](https://arxiv.org/abs/2606.31315)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Yiming Hu, Yong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates inference by using a lightweight draft model to generate candidate tokens in parallel, and are then verified by the target model, enabling lossless acceleration. Recently, diffusion-based speculative decoding further improves parallelism by generating multiple tokens per forward pass via block-level diffusion, achieving state-of-the-art (SOTA) performance. However, existing methods adopt a fixed inference block size and assume a uniform optimal decoding strategy across all inputs. In this paper, we show that this assumption is suboptimal, as the optimal block size varies across samples and plays a critical role in speculative decoding performance. Moreover, these values exhibit a clear local structure, concentrating around the training block size, which reduces the problem to a low-dimensional and structured decision space. Based on these insights, we propose BlockPilot, a sample-adaptive policy that predicts the optimal block size from the prefilling representation. Specifically, we formulate block size selection as a lightweight policy learning problem and propose an instance-adaptive decision mechanism that predicts the optimal block size based on the representation of the prefilling stage. The prediction is performed only once after prefilling, allowing for seamless integration. Extensive experiments demonstrate that our method is plug-and-play, introduces minimal overhead, and consistently improves efficiency, achieving an acceptance length of 5.92 and a 4.20$\times$ speedup on Qwen3-4B under temperature $T=1$.

---


### 140. [Wavelet-Optimized Pseudo-3D Accelerated Diffusion Model for Truncated Computed Laminography](https://arxiv.org/abs/2606.31318)

**<font color=#1a73e8>作者：</font>** Genyuan Zhang, Junyao Wang, Chuandong Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed Laminography (CL) is a key technology for the nondestructive testing of large plate-shaped objects. However, field-of-view (FOV) limitations inevitably lead to truncation of projected data, an ill-posed inverse problem that causes severe reconstruction artifacts. Existing deep learning methods typically rely on 2D architectures that lack rigorous data consistency constraints. Furthermore, they conventionally confine artifact removal strictly to the FOV, discarding potentially recoverable information outside it. To overcome these limitations, we first introduce a comprehensive CL FOV analysis, categorizing the space into data-complete, data-incomplete, and data-free regions. By extending our reconstruction target to encompass the data-incomplete region, we significantly expand the effective imaging range and enhance scanning efficiency. To achieve this, we propose a novel wavelet-optimized pseudo-3D accelerated diffusion model for CL truncation reconstruction (CL-DM). Our method utilizes a standard 2D diffusion model for slice aggregation, combined with a 3D model-based iterative reconstruction (MBIR) method to ensure strict data consistency. To mitigate inter-slice discontinuities, we introduce wavelet regularization along the z-direction, paired with a translation-invariant (TI) mechanism and a low-frequency preservation strategy. Finally, we introduce a 3D fast sampling architecture, significantly accelerating inference speed. Extensive simulations and real-world experiments demonstrate that CL-DM is superior in effectively eliminating truncation artifacts and restoring high-fidelity, continuous 3D structures.

---


### 141. [Safe Online Learning via Smooth Safety-Structured Policy Composition](https://arxiv.org/abs/2606.31320)

**<font color=#1a73e8>作者：</font>** Hongpeng Cao, Liqun Zhao, Yuliang Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe online reinforcement learning requires policies to respect safety constraints while maintaining smooth optimization dynamics. Existing approaches typically rely on either strict safety enforcement via action interventions, which introduce discontinuities in system interaction and learning, or soft safety constraint formulations, which preserve smooth learning but provide limited safety assurance. We propose AutoSafe, a safety-aware policy architecture that integrates structured safety monitoring and intervention directly into the action generation process. This design enables smooth, risk-dependent transitions between performance-driven and safety-preserving behaviors, resulting in continuous online interaction and learning dynamics. Empirical results across a suite of continuous-control benchmarks demonstrate strong safety enforcement without sacrificing learning smoothness. We further validate AutoSafe on a physical cart-pole system, highlighting its practical effectiveness for safe online learning in the real world.

---


### 142. [Accelerated Likelihood Maximization for Diffusion-based Versatile Content Generation](https://arxiv.org/abs/2606.31323)

**<font color=#1a73e8>作者：</font>** Hyunsoo Lee, Inwoo Hwang, Young Min Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating diverse, coherent, and plausible content from partially given inputs remains a fundamental challenge for diffusion models. Existing approaches face clear limitations: training-based approaches offer strong task-specific results but require costly computation, and they generalize poorly across tasks. Training-free approaches offer better efficiency, but they do not explicitly optimize over unobserved variables, leading to globally inconsistent results. To address these limitations, we introduce Accelerated Likelihood Maximization (ALM), a novel training-free sampling strategy integrated into the reverse diffusion process that significantly extends the applicability of diffusion models beyond simple generation tasks. Unlike previous methods that implicitly influence missing regions through pre-generated region constraints, we directly optimize the unobserved region during the sampling process, enabling globally coherent and plausible generation. Furthermore, we incorporate an acceleration strategy that significantly improves computational efficiency without sacrificing performance. Experimental results demonstrate that ALM consistently outperforms state-of-the-art methods in various data domains and tasks, establishing a powerful paradigm for versatile content generation.

---


### 143. [HistoriQA-ThirdRepublic: Multi-Hop Question Answering Corpus for Historical Research, Parliamentary Debates from the French Third Republic (1870-1940)](https://arxiv.org/abs/2606.31325)

**<font color=#1a73e8>作者：</font>** Aurélien Pellet, Julien Perez, Marie Puren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present HistoriQA-ThirdRepublic: a French-language dataset of multi-hop historical questions derived from parliamentary debates and newspapers of the French Third Republic. Designed in collaboration with a historian, the corpus captures complex reasoning patterns typical of historical inquiry, including cross-source synthesis, temporal reasoning, and the integration of sparse evidence. The dataset is made of 1782 questions and emphasizes multi-hop connections across heterogeneous historical documents, providing a resource for evaluating retrieval-augmented and large language model systems in domain-specific contexts. We describe the methodology for constructing the corpus, including the selection and alignment of sources, question validation, and metadata integration. While the dataset focuses on French historical documents, our methodology can be readily adapted to other languages and national corpora. Finally, we demonstrate how the corpus can support realistic evaluation scenarios for multi-hop question answering, bridging the gap between NLP benchmarks and the needs of historical scholarship.

---


### 144. [Bridging Video Understanding and Generation in a Unified Framework](https://arxiv.org/abs/2606.31326)

**<font color=#1a73e8>作者：</font>** Yuqi Wang, Runyi Li, Ruoyu Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, unified image generation and understanding have been extensively explored. However, extending such unified modeling paradigms to the video domain remains largely underexplored. A central challenge is that video understanding favors compact, discriminative semantic representations, whereas video generation requires dense signals that preserve visual details and temporal coherence. Videos naturally capture both spatial semantics and temporal dynamics, making them a more suitable modality for unified multimodal modeling compared to static images. In this paper, we propose Vega, a unified framework that bridges video understanding and generation. Vega leverages a shared vocabulary to jointly model text and visual representations and employs a hybrid architecture combining autoregressive (AR) prediction with diffusion-based rendering. Specifically, the AR model focuses on predicting semantically meaningful visual tokens for keyframes, providing a structured representation that guides the diffusion module in rendering dense, high-resolution video frames. Extensive experiments demonstrate that Vega achieves strong performance on video generation benchmarks such as VBench and video understanding benchmarks like VideoMME.

---


### 145. [Expected Gain-based Escalation in Vertical Federated Learning](https://arxiv.org/abs/2606.31331)

**<font color=#1a73e8>作者：</font>** Mohamad Mestoukirdi, Vincent Corlay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collaborative inference can improve predictive performance by integrating complementary information across agents, but applying collaborative fusion to every sample can incur unnecessary communication and computational overhead. This trade-off is particularly relevant in vertical federated learning (VFL), where clients observe different views of the same sample and fusion typically requires transmitting intermediate representations to a server. We study selective escalation in a two-round VFL inference protocol, in which a low-cost first round produces a prediction from client posteriors and a second embedding-fusion round is invoked only when it is expected to improve the final decision. We formulate routing as expected-gain score estimation: a sample is escalated when a predicted improvement in correctness justifies the additional communication. The proposed analytical score combines a calibrated pooled posterior with classwise reliability estimates of the VFL model, both obtained from held-out calibration data, yielding an interpretable router that requires no separately trained routing network. Experiments on multi-view classification benchmarks, including controlled test--time view degradation settings, show that the proposed router improves the communication-accuracy trade-off over confidence-, learned-gain-, and deferral-based baselines.

---


### 146. [CryoACE: An Atom-centric Framework for Accurate and Automated Model Building in Cryo-EM](https://arxiv.org/abs/2606.31332)

**<font color=#1a73e8>作者：</font>** Minzhang Li, Mingrui Li, Weichen Qin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Protein automodeling from cryo-EM density maps faces unique challenges in enforcing physicochemical validity and managing conformational heterogeneity. Current solvers are often limited to static predictions or require computationally intensive heuristic searches. We present CryoACE, an end-to-end framework that reconstructs precise atomic graphs for both homogeneous and heterogeneous structures. Our method features two key innovations: an atom-centric reconstruction paradigm, where density features are sampled directly at atomic coordinates and iteratively recycled to refine structures, replacing expensive voxel convolutions for efficient multimodal fusion; and a training-free guidance mechanism that leverages predicted local resolution priors to resolve dynamic ambiguity. Validated on a newly constructed high-quality dataset, CryoACE significantly outperforms existing baselines on static benchmarks and, for the first time, unveils atomic-level dynamic conformations on complex real-world datasets like EMPIAR-10345 without relying on pre-built static structures.

---


### 147. [Automated High-Precision Extraction and Forensic Verification of Data-Bearing Vector Figures](https://arxiv.org/abs/2606.31345)

**<font color=#1a73e8>作者：</font>** Bowen Sun, Chaowei Xiao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The quantitative record of science and engineering is increasingly carried by figures rather than text or tables, and a reader who needs the underlying numbers must usually re-digitize them by hand: slowly, imprecisely, and with no way to prove the result is faithful. Yet when a figure is stored as vector graphics, its data are not approximated by the picture but encoded in it: the renderer writes each marker and vertex at a printed precision that, for the dominant scientific toolchain, exceeds the data's own. We turn this into three contributions, one per shortcoming of hand digitization. First, a precision theory bounding how accurately data can be recovered for a given renderer and export format: bit-exact float32 for matplotlib markers, and a calibration-limited three to four significant figures end to end. Second, an automatic extractor that decodes a figure in one pass with no human in the loop, in place of the slow point-by-point tracing a digitizer demands. Third, a verification theory: recovery is injective except on a characterized, vanishingly small interval near zero; accidental agreement between unrelated data is astronomically unlikely; and a re-rendering certificate binds the recovered values to the markers, lines, and ticks the figure draws, not its text, making a result non-repudiable. With no ground truth used during recovery, decoded figures match external archives (Planck 2018 to 10^-9; the Keeling CO2 record to 5*10^-4, and one decoded figure independently reproduces a correction to the Chinchilla scaling-law confidence interval. We map the achievable precision across common renderers and their PDF, SVG, and EPS formats. What we deliver is certified data; the scientific significance of any particular dataset lies outside this paper's scope, and recovered values are candidates for human review, never accusations.

---


### 148. [Smart charging of large fleets of Electric Vehicles: Independent Multi-Agent Reinforcement Learning approaches](https://arxiv.org/abs/2606.31347)

**<font color=#1a73e8>作者：</font>** Xavier Rate, Eloann Le Guern, Raphaël Féraud 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The electrification of transportation through electric vehicles introduces new challenges for power grid management, such as increased peak demand, voltage fluctuations, line overloads, and the integration of variable renewable energy sources. To enable efficient integration of EVs while minimizing costs for users and avoiding network overloads, implicit coordination between EVs is required. This work compares two independent multi-agent reinforcement learning approaches for optimizing such decentralized EV charging: contextual combinatorial bandits and policy gradient algorithms. Using a realistic simulation environment with autonomous agents making decisions based on local environmental information (including price signals, state-of-charge, and temporal constraints), we evaluate their performance across varying congestion levels, and mixed-strategy configurations with heterogeneous agent groups under dynamic electricity pricing derived from real photovoltaic production data.

---


### 149. [Patient-Level Elbow Abnormality Detection: Leakage-Aware Evaluation of Learned Preprocessing, Calibration, and Triage-Oriented Operating Points](https://arxiv.org/abs/2606.31348)

**<font color=#1a73e8>作者：</font>** Ahmed Sallam, Ahmet Kaplan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this study, we examine learned preprocessing pipelines in the context of triage-oriented orthopedic abnormality detection task using elbow radiographs from MURA dataset. The evaluation focuses on patient-level detection of musculoskeletal abnormalities under a leakage-aware protocol. We compare multiple preprocessing pipelines, with and without a lightweight DnCNN module as a learned preprocessing component, to assess their impact on discrimination and calibration. Performance is assessed using discrimination metrics (AUROC, PR-AUC), calibration measures (ECE, Brier score), and validation-selected operating point analysis targeting high specificity. Results show that differences across preprocessing strategies are modest and configuration-dependent, with no consistent discrimination advantage over the raw-input DenseNet121 baseline. The raw and diverse inputs combined with the DnCNN front-end showed reduced ECE and Brier score, while CLAHE combined with DnCNN did not improve calibration. Overall, the results suggest that under patient-level evaluation, preprocessing gains are modest and configuration-dependent; the raw-input DenseNet121 baseline remains competitive throughout, and no tested preprocessing strategy produced a consistent discrimination advantage across all metrics.

---


### 150. [Dualformer: Efficient Feature Extractor for Complex-valued Blind Communication Signal Analysis](https://arxiv.org/abs/2606.31352)

**<font color=#1a73e8>作者：</font>** Yurui Zhao, Xiang Wang, Jingreng Lei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing effective feature extractors is critical for blind signal analysis tasks such as automatic modulation recognition (AMR), signal scheme recognition (SSR), and \color{black} signal structure parsing (SSP). In this work, we propose dual-channel neural network (DualNN) that efficiently exploits complex-valued signals through parameter sharing across IQ channels. Unlike traditional real-valued or complex-valued models, DualNN is a groundbreaking framework which shares the network parameters for processing the real and imaginary parts of the complex-valued signals, and is theoretically shown to reduce generalization error while preserving expressive capacity. Specifically, we propose a novel Transformer-based architecture to implement DualNN, called Dualformer. The Dualformer segments input signals into patch-level tokens and captures multi-granularity features, enabling robust performance across diverse signal analysis tasks. Furthermore, we conduct extensive experiments comparing Dualformer with three Transformer-based baselines and four conventional DL-based approaches. Results demonstrate consistent performance improvements on AMR, SSR, and SSP tasks. Besides, the modular design of DualNN allows it to generalize well to blind signal processing tasks such as blind source separation and low-SNR spectrum sensing. This work paves the way for a broader application of DualNN architectures in unsupervised and weakly supervised complex-valued signal analysis scenarios.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-274](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
