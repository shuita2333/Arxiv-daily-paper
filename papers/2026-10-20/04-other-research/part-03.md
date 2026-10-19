# 📦 其他研究 | 2026年10月20日

> 本类共 **213** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-213](./part-05.md)

---

### 101. [Towards a GraphNARX model for structural dynamics](https://arxiv.org/abs/2610.23103)

**<font color=#1a73e8>作者：</font>** George Tsialiamanis, Keith Worden  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The current paper introduces the GraphNARX model, a graph-based nonlinear autoregressive exogenous model for structural dynamics. The model is built to account for the geometry of structures and to model dynamic behaviour as the interaction between elements of the structure. Similar to other types of NARX models, GraphNARX is used for system identification. Nodal attributes of the graph encode past displacements and nodal forces, and the output of the model is the next-timestep displacement. The graph formulation of the model allows it to generalise to structures of different dimensions and degrees of freedom. Moreover, because graph-learning is performed locally between the nodes, the GraphNARX model can also learn to infer displacements of nodes for which data are not available, i.e.\ to perform virtual sensing. The proposed model's performance is evaluated in a system-identification framework and a virtual-sensing framework, and achieves good accuracy and exhibits generalisation capabilities to structures of different sizes.

---


### 102. [Reliability-Consistent Appearance Modeling for RGB-Infrared Multi-Object Tracking](https://arxiv.org/abs/2610.23125)

**<font color=#1a73e8>作者：</font>** Bingyang Wang, Jiazuo Yu, Lu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent RGB-infrared multi-object tracking (MOT) methods have substantially improved cross-modal representation learning and multimodal information integration. However, most existing methods compress RGB and infrared evidence into a unified descriptor. When one modality is temporarily degraded, the tracker can no longer regulate its contribution separately; unreliable evidence may distort association and contaminate appearance memory. We therefore propose RCA-MOT, a reliability-consistent appearance modeling framework that preserves cross-modal complementarity while retaining post-representation evidence controllability. RGB-specific, infrared-specific, and fused identity representations are maintained as jointly accessible appearance states. For each detection, a simple training-free target-scene estimator produces branch-wise appearance reliability used across the two temporal roles of appearance: relative reliability regulates different identity branches, absolute reliability calibrates borderline candidates near the ReID acceptance boundary, and the same branch-wise reliability controls how strongly matched descriptors update historical appearance memory. The individual components are intentionally simple, focusing evaluation on reliability-controllable appearance organization rather than elaborate fusion or learned reliability-estimation modules. RCA-MOT sets new SOTA results on VT-MOT and UniRTL, improving the previous best HOTA by 5.402/6.075 points and IDF1 by 11.549/12.789 points, respectively, while post-hoc analyses further validate reliability as an informative control signal. Code will be released upon acceptance.

---


### 103. [CIIR - Class-Indexed Interface Representation Learning](https://arxiv.org/abs/2610.23151)

**<font color=#1a73e8>作者：</font>** Doo Yon Kim, Christian Wallraven  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal learning commonly assumes paired or synchronized observations, yet independently collected datasets rarely provide such correspondence. We introduce CIIR, a modular encoder--decoder framework that connects heterogeneous datasets through a class-indexed address space while preserving each dataset's native input format and output module. A known local index selects address $k$, and an input-dependent 128-dimensional address representation Z_k(x) is written to that address. To demonstrate CIIR, we learn this address space from handwritten digits, clothing images, spoken-digit spectrograms, and hand signs without synchronized or instance-matched samples. Newly trained label-free receivers recover the requested addresses with 94.7% macro-average Address Realization Accuracy. We then attach the unseen SVHN dataset after freezing the base address space and train only lightweight adapters, achieving 90.2% MNIST>SVHN and 82.3% SVHN>MNIST end-to-end Address Transfer Accuracy without target-side decoder labels. To demonstrate generalizability of CIIR, we reuse the ten addresses as code elements in collision-free arithmetic and hierarchical address codes for all 100 CIFAR-100 classes and evaluate direct arithmetic-code realization through the existing receivers. These results establish CIIR as a compact interface for modular cross-dataset communication and post-hoc dataset attachment without exhaustive paired multimodal supervision.

---


### 104. [QuAD: Quantitative Assessment via Distribution-Alignment for Qualitative Data Quality Enabled by a Content-Aware Multi-Agent System](https://arxiv.org/abs/2610.23153)

**<font color=#1a73e8>作者：</font>** Wenshuo Zhang, Leixian Shen, Qiqi Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Assessing whether qualitative responses collected from semi-structured questions are ready for a particular analysis goal is a persistent challenge. Manual qualitative analysis is interpretive and labor-intensive, while existing automated methods often lack a dataset-level perspective for deciding whether a response set supports a researcher-selected analytical lens. We introduce QuAD, a framework for quantitative pre-analysis assessment of qualitative response datasets. QuAD compares a reconstructed intrinsic cluster distribution reconstructed from responses with an extrinsic, researcher-defined analytical lens derived from metadata. QuAD is structured into a four-quadrant assessment whose metrics are read jointly, from lens-level relations to within-cluster variation, to provide fitness-for-purpose signals for revealing general patterns and unique insights. Because this assessment relies on lens-conditioned inter-response dissimilarity, we propose a content-aware multi-agent system with two-stage instruction generation and adaptive anchors to improve scoring consistency. We validate QuAD through controlled experiments on synthetic data, including robustness and baseline comparisons, and a real-world social survey case study. The case study shows how QuAD quantitatively assesses whether a selected analysis axis is promising and also surfaces representative or unusual responses for human interpretation.

---


### 105. [Nearly Linear Private Learning of Littlestone Classes](https://arxiv.org/abs/2610.23160)

**<font color=#1a73e8>作者：</font>** Shay Moran, Chao Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially private learning aims to learn from data while protecting individual training examples. For binary classification, finite Littlestone dimension characterizes approximate private PAC learnability (Alon et al., JACM 2022). Understanding how this dimension controls private sample complexity remains a central question. For classes of Littlestone dimension $d$, the first general upper bound was doubly exponential in $d$ (Bun, Livni, and Moran, FOCS 2020). Subsequent work improved this to $\widetilde O(d^6)$ (Ghazi et al., STOC 2021) and then to $\widetilde O(d^5)$ (Lyu, STOC 2026). We prove a nearly linear upper bound of $O(d\log d)$.
Our main algorithmic contribution is a structural exponential mechanism for data-dependent candidate sets equipped with a rank satisfying suitable stability conditions. For natural Littlestone classes such as subspace indicators, this rank has a simple geometric interpretation: it is the codimension. This yields a private PAC learner for subspaces of dimension at most $d$ over any field, with tight linear dependence on $d$ and no dependence on the ambient dimension, improving the quadratic dependence of Kaplan et al. (STOC 2025). Our second contribution is combinatorial: drawing on model-theoretic ideas, we construct a suitable rank for general Littlestone classes and establish the counting bounds required by the mechanism.

---


### 106. [Algorithm Modelization: Transforming Optimization Algorithms into Evolvable Intelligence](https://arxiv.org/abs/2610.23161)

**<font color=#1a73e8>作者：</font>** Jian Yao, Zhiyao Zhang, Yichen Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can algorithms be learned and evolved as models, rather than repeatedly redesigned as programs? We explore this question by introducing Algorithm Modelization, a new paradigm that turns iterative algorithms into trainable models. Its central idea is to regard algorithm execution trajectories as computational experience: by learning how algorithmic states evolve over iterations, a model can internalize the knowledge embodied in existing algorithms, reproduce their computational behaviors, and further evolve beyond them through training. As a first realization of this paradigm, we modelize iterative optimization as an autoregressive process, where preceding generations constitute the computational context for generating the next population. We develop a dimension-independent population-temporal architecture to capture both population interactions and iterative dynamics, together with an imitation-to-surpassing learning framework that first acquires algorithmic knowledge from heterogeneous teachers and then improves the resulting optimizer directly through optimization feedback. The modelized optimizer consequently goes beyond reproducing individual algorithms: it consolidates heterogeneous search knowledge into a single trainable model, achieves stronger optimization capability through subsequent improvement, and generalizes its acquired knowledge across problems and substantially larger unseen dimensions. More fundamentally, Algorithm Modelization makes algorithmic capability accumulable through learning, where new algorithms and problem-solving experience can become training resources for progressively improving the model. Our results establish a promising path from manually designed algorithms toward general algorithm models that learn, generalize, and evolve from computational experience.

