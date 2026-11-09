# 📦 其他研究 | 2026年11月10日

> 本类共 **222** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-222](./part-05.md)

---

### 51. [Lea: An Agent Backbone for Mathematician-Controlled Formalization in Lean](https://arxiv.org/abs/2611.08849)

**<font color=#1a73e8>作者：</font>** Shaswat Patel, Daniel Aarao Reis Arturi, Kevin Gomez 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Agentic systems now formalize research-level mathematics in Lean, but they are built for autonomy: the mathematician states a target and inspects a result. The alternative, a general-purpose coding harness, is domain-neutral and must be assembled into a formalization workspace before any mathematics begins. Mathematicians, however, report wanting to keep high-level control over how an argument is decomposed and established. We present $\textbf{Lea}$, a Lean-specific agent backbone for mathematician-facing software rather than a single interface. Lea exposes runs, sessions, and typed events through one application-neutral API, and ships with Lean tooling (blueprints, LSP, Loogle, SafeVerify) already wired. We report two applications built on it: $\textbf{LeaChat}$, a web client for interactive proof authoring, and $\textbf{LeaOverleaf}$, which formalizes theorems annotated directly in an Overleaf document; a session begun in either continues in the other. In a case study, a mathematician outlined a proof of the Durfee square generating function in a few natural-language messages, and Lea produced a complete Lean development from Mathlib alone, following the intended decomposition closely and requiring substantive correction at a single point. Lea and both applications are released as open source so that further mathematician-facing tools can be built on the same backbone.

---


### 52. [Align3D: Image-Structure Co-Aligned 3D Scene Generation with Observability-Aware Fidelity-Preserving Guidance](https://arxiv.org/abs/2611.08861)

**<font color=#1a73e8>作者：</font>** Chenliang Zhou, Yifan Wang, Andrzej Banburski-Fahey  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Align3D, an image-conditioned diffusion model that generates 3D indoor layouts that are both faithful to a single input photograph and physically plausible beyond the observed view. From the photograph we infer a confidence-calibrated scene graph and train a set-diffusion layout denoiser with image-structure co-alignment where confidence-weighted modality fusion balances image and scene-graph alignment using predicted confidences, while observability-aware fidelity-preserving guidance projects conflicting scene-quality gradients and reweighs them with an object-level confidence mask so under-observed degrees of freedom absorb physical priors without undoing the image-graph match. On 3D-FRONT, Align3D improves image-alignment and scene-quality metrics over recent baselines; once trained, it maps previously unseen photographs to layouts in a single feed-forward pass.

---


### 53. [Rethinking Agent Trajectory Compression: A Workflow-Aware Perspective](https://arxiv.org/abs/2611.08865)

**<font color=#1a73e8>作者：</font>** Qijia Zhuang, Rui Liu, Yuxiang Ren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As long-horizon agents increasingly rely on multi-step tool interactions to accomplish complex tasks, their execution trajectories continuously accumulate structured outputs and intermediate artifacts, leading to growing context overhead. Existing compression methods primarily rely on text importance or fixed truncation rules, often overlooking cross-step dependencies within workflows and potentially discarding critical information required for subsequent task execution. To address this challenge, we propose WAAC, a workflow-aware framework for agent trajectory compression. WAAC structurally models successful historical trajectories to extract reusable workflow compression experience and incorporates online backward dependency analysis to dynamically identify information retention requirements. By combining current dependency constraints with historical experience, WAAC selects appropriate compression strategies for different types of historical information. Experiments on PinchBench and Odysseys demonstrate that WAAC achieves an overall score of 87.6 and a perfect completion rate of 19.0%, respectively, while reducing execution costs by 19.7% and 29.1% compared with the strongest baseline methods. These results demonstrate the effectiveness of workflow-aware trajectory compression in improving task performance and cost efficiency for long-horizon agents. Code and resources are available at this https URL.

---


### 54. [Bidirectional Modeling of mmWave Human Signals for Enhancement & Synthesis](https://arxiv.org/abs/2611.08870)

**<font color=#1a73e8>作者：</font>** Shuntian Zheng, Hoang Hai Pham, Jiaqi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Millimeter-wave (mmWave) is attractive for human-centered robotics in smoke, darkness, and privacy-sensitive indoor spaces: it measures reflections rather than visually identifiable imagery and remains usable without light. Deployed systems, however, face two complementary needs that run in opposite directions. Enhancement starts from a raw range-angle-Doppler (RAD) heatmap, where human returns coexist with nonhuman structure, and aims to isolate the human signal by removing nonhuman returns, yielding a clean RAD input for downstream perception. Synthesis starts from denser human geometry and aims to synthesize natural RAD observations, including environmental and hardware features, thereby expanding scarce supervision data. Although the two tasks reverse direction, both require modeling how human and nonhuman reflections coexist in the same measurement. Among RAD axes, Doppler provides motion information native to the modality, with the potential to support this modeling. We therefore cast both tasks on the dual-domain RAD heatmap and propose HeatWave, which injects Doppler when it is locally reliable, and routes Doppler asymmetrically for enhancement and synthesis within one shared backbone. This design improves both tasks: enhanced observations reduce mean per-joint position error by 11.4% relative to the raw recording, and synthesized samples that replace half of the real radar labels recover most of the activity accuracy lost to the reduced budget. Relative to an unspecialized dual-task heatmap baseline, the enhancement improves motion-critical samples under metallic clutter by 2.3times more than when geometry already suffices, and synthesis follows the same ordering with a narrower spread, providing the community with a research direction more closely aligned with the signal's characteristics.

---


### 55. [The Relational Capacity Framework: A Lens for AI-Mediated Relationality](https://arxiv.org/abs/2611.08877)

**<font color=#1a73e8>作者：</font>** Emily Tseng, Patrick Gage Kelley, Renee Shelby 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A growing literature examines the impact of engaging with AI chatbots on our relationality: our ability to form relationships with others, maintain them through life's changes, and exit when needed. Currently, substantial work focuses on purpose-built AI companions (e.g. Replika, this http URL), with less work investigating socioemotional uses of the more widely-used general-purpose chatbots. In this paper, we present a 100-person investigation into how people engage general-purpose AI for socioemotional needs. Participants' AI uses varied, from practicing specific social skills to seeking additional bandwidth and information as they navigated their social contexts. To explain this heterogeneity, we provide 8 states that describe how AI expands or contracts relationality for people with different levels of skills, bandwidth, and information. We then present a unified conceptual model for the role of technology in mediating human relationality, the Relational Capacity Framework, and outline future research designing appropriate roles for AI in human connection.

---


### 56. [Learning to Restart: Differentiable Restart Policies for Optimization Dynamics](https://arxiv.org/abs/2611.08883)

**<font color=#1a73e8>作者：</font>** Yiman Fong, Zhonglin Xie, Zaiwen Wen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive restart mechanisms, which reset the momentum or other auxiliary state of an iterative optimizer, play a central role in the empirical performance of accelerated first-order methods, yet existing restart rules remain almost entirely hand-designed. The obstruction to learning restart policies is that, unlike the typical Learning to Optimize (L2O) setting, the discrete restart events make the resulting trajectory non-differentiable in the algorithm parameters and thus block gradient-based optimization of the restart policy. We resolve this obstruction by developing a differentiable framework for restart policies through their continuous-time limit. We introduce surrogate gradients for the restart events and optimization trajectories that are efficient to compute and provably converge to their continuous-time counterparts. We validate the effectiveness of our surrogate gradients in L2O settings, training restart policies that improve upon standard handcrafted adaptive restart criteria on quadratic and linear programs, and that transfer zero-shot from synthetic quadratics to logistic regression on real datasets.

---


### 57. [Who's Asking? Audience-Conditioned Privatization](https://arxiv.org/abs/2611.08884)

**<font color=#1a73e8>作者：</font>** Daniil Filienko, Anusha Bagalkotkar, Xan Vongsathorn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The abundance of user-generated conversational data makes the question of how to responsibly derive insights from confidential data without putting the individuals in it at risk ever more important. However, the majority of existing differentially private (DP) synthetic text generation (SDG) and anonymization approaches ignore the context of the data's downstream usage, which results in loss of important information. DP-SDG provides the same guarantee regardless of the recipient, and anonymization relies on predefined attribute categories. They both ignore the observation that an attribute that is harmless to one audience can be sensitive to another, and each audience typically needs only some attributes preserved. We propose Ext-Classify-Priv, a framework that (1) extracts the information types present in a corpus, (2) classifies which of them are private for a given audience following contextual integrity, and (3) protects only those attributes, using either anonymization or SDG with Feature-DP approaches. On Reddit data with 3 audiences, our audience-specific releases are more faithful than a single audience-agnostic release for every audience. On bioRxiv data, our SDG method improves MAUVE from 0.097 to 0.420 at epsilon=1 and on the proprietary real estate data, our anonymization method improves MAUVE from 0.698 to 0.959 over the best baselines.

