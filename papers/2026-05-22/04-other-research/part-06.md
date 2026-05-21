# 📦 其他研究 | 2026年05月22日

> 本类共 **352** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-352](./part-08.md)

---

### 251. [LoCar: Localization-Aware Evaluation of In-Vehicle Assistants through Fine-Grained Sociolinguistic Control](https://arxiv.org/abs/2605.21086)

**<font color=#1a73e8>作者：</font>** Seogyeong Jeong, Kiwoong Park, Seyoung Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) are increasingly integrated into in-vehicle conversational systems, identifying the optimal model remains challenging due to the lack of domain-specific evaluation standards tailored to real-world deployment requirements. In this paper, we propose a novel evaluation framework for in-vehicle assistants, with a particular focus on Korean-language localization. Our empirical analysis reveals notable patterns in model behavior. First, fine-grained Korean honorific control remains unstable in current LLMs, indicating that precise speech-level realization must be explicitly evaluated in localization settings. Second, models exhibit weaker performance in strategic conversational metrics like clarification and proactivity. Our analysis suggests this stems from the inherent subjective complexity of these tasks, where our framework adopts a conservative evaluation stance to prioritize reliability. Together, our findings underscore that automotive AI must move beyond general competence toward precise linguistic tailoring and reliable, safety-oriented interaction management.

---


### 252. [Reviving Error Correction in Modern Deep Time-Series Forecasting](https://arxiv.org/abs/2605.21088)

**<font color=#1a73e8>作者：</font>** Minh Hoang Nguyen, Dai Do, Huu Hiep Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep-learning models have achieved remarkable success in time-series forecasting. Yet, their performance degrades in long-term prediction due to error accumulation in autoregressive inference, where predictions are recursively used as inputs. While classical error correction mechanisms (ECMs) have long been used in statistical methods, their applicability to deep learning models remains limited or ineffective. In this work, we revisit the error accumulation problem in deep time-series forecasting and investigate the role and necessity of ECMs in this new context. We propose a simple, architecture-agnostic error correction model that can be integrated with any existing forecaster without requiring retraining. By explicitly decomposing predictions into trend and seasonal components and training the corrector to adjust each separately, we introduce the Universal Error Corrector with Seasonal-Trend Decomposition (UEC-STD), which significantly improves correction accuracy and robustness across 4 backbones and 10 datasets. Our findings provide a practical tool for enhancing forecasts while offering new insights into mitigating autoregressive errors in deep time-series models. Code is available at this https URL.

---


### 253. [An Evidence-driven Protocol for Trustworthy CI Pipelines](https://arxiv.org/abs/2605.21089)

**<font color=#1a73e8>作者：</font>** Fernando Castillo, Eduardo Brito, Pille Pullonen-Raudvere 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Enterprise software supply chains are increasingly vulnerable to infrastructure attacks, resulting in financial and reputational damage. Ensuring the integrity and provenance of software artifacts remains a significant challenge, where re-execution of the build and tests by every consumer to guarantee provenance produces a verification bottleneck and credibility reduction. This paper presents an evidence-driven protocol for trustworthy Continuous Integration (CI) pipelines that combines Deterministic Build Systems (DBS) with Trusted Execution Environments (TEEs). The approach provides cryptographically verifiable guarantees of integrity, authenticity, and attestation for CI artifacts in distributed environments, reducing implicit trust without requiring costly re-execution by consumers. We introduce a protocol that binds deterministic builds with TEE-based attestations, formalizing the evidence life cycle, together with a practical implementation using Nix and Intel TDX. Experimental results show that artifact verification is reduced from redundant computation to lightweight signature and policy checks. These findings demonstrate that evidence-driven CI pipelines establish scalable and verifiable trust in digital infrastructure, effectively amortizing the initial computational overhead introduced by TEEs.

---


### 254. [UOTIP: Unbalanced Optimal Transport Map for Unpaired Inverse Problems](https://arxiv.org/abs/2605.21094)

**<font color=#1a73e8>作者：</font>** Donggyu Lee, Taekyung Lee, Jaewoong Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate unpaired image inverse problems, a challenging setting where only independent, non-paired sets of noisy measurements and clean target signals are available for training. We propose a novel inverse problem solver based on Unbalanced Optimal Transport, called Unbalanced Optimal Transport Map for Inverse Problems (UOTIP). Our method formulates the reconstruction task, predicting clean target signals from noisy measurements, as learning a UOT Map from noisy measurement distribution to clean signal distribution by incorporating a likelihood-based cost function. By relaxing the exact marginal constraint, the UOT framework provides key advantages to our model: robustness to multi-level observation noise, adaptability to class imbalance between noisy and clean datasets, and generalizability to diverse noise-type scenarios. Furthermore, we theoretically demonstrate that incorporating a quadratic cost term ensures the existence and uniqueness of the transport map by satisfying the twist condition, even for ill-posed inverse problems. Our experiments demonstrate that UOTIP achieves state-of-the-art performance on unpaired image inverse problem benchmarks, across linear and nonlinear inverse problems.

---


### 255. [R2AoP: Reliable and Robust Angle of Progression Estimation from Intrapartum Ultrasound](https://arxiv.org/abs/2605.21099)

**<font color=#1a73e8>作者：</font>** Yuanhan Wang, Yifei Chen, Beining Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of the Angle of Progression (AoP) from intrapartum transperineal ultrasound is critical for objective assessment of labor progression, yet remains highly sensitive to imaging noise, boundary ambiguities, and the geometric amplification of local segmentation errors. We propose R2AoP, a reliable and robust AoP estimation framework that integrates structurally informed segmentation and confidence-guided geometric modeling to achieve stable and reproducible measurements. A three-branch local-structure-enhanced backbone improves the delineation of the pubic symphysis (PS) and fetal head (FH), while confidence-weighted contour fitting explicitly suppresses the influence of unreliable boundary points in AoP computation. To further improve performance under heterogeneous acquisition conditions, we introduce a lightweight geometry-reliable test-time adaptation strategy as an auxiliary component, enabling stable inference without target annotations. Extensive evaluations on multi-center benchmarks demonstrate consistent reductions in AoP error and boundary metrics compared with state-of-the-art AoP methods. Our source code is available at this https URL.

---


### 256. [A Typed Tensor Language for Federated Learning](https://arxiv.org/abs/2605.21103)

**<font color=#1a73e8>作者：</font>** Theofilos Mailis, Kalliopi-Christina Despotidou, Konstantinos Filippopolitis 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning and analytics are often described as collections of separate protocols, even when they share the same mathematical form: client-local tensor computation, mergeable aggregation into shared state, and shared-only post-processing. We introduce a typed tensor language that formalizes this structure. The language distinguishes federated tensors, whose records are partitioned across clients along a tracked record axis, from shared tensors, which are available globally. Its semantics are defined by comparison with a virtual global tensor, used only as a reference object. The main result is a shared-state factorization theory. We show that typed one-round programs factor through fixed-dimensional shared state whose size is independent of the number of clients and records, computed from client-local tensor expressions and merged across clients. We also prove a converse representability result; factorizations whose encoders and decoders are expressible in the language are realized by typed one-round programs, and the correspondence extends to iterative programs whose cross-round state is shared. This gives a formal account of the computations in the language that can be expressed as encode, merge, and decode procedures. We then develop a differentiable fragment for learning. If a per-record loss and its per-record gradient are represented by client-local tensor expressions, the global gradient is represented by record-axis summation of the federated gradient tensor. This yields typed iterative programs for server-side gradient descent and shared-linear-algebra second-order updates. The framework characterizes a broad class of federated learning computations whose communication passes through fixed-dimensional shared state.

---


### 257. [HORST: Composing Optimizer Geometries for Sparse Transformer Training](https://arxiv.org/abs/2605.21104)

