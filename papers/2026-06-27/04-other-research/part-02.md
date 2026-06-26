# 📦 其他研究 | 2026年06月27日

> 本类共 **245** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-245](./part-05.md)

---

### 51. [Assistive Visual Cues for Visual Neglect Patients](https://arxiv.org/abs/2606.26407)

**<font color=#1a73e8>作者：</font>** Per Bjerre, Andreas Køllund Pedersen, Hendrik Knoche  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Previous research on exogenous and endogenous cues has shown how they direct attention and improve interaction speed and error rate in applications. However, most studies focus on people with normal sight. People suffering from visual neglect have difficulties attending to parts of the visual field. One treatment method calls for the use of strong visual cues to remind patients of their neglected area and help guide their attention to it. Therefore, we examine the effects of endogenous and exogenous cues on visual neglect patients. Our results showed that visual neglect patients perform better with endogenous cues, when targets are within their neglected area. In some cases, combining exogenous and endogenous cues improve performance further. However, the performance varies greatly between patients. Using one neglect patient as an example, we saw that the best endogenous cue had an average acquisition time of 3.5 seconds compared to 6.5 for the best exogenous. Combining exogenous and endogenous cues further improved acquisition time to 2.8 seconds.

---


### 52. [Neural Voxel Dynamics: Learning Implicit 3D Physics via Volumetric Feature Advection](https://arxiv.org/abs/2606.26410)

**<font color=#1a73e8>作者：</font>** Zican Wang, Niloy Mitra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a self-supervised framework for learning implicit 3D physical dynamics directly from video-derived supervisory signals. While current generative video models achieve high visual fidelity, they lack a 3D geometric foundation, often resulting in physical inconsistencies and a failure to maintain object permanence. We address this by shifting the predictive bottleneck from 2D image space to a `lifted' 3D Volumetric Latent Space. Our method unprojects semantic features from a Video Joint-Embedding Predictive Architecture (V-JEPA) into a voxelized grid, grounded by monocular depth priors. This lifting enables a Volumetric Feature Advection to learn an action-conditioned transition operator that treats physics as a spatio-temporal state advection problem, i.e., learn implicit 3D physics. Unlike state-of-the-art hybrid models that rely on explicit classical simulators for training and/or inference, our architecture tracks material states implicitly within high-dimensional V-JEPA features. This allows for the emergent simulation of heterogeneous phenomena (e.g., rigid body motion in fluid flow) within a single, unified pipeline. Supervised solely via end-to-end video-derived signal plus action conditions, without access to physics engine internal states, labels, or surrogate models, our model demonstrates good long-term structural stability and physical plausibility on multiple benchmarks (CLEVERER, PhysInOne, PhysGaia). We believe that this work opens a scalable pathway toward general-purpose dynamic world models that internalize the 3D invariants of the physical world solely through passive observation of monocular videos.

---


### 53. [What Browsers Do in the Shaders: A Measurement Study of WebGPU Privacy](https://arxiv.org/abs/2606.26412)

**<font color=#1a73e8>作者：</font>** Igor Santos-Grueiro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> WebGPU lets ordinary web pages run GPU workloads through a validated programming model. Validation protects memory safety, but shared browser, driver, OS, and GPU state can still expose privacy-relevant signals. We present WGPULens, a framework for measuring those signals across controlled scenarios, browser-native co-residency, a participant field study, public page loads, and mitigation policies. Our framework separates measurements: controlled scenarios support leakage, boundary, and mitigation claims; participant runs support deployment, compatibility, and fingerprintability; and a Tranco crawl measures WebGPU exposure in real-world pages.
Our controlled results identify persistent pipeline compilation state as the clearest surface. Cold/warm pipeline probes reveal prior compilation state across selected origin, profile, and browser placements. Controlled browser/native experiments also show native GPU activity can be inferred from browser-visible observables under labeled workloads. Other resource probes provide weaker positive results and negative controls.
The participant field study shows active WebGPU behavior is highly distinctive within the sample, with deterministic components stable within runs and lower exact stability across repeated visits. A page-load crawl finds WebGPU use mainly as adapter probing and static support code, with no observed page-load shader, pipeline, queue, query, or map activity. Mitigation pilots identify source-level key separation as a proxy for evaluating pipeline-cache partitioning. Overall, WGPULens shows that WebGPU privacy analysis must be surface-specific: browsers need to measure which GPU state crosses which boundary, which browser-visible signals reveal it, and what the corresponding mitigations cost.

---


### 54. [Unbiased Canonical Set-Valued Oracles Via Lattice Theory](https://arxiv.org/abs/2606.26418)

**<font color=#1a73e8>作者：</font>** Jobst Heitzig  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A non-agentic "oracle" AI that estimates probabilities of future events faces a self-reference problem: once its answer is learned and acted upon, it can change the very probability it was asked to report. One response, advocated for the Scientist AI programme, is to ask only counterfactual questions, evaluated as if the answer had no influence. We observe that such answers tend to become irrelevant the moment they are learned, precisely because their premise is then false. We therefore explore a self-referential alternative in which the oracle reports not a single probability but a credal set that is simultaneously unbiased and self-consistent with the consequences of being learned. The naive self-consistency requirement is satisfied by too many sets (including the useless answer $[0,1]$), so the problem is to single out a canonical, nontrivial member. We do so with the Knaster--Tarski fixed-point theorem on the complete lattice of closed credal sets, taking the least fixed point of a suitably defined isotone operator; a variant instead reports the least fixed point that contains every self-consistent point estimate. We prove existence, self-consistency, and nonemptiness, show that the construction collapses to the classical point answer for non-performative questions, and that for a binary event the canonical answer is, under a natural hull-factoring assumption, an interval. The development is purely lattice-theoretic and extends unchanged from a binary event $B$ to an arbitrary random variable $X$, with $P(B\mid A,C)$ replaced by the conditional law $\mathcal{L}(X\mid A,C)$. We close with open questions, including whether the interval characterization itself survives that generalization.

---


### 55. [Otter Weather: Skillful and Computationally Efficient Medium-Range Weather Forecasting](https://arxiv.org/abs/2606.26421)

**<font color=#1a73e8>作者：</font>** Cristiana Diaconu, Jonas Scholz, Aliaksandra Shysheya 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-of-the-art medium-range AI weather models can outperform traditional Numerical Weather Prediction (NWP) but require massive training budgets. This restricts usage for under-resourced groups and severely limits fast model iteration. Here we develop Otter Weather, a highly efficient spatiotemporal forecasting model designed to democratise high-performance weather prediction with AI. Evaluated on ERA5 reanalysis data at 1.5° resolution using standard WeatherBench protocols, the Otter family significantly advances the skill-compute Pareto frontier. The deterministic version outperforms the best NWP baseline by 9.6% at a 24-hour lead time while requiring fewer than 3.5 A100-days for training. It provides a 2x efficiency gain over lightweight AI models and a 100-fold reduction in compute compared to resource-intensive frontier architectures. We extend these efficiency gains into probabilistic forecasting by training via the Continuous Ranked Probability Score (CRPS). Scaling to a larger architecture, Otter-XL achieves a 9.7% CRPS improvement over the IFS ENS baseline. This yields an almost two-fold increase in predictive skill over comparable lightweight models at similar compute budgets. Otter-XL also outperforms frontier architectures like GenCast by over 2%, while using an order of magnitude less compute. Finally, Otter is applied out-of-the-box to a complex acoustic scattering PDE task where it outperforms a state-of-the-art foundation modelling approach, suggesting that the advances made here might apply across a range of scientific domains.

---


### 56. [Rethinking Training & Inference for Forecasting: Linking Winner-Take-All back to GMMs](https://arxiv.org/abs/2606.26424)

**<font color=#1a73e8>作者：</font>** Qiyuan Wu, Katie Z Luo, Bharath Hariharan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trajectory forecasting for autonomous driving has advanced rapidly, yet representative models often produce uninformative posteriors over forecast modes, causing problems for mode pruning. We trace this to a modeling-training mismatch: forecasters are typically modeled as conditional Gaussian mixture models (GMMs) but trained with a winner-take-all (WTA) loss that assigns each sample to its nearest mode. We argue that this K-means-like hard assignment (one-hot), while preventing mode collapse, is the source of uninformative mode probabilities: it over-segments the trajectory space, ignores relatedness among nearby modes, and yields assignment instability under small perturbations. Guided by this lens, we introduce two post-hoc treatments: (1) test-time posterior-weighted merging that aggregates nearby candidate trajectories; and (2) a one-step expectation-maximization (EM) update that replaces hard labels with soft responsibilities, sharing probability mass across neighboring modes. Across several WTA-trained architectures, these lightweight steps produce more informative, faithfully ranked mode posteriors and strengthen final forecasts on popular displacement metrics -- without retraining. Our analysis unifies recent design choices through a GMM-vs-K-means perspective and offers principled, practical corrections that better align training objectives with inference.