---


### 58. [Computer Vision by YOLOs for Detection of Major Diseases in Vietnamese Custard Apple Using Fruit Imagery](https://arxiv.org/abs/2611.08886)

**<font color=#1a73e8>作者：</font>** Tri Nhut Do, Quoc Tuan Vo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Amid Vietnam rapid digital transformation in agriculture, the integration of artificial intelligence technologies for identifying, monitoring, and predicting crop pests and diseases has emerged as an inevitable trend.

---


### 59. [Decoding spatial and semantic information from large-scale visual cortical activity for natural-movie reconstruction](https://arxiv.org/abs/2611.08887)

**<font color=#1a73e8>作者：</font>** Yukai Huang, Haoyu Albert Wang, Jiawei Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing natural visual experience from cortical population activity is a central challenge in neural decoding, particularly for calcium imaging, where signals are noisy, temporally filtered, and paired neural-video data are limited. Here we present Ca2REAL (Calcium Activity to Reconstruct Events, Appearance, and Layout), a neural-to-video framework that conditions a pretrained video diffusion model through separate layout and semantic controls derived from calcium activity. Using measured responses from 7,863 V1 neurons in one mouse, Ca2REAL reconstructed held-out natural-movie clips with 81.4% all-pairs stimulus-identification accuracy, with its clearest gains over deterministic baselines in perceptual and semantic measures. We further evaluated the framework in a stimulus-aligned virtual population of 116,705 neurons assembled from encoding-model-predicted responses across 11 independently recorded datasets. Perturbation and ablation analyses showed that reconstruction depends on distributed, stimulus-specific population structure, with layout and semantic pathways providing complementary spatial and identity information. Temporal analyses further showed improved preservation of semantic dynamics across reconstructed clips. These results show that large-scale cortical population activity constrains the spatial, semantic, and temporal structure of natural visual experience, providing a generative framework for high-fidelity neural reconstruction of dynamic visual scenes.

---


### 60. [MotionCore: A Latent Neural Simulator for Video Generation with Rigid-Body Dynamics](https://arxiv.org/abs/2611.08904)

**<font color=#1a73e8>作者：</font>** Zheng Wang, Zhengwei Gong, Yuanzhi Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models can produce highly realistic videos while generating physically inconsistent object motion. This limitation suggests that visual modeling alone may not provide a transferable representation of physical dynamics. We introduce MotionCore, a framework for learning physical dynamics via a learnable partial differential equation solver and focuses on rigid-body motion. We introduce a latent neural simulator learning to predict the evolution of object-level physical states from observed motion. Its predictions are then converted into spatially aligned latent controls for a controllable video diffusion model. The generator serves as a visual interface: it provides appearance and scene detail, while the learned dynamics model specifies the physical trajectory. To preserve this trajectory through the interface, MotionCore combines a diffusion-matching objective with a low-capacity decodability constraint on object identity and position. We evaluate MotionCore on public physical-consistency benchmarks and on paired data with known trajectories. Results indicate that MotionCore improves physical consistency and trajectory obedience in the evaluated rigid-body settings, while maintaining comparable visual quality. A controlled ablation protocol compares learned dynamics with an analytic prior and studies the choice of latent evolution processor.

---


### 61. [SSF-Net: A Spatial-Spectral Fusion Network for Accurate PDE Operator Learning](https://arxiv.org/abs/2611.08912)

**<font color=#1a73e8>作者：</font>** Siqi Zhao, Flora D. Salim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning methods for solving partial differential equations (PDEs) significantly improve computational efficiency over traditional numerical solvers such as finite element method (FEM). However, PDE dynamics inherently span both local and global dynamics: disturbances propagate and decay gradually through the domain, while global coupling effects can influence the whole system simultaneously. Capturing both types of dynamics with a low complexity model remains a key challenge. To address this, we propose the Spatial-Spectral Fusion Network (SSF-Net), built around a dual-branch Spatial-Spectral Fusion (SSF) block comprising a spatial branch and a spectral branch. The spatial branch employs a multi-directional Mamba, which mitigates its inherent causal, single-direction scanning bias and capture local interactions with reduced directional bias at linear complexity. The spectral branch leverages a Fourier transform with a block-diagonal MLP to efficiently capture global spectral features with reduced parameter count and complexity. The SSF block is embedded in a multiresolution convolutional encoder-decoder, which extracts multi-scale features. We evaluate SSF-Net on a comprehensive PDE benchmark spanning multiple task types and assess its long-horizon stability. Compared with attention-based and convolution-based baselines, SSF-Net achieves lower prediction error with fewer parameters while retaining near-linear asymptotic complexity in the number of spatial tokens.

---


### 62. [On the Incompleteness of do-calculus for Universal Identifiability](https://arxiv.org/abs/2611.08916)

**<font color=#1a73e8>作者：</font>** Yaroslav Kivva, Aliaksandra Novik, Negar Kiyavash  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study the problem of causal effect identification from an arbitrary set of observational and/or interventional distributions, which we call Universal Identifiability (uID). The uID problem generalizes existing classical identifiability (ID) and general identifiability (gID) problems, which considered the identification problem from either mere observational distributions or a specific type of interventional distributions. Prior research has established graphical criteria to determine when a causal effect is identifiable in ID and gID problems. Moreover, algorithms that leverage do-calculus and basic probability manipulations have been proposed to compute these effects. Consequently, it has been shown that do-calculus is both sound and complete in these problems. Despite these well-established results, a formal definition of what it means for the do-calculus to be complete does not exist. We propose a rigorous formalization for the completeness of the do-calculus and show that the completeness results in previous work remain valid. However, for more general problems, such as uID, the rules of do-calculus are no longer complete. This is perhaps the reason why the uID problem has remained open thus far.

---


### 63. [Composable Causality: A Toolkit for Systematic Time-Series Causal Discovery and Treatment-Effect Benchmarking](https://arxiv.org/abs/2611.08918)

**<font color=#1a73e8>作者：</font>** Muhammad Hasan Ferdous, Md Osman Gani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world multivariate time series rarely come with verified ground-truth causal structure, so research on time-series causal discovery and treatment-effect estimation depends on synthetic data. Existing tools are either fixed datasets that cannot be modified after release or script-based generators in which each script fixes one combination of mechanism, confounding, and missingness. Neither supports controlled experiments that vary a single property, such as sparsity, noise distribution, or missingness mechanism, while holding the others fixed. Counterfactual evaluation has the same gap, since existing simulators are built per paper with hardcoded mechanisms or produce observational data only. We introduce DTCD (Datasets and Toolkit for Causal Discovery), a data generation library that produces multivariate time series with ground-truth contemporaneous and lagged adjacency matrices. Topology, mechanism, noise, observational mask, and intervention policy are independent components that compose through configuration alone. Paired counterfactual twins, produced by caching the stochastic realization during the factual rollout and re-injecting it during the interventional rollout, recover individual treatment effects to numerical precision. A reference benchmark of eight discovery algorithms on eighty-one configurations and four treatment-effect estimators on eighteen configurations exposes failure modes that aggregate metrics hide. These include the inability of standard discovery methods to handle missing values, regardless of whether the missingness mechanism is informative, and a marginal-variance shortcut (varsortability) that we measure and remove by standardization. Code and data: this https URL

---


### 64. [Glyph: An Interpretability Engine for AI-Driven Scientific Discovery in Clinical Data](https://arxiv.org/abs/2611.08922)

**<font color=#1a73e8>作者：</font>** Robbie Holland, Ashwin Kumar, Mateus A. Esmeraldo 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated scientific discovery has the potential to advance understanding of disease mechanisms and accelerate identification of early disease markers. Manual data annotation is infeasible at population scale, motivating methods that automatically extract pre-defined phenotypes in multimodal and unstructured clinical data. Such pre-defined feature sets determine and limit which associations these approaches can discover. This limitation extends to agentic AI systems that use these tools to query population-scale data. In contrast, foundation models (FMs) trained on large volumes of clinical data can perform tasks beyond their training objectives. This suggests their latent embeddings may represent novel or unexplored features that could yield insights into disease mechanisms, yet such latent features remain difficult to interpret. To address this challenge, we introduce Glyph, an automated multistage framework that extracts features from multimodal and unstructured clinical data using FMs and sparse autoencoders, interprets them as coded clinical concepts, and evaluates their value for clinical scientific discovery. We applied Glyph to abdominal CT volumes, CT radiology reports and laboratory measurements from 41,628 patients across different institutions. We identified 397 predictive concepts supported by 4,463 Bonferroni-significant associations. Moreover, a majority of discovered associations were automatically reproducible in held-out cohorts across different sites. Glyph concepts provided complementary associations to literature-derived markers, leading to gains in predictive power. We envision that interpretability can extend beyond a mechanistic understanding of neural networks to connecting implicitly learned features with clinical knowledge and establishing their significance for patient outcomes. We release Glyph at this https URL.