**<font color=#1a73e8>作者：</font>** Tom Jacobs, Rohan Jain, Rebekka Burkholz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparsifying transformers remains a fundamental challenge, as standard optimizers fail to simultaneously encourage sparsity and maintain training stability. Effective adaptive optimizers exhibit an implicit $L_{\infty}$ bias favoring stability, yet, sparsity requires an $L_1$ bias. To integrate sparsity, we propose a composition of optimizer steps, which we cast as non-commutative operators to analyze and combine their optimization geometry in a principled way. This yields HORST (Hyperbolic Operator for Robust Sparse Training), a modular optimizer that inherits stability from adaptive methods while inducing $L_1$ sparsity bias through a hyperbolic mirror map. Our experiments demonstrate its utility for sparse training of transformers on both vision and language tasks. HORST consistently and significantly outperforms AdamW baselines across all sparsity levels, with large gains at higher sparsity.

---


### 258. [Improved Guarantees for Constrained Online Convex Optimization via Self-Contraction](https://arxiv.org/abs/2605.21107)

**<font color=#1a73e8>作者：</font>** Dhruv Sarkar, Abhishek Sinha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider Constrained Online Convex Optimization (COCO) with adversarially chosen constraints. At each round, the learner chooses an action before observing the loss and constraint function for that round. The goal is to achieve small static regret against the best point satisfying all constraints while also controlling cumulative constraint violation ($\mathsf{CCV}$). For strongly convex losses, state-of-the-art algorithms achieve $O(\log T)$ regret and $O(\sqrt{T \log T})$ $\mathsf{CCV}.$ The corresponding best-known bounds for convex losses is $O(\sqrt{T})$ regret and $O(\sqrt{T} \log T)$ $\mathsf{CCV}$. In this paper, we give a simple projection-based algorithm that simultaneously achieves $O(\log T)$ regret and $O(\log T)$ $\mathsf{CCV}$ for strongly-convex losses, yielding an exponential improvement in the $\mathsf{CCV}$. For the convex losses, our algorithm improves the $\mathsf{CCV}$ to $O(\sqrt{T})$ while maintaining the optimal $O(\sqrt{T})$ regret. The key to our improvement is a recent geometric result for self-contracted curves, which may be of independent interest.

---


### 259. [Efficient Learning of Deep State Space Models via Importance Smoothing](https://arxiv.org/abs/2605.21108)

**<font color=#1a73e8>作者：</font>** John-Joseph Brady, Nikolas Nusken, Yunpeng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent state space systems are ubiquitous in statistical modelling, arising naturally when a time series is observed through a noisy measurement function, however training deep state space models (DSSM) at scale remains difficult. Two largely distinct strategies and literatures have developed around the training of DSSMs. Firstly, auto-encoding DSSMs train generative DSSMs by optimising a variational lower bound. Secondly, DSSMs trained by back-propagating the outputs of a classical sequential Monte Carlo algorithm (SMC). Such approaches can train DSSMs for discriminative as well as generative tasks, however, due to the sequentiality of their forward pass, scale poorly on modern hardware. We propose a new training method \emph{parallel variational Monte Carlo} (PVMC) that bridges the gap between the paradigms, and can be used robustly to train DSSMs for both discriminative and generative tasks. Our method achieves state-of-the-art or better results on a set of baseline experiments and trains $10\times$ faster than the fastest competing SMC approach.

---


### 260. [RCGDet3D: Rethinking 4D Radar-Camera Fusion-based 3D Object Detection with Enhanced Radar Feature Encoding](https://arxiv.org/abs/2605.21112)

**<font color=#1a73e8>作者：</font>** Weiyi Xiong, Bing Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D automotive radar is indispensable for autonomous driving due to its low cost and robustness, yet its point cloud sparsity challenges 3D object detection. Existing 4D radar-camera fusion methods focus on complex fusion strategies, trading inference speed for marginal gains. This trade-off hinders real-time deployment due to heavy computation on dense feature maps. In contrast, feature extraction from sparse radar points is less time-consuming but remains under-explored. This work uncovers that simply enhancing radar feature extraction can achieve comparable or even higher performance than elaborate fusion modules, while maintaining real-time performance. Based on this finding, we propose RCGDet3D, which centers on radar feature encoding and simplifies multi-modal fusion. Its encoder inherits from the efficient Gaussian Splatting-based Point Gaussian Encoder (PGE) in RadarGaussianDet3D with two key improvements. First, the Ray-centric PGE (R-PGE) predicts Gaussian attributes in ray-aligned coordinate systems before unifying them to Bird's-Eye View (BEV) space, significantly improving geometric consistency and reducing learning difficulty by decoupling the coordinate transformation from representation learning. Second, a Semantic Injection (SI) module incorporates visual cues from images, producing more geometrically accurate and semantically enriched radar features. Experiments on View-of-Delft (VoD) and TJ4DRadSet show that RCGDet3D outperforms state-of-the-art methods in both accuracy and speed, setting a new benchmark for real-time deployment.

---


### 261. [A Unified Framework for Uncertainty-Aware Explainable Artificial Intelligence: A Case Study in Power Quality Disturbance Classification](https://arxiv.org/abs/2605.21114)

**<font color=#1a73e8>作者：</font>** Yinsong Chen, Samson S. Yu, Zhong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc explainable AI (XAI) methods typically produce deterministic attribution maps, whereas Bayesian neural networks (BNNs) induce a distribution over explanations. Capturing the variability of this distribution is important for uncertainty-aware decision-making. This paper formalises the \emph{explanation distribution} as the push-forward measure of the BNN posterior through any Lipschitz-continuous attribution operator. It further proposes the uncertainty-aware relevance attribution operator (UA-RAO), a general family of operators that summarises the explanation distribution using the mean, variance, coefficient of variation, quantiles, and set-theoretic aggregation measures. Theoretical support is provided through Monte Carlo accessibility and Wasserstein approximation bounds. The framework is evaluated on a 15-class power quality disturbance (PQD) classification benchmark, comparing three BNN approximations paired with three attribution operators using relevance mass accuracy and intersection-over-union as localisation metrics. Results show that deep ensembles with the mean UA-RAO improve localisation over the deterministic baseline, while other UA-RAO summaries reveal uncertainty patterns absent from point-estimate attributions. Qualitative results on measured signals further suggest that these patterns generalise beyond the synthetic training distribution. The framework is domain-agnostic and can be applied to any BNN paired with a Lipschitz-continuous attribution operator.

---


### 262. [Image Encryption via Data-Identified Discrete Chaotic Maps](https://arxiv.org/abs/2605.21118)

**<font color=#1a73e8>作者：</font>** Wenyuan Lia, Xiao-Yun Wang, Zhigang Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this work, we propose a data-driven image encryption framework that identifies chaotic maps directly from data using the SINDy-PI algorithm. Unlike conventional encryption schemes relying on predefined maps, our method learns the full explicit dynamics -- including cross-terms and higher-order nonlinearities -- from observational data. The validity of this approach is verified on three distinct chaotic systems: the H{é}non map, the three-dimensional logistic map, and the piecewise-linear Lozi map, demonstrating its generality. The encryption key consists solely of initial conditions; the map structure itself becomes data-dependent, introducing an extra layer of security. Moreover, even when the initial conditions are fixed, different training data (e.g., with a tiny noise seed) lead to slightly different maps, which produce completely different ciphertexts (NPCR $\approx 99.6\%$, UACI $\approx 33.5\%$). Numerical experiments on the H{é}non system show near-ideal information entropy ($\approx 8$ bits), negligible inter-pixel correlation, and extreme sensitivity to initial conditions: a perturbation of $10^{-16}$ causes total decryption failure. The scheme resists both differential and statistical attacks, with NPCR and UACI values matching theoretical ideals. Our results establish a new paradigm for chaos-based cryptography beyond fixed maps.

---


### 263. [ROAR-3D: Routing Arbitrary Views for High-Fidelity 3D Generation](https://arxiv.org/abs/2605.21121)