---


### 57. [ProvenAI: Provenance-Native Traces of Evidence in Generated Answers](https://arxiv.org/abs/2606.26449)

**<font color=#1a73e8>作者：</font>** Mohammad Faizan, Dalal Alharthi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented systems routinely present citations alongside generated answers, yet a citation does not confirm that the corresponding source meaningfully shaped the output. This paper introduces ProvenAI, a framework that decomposes transparency in multi-hop question answering into three independently measurable layers: answer correctness, citation fidelity against benchmark supporting evidence, and per-document influence under leave-one-resource-out intervention. Targeting the HotpotQA distractor benchmark through a seven-stage pipeline covering data normalisation, retrieval indexing, citation-aware answer generation, attribution auditing, ablation-based influence estimation, batch evaluation, and interactive inspection, ProvenAI evaluates 7,405 validation examples drawn from a canonical corpus of 509,300 passages. The system achieves 53.53% answer accuracy alongside a mean citation-fidelity score of 71.55%, and a worked example surfaces what we call the citation-influence gap: a clean citation audit co-occurring with a profile in which one cited source registers only weak influence while seven uncited sources demonstrably shift the output. We formalise the relationship between the implemented surface proxy and a token-level KL-divergence target through a stated faithfulness condition, ground the framework in causal-mediation analysis and database-provenance theory, and discuss how the three measurement layers compose with cryptographic provenance architectures emerging in autonomous scientific discovery. ProvenAI establishes that meaningful transparency in retrieval-grounded QA requires traceable links across retrieved, cited, and behaviourally influential evidence as three distinct, independently measured layers.

---


### 58. [AnySimLite: A Lightweight Few-Shot Similarity Encoder for On-Device Speech-Adjacent Classification](https://arxiv.org/abs/2606.26452)

**<font color=#1a73e8>作者：</font>** Sourav Ghosh, Yash Bhatia, Keshav Goyal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To minimize privacy concerns and inference latency on edge devices like smartphones, lightweight on-device models remain important for end-user applications. Many of these applications involve natural language classification, but deploying multiple specialized models creates a memory footprint challenge. We investigate: Can a single lightweight architecture solve multiple Speech-Adjacent (SA) classification tasks through reduction to a nuanced text similarity formulation? We propose AnySimLite, a lightweight similarity encoder that combines word-level and character-level channels. Together with a dataset transformation strategy, we evaluate AnySimLite across multiple SA classification tasks and show that it consistently achieves state-of-the-art (SOTA) or SOTA-competitive performance in few-shot settings while maintaining a low memory footprint. Even in the worst case, the performance drop remains below 7% while using $<\frac{1}{250}^{\mathrm{th}}$ of the model size of the SOTA qLLaMA_LoRA-7B baseline.

---


### 59. [Data-driven Machine Learning Cannot Reach Symbolic-level Logical Reasoning -- The Limit of the Scaling Law](https://arxiv.org/abs/2606.26454)

**<font color=#1a73e8>作者：</font>** Tiansi Dong, Mateja Jamnik, Pietro Liò  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sphere neural networks have achieved symbolic level syllogistic reasoning without training data, raising the question of where the limit of the scaling law for logical reasoning lies, i.e., whether data-driven machine learning systems can achieve the same level by increasing training data and training time. We show two methodological limitations that prevent supervised deep learning from reaching the symbolic-level syllogistic reasoning: (1) training data can not distinguish all 24 types of valid syllogistic reasoning; (2) end-to-end mapping from premises to conclusion introduces contradictory training targets between neural components for pattern recognition and logical reasoning. Beside theoretical analysis, we experimentally illustrate that Euler Net cannot achieve rigorous syllogistic reasoning. We further challenge the most recent ChatGPTs (GPT-5-nano and GPT-5) to determine the satisfiability of syllogistic statements in four surface forms (patterns): words, double words, simple symbols, and long random symbols, showing that surface forms affect the reasoning performance and that ChatGPT GPT-5 may reach 100% accuracy but still provide incorrect explanations. As empirical training processes are stopped after achieving 100% accuracy, we conclude that supervised machine learning systems will not attain the rigour of symbolic logical reasoning.

---


### 60. [Active Adversarial Perturbation-driven Associative Memory Retrieval for RGB-Event Visual Object Tracking](https://arxiv.org/abs/2606.26455)

**<font color=#1a73e8>作者：</font>** Xiao Wang, Xufeng Lou, Zikang Yan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-Event tracking improves localization robustness by fusing RGB appearance textures and dense temporal motion cues from event sensors. While this multi-modal scheme broadens tracking applicability, real-world scenes suffer diverse structured signal degradations that hinder traditional multi-modal fusion. In harsh environments, either modality can lose reliability drastically, and targets frequently appear incomplete due to occlusion, edge truncation and foreground this http URL tackle the above challenges, we present a hierarchical perturbation and retrieval framework tailored for RGB-Event tracking with robustness against partial target missing and modal degradation, termed APRTrack. To mimic real-world signal corruption, APRTrack constructs structured degradation via two adversarial perturbation branches at the modality and spatial levels, which separately simulate full-modal failure and localized target region absence. A hierarchical routing mechanism is designed to disentangle the training pipelines of the two perturbation types, effectively eliminating feature collapse induced by superimposed degradation constraints. Furthermore, we devise Footprint-guided Channel-calibrated Hopfield Retrieval (FCHR) for reliable historical information compensation. This module evaluates retrieval confidence based on association footprints between queries and memory banks, and calibrates the retrieval metric space prior to Hopfield matching, realizing controllable historical feature compensation bounded to target regions. Extensive experiments on FE108, COESOT, VisEvent, and FELT datasets demonstrate the effectiveness of our proposed strategies for the RGB-Event visual object tracking. The source code and pre-trained models will be released on this https URL

---


### 61. [auto-psych: Automating the science of mind using agent-driven theory discovery and experimentation](https://arxiv.org/abs/2606.26460)

**<font color=#1a73e8>作者：</font>** Ben Prystawski, Kushin Mukherjee, Daniel Wurgaft 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-based scientific automation is increasingly possible by using agents to generate hypotheses, design experiments, and analyze data. Data collection is a major bottleneck in this pipeline, however. Psychology, and computational cognitive science in particular, is well-positioned to benefit from AI experimentation because theories are often represented as code and crowdsourcing platforms enable programmatic human data collection at scale. Here, we apply automated discovery techniques to the project of generating theories in computational cognitive science, with an agent-based system collecting human data independently through crowdsourced survey experiments. As a testbed, we use a classic case study from cognitive psychology: judging which sequences of coin flips seem subjectively more random. Our system, auto-psych, uses nested agent-based discovery loops to generate explanatory theories of human behavior. The inner loop conjectures, fits, and critiques probabilistic cognitive models; the outer loop designs experiments to test these models, launches them online, and analyzes the data. This system can quickly and reliably recover ground-truth theories from synthetic data via systematic experimentation, but the nested structure is critical to model performance. Further, in three independent sequences of human experiments, the system finds theories that fit the data better than theories generated from the scientific literature. This work thus demonstrates the feasibility of automated data collection and theory discovery in computational cognitive science.

---


### 62. [Finding the Time to Think: Learning Planning Budgets in Real-Time RL](https://arxiv.org/abs/2606.26463)

**<font color=#1a73e8>作者：</font>** Aneesh Muppidi, Firas Darwish, Dylan Cope 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deliberating takes time. In real-time settings, that time is not free. Standard reinforcement learning (RL) sidesteps this as the environment waits indefinitely for the agent's decision. Instead, we study real-time RL environments where the environment progresses while waiting for the agent's action. Building on prior real-time formalizations, we introduce variable-delay real-time RL, where the agent chooses how long to deliberate at each decision point since the environment progresses. For the planning agents we use, the right delay is state-dependent, and naively planning how long to plan can paralyze the agent. We instead approach this setting by training a lightweight gating policy on top of a planner to select state-dependent planning budgets. Across real-time Pac-Man, Tetris, Snake, Speed Hex, and Speed Go, our gating policy outperforms fixed-budget and heuristic baselines, and transfers to a real-time setup where the environment and agent run on two different GPUs.

---


### 63. [Epiphany-Aware KV Cache Eviction Without the Attention Matrix](https://arxiv.org/abs/2606.26472)