---


### 107. [Structural Affinity: An Algorithm for Coherent Cage-Based Shape Design](https://arxiv.org/abs/2610.23173)

**<font color=#1a73e8>作者：</font>** Aviraj Newatia, Shengan Yang, Hantao Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cage-based deformation (CBD) parametrises 3D geometry through a small set of control handles, effectively enabling a variety of tasks from animation and interactive modelling to tool-based co-design, neural deformation transfer, and aerodynamic shape optimization. Many optimization approaches relying on CBD employ regularisation strategies to reduce the distortion of the deformed mesh by encouraging smooth, regular cage deformations. These techniques offer soft guidance to an optimization algorithm towards desirable deformations, but compete with the task objective rather than changing the deformation parameterization itself. In this work we introduce Structural Affinity for CBD, an explicit regularisation method which enables smooth deformations through control cages by exploiting a two-cage structure to couple cage-handle motion directly. Structural Affinity precomputes an affinity matrix using mean-value coordinates, binding the inner control-cage to a coarser outer-cage. This matrix defines how much a cage handle displacement propagates to neighbouring handles which substantially decreases and often eliminates cage self-intersections, reduces mesh distortion, and adds linear overhead at deformation time. Across robotic control--morphology co-design, source-to-target neural deformation transfer, and aerodynamic wing shape optimization, Structural Affinity produces more regular deformations and substantially reduces reliance on hand-designed structural loss terms. We report consistent gains on three complementary diagnostics: the cotangent Laplacian, a proxy for surface smoothness; cage distortion, capturing whether control handles move coherently; and surface roughness, which measures undesirable oscillation in wing geometry.

---


### 108. [Do Speech BCIs Need Larger Models? Rethinking Neural Decoding beyond Scaling](https://arxiv.org/abs/2610.23175)

**<font color=#1a73e8>作者：</font>** Zehui Feng, Weichuan Wang, Xiaohan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent speech brain-computer interfaces (BCIs) increasingly rely on large models and complex multi-stage pipelines for neural decoding. However, in speech BCI, where training data are scarce, noisy, and expensive to collect, the benefits of model scaling remain unclear. This work revisits a fundamental question: are large models truly necessary for accurate neural decoding? We propose BEST (Brain-Encoding-Speech-Text), a two-stage framework for efficient neural-to-text decoding. Instead of relying on large generative models or phoneme-centric pipelines, BEST introduces hierarchical intermediate representations and a compact speech-oriented decoder that directly maps neural activity to text. This design preserves essential structure while significantly reducing computational cost, enabling robust generalization in low-resource settings and practical deployment under constrained resources. On the Brain-to-Text '24 and '25 benchmarks, BEST achieves word error rates (WERs) of 6.19% and 1.62%, respectively, using only 3.85% of the parameters required by comparable methods. Beyond these results, we provide three key insights: (1) decoder scaling yields non-monotonic gains; (2) cross-modal alignment is more critical than model size; and (3) overfitting degards sequence-level performance. Representation analysis further reveals a consistent neural-audio-text alignment pathway.

---


### 109. [AMEND: Constraint-Guided Multi-Agent Text Detoxification with Isolated Critics](https://arxiv.org/abs/2610.23183)

**<font color=#1a73e8>作者：</font>** Tianyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text detoxification requires balancing toxicity removal, semantic preservation, and fluency. Existing methods typically optimize an unconstrained scalar objective---enabling safety scores to mask semantic loss---or rely on open-ended iterative debate prone to semantic drift and high computational cost. We propose AMEND, an inference-time framework that decouples detoxification into role-conditioned proposal generation, isolated multidimensional criticism, and constraint-first selection. AMEND evaluates diverse candidates with role-blind critics and enforces strict semantic and fluency feasibility before ranking by utility. To maximize efficiency, AMEND Lite restricts subsequent search to at most one targeted repair round only when residual toxic spans remain. On ParaDetox, one-round selection over diverse roles improves the joint evaluation metric by $+0.0508$ over the best single role. On a frozen confirmation test set, AMEND Lite achieves a joint score of $0.6597 \pm 0.0062$, outperforming unconstrained multi-round loops by $+0.0489$ ($p < 0.05$) while reducing inference requests by 28.4%.

---


### 110. [FuzzInsight: Navigating the Efficiency-Effectiveness Trade-off in Coverage-Guided DNN Fuzzing](https://arxiv.org/abs/2610.23195)

**<font color=#1a73e8>作者：</font>** Vivek Vekariya, Fathiyeh Faghih, Alexander Pretschner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collecting and labeling diverse test datasets for evaluating Deep Neural Networks (DNNs) is costly and time-consuming. This has motivated coverage-guided fuzzing techniques that generate defect-revealing corner cases from limited test data. However, their effectiveness depends heavily on configuration choices, particularly coverage criteria and seed-selection strategies. We present a configuration-oriented analysis and decision guidelines for scalable DNN fuzzing targeting two bottlenecks: inefficient seed utilization and the cost of coverage guidance. Our analysis shows that existing seed-selection strategies repeatedly prioritize a small subset of inputs, leaving many collected seeds unexplored. To address this issue, we propose Equalized Sampling, a constraint-based strategy that increases mean seed queue utilization to 77%, improving on prior approaches by 13 percentage points.
We further evaluate 84 fuzzing configurations on four benchmark datasets: MNIST, SVHN, GTSRB, and CIFAR-100. Results show that the non-structural criteria LSCD, LSC, and MDSC achieve coverage outcomes comparable to structural and alternative non-structural criteria while requiring substantially less computation. These criteria also promote broad behavioral exploration of the DNN under test, reducing the need to monitor multiple coverage metrics. Among them, LSCD provides a modest but consistent runtime advantage.
Finally, we show that retraining with generated corner cases improves generalization robustness by up to 77 percentage points on average without degrading performance on the original test distribution. Together, these findings provide a practical blueprint for selecting fuzzing configurations that balance efficiency, behavioral exploration, and model hardening.

---


### 111. [Non-Parametric Optimization for Scalable Learning in Stochastic Decision Problems](https://arxiv.org/abs/2610.23204)

**<font color=#1a73e8>作者：</font>** Mohsen Amidzadeh, Lauri Viitasaari, Mario Di Francesco  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic optimization (SO) plays a central role in decision-making under uncertainty. Among SO problems, time-varying stochastic optimization (TV-SO) is particularly important due to its applications in adaptive control and machine learning. Non-parametric approaches have been proposed for time-varying deterministic optimization; however, they have not been developed for their stochastic counterparts. This work addresses that gap by developing a stochastic variational framework based on Malliavin calculus. This framework yields non-parametric optimality conditions for SO problems with stochastic decisions and supports the design of a scalable deep-learning algorithm that is insensitive to the parameterization dimension. This algorithm, called the Stochastic Path Follower (SPF), is applied to two important problems under distribution drift, namely least-squares recovery and logistic regression. Experimental results show that the proposed approach outperforms state-of-the-art learning-based and gradient-based methods in both performance and scalability.

---


### 112. [X-Splat: Unified Gaussian Splatting for Joint RGB and X-ray 3D Reconstruction](https://arxiv.org/abs/2610.23237)

**<font color=#1a73e8>作者：</font>** Wangze Xu, Chu Zhou, Mae Yamaguchi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Jointly reconstructing RGB and X-ray provides new insights by connecting external appearance with internal structure, enabling a more complete understanding of real-world objects than single modality. Yet existing methods train separate models per modality and suffer from redundant geometry, alignment artifacts, and loose coupling that limits cross-modal insight discovery. We propose a unified representation in which all Gaussian primitives share a single set of geometric parameters, with only surface-proximal primitives additionally carrying appearance attributes. We perform cross-modal registration through clean multi-view stereo and X-ray geometric proxies instead of aligning two sets of optimized Gaussians, improving alignment stability. We then jointly optimize the unified representation via supervision from both modalities, complemented by a surface-depth consistency loss derived from X-ray geometry to guide RGB reconstruction. Experiments on the InsideOut dataset and our Flower & Insect dataset show that our framework achieves more robust cross-modal alignment, higher RGB rendering quality without compromising X-ray reconstruction, and a more compact representation than maintaining two independent geometries.

---


### 113. [Kingfisher: Fast Personalized Visual Autoregressive Generation via Scale-Aware Prompt-Conditioned Scale Decomposition](https://arxiv.org/abs/2610.23238)