---


### 65. [FANO: Anchored Forward-Noise Optimization for Diffusion Inverse Problems](https://arxiv.org/abs/2611.08923)

**<font color=#1a73e8>作者：</font>** Shilong Han, Hongxia Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained diffusion models have become a widely adopted zero-shot prior for image inverse problems, among which annealed decoupling methods achieve leading reconstruction performance on nonlinear tasks. We find, however, that annealed methods that directly optimize the denoiser input $x_t$ exhibit radial drift in later layers: within-layer optimization drives the noise-component norm of $x_t$ away from its typical value, pushing the denoiser out of its high-performance regime and degrading reconstruction quality. To address this, we propose FANO (Anchored Forward-Noise Optimization). At each annealing layer, FANO fixes the previous denoiser estimate as an anchor and optimizes only the forward noise $e$, whose distribution is known, instead of $x_t$, thereby preserving the forward-diffusion structure of the denoiser input. The standard Gaussian prior on $e$ concentrates its norm near the typical value, and deviations degrade denoiser performance. We accordingly decompose $e$ in polar coordinates into a direction and a radial magnitude, and apply a soft potential to regulate the radius, keeping $x_t$ in the high-density region of the forward distribution. On multiple linear and nonlinear inverse problems, FANO matches the strongest current baselines on linear tasks and achieves consistent improvements on nonlinear tasks.

---


### 66. [UAV-Based Computer Vision for Cattle Detection and Feed Bunk Spatial Analysis](https://arxiv.org/abs/2611.08928)

**<font color=#1a73e8>作者：</font>** Pedro Oliveira Torrente, Diego Giaretta de Paulo, Lucas Pascotti Valem 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Beef cattle production is central to Brazilian agribusiness and faces growing demands for efficiency, sustainability, and animal welfare. Precision Livestock Farming (PLF) offers tools to address these challenges, particularly through monitoring feeding-related spatial patterns in confined systems. Feeding management plays a decisive role in animal performance, yet its evaluation still relies largely on subjective, labor-intensive visual inspections that are hard to scale and prone to bias. This work proposes a computer vision framework based on Unmanned Aerial Vehicles (UAVs) to quantify cattle alignment and spatial dispersion at the feed bunk under real-world feedlot conditions. A UAV dataset was collected during flight campaigns at a commercial feedlot in Mato Grosso do Sul, Brazil. Images were manually annotated into cattle head and cattle back classes to support object detection and image-level spatial analysis of cattle distribution. You Only Look Once (YOLO) models, namely YOLOv8 and YOLOv11, were evaluated, with YOLOv8 small used for the downstream spatial analysis. The feed bunk region was segmented using the Segment Anything Model (SAM), and geometric metrics based on detected head positions were developed to characterize alignment, spacing regularity, and clustering. The selected detector achieved 84.30% mAP50 and 35.50% mAP50-95, with an inference time of approximately 2.7 ms per image on an NVIDIA RTX 5060 Ti GPU. The resulting metrics distinguished representative regular and irregular spatial distributions by Root Mean Square Deviation - RMSD (1.06 m and 4.26 m), Coefficient of Variation - CV (42.70% and 96.31%), and clustering (0 and 2 clusters), respectively. These findings indicate that the proposed approach can provide indicators for assessing feed bunk spatial patterns in PLF.

---


### 67. [Ordered Policy Optimization](https://arxiv.org/abs/2611.08936)

**<font color=#1a73e8>作者：</font>** Dongkyu Derek Cho, Pan Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proximal Policy Optimization (PPO) stabilizes policy updates by clipping the importance ratio between the new policy and the data-collecting policy. The standard rule uses one fixed clipping range for all samples. While this choice offers simplicity and effectiveness, it fails to distinguish statistically harmful extreme ratio values from large, yet tolerable changes. We study how to adapt the clipping radius to the reliability of the induced importance ratio distribution. Our case study demonstrates that reliable updates require controlling these extreme ratios, rather than merely verifying that individual ratios fall within a fixed interval. Motivated by this observation, we propose Ordered Policy Optimization (\textsc{OPO}). In each minibatch, \textsc{OPO} sorts the importance ratios, selects the extreme ratios that potentially have the largest effect on the update, and assigns them adaptive sample-wise radii instead of using the fixed clipping radius. These radii are derived from a prescribed tail profile, which specifies desired target values for the selected extreme ratios. The resulting objective remains first-order and requires only minibatch sorting and a modified policy loss. Experiments conducted on MuJoCo and Atari benchmarks demonstrate that this simple modification achieves strong performance relative to established baselines.

---


### 68. [Surrogate Quality Score: A Novel Composite Performance Metric for Model Selection](https://arxiv.org/abs/2611.08937)

**<font color=#1a73e8>作者：</font>** Maaz Ahmad, Iftekhar A. Karimi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing reliance on high-fidelity, state-of-the-art machine learning based models for engineering decision-making necessitates robust and systematic approaches for model selection. While high predictive accuracy at untrained points is a necessary trait in the final model, other attributes such as model complexity, forecastability, explainability, scalability, and physics-awareness may be equally important or relevant criteria depending on application context and user requirements. In this work, we propose a novel composite performance metric, Surrogate Quality Score (SQS) for model selection based on predictive accuracy and model complexity simultaneously. SQS heuristically integrates these two attributes through a weighted product of normalized measures, yielding a unified score to reflect overall model quality. A user-specified parameter in SQS enables explicit control over the accuracy-complexity trade-off, thereby incorporating human judgement and preference in the model selection process. We extensively discuss and justify the formulation of SQS and demonstrate its utility through an illustrative example. By combining predictive accuracy and model complexity, SQS offers a systematic and objective approach for model selection based on both attributes.

---


### 69. [MESAM: Enhancing SAM2 for Few-Shot Segmentation through Semantic-Visual Memory Generation and Refinement](https://arxiv.org/abs/2611.08943)

**<font color=#1a73e8>作者：</font>** Tianyu Zou, Shengwu Xiong, Rui Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper investigates how to leverage the powerful capabilities of the Segment Anything Model 2 (SAM2) to tackle few-shot segmentation (FSS) tasks. One major challenge lies in the substantial appearance differences between the support and query images, which may diminish the effectiveness of the memory-matching process in SAM2. Through systematic analysis, we find that the memory generated based on the categorical semantic information is robust to this appearance divergence and is more compatible with SAM2. Based on these observations, we propose a new Memory-Enhanced SAM2 (MESAM) method, which first introduces a Semantic-Visual Memory Generation (SVMG) module to separately construct a query semantic memory, a query foreground visual memory, and a support adaptive visual memory. Then, in our designed Interactive Semantic Memory Refinement (ISMR) module, we further enrich the obtained semantic memory with fine-grained visual details, and suppress its misatcivated background responses. Extensive experiments on the PASCAL-$5^i$, COCO-$20^i$, and LVIS-$92^i$ datasets demonstrate that MESAM consistently outperforms existing FSS methods, achieving new state-of-the-art segmentation performance. Our source code is available at: \href{this https URL}{this https URL}.

---


### 70. [MetricPose: Flexible 3D Human Pose Estimation with Depth and Geometric Cues](https://arxiv.org/abs/2611.08954)

**<font color=#1a73e8>作者：</font>** Shifan Zhu, Sabad Modi, Hang Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a 3D human pose estimator that predicts metrically accurate human joint positions in the camera coordinate frame. This task requires recovering the configuration of the body joints, scale, and metric camera-local placement. In monocular images, body size and camera distance are coupled through perspective projection and therefore cannot be determined uniquely from image alone. This ambiguity can be reduced by combining three complementary sources of information: learned RGB priors, direct depth measurements, and geometric constraints (e.g., ground contact) from the environment. We extend a pretrained full-body estimator with optional metric depth and geometry-processing modules that improve camera-distance estimation and depth-guided body refinement while preserving RGB-only operation. The resulting unified model supports RGB, RGB-Ground, and RGB-D using shared learned parameters. Unlike pelvis-relative error, camera-local error also measures placement relative to the camera. Compared with the existing foundation model SAM 3D Body, our methods with RGB, RGB-Ground, and RGB-D modes reduce camera-local joint-position error by 12.16%, 31.00% and 54.61% respectively.

---


### 71. [Accuracy Is Not Value: Choosing Weak Supervisors by What the Student Inherits](https://arxiv.org/abs/2611.08959)