**<font color=#1a73e8>作者：</font>** Hanxiao Sun, Mingxin Yang, Shuhui Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image-to-3D generative models can now produce high-quality geometry, yet conditioning on a single view inevitably introduces ambiguity about unseen regions. Multi-view conditioning can reduce this ambiguity, but existing methods either require fixed canonical viewpoints or rely on external reconstruction modules that impose heavy training costs and limit generation quality. We observe that pretrained single-view models already possess strong 2D-to-3D grounding that can be reused for multi-view conditioning. However, a closer analysis reveals that their conditioning mechanism entangles orientation control with geometry transfer, two functions that conflict when images from different viewpoints are naively combined. Based on this analysis, we propose ROAR-3D, a lightweight method that upgrades a pretrained single-view model to accept an arbitrary number of unposed images. A token-wise view router assigns each 3D latent token to its most relevant view, implicitly establishing 2D-to-3D correspondences without explicit pose input. A dual-stream attention design preserves the pretrained primary-view behavior while routing auxiliary views through a separate path dedicated to geometric enrichment. An orientation perturbation strategy ensures the auxiliary path learns orientation-independent geometry transfer. These components introduce minimal trainable parameters and add negligible inference overhead relative to the single-view baseline. ROAR-3D achieves state-of-the-art multi-view 3D generation quality and supports test-time view scaling from 1 to 12+ views with consistent improvements.

---


### 264. [Linear-DPO: Linear Direct Preference Optimization for Diffusion and Flow-Matching Generative Models](https://arxiv.org/abs/2605.21123)

**<font color=#1a73e8>作者：</font>** Kesong Li, Yixuan Xu, Kuo-kun Tseng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) is successful for alignment in LLMs but still faces challenges in text-to-image generation. Existing studies are confined to denoising diffusion models while overlooking flow-matching, and suffer from an objective mismatch when applying discrete NLP-based DPO to regression-based generative tasks.\ In this paper, we derive a generalized DPO objective that covers both diffusion and flow-matching via a unified reverse-time SDE framework, and point out from a gradient perspective that the standard DPO objective is suboptimal for text-to-image generation. Consequently, we propose Linear-DPO, which replaces the aggressive sigmoid-based utility function with a sustained linear utility and incorporates an EMA-updated reference model. Qualitative and quantitative experiments on diffusion models (SD1.5, SDXL) and flow-matching model (SD3-Medium) demonstrate the superiority of our approach over existing baselines.

---


### 265. [Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation](https://arxiv.org/abs/2605.21125)

**<font color=#1a73e8>作者：</font>** Xixiang He, Qiyao Sun, Ao Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO), a prominent algorithm within the Reinforcement Learning from Verifiable Rewards (RLVR) framework, has achieved strong results in improving the reasoning capabilities of large language models (LLMs). However, GRPO is prone to advantage collapse, a failure mode where homogeneous rewards within a group (e.g., all correct or all incorrect answers) yield near-zero advantages and vanishing gradients. To address this, we introduce the Advantage Collapse Rate (ACR), the first diagnostic metric quantifying the proportion of training batches with ineffective gradients. Across models from 0.5B to 14B parameters on mathematical reasoning benchmarks, we show that ACR strongly predicts training stagnation and final performance. We then propose Adaptive Virtual Sample Policy Optimization (AVSPO), a lightweight extension of GRPO that injects virtual reward samples, guided by real-time ACR monitoring, to enable learning from homogeneous groups without additional model rollouts. AVSPO reduces advantage collapse by 58-63% relative to GRPO and yields consistent accuracy gains of 4-6 percentage points across all model scales, while maintaining generalization on the evaluated out-of-domain task. Code and datasets are available at this https URL.

---


### 266. [VersusQ: Pairwise Margin Reasoning for Generalizable Video Quality Assessment](https://arxiv.org/abs/2605.21130)

**<font color=#1a73e8>作者：</font>** Shibei Meng, Binxin Yang, Yuan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Multimodal Models (LMMs) have shown promise for video quality assessment, but most methods still predict an absolute score for each video. Such pointwise supervision often mixes perceptual quality with dataset-specific calibration, including annotation protocols, rating habits, and score distributions. As a result, the learned scoring rule may work well within a benchmark but transfer poorly across unseen domains. We argue that relative comparisons alleviate the absolute-scale calibration bias by focusing purely on perceptual differences rather than dataset-specific rating habits. Consequently, we propose \textbf{VersusQ}, a pairwise margin reasoning framework driven entirely by direct comparisons. Specifically, VersusQ performs LMM-based comparison between two videos, reasons about their visual and temporal quality differences, and predicts a signed continuous margin that captures both the preferred choice and the degree of difference. Furthermore, to align interpretable comparison rationales with fine-grained numerical differences, we introduce Margin-Coupled GRPO, which jointly optimizes rollout-based relational reasoning and continuous margin regression. Extensive experiments on multiple public VQA benchmarks demonstrate that VersusQ achieves state-of-the-art performance, strong cross-domain generalization, and reliable fine-grained ranking under heterogeneous evaluation scenarios.

---


### 267. [UniT: Unified Geometry Learning with Group Autoregressive Transformer](https://arxiv.org/abs/2605.21131)

**<font color=#1a73e8>作者：</font>** Haotian Wang, Yusong Huang, Zhaonian Kuang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent feed-forward models have significantly advanced geometry perception for inferring dense 3D structure from sensor observations. However, its essential capabilities remain fragmented across multiple incompatible paradigms, including online perception, offline reconstruction, multi-modal integration, long-horizon scalability, and metric-scale estimation. We present UniT, a unified model built upon a novel Group Autoregressive Transformer, which reformulates these seemingly disparate capabilities within a single framework. The key idea is to treat groups of sensor observations as the basic autoregressive units and predict the corresponding point maps in an anchor-free and scale-adaptive manner. More specifically, diverse view configurations in both online and offline settings are naturally unified within a single group autoregression process. By varying the group size, online mode operates over multiple autoregressive steps with single-frame groups, whereas offline mode aggregates a multi-frame group in a single forward pass. Meanwhile, a queue-style KV caching mechanism ensures bounded autoregressive memory over long horizons. This is enabled by reducing long-range dependencies on early frames through anchor-free relational modeling, thereby allowing outdated memory to be discarded on the fly. To improve metric-scale generalization across scenes, a scale-adaptive geometry loss is further introduced within this framework. It couples relative geometric constraints with a partial absolute scale term, implicitly regularizing global scale and inducing a progressive transition from scale-invariant geometry to metric-scale solutions. Together with a dedicated modal attention module for integrating auxiliary modalities, UniT achieves state-of-the-art performance in unified geometry perception, as validated on ten benchmarks spanning seven representative tasks.

---


### 268. [SurgOnAir: Hierarchy-Aware Real-Time Surgical Video Commentary](https://arxiv.org/abs/2605.21132)

**<font color=#1a73e8>作者：</font>** Jingyi He, Yue Zhou, Long Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding surgical workflow in real time is fundamental for intelligent surgical embodiment, where AI systems continuously perceive and respond as surgery proceeds. In the operating room, critical decisions depend on subtle, moment-to-moment changes, such as fine instrument movements and evolving tissue states, where even slight perceptual delays can limit assistance or compromise safety. Yet existing methods remain offline or operate at coarse temporal scales, generating descriptions only after processing clips, preventing immediate reaction. We address this by proposing SurgOnAir, a streaming vision-language model that processes frames sequentially without future access and progressively generates narration tokens as visual input arrives. SurgOnAir achieves fine-grained frame-to-token generation, enabling instant responsiveness to evolving surgical dynamics. Built upon our curated hierarchical dataset SurgOnAir-11k spanning action-, step-, and phase-level supervision, the model is trained to produce multi-level textual responses that reflect the inherent hierarchy of surgical procedures. Furthermore, special transition tokens are generated to explicitly mark state changes, allowing SurgOnAir to capture and signal key workflow transitions as they occur. Experiments show that SurgOnAir enables real-time understanding through a single vision-language model that unifies streaming across multiple hierarchies of the surgical workflow, generating superior and hierarchy-aware narrations. Code and dataset will be public.

---


### 269. [Smarter edits? Post-editing with error highlights and translation suggestions](https://arxiv.org/abs/2605.21135)