**<font color=#1a73e8>作者：</font>** Dinh-Khoi Vo, Akihiro Sugimoto, Minh-Triet Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized image generation has been extensively studied in diffusion models, often relying on subject-specific optimization of model weights, textual embeddings, LoRA modules, or adapters. In this work, we explore a different direction for fast personalization in visual autoregressive models. Our key observation is that a short prefix of early autoregressive scale codes is sufficient to strongly determine both object structure and global appearance, while later scales primarily refine the established generation trajectory. Based on this insight, we introduce Kingfisher, a model-tuning-free framework that decomposes early residual scale codes into content- and style-related components through prompt-conditioned scale-code subspaces. Given two real images, Kingfisher first decomposes their early scale codes, then recomposes the content components of one image with the style components of the other into a compact semantic prefix. The frozen generator subsequently predicts the remaining scales through bitwise self-correction for coherent refinement. Experiments on CSD-100 show that Kingfisher achieves strong content preservation and the highest style and text alignment among the evaluated methods, while reducing pair-specific preparation time by approximately 54x compared with diffusion-based methods and 7.5x compared with VAR-based alternatives. These results demonstrate that effective personalization can be achieved by directly manipulating the native scale-space representation of a frozen visual autoregressive generator.

---


### 114. [Anisotropic Representation Dynamics in Transformers](https://arxiv.org/abs/2610.23242)

**<font color=#1a73e8>作者：</font>** Nguyen Do, My T. Thai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small differences between internal representations can shrink or grow as they pass through a Transformer layer, affecting how information is preserved and how sensitive the model is to perturbations. Yet it remains unclear when changes in attention weights can turn a representation difference that would otherwise shrink into one that grows. We develop a \textbf{Mixture-Gated Theory of Anisotropic Representation Dynamics} that separates self-attention into value transport, query gating, and key gating. Our analysis reveals how the geometry of attended representations constrains gating and how interactions between these mechanisms can reverse contraction induced by value transport. We formalize this phenomenon as gating-induced regime switching, where a representation difference contracts under fixed attention routing but expands under full attention. We derive a necessary and sufficient spectral criterion that certifies the existence or absence of switching and identifies switching directions without exhaustive search. Beyond existence, our theory characterizes maximum relative switching strength, certifies the severity of contraction that gating can overcome, and determines the largest dimension of a subspace in which every nonzero direction switches. Experiments across four Transformer architectures validate these predictions through analytical and finite-forward comparisons, revealing distinct and joint query--key gating mechanisms and nontrivial switching subspaces. Our results provide a mechanistic and spectral understanding of how attention routing can alter local representation dynamics.

---


### 115. [Think More or Read More? A Token-Budget Theory of Reasoning with Shared Context](https://arxiv.org/abs/2610.23246)

**<font color=#1a73e8>作者：</font>** Manh Nguyen, Sunil Gupta, Hung Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning systems increasingly improve answers by incorporating additional context into the model's input, from multi-agent debate, where agents read their peers' responses, to self-refinement, where a model revisits its own drafts. In these systems, communication consumes context as one agent's output becomes another's input. We study the regime where token reading and generation draw on one fixed token window, so every token spent reading is a token that cannot be spent reasoning. We develop a \textbf{token-budget theory} that formalizes this trade-off, modeling accuracy as a function of the reasoning budget remaining after reading and aggregating votes with a Condorcet jury model that permits correlated errors. For multi-agent debate, the theory gives a closed-form prediction for the optimal number of agents. This quantity is estimated from single-agent measurements, allowing the optimal group size to be determined without running debate, and the same accounting extends to a heterogeneous set of different models. We empirically verify our theory and show that, at the predicted group size, our method outperforms strong baselines under the tightest calibration spend, where debate-calibrated rules can afford only one or two questions. Self-refinement obeys the same accounting, with its own draft in place of a peer message. The theory further predicts that communication pays only when the gain in the accuracy ceiling exceeds the reasoning room spent on reading, with this condition tightening as the window shrinks. Across five open models and four reasoning tasks, self-consistency matches or beats deployed debate at $93$\% of $980$ matched window-and-group-size settings, with the gap being largest under tight windows and nearly disappearing at a loose one, consistent with the theory. Under a shared window, how much room a model has left to \textit{think matters more than what it reads}.

---


### 116. [Can the Parts Fool the Test? Counterfactual Pairing Cycles for Relational OOD](https://arxiv.org/abs/2610.23248)

**<font color=#1a73e8>作者：</font>** Yibo Zhou, Yirong Xiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Relational out-of-distribution errors are easy to describe and hard to evaluate cleanly. An image may be natural, a caption may be fluent, and all mentioned objects may be common, yet the caption may describe the wrong relation in the image. Many evaluations intended to test this behavior can be solved without checking the pairing at all, because negatives differ in caption style, template, length, object frequency, or image statistics. We propose counterfactual pairing cycles, a blocked evaluation primitive that reuses the same two images and the same two captions on both sides of the comparison, changing only which image is paired with which caption. This makes image-only, text-only, and additive component shortcuts cancel exactly in finite samples. The same contrast also gives a training loss for relational outlier exposure and a diagnostic for bilinear vision-language scores. Across synthetic controls, GQA, and COCO, cycles separate coarse image-caption matching from directional role-binding failures, while also identifying geometric size relations that remain strongly visible in global features. In a shortcut-contaminated COCO outlier-exposure stress test, a model selected by a near-perfect shortcut validation AUROC retains substantial relational signal but remains below cycle training on exact cycles; cycle training improves CycleAcc from 0.882 to 0.927. The main lesson is simple: to test whether a model understands a pairing, the benchmark should keep the parts fixed, change the pairing, and ask only about coupling. The official implementation is available online.

---


### 117. [LonGaussian: Tracking Foundation Priors for Long-Context Feedforward Gaussian Reconstruction](https://arxiv.org/abs/2610.23250)

**<font color=#1a73e8>作者：</font>** Zhoufeng Xie, Guanjun Wu, Shuai Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing high-quality, renderable 3D scenes from long videos is essential for robotic perception and embodied intelligence. Many feed-forward Gaussian reconstruction methods rapidly predict 3D scenes from a small set of images, but extending them to longer sequences presents two bottlenecks: jointly processing all views increases GPU memory requirements, while accumulating pixel-aligned predictions redundantly represents the same surfaces and increases storage and rendering costs. We present LonGaussian, a streaming feed-forward framework that reconstructs compact, globally renderable Gaussian scenes from long image sequences with known intrinsics and unknown camera poses. Built on a pretrained streaming 3D reconstruction backbone, LonGaussian decodes long-context geometric features into dense Gaussians. Within each chunk, multi-frame point tracks link repeated observations of the same surface and guide a learned merger to consolidate the corresponding Gaussian predictions. Rendered-depth consistency filtering further suppresses Gaussians from other chunks that incorrectly occlude locally reconstructed surfaces. On DL3DV and RealEstate10K benchmarks, LonGaussian improves novel-view rendering quality while using substantially fewer Gaussians than the evaluated feed-forward baselines.

---


### 118. [When Ubiquitous Health Data Stops Helping: Patients' Experience of Breakdowns in the Data-Interpretation-Action Loop at the End of Life](https://arxiv.org/abs/2610.23259)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Xinru Wang, Zhuoyan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Ubiquitous computing systems in healthcare often assume that greater data visibility improves awareness, interpretation, and action. In end-of-life care, however, this assumption warrants scrutiny. Through semi-structured interviews with 25 terminal-stage patients as primary informants and 8 clinicians as supplementary informants, we examine patients' descriptions of how they encountered, interpreted, acted on, and disengaged from state signals, trajectories, algorithmic outputs, and behavioral audits. Our analysis identifies three recurrent patterns in these descriptions. First, participants described repeated and unresolved sensemaking when visible data lacked explanatory pathways. Second, they described outputs they could understand but whose suggested actions did not fit their changing bodily capacities, care goals, or decision-making roles. Third, they described difficulty disengaging when data remained embedded across care environments. Rather than rejecting data altogether, patients called for less data exposure and a reorientation toward existential support. Based on this analysis, we situate data exposure as a central interaction problem in end-of-life ubiquitous computing and derive design implications for interpretive stability, care-context alignment, and existential support.

---


### 119. [SCALE: Improving Guidance-Free Visual Generation via Self-Contrastive Alignment for Likelihood Estimation](https://arxiv.org/abs/2610.23263)