**<font color=#1a73e8>作者：</font>** Steven Kolawole, Virginia Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As reasoning models emit chains of thought tens of thousands of tokens long, KV cache increasingly becomes a deployment bottleneck. Existing cache eviction methods rank tokens by attention weight, which is a noisy importance proxy in long reasoning traces, and prohibits the use of fused kernels in production inference by forcing the model to materialize the attention matrix. In this work, we instead score tokens with a metric we term the epiphany score: the change in the model's internal representation, read directly from the forward pass with no attention matrix and negligible extra state. Our resulting cache eviction method, EpiKV, requires no training, classifier, or custom kernel, and can be used directly in FlashAttention inference stacks unchanged -- scaling to a 16x longer feasible context than attention-based scoring. upper-mid layers negatively) and remove a positional trend with a causal rolling z-score. At a 4096-token cache EpiKV reaches 72% on MATH-500, matching the strongest attention-based baseline (ThinKV 71%, H2O 67%); a lag-normalized KV variant reaches 37% on AIME-2024 at 8192 tokens against the best of them (33%), at up to 2.8x the speed.

---


### 64. [Retrieval-Warmed Energy-Based Reasoning: A Five-Arm Ablation Methodology for Diffusion-as-Inference on Structured Reasoning Tasks](https://arxiv.org/abs/2606.26476)

**<font color=#1a73e8>作者：</font>** Libo Sun, Po-Wei Harn, Zewei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Warm-started diffusion samplers accelerate iterative inference, but it is rarely clear which part of the pipeline carries the gain. We study \textbf{retrieval-warmed energy-based reasoning (RW-EBR)} -- an IRED energy-based diffusion model \cite{du2024ired} augmented with a Modern Hopfield trajectory memory -- and contribute a \textbf{five-arm ablation methodology} (oracle, best-constant, per-query-random, shuffled, aligned) that separates three confounded effects: class-prior bias shift, stochastic warm-starting, and graph-aligned value reuse. The diagnostic decomposition is adapted from LLM-RAG evaluation \cite{ru2024ragchecker}. On \textbf{connectivity-2} (Erdős--Rényi all-pairs reachability), the aligned-vs-shuffled-oracle swing reaches \textbf{$+35$\,pp} balanced accuracy on a fixed 1{,}000-graph validation-set diagnostic, with value distribution and retrieval mechanics fixed, only per-graph alignment destroyed, while per-query random initialisation falls below cold -- per-graph alignment, not bias shift or stochasticity, dominates. Yet the \emph{deployable} cold-prediction pipeline misses the acceptance gate at stored-value quality. The same diagnostic logic, stopped at the key-quality screen, applied to \textbf{Sudoku} with a task-specific key encoder produces a clean negative at a \emph{different} component -- key quality, under the current setup. The decomposition names the first blocking component on each task. The setting -- graph reachability refined by an iterative diffusion sampler, with explainability of failure modes as the lens -- places the work within structured and spatio-temporal reasoning.

---


### 65. [Utilizing Cognitive Signals Generated during Human Reading to Enhance Keyphrase Extraction from Microblogs](https://arxiv.org/abs/2606.26485)

**<font color=#1a73e8>作者：</font>** Xinyi Yan, Yingyi Zhang, Chengzhi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Microblogging platforms generate massive amounts of short, noisy, and dispersed user content, making automatic keyphrase extraction (AKE) an important but challenging task. Prior studies have used eye-tracking signals to improve microblog-based AKE because such signals reflect readers' attention to salient words. However, eye tracking alone is limited by physiological, acquisition, and feature-decoding constraints. To address this issue, we investigate whether electroencephalogram (EEG) signals can complement eye-tracking signals for AKE. Using the ZuCo cognitive language processing corpus, we select 8 EEG features and 17 eye-tracking features and incorporate them into microblog-based AKE models. To reduce possible distortion of cognitive signals by model structures, we inject these features into the input of the soft-attention layer and the query vectors of the self-attention layer. We then evaluate different combinations of cognitive signals across AKE models. The results show that cognitive signals produced during reading consistently improve AKE performance, regardless of feature combinations and model architectures. EEG features bring the largest gains, while combining EEG and eye-tracking features yields performance between the two individual signal types, suggesting partial complementarity but also possible redundancy or noise. These findings indicate that EEG signals provide useful cognitive evidence for microblog-based AKE and that multimodal cognitive signals deserve further investigation.

---


### 66. [DKVE: Decentralized Key Validation for End-to-End Encrypted Messaging](https://arxiv.org/abs/2606.26486)

**<font color=#1a73e8>作者：</font>** Subin Song, Taekyoung Kwon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> End-to-end encrypted messaging systems depend on authentic public key distribution to prevent man-in-the-middle (MitM) attacks. Current solutions present a stark trade-off: out-of-band (OOB) verification provides strong security but lacks scalability for large contact lists, while key transparency (KT) systems enable automated verification at high storage costs and operational complexity.
We propose DKVE, a protocol that validates public keys through privacy-preserving cross-validation within users' social graphs. When obtaining a contact's public key from a key server, clients query mutual contacts to verify they hold the same key, combining Oblivious Pseudorandom Functions (OPRF) and Oblivious Key-Value Stores (OKVS) to preserve privacy of both queries and contact lists. DKVE employs a Sequential Probability Ratio Test (SPRT) to aggregate responses and detect server misbehavior with user-configurable error bounds.
We evaluate DKVE through simulations on real social network datasets, demonstrating DKVE can detect MitM attacks with exceeding 97% for strong-to-moderate-tie networks. The remaining 3% of cases require validation through alternative methods such as KT and OOB verification. Our proof-of-concept implementation confirms feasibility for background operation on commodity hardware, in terms of the latency and bandwidth.
As DKVE can reduce the frequency of KT queries by two orders of magnitude, it enables fundamental architectural shifts: KT directories can migrate from fast but space-inefficient Merkle trees to space-efficient data structures like RSA accumulators. While DKVE cannot replace existing methods entirely -- suffering from bootstrapping problems and degraded performance on weak-tie networks -- it provides a practical complementary key validation mechanism, making secure messaging more deployable for billion-user systems.

---


### 67. [What Survives When You Compress a Recursive Reasoner for the Edge?](https://arxiv.org/abs/2606.26488)

**<font color=#1a73e8>作者：</font>** Pearse Jim, Steven Kolawole, Opegbemi Matthias Busoye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive reasoning models can solve complex structured tasks with only a few million parameters by repeatedly updating a latent state. Deploying these models on edge hardware requires significant compression, but unlike conventional sequence models, quantization errors compound across recursive reasoning cycles rather than across output tokens. As a result, standard intuitions about compression fail to apply. In this work, we ask what survives when recursive reasoners are compressed. Across a full precision sweep, three tasks, and two recursive architectures, we find that aggressive compression preserves local prediction but destroys global reasoning: cell accuracy holds while puzzle-exact accuracy collapses to zero under naive INT4 pruning, distillation, and linear attention alike. Token-level objectives, including quantization-aware training, cannot repair it. The collapse is architectural -- it strikes MLP-mixing recursion but not attention on the same task -- and we reverse it with per-channel calibrated INT4 without retraining. We also introduce carry-trajectory fidelity, the cosine similarity to the full-precision reasoning path, as a label-free signal that predicts this damage and its recovery before a task evaluation. The combined result is a deployment recipe: flash-streamed embeddings remove a 99.4MB bottleneck, INT8 at one cycle matches full-depth accuracy at 6x fewer FLOPs (8MB SoC), and calibrated INT4 fits a 4MB microcontroller.

---


### 68. [Clinical Harness for Governable Medical AI Skill Ecosystems](https://arxiv.org/abs/2606.26494)

**<font color=#1a73e8>作者：</font>** Tianhan Xu, Lei Bao, Yongxiang Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical AI remains organized around isolated models, whereas clinical care requires accountable capabilities that persist across time. We propose clinical AI skills and the Clinical Harness: a runtime governance architecture for registering, orchestrating, guarding and monitoring AI-enabled clinical capabilities. Using osteoporosis as an exemplar, we show how knowledge-driven, data-driven and physics-enhanced skills can support lifecycle care under runtime governance.

---


### 69. [Learning Probabilistic Filters with Strictly Proper Scoring Rules](https://arxiv.org/abs/2606.26497)