**<font color=#1a73e8>作者：</font>** Romano Li, Xunfan Cai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weak supervisors are usually judged by their own errors, but what matters is what a student learns from them. For squared loss and any linear learner shared by all supervisors, we show that a supervisor's value is determined by its errors after they pass through the student's learning operator. Consequently, the inner products of the supervisors' raw errors can be compatible with every feasible value of the student's risk, and weighting supervisors by them can be arbitrarily worse than the best weighting in relative excess risk. This student-relative value is not identifiable from unlabeled data, but what is missing is small: one finite-dimensional projection of the target decides whether training on a weak aggregate helps, another decides how to weight the supervisors. Known teacher training rules, or a label-model condition stated in student-relative form, shrink it further. Clean labels close the remaining gap at a cost set by the geometry of the unresolved directions rather than by the dimension of the student's representation, with matching worst-case lower bounds. In Gaussian designs we also quantify when exact teacher structure beats ordinary stacking and when weak supervisors, combined with clean labels, beat every procedure that uses the clean labels alone. The guarantees extend to fitted ridge students and finite unlabeled data.

---


### 72. [Region-aware error triage for medical image segmentation with groupwise conformal risk control](https://arxiv.org/abs/2611.08962)

**<font color=#1a73e8>作者：</font>** Nishi Kanta Paul, Md Shihabul Islam Shovo, Hoileong Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation masks are increasingly reviewed rather than redrawn, which requires knowing where a mask is likely wrong. Learned error maps rank pixels by risk, but the number of pixels to warn is chosen ad hoc, and calibrating one warning threshold over all error pixels may leave errors far from the predicted contour under-flagged. We propose RACE-Triage, a post-hoc error triage framework that leaves the segmentation mask unchanged. A risk network is trained on out-of-fold predictions from backbone-independent inputs. The predicted contour partitions each image into a boundary band and a non-boundary region, and conformal risk control is applied separately in each region to bound the expected fraction of missed errors among cases with errors there. On ISIC 2018 dermoscopy and BUSI breast ultrasound (where patient identifiers are unavailable, so independence across images is assumed), pooled control met its overall target but missed on average 31.8% and 36.4% of non-boundary errors. Regional control reduced these fractions to 19.3% and 20.9% and raised the recall of size-filtered false-negative components from 0.722 to 0.818 and from 0.611 to 0.763. The mean warned area grew by 1.6 and 4.9 percentage points, and its 95th percentile reached 23.5% and 38.5%. The effect held across three seeds and a second backbone, and area-matched heuristics did not reproduce it. On the external PH$^2$ set, frozen thresholds exceeded both targets, whereas recalibration with 100 local images brought the mean over repeated splits below them. Regional calibration improves non-boundary error coverage at a measured increase in warned area.

---


### 73. [NotaryMark: Multi-Bit Watermarking for Black-Box DatasetUsage Auditing in Text-to-Image Diffusion Models](https://arxiv.org/abs/2611.08985)

**<font color=#1a73e8>作者：</font>** Xinyi Yu, Linkang Du, Zhou Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As generative artificial intelligence (AI) models increasingly require data, more publicly available yet licensed data is being harvested and used without authorization. Although several previous studies have proposed watermarking methods for dataset copyright auditing, their applicability to the text-to-image (T2I) setting remains notably limited. The core drawback is that watermarks embedded by existing techniques are often treated as noise and are gradually filtered out and attenuated during the latent noising-denoising process of diffusion model training. We propose NotaryMark, to our knowledge the first multi-bit watermarking method specifically designed for black-box auditing of T2I training dataset use. The core idea of NotaryMark is to align the watermark with the latent denoising of diffusion models, thereby overcoming the signal decay that plagues existing multi-bit methods during sampling. We evaluate NotaryMark across three datasets and three diffusion models spanning watermark capacities from 8 to 1024 bits. With a watermark capacity below 32 bits, it achieves a high average bit accuracy of 0.85-0.90. With a watermark capacity exceeding 32 bits, it maintains bit accuracy between 0.67 and 0.80, consistently outperforming existing multi-bit watermark methods whose bit accuracy is around 0.42-0.60. Furthermore, we design a voting-based aggregation scheme to boost the bit accuracy with a modest budget of 30 queries. Building on this, we incorporate error-correcting codes to enable reliable decoding and tracing of the embedded identifier information. Robustness evaluation against fifteen evasion attacks spanning seven categories shows that NotaryMark remains robust under most evaluated settings, while stronger attacks generally suppress watermark evidence only at the cost of substantial utility degradation, demonstrating its practical reliability against malicious tampering.

---


### 74. [LEF-JEPA: Denoising-Trained Latent Energy Fields for Spatial Representation Learning](https://arxiv.org/abs/2611.08989)

**<font color=#1a73e8>作者：</font>** Zhiyuan Liu, Zhihao Xu, Sicheng Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A joint-embedding predictive architecture (JEPA) that applies prediction supervision only at masked positions struggles to clearly capture object shapes and boundaries in its latent representations. We further observe that some existing methods improve spatial structure while also retaining rich variations in texture and color. However, preserving more low-level visual information does not necessarily make representations better suited to prediction and action. This raises a key question: how can we strengthen the spatial structure in latent representations that supports prediction and action without over-encoding these details? We introduce LEF-JEPA, which learns spatial structure through target-guided latent recovery and transfers this supervision to the visual encoder through a relative-energy constraint; the energy module is used only during pretraining and adds no inference overhead. To reduce the cost of energy optimization during pretraining, we further construct a conditional Ising Hamiltonian that allows low-energy-state search to be performed by specialized Ising solvers. On physical hardware, we validate the feasibility of achieving lower forward latency with fewer local updates. Under a unified CIFAR-10 pretraining and frozen-encoder evaluation protocol, both realizations outperform V-JEPA2.1 in image classification, foreground segmentation, and visual planning.

---


### 75. [Action-Centered Causal Bandits for Budget-Constrained Promotion Targeting](https://arxiv.org/abs/2611.08990)

**<font color=#1a73e8>作者：</font>** Yifan Lin, Kaixu Yang, Di Mo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Web platforms select among costly interventions for each user to maximize incremental outcomes under a global budget. We formulate this problem as a budget-constrained contextual bandit with heterogeneous treatment effects. Although an action-independent outcome baseline cancels from treatment comparisons, modeling a nonlinear baseline can increase statistical complexity.
We propose DR-CATE-CBwK, an action-centered causal bandit that directly learns treatment contrasts. Its online update remains valid under baseline-model misspecification without inverse-propensity weighting. It combines an offline doubly robust learner to warm-start treatment-effect estimates, an online action-centered estimator for sequential contrast learning, and a primal-dual controller with an affordable-action rule to enforce the effective-cost budget pathwise.
For linear conditional average treatment effects (CATEs) in a stationary i.i.d. setting, we prove a high-probability (\widetilde{O}(Kd\sqrt{T})) regret bound, where K is the number of priced actions, d the context dimension, and T the horizon. We benchmark against the fluid linear program (LP) under the coverage-guaranteed action rule. We further show that the action-centered estimating moment remains unbiased under any predictable baseline estimate, whereas a specified separate-arm reward regression can exhibit asymptotic contrast bias under action-dependent logging and shared-baseline misspecification.
On a semi-synthetic job-marketplace benchmark with real logged features and simulated outcomes, our practical Thompson-restricted variant achieves the lowest regret among evaluated budget-feasible methods in the operating regime. It reduces regret by approximately 20% versus the strongest reward-based baseline, outperforming raw-reward contextual bandits, BwK baselines, and a static offline policy, while never exceeding the effective-cost budget.

---


### 76. [Rethinking Optimization Methods for Hierarchical Feature Selection](https://arxiv.org/abs/2611.08991)

**<font color=#1a73e8>作者：</font>** Xinyuan Song, Zekun Cai, Liang Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rare-event forecasting often depends on interpretable conjunctions: a single keyword, location, or temporal cue may be weak, while their joint occurrence can identify a meaningful precursor. Hierarchical-Task Numerical conjunctive feature Learning (HTNL) selects Numerical Conjunctive Features (NCFs) through a structured sparsity objective. However, the resulting optimization problem is challenging, making optimization design critical to its practical performance. We give a unified diagnosis of four HTNL optimization families: original majorization-minimization (MM), variational quadratic form (VQF), alternating direction method of multipliers (ADMM), and weighted group lasso (WGL). Our analysis distinguishes three key factors that jointly determine HTNL optimization behavior. First, VQF and MM are algebraically equivalent under matched variational updates and optimize a squared-penalty formulation. Second, ADMM optimizes the unsquared objective through consensus splitting; we replace its truncated FISTA proximal solver with a scalar bisection update (ADMM-Bisect) for more accurate treatment of near-threshold blocks. Third, WGL targets the same unsquared objective, while all methods face rapidly decaying active-set admission scores. Across two synthetic datasets and 11 civil-unrest and flu-surveillance tasks, VQF achieves the highest mean AUC with the most compact non-collapsing supports. ADMM-Bisect reduces measured runtime, while calibrated WGL avoids the empty-support failures of its original scale. Synthetic results further show how proximal accuracy, pruning, and search budget affect candidate recovery, especially for longer conjunctions. Code will be made publicly available upon publication.

