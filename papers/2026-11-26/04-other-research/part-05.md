# 📦 其他研究 | 2026年11月26日

> 本类共 **342** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-342](./part-07.md)

---

### 201. [LRQ-Cache: Compressing Feature Caches in Video Diffusion via Low-Rank Approximation and Quantization](https://arxiv.org/abs/2611.32345)

**<font color=#1a73e8>作者：</font>** Ruizhe Yao, Zhen Huang, Songpan Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion transformers (DiTs) achieve high-fidelity generation, but inference is expensive because every denoising step evaluates a large transformer over all spatiotemporal tokens of the video. Temporal caching accelerates them by reusing intermediate features across denoising steps. However, retaining dense feature tensors introduces a persistent storage cost that grows with video length, resolution, and cache coverage, reaching 109-346 GiB per video for the predictive caches we evaluate. Such states exceed the memory of a single GPU, so native caches must either be offloaded to the CPU, which slows generation, or be sharded across several GPUs, e.g., with sequence parallelism, so that the cache rather than the compute sets the number of GPUs. We instead shrink the cached state itself, exploiting its redundancy: a few channel patterns shared across tokens capture much of the energy of each cached feature. Based on this observation, we propose LRQ-Cache, a training-free method that combines low-rank approximation and quantization for feature-cache compression. LRQ-Cache represents each cached feature with a small set of factors, quantizes them before storage, and reconstructs the feature at reuse time, leaving cache mechanisms unchanged. Across three caching mechanisms on HunyuanVideo and Wan2.1, LRQ-Cache reduces the persistent state of predictive caches by 42-71x, to 2.3-4.9 GiB per video. VBench stays within 0.25 pp of the native cache for TeaCache, and the larger drops of the Wan2.1 predictive caches, up to 3.5 pp, shrink at higher ranks. As a result, predictive caches that exceed the memory of a single 80 GB H100 GPU fit on it with LRQ-Cache, making generation 2.7-5.9x faster than with CPU-offloaded native caches.

---


### 202. [CriticJEPA: World Models Are Better Critics Than Optimizers](https://arxiv.org/abs/2611.32357)

**<font color=#1a73e8>作者：</font>** Xvyuan Liu, Jianjie Fang, Honglin Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual world models enable goal-directed planning by predicting action outcomes. Gradient-based planners optimize actions to lower predicted goal cost, but continued optimization can exploit prediction errors after execution stops improving. Comparing plans requires informative relative scores; improving them also requires reliable update directions. Exact-state execution reveals that a frozen hierarchical world model ranks goal-conditioned proposals even when its rankings among outputs of prolonged gradient search are uninformative. Effective planning pairs goal-directed candidates with predictions that distinguish their outcomes. We introduce CriticJEPA, which learns goal-conditioned flow proposals from reward-free trajectories and uses frozen rollouts to select among them at every hierarchy level. Forward selection forms a complete planner; short anchored updates refine candidates before selection. Across visual navigation and manipulation, CriticJEPA increases success at a fraction of the planning compute, transferring shared settings across independently trained models, hierarchy depths, and unseen tasks while keeping every world-model weight fixed.

---


### 203. [Implementation of Machine Translation for the Uzbek Language Based on Transformer Models](https://arxiv.org/abs/2611.32359)

**<font color=#1a73e8>作者：</font>** Mukhammadjon Musaev, Mannon Ochilov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This research focuses on building a machine translation system for the Uzbek language using transformer models such as T5 and mT5. Because of the limited data and the complexity of the Uzbek language, we collect, preprocess and augment data to create a strong Uzbek-English parallel corpus of about 3 million sentence pairs. The models are fine-tuned for optimal translation performance, and we use the BLEU score to evaluate the results. This study shows that our approach significantly improves upon older methods and helps promote the Uzbek language in the digital world.

---


### 204. [Sub-Riemannian structure for Oriented Point Clouds](https://arxiv.org/abs/2611.32361)

**<font color=#1a73e8>作者：</font>** Thomas Besnier, Stefan Sommer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many frameworks dealing with 3D (oriented) point clouds define locality in the ambient Euclidean space: $k$-nearest-neighbor graphs and radius balls in $\mathbb{R}^3$ are critical to define which points are "close to one another" and should exchange information. This can unintentionally merge sampled surfaces that are close in space but geometrically distinct such as the two faces of a thin leaf. Then, features are more prone to leak across boundaries which hinder performance. To address this, we propose to define a sub-Riemannian contact metric on position-orientation space $\mathbb{M}=\mathbb{R}^3\times \mathbb{S}^2$: points are lifted to $(x,n)$ with $n$ a surface normal, and "motion" is constrained to a non-holonomic horizontal distribution in which spatial velocity must stay in the plane orthogonal to the normal which can reorient at a cost. From this, we derive an explicit score, which locally approximate the distance, to compare oriented points for downstream tasks. We report improved segmentation and correspondence accuracy near contact when using the score as a drop-in change inside PointNet++ aggregation mechanism as well as reduced leakage when using it to simulate heat diffusion on oriented points.

---


### 205. [Decision Models: An Introduction and Capability Evaluation](https://arxiv.org/abs/2611.32368)

**<font color=#1a73e8>作者：</font>** Rongtao Zhang, Mingjing Qi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Applications such as ticket routing and incident triage need decisions that software can act on. Decision models provide these outputs through explicit types for choices, binary judgments, and policy scores. We evaluate the accuracy, output validity, and request latency of eleven configurations on 1,000 English and Chinese cases across nine task suites. StartLux Instant achieves 95.3% overall accuracy, returns valid outputs on all 1,000 cases, and has a median request latency of 0.084 s. It reaches 99.4% on classification and routing and selects the correct response on all 100 tool-selection cases. The highest overall accuracy among the evaluated configurations is 97.1%. These results show how a typed decision service can support fast, programmatic decisions and why its suitability depends on task-specific errors and latency requirements.

---


### 206. [From the ELBO to Maximum Likelihood: Convergence of Variational Autoencoders for Nonlinear Mixed-Effects Modeling](https://arxiv.org/abs/2611.32372)

**<font color=#1a73e8>作者：</font>** Jan Rohleff, Johannes Schropp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonlinear mixed-effects (NLME) models are the central statistical models of pharmacometrics, where they support dose selection, individualized dosing and regulatory decisions in drug development. Statistically, NLME modeling is a marginalized likelihood problem. Variational autoencoders (VAEs) solve such problems with a neural network encoder that amortizes the approximation of the intractable posterior distribution, and allow the integration of AI components into NLME modeling. This paper provides the convergence analysis of the VAE-NLME algorithm. First, its version for the evidence lower bound (ELBO) is proven to converge almost surely to the set of stationary points of the ELBO, without assuming that the encoder is trained exactly. Second, the final VAE-NLME algorithm trains the encoder on the ELBO by gradient-based optimization and uses it as proposal for importance-weighted sufficient statistics. It converges almost surely to the set of stationary points of the marginal log-likelihood, without any assumption on the training of the encoder. Thus, it combines the fast gradient-based training of VAEs with the limit of maximum likelihood estimation.

---


### 207. [Metamorphic Testing of Learned Spatial Surrogates for Transit Accessibility](https://arxiv.org/abs/2611.32373)

**<font color=#1a73e8>作者：</font>** Till Zacher, Markus Lienkamp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transit-network design requires evaluating many candidates, but detailed accessibility calculations are too slow to repeat inside an optimization loop. We therefore train a neural surrogate to approximate them. Given a candidate bus network and fixed information about rail service and nearby opportunities, it predicts the calculated spatial change in accessibility. We compare its predictions with routing-derived targets in geographically held-out regions and test specified qualitative relations under controlled input changes. Reference calculations on constructed networks assess the applicability of relations that have a routing-level counterpart. Models with positive predictive skill can still fail basic connectivity tests. One targeted intervention substantially increases pass rates for two connectivity relations while predictive skill also improves. Average prediction error is therefore insufficient when a learned model becomes an optimization objective. Predictive agreement and controlled behavioral tests should be reported separately.

---


### 208. [Found in Translation: Five Entry Points to Translate AI Literacy Frameworks in the Design of Educational Materials](https://arxiv.org/abs/2611.32377)

**<font color=#1a73e8>作者：</font>** Luis Morales-Navarro, Karl-Emil K. Bilstrup, Mille Skovhus Lunding 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While there is a plethora of AI literacy and informatics frameworks, in practice it is difficult for designers of educational materials and educators to decide where to start and how to use these in learning activities. At the same time, recent reviews show that despite the fact that most frameworks emphasize the socio-technical nature of AI, in practice interventions tend to center on preparing learners to use AI. To address these issues, we ask: How can multiple stakeholders negotiate and translate AI literacy framework ideas into common language that can be used to design introductory learning materials for primary school children, teachers and parents? We introduce five entry points into AI literacy that were developed from a computational empowerment perspective through a participatory design process involving primary teacher educators, curricular designers, media producers, and researchers. We present three vignettes that illustrate how the entry points were generative in the design of learning activities, learning tools and media content for school and home. This paper contributes an account of the participatory development of five entry points that serve as generative and negotiable resources for designing educational materials.