**<font color=#1a73e8>作者：</font>** Fleur V.J. van Tellingen, Gautam Ranka, Dora Žugčić 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As MT quality increases, interest in enhanced post-editing features such as QE-derived error highlights is growing, yet evidence for their usefulness remains limited. In this work, we explore the usefulness of LLM-derived error highlights and correction suggestions based on automatic post-editing (APE). We conduct a study where professional translators (En-Nl) post-edit translations using APE error highlights and correction suggestions and compare productivity, quality and user experience to regular PE and PE with QE-derived highlights. While no condition yielded productivity or quality gains compared to regular PE, APE highlights were better received than QE-derived highlights, and correction suggestions improved overall user experience.

---


### 270. [Distill to Think, Foresee to Act: Cognitive-Physical Reinforcement Learning for Autonomous Driving](https://arxiv.org/abs/2605.21139)

**<font color=#1a73e8>作者：</font>** Yang Wu, Qiang Meng, Zhaojiang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current end-to-end autonomous driving models are fundamentally constrained by the behavioral cloning ceiling of imitation learning. While reinforcement learning offers a path to smarter autonomy, it demands two missing pieces of infrastructure: (1) a cognitive foundation that understands traffic semantics and driving intent, and (2) a foresighted physical environment that can anticipate the consequences of candidate actions. To this end, we propose CoPhy, a CognitivePhysical reinforcement learning framework for autonomous driving. To distill to think, we distill VLM knowledge into the BEV encoder and then discard the VLM entirely, retaining cognitive ability at zero inference cost while releasing the cognitive channel as a pluggable interface for optional human language commands. To foresee to act, we build an auto-regressive BEV world model that explicitly predicts future semantic maps conditioned on candidate actions, serving as an interpretable physical sandbox from which safety metrics are directly derived. Built upon this dual infrastructure, we optimize the driving policy via GRPO with a novel dual-reward mechanism: a physical reward derived from BEV rollouts enforces hard safety constraints, while a cognitive reward from a language-aligned scorer ensures intent compliance. Extensive experiments demonstrate that CoPhy not only achieves state-of-the-art results on NAVSIM v1 and v2 benchmarks, but also enables safer driving via cognitively informed scene compliance and flexible intent control through user-defined language instructions.

---


### 271. [Detecting Trojaned DNNs via Spectral Regression Analysis](https://arxiv.org/abs/2605.21146)

**<font color=#1a73e8>作者：</font>** Samuele Pasini, Jinhan Kim, Paolo Tonella  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern DNNs are repeatedly fine-tuned to incorporate new data and functionality. This evolutionary workflow introduces a security risk when updated data cannot be fully trusted, as adversaries may implant Trojans during fine-tuning. We present MIST, a Trojan detection approach that analyzes how a model's internal representations change during fine-tuning. Rather than attempting to reconstruct trigger conditions, MIST characterizes benign model evolution using pre-activation spectra and flags updates whose spectral deviations are inconsistent with this reference. This framing treats Trojan detection as a regression problem over model updates. An empirical evaluation across four datasets and eight Trojan attacks shows that spectral distances reliably distinguish Trojaned updates from clean fine-tuning. MIST outperforms state-of-the-art detection accuracy after a single update, without requiring any knowledge about the poisoned data or the trigger, and remains effective under multi-step benign evolution, with graceful and bounded degradation. These results indicate that spectral evolution provides a stable and assumption-light signal for detecting malicious model updates.

---


### 272. [Comparative Analysis of Military Detection Using Drone Imagery Across Multiple Visual Spectrums](https://arxiv.org/abs/2605.21157)

**<font color=#1a73e8>作者：</font>** Sourov Roy Shuvo, Prajwal Panth, Rajesh Chowdhury 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In modern warfare, drones are becoming an essential part of intelligence gathering and carrying out precise attacks in different kinds of hostile environments. Their ability to operate in real-time and hostile environments from a safe distance makes them invaluable for surveillance and military operations. The KIIT-MiTA dataset is comprised of images of different military scenarios taken from drones, and these provide a foundation for detecting military objects, but it does not take into account the various types of real-world scenarios. With that in mind, to evaluate how the models are performing under varying conditions, four different types of datasets are created: Gray Scale, Thermal Vision, Night Vision, and Obscura Vision. These simulate the real-world environments such as low visibility, heat-based imagery, and nighttime conditions. The YOLOv11-small model is trained and used to detect objects across diverse settings. This research boosts the performance and reliability of drone-based operations by contributing to the development of advanced detection systems in both defensive and offensive missions.

---


### 273. [Q-SYNTH: Hybrid Quantum-Classical Adversarial Augmentation for Imbalanced Fraud Detection](https://arxiv.org/abs/2605.21164)

**<font color=#1a73e8>作者：</font>** Adam Innan, Mansour El Alami, Nouhaila Innan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Credit card fraud detection is fundamentally challenged by extreme class imbalance, where fraudulent transactions are rare yet operationally critical. This imbalance often biases supervised learners toward the legitimate class, leading to high overall accuracy but weaker fraud-class recall and F1-score. This paper introduces Q-SYNTH, a hybrid classical--quantum generative adversarial framework in which a parameterized quantum circuit serves as the generator and a classical neural network serves as the discriminator. Q-SYNTH is designed for minority-class fraud synthesis in tabular data and is evaluated along two dimensions: statistical fidelity to real fraud samples and downstream performance for fraud detection. To this end, generated samples are assessed using distributional similarity measures based on Kolmogorov-Smirnov statistics and Wasserstein distances, real-vs-synthetic detectability measured by AUC-ROC, and downstream classification performance across both quantum and classical classifiers. Under the reported protocol, Q-SYNTH reduces marginal distribution mismatch relative to a classical GAN baseline while maintaining competitive downstream fraud-detection performance. Although SMOTE achieves the strongest feature-wise similarity and the classical GAN attains the highest downstream performance in several settings, Q-SYNTH offers a favorable compromise between distributional fidelity and downstream performance, supporting the feasibility of hybrid quantum augmentation for imbalanced fraud detection.

---


### 274. [ScenePilot: Controllable Boundary-Driven Critical Scenario Generation for Autonomous Driving](https://arxiv.org/abs/2605.21168)

**<font color=#1a73e8>作者：</font>** Qiyu Ruan, Yuxuan Wang, He Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety-critical scenarios are central to evaluating autonomous driving systems, yet their rarity in naturalistic logs makes simulation-based stress testing indispensable. Most scenario generation methods treat surrounding agents as adversaries, but they either (i) induce failures without explicitly modeling vehicle-road physical limits, yielding visually extreme yet physically unsolvable crashes, or (ii) enforce physical feasibility or policy feasibility in isolation, which can over-focus on aggressive maneuvers or remain tied to a controller-dependent capability boundary. We propose ScenePilot, a feasibility-guided, boundary-driven framework that targets the boundary band: scenarios that are physically solvable in principle yet still cause the deployed autonomy stack to fail. We formulate generation as constrained multi-objective reinforcement learning, combining an RSS-derived physical-feasibility score $\sigma$ with an online-learned AV-risk predictor $\Phi$, and introduce step-level feasibility-aware shielding to keep exploration near the feasibility boundary while avoiding infeasible artifacts. Experiments on SafeBench with multiple planners show that ScenePilot yields substantially higher collision rates (+6.2 percentage points) while preserving physical validity, and that adversarial fine-tuning on these boundary-band scenarios consistently reduces downstream crash rates. The code is available at this https URL.

---


### 275. [FTerViT: Fully Ternary Vision Transformer](https://arxiv.org/abs/2605.21171)