---


### 77. [Enforcing Symmetries on Pre-trained ML Models for Physics](https://arxiv.org/abs/2611.08992)

**<font color=#1a73e8>作者：</font>** Wenjie Zhou, Valentino F. Foit, David W. Hogg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc group averaging (or test-time augmentation) is a simple way to impose symmetry on a trained predictor without changing its architecture or retraining it. For finite and compact groups, averaging over a normalized Haar measure on the group gives the Reynolds operator: a canonical projection onto invariant or equivariant predictors with known non-increasing risk guarantees under certain assumptions. This paper provides numerical experiments on physics emulation models that demonstrate the effectiveness of the approach in this setting. We then extend this framework to non-compact group symmetries. For non-compact groups, the Haar measure cannot be normalized, so group averaging cannot be defined in the same way. We replace it with three alternatives: the Weyl unitary trick (which requires complexifying the space and extending the predictor), a data-dependent orthogonal projection (which involves a non-trivial optimization on the space of invariant or equivariant functions), and a frame averaging approach (which involves mapping each point to a set of orbit representatives). We illustrate the constructions theoretically and empirically on the unit-rescaling group and the Lorentz group. Our results show that in the non-compact case, the Weyl trick and frame averaging do not provide a consistent improvement over the baseline, except where the test data is out-of-distribution (an orders-of-magnitude improvement in this case) and, for the Weyl trick, in low-data regimes. The orthogonal projection can provide improvements in-distribution and out-of-distribution. We also observe that models trained directly on invariant features matched or beat the projection of an unconstrained one. We conclude that post-hoc symmetrization extends to non-compact groups, but it does not consistently outperform training a symmetric model.

---


### 78. [When2What: A Timing-Conditioned Framework for Long-Horizon Forecasting of Continuous Cardiovascular Waveforms](https://arxiv.org/abs/2611.08993)

**<font color=#1a73e8>作者：</font>** Chaoqi Zhang, Shujie Yan, Zhao Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon forecasting of quasi-periodic cardiovascular waveforms, such as the electrocardiogram (ECG), arterial blood pressure (ABP), and photoplethysmogram (PPG), requires predicting both when future cardiac events will occur (beat timing) and what the local structural pattern looks like around each event (beat morphology). However, standard sequence forecasters trained with pointwise mean squared error (MSE) average across uncertain future heartbeat phases, flattening sharp R peaks and pulse upstrokes into featureless baselines. Our analysis of intraoperative ECG reveals a clear temporal asymmetry: beat-time predictability from history decays within seconds due to stochastic heart-rate variability, whereas local beat morphology aligned at true beat times remains stable over several minutes. Guided by this insight, we introduce When2What, a timing-conditioned framework comprising three stages: Predict, Commit, and Generate. Given a 120-s history, When2What predicts a dense 60-s timing map, selects and sharpens discrete beat events into unit-height Gaussian impulses, and conditions a neural waveform generator on both these committed events and the observed history. Across intraoperative ECG, When2What substantially outperforms existing time-series and physiological forecasters, achieving a near-term waveform event skill of 0.644 and reproducing 95.62% of its predicted heartbeats in the generated waveform where direct long-horizon forecasters collapse into flat baselines. Furthermore, When2What transfers zero-shot to external hospital and atrial fibrillation cohorts, extends effectively to ABP and PPG pulse waveforms, and is supported by ablations and synthetic analyses that establish explicit timing conditioning as an effective paradigm for quasi-periodic long-horizon waveform forecasting.

---


### 79. [The Drawing You Watch Is the Portrait You Keep: A Replayable Machine Portrait Studio](https://arxiv.org/abs/2611.08994)

**<font color=#1a73e8>作者：</font>** Vinod Rajpurohit  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Ask an image model for your portrait and a finished picture arrives: no first line, no second thoughts, no record of how it got there, and a different picture if you ask again. I built a portrait studio that works the other way. A sitter chooses one of eight fictional artists, each written with a city, a medium and a tempo of its own, holds still for 8 to 12 seconds, and watches a drawing of themselves appear over 44 seconds. One still is sent after consent, a hosted image model returns a private study the sitter never sees, and a compiler turns that study into one drawing document. The live drawing, the saved sheet, the vector export and the film all read that document, and a replay makes no model call, so the drawing you watch is the portrait you keep. I describe the compiler in enough detail to rebuild it and say plainly what it is: an authored reconstruction at a compressed speed, not a recorded hand. On 16 generated test studies a sheet holds 8,784 to 16,378 timed contacts, about three quarters of them fixed-grid fills and nearly all shorter than one video frame, and recompiling one study gave byte-identical output four times on one machine. The paper also traces a bug that matters more than any of that. The earlier compiler estimated the paper colour tile by tile, read dark skin as paper, and in all eight hands kept less of a deep-complexioned face than a fair one (13 to 48 percent against 41 to 56). On 80 generated studies the rebuilt engine keeps the complexion difference the study already has (raw retention 89 to 120 percent), so the fairness question has moved upstream, to the study and the hosted model. The two test sitters are generated and differ in more than complexion, and no real-face or perceptual study exists yet. The studio is live at this https URL.

---


### 80. [Calibrating your confidence requires thinking of all the ways you could be wrong](https://arxiv.org/abs/2611.08997)

**<font color=#1a73e8>作者：</font>** Marco Miani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A primary limitation of modern deep learning is the miscalibration of model confidence; traditional architectures fundamentally lack a mechanism to quantify their own uncertainty. Larger models and larger datasets mitigate this issue, but they do not resolve the underlying structural deficiency. Bayesian methods offer a principled uncertainty-aware learning framework through stochastic parameters. Yet, despite the established benefits, the inherent computational overhead often compromises either scalability or quality. This trade-off currently prevents the widespread adoption of Bayesian methods.
This Thesis bridges the gap between high-quality and low-complexity by introducing a novel distribution on parameter space: a degenerate Gaussian whose covariance is a projection matrix aligned with the null space of the Fisher information matrix. We demonstrate the scalability of this Bayesian posterior through two numerically efficient algorithms: one for posterior sampling and another for the direct computation of predictive confidence. Empirically, we show State-Of-The-Art confidence calibration and out-of-distribution detection for large models.
We provide theoretical grounding for this approach. We study the degeneracies inherent in Amari's information geometry and highlight its most relevant component: the split of parameter's perturbations into two orthogonal subspaces. From this perspective, our posterior naturally emerges as the simplest choice that captures this split, assigning unitary variance to one subspace and zero variance to the other. Moreover, through the tools of differential geometry, we utilize this split to identify and rectify a critical misalignment issue of the non-linearized Laplace Approximation. Finally, with a focus on PAC-Bayes generalization bounds, we pave the way for a deeper understanding of the learning capabilities of overparametrized models.

---


### 81. [Towards Robust Reinforcement Learning Market Making: Lessons from Loss Function Experimentation](https://arxiv.org/abs/2611.09012)

**<font color=#1a73e8>作者：</font>** Siddharth Nand, Bora Guney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Market makers play a vital role in ensuring efficient trade within financial markets. Recent literature has delved into training market-making systems using reinforcement learning. This paper delves into the impact of various loss function formulations on risk management behavior within reinforcement-based market making. Through empirical evaluation, we contrast profit-maximizing strategies with risk-averse approaches, finding that penalties for inventory and cash management foster more resilient and adaptable market-making strategies. Our results underscore the significance of striking a balance between profit maximization and risk management in algorithmic trading, providing actionable insights for refining strategies in practical settings.

---


### 82. [SIMBAD: Spatio-Temporal Traffic Forecasting Robust to Aperiodicity](https://arxiv.org/abs/2611.09015)

**<font color=#1a73e8>作者：</font>** Daniel Y. Lee, Seungwon Shin, Seunghoon Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate traffic prediction is essential for urban planning but remains challenging due to the irregular patterns caused by unexpected events. While Spatio-Temporal Graph Neural Networks (STGNNs) effectively model periodic data, they often struggle with these aperiodic fluctuations. To address this, we propose SIMBAD, which improves generalization irregular patterns via two key mechanisms: 1) adaptive regulation of periodic signals to prioritize recent signals, and 2) dynamic spatial modeling that adjusts influence between connected nodes based on contextual relations. Built upon simple similarity metrics to adapt to aperiodic patterns, SIMBAD outperforms existing methods on real-world benchmark datasets, demonstrating superior performance in predicting unseen and irregular traffic events.