**<font color=#1a73e8>作者：</font>** Eviatar Bach, Ricardo Baptista, Jochen Bröcker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian filtering of partially and noisily observed dynamical systems seeks to infer the evolving conditional distribution of the state of a dynamical system, given observations, in an online fashion. This Bayesian filtering distribution is the natural object for uncertainty quantification, but it is rarely available as a supervised learning target. However, one can often use the forecast model to generate synthetic system trajectories, along with synthetic observations. We introduce the proper scoring ensemble filter (PSEF), an ensemble data assimilation method based on training an analysis map to approximate the filtering distribution using only synthetic state--observation trajectories. The analysis step is represented as a permutation-invariant, transformer-based map that takes as input a forecast ensemble and observations, producing an analysis ensemble. Training is based on strictly proper scoring rules -- with the energy score used in our implementation -- so that probabilistic accuracy is rewarded over the whole probability distribution. We prove that, under a realizability assumption, the population objective is minimized by the true Bayesian filtering distribution. We also derive the finite-ensemble empirical objective used in training and relate its single state--observation trajectory form to the population objective, using a mean-field consistency argument. Numerical experiments show that the learned filter accurately approximates challenging filtering distributions, including nonlinear, non-Gaussian, and multi-modal posteriors, and achieves stronger performance in data assimilation tasks than classical methods or learning-based methods with mean-squared-error objectives. For close-to-Gaussian problems, learning a correction to the EnKF is the best approach, while for highly non-Gaussian problems an end-to-end approach that discards this inductive bias is superior.

---


### 70. [TinyCNNDeep: Lightweight Attention-Based CNN for EEG Classification of Eye States and Sleep Deprivation](https://arxiv.org/abs/2606.26506)

**<font color=#1a73e8>作者：</font>** Thien Nhan Vo, Yen Nhi Tran Thi, Ngan Nguyen Xuan Phuong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Sleep deprivation impairs vigilance and cognitive function, yet jointly identifying the sleep condition (normal vs deprived) and the eye state (open vs closed) from electroencephalography (EEG) remains underexplored. We address this four-class problem with TinyCNNDeep, a lightweight convolutional neural network that combines residual learning with a Squeeze-and-Excitation (SE) attention module. We convert short multi-channel EEG segments from five physiologically relevant channels (Fp1, Fp2, O1, Oz, O2) into 224x224 grayscale images through per-channel Z-score normalization, min-max scaling, and center padding, enabling 2D convolutions to jointly model inter-channel and temporal structure. On a 35-subject dataset recorded under normal-sleep and sleep-deprivation sessions, TinyCNNDeep attains a subject-wise mean accuracy of 83.69%, outperforming the strongest baseline (Random Forest with combined time-frequency features, 47.66%) by 36.03 percentage points, while three established EEG architectures (EEGNet, ShallowConvNet, DeepConvNet) operate near chance. Per-subject analysis quantifies inter-subject variability, and confusion-matrix inspection shows that residual misclassifications concentrate between eyes-closed states across sleep conditions. These results indicate that an image-based EEG representation paired with residual feature extraction and channel attention provides an accurate and computationally efficient framework for multiclass sleep-related EEG classification under a minimal electrode configuration.

---


### 71. [DanceDuo: Bridging Human Movement and AI Choreography](https://arxiv.org/abs/2606.26507)

**<font color=#1a73e8>作者：</font>** Gia-Cat Bui-Le, Tuong-Vy Truong-Thuy, Hai-Dang Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In recent years, advancements in deep learning and generative models have revolutionized music-driven dance generation. This paper introduces a novel platform, namely DanceDuo, leveraging diffusion models to generate AI-choreographed dance sequences synchronized with a variety of music genres, to encourage dancing practice. The system allows users to interact with AI by selecting music tracks, humanoid models, and importing personal dance videos for comparison, fostering a rich and engaging user experience. DanceDuo not only offers dance generation but also integrates human pose estimation models to provide users with insightful comparisons of their own performances with AI-generated sequences. We conducted a comprehensive user study, revealing that users found the interface intuitive, with particular praise for the dance comparison feature. Our DanceDuo contributes significantly to the integration of AI in dance choreography, offering novel avenues for both recreational and professional applications.

---


### 72. [Budget-Aware Keyboardless Interaction](https://arxiv.org/abs/2606.26508)

**<font color=#1a73e8>作者：</font>** Quang-Thang Nguyen, Gia-Phuc Song-Dong, Minh-Triet Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interacting with computers typically relies on traditional input devices such as keyboards, mice, and monitors, which can be cumbersome for users seeking greater mobility. Virtual keyboards have been explored to address these limitations, but they often involve complex setups or expensive equipment. This paper proposes a novel virtual keyboard system that leverages only a standard camera and a paper with a printed keyboard layout. Unlike previous methods requiring complex calibration or special lighting conditions, our approach can work on standard environment using modern computer vision technologies. Combining modern segmentation and detection models with traditional image processing algorithms, we efficiently identify the keyboard region. Touch detection is performed using an algorithm analyzing the color of the user's fingernail. Experiments demonstrated a promising results our proposed solution of keyboard and keystroke detection for practical applications. Participants attended our user study also found the proposed system interesting.

---


### 73. [Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge](https://arxiv.org/abs/2606.26511)

**<font color=#1a73e8>作者：</font>** Neeraj Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time. When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity. The agent then either abstains or serves the superseded fact. We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), as contradictions are often more embedding-similar to the original than rephrased duplicates.
We present MemStrata, a retrieval memory maintaining temporal validity. It stores facts like RAG, preserving static recall, but when a fact's value is contradicted, a deterministic (subject, relation, object) supersession rule retires the stale value in a bi-temporal ledger - with no similarity threshold and no LLM call. Across six benchmarks run locally with a 7B model, MemStrata ties RAG on static knowledge and reaches 0.95-1.00 accuracy on evolving knowledge (where RAG reaches 0.20-0.47). The central result is the stale-fact-error rate: when required to answer, RAG serves superseded values 15-40% of the time; MemStrata drives this to ~0%, a failure class RAG cannot avoid. MemStrata achieves this at retrieval latency (~2.1s) versus ~16-18s for LLM-reranking baselines. We release the harness, datasets, and a marker-free evaluation protocol for memory under knowledge evolution.

---


### 74. [Forget, Anticipate and Adapt: Test Time Training for Long Videos](https://arxiv.org/abs/2606.26515)

**<font color=#1a73e8>作者：</font>** Rajat Modi, Sebastian Noel, Xin Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test Time Training (TTT) is a mechanism in which a model adapts to an incoming test-sample by performing some self-supervised (SSL) task and updating its weights even during inference. This procedure does not require labels at test-time. This paper focuses on TTT for long-videos. A major concern with existing approaches is: 1) they perform TTT updates using a sliding window containing frames in the past, whose compute increases linearly with the size of window. This becomes computationally intractable when the videos are hours long. 2) TTT is performed even when temporally close frames look similar, thereby consuming a lot of compute.
We present the Frame Forgetting Network (FFN) that: 1) operates on only three frames within the sliding window, namely the frame that exits, the current frame and the frame after that. The model still manages to retain temporal context and work for hours long-videos; 2) mathematically define a surprise metric: how much new information the incoming frame contains with respect to the past seen frame. This facilitates determining how to modify the effective window size during TTT and constitutes the core mechanism of an adaptive windowing algorithm. Additionally, we curate a dataset EpicTours containing up to 3 hour long videos of walking city-tours, whereas earlier datasets on this problem were only 5 min long. We demonstrate FFNs empirical effectiveness on dense-segmentation, video classification tasks, generalization to depth-estimation, and multi-hour long videos.

---


### 75. [NeuraDock Visual Cognitive Load Agent Tutorial: A Quality-Gated Open-Source EEG Workflow for Alpha Dynamics and Real-Time Applications](https://arxiv.org/abs/2606.26518)

**<font color=#1a73e8>作者：</font>** Zhiyuan Xu, Yueqing Dai, Junling Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This tutorial paper provides a step-by-step, reproducible walkthrough of NeuraDock Agent, an open-source EEG agent focused on Alpha dynamics and visual cognitive-load analysis. The goal is practical: a reader should be able to install the agent, run EEG preprocessing and quality control, generate Alpha dynamics figures, perform within-subject Rest/Task visual cognitive-load comparison, run the public mini-dataset analyses and compare them with the reference validation summary, start an online dashboard, call the real-time API from an external application, and use the LLM interpretation layer to explain quality risks. Existing EEG toolkits provide excellent offline analysis, but assembling a real-time, quality-gated cognitive-load pipeline often requires manually bridging acquisition, custom QC, Alpha feature extraction, and a web API; this tutorial closes that offline-to-online gap. The tutorial uses a quality-gated workflow: downstream Alpha and workload metrics are computed only after preprocessing and QC gating rather than directly from raw EEG. In the included mini-dataset validation, the agent processed 18 recordings, generated 10 within-subject comparisons, observed task-related posterior Alpha suppression in 7 of 10 contrasts, estimated initial evidence of within-subject repeatability, and benchmarked local online API latency. The tutorial is intended for researchers, developers, and applied teams who want a transparent path from EEG files to real-time visual cognitive-load prototypes.