**<font color=#1a73e8>作者：</font>** Szymon Ruciński, Pietro Bonazzi, Engin Türetken 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ternary Vision Transformers offer substantial model compression, however state-of-the-art methods only ternarize the encoder layers, leaving patch embeddings, LayerNorm parameters, and classifier heads in full precision. In compact models targeting resource-constrained processors, such as microcontrollers, these remaining full-precision components determine the total memory footprint, severely limiting deployment efficiency and on-device feasibility. In this work, we introduce a fully ternarized Vision Transformer in which \emph{all} weight matrices and normalization parameters are ternarized (FTerViT). To this end, we introduce two novel operators : TernaryBitConv2d with per-channel scaling for patch embedding and TernaryLayerNorm. FTerViT is trained using knowledge distillation, followed by a lightweight quantization-aware recovery phase. Our ternary W2A8 DeiT-III-S at 384$\times$384 resolution achieves 82.43\% ImageNet-1K top-1 at 6.09\,MB (${\sim}$15$\times$ compression, $-$2.42\,pp vs.\ FP32), outperforming prior ternary ViTs methods up to 8 pp. Finally, we demonstrate the first implementation of ternary vision transformers on a dual cores XTensa LX7 microcontroller inside the ESP32-S3 system-on-chip. By deploying FTerViT-Small (based on DeiT-III-Small at 224$\times$224 resolution, 5.81\,MB), we achieve 79.64\% ImageNet-1K top-1 accuracy.

---


### 276. [Metaphors in Literary Post-Editing: Opening Pandora's Box?](https://arxiv.org/abs/2605.21178)

**<font color=#1a73e8>作者：</font>** Aletta G. Dorst, Mayra O. Nas, Katinka Zeven  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates how post-editors of literary texts react and respond to the way metaphors have been translated by Neu ral Machine Translation (NMT) and Large Language Models (LLMs). The results show that one in three metaphors in the output were changed by the post-editors, demonstrating that the translation of fig urative language is indeed problematic in literary MT (LitMT). The responses indi cate that the post-editors were aware of overly literal translations, though mostly for multiword expressions. Moreover, at times they found it difficult to determine whether solutions were acceptable. They rated the overall quality of the MT out put as quite poor and stated that the post editing was more work and more effort than it would have been translating from scratch. This supports previous studies ar guing that post-editing constrains transla tors in their creativity and diminishes their sense of text ownership.

---


### 277. [Domain-Adaptable Reinforcement Learning for Code Generation with Dense Rewards](https://arxiv.org/abs/2605.21180)

**<font color=#1a73e8>作者：</font>** Erfan Aghadavoodi Jolfaei, Daniel Maninger, Abhinav Anand 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models show strong potential for automated code generation, but lack guarantees for correctness, quality, safety, and domain-specific constraints. For instance in robotics, where code generation is increasingly being used for planning and executing actions, awareness of the environment and physical constraints is critical. To facilitate the adaption of code-generating LLMs to diverse requirements, including domain-specific ones, we present a reinforcement learning framework that fine-tunes pre-trained LLMs using proximal policy optimization. Our customizable execution-aware reward formula captures and optimizes syntax, functional correctness, code style, security, and simulator executability. A token-level reward mapping mechanism enables effective credit assignment from execution outcomes to generated tokens. The framework is evaluated on general-purpose code generation (MBPP/MBPP+) and robotic program synthesis (RoboEval). The results show substantial improvements in functional correctness and simulator executability, including an absolute pass@1 increase of 19% on MBPP and a reduction in execution failures by 51% on RoboEval. These findings demonstrate that structured reinforcement learning can effectively align language models to correct program generation and domain-specific requirements.

---


### 278. [Manga109-v2026: Revisiting Manga109 Annotations for Modern Manga Understanding](https://arxiv.org/abs/2605.21182)

**<font color=#1a73e8>作者：</font>** Jeonghun Baek, Atsuyuki Miyai, Shota Onohara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Manga is a culturally distinctive multimodal medium and one of the most influential forms of Japanese popular culture. As AI systems increasingly target manga understanding, OCR, and translation, Manga109 has become a foundational dataset for manga-related AI research. However, the current Manga109 dataset contains transcription errors and coarse annotations, which do not align well with modern OCR and multimodal manga understanding tasks. In this work, we revisit the dialogue text annotations of Manga109 and identify five categories of annotation issues, including transcription errors, missing text regions, overlapping dialogue and onomatopoeia, and under-segmented speech balloons. To address these issues, we combine OCR-based issue detection and manual revision to construct Manga109-v2026, revising approximately 29,000 dialogue annotations. Our revisions better align Manga109 with modern OCR and multimodal manga understanding systems while preserving expressive structures characteristic of manga.

---


### 279. [Information Leakage Envelopes](https://arxiv.org/abs/2605.21185)

**<font color=#1a73e8>作者：</font>** Sara Saeidian, Carlos Pinzón, Catuscia Palamidessi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study privacy guarantees in the framework of pointwise maximal leakage (PML) that satisfy two requirements: they are robust under post-processing and upper bound the failure probability, i.e., the probability that the information leakage exceeds a given threshold. We first examine two candidate definitions inspired by (approximate) differential privacy and show that neither one satisfies both requirements simultaneously. We then introduce the notion of the PML envelope, which quantifies the largest amount of information leakage about a secret after arbitrary post-processing of a mechanism's output. By construction, the PML envelope satisfies both requirements. We discuss basic structural properties of the envelope, such as monotonicity, and derive general upper and lower bounds. We further analyze the envelope for two widely used privacy mechanisms: the PML-extremal mechanisms in the high-privacy regime and randomized response. Overall, this work establishes the PML envelope as a natural and operationally meaningful definition for providing privacy guarantees that are preserved under arbitrary downstream transformations.

---


### 280. [SAM-Sode: Towards Faithful Explanations for Tiny Bacteria Detection](https://arxiv.org/abs/2605.21186)

**<font color=#1a73e8>作者：</font>** Wanying Tan, Shuo Yan, Dazhi Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interpretability in object detection provides crucial confidence support for clinical auxiliary diagnosis. However, in tiny bacteria detection, traditional explanation methods often suffer from blurred foreground boundaries and diffuse feature attribution due to the extreme sparsity of target morphological features and severe interference from complex backgrounds. Such limitations hinder the provision of logically coherent morphological evidence. To bridge this gap, we propose a novel eXplainable AI (XAI) framework, SAM-Sode. The framework innovatively transforms initial feature attribution maps into geometry-aware prompts, leveraging the prior knowledge of the foundation model (SAM3) to achieve spatial refinement and morphological reconstruction of the explanatory mappings. Furthermore, we introduce a dual-constraint mechanism based on physical significance and geometric alignment to perform instance-level denoising, generating coherent explanations that better align with human expert intuition. Experimental results on our self-constructed bacteria dataset with complex circuit backgrounds (containing 2,524 images) and other public datasets demonstrate that the proposed method effectively suppresses background redundancy and significantly enhances the decision-making transparency of tiny object detection.

---


### 281. [Semantic Granularity Navigation in Image Editing](https://arxiv.org/abs/2605.21190)

**<font color=#1a73e8>作者：</font>** Liangsi Lu, Minzhe Guo, Xuhang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the generative capabilities of diffusion and flow models, real-image editing remains constrained by a persistent trade-off between semantic editability and structural fidelity. We trace a primary cause of this limitation to the implicit coupling of edit progress with model scale in existing paradigms. Under this coupling, stronger edits typically require visiting noisier states, which spends computation on destabilizing layout before the semantic change is well localized. We introduce NaviEdit, a training-free inference-time controller that decouples edit progress from model scale traversal through a strict self-consistency contract. NaviEdit operates at the rollout level and leaves the underlying pretrained model unchanged. It treats scale as a control input and reallocates a fixed step budget toward semantically responsive intermediate scales instead of destructive high-noise regimes. Experiments show positive average gains across compatible editors and flow backbones, supporting decoupling as a portable inference-time control principle.

---


### 282. [PGC: Peak-Guided Calibration for Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2605.21207)

**<font color=#1a73e8>作者：</font>** Xiaoyu Zhou, Jianwei Fei, Peipeng Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of generative AI, from GANs to modern diffusion models, has resulted in increasingly subtle discriminative clues. These fine-grained signals are often overshadowed by dominant, high-fidelity image content (e.g., the main subject), limiting the reliability of existing detectors that predominantly rely on global representations. To address this challenge, we propose the Peak-Guided Calibration (PGC) framework. PGC introduces a novel strategy that aggregates salient features via a peak-focusing mechanism. Specifically, by employing a peak-sensitive aggregation that accentuates the most discriminative local clues, PGC leverages these critical signals to calibrate the global decision. This approach recovers subtle patterns that would otherwise be submerged in the global context. Furthermore, to better simulate real-world threats, we introduce the CommGen15 dataset, a challenging benchmark comprising samples from 15 commercial models. Extensive experiments demonstrate that PGC achieves state-of-the-art performance. Specifically, it improves mean accuracy by +12.3% on our CommGen15 dataset, and sets new records on standard benchmarks, including GenImage (+2.1%), AIGI (+3.5%), and UniversalFakeDetect (+1.7%). Code is available at this https URL.