---


### 83. [Knowledge Distillation from Neural Networks to Differentiable Logic Networks](https://arxiv.org/abs/2611.09024)

**<font color=#1a73e8>作者：</font>** Hee Yun Suh, Niraj K. Jha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentiable logic networks (DLNs) are interpretable, edge-friendly classifiers that learn both their logic operators and their connections through gradient descent, achieving accuracy competitive with multi-layer perceptrons at orders-of-magnitude lower inference cost. Their accuracy, however, is bounded by the problems of vanishing gradients, scalability, and lack of an ecosystem, leaving a gap relative to conventional neural networks on several datasets. We introduce knowledge distillation for DLNs to narrow this gap. We distill from a trained multi-layer perceptron teacher into a DLN student, integrating the distillation objective into a two-phase training loop without altering the architecture or the inference procedure. The teacher is discarded after training. Hence, the distilled model retains the interpretability, sparsity, and inference cost of a conventionally trained DLN. We investigate this approach through four variants: a joint hyperparameter search that optimizes the distillation weight and temperature alongside the architecture, a grid search over these two hyperparameters with the architecture fixed, and two single-phase variants that employ distillation during only the neuron-function or only the connection phase. On 20 public tabular classification tasks, distillation improves balanced-class accuracy at negligible cost to gate-level operation counts and model size, though the benefit varies by dataset. Performance improvements of up to 15% are observed, in some cases surpassing the teacher itself.

---


### 84. [Function-Space Certification for Neural Operators](https://arxiv.org/abs/2611.09038)

**<font color=#1a73e8>作者：</font>** Ryan Hsiang, Robert Joseph George, Anima Anandkumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Certifying the robustness and physical consistency of scientific machine-learning models ensures that their predictions remain reliable beyond the test set. For neural operators, which learn PDE solution operators by mapping infinite-dimensional function spaces, certification means establishing rigorous, domain-wide guarantees for their output functions. However, standard neural network (NN) verification methods are fundamentally designed for vector-to-vector mappings, and they can only certify neural operators at fixed grid resolutions and provide no guarantees over the entire domain or across another resolution. We close this gap by introducing a function-space certification framework that verifies neural operators across the entire continuous domain. We formulate interval bound propagation (IBP) and CROWN in function space, propagating upper and lower bound functions through each layer using rigorous numerical integration. In addition, we extend bound propagation to higher-order derivatives to certify PDE residuals and solution error bounds. Experiments across several neural operator architectures and scientific problems, including the 572.5-million-parameter spherical Fourier neural operator for global weather forecasting, show that our method produces tight, domain-wide guarantees efficiently, providing a foundation for trustworthy operator learning.

---


### 85. [From Emergence to Reversibility: Toward Reversible Multi-Agent Systems](https://arxiv.org/abs/2611.09054)

**<font color=#1a73e8>作者：</font>** Zhengye Han, Linda Ng Boyle  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems become capable through institutional mechanisms, such as rules that route information to agents that act on it. These mechanisms are also natural places to restrict the system. Yet as agents learn, share memory, delegate, and repair failures, the collective can find other paths to the same effects: a restriction on the original mechanism still operates but no longer stops them, while routine performance and compliance checks pass. We propose \textbf{Reversible Multi-agent Systems} as a research agenda: collectives that grow while an authorized supervisor can still restrict specified effects, keep them restricted as agents adapt, and reconstitute useful cooperation under renewed authority. What is reversed is the ability to produce a specified effect; restrictions must hold even if learned knowledge persists. The goal is to preserve effective intervention, not a particular mechanism: at every step of growth, some authorized intervention must keep a specified prohibited effect rare while maintaining required service. We identify three research problems: tracking what capabilities depend on, handing off control before an old mechanism loses its effect, and separating legitimate repair from unauthorized reconstruction. We outline how to evaluate control across growth paths, back control claims with evidence, and allocate the rights to restrict and restore.

---


### 86. [OmniLatent: Unified Latent for 3D Part Modeling](https://arxiv.org/abs/2611.09055)

**<font color=#1a73e8>作者：</font>** Yunhan Yang, Yunfei Zhao, Zeqiang Lai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D part decomposition is a central capability for editable asset creation, yet existing workflows typically segment a completed mesh as a post-processing step, making the result sensitive to geometric artifacts, texture ambiguity, and limited part-level annotations. We present OmniLatent, a unified latent modeling framework for 3D part decomposition. Instead of predicting part labels in isolation, OmniLatent learns a shared latent space that jointly encodes geometry, deformation, appearance, and binary part IDs, allowing data-rich geometric and visual priors to support data-scarce part learning. Given a single input image, the base model generates geometry, deformation, texture, and surface part IDs in one pass, producing a part-aware 3D asset without a separate segmentation stage. We further tune the pretrained model for two extensions: a point-prompt adapter that maps arbitrary 3D point prompts with binary part IDs into latent tokens for full segmentation, refinement, and part subdivision, and an amodal part completion model that completes partial surface masks into a coherent full-object decomposition through dynamic per-part token allocation, cross-attention to the given geometry latent, and alternating part-local and global attention. Extensive experiments show that OmniLatent produces semantically meaningful part segmentations with precise boundaries, supports interactive part editing, and completes partial part observations while preserving global object consistency.

---


### 87. [ProtoCouncil: Multi-Encoder Anatomical Prototypes for Prostate Cancer Detection in Micro-Ultrasound](https://arxiv.org/abs/2611.09058)

**<font color=#1a73e8>作者：</font>** Mohammad Mahdi Abootorabi, Nooshin Maghsoodi, Armin Saadat 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Micro-ultrasound ($\mu$US) is a promising modality for prostate cancer (PCa) detection, but identifying suspicious tissue depends heavily on clinical experience. Models trained on sparse, noisy core-level pathology offer little insight into their decisions and can fail under domain shift. Clinical use needs a traceable decision process and a flag for uncertain predictions.
Methods: We introduce ProtoCouncil, in which three foundation encoders (MedSAM, DINOv3 and V-JEPA 2.1) learn case-based prototypes at three anatomical levels: whole gland, needle track and gland sectors. Prototypes are projected onto real training-core regions, and label-free fusion keeps every class logit as a bias plus an exact sum of prototype similarity contributions. Encoder disagreement triggers selective prediction.
Results: In five-fold patient-level cross-validation (6,588 cores, 693 patients), ProtoCouncil reaches 82.9% AUROC for clinically significant PCa (csPCa, Grade Group $\geq$3), 4.3 points above the best previously published method. In zero-shot evaluation on two external cohorts, ProtoCouncil achieves higher all-cancer and csPCa AUROC than all previous methods. Nearest same-class exemplars match test-core tumor involvement better than random same-class cases. Externally, csPCa accuracy falls from 79% when encoders agree to 27% when two oppose the fused call. Abstaining on disagreement raises balanced accuracy by 7 and 15 points, while retaining 58% and 54% of the cores.
Conclusion: ProtoCouncil grounds core-level predictions in exact similarity-based evidence from real, anatomically indexed training cases, which makes its reasoning interpretable. It achieves the highest csPCa AUROC across three cohorts and identifies unreliable predictions through encoder disagreement.

---


### 88. [WearableBridge: Task-Guided Latent Transport for Free-Living Activity Recognition](https://arxiv.org/abs/2611.09067)

**<font color=#1a73e8>作者：</font>** Jingjing Zou, Yixin Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wrist-worn accelerometers make activity monitoring feasible at scale, but incidental arm motion, device orientation, and shifting context blur the signal that separates activities. Calibration studies supply higher-quality references such as concurrent thigh recordings or supervised laboratory wrist sessions, but they are expensive, cover few participants, and are rarely available at deployment. How can limited reference data improve recognition for participants who wear only a wrist device? We propose WearableBridge, which holds the reference encoder and classifier fixed and learns a task-guided transport map, the bridge, that carries each wrist feature into the region the classifier associates with its activity. Reference features or the classifier's predictions indicate the destination, and a classification loss penalizes wrist features that land in the region of another activity. We instantiate WearableBridge with three bridges: Mapper regresses onto reference features, Distillation matches the classifier's class probabilities, and MeanFlow learns a one-step flow from wrist toward reference features. On 40 held-out free-living PAAWS participants, all three bridges improve macro-F1 in every training run, and the strongest, MeanFlow, raises mean macro-F1 from 35.1% to 56.0% with concurrent thigh references (Thigh2Wrist), and from 54.0% to 63.5% with group-matched laboratory wrist references (Lab2Freeliving). Fitted only on PAAWS, MeanFlow also raises macro-F1 on the CAPTURE-24 cohort from 42.8% to 54.7%. The gains replicate on selfBACK, hold across four reference encoders, and grow with temporal context. A study can therefore collect reference recordings for a calibration subset and improve wrist-only recognition for every other participant, training only a bridge of 0.13 to 2.44 million parameters while the reference encoder and classifier stay unchanged.