**<font color=#1a73e8>作者：</font>** Jiwan Hur, Dong-Jae Lee, Dongyeun Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classifier-free guidance (CFG) is essential for improving sample quality in visual generation, but it incurs substantial sampling overhead. Existing guidance-free approaches halve this cost by approximating the CFG with a single model inference, but their performance is bounded by the CFG and inherits its limitations. In this paper, we propose self-contrastive guidance (SCG), which contrasts the model's prediction on real and self-generated samples to obtain a direct, model-based signal that pushes generation toward the true data manifold. Integrating SCG into the standard likelihood objective via reparameterization yields Self-Contrastive Alignment for Likelihood Estimation (SCALE), a guidance-free training framework that produces SCG-enhanced predictions in a single forward pass. Across class-conditional and text-to-image generation on diffusion and autoregressive models, SCALE consistently outperforms CFG-mimicking guidance-free baselines and improves further when combined with DPO, demonstrating that the self-contrastive signal yields gains complementary to both CFG and preference-based fine-tuning.

---


### 120. [ADT: All-Atom Diffusion Tokenizer for 3D Molecular Structures](https://arxiv.org/abs/2610.23265)

**<font color=#1a73e8>作者：</font>** Xuantuo Huang, Encheng Su, Aoran Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete structural tokenization provides a promising route to autoregressive 3D molecular generation. Yet, existing tokenizers face a trade-off between compact representation and all-atom reconstruction: atom-level tokens preserve atomic details but produce long sequences, while compact residue-level protein tokens typically omit side-chain geometry. To overcome this limitation, we propose All-atom Diffusion Tokenizer (ADT), which decouples token granularity from reconstruction resolution. ADT uses one structural token per atom for small molecules and one token per protein residue that jointly represents backbone and side-chain geometry. To mitigate geometric distortion introduced by quantization, we leverage the generative capacity of diffusion models to recover fine-grained atomic geometry beyond deterministic decoding from discrete tokens. Extensive experiments across small molecules and proteins demonstrate that ADT achieves strong reconstruction from compact discrete representations while enabling high-quality autoregressive generation of both small molecules and all-atom protein structures. These results establish compact structural tokens as an effective discrete interface for all-atom molecular reconstruction and generation.

---


### 121. [Agentic Image Generation in the Wild](https://arxiv.org/abs/2610.23269)

**<font color=#1a73e8>作者：</font>** Yifan Li, Bowen Qin, Kun Zhou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic image generation pairs an image generator with a search agent that retrieves references from the web, extending generation beyond the generator's training data. Real-world requests, however, often concern entities that appeared only days ago. We call this setting Image Generation in the Wild. In this setting, the web offers limited visual evidence, search results are crowded with easily confused entities, and the target is rarely shown on its own. To study this setting, we build an automated pipeline that synthesizes prompts from recent headlines and keeps only those whose real search results are highly confusing, yielding requests that are hard to solve yet natural to ask. With it, we construct Savanna, a benchmark of 500 prompts across 16 subcategories. On Savanna, even harness frameworks built on the frontier models retrieve a correct reference for only about half of the prompts. We then propose Locate-Corroborate-Isolate, a paradigm in which the agent first pins down the target's identity through text search, then verifies candidate images against multiple sources, and finally crops a clean reference for the generator. Trained on 15K trajectories that follow this paradigm, Ranger-8B achieves a search score of 67.2, outperforming harnesses equipped with frontier models. It also achieves the best generation quality with every generator we test, and surpasses prior agentic methods on other image generation benchmarks. We release the pipeline, benchmark, training data and model at this https URL.

---


### 122. [DeDiCa: A Scalable Deconfounding Discrete Causal Generative Model](https://arxiv.org/abs/2610.23272)

**<font color=#1a73e8>作者：</font>** Kunchangtai Liang, Adrián Javaloy, Antonio Vergari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce DeDiCa, a practical framework for efficient causal inference with discrete variables and hidden confounding that revisits classical probabilistic modeling through a tensorized parameterization of causal Bayesian networks, enabling tractable inference. Given a causal graph, DeDiCa is trained once on observational data by maximum likelihood, exactly marginalizing over hidden confounders, and can then estimate any (proxy-)identifiable interventional query. Despite this deliberately simple parameterization, DeDiCa matches state-of-the-art neural causal generative models in ATE estimation, while supporting memory-efficient CPU training and exact interventional inference in milliseconds. Compared with causal foundation models, DeDiCa scales more effectively with additional observational samples and achieves competitive accuracy at substantially lower inference time and memory. DeDiCa provides a tractable, accurate, and scalable approach to causal inference in discrete settings with hidden confounding.

---


### 123. ["Can Computing Systems Eventually Disappear?": A Long-Term Tracking Study on the Use of Diabetes Computing Systems by Patients with Diabetes](https://arxiv.org/abs/2610.23276)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Jinyuan Zhan, Yao Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Ubiquitous computing has long pursued Weiser's vision of technologies that "disappear" into everyday life. As wearable health systems advance, they increasingly substitute for rather than scaffold users' judgment, yet the long-term consequences remain underexplored. We report an eight-year, five-wave longitudinal interview study from 2017 to 2025 with 37 patients with diabetes, complemented by interviews with 15 clinicians, designers, and vendors. Across three technological generations including glucometers, continuous glucose monitoring, and predictive and automated insulin delivery systems, we identify a novel user state, continued use with cognitive disengagement. In this state, devices remain in use but active interpretation and questioning recede, leaving users to respond only to alarms. This state emerges from functional expansion, delegation of interpretive authority, and information fatigue, and is reinforced by clinical prioritization, information compression, and automation. It results in less frequent independent health judgment and a shift from understanding to responding. We argue that future diabetes computing systems should reduce unnecessary cognitive work while preserving users' opportunities to interpret, contextualize, and question system outputs.

---


### 124. [I2V-DETACH: Source Grounding Detachment for Unauthorized Image-to-Video Generation](https://arxiv.org/abs/2610.23287)

**<font color=#1a73e8>作者：</font>** Chanhui Lee, Yeonghwan Song, Yewon Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion models have advanced image-conditioned video generation, but their accessibility raises risks of unauthorized manipulation. Image immunization has emerged as a promising defense for Image-to-Video (I2V) protection, yet existing methods often rely on degrading visual quality or temporal coherence. In this work, we revisit I2V immunization as reducing source-content preservation, shifting the focus from output degradation to weakening source-conditioned content propagation. To this end, we propose I2V-DETACH, an image immunization method that prevents unauthorized I2V generation through source grounding detachment. I2V models preserve source content by propagating source-image cues into video latents during denoising. Accordingly, I2V-DETACH disrupts this process in two complementary ways: it suppresses source-video grounding to reduce source cue propagation, and strengthens intra-video interactions to shift denoising toward video-side dynamics with reduced reliance on the source image. To obtain informative optimization signals, we initialize auxiliary video latents with source-oriented states that remain within the source-conditioned generation regime while deviating from source-preserving trajectories. Extensive experiments across diverse diffusion architectures show that I2V-DETACH substantially reduces source-content preservation, improves over prior immunization methods, and exhibits strong black-box transferability.

---


### 125. [Data-Efficient Classifier Pretraining Through Diffusion Models](https://arxiv.org/abs/2610.23289)

**<font color=#1a73e8>作者：</font>** Qinyu Li, Yee Whye Teh, Chris Holmes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning with limited data is susceptible to overfitting, especially with modern deep neural networks. Prior to the introduction of AlexNet, reconstruction-based pretraining with auto-encoder and denoising auto-encoder were found to be beneficial, partially due to the limited size of the training sets at the time. Motivated by these traditional approaches, we propose DiffPT, a simple diffusion modeling approach to pretrain a given classifier backbone for limited domain-specific training data. We experiment on time-series data, standard natural-image benchmarks, and medical imaging datasets, and contrast the diffusion approach to a multitude of modern and traditional un/self-supervised methods. While contrastive pretraining performs better on CIFAR-10 and Tiny ImageNet in low-data regimes, DiffPT is particularly effective on medical imaging and time-series tasks, where it outperforms self-supervised baselines across a range of low-data regimes. Our results suggest that DiffPT is a simple and effective approach for data-efficient classifier pretraining on different modalities.

---


### 126. [FlashReFocus: Interactive Image Refocusing in Seconds](https://arxiv.org/abs/2610.23297)