---


### 283. [Behavior-Consistent Deep Reinforcement Learning](https://arxiv.org/abs/2605.21214)

**<font color=#1a73e8>作者：</font>** Marcel Hussing, Liv G. d'Aliberti, Claas Voelcker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) often exhibits high variance across training runs, leading to unreliable performance and posing a major challenge to deployment in real-world domains. In this work, we address the challenge of cross-run policy divergence by formalizing the problem of behavior-consistent RL, where the objective is to obtain policies that are both high-performing and distributionally similar across training runs. Our key observation is that maximum-entropy RL provides a direct mechanism for controlling behavioral divergence by anchoring runs to a common (uniform) prior. We prove that, for Boltzmann policies, choosing the temperature proportional to $Q$-function disagreement bounds the pairwise KL divergence between the induced policies. However, we also show that naïvely increasing entropy might impair policy optimization while amplifying off-policy error. Building upon these observations, we propose $Q$-value Expectile Disagreement (QED), a state-dependent temperature schedule that uses double-critic disagreement as a single-run proxy for cross-run disagreement. Empirically, we demonstrate that across 18 continuous-control tasks, QED reduces across-run divergence by two orders of magnitude without sacrificing performance, resulting in a considerable reduction in return variance at modest sample-efficiency costs.

---


### 284. [OCTOPUS: Optimized KV Cache for Transformers via Octahedral Parametrization Under optimal Squared error quantization](https://arxiv.org/abs/2605.21226)

**<font color=#1a73e8>作者：</font>** Mark Boss, Vikram Voleti, Simon Donné 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The key-value (KV) cache dominates memory bandwidth and footprint in long-context autoregressive inference. Recent rotation-preconditioned codecs (TurboQuant, PolarQuant) show that a structured random rotation followed by a per-coordinate scalar quantizer matched to an analytically tractable marginal is a near-optimal recipe for KV compression. OCTOPUS advances this paradigm through joint quantization of rotated coordinate triplets. Each triplet's direction is mapped to a square via an octahedral parameterization, and the two resulting coordinates and the triplet norm are Lloyd-Max quantized against implementation-matched marginals. Optimizing the per-triplet squared error gives a strictly non-uniform bit allocation depending only on the total dimensionality of the keys. We find the finite-dimensional quality optimum with sweeps to be constant on every real decoder we test. The codec is data-oblivious, online, and deterministic given a seed. Across text, video, and audio, OCTOPUS matches or beats every prior rotation codec at every reported bit width and metric, with a lead that grows as bits drop for extreme compression. Furthermore, a fused Triton implementation reconstructs keys on the fly without materializing the uncompressed key, so the codec adds no decode-time bandwidth or latency over the existing dequantization. Project Page: this https URL

---


### 285. [RePCM: Region-Specific and Phenotype-Adaptive Bi-Ventricular Cardiac Motion Synthesis](https://arxiv.org/abs/2605.21237)

**<font color=#1a73e8>作者：</font>** Xuan Yang, Xiaohan Yuan, Hao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cardiac motion over a cardiac cycle is crucial for quantifying regional function and is strongly affected by cardiovascular diseases. Since temporally dense mesh sequences are difficult to obtain in practice, we focus on leveraging the more accessible end-diastolic frame to infer a full-cycle sequence. Due to strong regional and disease-specific differences, traditional methods often oversmooth the data by relying on generative models that are optimized for global patterns. To address this problem, we propose Region-Aware and Phenotype-Adaptive Bi-Ventricular Cardiac Motion Synthesis (RePCM) for single frame Bi-ventricular mesh motion completion. In Stage I, a reconstruction network learns vertex wise motion descriptors and clustering yields a data driven functional partition, providing an explicit motion derived region structure. In Stage II, a Region-Specific Injection Module enforces masked, synchronized region exchange within a conditional VAE, preserving localized specific dynamics and restricting cross-region mixing. A Phenotype-Adaptive Mixture-of-Experts prior conditioned on ED shape uses anatomy-guided cues to model latent motion trends and capture inter-disease variability. Experiments on three datasets covering different cardiovascular diseases show consistent gains in geometric and functional metrics and improved preservation of region specific dynamics.

---


### 286. [Divide and Contrast: Learning Robust Temporal Features without Augmentation](https://arxiv.org/abs/2605.21241)

**<font color=#1a73e8>作者：</font>** Abdul-Kazeem Shamba, Kerstin Bach, Gavin Taylor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning for time-series representation aims to reduce reliance on labeled data while maintaining strong downstream performance, yet many existing approaches incur high computational costs or rely on assumptions that do not hold across diverse temporal dynamics. In this work, we introduce Divide and Contrast (Di-COT), an unsupervised framework that avoids data augmentation and multiple encoder passes by contrasting informative substructures within a window rather than individual timesteps. Di-COT stochastically partitions each window into a small number of overlapping sub-blocks per iteration, enabling efficient and meaningful contrast while mitigating false positives during temporal transitions. To further improve scalability, we adopt a contrastive objective whose computation depends on the batch size and the number of sub-blocks, making loss computation independent of sequence length. Extensive experiments on six large-scale real-world datasets, as well as the UCR and UEA benchmarks, demonstrate that Di-COT learns semantically structured and transferable representations, achieving state-of-the-art performance on classification, clustering, $k$NN, and cross-dataset transfer, while substantially reducing training time. The source code is publicly available at this https URL.

---


### 287. [SR-Ground: Image Quality Grounding for Super-Resolved Content](https://arxiv.org/abs/2605.21244)

**<font color=#1a73e8>作者：</font>** Artem Borisov, Evgeney Bogatyrev, Khaled Abud 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Super-Resolution (SR) has advanced rapidly in recent years, with diffusion-based models achieving unprecedented fidelity at the cost of introducing new types of visual artifacts. While existing Image Quality Assessment (IQA) methods provide holistic quality scores, they lack interpretability and fail to distinguish between different artifact types arising from modern SR approaches.
To address this gap, we introduce SR-Ground, a large-scale dataset specifically designed for fine-grained artifact segmentation in super-resolved images. The dataset comprises images processed by a diverse set of state-of-the-art SR models, with pixel-level annotations for multiple artifact categories. We conduct a large-scale crowdsourcing study involving 1,062 participants to validate and refine automatically generated segmentations, resulting in a high-quality dataset of 63,000 images spanning 6 distinct artifact types.
We demonstrate that training IQA models with grounding capabilities on SR-Ground significantly improves performance on downstream tasks. Furthermore, we introduce a fine-tuning pipeline that leverages our grounding model to reduce perceptible artifacts in SR outputs, showcasing the practical utility of our dataset.

---


### 288. [Profiling User Vulnerability to Phishing Through Psychological and Behavioral Factors](https://arxiv.org/abs/2605.21246)

**<font color=#1a73e8>作者：</font>** Valeria Formisano, Danilo Gentile, Gennaro Esposito Mocerino 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing remains one of the most pervasive cybersecurity threats, shifting the focus from technological vulnerabilities to human cognitive and psychological factors. In coherence with the trend of studies on phishing to increasingly focus on human aspects and vulnerable users profiling, this study investigates the multidimensional nature of user susceptibility by analyzing data from the Spamley dataset, involving 1,086 participants evaluated through a realistic phishing detection task. Using Exploratory Factor Analysis (EFA), five latent constructs were identified, named: Seniority, Expertise, Creativity, Stability, and Vulnerability. Behavioral findings, validating self-reported impulsivity through its negative correlation with response times, demonstrate that faster decision-making significantly distinguishes vulnerable users from resilient ones. A K-Means clustering procedure, driven by the dimensions of Seniority (F1) and Creativity (F3), revealed two distinct user profiles: the Aware User and the High-Risk User. The results demonstrate that technical knowledge alone is insufficient to guarantee resilience; rather, the interaction between operational maturity, decision-making speed, and cognitive approach determines effectiveness. The findings suggest that the majority of users fall into the High-Risk category, characterized by hasty evaluation processes and lower critical analysis. These results underline the urgent need to move beyond "one-size-fits-all" training toward personalized, adaptive cybersecurity programs that actively address cognitive biases and behavioral tendencies.