---


### 89. [UniRGBA: Unifying RGB and Alpha in Pretrained Video Diffusion Models](https://arxiv.org/abs/2611.09069)

**<font color=#1a73e8>作者：</font>** Lei Xu, Zhuo Li, Yongyi Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video diffusion models have achieved remarkable photorealistic RGB synthesis, yet generating videos with a native alpha channel remains an open challenge. Existing approaches often rely on matting-style data and non-native RGBA designs, causing them to specialize in real-object scenes and to degrade severely on visual-effect content whose semi-transparency is spatially non-local and non-elliptical. We present UniRGBA, a unified framework whose key insight is that RGBA generation does not require a dedicated alpha encoder or complex latent-space restructuring---a minimal, targeted extension of the existing RGB pathway is sufficient. UniRGBA-VAE extends a causal video VAE to 4-channel RGBA via zero-initialized channel expansion, symmetric selective layer unfreezing (5% trainable), and a six-term progressive reconstruction loss anchored by a KL reference loss that prevents latent drift, followed by a two-stage schedule that introduces a lightweight GAN objective. We then apply standard DoRA to the pretrained DiT, reusing the unified 4-channel latent without any alpha-specific architectural changes. On a visual-effect RGBA benchmark, UniRGBA substantially outperforms Wan-Alpha on RGBA reconstruction while preserving RGB fidelity. For generation, UniRGBA outperforms Wan-Alpha on RGBA text-to-video tasks and matches or surpasses the original pretrained Wan2.1 backbone on RGB-only metrics, demonstrating that native alpha support can be integrated without compromising the underlying RGB prior or the model's architectural versatility.

---


### 90. [Emo-LiveSync: Real-Time Universal Lip Synchronization with Explicit Emotion Control](https://arxiv.org/abs/2611.09074)

**<font color=#1a73e8>作者：</font>** Sangjoon Yu, Seungeun Lee, JoonHeyok Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lip synchronization, the task of generating realistic lip movements synchronized with audio signals, is fundamental to applications such as film dubbing, virtual avatars, and digital content creation. Recent GAN-based methods offer computational efficiency but often lack visual fidelity, while diffusion-based approaches achieve high-quality results at the cost of substantial computational overhead. Moreover, most existing methods are limited to photo-realistic human faces, restricting their applicability to stylized characters and non-human entities. In this paper, we propose an efficient universal lip-sync video generation framework that achieves high-quality results without compromising computational efficiency. We build on LivePortrait, a warp-based portrait animation model, and introduce a training strategy that aligns audio signals to an implicit motion space by distilling knowledge from a pre-trained video-to-motion model. This enables real-time inference while maintaining high visual fidelity, and naturally generalizes to diverse stylistic characters beyond photo-realistic humans. Furthermore, we introduce an expressive control gate that enables explicit manipulation of emotional expressions for content enrichment. Extensive experiments demonstrate that our method achieves state-of-the-art performance in both visual quality and lip-sync accuracy while ensuring real-time inference.

---


### 91. [GlobalPuzzle: Globally Informed Genetic Search for Eroded Jigsaw Puzzle Reassembly](https://arxiv.org/abs/2611.09077)

**<font color=#1a73e8>作者：</font>** Lunyan Wang, Chuanzhi Xu, Ziyuan Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Jigsaw puzzle reassembly remains a highly challenging task, particularly when piece boundaries are irregularly eroded to simulate damage to cultural artifacts. On the GAP benchmark, existing methods achieve a perfect assembly accuracy of only 0.3% on $5 \times 5$ puzzles, whereas humans can solve jigsaw puzzles with remarkably high accuracy. Humans typically approach puzzle solving by identifying potentially adjacent pieces, evaluating the current assembly, and iteratively performing complex operations such as adding pieces, replacing incorrectly placed pieces, and moving entire connected groups of pieces. However, existing methods face a fundamental limitation: approaches that leverage global visual information typically predict piece arrangements directly, making it difficult to explicitly perform such complex iterative operations, while search based methods can rearrange pieces but primarily rely on pairwise boundary compatibility, lacking global visual information to evaluate and guide the search process. To bridge this gap, we propose GlobalPuzzle, a jigsaw puzzle reassembly framework that integrates global canvas level evaluation, action guidance, and genetic search. By incorporating global visual information into the evaluation and optimization of candidate assemblies, GlobalPuzzle aims to resolve ambiguous adjacency relationships that are difficult to determine from irregularly eroded piece boundaries alone, enabling flexible, globally informed reconstruction.

---


### 92. [TUGB: A Two-stage Uncertainty-aware Generative Auto-Bidding Framework](https://arxiv.org/abs/2611.09091)

**<font color=#1a73e8>作者：</font>** Luzhan Yuan, Chao Mi, Xiahao Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative modeling, particularly Decision Transformers, shows promise in auto-bidding strategies. However, it struggles with limited exploration in static offline datasets, vulnerability to dynamic environmental shifts, and a reliance on heuristic return-to-go (RTG) specifications that may yield suboptimal performance on unseen traffic. To address these challenges, we propose the Two-stage Uncertainty-aware Generative Auto-Bidding (TUGB) framework. TUGB integrates generative sequence modeling with Reinforcement Learning (RL). It employs a two-stage pipeline where a pre-trained Generative Bidding Model is fine-tuned via an ensemble-based Uncertainty-aware Environment Model. This approach quantifies epistemic uncertainty to penalize high-risk trajectories and evolves the policy from RTG-conditioning to direct bidding optimization. Extensive experiments demonstrate that TUGB significantly outperforms SOTA baselines. Notably, full-scale deployment on JD Search Ad achieved a 2.32\% increase in cost and 3.57\% in target cost, validating its industrial efficacy, while its successful adaptation to subsequent mechanism upgrades and JD Food Delivery Ad further validates TUGB's superior generalization capability.

---


### 93. [BayesCrop: Real-Time Probabilistic Multi-Crop Video Reframing](https://arxiv.org/abs/2611.09100)

**<font color=#1a73e8>作者：</font>** Cheng-Han Lee, Rajesh Sureddi, Neil Birkbeck 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic video reframing is increasingly important for adapting landscape content to heterogeneous display formats. Existing methods typically predict a single deterministic crop, despite the subjective nature of reframing and the presence of multiple plausible regions of interest. We present \textbf{BayesCrop}, a real-time probabilistic framework for multi-crop video reframing. BayesCrop represents crop preferences using a two-component spatially isotropic Gaussian mixture over crop position and scale. Each component defines a representative reframing mode together with its local uncertainty, enabling both dual-view prediction and sampling of additional plausible crop candidates. For efficient video processing, we introduce an anchor-and-propagate strategy that performs neural prediction only on sparse anchor frames and propagates crop trajectories using motion vectors available from the compressed video bitstream. The resulting trajectories can be combined into a single output using a lightweight periodic view-switching strategy. Experiments on LIVE-YT-MC, LIVE-YT-VC++, and a multi-target long-video benchmark demonstrate competitive single-output localization, high multi-crop reference coverage, diverse yet coherent crop hypotheses, and stable perceptual quality. BayesCrop achieves real-time throughput of 112 FPS at the default operating point, while sampling from the learned distributions further improves reference coverage beyond the two representative crop means.

---


### 94. [COMBIO: Automated Discovery of a Compact Composite Biomarker from Routine Laboratory Panels](https://arxiv.org/abs/2611.09102)

**<font color=#1a73e8>作者：</font>** Tomer D. Meirman, Lior S. Rokach, Bracha Shapira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning models based on routine laboratory panels can predict outcomes but can be difficult to interpret and operationalize. We present COMBIO, an automated pipeline that distils such a model into a compact closed-form biomarker. The composite is a product of laboratory measurements raised to integer powers from minus two to two. The sign of each exponent indicates whether higher values of the corresponding measurement increase or decrease the composite. Shapley additive explanation values from the gradient-boosted reference model rank five candidate measurements and guide eligible exponent signs. An exhaustive search over small integer exponents selects the formula on an inner validation set, before evaluation on the reserved test set. We evaluated COMBIO across six tasks: three National Health and Nutrition Examination Survey outcomes, liver-disease classification in the Indian Liver Patient Dataset, and Medical Information Mart for Intensive Care IV in-hospital mortality and sepsis case-finding, with external evaluation in the eICU Collaborative Research Database for the two hospital tasks. Across the six test sets, COMBIO's area under the receiver operating characteristic curve differed by at most 0.03 from logistic regression using the five candidate laboratory measurements. The hospital mortality composite had an area under the curve of 0.698 in the external database. A version restricted to widely available measurements in the source hospital database achieved an area under the curve of 0.786 in a cohort covering 92% of admissions. The multiplicative representation provides compactness rather than additional accuracy, and local validation and recalibration are required before clinical use.