---


### 76. [Multipath Adaptive Gated Bottleneck Latent ODE with Raman Data Fusion for Cell Culture Process Forecasting](https://arxiv.org/abs/2606.26520)

**<font color=#1a73e8>作者：</font>** Johnny Peng, Thanh Tung Khuat, Ellen Otte 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mammalian cell-culture processes underpin the manufacture of many biopharmaceuticals, yet keeping a run on track is hard: critical process parameters drift over days, and an off-specification trend is often confirmed too late to intervene. Early-stage, multi-day forecasts could enable timely adjustment of feeding, sampling, and control, but bioprocess forecasting is challenging because measurements are sparse and irregularly sampled, operating conditions are heterogeneous across cell lines and media, and runs with near-identical early behaviour can diverge into different futures. We propose an adaptive framework combining a Gated Bottleneck Latent Ordinary Differential Equation (GB-Latent ODE) with Multi-Path Just-In-Time Fine Tuning (MP-JIT-FT). The GB-Latent ODE augments the stan dard Latent ODE with learnable variable-wise gating and a mask-aware bottleneck that compress high-dimensional sparse inputs, improving learning under limited data. Given a partially observed run, MP-JIT-FT retrieves similar historical trajectories, clusters the local neighbourhood into candidate regimes, and fine-tunes a separate model per regime to produce multiple plausible paths, each with a reconstruction-based confidence score, not a single averaged forecast. We further fuse Raman spectroscopy data: a machine-learning soft sensor turns dense Raman spectra into pseudo-observations that enrich the sparse offline measurements for more robust training. On 38 fed-batch 5L bioreactor runs spanning 14 conditions, MP-JIT-FT with Raman fusion achieves the best average rank and outperforms a global Latent ODE baseline on 8 of 9 target variables. Using local-divergence metrics, we show the multi-path gains are largest when locally similar prefixes diverge, whereas Raman fusion helps most when early dynamics are representative of later behaviour.

---


### 77. [Assessing Post-Reform Changes in Risk Disclosure Quality with a Multidimensional Text Analysis Approach](https://arxiv.org/abs/2606.26522)

**<font color=#1a73e8>作者：</font>** Nobuhiro Aikawa, Mitsuo Yoshida  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While corporate narrative disclosures provide crucial information to capital markets, comprehensively evaluating their qualitative changes over time remains challenging. Narrative text is inherently multidimensional, meaning that an improvement in one textual dimension often occurs alongside changes in others. To capture these underlying dynamics, we propose a longitudinal text analysis approach combining Japanese-language NLP metric extraction with paired testing, shift function analysis, and inter-metric correlation. Our framework extends prior indicator sets by incorporating a cross-section relevance indicator to measure topical alignment between risk disclosures and management strategies. Applying this approach to evaluate Japan's 2019 disclosure reforms, we analyze 19,770 firm-year observations over a 10-year period (FY2015-FY2024). The joint analysis reveals complex shifts in disclosure patterns that are frequently masked by conventional single-indicator methods. Specifically, we find that while disclosure volume increased substantially, it was accompanied by a decline in readability. Furthermore, although the overall information structure improved, specific descriptive quality stagnated, and the degree of adaptation varied across market segments.

---


### 78. [Radical AI Interpretability](https://arxiv.org/abs/2606.26523)

**<font color=#1a73e8>作者：</font>** Daniel A. Herrmann, Benjamin A. Levinstein  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We develop a framework for interpreting AI systems as agents, drawing on the philosophical tradition of radical interpretation and the tools of mechanistic interpretability. The core question is: given the computational facts about a system, how do we solve for its beliefs, desires, and meanings? This matters increasingly for safety. We want to be able to trust the systems we deploy, whether by understanding their goals or, more modestly, by reliably detecting deception. Interpretability researchers are building tools to read beliefs and desires off a model's internals, but there is no settled account of when such a tool has succeeded. This book supplies one. We propose criteria on both representationalist and interpretationist approaches, and tie each to tests current interpretability methods can carry out. A central lesson is that these attributions cannot be made piecemeal. Beliefs, desires, and the propositional structure they presuppose are jointly constrained, and a method that fixes one while measuring the others inherits whatever distortions that introduces. This holism becomes pressing for AI systems, which may not share the interpreter's concepts. However, it also provides leverage: a system's attitudes constrain its propositional structure, that structure constrains which attitudes can be attributed, and mechanistic interpretability can help us measure both.

---


### 79. [VIGIL: Runtime Enforcement of Behavioral Specifications in AI Agent Skills](https://arxiv.org/abs/2606.26524)

**<font color=#1a73e8>作者：</font>** Ying Li, Yanju Chen, Hongbo Wen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic systems increasingly act through third-party skills, allowing model-generated decisions to affect files, communication channels, and cyber-physical devices. These skills often include natural-language specifications that define access permissions, disclosure limits, execution privileges, and required preconditions. Although such specifications describe the intended boundaries of skill behavior, they do not by themselves provide executable runtime enforcement. Enforcing them raises a contextual granularity challenge: even when a policy is written for a particular task context, a monitor must still decide which events to observe, what state to retain, how far across the execution to reason, and where to intervene. Choosing the wrong granularity can either block benign executions or miss violations that emerge only across multiple actions. Most existing enforcement mechanisms, however, assume a fixed event model or enforcement point.
In this work, we present VIGIL, an end-to-end runtime enforcement framework for agentic systems. VIGIL checks an agent's actual execution trace against behavioral policies from skill specifications, operator-defined constraints, and global rules spanning multiple skills. To make such policies executable, VIGIL introduces a policy language that captures context-specific enforcement requirements over agent-tool events, including temporal dependencies, argument constraints, and value-flow conditions. The language is paired with symbolic evaluation rules that translate policies into SMT constraints over finite traces, allowing VIGIL to detect violations that depend on event order, argument relationships, or cross-call value flow rather than relying on fixed single-call filters. On real LLM-agent runs spanning office-document, operational, and engineering tasks, VIGIL detects policy violations with over 95% recall and a false-positive rate below 10%.

---


### 80. [Theory-Scale Auto-Formalization of Logics for Computer Science](https://arxiv.org/abs/2606.26525)

**<font color=#1a73e8>作者：</font>** Yuming Feng, Frederick Pu, One An 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auto-formalization is critical for scalable formal verification, but existing progress largely focuses on isolated statements, while theory-scale auto-formalization, which coherently translates hundreds of interdependent definitions, lemmas, and theorems, remains open due to challenges in consistency, faithfulness, scalability, and correctness. In this paper, we introduce LCS-Bench, a stand-alone, theory-scale benchmark based on Logics for Computer Science. LCS-Bench is built through a novel semi-automated agentic pipeline that leverages concept graphs, formal signature planning, issue tracking, sorry-filling with counter-example search, complemented by faithfulness review from human experts. The resulting artifact covers 327 textbook items, over 4,076 Lean declarations, and more than 85K lines of Lean code. The dataset supports broad evaluation through a data engine that automatically derives five tracks of evaluation benchmarks, measuring different aspects of auto-formalization and theorem-proving capabilities. We also introduce a novel evaluation protocol featuring definitional equivalence checkers, enabling more fine-grained and faithful assessment. Through extensive evaluation on 14 models, we demonstrate that (1) LCS-Bench is of high quality, consistent, and faithful; (2) the benchmark is challenging, with state-of-the-art models achieving only 20.1% on auto-formalization tasks; and (3) our analysis reveals key findings regarding theory-scale auto-formalization and suggests promising directions for future work.

---


### 81. [Sample-efficient Transfer Reinforcement Learning via Adaptive Reward Shaping and Policy-Ratio Reweighting Strategy](https://arxiv.org/abs/2606.26527)

**<font color=#1a73e8>作者：</font>** Wenjie Huang, Yang Li, Jingjia Teng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transfer learning improves policy learning efficiency by reusing knowledge from source tasks, providing a feasible paradigm for safe and efficient autonomous highway lane changing decision-making. Existing methods frequently encounter transfer mismatch induced by distribution shifts between source and target domains, leading to training oscillation and performance decline. Besides, target domain adaptation depends on exploratory interactions, which struggles to guarantee training safety in safety-critical lane changing cases. To tackle these limitations, this paper proposes a safe transfer reinforcement learning framework for autonomous highway lane changing. First, we design an adaptive teacher intervention mechanism based on instantaneous safety cost to restrain risky exploration and fade intervention strength progressively, with theoretical analysis on return bounds for mixed behavior policy. This intervention also produces dual-source samples for joint training. Second, a teacher-guided safe transfer module embeds action evaluation information of teacher policy into student learning via reward shaping to boost training safety and efficiency, with teacher guidance decaying as policy safety rises. Third, a teacher-guided weighted optimization mechanism adjusts sample weights in policy optimization using a likelihood ratio factor to stabilize transfer performance. Experiments under varied traffic densities and validations on real-world NGSIM dataset reveal that our method surpasses baseline approaches by over 52.2% in safety and 5.0% in learning efficiency. Results verify the efficacy and robustness of our safety-aware transfer strategy for autonomous highway lane changing under various traffic conditions.