---


### 209. [The Activity Geometry of Discrete Generative Sampling](https://arxiv.org/abs/2611.32380)

**<font color=#1a73e8>作者：</font>** Xinlong Guo, Jie Zhang, Lingyou Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iterative refinement is a key capability of diffusion-based generation and has motivated growing efforts to bring similar behavior to discrete diffusion and flow models. A growing line of work enables such refinement by allowing previously generated tokens to be revised during sampling, thereby shaping the coupling between successive sampling states. Despite its growing role in sampler design, this coupling freedom remains insufficiently characterized. We introduce Activity Geometry to study these finite-step couplings through expected transition cost, which we call activity. We show that activity decomposes into the minimum required by the induced marginal transport and an excess term arising from the coupling. Using this minimum as a reference, we propose Minimal-Activity Finite-Time Coupling (MAFTC) to realize prescribed marginals with minimum activity without retraining or additional model evaluations. In the continuous-time limit, the minimum activity per unit time converges to the minimum expected jump rate compatible with the prescribed path. For metric-induced Gibbs paths, we further show that the activity of the kinetic-optimal flux admits a geometric decomposition. We find that total activity alone can obscure coupling excess: a sampler may approach the minimum activity required by the prescribed marginal transport while still retaining substantial coupling excess. In language generation, as the number of model evaluations increases, refinement-based samplers accumulate additional trajectory activity with limited diversity gains, whereas MAFTC reduces trajectory activity while maintaining comparable generation quality and higher lexical diversity.

---


### 210. [Improving Character Identity Consistency in Diffusion-Based Visual Story Generation through Identity Memory and Automatic Reranking](https://arxiv.org/abs/2611.32383)

**<font color=#1a73e8>作者：</font>** Maria-Emilia Grigore, Stelian Spînu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic visual story generation using diffusion-based models has become an increasingly important research direction in generative artificial intelligence. However, maintaining character identity consistency across consecutive frames remains an open challenge, as existing models often produce significant variations in facial traits, clothing, visual style, or anatomical proportions. This paper proposes a modular pipeline to improve character identity consistency in multi-frame visual story generation using Stable Diffusion XL alongside additional conditioning and automatic selection mechanisms. The proposed system integrates LoRA fine-tuning for character personalization, ControlNet for pose-based structural control, and IP-Adapter for visual identity transfer. Furthermore, a reranking mechanism based on Best-of-K candidate selection and persistent identity memory is introduced to automatically select the most visually consistent generated images. The work also includes integrating and extending the StoryDiffusion framework into a reproducible local workflow, along with improvements for generated frame selection. Performance evaluation uses automatic metrics such as CLIP image similarity, DINO similarity, and CLIP text-image alignment. Experimental evaluation was conducted on a custom benchmark of multiple characters and visual stories organized into difficulty levels (easy, medium, and difficult). Both progressive variants of the proposed pipeline and extended versions of StoryDiffusion were evaluated, including SDXL baseline, Best-of-K, Identity Memory, and the Full Pipeline. Results show that reranking, identity memory, and visual conditioning reduce identity drift across frames and improve the overall coherence and stability of generated visual stories.

---


### 211. [Spoofing Wireless Sensing with Metasurfase-based Physical Deepfakes](https://arxiv.org/abs/2611.32386)

**<font color=#1a73e8>作者：</font>** Johannes Kortz, Vignesh Natarajkumar, Christof Paar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Wireless communication networks are expanding from mere information transfer to sensing: in the Integrated Sensing and Communication paradigm, existing infrastructure and signals are reused to capture physical information about the surroundings of devices, envisioned to inform high-stakes applications such as healthcare and autonomous vehicles. From a security perspective, wireless sensing inherently trusts physical observations of the radio environment. However, as in wireless communication, the open nature of radio propagation allows attackers to tamper with victim signals. In particular, attackers can use programmable metasurfaces to manipulate wireless channels and thereby mislead sensing systems. Yet, prior metasurface-based manipulations target only individual channel features such as variance or Doppler shifts. Thus, they require knowledge of the victim sensing system and produce implausible channels that are easy to detect.
In this work, we show that metasurfaces enable physically plausible manipulation of wireless sensing that is independent of the features used by the victim sensing system. Our attack reproduces genuine pre-recorded events at the physical layer and thereby synthesizes physical deepfakes of wireless channels. To this end, we develop an attack framework that controls the amplitude and phase of victim channels across time, frequency, and antennas. The key challenge here is to build a deep learning model of the interaction between metasurface and victim channel. We demonstrate that attackers can solve this challenge in several settings, e.g., by exploiting Wi-Fi Beamforming Feedback Information or replicating the victim environment. We validate the attack both in a controlled lab study on MIMO channels and with off-the-shelf Wi-Fi sensing. Our results fundamentally challenge the trustworthiness of wireless sensing.

---


### 212. [AgentBank: Banking on Blockchain Agentic Payments](https://arxiv.org/abs/2611.32389)

**<font color=#1a73e8>作者：</font>** Yuexin Xiang, Martin Perešíni, Yuchen Lei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly pay for data and computation through protocols such as x402 and AP2, but individually funded wallets idle and require asset transfers for every payment. We present AgentBank, a smart-contract banking layer that lets agents spend bank liabilities under owner-issued mandates and on-chain spending limits. Internal payments update account balances without transferring assets, while pooled backing funds are allocated between reserves and yield-bearing strategies. We bound losses from compromised agent keys and analyze how correlated demand affects reserve requirements. Experiments show that AgentBank reduces idle liquidity by 52-77% relative to per-agent wallets and lowers gas costs for batched internal payments. Using historical DeFi liquidity data, we evaluate how reserve policies balance treasury returns against payment availability during market stress. We further examine the risks of automated bank runs and evaluate mechanisms to mitigate them.

---


### 213. [Fractal Neural Synthesis: Constant-Storage Procedural Weight Derivation via Complex Quadratic Boundary Dynamics](https://arxiv.org/abs/2611.32393)

**<font color=#1a73e8>作者：</font>** Volkan Dagli, Zerrin Dagli, Daghan Dagli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional neural networks store synaptic parameters as explicit tensors whose persistent Flash footprint scales linearly (O(W)) with parameter count, constraining resource-limited edge microcontrollers. We formulate and systematically evaluate Fractal Neural Synthesis (FNS), a procedural weight derivation architecture that replaces hidden-layer matrices with a constant 24-byte coordinate seed Theta = (c_x, c_y, ell) in F_64^3 anchored near the complex quadratic bifurcation boundary dM of f_c(z) = z^2 + c. We introduce a large-bailout (R = 256) smooth escape kernel, four zero-overhead geometric sampling apertures--Cartesian Grid, coprime 3x3 Rule-of-Thirds (Z/9Z), phi-Vogel spiral, and multi-scale Harmonic Tripod--and prove conditional Kolmogorov (K_Kolm <= 192 + c_0 bits) and Shannon entropy bounds. Across magnifications zeta in [10^0, 10^8], C^1 Fourier and lattice-noise bases collapse to post-standardization rank ~2.25 and SHA-256 PRNG exhibits avalanche discontinuity (rho ~ 0.019, 50.6% micro-step retention), whereas dM uniquely sustains both rank (~10.0) and local continuity (rho in [0.81, 0.97], 89.2% retention). Under leak-free 10-fold CV across four zero-scaler-byte non-linear benchmarks, FNS with an INT8 readout surpasses 0-hidden Linear-INT8 by +3.6 to +10.8 pp while delivering 10.7x-129x total Flash reduction (725x-2,773x hidden reduction) relative to converged Float32 MLPs (90.30% Ionosphere in 285 B; 97.22% Optical Digits in 2,598 B; 97.90% PenDigits in 2,598 B; 87.00% Satimage in 1,570 B).

---


### 214. [Adaptive and Detection-Aware Super-Resolution for Small Object Detection](https://arxiv.org/abs/2611.32394)