**<font color=#1a73e8>作者：</font>** Ching-Heng Cheng, Chia-Ming Lee, Ming-Ching Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image refocusing changes the focal plane and depth of field of a photograph after capture. It is inherently interactive: users try many focal points and blur strengths on one image, so each edit should be fast and change only the blur. Recent generative methods, however, rerun large diffusion models for every edit. We observe that the two sub-problems differ in kind: recovering the all-in-focus image is ill-posed and needs a generative prior, whereas rendering blur is largely determined by depth and the focal plane. We therefore propose FlashReFocus, which runs diffusion once per photograph and renders every edit with a lightweight network. To address the ill-posed restoration, a one-step diffusion deblurrer with a decoder refiner recovers fine detail efficiently while balancing fidelity and perceptual quality. For precise control, the renderer is conditioned on an explicit defocus map and uses defocus-bias attention, which lets pixels at similar defocus share information without interference from pixels at other depths; in-focus content stays unchanged, and editing the map yields tilt-shift and two focal planes. To further test generalization to unseen cameras, we collect 3CReal, a three-camera benchmark of 89 pairs. FlashReFocus achieves the best perceptual fidelity for zero-shot bokeh rendering on EBB! and 3CReal, refocuses 148.3x faster than GenRefocus, and takes about half a second per further edit, 462x faster.

---


### 127. [On the (In)stability of Adaptive Fee Mechanisms in Multi-Chain Systems](https://arxiv.org/abs/2610.23305)

**<font color=#1a73e8>作者：</font>** Yifan Zhou, Jiang Xiao, Xuechao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> EIP-1559 has become the dominant transaction fee mechanism in permissionless blockchains, regulating scarce block space through an adaptive base fee. The design balances a trade-off between responsiveness to demand fluctuations and stability of long-term resource usage. On a single chain, this trade-off is well understood and empirically stable. In multi-chain systems, however, cross-chain flows introduce delayed economic interactions across otherwise independent fee markets. These interactions alter the control dynamics and create stability risks that existing models do not capture. Deployed systems have already polarized. Polkadot enforces conservative update rates, effectively disabling fee adaptivity and reverting the market to inefficient first-price auctions. Cosmos adopts aggressive update rates without formal guarantees.
To fill this gap, we propose a control-theoretic framework that formalizes multi-chain fee markets as a nonlinear dynamical system with delayed feedback. We identify delay-amplified over-correction as the structural root of instability. Experiments show that cross-chain coupling erodes stability relative to monolithic blockchains, reducing the safe parameter space for base fee update rates by up to 84.8%. Moreover, instability propagates across chains, contaminating the otherwise stable peer chains. At Ethereum's update rate, which leaves a monolithic chain stable, the multi-chain system exhibits extreme load oscillation between full and near-empty blocks, with over half of all blocks at full capacity. Mainstream Cosmos chains already exceed their safe bounds under their default configurations, and the resulting load oscillation raises their block failure rate by an order of magnitude. Guided by this mechanism, we design a lightweight protocol-level mitigation that removes the over-correction and stabilizes dynamics in multi-chain environments.

---


### 128. [Untrained CNN and coefficient-space regularization for joint reconstruction in photoacoustic tomography](https://arxiv.org/abs/2610.23315)

**<font color=#1a73e8>作者：</font>** Alfio Bozi, Anwesa Dey, Souvik Roy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The joint reconstruction of the initial pressure and spatially varying sound speed in photoacoustic tomography from boundary measurements is considered. A regularized data-driven framework is proposed in which the unknown fields are represented in finite-dimensional wavelet spaces and fixed nonlinear features generated by an untrained convolutional neural network (CNN) are used to reconstruct the initial-pressure coefficients through Tikhonov-regularized least squares. A learned coefficient-space prior is subsequently used to infer the squared sound-speed coefficients. Numerical experiments demonstrate accurate reconstruction on held-out data and strong generalization to previously unseen phantom geometries. The frozen reconstruction map also remains stable under measurement noise not represented during training, with only minor changes in reconstruction accuracy for noise levels up to $10\%$. In comparison with the supervised trained-CNN approach considered in this work, the untrained representation yields substantially smaller reconstruction errors while requiring approximately one-sixth of the computational time. These results demonstrate that fixed random convolutional features combined with regularized coefficient-space learning provide an efficient and robust approach to joint reconstruction in photoacoustic tomography.

---


### 129. [Peak-Memory Schedules You Can Trust: Exact Realization, Certified Optimality, and the Limits of Recomputation for Inference](https://arxiv.org/abs/2610.23328)

**<font color=#1a73e8>作者：</font>** Ivan Fomin, Ivan Koryabkin, Boris Sheludko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time inference on small devices needs low activation memory without extra latency, which makes operator order the most valuable memory lever: it is free in time. We show that the usual way of deploying a better order, handing it back to the compiler and regenerating code, is unreliable. In PyTorch Inductor the regenerated program misses its predicted peak in 22 of 54 CPU configurations. It is worse than the stock program in 9 of them and in 19 of 50 on a GPU, and on the GPU it also changes numerical results. We instead profile the generated program, model its memory exactly from its own statements and their read/write effects, and permute those statements. We prove that this realizes the modeled peak whenever allocation does not depend on history. It does so to the byte, with bitwise-identical results, in all our CPU runs. On the GPU we characterize why the caching allocator breaks the condition. To know when to stop, we give forward and reverse "trap" lower bounds, each computable with $O(n^2)$ minimum cuts. They certify the found order optimal for 94% of held-out wrapper graphs and all 16 microcontroller-class models we study, in under a second. So most inference graphs are already scheduled optimally. Branching networks are the exception, where reordering is free and pays, e.g. 10.0% on DeepLabV3. In compiled training we save up to 7.6%. Beyond the certified optimum we study selective recomputation with per-operator caps. It is strongly NP-hard for every fixed cap even at treewidth two, encodes knapsack exactly on series-parallel graphs, and is solvable exactly on bounded treewidth. It is useless on public tiny models whose peak is a single layer, but on architectures that hold a cheap value for a late reuse it pays: on the public ReDimNet speaker networks, whose order is already optimal, it lowers the peak by 5.2-6.1% at under 0.4% extra MACs, with bitwise-identical outputs.

---


### 130. [HiPredict: Predicting the missing HiRISE RED4 spectral channel with machine learning](https://arxiv.org/abs/2610.23335)

**<font color=#1a73e8>作者：</font>** Ardan Suphi, Ben Moseley, Gareth S Collins 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The High Resolution Imaging Science Experiment (HiRISE) onboard the Mars Reconnaissance Orbiter (MRO) acquires imagery of Mars at 25--30 cm/pixel, supporting studies of martian geology, climate history, and landing-site characterization. Its 14-detector focal plane assembly includes several overlapping detectors that enable the acquisition of three-channel colour-infrared images, which are important for identifying compositional variations and studying active surface processes. In 2023, a detector in the center of the focal plane assembly (RED4) began failing intermittently, creating a gap in acquired imagery and reducing the instrument's colour-imaging capability by half. The HiRISE processing pipeline provides a synthetic red (SYN4) channel obtained by linearly scaling the co-located infrared (IR10) channel. However, this approach cannot capture observed non-linear relationships between the colour channels, limiting its accuracy and applicability. Here, we present HiPredict, a machine-learning framework that reconstructs RED4 from co-located IR10 and blue-green (BG12) imagery, neighbouring red-channel observations, and acquisition metadata. The model employs a U-Net architecture to learn non-linear spatiotemporal-spectral relationships between these inputs and is trained on 81,717 training samples, representing 13,625 observations. Evaluated on 23,348 test samples, representing 3,892 pre-failure observations, HiPredict reconstructs RED4 with a Normalised Mean Absolute Error of 1.1%, substantially outperforming SYN4 (3.1%). The reconstructed products improve colour image recovery and more closely represent features of interest such as icy craters, stratigraphy exposed along ridge crests and chloride deposits. We release HiPredict as an open software tool. This work demonstrates the potential of machine learning to mitigate data loss as planetary missions age and naturally degrade.

---


### 131. [SETAREH Transform: A Sorting-Assisted Haar-Wavelet Sparsification Method for Approximate Inner-Product Computation](https://arxiv.org/abs/2610.23338)