---


### 82. [TESLA-for-5G: Broadcast Authentication for 5G Networks Using TESLA](https://arxiv.org/abs/2606.26528)

**<font color=#1a73e8>作者：</font>** Subin Song, Michael K. Reiter, Taekyoung Kwon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> 5G base stations broadcast unauthenticated system information (SI) that every user equipment (UE) reads during cell selection. This enables attackers to broadcast forged SI from a fake base station (FBS), deceiving UEs into camping on it. Prior approaches require UEs to authenticate System Information Block 1 (SIB1) using digital signatures. This necessitates computation-heavy verification for every SIB1 reception, imposing a significant burden on resource-constrained UEs. We propose TESLA-for-5G (TF5), a broadcast authentication protocol for 5G SIB1 that combines TESLA with GG09 Schnorr-like identity-based signatures (IBS). In the steady state, TF5 enables UEs to authenticate each SIB1 message using a symmetric MAC and delayed key disclosure, eliminating the need for per-message digital signatures. Initial trust is bootstrapped during cell entry using a lightweight GG09 IBS over the TESLA parameters, avoiding certificate distribution overhead. We formally verify TF5 in Tamarin under a Dolev-Yao adversary and demonstrate its favorable computation, communication, and storage costs through both an implementation on the OpenAirInterface 5G stack and trace-driven analysis.

---


### 83. [The Inattentional Gap: Task-Conditioned Language and Vision Models Omit the Safety-Critical Signals They Can Otherwise Report](https://arxiv.org/abs/2606.26529)

**<font color=#1a73e8>作者：</font>** Kwan Soo Shin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI safety is evaluated by how reliably a model detects the hazards it is told to find, yet accidents often arise from the hazard no one specified. We show that conditioning a language or vision model on a narrow task suppresses its reporting of co-present, safety-critical signals it can otherwise report, a machine analogue of human inattentional blindness arising from a different mechanism. Across radiology and driving text scenarios and chest-radiograph vision tasks, suppression appeared in every model tested, did not diminish with scale, persisted in a reasoning model, and varied more by model family than by size, while the same models reported these signals at substantially higher rates when unconstrained. We name this dissociation the Inattentional Gap and argue that it decouples measured benchmark safety from real-world safety: a system can score near-perfectly on the hazards an evaluation specifies while remaining blind to those that cause harm.

---


### 84. [CascadeFormer: Depth-Tapered Transformers Motivated by Gradient Fan-in Asymmetry](https://arxiv.org/abs/2606.26538)

**<font color=#1a73e8>作者：</font>** Huzama Ahmad, Cao Viet Hai Nam, Se-Young Yun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Transformers are composed of uniformly stacked residual blocks, yet their deepest layers often add little value. We present two efficiency methods that exploit this asymmetry. CascadeFormer tapers width with depth to match the uneven information flow across layers, achieving comparable perplexity to a uniform baseline at the same training budget while reducing latency by 8.6% and increasing throughput by 9.4%. CascadeFlow Pruning removes layers using accumulated training gradients, with no post hoc analysis. It outperforms standard heuristics on perplexity and rank-stability and stays competitive on downstream accuracy. To motivate these methods, we propose Gradient Fan-in Asymmetry (GFA) as a structural account of why deeper layers contribute less. In Pre-LayerNorm residual stacks, the gradient at a layer is the sum of an identity path and all downstream functional paths, producing a gradient fan-in that decays linearly with depth (and quadratically under deep supervision), yielding richer gradients for early layers and sparser ones for later layers. We provide correlational and interventional evidence for GFA on models trained from scratch up to 1.2B parameters. Across Transformers and ResNets, accumulated training gradients follow the theoretical fan-in and are associated with post hoc layer importance. Two interventions point to structure rather than magnitude as the bottleneck: equalizing per-layer gradient norms does not restore late-layer value, while increasing downstream path counts via parameter-shared repetition restores and elevates it. Whether gradient magnitude proxies fan-in beyond high-rank regimes, and how these dynamics behave at the 100B+ scale, remain open questions.

---


### 85. [PMDformer: Patch-Mean Decoupling Information Transformer for Long-term Forecasting](https://arxiv.org/abs/2606.26549)

**<font color=#1a73e8>作者：</font>** Ao Hu, Liangjian Wen, Jiang Duan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term time series forecasting (LTSF) plays a crucial role in fields such as energy management, finance, and traffic prediction. Transformer-based models have adopted patch-based strategies to capture long-range dependencies, but accurately modeling shape similarities across patches and variables remains challenging due to scale differences. To address this, we introduce patch-mean decoupling (PMD), which separates the trend and residual shape information by subtracting the mean of each patch, preserving the original structure and ensuring that the attention mechanism captures true shape similarities. Futhermore, to more effectively model long-range dependencies and capture cross-variable relationships, we propose Trend Restoration Attention (TRA) and Proximal Variable Attention (PVA). The former module reintegrates the decoupled trend from PMD while calculating attention output. And the latter focuses cross-variable attention on the most relevant, recent time segments to avoid overfitting on outdated correlations. Combining these components, we propose PMDformer, a model designed to effectively capture shape similarity in long-term forecasting scenarios. Extensive experiments indicate that PMDformer outperforms existing state-of-the-art methods in stability and accuracy across multiple LTSF benchmarks. The code is available at this https URL.

---


### 86. [PhyEditBench: A Real-World Multi-Stage Benchmark for Physics-Aware Image Editing](https://arxiv.org/abs/2606.26551)

**<font color=#1a73e8>作者：</font>** Shengbin Guo, Shaokang He, Chaoyue Meng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While instruction-based image editing, enabled by multi-modal generative models, has advanced significantly, existing benchmarks lack a comprehensive evaluation of physics-based reasoning, a critical capability for handling real-world scenarios. To address this, we introduce PhyEditBench, a benchmark designed to assess the physical understanding of editing models. Guided by a hierarchical taxonomy, we establish 4 primary classes and 12 subclasses. It comprises 238 high-quality, high-resolution, real-world instances meticulously extracted from videos to capture authentic physical dynamics, alongside 35 synthetic Anti-Physics instances. Our empirical analysis of current SOTA editing methods exposes substantial limitations in their physics-based reasoning. We further propose a training-free baseline named PhyWorld that uses test-time scaling and a latent reduction strategy. PhyWorld outperforms comparable models and suggests that the video generation process can effectively serve as a reasoning mechanism for image editing. The project page is available at this https URL.

---


### 87. [Coarse-to-Fine: A Hybrid Self-Supervised Method for Non-rigid 3D Shape Matching](https://arxiv.org/abs/2606.26557)

**<font color=#1a73e8>作者：</font>** Feifan Luo, Ting Li, Zhao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-rigid 3D shape matching is a fundamental task in computer vision and graphics. In this paper, we propose a hybrid self-supervised method based on a coarse-to-fine strategy, which ensures consistency between the coarse mapping and the refined correspondence produced by our refinement module. The architecture features a dual-branch design, consisting of two symmetric functional map learning streams: one based on the Laplacian basis and the other utilizing the elastic basis. Extensive experiments show that our approach not only maintains computational efficiency, but also achieves state-of-the-art performance across a variety of challenging scenarios, including non-isometric deformations and topological noise. Finally, we rigorously demonstrate that contrastive energies promote feature discrimination. Furthermore, integrating these energies with existing methods yields consistent improvements, validating the overall efficacy of our approach. Our code is available at this https URL.

---


### 88. [SpaceRipple: Lightweight Semantic Delivery for Mission-Oriented LEO Earth Observation Satellite Networks](https://arxiv.org/abs/2606.26559)

**<font color=#1a73e8>作者：</font>** Ziyi Yang, Hao Yuan, Yunxiang Yi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth observation satellite networks generate massive volumes of high-resolution imagery, whereas inter-satellite and downlink resources remain limited. In many time-sensitive missions, ground users require mission-relevant semantic information rather than a full raw-image downlink. This paper proposes SpaceRipple, a lightweight framework for mission-oriented semantic delivery and on-board processing in Earth observation satellite networks. A sensing satellite performs adaptive compression and metadata generation to reduce inter-satellite traffic, while an edge computing satellite restores the received representation and extracts task-relevant semantic information. Unlike fidelity-driven image transmission, SpaceRipple coordinates compression, forwarding, restoration, and semantic inference within a collaborative pipeline, enabling semantic-oriented delivery instead of pixel-level image delivery. A compression-aware MoE enhancement module is further introduced to improve robustness under degraded visual inputs. Experimental results show that SpaceRipple achieves favorable reconstruction quality, improved semantic detection performance, and substantial bandwidth savings, demonstrating its potential for efficient and reliable Earth observation under constrained satellite-network resources.