**<font color=#1a73e8>作者：</font>** Cezica-Elena Luncanu, Stelian Spînu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image super-resolution aims to reconstruct a high-resolution image from a low-resolution input and is relevant for surveillance, satellite imagery, medical imaging, and object detection. This paper investigates SRCNN-based single-image super-resolution for a scale factor of x4, starting from a classical baseline and progressively introducing residual learning, Charbonnier loss, and adaptive loss functions. The proposed approach includes a three-region adaptive loss, where image areas are divided into smooth, texture, and edge regions using gradient information. The models are evaluated using PSNR, SSIM, LPIPS, and EdgeMAE in order to measure both reconstruction quality and structural detail preservation. In addition to reconstruction evaluation, the paper analyzes the impact of super-resolution on object detection. A YOLOv8 detector is applied to images processed through bicubic interpolation and SRCNN-based variants, using images from the COCO validation dataset. The results show that improved reconstruction quality does not always lead to better detection performance. However, for small objects, a detection-aware variant combined with residual scaling improves the F1 score compared to the bicubic baseline. These results highlight the importance of task-aware evaluation when super-resolution is used in computer vision pipelines.

---


### 215. [PRC4D: Physical Relation-Constrained Persistent 4D Reconstruction](https://arxiv.org/abs/2611.32396)

**<font color=#1a73e8>作者：</font>** Junho Kim, Hyunyoung Choi, Jiseok Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A faithful 4D reconstruction should capture both the shape and motion of objects, even when they disappear from view. Existing methods preserve previously observed geometry and extend motion through occlusion using local spatial and motion associations. However, treating short-term contact or shared motion as sufficient evidence of persistent rigidity can introduce incorrect motion constraints and distort overall reconstruction. To address this limitation, we present PRC4D, a physical relation-constrained framework that identifies reliable rigid relations and uses them to maintain spatial consistency through occlusion. PRC4D combines 3D contact and relative motion consistency with sequence-level verification to distinguish persistent couplings from transient interactions. The resulting graph guides observed-pose refinement and motion propagation from visible to occluded components without altering reconstructed geometry. Experiments on diverse real-world multi-object sequences and controlled occlusion simulations demonstrate improved reconstruction accuracy, reduced relative pose errors, and more consistent object configurations under changing visibility.

---


### 216. [Not All Pairs Align: Caption-Guided Audio-Visual Contrastive Learning](https://arxiv.org/abs/2611.32399)

**<font color=#1a73e8>作者：</font>** Omar Emara, Nan Lu, Dima Damen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the problem of learning audio-visual representations from co-occurring modalities. Multimodal contrastive learning typically assumes that paired observations provide shared views of the same underlying information. While this may be true for datasets collected in constrained environments, it does not always hold. For instance, co-occurring audio and visual signals can differ substantially in their content due to off-screen sounds. Nevertheless, standard contrastive objectives treat all paired samples as equally aligned. In this work, we propose Caption Guided Alignment Aware Loss (CGAAL), a model-agnostic objective that leverages modality-specific captions to estimate semantic agreement between audio and video. CGAAL uses these agreement scores to weight the contribution of each positive pair. A warm-up period and gradual thresholding strategy progressively introduce this alignment-aware training signal. We demonstrate the generality of CGAAL by applying it to three contrastive baselines, consistently improving their performance on audio-visual retrieval.

---


### 217. [Optimal Transport Meets t-SNE: Integrated Visualization without Batch Effects in OT-tSNE](https://arxiv.org/abs/2611.32402)

**<font color=#1a73e8>作者：</font>** Azhar Akhmetova, Edward Eichhorn, Boris Landa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual exploration is an integral step in understanding the structure of datasets. However, systematic variation between datasets collected under different conditions, known as batch effects, can obscure shared structure and complicate their joint visualization. Existing methods often rely on cross-batch nearest-neighbor relations to integrate the batches. Yet, these local correspondences can be unreliable for challenging cross-batch geometries. We propose optimal-transport t-SNE (OT-tSNE), which replaces nearest-neighbor-based matching with globally coupled affinities derived from entropic optimal transport. Controlled synthetic experiments demonstrated that nearest-neighbor-based methods can deteriorate, while optimal-transport affinities and OT-tSNE embeddings remain robust. Across seven real single-cell datasets, we benchmarked OT-tSNE against a broad range of integration and visualization methods and found that it achieves a Pareto-efficient trade-off between batch mixing and biological conservation, and integrates batches particularly well.

---


### 218. [A Framework for Graph Node Symmetric Quantification under Dataset Shift](https://arxiv.org/abs/2611.32403)

**<font color=#1a73e8>作者：</font>** Alessio Micheli, Alejandro Moreo, Marco Podda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph node quantification is the supervised learning task of estimating the prevalence of different classes within an arbitrary sample of unlabelled nodes from a graph, subject to some form of dataset shift. Existing approaches to graph node quantification typically follow the standard aggregative paradigm, i.e., they use labelled nodes from the graph to train an intermediate node classifier, and obtain an estimated class distribution for the sample by aggregating the classifier's predictions for the individual nodes and then correcting the result via some adjustment strategy that accounts for dataset shift. In this work we propose a framework for graph node quantification that does away with both node-level supervision, since its training phase only requires node samples labelled by their class distribution, and node-level predictions, since it estimates class prevalence values directly, without the need of any intermediate node classifier. The framework thus allows symmetric quantification, since (unlike in standard ``asymmetric'' quantification methods) the labelled items used for training and the unlabelled items on which predictions must be issued are of the same type (i.e., node samples). This framework (that we dub GSQ, for Graph Node Symmetric Quantification) allows building pipelines consisting of a node encoder, an embedding pooler, a prevalence predictor, and an optional post-hoc scaling step. These components can be instantiated by choosing from different trainable and reservoir-based encoders, different pooling operators, and different prediction objectives. We evaluate the GSQ framework on binary and multi-class datasets with different levels of homophily, under prior probability shift and under structural covariate shift.

---


### 219. [BEACON: Learning Observation-Conditioned Starting Points for Guided Conditional Flow Matching in Microscopy](https://arxiv.org/abs/2611.32406)

**<font color=#1a73e8>作者：</font>** Anirban Ray, Florian Jug  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fluorescence microscopy drives much of modern life science, but accessible imaging setups often yield images degraded by out-of-focus light, limited resolution, and strong signal-dependent noise. Computational restoration can recover high-quality images from such data, enabling cheaper and faster imaging at lower light dose, provided biologically meaningful structures are preserved. Guided conditional flow matching has recently shown strong results for microscopy dehazing and computational super-resolution by learning distributions of plausible restorations. However, it pairs each clean target with an independent standard Gaussian sample, so the starting point of every training path does not leverage the degraded observation. This arbitrary noise--target coupling can produce conflicting velocity targets and makes the conditional velocity field harder to learn. We present BEACON, a $BE$st-of-$K$ $A$daptive learned coupling for guided $CON$ditional flow matching, which learns an observation-conditioned base distribution. During training, a lightweight conditional noise model proposes $K$ starting points for each degraded input, and the candidate with the lowest flow-matching loss supervises both networks, while a KL term keeps the proposal close to the Gaussian prior. At inference, a single draw from the learned proposal is transported along the velocity field, requiring neither candidate selection nor the target. We evaluate BEACON on ten datasets spanning microscopy dehazing and computational super-resolution against 13 baseline families. BEACON achieves the best median perception--distortion rank for every pairing of a fidelity metric (PSNR, MicroMS-SSIM) with a perceptual metric (LPIPS, FID). Code and pretrained models will be released under a permissive license.

---


### 220. [TESS: Query-Guided Temporal Event-Structured Frame Selection for Long-Video Understanding](https://arxiv.org/abs/2611.32410)

**<font color=#1a73e8>作者：</font>** Qi Lu, Shiyan Tong, Shujie Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal localization in long videos is challenging because brief, question-relevant events are dispersed among extensive redundant content. Limited visual budgets increase the risk of omitting these events or their temporal context, undermining reliable reasoning. Existing frame selection methods emphasize semantic relevance or temporal coverage, often overlooking the complementary evidence needed to locate related events and establish their temporal relationships. To address this limitation, we propose TESS, a training-free framework for query-guided temporal event-structured frame selection. TESS selects frames that jointly show the reference event and the event asked about, in the required temporal order. Leveraging frozen vision-language representations, TESS integrates soft temporal gating, role-aware budget allocation, and within-role redundancy suppression to preserve complementary event evidence. Extensive experiments across four long-video understanding benchmarks and three multimodal backbones demonstrate that TESS consistently outperforms the strongest compared baseline by 4.0-5.5 percentage points under a fixed frame budget. Further analyses reveal greater improvements on longer videos and robust performance under tighter visual budgets, while independent evidence annotations confirm enhanced event and temporal-relation coverage. These findings establish explicit temporal evidence organization as an effective training-free strategy for preserving event relationships and supporting efficient temporal reasoning over long videos. Our code is available at this https URL.

---