**<font color=#1a73e8>作者：</font>** Seyed Kamaledin Setarehdan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep learning systems increasingly rely on high-dimensional vector operations, in which large input and parameter vectors are repeatedly stored, transferred, and processed. Although substantial research has focused on reducing neural-network model size through pruning, quantization, knowledge distillation, and efficient architectures, the storage, memory-traffic, and communication costs associated with repeatedly presented high-dimensional input vectors remain important practical considerations, particularly in distributed and edge-computing environments. This paper proposes the SETAREH (Sorting-assisted Energy-concentrating Transform for Approximate Representation using Haar wavelets) transform, a Haar-wavelet-based sparsification approach for approximating the inner product between a fixed high-dimensional coefficient vector and successive input vectors. By applying the same sequence of permutations and Haar transforms to both vectors, SETAREH preserves the exact inner product before truncation. It then retains only a subset of the transformed coefficient-input pairs, reducing their representation cost while introducing a controllable approximation error. To evaluate SETAREH, we consider two complementary experimental settings: a synthetic Gaussian-vector baseline and a real apparent-age estimation task using a convolutional neural network on the APPA-REAL dataset. The results show that SETAREH can approximate the evaluated inner products using substantially fewer transformed coefficient-input pairs than the original vector dimension. The findings support its use as a potential structured data-representation method for repeated inner products with fixed weights, while the practical benefit depends on approximation accuracy and the cost of storing or transmitting permutation metadata.

---


### 132. [How Finite-Rank Bottlenecks Shape the Low-Rank Adaptation Landscape](https://arxiv.org/abs/2610.23343)

**<font color=#1a73e8>作者：</font>** Long Nguyen-Chi, Quynh Nguyen, Thanh Nguyen-Cung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) has become the standard method for parameter-efficient fine-tuning of large pretrained models, yet theoretical explanations for why low-rank updates suffice remain incomplete. Most existing analyses rely on the Neural Tangent Kernel (NTK) regime, which linearizes the network around the pretrained weights. In this work, we take a different approach that requires no linearization: our key observation is that, once the backbone is frozen, the loss sees each adapted weight matrix only through a finite-rank linear map induced by the frozen activations. Trace-norm regularization then forces the optimizer to pick a low-rank matrix among all matrices that produce the same observed output. This yields global minimizers whose ranks are controlled by the rank of this map, which we call the \emph{bottleneck rank}, rather than the sample size. For multi-head attention, we obtain tighter rank upper bounds by exploiting two additional invariances: row-wise softmax is insensitive to additive row constants in the score matrix, and value updates are observable only after attention weighting and frozen output projection. For the factorized LoRA objective with weight decay, we prove a complementary result on the nonconvex side: after an arbitrarily small generic positive semidefinite perturbation, every first-order stationary point is rank-deficient once the LoRA rank exceeds a threshold determined by the bottleneck rank. Finally, we show that global minimizers of the perturbed objective are near-optimal for the original trace-norm problem, and we provide uniform generalization bounds governed by the spectral structure of the frozen features.

---


### 133. [OliO: ODE-based Linear Transition Operator for Self-Supervised Time Series Forecasting](https://arxiv.org/abs/2610.23345)

**<font color=#1a73e8>作者：</font>** Kwangryeol Park, Seulki Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-supervised representation learning has advanced time series forecasting by capturing robust features from unlabeled data. However, existing contrastive and masking-based methods often struggle to explicitly model the underlying temporal flow, either by treating time lag as noise or by disrupting the inherent temporal dynamics essential for forecasting. To address these limitations, we propose OliO (**O**DE-based **Li**near Transition **O**perator), a plug-and-play self-supervised learning method that learns bidirectional temporal flows as a continuous and structurally consistent dynamical system. OliO introduces a transition operator derived from linear Ordinary Differential Equations (ODEs) to align latent representations across arbitrary time shifts. By imposing a strictly upper triangular constraint on the transition matrix, we mathematically ensure numerical stability and enforce a robust polynomial boundary that effectively captures long-term dependencies while preventing the exponential divergence typically found in unconstrained ODE-based models. This structural constraint induces a temporally coherent representation space that preserves the underlying flow essential for accurate forecasting. Extensive experiments across various backbone architectures and benchmarks demonstrate that OliO achieves significant performance gains, providing Mean Squared Error (MSE) reductions of up to 5.75% over the most competitive grid-searched SOTA baselines. The code is available at *this https URL

---


### 134. [RTSM: Adapting Recursive Models to Multivariate Time-Series Classification](https://arxiv.org/abs/2610.23353)

**<font color=#1a73e8>作者：</font>** Georg Tenzing, Anna Tegon, Luca Benini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate multivariate time-series classification requires extracting temporal features and integrating information across a sequence. Weight-tied refinement offers a way to repeatedly process these features without allocating new parameters at each stage. Applying this principle to time series requires choosing both a temporal representation and a latent-state organization suited to classification. We introduce the Recursive Time-Series Model (RTSM), which combines a learned convolutional temporal tokenizer, single-state weight-tied refinement, and a pooled classification readout. Across all 30 UEA datasets, RTSM achieves 72.81% mean accuracy under validation-based configuration and checkpoint selection, the highest observed mean among the 17 evaluated deep-learning models and 1.60 percentage points above MambaSL. Ablations on eight datasets favor the proposed tokenizer over a simple convolutional embedding and the single-state model over the tested two-state variants. The complete classifier reaches 86.10% mean accuracy versus 84.79% for a separately trained tokenizer-only classifier. These findings identify temporal encoding and state organization as key design choices for adapting recursive architectures to time series. The resulting classifier combines competitive accuracy with a shared refinement module whose parameter count is independent of computational depth.

---


### 135. [STC-MGNet: Spatial-Temporal-Channel Attention-Enhanced Multimodal Graph Network for Pedestrian Intention Prediction](https://arxiv.org/abs/2610.23356)

**<font color=#1a73e8>作者：</font>** Yuanzhe Li, Meng Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of pedestrian crossing intentions plays a critical role in enhancing the safety of pedestrian-vehicle interactions in autonomous driving. However, effectively capturing subtle spatiotemporal patterns in pedestrian pose sequences and integrating complementary visual and ego-vehicle motion information remain challenging. This paper proposes a spatial-temporal-channel attention-enhanced multimodal graph network (STC-MGNet) for pedestrian crossing intention prediction. STC-MGNet introduces a spatial-temporal-channel (STC) attention-enhanced pose graph encoder to learn discriminative representations from pedestrian pose sequences. Three parallel attention branches selectively emphasize informative skeletal joints, observation frames, and feature channels, with their outputs integrated through learnable fusion weights. To leverage complementary visual and ego-vehicle motion information, a multi-stage cross-modal channel modulation mechanism is introduced to adaptively refine pose representations through modality-specific channel gating at successive graph encoding stages. Experimental results demonstrate that STC-MGNet achieves accuracy rates of 70%, 87%, and 88% on the JAADbeh, JAADall, and PIE datasets, respectively, outperforming several representative baseline methods. Ablation experiments further highlight the complementary contributions of visual and ego-vehicle motion information to prediction performance.

---


### 136. [UniPolar: Joint Image and Polarimetric Restoration under Compound Degradations via Physical Consistency Learning](https://arxiv.org/abs/2610.23360)

**<font color=#1a73e8>作者：</font>** Yang Jin, Guangyu Guo, Linghao Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Polarimetric image restoration aims to recover polarization angle images and reliable polarimetric quantities from degraded observations. Beyond visual fidelity, it also requires preserving the physical relationships underlying reliable polarimetric estimation. However, existing methods typically address either device- or environment-induced degradations in isolation, limiting their applicability to color polarization filter array (CPFA) imaging, where both often coexist. Such compound degradations jointly perturb image intensities and cross angle polarization differences. Consequently, improved image fidelity alone does not necessarily ensure accurate Stokes, DoLP, and AoLP recovery. To address this challenge, we propose UniPolar, a coupled Image Stokes framework for joint image polarimetric restoration from compound-degraded CPFA observations. Specifically, UniPolar employs two complementary streams to reconstruct four polarization-angle images and directly predict Stokes difference components. To coordinate these streams, Degradation Conditioned Cross Domain Interaction combines Dual Domain Frequency Interaction for frequency selective evidence exchange with Degradation Conditioned Modulation for condition adaptive feature correction. Furthermore, at the output level, Image Stokes Physical Consistency Learning aligns image derived and directly predicted Stokes components while regularizing angular fidelity and the physical feasibility of DoLP. On the compound-degradation benchmark, UniPolar achieves average image and DoLP PSNR of 31.522 dB and 24.097 dB, respectively, with an average AoLP error of 16.833 degree. These results underscore the importance of jointly considering visual fidelity and polarimetric reliability, offering a physically grounded perspective on learning based restoration under compound degradations.