---


### 89. [Erase-then-Delta Attention: Decoupling Erase and Write Addresses in Delta-Rule Linear Attention](https://arxiv.org/abs/2606.26560)

**<font color=#1a73e8>作者：</font>** Xiao Li, Chengruidong Zhang, Hao Luo 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Delta-rule linear attention improves recurrent memory updates by correcting what is already stored at the current write address before writing new content. However, the active correction is still anchored to that same write address. As a result, stale information stored at a different address cannot be actively removed before new content is written elsewhere. We propose Erase-then-Delta Attention (EDA), a memory update rule that decouples where to erase from where to write. The key insight is that recurrent memory models should not only correct the current write, but also selectively suppress outdated memory at an independently chosen address. Concretely, our method first applies a targeted erase step along a learned erase direction, and then performs the standard delta-style corrective write along the current write direction. This preserves the corrective behavior of delta-rule updates while expanding their memory-management capacity. Language-model pretraining experiments across dense 2.5B and MoE 25B-A2.8B model families show that EDA performs best in both settings. The gain persists after 80B-token long-context midtraining of the MoE models, where EDA also performs best in long-context evaluations from 4k to 128k contexts. A compact update analysis and memory-state probes suggest why: EDA keeps the delta-rule corrective write intact while allocating an additional cleanup path most strongly when passive decay is weak. These results suggest that recurrent memory models should decide not only what to write, but also what stale information to erase and where.

---


### 90. [Explainable Ensemble-Based Machine Learning Models for Detecting the Presence of Cirrhosis in Hepatitis C Patients](https://arxiv.org/abs/2606.26561)

**<font color=#1a73e8>作者：</font>** Abrar Alotaibi, Lujain Alnajrani, Nawal Alsheikh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hepatitis C is a liver infection caused by a virus, which results in mild to severe inflammation of the liver. Over many years, hepatitis C gradually damages the liver, often leading to permanent scarring, known as cirrhosis. Patients sometimes have moderate or no symptoms of liver illness for decades before developing cirrhosis. Cirrhosis typically worsens to the point of liver failure. Patients with cirrhosis may also experience brain and nerve system damage, as well as gastrointestinal hemorrhage. Treatment for cirrhosis focuses on preventing further progression of the disease. Detecting cirrhosis earlier is therefore crucial for avoiding complications. Machine learning (ML) has been shown to be effective at providing precise and accurate information for use in diagnosing several diseases. Despite this, no studies have so far used ML to detect cirrhosis in patients with hepatitis C. This study obtained a dataset consisting of 28 attributes of 2038 Egyptian patients from the ML Repository of the University of California at Irvine. Four ML algorithms were trained on the dataset to diagnose cirrhosis in hepatitis C patients: a Random Forest, a Gradient Boosting Machine, an Extreme Gradient Boosting, and an Extra Trees model. The Extra Trees model outperformed the other models achieving an accuracy of 96.92%, a recall of 94.00%, a precision of 99.81%, and an area under the receiver operating characteristic curve of 96% using only 16 of the 28 features.

---


### 91. [Co-Designing Community-Centered AI Education for Adults: A Midwestern Case Study](https://arxiv.org/abs/2606.26565)

**<font color=#1a73e8>作者：</font>** Yao Lyu, Leonymae Aumentado, Holden Winton 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) education is increasingly important, yet adults outside higher education receive less attention. We report a case study of an AI education session with 54 adults (48 in-person and 6 virtual) in a predominantly African American community on the east side of a major Midwestern city. We ask: "What does AI education for adults outside formal educational systems look like in practice?" and "What does this AI education session reveal about AI literacy at the community level?" Through a co-designed session developed with community partners, we found that concerns about AI persisted but shifted to specific, locally grounded questions about AI design and deployment. We also discuss AI literacy from a community capacity perspective and argue for AI literacy frameworks grounded in local community contexts that strengthen community capacity.

---


### 92. [Zero-shot Tweet-Level Stance Detection Enhanced by External Knowledge and Reflective Chain-of-Thought Reasoning](https://arxiv.org/abs/2606.26571)

**<font color=#1a73e8>作者：</font>** Yiju Huang, Wenxian Wang, Lijun Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Zero-shot tweet-level stance detection confronts two primary challenges: (1) mitigating the context sparsity inherent in short texts, and (2) establishing the relevance between implicit targets and textual content. While existing methods primarily focus on incorporating external knowledge, they neglect the intrinsic semantic cues embedded within key intra-textual entities. Furthermore, current models exhibit limited capability in determining the relevance of unseen targets to the given text, thereby struggling to differentiate between "neutral" and "irrelevant" stance labels. To address these issues, we first construct a four-class, multi-topic Japanese tweet dataset. To our knowledge, this is the first Japanese tweet-level dataset for stance detection. We then propose KIRP, a zero-shot stance detection framework. It integrates external knowledge with entity reorganization for data augmentation and employs prompt chaining for reasoning. Specifically, the framework incorporates knowledge graphs to supplement and reorganize key textual entities, while reflective Chain-of-Thought (CoT) reasoning extracts and validates implicit targets. To better distinguish "neutral" from "irrelevant" labels, we adopt stance-aware contrastive learning to capture discriminative features and design a three-layer iterative prototype network for fine-grained classification. Experimental results on SemEval-2016, WT-WT, and KIRP-D show that KIRP achieves state-of-the-art performance. KIRP obtains F1 scores of 84.05% (three-class) on SemEval-2016, and 84.99% and 79.18% (four-class) on WT-WT and KIRP-D, respectively.

---


### 93. [Revisiting Action Factorization for Complex Action Spaces](https://arxiv.org/abs/2606.26574)

**<font color=#1a73e8>作者：</font>** Timothy Flavin, Sandip Sen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world control problems involve hybrid discrete-continuous action spaces. For example, steering and signaling in autonomous driving, and aiming and firing in robotics or video-games. Despite real-world hybrid factorization and reinforcement learning framework support for complex action spaces (e.g., Gymnasium, PettingZoo, TorchRL, SeedRL, Mujoco, etc), the default environments within those frameworks often implement uniform action space configurations (LunarLander, Walker2D, Cheetah, SMAC, SUMO, Ant, Atari). Landmark hybrid-action benchmarks (RoboCup 2D HFO, SC2LE, Platform, CARLA, etc) are mostly heavyweight or archival implementations originating from papers which test one or a small number of competing factorization methods on one kind of control. This article provides a cross-sectional study of factorization methods [independent networks, shared encoder, VDN, QPLEX, Joint, Auto-Regressive] on each of three families of algorithms [PPO, SAC, DQN] across three action spaces [discretized, hybrid, continuous] over four lightweight environments [Platform, hybrid-LunarLander, Hybrid-Shoot, CoopPush]. Accounting for some invalid pairings such as joint-continuous, we are left with 220 configurations to analyze each method. We provide two new C++ parallel gymnasium and petting-zoo compliant environments [CoopPush, Hybrid-Shoot] to isolate particular challenges such as state-dependent inter-action dependence. Finally, we introduce VDN-PPO and PPO-MIX which use a branching critic to assign credit to multi-headed PPO. These variants out-perform all other tested PPO factorizations. Our results suggest that branching dueling architectures balance compute and performance most effectively, with Auto-Regressive actions reaching the highest performance overall and native continuous SAC outperforming discrete and hybrid algorithms, albiet both at increased computational cost.

---


### 94. [An exploratory behavioral and electroencephalographic study of artificial intelligence-assisted learning modes in high school students](https://arxiv.org/abs/2606.26579)