### 221. [One Subspace Is Not Enough: LocalSubspaceAD for Training-Free Few-Shot Anomaly Detection](https://arxiv.org/abs/2611.32424)

**<font color=#1a73e8>作者：</font>** Daniel Pröll, Sebastian Hegenbart  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Defect-free industrial samples can vary considerably in appearance, texture, and geometry. In few-shot anomaly detection, this variability has to be modeled from only a handful of images. SubspaceAD showed that a single principal subspace of foundation-model patch features is a strong training-free model of nominal appearance. However, a single subspace has to cover all of the nominal data's variability, so a deviation that is anomalous for one semantic region can be within the nominal variability of another. We propose LocalSubspaceAD, which extends SubspaceAD from a single subspace to a mixture of subspaces, assigning each group of patches with similar features its own subspace. The set of patch-features is partitioned using k-means, one subspace is fit per cluster, and each patch is scored by the minimum of re-projection residuals over all subspaces. The proposed method requires no training and no EM refinement. On MVTec AD, VisA and Real-IAD with 1, 2 and 4 shots, it improves over a single subspace (SubspaceAD) on both evaluated backbones: by 1.2 to 1.8 points image AUROC on DINOv2, and by 1.4 to 4.4 points in image AUROC, pixel AUPR and AUPRO on DINOv3. The gains are most pronounced on objects with heterogeneous nominal appearance, such as multi-instance categories and PCBs. Ablations show that the gains stem from a finer-grained model of variability through locally oriented subspaces, rather than from the subspace offsets (cluster means). We further show that the gains do not stem from added capacity alone: the local subspaces appear to capture the structure of coherent clusters in feature space, and the model does not merely act as a compressed memory bank.

---


### 222. [NRG-Twins: Pixel-Level Ground Truth for Rigidity Violations in Generated Videos](https://arxiv.org/abs/2611.32431)

**<font color=#1a73e8>作者：</font>** Chenrui Fan, Qiyang Hu, Luca Scharr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generators now produce realistic clips of scenes and objects, which makes generated video an attractive source of 3D content. Yet generated video is not 3D consistent: static content slowly deforms or slides, 3D reconstruction degrades, and the errors are too subtle to label by hand. To make generators 3D consistent, or to build rewards and guidance that push them there, we need data that say where and by how much a generated video breaks rigidity, and these data must come from generated video itself. We obtain per-pixel ground-truth labels from real-generated twins: a real clip paired with its re-creation by a keyframe-conditioned video generator. After inserting real keyframes so that the twin camera roughly follows the real one, we measure per pixel, in degrees, how far the twin departs from a rigid scene seen along its own camera path. We release Non-Rigidly Generated Twins (NRG-Twins), 871 twins, the code that builds them for new generators, and a benchmark with an official test split. A detector trained on these data, the Non-Rigidly Generated Pixel Detector (NRG-PD), predicts the per-pixel angle from RGB alone. It separates inconsistent from consistent pixels with AUROC 0.85, against 0.40-0.74 for seven existing consistency and motion-segmentation methods, and its predictions improve 3DGS of video that contains generated content.

---


### 223. [Video Models are Excellent Motion Models](https://arxiv.org/abs/2611.32432)

**<font color=#1a73e8>作者：</font>** Kian Izadpanah, Ali Mahdavi Amiri, Daniel Cohen-Or 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video foundation models have emerged as powerful generators of dynamic visual content, exhibiting remarkable capabilities in synthesizing complex actions and interactions. We argue that these models have also become excellent motion generators, with motion priors that are richer and more general than those learned by dedicated motion models. Their advantage extends beyond visual realism and is manifested in two important aspects: motion naturalness, including coherent body coordination, physical plausibility, and realistic interactions with objects and the environment; and motion scope, encompassing a much broader range of activities and semantic coherence, particularly uncommon, complex, and compound actions. To investigate this position, we introduce a common evaluation framework that compares video and dedicated motion models through three complementary settings: text-only motion generation, reconstruction of video-generated motion from sparse keyframes, and video-based enrichment of motion-model outputs. By converting all outputs into a shared 3D skeletal representation, we evaluate motion naturalness, semantic alignment, action coverage, physical motion characteristics, and fidelity to motion constraints. Our results suggest that video foundation models can generate more natural and semantically meaningful movements, particularly for complex and compound actions. Moreover, we investigate motion-conditioned generation through loose skeletal control, finding that dedicated motion models do not consistently improve video-generated motion, while video models can enrich skeletal animations using sparse motion guidance. Our findings suggest a shift in the role of specialized motion models, from generating complete animations to guiding and controlling the richer motion capabilities already embedded in video foundation models.

---


### 224. [See the Answer, Learn to Embed: Learning Universal Multimodal Embeddings from Hindsight](https://arxiv.org/abs/2611.32439)

**<font color=#1a73e8>作者：</font>** Yoonki Cho, Youngju Na, Taegeun Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Universal Multimodal Embedding (UME) models map heterogeneous multimodal inputs into a shared embedding space, where pairwise similarity supports diverse downstream tasks. Recent reasoning-driven UME approaches use intermediate reasoning to generate additional context for embedding, but often incur extra computation at inference. In this paper, we explore the matched candidate (i.e., the paired target) as an alternative source of context, asking whether a model can "see the answer" during training and "learn to embed" without it at inference. However, direct conditioning on this privileged context can introduce candidate-specific information unavailable from the query alone or cause the candidate-conditioned query representation to collapse toward the candidate embedding. To address this, we introduce Hindsight-Enhanced Multimodal Embeddings (HEME), which learns query-grounded hindsight representations from such candidate context. HEME first trains a hindsight teacher with a hindsight attention mask, mismatched-candidate conditioning, and query-token alignment to limit excessive reliance on the candidate. It then freezes the teacher and distills its hindsight representation and similarity distribution into a standalone student embedder. At inference, the student independently encodes queries and candidates without candidate conditioning or the hindsight teacher. Experiments on MMEB-V2 and the agent and text tasks of MMEB-V3 demonstrate the effectiveness of HEME and show that it enables more efficient inference than explicit reasoning-driven methods.

---


### 225. [PVWander: 3D Memory-guided Panoramic Video Wandering with Path-Facing Canonicalization](https://arxiv.org/abs/2611.32443)

**<font color=#1a73e8>作者：</font>** Chuanxin Song, Xiaodong Wang, Shijie Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon panoramic video wandering aims to continuously synthesize scene-consistent $360^\circ$ observations along user-specified camera trajectories from an initial equirectangular projection (ERP) panorama. Existing panoramic video models have achieved promising results in camera-controlled generation, while recent 3D-guided approaches further provide geometric guidance for improving scene consistency. However, stable long-horizon wandering remains challenging due to diverse motion--orientation relationships and imperfect memory guidance induced by accumulated generation artifacts and depth inaccuracies. To address these challenges, we propose \textbf{PVWander}, a 3D-memory-guided framework that accumulates generated observations into an online point-cloud memory and reprojects it to guide subsequent generation, with two complementary designs: \textit{Path-Facing canonicalization} for motion--orientation alignment and \textit{Timestep-aware gating modulation} for adaptive memory guidance. \textit{Path-Facing canonicalization} exploits the horizontal cyclic symmetry of ERP panoramas to uniformly align each clip's ERP orientation with its principal translation direction, yielding more consistent, forward-like relative motions while preserving the prescribed camera path. \textit{Timestep-aware gating modulation} exploits the coarse-to-fine nature of diffusion denoising to adaptively regulate reprojected memory guidance through timestep-dependent channel-wise gates, preserving its structural benefits while mitigating visual artifacts from imperfect projections. Extensive experiments demonstrate that PVWander achieves improved long-horizon generation quality, while ablations validate the effectiveness of both designs.

---


### 226. [ObsBridge: Observation-Grounded Conditioning for Ego Trajectory Prediction](https://arxiv.org/abs/2611.32447)

**<font color=#1a73e8>作者：</font>** Zhenhao Wang, Shaofeng Liang, Jiemin Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian forecasting from ego-view observations is challenging because occlusion, limited visibility, and tracking errors corrupt observed motion histories. Such errors are particularly consequential for autonomous robot navigation. Existing paradigms typically either impute noisy history positions before forecasting or jointly train an auxiliary history reconstruction branch. However, predictors trained on clean histories may be sensitive to residual errors in recovered histories at deployment. Meanwhile, auxiliary reconstruction still computes inter-agent interactions over raw, corrupted coordinates. We investigate conditioning future prediction on both recovered historical states and raw observation evidence, with progressive training to accommodate imperfect recovery. Building on this insight, we propose ObsBridge, a flow-based trajectory forecasting framework with observation-grounded historical bridging. Specifically, ObsBridge first employs a frozen estimator to recover historical motion from agent-relative and ego-relative positions, image-plane locations, and visibility states. During training, we introduce an agent-wise curriculum that gradually replaces clean teacher histories with complete estimated histories before context encoding. This progressively exposes the predictor to estimated histories during training. Furthermore, we design a residual geometry adapter to fuse the encoded motion with original observation evidence. We aggregate the resulting representations through social attention to condition the flow-based trajectory generator. Extensive experiments across multiple benchmarks demonstrate that ObsBridge outperforms state-of-the-art methods. On EgoTraj-TBD, it reduces minADE@20 by 6.5\% and minFDE@20 by 8.7\%. The code will be provided at this https URL.