---


### 137. [MOSS-Image Technical Report](https://arxiv.org/abs/2610.23374)

**<font color=#1a73e8>作者：</font>** MOSI.AI  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system that combines high-fidelity visual synthesis with intent-aware composition. First, we pretrain a 5B single-stream diffusion transformer (DiT) from scratch with a carefully designed recipe, enabling bilingual long-form text rendering and precise layout control. Second, we develop an intention-aware agentic prompt enhancement (PE) module that translates diverse user requests into detailed content and layout specifications. Together, they enable MOSS-Image to generate text-rich and layout-coherent images. We further introduce LongLongTextBench (LLTB) for evaluating long-form English and Chinese text rendering, and RealLayoutArena (RLA) for end-to-end layout-rich generation. MOSS-Image achieves state-of-the-art performance among open-weight models on LLTB, with an average text coverage of 96.3%. On RLA, MOSS-Image ranks second in the end-to-end system comparison, while its backbone ranks first among generators evaluated with shared enhanced prompts. We will release the model, training recipe, and evaluation framework to support further research and promote the text-to-image community.

---


### 138. [Sentence-Level Topic Modeling with Lexical and Contextual Evidence](https://arxiv.org/abs/2610.23388)

**<font color=#1a73e8>作者：</font>** Federica Granese, Serena Villata, Charles Bouveyron  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Topic modeling faces a fundamental granularity dilemma: probabilistic topic models assign topics at the word level, whereas transformer-based methods operate at the document level. The latter overlooks that real-world documents typically cover multiple topics, whereas the former relies on individual words, which rarely provide sufficient context to identify them. We introduce SentenceETM, a neural topic model that assigns a topic to each sentence by jointly using lexical and contextual evidence. Each topic is described both by a distribution over the vocabulary, defined through word embeddings, and by a Gaussian over sentence embeddings concentrated on a topic-specific low-dimensional subspace. The topic of a sentence generates both its words and its embedding and is marginalized exactly, so that its posterior combines the two sources of evidence. Document proportions are inferred with amortized variational inference, while the Gaussian parameters are re-estimated in closed form. Experiments show that SentenceETM consistently improves sentence-level topic assignment over state-of-the-art approaches, and a case study of a presidential debate shows how sentence-level topics reveal how candidates handle the same subjects.

---


### 139. [Forecasting Voltage Time Series under Anomalies Using a WGAN Model With Lipschitz Control and Progressive Kernel Critic Strategy](https://arxiv.org/abs/2610.23394)

**<font color=#1a73e8>作者：</font>** Najmieh Sadat Safarabadi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In time-series forecasting tasks, the use of recursive forecasting on high-dimensional data substantially increases the complexity of the prediction process. The main challenge is that long-term dynamics becomes harder to model, since the sequences show greater temporal variability. To counteract this limitation and improve the modeling of long-term dynamics, and more importantly, address high-dimensional recursive forecasting, this paper uses a Wasserstein GAN equipped with a progressive Lipschitz penalty and an adaptive kernel. This model is capable of taking a window of the data stream and forecasting the next values, subsequently reconstructing the time-series stream and dynamically adapting its kernel to each new window. The proopsed model is a deep learning framework based on a Wasserstein GAN (WGAN-CLP) with an adaptive kernel to model alterations in streaming voltage time series. To establish the methodological foundation, we review the WGAN-LP formulation another variant model in this class and extend its framework through an adaptive kernel critic model. We then evaluate this extended model using power ratios, correlation coefficient (CC), and relative root mean squared error (RRMSE). The experimental results demonstrate that the proposed model outperforms benchmark methods in both accuracy and robustness. The evaluation shows promising performance of the WGAN-CLP with an adaptive kernel framework in forecasting sequence alterations across the voltage and energy time-series datasets.

---


### 140. [Contracting with an Agent under Model Mismatch](https://arxiv.org/abs/2610.23402)

**<font color=#1a73e8>作者：</font>** Elif Yılmaz, Jakub Tłuczek, Victor Villin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the classical principal-agent setting, the principal delegates some task to the agent, who receives a payment conditioned on the outcome of the task, which in turn benefits the principal. To align their objectives, the principal designs a contract that incentivizes the agent to take actions beneficial to the principal. In practice, however, the agent may act under misspecified beliefs about the underlying environment, leading to systematically suboptimal decisions. In this work, we study this problem through a principal-agent Markov Decision Process (PAMDP), in which the principal repeatedly interacts with an agent whose transition model may differ from the true environment dynamics. The principal has access to the true transition model and designs contracts that account for the agent's belief and incentives. We characterize contract design under model mismatch and develop a framework that enables the principal to induce desirable long-term benefits even though the agent has a potentially inaccurate understanding of the environment.

---


### 141. [Information Estimation with Discrete Diffusion](https://arxiv.org/abs/2610.23404)

**<font color=#1a73e8>作者：</font>** Alberto Foresti, Giulio Franzese, Pietro Michiardi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Information-theoretic measures, such as Mutual Information (MI), play a crucial role in understanding non-linear relationships between random variables and are widely used across scientific disciplines. Yet, their use on real-world discrete data remains challenging. Existing methods typically rely on embedding discrete data into a continuous space and apply neural estimators originally designed for continuous distributions. This process requires careful engineering for both the embedding model and estimator architecture, but suffers from issues related to high data dimensionality. In this work, we introduce InfoSEDD, a discrete diffusion-based approach that bridges information-theoretic estimation and generative modeling such that they can be used to compute Kullback-Leibler divergences. Backed by Continuous Time Markov Chains theory principles, the design of InfoSEDD is lightweight and scalable and allows seamless integration with pretrained models. We showcase the versatility of our approach through applications on motif discovery in genetic promoter data, semantic-aware model selection in text summarization, and entropy estimation in Ising models. Finally, we construct consistency tests on real-world textual and genomics data. Our experiments demonstrate that InfoSEDD outperforms alternatives that rely on the "embedding trick". Our results position InfoSEDD as a robust and scalable tool for information-theoretic analysis of discrete data.

---


### 142. [LithoWorld: An Endpoint World Model for Lithography Process-Window Recovery](https://arxiv.org/abs/2610.23408)

**<font color=#1a73e8>作者：</font>** Botong Zhao, Fang Yu, Xinyuan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lithography process drift can move a fabricated pattern outside its process window, producing unqualified scanning electron microscopy (SEM) morphology. We present LithoWorld, an endpoint world model for SEM-guided parameter recovery. Interior representative targets jointly determine qualified reference appearance and correction supervision. A causal predictive branch aligns currentimage features with endpoint representations, while a conditional flow policy generates a two-dimensional correction as an action chunk. The model learns from 173 groups of measured SEMs organized as focus-exposure maps, preserving unmeasured cells as unknown. On 200 test pairs from the 73-group subset, LithoWorld achieves 88.5% qualified-region success and 46.0% interior success, exceeding the strongest comparison method by 2.5 and 6.0 percentage points, respectively. Ablations separate the effects of target selection, endpoint alignment, and output parameterization. Qualitative SEM retrieval illustrates recovery to qualified interiors without requiring exact reference-coordinate matching.

---


### 143. [Flash RNN-T: Memory-Efficient Joint Network and Transducer Loss Computation](https://arxiv.org/abs/2610.23409)

**<font color=#1a73e8>作者：</font>** Mahmoud Ashraf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The recurrent neural network transducer (RNN-T) remains a practical choice for streaming speech recognition, but training requires large intermediate tensors. We present Flash RNN-T, a joint and loss implementation combining specialized kernels with optional tiled recomputation over the full alignment space and vocabulary. Tiled and untiled Flash form the entire measured throughput-memory frontier on medium and long workloads. On H100, untiled Flash achieves 24-39% higher throughput with 26-56% less memory than the fastest baseline on these workloads wherever it fits. Tiling reduces memory further through recomputation. On medium, tiled Flash uses ninefold less memory than that baseline at 16% lower throughput when both use one backward call per batch. On long, it fits where all tested alternatives with that backward schedule run out of memory with 80 GB. These comparisons use each implementation's lowest-memory configuration reaching at least 95% of its peak throughput.

---


### 144. [Can We Use Saliency Maps for the Evaluation of Generative Image Models?](https://arxiv.org/abs/2610.23411)