---


### 289. [Graph Navier Stokes Networks](https://arxiv.org/abs/2605.21247)

**<font color=#1a73e8>作者：</font>** Zexing Zhao, Guangsi Shi, Yu Gong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have emerged as a cornerstone of deep learning, with most existing methods rooted in graph signal processing and diffusion equations to model message passing. However, these approaches inherently suffer from the oversmoothing problem, where node features become indistinguishable as the network depth increases. Inspired by the Navier Stokes equations, we introduce Graph Navier Stokes Networks (GNSN), a novel architecture that transcends conventional diffusion-based message passing by incorporating convection into graph structures. GNSN defines a dynamic velocity field on the graph to govern convection, enabling more efficient and direct message propagation. By adaptively balancing convection and diffusion, GNSN is able to efficiently handle datasets with varying levels of homophily. Extensive evaluations across twelve real-world datasets demonstrate that GNSN consistently outperforms state-of-the-art baselines in classification accuracy. Moreover, experimental results further emphasize its effectiveness in alleviating the oversmoothing problem.

---


### 290. [Reliable Automated Triage in Spanish Clinical Notes: A Hybrid Framework for Risk-Aware HIV Suspicion Identification](https://arxiv.org/abs/2605.21256)

**<font color=#1a73e8>作者：</font>** Rodrigo Morales-Sánchez, Soto Montalvo, Raquel Martínez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard clinical Natural Language Processing (NLP) benchmarks often yield inflated metrics by forcing deterministic classification on ambiguous instances, thereby obscuring the clinical risks of overconfident predictions. To bridge this gap, we propose a risk-aware hybrid selective classification framework, evaluated on early Human Immunodeficiency Virus suspicion identification in Spanish clinical notes. Our dual-verification approach explicitly decouples aleatoric uncertainty through Mondrian conformal prediction and epistemic uncertainty using a Multi-Centroid Mahalanobis Distance veto. Empirical evaluations reveal that standard uncertainty metrics and baseline classifiers are structurally insufficient for safe medical triage, suffering severe coverage collapse when forced to operate under strict reliability constraints. In contrast, by demanding that clinical narratives pass both probabilistic and geometric safeguards, the proposed framework successfully isolates a highly trustworthy operational domain.

---


### 291. [On the Cost and Benefit of Chain of Thought: A Learning-Theoretic Perspective](https://arxiv.org/abs/2605.21260)

**<font color=#1a73e8>作者：</font>** Yue Zhang, Zhiyi Dong, Tommaso Cesari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a learning-theoretic framework for understanding Chain of Thought (CoT). We model CoT as the interaction between an answer map and a chain rule that generates intermediate questions autoregressively, and define the reasoning risk of a hypothesis under this interaction. Our first result is a tight canonical decomposition of this risk into two terms with opposing roles: an oracle-trajectory risk (OTR), which captures the benefit of CoT and reduces to a target-domain risk in a domain adaptation problem, and a trajectory-mismatch risk (TMR), which captures the cost of CoT through error accumulation along mismatched reasoning trajectories. We then show that this cost is unavoidable without structure: if any one of the loss, the hypothesis answer map, or the chain rule lacks stability, the TMR can be arbitrarily large even when the OTR is zero and the hypothesis is uniformly close to the ground truth. Conversely, under stability, we prove a tight upper bound on the TMR governed by an exact amplification factor that identifies bounded, linear, and exponential error-growth regimes. Together, these results give a precise theory of when CoT helps, when it hurts, and what controls the transition between the two.

---


### 292. [STiTch: Semantic Transition and Transportation in Collaboration for Training-Free Zero-Shot Composed Image Retrieval](https://arxiv.org/abs/2605.21261)

**<font color=#1a73e8>作者：</font>** Miaoge Li, Dongsheng Wang, Zening Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free zero-shot composed image retrieval models are recently gaining increasing research interest due to their generalizability and flexibility in unseen multimodal retrieval. Recent LLM-based advances focus on generating the expected target caption by exploring the compositional ability behind the LLMs. Although efficient, we find that 1) the generated captions tend to introduce unexpected features from the reference image due to the semantic gap between the input image and text modification, where the image contains much more details than the text; 2) the point-to-point alignment during the retrieval stage fails to capture diverse compositions. To address these challenges, we introduce a novel Semantic Transition and Transportation in collaboration framework for training-free zero-shot CIR tasks. Specifically, given the composed caption inferred by an LLM, we aim to refine it through a transition vector in the embedding space and make it closer to the target image. Combining LLMs with user instruction, the refined caption concentrates more on the core modification intent and thus filters out unnecessary noise. Moreover, to explore diverse alignment during the retrieval stage, we model the caption and image as discrete distributions and reformulate the retrieval task as a set-to-set alignment task. Finally, a bidirectional transportation distance is developed to consider fine-grained alignments across modalities and calculate the retrieval score. Extensive experiments demonstrate that our method can be general, effective, and beneficial for many CIR tasks.

---


### 293. [Nonparametric Learning and Earning with One-Point Feedback under Nonstationarity](https://arxiv.org/abs/2605.21263)

**<font color=#1a73e8>作者：</font>** Xiangyu Yang, Feng Xu, Jian-Qiang Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Firms increasingly rely on dynamic pricing to respond to evolving customer demand, yet in many applications they observe only the revenue generated by a single posted price in each period. At the same time, market conditions may shift gradually or abruptly due to changes in customer preferences, competition, or external shocks. These features create two intertwined challenges: learning the revenue--demand relationship from limited feedback and adapting pricing decisions to a changing environment. We study how a seller can learn and earn effectively under these constraints, without assuming a specific parametric form for demand. We develop a learning framework that updates prices using revenue-based gradient approximations constructed from one observation per period. To address environmental changes, we incorporate a restarting mechanism that periodically refreshes the learning process so that outdated information is discounted. When the degree of nonstationarity is unknown, we further introduce a meta-learning layer to adaptively hedge across multiple restarting schedules. We provide performance guarantees for our approach, showing how cumulative revenue loss relative to a fully informed benchmark depends on both the time horizon and the magnitude of market variation. Simulation experiments using synthetic and real-world data illustrate the effectiveness of the proposed procedures.

---


### 294. [Vision Transformers and Convolutional Neural Networks for Land Use Scene Classification](https://arxiv.org/abs/2605.21268)

**<font color=#1a73e8>作者：</font>** Arun D. Kulkarni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Land Use Scene Classification (LUSC) from remote sensing imagery plays a critical role in environmental monitoring, urban planning, and sustainable resource management. In recent years, deep learning methods have significantly advanced the state of the art, with Convolutional Neural Networks (CNNs) dominating the field because of their strong ability to capture local spatial features. However, the emergence of Vision Transformers (ViTs) has introduced a new paradigm that models long-range dependencies through self-attention mechanisms, potentially enabling improved global context understanding. This paper presents a comparative assessment of Vision Transformers and CNN-based architecture for remote sensing land use scene classification. Representative CNN models, such as AlexNet, is evaluated alongside the Vision Transformer (ViT) using benchmark remote sensing datasets, including the UC Merced Land Use and EuroSAT Land Use datasets. The study examines classification accuracy, precision, recall, F1-score, and computational complexity to provide a comprehensive performance comparison. Experimental results demonstrate that CNNs perform robustly on datasets with limited training samples and strong local texture characteristics, whereas Vision Transformers exhibit superior performance in capturing global spatial relationships in complex scenes when sufficient training data are available. However, ViTs typically require greater computational resources and larger training datasets to achieve optimal performance. The findings of this study provide insights into the strengths and limitations of both architectures and offer guidance for selecting appropriate models for remote sensing land use scene classification applications.