---


### 227. [Which Parameters to Update? An Instance-Specific Adaptation Framework for Real-World Pansharpening](https://arxiv.org/abs/2611.32450)

**<font color=#1a73e8>作者：</font>** Jin-Liang Xiao, Liang-Jian Deng, Yu-Xuan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pansharpening aims to fuse a single observed image pair, comprising a low-resolution multispectral (LRMS) image and a panchromatic (PAN) image, to obtain a high-resolution multispectral (HRMS) image. Recently, deep learning-based methods have achieved significant performance due to their strong capability of extracting nonlinear features. However, distribution shifts between training data and test images can degrade the performance of pretrained pansharpening networks, limiting their generalization in real-world scenarios. In this work, we propose an instance-specific test-time adaptation framework that uses the observed PAN-LRMS pair to select and update only a subset of the pretrained network's parameters. Specifically, the framework uses cross-scoring to identify parameter groups whose updates improve reconstruction across image patches. It then updates the selected groups by minimizing a loss that combines a spectral consistency term with a newly designed spatial consistency term. Experiments show that the adapted networks perform better than their pretrained counterparts and outperform representative state-of-the-art pansharpening methods on GaoFen-2, QuickBird, and WorldView series datasets.

---


### 228. [TDD: Target-Discrepancy Distillation for Underwater Image Enhancement](https://arxiv.org/abs/2611.32467)

**<font color=#1a73e8>作者：</font>** Zefan Feng, Zhaocheng Yu, Laibin Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater degradation changes image appearance and can compromise the semantic cues used to guide enhancement. Identifying scene content alone does not explicitly specify the appearance to recover or the input-dependent changes associated with that target. We propose target-discrepancy knowledge distillation (TDD) for underwater image enhancement, which organizes guidance around these two aspects of the same restoration problem. For each degraded-reference training pair, reference features from an underwater vision-language teacher provide target-appearance supervision, while paired feature residuals describe the observation's discrepancy relative to the same target. Both representations are jointly distilled into a lightweight guidance network that predicts them from the degraded image alone; neither the teacher nor reference images are required at inference. To align their use with their supervisory roles, we introduce progressive knowledge fusion within a multi-scale enhancement network. The estimated discrepancy first conditions spatial feature updates, after which target-appearance guidance refines the updated features and channel interactions consolidate their responses. This correction-before-refinement design lets target-guided refinement build on discrepancy-conditioned features. Experiments on six underwater benchmarks demonstrate competitive performance across full-reference and no-reference metrics. Ablations and feature visualizations analyze the contributions of the knowledge source, joint distillation, and progressive fusion.

---


### 229. [BCP: A Lightweight Boundary-Controlled Framework for Online Sign Language Recognition and Translation](https://arxiv.org/abs/2611.32471)

**<font color=#1a73e8>作者：</font>** Xiao Ma, Lin Li, Shiqing Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online sign language recognition (SLR) and translation (SLT) incrementally produce gloss sequences or natural language text from sign video as it arrives, a capability essential for real-time communication and live captioning. However, powerful pretrained offline models cannot be directly deployed in this setting, while existing online methods typically retrain the entire model on simulated streaming prefixes constructed from offline videos, incurring high costs. To address this challenge, we propose Boundary-Controlled Prefix Commit (BCP), a unified lightweight framework that converts pretrained offline methods into online counterparts for sign-to-gloss (S2G), sign-to-text (S2T), and sign-to-gloss-to-text (S2G2T). Specifically, BCP freezes the pretrained model and introduces a lightweight boundary adapter that decides when to commit, supervised by Connectionist Temporal Classification (CTC) alignments from a pretrained SLR model, without any human annotation. At inference, a Boundary-Controlled Wait-K Output Policy then decides what to commit via prefix voting, yielding adaptive burst commits while preserving the output progress of the base Wait-K schedule. Experiments on PHOENIX-2014T and CSL-Daily across four offline methods show that BCP, with less than 0.1% additional trainable parameters per offline method, achieves a strong quality-latency trade-off on S2T and remains competitive on S2G and S2G2T.

---


### 230. [OmniPersist: Persistent Dynamic World Modeling via Coupled Panoramic Evolution](https://arxiv.org/abs/2611.32473)

**<font color=#1a73e8>作者：</font>** Zhilu Zhang, Xiaoyu Liu, Wenxi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-conditioned world models play a vital role in robotics and autonomous driving, yet existing video diffusion models struggle to maintain dynamic object persistence. When the camera turns away and returns, out-of-view moving entities fail to evolve plausibly in latent space, often mutating or vanishing entirely due to bounded perspective views. To resolve this issue, we propose OmniPersist, a unified framework that couples perspective video generation with panoramic evolution within a single-stage diffusion model, without relying on auxiliary models or initial panoramic inputs. To maintain efficiency, we model the panoramic stream at a lower frame rate, bridging both views across space and time via Geometric Anchoring (GeoAnch) for spatial correspondence and Temporal Compensation (TemComp) for temporal aggregation. OmniPersist is agnostic to camera-control architectures, supporting both latent-level and attention-level conditioning. Extensive experiments on a newly constructed dynamic benchmark across image-to-video and video continuation tasks demonstrate consistent gains in visual quality, camera controllability, revisit consistency, and dynamic persistence.

---


### 231. [Progressive Reliable Supervision for Black-Box Universal Domain Adaptation](https://arxiv.org/abs/2611.32474)

**<font color=#1a73e8>作者：</font>** Jing Li, Zhe Zhang, Huateng Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Black-Box Universal Domain Adaptation (B$^2$-UniDA) aims to adapt a target model to an unlabeled target domain under arbitrary label-space relationships, while neither source data nor source-model parameters are accessible during adaptation. Under such restrictive information access, reliable target supervision is unavailable, while predictions from the black-box source model can be unreliable due to source bias and domain shifts. To address this challenge, we propose Progressive Reliable Supervision (PReS), which progressively establishes and refines reliable target supervision by coordinating complementary knowledge from the black-box source model, foundation models, and the evolving target model. PReS first identifies reliable known samples by exploiting semantic consistency under diffusion-based perturbations and cross-model consensus between the black-box source model and CLIP. It then estimates the sample-wise reliability of the two predictors and adaptively integrates their complementary predictions to construct reliable pseudo labels. The resulting supervision is exploited asymmetrically to encourage confident and discriminative predictions for reliable known samples while maintaining uncertain yet locally consistent predictions for potential unknown samples. As adaptation proceeds, the emerging target-domain knowledge is further leveraged to refine both the pseudo labels and the known/unknown sample partition, forming a closed-loop process in which supervision construction and target adaptation mutually reinforce each other. Extensive experiments on multiple benchmark datasets under diverse label-space relationships demonstrate that PReS achieves state-of-the-art or highly competitive performance under the restrictive B$^2$-UniDA setting.

---


### 232. [A Star is Reborn: The PHP Interpreter Rewritten in Safe Rust](https://arxiv.org/abs/2611.32477)

**<font color=#1a73e8>作者：</font>** Tianyu Li, Bo Wang, Prateek Saxena 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> PHP powers most of the web, yet its C interpreter has had many memory-safety vulnerabilities. Reimplementing the interpreter in safe Rust offers a promising way to eliminate these vulnerabilities. However, eliminating native memory violations alone does not necessarily prevent unintended accesses to the logical memory of the translated program.
To prevent such failures, we introduce logical memory safety, which confines the program operations to their permitted memory. In this paper, we formalize this property for PHP through an abstract PHP machine model that captures how the PHP interpreter manages program values while abstracting away functionality details. Guided by this model, we reimplement the PHP 5.0.0 engine in safe Rust, and formally prove that, for a core fragment of PHP, our Rust translation refines the abstract PHP machine, thereby establishing logical memory safety for this fragment.
Our translation safely handles all 173 memory vulnerabilities we collected that affect PHP 5.0.0 prior to the rewrite. The Rust version matches the C implementation on all functionality tests, and produces identical outputs for the real-world PHP applications we evaluate. To our knowledge, this is the first principled safe Rust port of a core fragment of the PHP interpreter that combines formal guarantees of logical memory safety with functional compatibility. The improved security comes at a modest average runtime overhead of only 15% compared to C.