**<font color=#1a73e8>作者：</font>** Eleonora Ristori, Luca Bindini, Marco Lippi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating generative image models remains challenging, as commonly used metrics depend on fixed pretrained feature extractors optimized for different tasks that do not always align with human realism perception across datasets and model families. To address this limitation, we investigate a human-inspired evaluation framework that avoids representations learned for unrelated tasks. Specifically, we train a generator-specific classifier to distinguish real images from samples produced by a given model and analyze its decisions using saliency maps. Across diverse benchmarks, we observe that these classifiers learn generator-specific artifacts rather than a universal notion of "fakeness", exhibiting strong accuracy and limited cross-generator transfer. This makes saliency analysis particularly informative: the resulting attribution maps highlight visual cues and structural irregularities characteristic of each model's outputs. By combining classification accuracy and saliency information, we obtain a composite score aligned with human judgments, without relying on large pretrained backbones and using only real and generated samples from the evaluated model.

---


### 145. [Residual Stochastic Concept Bottleneck Models](https://arxiv.org/abs/2610.23421)

**<font color=#1a73e8>作者：</font>** Stephen Marcou, Mateo Espinosa Zarlenga, Sonia Laguna 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept-based models (CMs) learn human-interpretable intermediate representations that enable users to understand the model's reasoning and steer its predictions through test-time concept interventions. However, in realistic settings, their performance can be limited by concept incompleteness, where the training concepts fail to capture all task-relevant information. Adding an unconstrained residual pathway to the model's predictive process can overcome the consequences of incompleteness. However, this introduces an inscrutable, leak-prone prediction pathway that may weaken concept interventions, as these often leave residual variables unchanged. To address this limitation, we introduce Residual Stochastic Concept Bottleneck Models (Res-SCBMs), a family of concept-based models that jointly model concept and residual variables through a multivariate Gaussian distribution. Res-SCBMs learn a covariance structure that explicitly captures dependencies between the known concepts and learnt residual variables, allowing interventions to propagate to statistically dependent residual variables through Gaussian conditioning. This extends the intervention capabilities of previous CMs without requiring concept completeness during training. Our results show that, across multiple concept-incomplete benchmarks, Res-SCBMs improve predictive performance over competing baselines while retaining effective test-time concept interventions.

---


### 146. [Momentum: Persistent Dynamics for Video World Models](https://arxiv.org/abs/2610.23423)

**<font color=#1a73e8>作者：</font>** Nedko Savov, Stefan Maria Ailuro, Danda Pani Paudel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models must capture how a scene evolves beyond the current camera view to generate consistent observations when its content reappears. Existing approaches rely on observation history, static point clouds, or image caches constructed from past frames. These representations are often expensive and, more importantly, cannot update dynamic scene content outside the field of view: generated vehicles and pedestrians may be forgotten after leaving the field of view or reappear in physically inaccurate states. We represent an evolving scene through synchronized videos from reference-camera rigs, each comprising eight cameras that jointly cover the surrounding scene. We connect these rigs in a graph and propagate video generation between neighboring rigs to coordinate scene dynamics across locations and time. We introduce Momentum, a two-stage pipeline: WorldUpdate jointly generates reference-camera videos as a shared memory of scene dynamics, and WorldInteract grounds camera-controlled video generation in this evolving memory, allowing moving content to remain represented outside the target view and reappear consistently. To support training and evaluation, we develop a CARLA pipeline that captures synchronized videos from reference camera rigs and a moving target camera, together with an evaluation framework measuring consistency within the generated world state and the target this http URL on generated street scenes show that grounding target videos in scene dynamics generated by Momentum improves dynamic scene consistency by 126.2% in unseen scenes over static image conditioning, while also improving visual fidelity. Our models and source code will be made publicly available.

---


### 147. [Bridging Compressed Communication and Local Steps via Spectral Method in Federated Learning](https://arxiv.org/abs/2610.23434)

**<font color=#1a73e8>作者：</font>** Dmitriy Bystrov, George Chirkov, Daniil Medyakov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative training of complex models across large-scale networks of edge devices while keeping data localized. However, data heterogeneity and high communication overhead remain fundamental bottlenecks. Recently, the spectral optimizer Muon has demonstrated remarkable advantages over Adam-like methods in centralized training. While recent efforts have attempted to transition Muon to FL, naive integrations into traditional architectures fail short. Crucially, existing approaches do not support the the communication compression and local steps --- the two foundational techniques of efficient FL. To address this limitation, we introduce a novel spectral FL method that utilizes both local updates and compression. We establish rigorous convergence guarantees under mild assumptions, notably eliminating the restrictive bounded heterogeneity condition. Empirical evaluation on standard image classification benchmarks validates the efficiency and robustness of our approach.

---


### 148. [ShadowCast: On-the-Fly Context-Aware Shadow Augmentation for Remote Sensing Image Segmentation](https://arxiv.org/abs/2610.23440)

**<font color=#1a73e8>作者：</font>** Yechan Kim, Dongho Yoon, Jongmin Joo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shadows cast by elevated objects alter the spectral appearance and obscure the boundaries of objects in remote sensing images, thereby degrading semantic segmentation performance. Most existing approaches handle shadows as degradations to be detected and removed, requiring additional costs from dedicated networks and shadow-specific annotations. We propose ShadowCast, which takes the opposite approach: it synthesizes shadows and injects them during training for remote sensing segmentation. It extracts masks of elevated objects, such as buildings and trees, directly from the segmentation labels and estimates an image-specific cast-shadow direction cue by probing the brightness around them. It then projects synthetic shadows along the inferred cast-shadow direction, requiring no learned network and no acquisition metadata. Experiments on three widely used remote sensing benchmarks, Vaihingen, Potsdam, and LoveDA, show that ShadowCast consistently outperforms the baseline across diverse state-of-the-art segmentation architectures. Moreover, it brings additional performance gains when combined with standard augmentation and regularization techniques, indicating that stochastic shadow injection serves as a simple and complementary augmentation strategy for remote sensing segmentation.

---


### 149. [RECREG: Recovery-based Shielding for Regular Safety Properties in Reinforcement Learning](https://arxiv.org/abs/2610.23445)

**<font color=#1a73e8>作者：</font>** Alexander W. Goodall, Francesco Belardinelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many real-world scenarios we need to consider formal requirements, such as safety and constraint compliance, to deploy Reinforcement Learning (RL) agents. In this paper we introduce RecReg, a safe RL framework capable of enforcing non-Markovian regular safety properties via recovery-based shielding. RecReg is a unified approach that supports different levels of a priori knowledge and safety guarantees. The paper primarily focuses on building the theoretical foundations for RecReg in the tabular setting, providing rigorous safety and convergence guarantees that are not present in related work. We provide an extensive set of empirical results using the MASA-Safe-RL library, and we outline an extension of RecReg to deep RL domains using SOTA model-based RL. Our empirical results demonstrate that RecReg achieves efficient learning and matches the theory in this paper.

---


### 150. [Regularized free deconvolution for spectral repair of resampling distortion in high-dimensional particle filters](https://arxiv.org/abs/2610.23448)

**<font color=#1a73e8>作者：</font>** Deming Song, Chi-Kin Lam, Kefeng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Resampling is the standard remedy for weight degeneracy in particle filters, but in high dimensions it distorts the spectrum of the ensemble covariance in a way that is computable from the importance weights. This paper studies the inverse problem: recovering the pre-resampling spectrum from the observed weights and the empirical spectrum alone, and using it without biasing the filter. We first show that the forward spectral law extends to random importance weights once one conditions on the weights together with the realized offspring counts, rather than on the weights alone. We then construct a regularized free-deconvolution estimator, prove its consistency with an explicit error budget at a fixed resolution scale, and certify model mismatch through a computable forward residual. The repaired spectrum enters the filter only as the preconditioner of a Metropolis-adjusted rejuvenation move, so that spectral error affects mixing efficiency but not the invariant target. For the full filtering cycle, we derive a geometrically summable error recursion under stable scalar dynamics and an explicit law for the cost of abstaining from repair. Pre-registered simulations show that the inversion reduces the spectral error by an order of magnitude, that the corrected preconditioner recovers about 90% of the oracle's sampling efficiency in an anisotropic regime, and that the cost of abstention depends on when abstentions occur rather than on how many. The repair recovers eigenvalue laws, not eigenvectors, and is certified only within an explicitly stated exogenous-weight regime.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-213](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