**<font color=#1a73e8>作者：</font>** Kashika Khurana, Ally Liew  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As artificial intelligence (AI) is rapidly integrating into education, concerns have emerged regarding its potential implications on cognitive engagement and problem-solving behavior. However, existing research largely treats AI exposure as a binary condition (AI vs. no-AI), with limited differentiation between interaction modalities and post-exposure effects. This study investigates whether distinct AI interaction modes (Tutor, Collaborator, Solver) influence frontal EEG spectral activity. Electroencephalography (EEG) data and quantified behavioral metrics were recorded from 48 study participants (24 males, 24 females; ages 14-18) across two counterbalanced quizzes in a within-subject design. Statistical analyses included Friedman tests, repeated-measures ANOVA, paired t-tests, and effect size calculations. Behavioral changes were mathematically analyzed in an observation matrix of three characteristics -Initiation, Processing, and Stress-measured on an ordinal scale. Each mode showed significant differences in all three behavioral measures. Descriptive EEG patterns in AI interaction mode were observed, and the possibility of short-term carryover effects of AI was explored. Although the EEG data did not reach statistical significance, the patterns observed across the three AI interaction modes warrant further investigation. This study provides preliminary behavioral evidence and investigative electrophysiological observations, exploring possible AI-interaction-mode-based differences in neural activity and behavior, while establishing a replicable framework for future human-AI interaction studies.

---


### 95. [A Multi-Level Validation and Traceability Framework for AI-Generated Telescope Scheduling Decisions](https://arxiv.org/abs/2606.26585)

**<font color=#1a73e8>作者：</font>** Hengchu Xiao, Chuanjun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the gradual introduction of AI into telescope scheduling, AI-based decision-making has shown advantages in handling complex multi-constraint problems. However, its outputs often suffer from inconsistent data references, reasoning errors, and non-executable decisions, limiting applicability in high-reliability observational tasks. In this work, we propose a multi-level validation and traceable reasoning framework that performs systematic reliability verification of AI-generated decisions prior to execution, and enables explicit representation of the reasoning process to support traceable decision-making. The framework integrates data reference validation, logical consistency checks, and observational and instrumental constraint verification to filter and correct invalid decisions. It also introduces atomic reasoning units and their dependency relationships, representing scheduling decisions as a sequence of interconnected reasoning steps that support error localization and post hoc analysis. Experiments show that the framework improves executability and reliability of AI scheduling and reduces loss of transient opportunities. In particular, feedback correction and structured validation of reasoning steps enhance the ability to repair and block erroneous decisions, especially in complex scenarios. Compared with pure AI methods, the framework-enhanced approach maintains flexibility while substantially improving reliability and executability. These results demonstrate a feasible and verifiable pathway for applying AI to high-reliability astronomical observation scheduling.

---


### 96. [LogicIR: Logic Gate Networks for Image Restoration](https://arxiv.org/abs/2606.26609)

**<font color=#1a73e8>作者：</font>** Hongjae Lee, Myungjun Son, Jaeseong Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration aims to reconstruct high-quality images from degraded low-quality inputs. As the computational demands of image restoration models continue to rise, there is growing interest in lightweight architectures optimized for fast and efficient inference. Logic gate networks (LGNs), which operate using fundamental logic operations such as NAND and XOR, have recently emerged as a promising direction for achieving highly efficient computation. However, their potential remains largely untapped in the domain of image restoration. In this work, we introduce LogicIR, the first LGN specifically designed for image restoration tasks. LogicIR incorporates a UNet-inspired architecture composed entirely of logic gates. In addition, we propose a differentiable bit decoding layer and an index shuffling mechanism that improves information propagation across logic gates. Experimental results across multiple image restoration benchmarks demonstrate that LogicIR achieves strong performance with significantly reduced computational cost, establishing LogicIR as a viable and efficient alternative for image restoration. The source code is available at this https URL

---


### 97. [TaskTok: Delving into Task Tokens for Task-driven Image Restoration](https://arxiv.org/abs/2606.26615)

**<font color=#1a73e8>作者：</font>** Hongjae Lee, Sojung Kang, Jaeseong Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While traditional image restoration focuses on perceptual quality, Task-Driven Image Restoration (TDIR) aims to maximize the performance of downstream high-level vision tasks. Recent approaches leveraging generative priors have shown promise for TDIR; however, they typically suffer from computational inefficiency and potential semantic alteration by indiscriminately updating all latent tokens. In this paper, we posit that not all visual information is equally important for machine perception. Through an analysis of the latent token space, we observe that task-relevant cues are unevenly distributed across the token sequence, exhibiting index-wise specialization. This suggests that selectively refining a subset of tokens can be sufficient for task-driven objectives. Leveraging this insight, we propose TaskTok, a novel framework that selectively restores only task-relevant tokens via a learnable token switch and a lightweight token refinement module. Extensive experiments across image classification, semantic segmentation, and object detection demonstrate that TaskTok significantly enhances task performance with high computational efficiency. The source code is available at this https URL

---


### 98. [Sketched Linear Contrastive Learning: Approximation, Optimization, and Statistical Scaling](https://arxiv.org/abs/2606.26617)

**<font color=#1a73e8>作者：</font>** Ziyan Chen, Zhongzhu Zhou, Ding-Xuan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws describe how learning performance varies with model size, data size, and compute. While recent theoretical work has established scaling laws for sketched linear regression, much less is understood for contrastive representation learning. In this paper, we study a sketched linear model for contrastive learning under a paired Gaussian latent-variable setup. The learner observes only sketched views of two correlated variables and trains a bilinear contrastive score by full-batch empirical gradient descent. We analyze a Gaussian-negative quadratic contrastive surrogate under aligned power-law spectra and a contrastive source condition, where we derive a risk decomposition into irreducible risk, approximation error, GD bias, GD variance, and a cross term. The cross term is controlled by the bias and variance and therefore does not affect the upper-bound scaling. Our main theorem gives an explicit scaling law with respect to sketch dimension $M$, sample size $N$, and effective optimization horizon $L_{\mathrm{eff}}\gamma$. Compared with standard linear-regression scaling laws, the contrastive setting must learn interactions between two views, and this changes how optimization and finite-sample noise scale with model size, data, and training time. This provides a first theoretical step toward understanding scaling behavior in contrastive learning and gives guidance for balancing model size, data, and optimization compute.

---


### 99. [Discovering Millions of Interpretable Features with Sparse Autoencoders](https://arxiv.org/abs/2606.26620)

**<font color=#1a73e8>作者：</font>** XinYang He, Wei Wang, Bing Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) have emerged as a powerful tool for decomposing superposed language model representations into sparse and interpretable features. However, training SAEs is computationally expensive, and available open-source SAE models remain limited. In this work, we introduce \textbf{Qwen3-Instruct SAE}, a comprehensive suite of SAEs trained on the Qwen3 instruction-tuned model family, covering Qwen3-1.7B, Qwen3-4B, and Qwen3-8B. For Qwen3-1.7B and Qwen3-4B, we train layer-wise SAEs at three key activation sites: residual streams, MLP outputs, and attention outputs. For Qwen3-8B, we train SAEs on a subset of residual stream layers. We systematically evaluate these SAEs using both activation-level reconstruction metrics and model-level recovery metrics, revealing distinct sparsity--fidelity trade-offs across layers and components. Finally, we demonstrate the utility of Qwen3-Instruct SAE through a refusal-steering case study, showing that selected SAE features can causally steer instruction-tuned Qwen3 models toward refusal behavior. Our release provides a practical resource for studying sparse representations, feature-level mechanisms, and behavioral interventions in instruction-tuned language models

---


### 100. [Temporally Consistent Label Interpolation for Robust Surgical Multi-Task Learning under Challenging Conditions](https://arxiv.org/abs/2606.26634)

**<font color=#1a73e8>作者：</font>** Garam Kim, Juyoun Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective multi-task learning for surgical scene understanding is fundamentally hindered by annotation granularity mismatch; temporal workflow tasks such as phase recognition, step recognition and anticipation benefit from dense frame-level supervision, whereas pixel-level spatial tasks including instrument segmentation and action recognition are only sparsely annotated on selected keyframes due to prohibitive labeling costs. This supervision imbalance undermines shared representation learning and limits joint optimization across heterogeneous surgical tasks. To address this, we propose Flow-guided Annotation for Robust Operating Scenes (FAROS), a flow-guided label interpolation framework, that combines zero-shot segmentation-based mask propagation with optical flow estimation to overcome the limitations of appearance-based propagation under challenging surgical conditions such as occlusion, smoke, and motion blur, generating temporally consistent dense pseudo labels from sparse keyframe annotations. The densified instrument masks and action labels are integrated into a unified Transformer-based multi-task framework that jointly learns surgical phase recognition, step recognition, anticipation, instrument segmentation, and action recognition, enabling balanced optimization between dense temporal supervision and sparse spatial supervision. The label interpolation quality of FAROS is first validated on the DAVIS 2017 benchmark under a sparse ground-truth protocol, confirming robust propagation beyond the surgical domain. Extensive experiments on GraSP, MISAW, and AutoLaparo benchmarks further demonstrate that FAROS significantly improves cross-task representation learning and enhances holistic surgical scene understanding performance across spatio-temporal tasks.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-245](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