---


### 233. [COHERE4D: Training-Free Dense Surface Alignment for Coherent Metric 4D Human-Scene Reconstruction](https://arxiv.org/abs/2611.32482)

**<font color=#1a73e8>作者：</font>** Zhumei Wang, Shaofei Wang, Xiang An 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human and scene foundation models offer complementary strengths for monocular 4D reconstruction: human models recover metric-scale body meshes but lack scene grounding, whereas scene models estimate globally consistent 3D geometry and camera motion without reliable metric scale. Crucially, both models reconstruct the same foreground human surface. Yet existing methods do not directly exploit this shared surface: lacking reliable foreground human geometry in scene reconstructions, earlier approaches either resort to sparse contact constraints or learn data-driven alignment modules that generalize poorly to out-of-distribution scenes. We present COHERE4D, a training-free framework that directly registers the human surfaces predicted by independently pretrained human and scene foundation models to reconstruct a coherent, metric 4D world. COHERE4D establishes dense, pixel-aligned 3D correspondences over the visible human surface and employs RANSAC with cross-frame consensus to suppress outliers from occlusion, background contamination, and depth noise. This formulation solves for two complementary geometric quantities: a sequence-level shared scale that calibrates scene geometry and camera motion to metric human size, and per-frame human translations that align camera-space human meshes with the scaled scene geometry to enforce spatial and temporal consistency. Across diverse backbones and benchmarks, COHERE4D substantially outperforms prior methods in human--scene alignment, metric scene and camera pose reconstruction, and global human motion estimation, adding only 4,ms/frame, enabling overall inference at up to 14 FPS.

---


### 234. [When Knowledge-Tracing Rankings Depend on Available History: A Source-Correction and Matched-Information Audit on ASSISTments 2009 and 2015](https://arxiv.org/abs/2611.32489)

**<font color=#1a73e8>作者：</font>** Devis Wawan Saputra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge-tracing benchmarks often compare models that have different access to a learner's previous responses. We examine how data provenance, history length, and representation affect those comparisons. First, we compare a pinned ASSISTments 2009 sequence mirror against the corrected official release. Of 4,148 learners represented in both, 817 have different ordered skill-response sequences; the mirror also contains fewer labeled events. Second, we retain earlier learner-disjoint model evaluations on the 2009 and 2015 datasets, distinguishing exploratory results from a corrective 2015 replication. Finally, we evaluate a new, nonoverlapping sample of 4,000 ASSISTments 2015 learners using three models constrained to the same one-event or 20-event prior-response window. On 20,592 test responses from 582 learners, the 20-event Brier scores were 0.17667 for count-based logistic regression, 0.17389 for an order-aware logistic model, and 0.17514 for a GRU. The GRU-minus-order-aware difference was 0.00125 (95% learner-cluster bootstrap interval [0.00008, 0.00243]); at one prior event, the corresponding difference was 0.00212 [0.00120, 0.00301]. Earlier comparisons had favored the GRU against simpler history summaries. The newer analysis instead favors a logistic comparator that represents order using the same permitted event stream. These results concern predictive performance on particular historical cohorts and model settings. They neither isolate an architectural effect nor establish generalization to contemporary classrooms.

---


### 235. [X-3DComposer: Feed-Forward 3D Scene Composition with Any Assets from Any Views](https://arxiv.org/abs/2611.32491)

**<font color=#1a73e8>作者：</font>** Zidian Qiu, Ancong Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composing an editable 3D scene from images requires an asset for each object and a layout that places the assets. 3D generation and CAD retrieval now supply the assets, but layout still lacks a general solution: scene generation methods couple it with generation, and pose estimators handle one object at a time and need true-size CAD models, depth, or iterative refinement. We present X-3DComposer, a feed-forward model that predicts the layout separately from asset generation. Given one or more images of a scene, the object masks, and an asset for each object from any source, it jointly predicts the rotation, translation, and per-axis scale of all objects in a single forward pass of about one second. The key idea is to treat objects as views: renders of the assets are processed together with the scene images by a multi-view geometry model adapted from VGGT-$\Omega$, and each object pose follows in closed form from the cameras predicted for its renders. Camera intrinsics, camera poses, and depth are optional inputs. When the meshes produced by five scene generation methods are kept fixed and only their layout is replaced, the layouts of X-3DComposer are more accurate than the native layouts of these methods. Compared with the stand-alone layout model SceneMaker, it reduces the scene-level Chamfer distance by 52% on IndoorMix, our test set from six indoor datasets, and by 28% on 3D-FUTURE.

---


### 236. [Assessing Robustness to Catastrophic Forgetting in Continual Deep Reinforcement Learning for Cyber-Physical Systems](https://arxiv.org/abs/2611.32496)

**<font color=#1a73e8>作者：</font>** Kim N. Nolle, Ivana Dusparic, Rhodri Cusack 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As the use of reinforcement learning (RL) becomes more widespread in cyber-physical systems, it becomes increasingly important to design RL agents that are able to adapt to changes in their environments in order to maintain safety and reliability. This paper addresses the question of whether different classes of RL algorithm are more robust against forgetting previously learned behaviours, a critical issue in continual learning, in non-stationary environments. We evaluate the robustness of representative examples of three important classes of RL algorithm in a non-stationary autonomous parking environment. These are Proximal Policy Optimization (PPO), which is a model-free on-policy algorithm, Soft-Actor-Critic (SAC), which is a model-free off-policy algorithm, and Drama, which is a model-based algorithm. The agents must learn to successfully park in four different scenarios, which are presented successively, with parking spaces oriented at varying angles. We find off-policy algorithms appear to be more robust compared to on-policy algorithms due to their use of replay, while model-based algorithms do not appear to offer any direct advantage over model-free algorithms. These experiments also highlight the additional challenges of finding robust abstractions of the environment, and oversensitivity to hyperparameters.

---


### 237. [CalibTrack: Exploring Learned Heteroscedastic Covariance for Robust Multi-Camera Pedestrian Tracking](https://arxiv.org/abs/2611.32500)

**<font color=#1a73e8>作者：</font>** Jack Roberts, Aditya Iyer, Nora Ayanian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Analytical multi-view multi-object tracking (MV-MOT) systems rely on measurement covariance estimates to guide association, fusion, and state estimation. These covariance estimates are typically heuristic, requiring hand-tuning to the specific deployment scenario. We investigate how learned heteroscedastic measurement covariance affects calibration and robustness in analytical multi-camera tracking. To support this analysis, we introduce CalibTrack, a detector-side predictor that replaces uniform measurement covariance with per-detection covariance. We evaluate CalibTrack on the WildTrack and MultiviewX pedestrian tracking datasets with multiple analytical tracker cores, including an identity-informed GM-PHD, JIPDA, and pruned delta-GLMB filter. We additionally evaluate robustness by simulating adverse weather conditions with stable diffusion, Gaussian noise, camera browning, and camera dropout. CalibTrack improves average adverse tracking performance over confidence-scaled covariance, while producing better calibrated predictions, indicating the value of heteroscedastic covariance within analytical tracking. Comparisons with stronger heuristic covariance methods show that the benefits of learned covariance remain bounded by the quality of available observations and the downstream tracker choice. Together, these findings provide a principled exploration of learned covariance estimation and its potential for uncertainty-aware analytical tracking.

---


### 238. [Déjà-VAE: Training-Free Consistent Editing with Pseudo-Invertible Encoders and Latent Back-Projection](https://arxiv.org/abs/2611.32501)

**<font color=#1a73e8>作者：</font>** Ron Libman, Yamit Ehrlich, Ohad Fried 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Consistency is essential to generative workflows: repeated processing should preserve information beyond the changes explicitly requested. In latent diffusion models, this requires stability both when moving between latent and pixel spaces and when applying successive edits. Autoencoding errors and unintended changes from the editing model can accumulate across these operations, progressively altering image structure, texture, and color. We introduce Déjà-VAE, a framework that combines exact autoencoding consistency with calibrated editing stabilization, without training or fine-tuning. Its autoencoding component converts a pretrained variational autoencoder into a surjective pseudo-invertible neural network, with a fixed gain balancing deviations from the pretrained encoder and decoder. The modified decoder $D'$ is an explicit nonlinear right inverse of the encoder $E'$, satisfying $E'(D'(z))=z$ by construction. Consequently, $D'$ is a reflexive generalized inverse: latent round trips preserve their input, up to numerical precision, and repeated image reconstruction is idempotent. To suppress editing drift, adaptive wavelet back-projection finds the closest latent to the editor's output in $\ell_2$, subject to matching the previous latent on wavelet coefficients whose changes fall below calibrated thresholds. This correction is applied once per turn, with no additional network evaluations after calibration. Together, these components support workflows that remain in latent space or interleave generation with pixel-space operations and constraints. Tests across models and editing benchmarks show less drift than stock pipelines and dedicated consistency methods.