---


### 95. [PhoPunct: A Large-Scale Benchmark of Transformer Architectures for Vietnamese Punctuation Restoration](https://arxiv.org/abs/2611.09107)

**<font color=#1a73e8>作者：</font>** Khoa D. Nguyen, Thai Bao Huynh, Binh T. Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vietnamese punctuation restoration is often evaluated on relatively small benchmarks, limiting conclusions about how architectural choices scale with data volume. We present a controlled benchmark on News and Novels corpora containing 22.1 million labeled tokens (19.9M News and 2.2M Novels). We evaluate 17 architectures formed from four pretrained Transformer backbones and optional bidirectional long short-term memory (Bi-LSTM) and conditional random field (CRF) layers, together with a PhoBERT-large-Bi-LSTM-CRF model, PhoPunct. Every model is trained for eight epochs with the same learning rate and without architecture-specific tuning. Under this fixed budget, adding Bi-LSTM and CRF layers does not reliably improve macro F1: in seven of eight matched domain-backbone comparisons, a plain Transformer classifier matches or outperforms its Bi-LSTM-CRF counterpart. PhoPunct obtains the best News result (61.35), whereas XLM-R with a CRF obtains the best Novels result (50.18), exceeding PhoPunct (48.97). These results show that the value of recurrent and structured-prediction heads depends on their optimization regime and motivate explicit separation between architectural improvements and improvements due to architecture-specific tuning. Our source code is available at: this https URL

---


### 96. [Finite-sample Calibration Guarantees for Binary Segmentation](https://arxiv.org/abs/2611.09120)

**<font color=#1a73e8>作者：</font>** Bruno Viti, Martin Holler  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine learning based segmentation models are frequently miscalibrated, producing for each pixel a label prediction whose associated confidence does not accurately reflect the true underlying probability. This limitation is particularly critical in high-stakes applications such as medical image segmentation. Although several calibration methods have been proposed, only a small subset of them provides theoretical guarantees on the calibration error, i.e., they do not typically ensure that, with high probability, the model exhibits a low calibration error. In this work, we develop a post-hoc calibration method for which formal calibration guarantees can be established. To achieve this, we derive from standard concentration inequalities an improved theoretical bound that explicitly accounts for the spatial dependence inherent in binary segmentation outputs. We empirically demonstrate that the proposed calibrator satisfies the derived guarantee and outperforms existing post-hoc calibration approaches.

---


### 97. [CoMET: Tracking the Shared Pose Error of Roadside Messages for Asynchronous Vehicle-Infrastructure Cooperative 3D Detection](https://arxiv.org/abs/2611.09121)

**<font color=#1a73e8>作者：</font>** Shuwei Sun, Jian Huang, Hui Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A roadside sensor can detect vehicles hidden from the ego vehicle, but a pose error shifts every detection in the same message. We study asynchronous vehicle-infrastructure cooperative 3D detection on V2X-Seq using only information available at decision time, without ground truth, future frames, or per-pair calibration offsets at inference. Objects seen by both sensors reveal the shared translation, but even at zero added delay, 38% of validation messages have no matched pair. We propose CoMET (Common-Mode Error Tracking), which estimates this translation over time. At each message arrival, CoMET matches vehicle and roadside detections, estimates the offset from mutually nearest pairs, and updates a Kalman filter for that sender. When no pair matches, the filter carries its estimate forward. The correction applies to all roadside boxes, including those unseen by the ego vehicle. The estimator has no learned parameters; a separate frozen head ranks the merged detections. Across four delays from 0 to 400 ms on 21 validation sequences, CoMET averages 66.63 bird's-eye-view AP at IoU 0.7, compared with 63.18 for the same late fusion using uncorrected online poses and 62.96 for the best intermediate-fusion baseline. Across five detectors from three architectures, CoMET gains 2.2 to 3.5 AP points over online poses and 0.3 to 0.6 over estimating the offset from the current message alone. We find that the benchmark uses a zero offset as a placeholder in 28% of validation messages and that its offset search reaches the boundary in 45% of the rest. These offsets affect the labels for objects seen only from the roadside. Under two alternative label references, CoMET improves on uncorrected online poses in every evaluated population. Retraining intermediate fusion with CoMET poses and corrected labels improves detection on all three architectures tested, with statistically significant gains on two.

---


### 98. [Look Closer, Align Better: Explicit Visual Attributes for Robust EEG-to-Image Decoding](https://arxiv.org/abs/2611.09123)

**<font color=#1a73e8>作者：</font>** Ke Xiao, Banghua Yang, Wenbin Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> EEG-to-image retrieval commonly aligns neural responses with representations from pretrained vision encoders. However, these representations may underrepresent fine-grained visual details needed to distinguish semantically similar images. To address this limitation, we first investigate the EEG decodability and complementary predictive value of explicit visual attributes, identifying visual cues that capture EEG-relevant information beyond pretrained representations. Building on these findings, we propose AttrEcho, a framework that enriches pretrained visual representations with complementary, spatially aligned visual attributes. Specifically, Region-Aligned Visual Attribute Fusion (RAVF) integrates EEG-relevant local visual attributes with spatially corresponding pretrained features through a learnable signed residual gate. We further employ Feature Token Aggregation (FTA), which learns dimension-specific weights across regions to aggregate refined visual features for contrastive alignment with EEG representations. Experiments on THINGS-EEG demonstrate that AttrEcho achieves 94.8% Top-1 and 99.7% Top-5 accuracy in intra-subject 200-way retrieval, while maintaining 82.1% Top-1 accuracy as the gallery expands to 1,600 images with same-concept distractors. AttrEcho also achieves 25.3% Top-1 and 53.0% Top-5 accuracy in inter-subject retrieval. These results highlight the importance of EEG-relevant visual attributes and spatially aligned fusion for fine-grained EEG-to-image retrieval.

---


### 99. [TouchAnnotator: Multi-Source Tactile Supervision with Privileged-View Distillation](https://arxiv.org/abs/2611.09129)

**<font color=#1a73e8>作者：</font>** Ao Li, Zhihao Yuan, Chubin Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video captures human-object interaction at scale but rarely includes tactile labels for hidden contact and pressure. We introduce TouchAnnotator, an ego-only bimanual tactile annotator trained with multi-source tactile supervision and privileged-view distillation. A canonical hand field unifies glove pressure, geometry-derived human contact, and robot fingertip deformation from six datasets and three embodiments, while source-aware masks preserve valid targets. During training, an EMA teacher observes synchronized ego and wrist views and distills hand-local representations and tactile predictions into a student that uses only ego video and estimated pose at inference. Compact past-clip memory supplies temporal context. We evaluate on EgoTouch, zero-shot FPHA transfer, and 860 synchronized glove recordings. The model transfers to bare-hand contact and produces qualitatively coherent tactile responses across bare-hand, gloved-hand, and robot embodiments. On measured recordings, it improves temporal accuracy by 5.38 points and Volumetric IoU by 5.02 points under a shared protocol. These results show that heterogeneous human--robot supervision and privileged training views can turn egocentric video into dense tactile annotations.

---


### 100. [DINO-Nucleus: Multi-Level Self-Supervised Features for Nucleus Instance Segmentation](https://arxiv.org/abs/2611.09133)

**<font color=#1a73e8>作者：</font>** Mohammad Sarhangzadeh, Elyar Esmaeilzadeh, Doruk Oner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nucleus instance segmentation and counting are essential for quantitative microscopy, enabling reliable analysis of cell populations, tissue organization, and disease-related changes. However, accurately separating touching nuclei remains difficult, and many existing approaches rely on complex models or sensitive post-processing procedures. We present DINO-Nucleus, a parameter-efficient framework that leverages multi-level self-supervised DINOv2 representations for nucleus instance segmentation and counting. The model jointly predicts nucleus regions, pixel-wise instance flows, and explicit nucleus centers, while a consistency objective encourages the predicted flows to converge toward their corresponding centers. Multi-level transformer features provide complementary spatial and semantic information, and the pretrained backbone is adapted using lightweight LoRA modules to reduce fine-tuning cost. Experimental results show that DINO-Nucleus achieves strong segmentation and counting performance with parameter-efficient backbone adaptation. These findings demonstrate that parameter-efficient adaptation of multi-level self-supervised features can provide an effective solution for nucleus instance segmentation in microscopy images.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-222](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