---


### 295. [MONET: A Massive, Open, Non-redundant and Enriched Text-to-image dataset](https://arxiv.org/abs/2605.21272)

**<font color=#1a73e8>作者：</font>** Benjamin Aubin, Gonzalo Iñaki Quintana, Onur Tasar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training large text-to-image models requires high-quality, curated datasets with diverse content and detailed captions. Yet the cost and complexity of collecting, filtering, deduplicating, and re-captioning such corpora at scale hinders open and reproducible research in the field. We introduce MONET, an open Apache 2.0 dataset of approx. 104.9M image--text pairs collected from 2.9B raw pairs across heterogeneous open sources through successive stages of safety filtering, domain-based filtering, exact and near-duplicate removal, and re-captioning with multiple vision-language models covering short to long-form descriptions, and further augmented with synthetically generated samples. Each image is shipped with pre-computed embeddings and annotations to accelerate downstream use. To validate the effectiveness of MONET, we train a 4B-parameter latent diffusion model exclusively on it and reach competitive GenEval and DPG scores, demonstrating that our dataset lowers the barrier to large-scale, reproducible text-to-image research.

---


### 296. [DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions](https://arxiv.org/abs/2605.21273)

**<font color=#1a73e8>作者：</font>** Weicheng Zheng, Yixin Huang, Qiao Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving Vision-Language-Action Models (Driving VLAs) commonly introduce natural-language reasoning as an intermediate interface for end-to-end planning, but reasoning-centric interfaces face three practical bottlenecks: obtaining high-quality reasoning annotations is difficult, generating and understanding long reasoning chains is challenging for compact models, and inference latency is substantially increased. In this paper, we rethink the design of language interfaces in Driving VLAs and show that concise one-step meta-actions are a simple yet effective alternative to verbose reasoning. Meta-actions provide semantic decision grounding while remaining low-entropy, and being automatically derivable from expert trajectories, enabling scalable supervision and reliable trajectory conditioning. Building on this interface, we propose DriveMA, which combines action-centric supervised training with a turn-level credit-assignment reinforcement learning framework that jointly optimizes meta-action correctness, trajectory quality, and trajectory--meta-action consistency. Experiments show that DriveMA already achieves a new state of the art on the Waymo End-to-End Driving Challenge with a 2B model, reaching a Rater Feedback Score (RFS) of 8.060, while its 4B version further improves the state of the art to 8.079; DriveMA also obtains competitive performance on NAVSIM. Ablations demonstrate that one-step meta-actions offer a better practical trade-off between expressiveness, predictability, and inference efficiency than natural-language reasoning or finer-grained action sequences. Code, data, and models will be released to facilitate future research.

---


### 297. [Let EEG Models Learn EEG](https://arxiv.org/abs/2605.21280)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Yijia Ma, Wen Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity EEG generation is critical for alleviating data scarcity and addressing privacy constraints in large-scale neural modeling. Despite recent progress, most existing approaches formulate EEG generation via discrete denoising objectives, which inadequately reflect the inherently continuous temporal dynamics and spectral structure of neural activity. As a result, these methods often struggle to preserve long-range temporal dependencies and exhibit mismatches in the spectral and temporal structure of the generated signals. In this work, we argue that effective EEG generation requires models that operate directly on the continuous evolution of neural signals. We introduce Just EEG Transformer (JET), a generative framework based on conditional flow matching that models EEG as raw sequences evolving along continuous trajectories. By learning a smooth vector field that transports noise to the EEG data distribution, JET captures temporal continuity and transient dynamics without relying on discretized denoising schemes or domain-specific representations. To ensure that the learned dynamics remain consistent with key properties of EEG signals, we introduce principled constraints that preserve spectral structure, temporal stationarity, and signal-level statistics. Across three large-scale benchmarks, JET consistently achieves state-of-the-art performance, reducing TS-FID by over 40% compared to strong baselines. Extensive analyses show that JET captures key structural properties of neural dynamics, providing a scalable and principled approach to EEG generation. Project page: this https URL .

---


### 298. [\textit{Stochastic} MeanFlow Policies: One-Step Generative Control with Entropic Mirror Descent](https://arxiv.org/abs/2605.21282)

**<font color=#1a73e8>作者：</font>** Zeyuan Wang, Da Li, Yulin Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online off-policy reinforcement learning (RL) is shaped by two coupled choices: the policy class and the update rule. Gaussian policies are fast and have tractable entropy, but struggle with multimodal action distributions. Generative policies are more expressive, but often require iterative sampling or lack tractable entropy estimates. On the optimisation side, SAC-style soft policy improvement and mirror descent (MD) can be viewed as minimising different KL divergences: the former moves the policy towards a value-induced Boltzmann distribution, while the latter regularises each update against the previous policy. Combining entropy regularisation with an MD constraint is therefore attractive, as it supports exploration while stabilising policy improvement; however, the resulting target can be multimodal and is poorly matched by unimodal Gaussian policies. We propose Stochastic MeanFlow Policies (SMFP), a one-step generative policy class that maps Gaussian noise to actions through a MeanFlow transformation. This stochastic reparameterisation yields a tractable entropy surrogate and allows MeanFlow policies to be trained within off-policy mirror descent under a unified objective for exploratory yet stable improvement. Across seven MuJoCo benchmarks, SMFP improves over Gaussian and generative baselines while retaining single-step inference efficiency.

---


### 299. [Automatic Discovery of Disease Subgroups by Contrasting with Healthy Controls](https://arxiv.org/abs/2605.21301)

**<font color=#1a73e8>作者：</font>** Robin Louiset, Edouard Duchesnay, Benoit Dufumier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In biomedical Subgroup Discovery, practitioners are interested in discovering interpretable and homogeneous subgroups within a group of patients. In this paper, assuming that healthy subjects (i.e., controls) share common but irrelevant factors of variation with the patients, we motivate and develop a Contrastive Subgroup Discovery method, entitled Deep UCSL. By contrasting patients with controls, Deep UCSL identifies subgroups driven solely by pathological factors, ignoring common variability shared with healthy subjects. Our framework employs a deep feature extractor to learn a discriminative representation space. Mathematically, we derive a novel loss based on the conditional joint likelihood of latent clusters and patient/control labels, optimized via an Expectation-Maximization strategy alternating between subgroup inference and feature encoder updates. A regularization term further encourages representations to capture disease-specific variability while ignoring variability shared with controls. Compared to previous related works, our approach quantitatively improves the quality of the estimated subgroups, as demonstrated on a MNIST example and four distinct real medical imaging datasets. Code and datasets are available at: this https URL.

---


### 300. [From Circuit Evidence to Mechanistic Theory: An Inductive Logic Approach](https://arxiv.org/abs/2605.21303)

**<font color=#1a73e8>作者：</font>** Nura Aljaafari, Danilo S. Carvalho, Andre Freitas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability produces circuit-level causal analyses of neural network behaviour, but discovered circuits often remain isolated experimental artefacts: there is no shared formal representation for what circuits compute, how they relate, or when two findings provide evidence for the same mechanism. This work provides a formal infrastructure for cumulative mechanistic science by treating circuit interpretation as inductive theory construction. Each circuit is characterised at two levels: a Causal Functional Signature (CFS), which grounds component behaviour in causal attribution evidence and token role profiles, and an architectural signature $\tau_{\mathrm{arch}}$, learned by inductive logic programming (ILP) from scale-invariant structural predicates. Together, these constitute a formal coherence layer that makes mechanistic claims explicit, comparable via $\theta$-subsumption, and portable across model scales. CFS reveals qualitatively distinct computational strategies across task types, including attention-mediated copying versus MLP-mediated binding. ILP signatures achieve substantially better structural separation than graph kernel and feature-vector baselines, and support principled transfer across model scales and architecture families.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-352](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