---


### 239. [An Integrated Remote Sensing and Machine Learning Framework for Mapping Hazard Associated with Leached Metals](https://arxiv.org/abs/2611.32505)

**<font color=#1a73e8>作者：</font>** Salman Karim, Bahareh Nojabaei, Hosein Foroutan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study integrates satellite remote sensing, groundwater monitoring, and machine learning to map leached-metal-associated hazards at four coal combustion residual (CCR) sites in Virginia, USA. Constituent-specific groundwater concentrations were expressed as Hazard Quotients (HQ) and combined into a composite Hazard Index (HI). Predictors included Sentinel-2 vegetation indices, biophysical parameters, and spatiotemporal metrics (2019-2025), alongside soil, climate, hydrology, topography, and land cover. Six supervised classifiers were evaluated using spatially separated test blocks, feature-set ablation, and leave-one-site-out testing. Higher HQ coincided with lower vegetation indices in 24 of 33 metal-site combinations near monitoring wells (sign test p = 0.007). Well HI was negatively correlated with CIRE and canopy chlorophyll content at three sites (Spearman rho as low as -0.71). Random Forest achieved within-site HI classification accuracies of 0.768-0.924 and higher-HI-class recall of 0.965-0.999. For 34 constituent-site combinations, HQ classification accuracies ranged from 0.775 to 0.989. Environmental covariates generally contributed more predictive information than vegetation features. Removing vegetation predictors did not reduce performance, and distance to the CCR unit alone performed best at one site. Zero-shot cross-site accuracy declined to 0.734-0.749, no better than the majority-class baseline. These findings demonstrate the potential of integrating satellite observations and environmental data with groundwater measurements for site-calibrated spatial hazard screening. The framework identifies indirect environmental associations rather than directly detecting dissolved metals, highlighting the importance of local calibration and independent validation.

---


### 240. [DiffAnchor: Anchor-Space Diffusion for Monocular 3D Hand Pose Estimation](https://arxiv.org/abs/2611.32513)

**<font color=#1a73e8>作者：</font>** Changlong Jiang, Youci Tang, Haohong Kuang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate and efficient monocular 3D hand pose estimation is an important perception capability for embodied human interaction and dexterous manipulation. Recent diffusion-based methods model pose uncertainty by iteratively denoising 3D joint coordinates. However, directly diffusing the final joints requires the generative process to simultaneously explore plausible poses and recover precise coordinates, often relying on additional denoising steps or multiple hypotheses and consequently increasing inference cost. In this work, we propose DiffAnchor, a few-step anchor-space diffusion framework that diffuses anchors rather than joints. Our key insight is that stochastic exploration does not need to operate directly on the final output. Instead, diffusion searches for informative intermediate anchors that serve as local 3D regressors, while anchor-to-joint offset prediction and weighted aggregation complete precise joint localization. Specifically, fixed context anchors provide stable global references, whereas noisy dynamic anchors are iteratively refined toward informative joint regions. An importance-guided anchor selection and replenishment mechanism further retains useful anchors, removes ineffective ones, and explores insufficiently covered regions. This design reduces the precision burden of the diffusion process and enables accurate prediction using only a few denoising steps and a single hypothesis. Extensive experiments on HO-3D V2, NYU, ICVL, and InterHand2.6M demonstrate state-of-the-art performance on the first three benchmarks and competitive performance on challenging interacting-hand estimation, while maintaining inference efficiency comparable to deterministic regression baselines.

---


### 241. [HS-OVSeg: Multi-Granularity Open-Vocabulary Semantic Segmentation in Remote Sensing via Heterogeneous Supervision](https://arxiv.org/abs/2611.32518)

**<font color=#1a73e8>作者：</font>** Wei Huang, Chenying Liu, Xudong Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation (OVSS) enables flexible, text-driven mapping of remote sensing (RS) imagery beyond predefined categories. Despite advances in segmentation foundation models, RS-OVSS remains constrained by the scarcity of large-scale, semantically diverse datasets with accurate pixel-level annotations. Meanwhile, existing RS datasets contain abundant scene- and object-level annotations that offer valuable semantic information but lack precise pixel-wise supervision. To exploit these complementary sources, we propose HS-OVSeg, a unified training framework that integrates heterogeneous scene-, object-, and pixel-level supervision for RS-OVSS. Specifically, we generate pixel-wise pseudo-labels using SAM3, conditioned on scene-level class names and object-level class names with bounding boxes. Combined with ground-truth semantic masks, these pseudo-labels enable joint training across all three annotation granularities through LoRA-based fine-tuning of SAM3. Our unified training spans 20 RS datasets, including 3 scene classification, 4 object detection, and 13 semantic segmentation datasets, with 1,000 images from the 7 classification and detection datasets manually annotated for pixel-level evaluation. HS-OVSeg substantially outperforms existing RS-OVSS models across both the 20 training-source and 5 held-out datasets, demonstrating strong multi-granularity segmentation capabilities under heterogeneous supervision. The code will be publicly available upon publication.

---


### 242. [Rescuing Discarded Boundary Samples in Semi-Supervised Learning](https://arxiv.org/abs/2611.32532)

**<font color=#1a73e8>作者：</font>** Yuzhao Jiang, Meng Zhang, Jie Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The field of semi-supervised learning (SSL) has seen substantial progress, driven by ongoing refinements within the pseudo-label SSL paradigm. The main difficulty lies in reducing the adverse impact of confirmation bias. The predominant approach is to apply a confidence threshold during training to discard low-confidence samples. Nevertheless, while this mitigates the bias, the discarded samples are mostly situated near class boundaries, and consequently, this strategy also loses valuable boundary information. To address this problem, we propose Boundary Refinement and Correction (BRC), an add-on for confidence-thresholded SSL that rescues useful discarded samples without changing how the base SSL method selects pseudo-labels. BRC keeps the original confidence-based selection rule and operates only on the rejected set. It first identifies discarded samples that may still be useful for training, then replaces their original pseudo-labels with corrected soft pseudo-labels and returns them to the unsupervised loss. Extensive experiments on CIFAR-100, STL-10, and TissueMNIST demonstrate the flexibility and broad applicability of BRC across diverse datasets and base SSL methods, reducing error rates by up to 4.97 percentage points. On boundary-near samples, BRC further improves Top-1 accuracy by 12.80 percentage points, directly supporting its ability to refine the model's decision boundary. An exploratory extension to semantic segmentation also yields consistent gains of 1.03-2.39 mIoU, indicating that BRC generalizes beyond image classification.

---


### 243. [RSReasoner: Reformulating and Auditing Geospatial Reasoning Segmentation](https://arxiv.org/abs/2611.32536)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Xinpeng Zhang, Yunrui Zou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial reasoning segmentation aims to localize geographic targets from language requiring semantic inference beyond direct visual perception. However, existing benchmarks often operationalize reasoning as category omission while overlooking attribute mixing, which neglects explicit-category reasoning, introduces perceptual shortcuts, and fails to precisely evaluate reasoning capability. To diagnose and address these limitations, we first reformulate geospatial reasoning segmentation along category expression (explicit vs. implicit) and attribute nature (perceptual vs. inferential), and audit 90,708 queries across existing benchmarks to reveal that pure explicit-inferential queries account for only 0.61% whereas 31.98% mix both attribute types. We then develop a three-stage pipeline that harnesses OpenStreetMap attributes while mitigating geometric and semantic noise to construct RSReasoner, a large-scale dataset of 106,610 images with 213,220 reasoning queries, and RSReasoner-Bench, a diagnostic benchmark of 75,400 queries across four canonical types and controlled variants. Extensive experiments demonstrate that RSReasoner-Bench precisely evaluates model capability across multiple dimensions while exposing shortcut behaviors, and fine-tuning on RSReasoner boosts both reasoning and cross-type generalization. Our findings offer key insights for future geospatial reasoning research and benchmark design. Datasets and code will be released at this https URL.

---


### 244. [Smooth Essential-Manifold Residuals for View-Graph Calibration](https://arxiv.org/abs/2611.32540)

**<font color=#1a73e8>作者：</font>** Viktor Larsson, Johannes Schönberger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> View-graph calibration jointly estimates camera intrinsics from multiple pairwise fundamental matrices. The correct intrinsics transform each fundamental matrix into an essential matrix, casting the calibration problem as minimizing the distance to the essential manifold. We study how to represent this objective for nonlinear least squares. The conventional singular-value formulation collapses two independent essential-matrix constraints into one scalar residual. Its per-edge Gauss-Newton model is therefore rank deficient, which leads to poor convergence. We instead derive an isometric reduction to 2x2 matrices, where each branch of the nonlinear essential-matrix constraint becomes a linear subspace. This reduction yields a smooth two-dimensional residual whose squared norm is exactly the original manifold distance, whose Gauss-Newton approximation is generically full rank, and whose evaluation requires no per-edge singular value decomposition. Experiments show that the new residual retains the estimation accuracy of the geometric objective while converging in fewer, computationally cheaper iterations. Combined with robust initialization and optimization, it achieves state-of-the-art view-graph calibration accuracy at a runtime comparable to inexpensive algebraic objectives.

---


### 245. [Align or Fail: The Hidden Gap in Cross-Domain Panoptic Segmentation](https://arxiv.org/abs/2611.32542)

**<font color=#1a73e8>作者：</font>** Huy Hoang Nguyen, Oliver Zendel, Tobias Glueck 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation backbones are often treated as drop-in upgrades for improving region proposals in open-vocabulary panoptic segmentation (OVPS). Yet, improvements in backbones often fail to translate well into downstream cross-domain performance. Using ODISE, a diffusion-based OVPS model with a CLIP-based recognition branch, as a testbed, we replace its diffusion visual extractor with DINOv2, ConvNeXt, or DINOv3, and find that backbone upgrades can introduce a grouping-recognition mismatch: an alignment gap between dense-region features and CLIP text embeddings. Across source and near-domain, the newer DINOv3 variant improves source-domain performance but collapses on several cross-domain targets, whereas other baselines, interestingly, show the opposite. Stage-wise diagnostics, linear probes, and region-text alignment analyses indicate that DINOv3 embeddings retain semantic information but are geometrically incompatible with CLIP. We test adaptations, including text-side adapters, conformal mask retention (CMR), and a lean 2.7M-parameter visual-side LoRA, and find that text-side adaptation is more sensitive to vocabulary overlap. CMR provides only limited and target-specific gains, indicating that retention alone cannot resolve the full cross-domain failure. To understand why ADE20K resists improvement across all interventions, we evaluate OVSeg, CAT-Seg, and MaskCLIP. This separates two failure axes: a recoverable visual-to-CLIP interface gap that visual-side LoRA largely repairs, and a vocabulary-boundary limitation shared by the evaluated CLIP-based recognition systems that requires different remedies.

---


### 246. [Beyond Robust Algorithmic Recourse: Sharing the Burden of Validity through Model Multiplicity](https://arxiv.org/abs/2611.32543)

**<font color=#1a73e8>作者：</font>** Prakhar Ganesh, Afaf Taïk, Golnoosh Farnadi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Algorithmic recourse provides actionable recommendations that enable individuals to achieve favourable outcomes. Implementing recourse for individuals requires significant time and effort, thus emphasizing robust recourse: recommendations that remain valid even under future model updates. While robustness preserves validity, we show it introduces systematic harms by constraining feasible recommendations to regions that disproportionately reflect majority behavior, reducing individual flexibility and amplifying disparities. Thus, non-robust recourse risks invalidation, whereas robust recourse creates a preference for high-density regions in the data that induces unfairness. However, this trade-off is driven by an implicit assumption that individuals alone should bear the burden of validity. We challenge this narrative and show that strategic model selection can help maintain validity while relaxing robustness requirements for individuals. By leveraging multiplicity, the existence of equally good yet competing models, system owners can share this burden with individuals, thus resolving the tension between validity and unfairness.

---


### 247. [Contact Geometry for Generative Models: An Unbalanced Optimal Transport Formulation](https://arxiv.org/abs/2611.32547)

**<font color=#1a73e8>作者：</font>** Andrea Testa, Søren Hauberg, Andras Gabor Kupcsik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world generative problems in biology, medical imaging, or robotics, rarely come with perfectly paired source and target distributions. While unbalanced Optimal Transport (uOT) provides a robust framework to bridge unpaired datasets via minimum-length paths in probability space, existing formulations based on the Wasserstein-Fisher-Rao (WFR) geometry introduce a structural bias toward high density regions, often triggering mode collapse. We introduce Contact unbalanced Optimal Transport (CuOT), a novel uOT formulation grounded in contact geometry that decouples density transport direction from mass growth to eliminate structural bias. This allows CuOT to adapt sampling steps to the local data structure, naturally reducing step sizes in high-density regions to prevent overshooting and ensuring stable convergence. The result is a stable, scalable path-length minimization solver that consistently outperforms WFR-based methods on biological dynamics reconstruction, unpaired image-to-image translation, and video generation.

---


### 248. [UnifiedAD: One-Shot Anomaly Detection across Modalities via Evidence Calibration](https://arxiv.org/abs/2611.32551)

**<font color=#1a73e8>作者：</font>** Shangze Li, Chuancheng Shi, Simiao Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Both single-modal and multi-modal anomaly detection aim to identify deviations from normal patterns, providing a common foundation for unified detection. However, existing methods rely on modality-specific modeling and scoring, making it difficult to obtain comparable anomaly evidence with limited normal references. To that end, we propose UnifiedAD, which unifies single-modal and multi-modal anomaly detection through anomaly evidence calibration, requiring only one normal reference per target category and no gradient updates. Specifically, we first derive neuron-level discriminative priors from normal and anomalous samples in an independent auxiliary dataset and combine them with neuron response consistency under normality-preserving transformations of the target reference to select reliable neurons, termed anomaly neurons, and identify anomaly directions. Next, we construct a low-rank normal subspace for each layer and modality from the selected neurons' spatial responses to the reference and quantify query feature deviations from normal structure using projection residuals. Finally, we separately calibrate projection residuals and anomaly-direction responses using the response distributions obtained from the normal reference and its transformations, converting them into comparable anomaly evidence for aggregation across layers and modalities. Experiments on multiple anomaly detection benchmarks demonstrate that UnifiedAD achieves strong performance in both image-level anomaly detection and pixel-level anomaly localization.

---


### 249. [PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop Refinement](https://arxiv.org/abs/2611.32554)

**<font color=#1a73e8>作者：</font>** Yang Cao, Zhe Zhu, Yiheng Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmenting a 3D object into semantically meaningful parts requires joint reasoning about geometric structure and semantic context. Pretrained 3D experts provide spatially grounded region proposals, while 2D experts provide semantic cues for identifying object parts. The challenge is to integrate these complementary capabilities into a framework that can both produce meaningful part segmentations and progressively refine them. We present PartAgent, a training-free agentic framework for 3D part segmentation built upon two complementary modules: (i) Structural-Semantic Expert Integration combines regions predicted by the 3D expert with multiview semantic evidence from the 2D expert through image-to-surface correspondences, constructing compositional part partitions at multiple granularities. (ii) Observation-Driven Closed-Loop Partition Refinement observes the current partition and its supporting evidence to select targeted inspection, evidence repair, composition, or reselection actions. It verifies proposed changes and uses the updated state and action outcomes to guide subsequent decisions. On PartObjaverse-Tiny-WT, PartAgent achieves 68.41 mIoU, outperforming the strongest competing method by 8.53 points. Across 3DCoMPaT200, PartNeXt, PartNetE, and PartObjaverse-Tiny, PartAgent achieves the highest mIoU on each dataset, averaging 69.36 across the four datasets, 7.28 points above the highest mean among competing methods.

---


### 250. [Sol$^{3}$: Accelerating Video Diffusion for Free via Hierarchical Sparse Attention Routing](https://arxiv.org/abs/2611.32562)

**<font color=#1a73e8>作者：</font>** Guoxin Fan, Weilun Feng, Chuanguang Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sol-Attn (Sparsifying online attention) combines sparse exact computation with low-cost representative approximation to accelerate training-free inference in diffusion video models. However, intra-block attention can focus on only a few tokens. While preserving these key interactions exactly, the block-level decision incurs the cost of evaluating many low-response members. We propose Sol$^{3}$, a training-free hierarchical sparse attention method that further refines how exact computations are allocated. First, we introduce Gaussian-guided hierarchical routing, which determines the scope of exact computation step by step, from blocks to tokens, using statistical thresholds at each level. Only a subset of members within Mixed blocks that require refinement is selected for exact computation, while representative terms approximate the remaining members. We further design heterogeneous routing statistics that combine block-center correlations with variations in Key and Value within blocks to identify blocks that are difficult to approximate. Among these Mixed blocks, we uniformly compare raw token relevance to select members requiring exact computation. Experiments on video generation, audio-video co-generation, and world simulation tasks demonstrate that Sol$^{3}$ achieves 86% attention sparsity and delivers a $3.07\times$ attention speedup while preserving quality. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-342](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
