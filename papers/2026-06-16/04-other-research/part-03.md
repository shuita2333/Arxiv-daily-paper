# 📦 其他研究 | 2026年06月16日

> 本类共 **211** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-211](./part-05.md)

---

### 101. [Learning Urban Access Costs from Origin-Destination Flows via Inverse Optimal Transport](https://arxiv.org/abs/2606.14157)

**<font color=#1a73e8>作者：</font>** Paula Joy B. Martinez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cities deliver basic services through mixed public-private facility networks, including schools, clinics, transit providers, and subsidized service points. In these systems, planners often observe where households go, but not the latent cost function through which they trade off factors such as distance, price, and institutional access. We study this urban problem through school choice in the Philippines, where the country's largest national education subsidy is intended to redirect learners from congested public schools to participating private schools. Treating school-to-school enrollment flows as an entropic optimal transport plan, we recover latent choice costs using two complementary inverse optimal transport models: an interpretable distance-banded model with a subsidy term, and a neural cost model trained through a differentiable Sinkhorn forward pass. Applied to 283{,}016 learner trips across 23{,}820 observed flows in the most populated region, the framework estimates a subsidy-equivalent distance, $\lambda^{(k)}$, interpreted as the kilometers of perceived travel cost offset by the subsidy. The case demonstrates how administrative origin-destination data can be transformed into interpretable planning metrics for accessibility-aware subsidy design, facility siting, and urban service allocation.

---


### 102. [Curvature-Guided Geometric Representation for Protein-Ligand Binding Affinity Prediction](https://arxiv.org/abs/2606.14159)

**<font color=#1a73e8>作者：</font>** Shuai Li, Chuan-Xian Ren, Yuhao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein-ligand binding affinity (PLA) prediction is critical in drug discovery. Despite the notable advancements in machine learning-based approaches, existing methods struggle to jointly characterize local geometric organization and globally coordinated cross-molecular interactions, limiting their ability to model complex binding mechanisms. Here, we propose RicciBind, a geometric representation framework that integrates curvature-guided hierarchical structure learning with optimal transport (OT)-based cross-domain alignment to model molecular interactions. Specifically, RicciBind leverages Ricci curvature to capture local interaction tightness within molecular structures, enhancing structural awareness and organizing atomic interactions into curvature-aware hierarchical representations. An OT-based cluster matching mechanism then aligns protein and ligand clusters across heterogeneous domains under geometric constraints, enabling globally consistent correspondences and revealing higher-order interaction patterns beyond local neighborhoods. By coupling curvature-guided structure encoding with OT-driven cross-domain alignment, RicciBind effectively models complex interaction semantics and substantially improves both the accuracy and interpretability of binding affinity prediction. Extensive experiments demonstrate that RicciBind achieved superior predictive performance and generalization across PLA benchmarks and virtual screening tasks. Ablation studies further confirmed the essential role of Ricci curvature in enhancing molecular interaction representations.

---


### 103. [VideoWeave: Unlocking Geometric Consistency in Video Generation via Joint Geometry-Video Modeling](https://arxiv.org/abs/2606.14162)

**<font color=#1a73e8>作者：</font>** Xunzhi Xiang, Zixuan Duan, Yabo Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale video diffusion models often fail to preserve 3D structure over time, causing geometric drift and implausible motion under viewpoint changes. Existing methods usually enforce geometric consistency by using explicit geometry reconstructions, such as depth maps, point clouds, or reconstructed 3D structures, to define conditions, supervision, or reward signals, making the generator sensitive to errors from upstream geometry pipelines. We propose VideoWeave, a latent-space post-training framework that uses implicit geometry-model features to constrain the generative distribution, providing a more flexible and non-rigid form of guidance that mitigates the impact of reconstruction errors from geometry models. Specifically, VideoWeave adapts these features into geometry latents and jointly models them with video latents in a shared denoising space, allowing geometry to shape the generative distribution during training. To support this process, we build GeoVid-80K, an 80K-video dataset with paired appearance and geometry representations. Experiments on text-to-video and image-to-video generation show that VideoWeave improves geometric coherence while preserving strong visual quality. VideoWeave project page at this https URL

---


### 104. [Security Evaluation of Mobile Banking Applications in Sudan](https://arxiv.org/abs/2606.14165)

**<font color=#1a73e8>作者：</font>** Abdelmonim Naway  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid digitalization of the Sudanese financial sector has precipitated a surge in Mobile Banking Applications (MBAs); however, this growth has frequently outpaced rigorous security auditing. This study provides a comprehensive technical audit of the four most widely used Sudanese MBAs( Bankak, Fawry, Okash, and Sahil )collectively serving a user base of over 1.6 million. Utilizing Static Application Security Testing (SAST) via the Mobile Security Framework (MobSF) and Quixxi, the applications were evaluated against the OWASP Mobile Application Security Verification Standard (MASVS). Findings were mapped to Common Weakness Enumeration (CWE) identifiers to identify systemic vulnerabilities. Analysis revealed critical disparities in security posture. Bankak, the market leader, exhibited the highest risk profile (12 vulnerabilities), including a critical absence of SSL certificate pinning and unsafe TrustManager implementations, rendering it highly susceptible to Man-in-the-Middle (MitM) attacks. While Fawry demonstrated relative maturity (7 vulnerabilities), a universal failure was observed across all four applications regarding secure random number generation (CWE-330), potentially compromising session token integrity. Additionally, Bankak and Okash were found to utilize deprecated cryptographic algorithms (MD5/SHA-1). Notably, all applications successfully disabled ADB backups, yet 100% retained verbose debugging symbols in production APKs, significantly lowering the barrier for reverse engineering. This research addresses a critical gap in the national fintech ecosystem by providing actionable technical recommendations for developers and a strategic roadmap for implementing "security-by-design" principles across the sector.

---


### 105. [Machine Learning for Biomedical Raman Spectroscopy: From Spectral Acquisition to Clinical Translation](https://arxiv.org/abs/2606.14169)

**<font color=#1a73e8>作者：</font>** Bogdan Oancea, Ana Maria Seciu-Grama, Nicoleta Siminea 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Raman spectroscopy provides label-free, chemically specific characterization of biological systems and has become an important tool for cancer diagnosis, molecular subtyping, microbiological identification, and intraoperative decision support. Biomedical Raman spectra are, however, high-dimensional, noisy, and affected by fluorescence background, acquisition variability, and biological heterogeneity, making robust computational analysis essential.
This review examines the role of machine learning across the biomedical Raman spectroscopy pipeline, from preprocessing and signal correction to unsupervised structure discovery, supervised diagnosis and molecular stratification, representation and transfer learning, explainability, biomarker discovery, and multimodal integration with imaging, pathology, and molecular profiling. Emphasis is placed on the use of machine learning not only for diagnostic classification, but also for biologically interpretable and clinically actionable analysis.
We also discuss the main barriers to clinical translation, including limited dataset sizes, inter-instrument variability, inconsistent preprocessing, insufficient external validation, reproducibility concerns, and limited sharing of software, data, and metadata. We argue that progress will require methodological advances together with standardization, robust validation, explainability, and deployment-ready analytical frameworks. By integrating methodological, biomedical, and translational perspectives, this review outlines key directions for developing reliable and clinically deployable Raman-AI systems.

---


### 106. [VeriGeo: Controllable Geometry Question Generation with Numerical and Analytical Verification](https://arxiv.org/abs/2606.14176)

**<font color=#1a73e8>作者：</font>** Xiaoxian Duan, Zequn Liu, Yingce Xia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geometry problem generation is useful for AI-assisted education and multimodal mathematical reasoning, but reliable synthesis remains difficult because the problem statement, diagram, constraints, and solution should be mutually consistent. Existing methods often trade off controllability and reliability: seed-based rewriting is flexible but weakly verifiable, whereas diagram-first construction improves validity but is less suited to arbitrary user-specified constraints. We introduce VeriGeo, a controllable geometry generation framework grounded in executable reasoning traces. Given user constraints such as target concepts and difficulty, an Author agent generates a problem and diagram, and a Solver agent produces a proof-aligned solution. Both agents use a shared action sequence that connects natural language, diagrams, geometric constraints, and proof steps into a verifiable representation. A three-stage pipeline checks numerical consistency, analytical realizability, and global consistency, using verification-guided reflection to repair recoverable failures and reject unrecoverable ones. Across five LLM backbones, raw generations frequently fail these checks, while VeriGeo repairs a substantial fraction of the invalid attempts. Supervised fine-tuning on 8.7k examples generated by VeriGeo achieves the best reported GeoQA performance among end-to-end multimodal LLM-based solvers, and obtains strong results on PGPS9K and MathVista-GPS, demonstrating the effectiveness of verified synthetic data for improving multimodal geometry reasoning.

---


### 107. [Zeta: Dual Whitening for Matrix Optimization via Coordinate-Adaptive Preconditioning](https://arxiv.org/abs/2606.14187)

**<font color=#1a73e8>作者：</font>** Kaiwen Chen, Shuhai Zhang, Qiuwu Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale neural network training increasingly relies on matrix-aware optimizers that exploit the structure of weight parameters beyond element-wise adaptation. However, existing matrix-aware methods such as Muon have an underappreciated vulnerability: their core operation, Newton-Schulz iteration, depends critically on input conditioning, yet the raw momentum matrices exhibit severe coordinate-wise scale heterogeneity. In this paper, we first verify this scale heterogeneity through a chi-square uniformity test, showing that intra-matrix scale imbalance is prevalent across Transformer layers and that coordinate whitening effectively corrects it. Motivated by this finding, we propose Zeta, a dual whitening optimizer that applies coordinate whitening and spectral whitening in a strictly ordered pipeline. The ordering is not a tunable choice but follows from a mathematical dependency: coordinate whitening establishes the statistical isotropy that spectral whitening requires to function reliably. We further prove that this dual pipeline strictly reduces orthogonalization error relative to pure spectral methods by improving the condition number of the input. Empirically, Zeta matches or surpasses strong baselines across language modeling (0.6B to 8B parameters), mixture-of-experts architectures, and vision tasks, demonstrating that resolving scale imbalance before orthogonalization leads to faster convergence and better generalization. Code is available at this https URL.

---


### 108. [DRIVE: Distributional and Retrieval-Augmented Bidding with Value Evaluation](https://arxiv.org/abs/2606.14192)

**<font color=#1a73e8>作者：</font>** Miduo Cui, Haochen Wang, Shangqin Mao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auto-bidding is a core component of real-time advertising systems, where decisions must optimize long-term performance under budget and cost constraints, while online exploration is prohibitively risky. Offline reinforcement learning and, more recently, Transformer-based sequence modeling have shown promise for learning bidding policies from logged data, but their unimodal and purely parametric formulations often collapse multiple effective bidding strategies into suboptimal averaged actions and perform unreliably under sparse or long-tail traffic. To mitigate these limitations, we propose DRIVE (Distributional and Retrieval-Augmented Bidding with Value Evaluation), a unified Transformer-based framework that decouples candidate action generation from decision making for offline auto-bidding. DRIVE combines distributional action modeling, retrieval-augmented candidate generation from high-quality historical decisions, and value-based evaluation to select the most promising bid at inference time. Extensive experiments on AuctionNet and additional offline reinforcement learning benchmarks demonstrate that DRIVE consistently improves bidding performance and generalizes well across multiple Transformer-based methods.

---


### 109. [Hybrid Classical-Quantum (HCQ) Alzheimer's Classification via Supervised $β$-VAE and Quantum Kernels](https://arxiv.org/abs/2606.14194)

**<font color=#1a73e8>作者：</font>** Tia Tiwari, Vamshi Krishna Kancharla, Neelam Sinha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a two-stage Hybrid Classical-Quantum (HCQ) pipeline for binary Alzheimer's disease (AD) classification from 3D T1-weighted structural MRI volumes, where the classical and quantum components are designed to complement each other rather than operate independently. A supervised 3D $\beta$-variational autoencoder (VAE) is trained end-to-end under voxel-wise reconstruction, KL-divergence, and focal classification losses that compress each 3D MRI volume (resized from 152 x 184 x 152 to 96 x 96 x 96) into a 64-dimensional latent code. Partial Least Squares (PLS) regression selects the six components in the latent code that best separate Alzheimer's Disease (AD) from cognitively normal (CN) subjects and rescales them into rotation angles, which are encoded onto a six-qubit register using the ZZ quantum feature map to give us the respective quantum states. The input to a precomputed-kernel Support Vector Machine (SVM) is an N x N Gram matrix (N = 308), created by calculating the overlap between every pair of quantum states. The novelty of this work lies in the fact that the quantum kernel operates directly on disease-aware features that are learned end-to-end by a supervised autoencoder, rather than on pre-extracted inputs. On 308 ADNI-1 subjects, consisting of 137 AD and 171 CN subjects, the baseline achieved 67.2% accuracy and 0.759 AUC, while the stability-enhanced variant reached 72.1% accuracy and 0.799 AUC with cross-fold variance halved. 3D Grad-CAM further helped validate our model's focus on brain regions linked to Alzheimer's. The HCQ pipeline could serve as a general-purpose framework for diagnostic classification across biomedical imaging domains that present similar challenges for classical approaches.

---


### 110. [Structured Noise Adaptation for Sequential Bayesian Filtering with Embedded Latent Transfer Operators](https://arxiv.org/abs/2606.14195)

**<font color=#1a73e8>作者：</font>** Naichang Ke, Pongpisit Thanasutives, Yoshinobu Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kalman filters based on the Embedded Latent Transfer Operators (ELTO) emerge as novel statistical tools for sequential state estimation. However, a critical limitation stems from their use of simplified noise models, which fail to dynamically adapt to non-stationary processes. To address this limitation, we introduce an ELTO-based Bayesian filtering approach with a new structured parameterization for the filter's noise model. This parameterization enables structured noise adaptation, which couples the data-driven learning of an optimal time-invariant noise model with dynamic parameter adaptation that responds to changes in dynamics within non-stationary processes. Empirical results show that our structured noise adaptation improves the filter's dynamic state estimation performance in noisy, time-varying environments.

---


### 111. [When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms](https://arxiv.org/abs/2606.14200)

**<font color=#1a73e8>作者：</font>** Yihan Xia, Taotao Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open platforms increasingly route tasks among heterogeneous LLM agents--differing in base model, scaffold, and tool stack--whose competence varies sharply by skill: an agent excellent at one skill may be useless at another. The standard reputation approach summarizes each agent by a single global trust score, but that scalar is the wrong object here, because routing every task to the globally most-trusted agent leaves the value of specialization unclaimed. We study skill-conditional trust R(i | k)--the trust to place in agent i for a task requiring skill k, rather than one score per agent--and pose three falsifiable questions: when is conditioning worth it, how much cross-skill evidence should be borrowed, and whether that borrowing is safe. A controlled phase-diagram analysis answers the first two: conditional trust wins only in a specific regime--high agent heterogeneity, sparse per-skill evidence, and correlated skills--and the coupling strength beta that buys this data efficiency is dual-use, because the same cross-skill borrowing is also a laundering channel. On a public benchmark of 14 genuinely heterogeneous AppWorld agents, real pools land inside the beneficial regime--a small but genuine gain, with the per-skill best agent genuinely changing across skills. We then show that an attacker with cheap evidence in one skill and none in a target skill hijacks the conditional router, driving routing regret from 0 to 0.94 on a pool our zero-cost Conditional Information Value Test (CIVT) rates GREEN--while the ungated trust verdict it contaminates reads -0.06 instead of the honest +0.19. A zero-evidence gate bounds the attack but does not eliminate it; we characterize the residual cost under an explicit budget. We do not claim Sybil-resistance--we quantify the trade-off.

---


### 112. [Curvature-Informed Potential Energy Surface for Protein-Ligand Binding Affinity Prediction](https://arxiv.org/abs/2606.14217)

**<font color=#1a73e8>作者：</font>** Peng-Fei Sun, Chuan-Xian Ren, Hong Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of protein-ligand binding affinity is essential for structure-based drug discovery. Recent geometric deep learning methods have achieved promising performance by representing protein-ligand complexes as three-dimensional graphs. However, most existing approaches mainly rely on static interaction geometry from a single bound conformation, while neglecting molecular flexibility and binding-induced conformational changes. To address this limitation, we propose a curvature-informed potential energy surface (CPES) graph neural network for protein-ligand binding affinity prediction, which incorporates physics-informed curvature representations to model conformational flexibility. CPES first derives curvature spectral descriptors from the Hessian of the potential energy surface evaluated at equilibrium configurations, whose eigenvalues define the local principal curvatures of the potential energy surface. It then uses spectral cross-attention to compare the unbound ligand and protein with the bound complex, thereby capturing binding-induced changes in conformational dynamics. In parallel, hierarchical protein-ligand interaction representations are learned from static structural features through geometry-aware message passing, soft clustering, and bidirectional cross-attention. Finally, CPES fuses the curvature-informed dynamic representations with static interaction representations for affinity regression. Extensive evaluations on multiple benchmark datasets demonstrate that CPES achieves improved predictive performance and offers physical interpretability.

---


### 113. [A Multi-Domain Feature Fusion Framework for Generalizable Deepfake Detection Across Different Generators](https://arxiv.org/abs/2606.14230)

**<font color=#1a73e8>作者：</font>** Amna Amjid, Sana Qadir, Mehwish Fatima 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfakes are artificially generated images, audio, or videos that threaten privacy, security, and information integrity. Detecting such content is crucial for countering disinformation, as the latest models generate highly realistic content. While spatial- or frequency-based approaches achieve good detection rates on Generative Adversarial Networks (GANs)-based generated deepfakes, they often struggle with recent diffusion model-generated images. In particular, existing approaches rarely exploit complementary multi-domain representations or systematically evaluate cross-generator robustness. To address these challenges, we propose a multi-domain deepfake detection framework called SGFF-Net (Spatial-Gradient-Frequency Fusion Network) that integrates spatial, gradient, and DWT (Discrete Wavelet Transform)-based frequency representations within a dual residual learning architecture. Experimental results show that the SGFF-Net achieves 98.95\% accuracy in intra-dataset evaluation and improves performance in both cross-model (70.46\%) and cross-paradigm (69.94\%) settings. Incorporating multi-source training and data augmentation further enhances robustness, increasing accuracy from 70.46\% to 79.80\% in cross-model evaluation, from 69\% to 78\% in cross-paradigm evaluation, and from 61.50\% to 75.80\% on real-world data. Unlike single-domain detectors, the SGFF-Net learns complementary forensic cues across spatial, gradient, and wavelet-frequency domains, resulting in greater robustness under cross-generator and cross-paradigm evaluation. The results further show that combining multi-domain representations with data diversity and augmentation substantially improves generalization, providing practical insights for developing more reliable deepfake detection systems.

---


### 114. [Implicit Variational Rejection Sampling](https://arxiv.org/abs/2606.14235)

**<font color=#1a73e8>作者：</font>** Jian Xu, Shigui Li, Wei Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variational Inference (VI) is a fundamental inference technique in Bayesian machine learning for approximating complex posterior distributions. Traditional VI often relies on the mean-field factorization, which can inadequately capture true posterior complexity. Recent advancements have leveraged neural networks to model implicit distributions, offering increased flexibility. However, the practical constraints of neural network architectures still produces inaccuracies. In this paper, we propose a method called Implicit Variational Rejection Sampling (IVRS), which integrates implicit distributions with rejection sampling to improve the posterior approximation. Our method uses neural networks to construct implicit proposal distributions, and rejection sampling with a discriminator network that estimates the density ratio between the implicit proposal and the true posterior for refining the approximation. Towards this end, we introduce the Implicit Resampling Evidence Lower Bound (IR-ELBO) as a metric to characterize the resampled distribution's quality and derive a tighter variational lower bound. Experimental results demonstrate that our method outperforms traditional variational inference techniques.

---


### 115. [SkillAudit: Ground-Truth-Free Skill Evolution via Paired Trajectory Auditing](https://arxiv.org/abs/2606.14239)

**<font color=#1a73e8>作者：</font>** Haowen Gao, Haoran Chen, Can Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills are structured procedural packages that guide frozen LLM agents in specialized workflows. Skills rarely remain sufficient after deployment: edge cases, API changes, and deployment constraints become visible only through use, making skill evolution a practical necessity. Existing methods depend on privileged feedback such as held-out validation scores, hidden test outcomes, or environment rewards -- signals often unavailable when a practitioner has only a task description and workspace data. We introduce SkillAudit, a framework for evolving agent skills without ground-truth feedback. The key idea is paired trajectory auditing: at each iteration, the same task is executed with and without the candidate skill, isolating how the skill changes agent behavior without external labels. To turn behavioral differences into edit guidance, SkillAudit uses Process-Aligned Contrastive Evaluation (PACE), a cluster of evaluators that maps trajectory divergences to diagnostic signals linked to specific passages in the skill document. A structural verifier, compiled once from the task specification and then fixed, checks task constraints and rolls back harmful updates. SkillAudit routes edits through two pipelines: Refine removes noisy or irrelevant guidance from broadly useful skills, while Repair replaces passages that conflict with the task. Across 89 containerized tasks spanning 8 professional domains, SkillAudit achieves 73.9% average task reward, outperforming an agent without skills (40.9%) and the static expert skill (56.7%). These gains are obtained without accessing hidden tests, reference solutions, or external scoring functions during evolution.

---


### 116. [Where Black-box Drug-Target Interaction Prediction Models Look: Cross-Method Explainability](https://arxiv.org/abs/2606.14245)

**<font color=#1a73e8>作者：</font>** Ali Vefghi, Zahed Rahmati, Mohammad Akbari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug-target interaction (DTI) and affinity (DTA) predictors increasingly achieve strong benchmark scores, yet their internal use of sequence, fingerprint, and graph features often remains opaque. We present an interpretability audit of BridgeDPI architecture on three different datasets including Gao, Human, and this http URL. This study combines gradient-based attributions -- integrated gradients, saliency, layer-wise relevance propagation, SmoothGrad, and SmoothGrad-IG -- with feature-wise occlusion ablation and strict intersection consensus across methods to reduce single-explainer bias. We summarize sensitivity and signed effects at raw inputs, at the bridge similarity scaffold, and through the graph convolution, including edge-level sensitivities and targeted edge removals. The results show that explainability is most informative when treated as model criticism: it reveals modality dominance, padding and special-token artifacts, dataset-dependent cooperative versus suppressive effects across layers, and chemistry-consistent fragment and composition motifs where methods agree. These analyses do not substitute for structural or experimental ground truth, yet they can provide testable hypotheses for downstream validation in computational drug discovery pipelines. More broadly, applying modern XAI to contemporary DTI/DTA models is still an early pass over the rich structure implicit in trained weights and data -- yet even this first layer of scrutiny already helps researchers relate predictions to drug- and target-side representations and to prioritize external validation.

---


### 117. [HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry](https://arxiv.org/abs/2606.14249)

**<font color=#1a73e8>作者：</font>** Tingyang Chen, Shuo Lu, Kang Zhao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agent performance depends critically on the runtime harness, comprising the prompts, tools, memory, and control flow that mediate how a model observes, reasons, and acts. Yet today's harnesses remain largely hand-crafted and static: each new model or task still demands bespoke scaffolding, and the rich traces produced during execution are rarely distilled back into systematic improvement. We introduce HarnessX, a foundry for composable, adaptive, and evolvable agent harnesses. HarnessX assembles typed harness primitives via a substitution algebra, adapts them through AEGIS, a trace-driven multi-agent evolution engine grounded in an operational mirror between symbolic adaptation and reinforcement learning, and closes the harness-model loop by turning trajectories into both harness updates and model training signal. Across five benchmarks (ALFWorld, GAIA, WebShop, tau^3-Bench, and SWE-bench Verified), HarnessX yields an average gain of +14.5% (up to +44.0%), with gains largest where baselines are lowest. These results suggest that agent progress need not come from model scaling alone: composing and evolving runtime interfaces from execution feedback is an actionable and complementary lever. The complete codebase will be open-sourced in a future release.

---


### 118. [HiST: A Hierarchical Sparse Transformer for Cross-Modal Spatial Transcriptomics Modeling](https://arxiv.org/abs/2606.14251)

**<font color=#1a73e8>作者：</font>** Weiyi Wu, Xinwen Xu, Xingjian Diao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) links gene expression with tissue morphology but remains expensive and low-throughput, motivating surrogates that infer expression from routine histology. Whole-slide H&E-to-ST inference pairs a gigapixel image with gene measurements at a sparse, irregular set of locations, making multiscale modeling challenging without incurring dense-grid overhead or quadratic token mixing. We propose HiST, a hierarchical sparse transformer that treats measured locations as a lattice-indexed sparse field and builds a dyadic encoder--decoder directly on the active tissue footprint. HiST combines sparse window attention for local geometric correspondence with resolution-changing operators for rapid multiscale context integration. For a fixed window size, the dominant runtime and memory scale with the number of observed locations rather than the dense slide area. To mitigate slide-specific acquisition variation, HiST adds a bottlenecked global conditioning pathway via a \emph{slide calibration token} that summarizes slide-level context and conditions local representations. On a multi-organ benchmark spanning diverse tissues and acquisition sources, HiST improves predictive performance over recent baselines while reducing runtime and peak memory.

---


### 119. [The Linguistics Olympiads: Towards a New Corpus for Linguistics Research?](https://arxiv.org/abs/2606.14257)

**<font color=#1a73e8>作者：</font>** Vlad A. Neacsu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linguistics olympiad problems (LOPs) are a category of self-sufficient puzzles consisting of a scaled-down corpus representative of certain linguistic phenomena, from which the solver must deduce a primitive set of rules of the language and then translate a new set of elements. The linguistics olympiads (LOs) have become a worldwide phenomenon with 43 different territories taking part in the International Linguistics Olympiad (IOL) 2025. While the typology and solving strategies of LOPs have been analysed, their scientific facet and connections to academic linguistics have yet to be explored. LOPs are directly connected to many linguistic fields, e.g., linguistic typology, linguistic relativity, and linguistics fieldwork. Recently, LOPs have become a research focus as benchmarks for large language models, thus highlighting their usefulness in computational linguistics. Nevertheless, they have not yet been integrated into mainstream linguistics research. This paper attempts to open new directions of including this particular type of puzzle in academic research by offering a structured evaluation of LOPs as linguistic data sources and proposes criteria for their responsible use in academic research. Starting from a set of over 1800 LOPs, this study critically examines the potential of LOPs as a novel corpus for linguistics research by discussing their strengths and limitations as tools, as well as the areas of linguistics into which these problems could fit. This work forms the foundation for a broader initiative aimed at bridging the gap between LOs and academic linguistics, by establishing a robust theoretical framework for LOPs.

---


### 120. [Beyond a Single Explanation of the Adam--SGD Gap](https://arxiv.org/abs/2606.14259)

**<font color=#1a73e8>作者：</font>** Chenxiang Zhang, Rustem Islamov, Enea Monzio Compagnoni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior work has identified several factors that can contribute to the performance gap between Adam and SGD, spanning data aspects, architecture design, and optimization properties. Yet these explanations are often studied in isolation, leaving their relative importance unclear. In this work, we revisit these hypotheses through a controlled empirical study across vision, language, genomics, and graph tasks, spanning modern and classical architectures, and carefully designed training setups. Our results suggest that no single factor consistently explains the Adam--SGD gap. For instance, the Adam advantage can (1) persist under a uniform vocabulary distribution yet nearly disappear under a heavy-tailed one; (2) reverse in favor of SGD in softmax-attention models; and (3) become larger under soft architectural modifications, e.g., when ReLU is replaced by a GeLU nonlinearity. This suggests that the gap arises from nontrivial data and architecture interactions, rather than from a single common factor. Yet, we observe a pattern across our settings: a \emph{crossover batch size} at which the relative advantage shifts from SGD to Adam as the batch size scales. These empirical results are captured by our theoretical gap model, which predicts this batch-size-dependent crossover. Our perspective helps reconcile several existing hypotheses while offering practical insights across domains.

---


### 121. [DIFF-ERO: A Conformance-Aware Loss for Deep Learning in Process Mining](https://arxiv.org/abs/2606.14283)

**<font color=#1a73e8>作者：</font>** Johannes De Smedt, Jari Peeperkorn, Artem Polyvyanyy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has driven many recent advances in process analytics, especially for predictive and prescriptive monitoring. However, standard objectives such as cross-entropy optimize local next-step likelihoods and only implicitly capture control-flow structure. As a result, models can achieve high token-level accuracy while permitting imprecise global behaviour. We introduce DIFF-ERO, a conformance-aware loss function for deep learning models on process data. DIFF-ERO is a differentiable formulation of entropy-based stochastic conformance that incorporates control-flow information during training. Our approach constructs batch-level stochastic transition matrices with soft edge memberships, allowing structural precision and recall signals to directly inform backpropagation. The loss is model-agnostic and can be applied whenever the final representation parametrizes stochastic transitions. We instantiate DIFF-ERO in transformer encoder-decoder pipelines for next-activity prediction and use it jointly with cross-entropy to analyse its theoretical components with respect to convergence. Across benchmarks comparing other loss functions and targets, DIFF-ERO shows improved predictive performance where structure matters most while maintaining parity elsewhere. At the same time, the learned stochastic automaton converges towards the structural ground truth, indicating that the network internalizes process model structure.

---


### 122. [Hierarchical ODE: Learning Continuous-Time Physical Prototypes for Early Link Failure Detection](https://arxiv.org/abs/2606.14284)

**<font color=#1a73e8>作者：</font>** Jiaen Lv, Leran Qi, Shaowei Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series prototype learning is fundamentally challenged by observational ambiguity. Discrete architectures fail to resolve this, as they lack the capacity to decouple stochastic noise from continuous dynamics. Furthermore, rigid closed-set assumptions fail to capture unseen diversity. To address these limitations, we propose a hierarchical ordinary differential equation clustering network, which utilizes neural ordinary differential equation to model latent state evolution as a continuous integral curve. This formulation enforces temporal continuity to effectively disentangle smooth feature trends from stochastic noise, while our adaptive hierarchical mechanism autonomously determines the appropriate number of prototypes without rigid prior constraints. Validated on the early link failure detection task with irregularly sampled time series, the proposed method effectively extracts underlying physical prototypes, thereby enabling robust failure detection. Our code is available at this https URL.

---


### 123. [A Robust Point Cloud Analysis Framework Inspired By Primary Visual Cortex](https://arxiv.org/abs/2606.14292)

**<font color=#1a73e8>作者：</font>** Jisheng Dang, Dengyue Pan, Delin Deng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite significant advancements in point cloud analysis, reducing energy consumption and improving robustness remain understudied, largely due to the inherent limitations of Convolutional Neural Networks (CNNs). To address this issue, we draw inspiration from the primary visual cortex and propose a Dendritic-Connected Continuous-Coupled Neural Network (DC-CCNN), a novel Brain-Inspired Neural Network (BINN) architecture for point cloud analysis. By combining discrete and continuous encoding, our design replaces traditional Multilayer Perceptrons (MLPs) with more efficient and robust BINNs. Building upon this framework, we further propose an extended model, DC-CCNN++, to improve robustness under complex corruption conditions. Specifically, we introduce a Neuro-Inspired Robust Modulation-and-Readout Module (NRMR) to enhance feature stability and decision robustness through global-context gain modulation and dual-code evidence integration. We also design a Cortically Inspired Progressive Variability Training (CPVT) strategy, which progressively exposes the model to structured environmental variability while preserving stable clean-sample anchors during training. Experimental results show that DC-CCNN++ improves the performance of brain-inspired networks on point cloud analysis while maintaining performance comparable to state-of-the-art methods. Compared with the original DC-CCNN, it achieves stronger results on both classification and part segmentation, and exhibits enhanced robustness against sparsity, occlusion, Gaussian noise, salt-and-pepper noise, and spatial transformations. With its efficiency, robustness, and biologically grounded design, DC-CCNN++ provides a promising alternative to traditional deep learning methods for point cloud analysis. Code is available at this https URL.

---


### 124. [AgentCyberRange: Benchmarking Frontier AI Systems in Realistic Cyber Ranges](https://arxiv.org/abs/2606.14295)

**<font color=#1a73e8>作者：</font>** Fengyu Liu, Jiarun Dai, Yihe Fan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Frontier AI systems are increasingly capable of cybersecurity tasks, including codebase inspection, vulnerability detection, and exploitation. However, evaluating their offensive capabilities remains constrained by limited access to open, reproducible, multi-host cyber ranges. Existing public benchmarks capture isolated skills such as CTF solving, vulnerability reproduction, and exploit generation, but often abstract away realistic intrusion workflows: discovering exposed services, gaining a foothold, collecting internal information, and expanding compromise across hosts. This gap makes it difficult to observe emerging risks early, because frontier AI systems are rarely evaluated under realistic attack conditions.
We introduce AgentCyberRange, the first open, multi-range infrastructure for measuring autonomous cyber attack capability in realistic cyber ranges. It combines 110 vulnerabilities across 15 real web applications and 8 enterprise-like cyber ranges with 156 internal hosts, plus Cage, a toolchain for execution, orchestration, result collection, and verification. The benchmark covers two core stages: web exploitation, where agents explore exposed applications and validate vulnerabilities, and post exploitation, where agents turn an initial foothold into broader internal compromise. We evaluate six frontier AI systems under matched prompts and budgets. GPT-5.5 with Codex performs best, solving 16.1% of web exploitation tasks and 31.7% of post-exploitation tasks; with more concrete hints, these rates increase to 33.0% and 46.3%. We also observe out-of-benchmark findings, including unknown vulnerabilities in popular projects, and payload mutation that bypasses host defenses. These results show that open cyber-range evaluation is necessary for observing emerging offensive capabilities under realistic and reproducible conditions.

---


### 125. [Pix2Pix-Hybrid: Structure-Guided Conditional Synthesis of Hajj Crowd Images with Multi-Channel Conditioning and Weak Attribute Supervision](https://arxiv.org/abs/2606.14297)

**<font color=#1a73e8>作者：</font>** Amirah F. Alshammari, Bander A. Alzahrani, Nahed A. Alowidi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing accurate crowd-counting models for Hajj pilgrimage scenes remains challenging because domain-specific annotated images are scarce and data collection during large gatherings raises privacy concerns. To address these limitations, this paper proposes Pix2Pix-Hybrid (P2P-H), a hybrid conditional GAN for structure-guided Hajj crowd-image synthesis and data augmentation. P2P-H builds on Pix2Pix and employs a U-Net generator conditioned on eight input channels that jointly encode structural cues (edges and grayscale) and contextual attributes (crowd density and time of day). To capture detailed textures in dense scenes, the framework integrates two multi-scale PatchGAN discriminators operating at different resolutions. The training procedure combines adversarial, perceptual, and feature-matching objectives with adaptive data augmentation and stabilization strategies. The model was trained on 993 real Hajj frames collected from 60 publicly available video sources, with conditioning attributes derived automatically to reduce manual labeling effort. Using this framework, we constructed CrowdH, a synthetic dataset of 10,000 high-resolution Hajj crowd images. Experimental results show that P2P-H improves structure-preserving conditional synthesis quality compared with Pix2Pix and StyleGAN2-ADA baselines and shows favorable transfer to other crowd datasets. To assess downstream utility, we further constructed CrowdH-Mix-469, an annotated mixed real-synthetic dataset comprising 384 real Hajj images and 85 selected synthetic images,and evaluated five crowd-counting models under real-only and real-plus-synthetic training. The selected synthetic data reduced MAE across all five models, with the strongest gain observed for CSRNet.

---


### 126. [What Drives Test-Time Adaptation for CLIP? A Controlled Empirical Study from an Update Perspective](https://arxiv.org/abs/2606.14299)

**<font color=#1a73e8>作者：</font>** Jiazhen Huang, Xiao Chen, Zhiming Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) such as CLIP have become a standard backbone for open-vocabulary recognition, yet their zero-shot predictions remain vulnerable to distribution shifts encountered at deployment. Test-Time Adaptation (TTA) has recently been extended to CLIP as a lightweight solution, leading to a rapidly growing body of TTA4CLIP methods. However, empirical progress in this area has largely outpaced our understanding of what truly drives adaptation, where their gains originate, and under which shifts they remain reliable. In this paper, we take a step back from the pursuit of state-of-the-art accuracy and conduct a systematic controlled study of TTA4CLIP. We first organize existing methods into three unified paradigms according to what is updated at test time. We then introduce TTABC, an open-source TTA Benchmark for CLIP, which standardizes evaluation protocols and integrates more than 20 representative methods. Our controlled empirical analysis focuses on three key areas. First, we determine the driving factors in parameter-based methods, revealing that adaptation gains are primarily driven by test-time evidence and reliable proxies rather than heavy optimization. Second, we explore evidence utilization beyond heavy parameter tuning, showing that competitive and efficient performance can be achieved through cross- or current-sample evidence and lightweight prototype updates. Finally, we demonstrate that there is no silver bullet for TTA: no single adaptation paradigm is universally optimal, and the preferred paradigm depends on the nature of shift. We hope our benchmark and study provide a clearer understanding of the current TTA4CLIP landscape and establish a foundation for further research.

---


### 127. [Thinking Outside the [Chat]Box: Bridging Computer Science and Industrial Design for Cognitive-Inclusive Generative AI](https://arxiv.org/abs/2606.14306)

**<font color=#1a73e8>作者：</font>** Virginia Francisco, Daniel Guasch, Raquel Hervás  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Current Generative AI (GenAI) interfaces remain largely constrained to chatbox interaction, which can impose high cognitive demands on users and create substantial barriers for people with intellectual disabilities (ID), including prompt formulation difficulties, response overload, and limited mechanisms to assess information reliability. To explore alternative interaction models for cognitive accessibility, we conducted a cross-disciplinary co-design challenge in which two student cohorts (Computer Science and Industrial Design) developed interface concepts from the same set of functional requirements (e.g., prompt scaffolding, structured output, GUI-based refinement, transparency, and personalization). Comparing the resulting proposals reveals both convergence on foundational requirements (notably initial calibration, proactive prompting, and direct manipulation of response fragments) and complementary contributions that outline a multi-layered support system. Computer Science teams primarily produced structural scaffolding, emphasizing predictability, navigability, and trust through mechanisms such as reliability indicators, explicit sources, and context management for long conversations. Industrial Design teams emphasized experiential scaffolding, focusing on pacing, attention guidance, multimodality, and proactive agency, including step-by-step response flows, focus modes, and assistant-like integrations. We synthesize these findings into a dual-layer scaffolding framework that expands the design space for cognitively accessible GenAI interaction beyond chat-centric models and motivates future work on expert refinement, technical feasibility, and empirical validation with users with ID.

---


### 128. [Pano3D: Unified 3D Reconstruction and Panoptic Segmentation](https://arxiv.org/abs/2606.14307)

**<font color=#1a73e8>作者：</font>** Victor Barberteguy, Ahmet Iscen, Mathilde Caron 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D feedforward reconstruction neural networks have achieved remarkable success in dense reconstruction from images without any camera parameters. Yet, equipping these models with robust semantic understanding remains an open problem. Here we introduce an approach that performs 3D reconstruction and 3D panoptic segmentation in a unified framework. We build on existing 3D reconstruction models and augment them with a set-based mask decoder. The approach is jointly trained with a geometric and semantic loss, which are shown to be mutually beneficial. More precisely, the features are initialized from the geometric information and then finetuned to capture jointly geometry and semantics. We demonstrate the generality of our approach by successfully applying our framework both to online and all-to-all attention reconstruction backbones. Our method achieves state-of-the-art performance in 3D panoptic segmentation across ScanNet, ScanNet200, and ScanNet++ datasets. Ablation studies show that such joint training of a unified model equips 3D feedforward reconstruction neural networks with panoptic segmentation and yields mutually beneficial improvements.

---


### 129. [CausalMotion: Structured Physical Reasoning as Keyframe and Trajectory Guidance for Training-Free Video Generation](https://arxiv.org/abs/2606.14317)

**<font color=#1a73e8>作者：</font>** Sihan Zhuang, Xinyuan Chen, Tianfan Xue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in diffusion-based video generation have significantly improved visual quality and short-term temporal coherence. However, existing methods still struggle to produce videos with physically consistent and causally plausible dynamics, especially in scenarios involving long-horizon interactions. This limitation arises from the fact that video diffusion models primarily learn physical consistency implicitly, while vision-language models can directly model physical laws. Based on this idea, in this work, we propose \textbf{CausalMotion}, a training-free framework that injects explicit physical reasoning into video generation through structured intermediate representations. Our key idea is to decouple reasoning from generation by leveraging a vision-language model to decompose a text prompt into a sequence of causally consistent keyframes and object-centric motion trajectories. These representations are then aligned and integrated as soft constraints to guide a pretrained video diffusion model during inference. This design enables explicit modeling of object dynamics and causal transitions without requiring additional training or supervision. Extensive experiments show that our method consistently improves physical plausibility and temporal coherence, particularly in dynamics-intensive scenarios, while maintaining high perceptual video quality.

---


### 130. [Achieving Precise Text-To-Cypher Via Grounded Knowledge Graph Data Generation](https://arxiv.org/abs/2606.14325)

**<font color=#1a73e8>作者：</font>** Francesco Cazzaro, Jessica Lennon, Ariadna Quattoni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Property Graphs are rapidly being adopted as database frameworks for representing heterogeneous data sources. To enable precise access to the information contained in them we need conversational interfaces based on Text-To-Cypher (Text2Cypher) parsers. This paper presents an automatic synthetic data generation method that can be leveraged to fine-tune small LLMs for this task. We conduct experiments on all the major Text-To-Cypher benchmarks, demonstrating that with our synthetic data generation approach we can significantly increase the performance of small LLMs, allowing them to compete with much larger proprietary models. This means that in settings in which models must be locally deployed we can ensure data-sovereignty without sacrificing accuracy and without costly annotation campaigns.

---


### 131. [Riemannian Metric Matching for Scalable Geometric Modeling of Distributions](https://arxiv.org/abs/2606.14334)

**<font color=#1a73e8>作者：</font>** Jacob Bamberger, Adam Gosztolai, Pierre Vandergheynst 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional datasets often concentrate near low-dimensional structures, but estimating their geometry from samples typically relies on graphs and kernels that scale poorly with dataset size and dimension. We propose Riemannian metric matching: a denoising probabilistic framework for learning the Riemannian geometry of data using neural networks. Specifically, we learn the carré du champ operator, which, using diffusion geometry, gives us access to the Riemannian geometry toolkit for downstream machine learning and statistical tasks. Our key observation is that the carré du champ operator can be formulated as a conditional expectation over random perturbations of the data, which can be exploited for sample-wise training and constant cost, amortized inference without explicit kernel construction. Empirically, metric matching rivals or improves the accuracy of $k$-NN-based diffusion geometry estimators, while enabling amortized inference that is up to $400\times$ faster, and supports graph-free geometric analysis on high-dimensional images where nearest neighbors break down.

---


### 132. [More with LESS -- Local Scene Representations for Tactile Imaging](https://arxiv.org/abs/2606.14344)

**<font color=#1a73e8>作者：</font>** Zohar Rimon, Elisei Shafer, Tal Tepper 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tactile imaging seeks to reconstruct the internal structure of soft objects through touch sensing, with applications in medical diagnosis and robotic manipulation. Recent self-supervised learning approaches have shown promising results, but rely on global, unstructured representations and robot-controlled sensing, limiting generalization and practical use. We propose Local Encoder for Spatial Sensing (LESS), an object-centric tactile representation that exploits the local nature of touch. The tactile scene is modeled as a grid of recurrent encoders with local receptive fields, whose states are fused to reconstruct 2D or 3D images of internal structure. This compositional design enables strong generalization: models trained on single-inclusion phantoms accurately image objects with multiple inclusions and varying sizes. The local structure further supports spatial uncertainty estimation. In addition, we enable hand-held tactile imaging via external pose tracking and human-like palpation data, and extend tactile imaging to full 3D reconstruction.

---


### 133. [Squeeze-Release: Iterative Pruning with Exact Structural Minimization](https://arxiv.org/abs/2606.14346)

**<font color=#1a73e8>作者：</font>** Roman Denkin, Ida Akerholm, Prashant Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unstructured pruning produces sparse weight tensors, but the standard implementation keeps tensor shapes unchanged so the deployed model is no smaller than before pruning. We present an exact structural rewrite, which we call minimization, that converts a masked network into a smaller dense network with the same forward function up to floating-point rounding. The Squeeze-Release cycle iterates pruning and minimization with an intermediate release step that re-enables the exact-zero positions inside the compacted tensors as small calibrated noise, turning otherwise wasted capacity back into trainable parameters. Successive cycles use that capacity to find structural redundancy a single pass cannot reach. We additionally introduce CompensatedLayerNorm, a function-preserving replacement for LayerNorm that extends minimization to channel reduction across LayerNorm-equipped residual streams. Squeeze-Release compresses the deployable network to 39x smaller than the unpruned model on a fully-connected model network and 14.8x smaller on modern CNN (ConvNeXt-Tiny), at comparable accuracy. In addition we prove that the rewrite can be extended to transformer architectures.

---


### 134. [ForceForget: Reinforcement Concept Removal for Enhancing Safety in Text-to-Image Models](https://arxiv.org/abs/2606.14351)

**<font color=#1a73e8>作者：</font>** Dong Han, Yong Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the advance of generative AI, the text-to-image (T2I) model has the ability to generate various contents. However, T2I models still can generate unsafe contents. To alleviate this issue, various concept erasing methods are proposed. However, existing methods tend to excessively erase unsafe concepts and suppress benign concepts contained in harmful prompts, which can negatively affect model utility. In this paper, we focus on eliminating unsafe content while maintaining model capability in safe semantic meaning interpretation by optimizing the concept erasing reward (CER) with reinforcement learning. To avoid overly content erasure, we introduce the Safe Adapter to project partial text embedding for efficient concept regulation in cross-attention layers. Extensive experiments conducted on different datasets demonstrate the effectiveness of the proposed method in alleviating unsafe content generation while preserving the high fidelity of benign images compared with existing state-of-the-art (SOTA) concept erasing methods. In terms of robustness, our method outperforms counterparts against red-teaming tools. Moreover, we showcase the proposed approach is more effective in emerging image-to-image (I2I) scenarios compared with others. Lastly, we extend our method to erase general concepts, such as artistic styles and objects. Disclaimer: This paper includes discussions of sexually explicit content that may be offensive to certain readers. All images used in this work are synthesized or from public datasets.

---


### 135. [Can Deep Neural Networks Improve Compression of Very Large Scientific Data?](https://arxiv.org/abs/2606.14353)

**<font color=#1a73e8>作者：</font>** Muhannad Alhumaidi, Guozhong Li, Spiros Skiadopoulos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Error-bounded lossy compression is a fundamental technique for managing the rapidly growing volumes of scientific data produced by modern simulations and observational instruments. Most state-of-the-art-compressors follow a prediction-residual paradigm, where compression effectiveness depends on the quality of the predictor: more accurate predictions generate smaller residuals that are easier to compress. This observation raises a question: can modern machine learning models serve as superior predictors for scientific data compression? Answering this question directly is challenging because developing compression-specific ML predictors requires substantial resources. Instead, we leverage the climate domain where highly accurate pretrained weather forecasting foundation models already exist, making them an ideal testbed. We present a framework that integrates spatial and temporal deep learning models into a conventional error-bounded compression pipeline. The framework supports auto-regressive forecasting models and avoids error accumulation. Using ERA5 climate data as a representative large-scale scientific dataset, we evaluate three distinct ML predictors: a VAEformer-based codec (CRA5), a graph neural network forecaster (GraphCast), and a vision-transformer forecaster (Aurora), against the state-of-the-art compressor SZ3.1 under identical quantization and entropy-coding backends. Our evaluation over approximately 1.7 TB of data reveals a surprising result: although ML predictors generate more accurate predictions and can improve reconstruction quality by up to 91% while achieving up to 9.6x higher compression ratios for highly predictable variables, they do not improve overall dataset-level compression ratio. We show that prediction accuracy alone is insufficient: the spatial structure of the resulting residuals plays a decisive role in entropy coding efficiency.

---


### 136. [MUFFLe: Efficient Model Update Compression via Generalized Deduplication for Federated Learning](https://arxiv.org/abs/2606.14354)

**<font color=#1a73e8>作者：</font>** Xiaobo Zhao, Daniel E. Lucani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning is well suited to edge environments but is often limited by the uplink cost of transmitting model updates. This Work-in-Progress paper presents MUFFLe, a communication-efficient update compression scheme that integrates generalized deduplication (GD) into the FedAvg pipeline. MUFFLe deduplicates repeated patterns across the update vector, yielding a fixed-rate, variable-count compression scheme. Preliminary experiments on IID MNIST with 20 clients show that MUFFLe reaches the target accuracy of $92.93\%$ with 38~MB cumulative uplink communication, compared with 75~MB for 8-bit quantization, 86~MB for Top-$k$ sparsification, and 310~MB for uncompressed FedAvg. These results demonstrate the feasibility of applying GD to communication-efficient federated learning.

---


### 137. [Point Cloud Upsampling through Patch-based Frequency Superposition](https://arxiv.org/abs/2606.14355)

**<font color=#1a73e8>作者：</font>** Marina Ritthaler, Azhar Hussian, Vasileios Belagiannis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, neural networks have become the dominant models in most point cloud upsampling methods. Although these approaches are achieving good results, they do have drawbacks, such as a lack of interpretability and data dependency. Moreover, they have to be trained on a dataset that is similar to the test data in order to perform well. To avoid these disadvantages, we propose Point Cloud Upsampling through Patch-based Frequency Superposition (PUtPFS), an optimization-based approach that selects subsets of points and estimates the surface of this set through superpositioning spatial frequencies. Then, new points are placed on this surface. By successively selecting points in the least dense regions of the point cloud, a uniform upsampling can be reached. With this method, we surpass the current best upsampling results in the commonly considered point-to-surface distance. Furthermore, we achieve the best Chamfer and Hausdorff distance among the optimization-based approaches. As an additional advantage, our method does not need any training data and is mathematically interpretable.

---


### 138. [SemPiper: Interactive Code Synthesis for Semantic Operators in Machine Learning Pipelines](https://arxiv.org/abs/2606.14361)

**<font color=#1a73e8>作者：</font>** Olga Ovcharenko, Luciano Duarte, Sebastian Schelter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) pipelines require extensive data preparation, feature engineering, and integration across heterogeneous sources, making them tedious and error-prone to develop. While large language models (LLMs) have recently shown promise for assisting programming tasks, chat-based interfaces provide limited control over pipeline behavior and often produce code that is difficult to optimize or integrate into production systems. We demonstrate SemPipes, a novel programming model that extends ML pipelines with declarative, LLM-powered semantic data operators. SemPipes allows developers to specify high-level natural language instructions for data-centric operations, while seamlessly combining these operators with arbitrary Python code from standard data science libraries. For the semantic operators, it synthesizes specialized implementations at pipeline training time, conditioned on dataset characteristics and pipeline context, enabling the flexible yet controlled integration of LLM capabilities. We demonstrate SemPipes through SemPiper, an interactive interface that visualizes computational graphs of the pipelines, synthesized operator implementations, and optimization trajectories produced by an evolutionary search procedure. Attendees can explore three end-to-end scenarios, modify pipelines, inspect generated code, and observe how semantic operators are synthesized and iteratively optimized. The demonstration highlights how declarative semantic operators enable controllable, optimizable, and practical integration of LLMs into ML pipeline development.

---


### 139. [FLaRA: Predicting Future Latent Representations for Accident Anticipation](https://arxiv.org/abs/2606.14380)

**<font color=#1a73e8>作者：</font>** Lorenzo Caselli, Tomaso Trinci, Tommaso Bianconcini 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anticipating traffic accidents from dashcam videos is a critical challenge in intelligent transportation systems. Existing methods typically map visual context directly to a collision probability without explicitly modeling the future evolution of the driving scene. In this paper we propose FLaRA (Predicting Future Latent Representations for Accident Anticipation), a novel predictive architecture that shifts this paradigm by forecasting future latent representations for accident anticipation. Building upon the Video Joint-Embedding Predictive Architecture (V-JEPA2), our model conditions a predictor network on observed context frames to predict the forthcoming latent features of the scene. A classifier then operates on these predicted future representations rather than only on past observations. To ensure these forecasts remain grounded in realistic future dynamics, we introduce a joint training objective that simultaneously optimizes an auxiliary feature-level reconstruction loss and a cross-entropy classification loss. Extensive evaluations on the Nexar dataset, alongside cross-domain validations on the DAD, DADA-2000, and DoTA benchmarks, demonstrate that our approach achieves state-of-the-art performance while maintaining realistic early warning capabilities.

---


### 140. [Discovery under Hypothesis Redundancy: A Geometric Theory of Discovery Bottlenecks](https://arxiv.org/abs/2606.14386)

**<font color=#1a73e8>作者：</font>** Li Xia, Baoxun Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific discovery saturates when new hypotheses cease to provide independent information, even if the nominal hypothesis space remains large. We study hybrid discovery systems that combine structured local search with LLM-generated non-local proposals and pose the Search Compression Hypothesis: non-local exploration helps only when three geometric conditions co-occur: spectral compression, orthogonal escape from the explored span, and residual signal alignment with the target. We formalize these conditions, derive necessary conditions for hybrid advantage, and test the mechanism in controlled synthetic environments, large-scale A-share factor discovery, and symbolic-regression benchmarks; a public tabular operational sanity check tests the associated budget-allocation implication. Signal-planting and directed-versus-random experiments show that novelty alone is insufficient: random orthogonal jumps expand coverage but do not improve yield without predictive alignment. Across compression sweeps, real factor archives, and LLM-SRBench tasks, hybrid gains concentrate in weakly represented but target-bearing directions and vanish as the hypothesis space approaches full rank. The framework turns LLM-guided discovery from generic novelty search into a diagnostic procedure for deciding when directed non-local exploration is warranted.

---


### 141. [MooMIns -- Monocular 3D Reconstruction and Object Pose Estimation from Multiple Instances](https://arxiv.org/abs/2606.14389)

**<font color=#1a73e8>作者：</font>** Robert Langendörfer, Markus Hillemann, Markus Ulrich  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Simultaneous 3D reconstruction and 6D object pose estimation from a single monocular image is an inherently ill-posed problem. In industrial settings, however, multiple instances of an object are often randomly arranged in bins, implicitly providing several views of the same object within a single image. We show that this implicit multi-view geometry can be exploited to simultaneously reconstruct the object in 3D and estimate the 6D pose of each visible object instance. We present MooMIns, a new Gaussian-splatting-based approach that inverts the original Gaussian splatting formulation: instead of rendering a single scene from multiple cameras, we render multiple object instances from a single camera. Our method is initialized with SAM3 instance segmentation masks and a modified Structure from Motion (SfM) pipeline. In contrast to learned monocular depth estimation, we perform true geometry-based reconstruction from image evidence, avoiding hallucinations caused by training data priors. We evaluate MooMIns on synthetic and real bin-picking scenarios, and demonstrate accurate reconstruction of previously unseen objects as well as reliable pose estimation of individual instance

---


### 142. [Learning to Hear Hesitation: Continual Learning for Disfluency-Aware ASR](https://arxiv.org/abs/2606.14391)

**<font color=#1a73e8>作者：</font>** Henri-Leon Kordt, Theresa Pekarek Rosin, Jae Hee Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite advances in large-scale Automatic Speech Recognition (ASR), disfluent speech remains challenging, as state-of-the-art systems are often optimized to omit disfluencies, leading to information loss and hallucinations. Prior work has focused on verbatim transcription and the integration of disfluency markers, but adapting models on limited datasets can lead to catastrophic forgetting of general-domain knowledge. We address this gap by leveraging continual learning (CL) with explicit disfluency tokens. We first introduce these tokens into a pretrained ASR model to establish stable token mechanisms, and then continue training on additional datasets with varying disfluency distributions. Through a detailed analysis of model dynamics during training, we identify a trade-off between marker learning and ASR performance, and a consistent cross-attention head mechanism shared across CL methods.

---


### 143. [REPOSE: Quantifying the Price of Security in Weakly-Hard Real-Time Cyber-Physical Systems](https://arxiv.org/abs/2606.14395)

**<font color=#1a73e8>作者：</font>** Vijay Banerjee, Monowar Hasan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In contemporary IoT edge devices with real-time requirements, security is primarily enforced through design-time parameters associated with security tasks, leading to mechanisms that operate in an \emph{opportunistic} manner. As a result, security checks are often performed as secondary operations. This approach can result in systems where no security tasks are executed due to high utilization by other tasks. An alternative approach taken in prior work is to add security mechanisms to every task in the system, resulting in substantially lower performance than that of a system with no security. These approaches have resulted in an \emph{all-or-nothing} scenario for edge device security, motivating numerous studies on the safety-security trade-off in real-time cyber-physical systems (RT-CPS). This study introduces an analytical framework -- REPOSE -- for evaluating the security feasibility of real-time control systems at runtime. REPOSE is developed for \textit{weakly-hard} real-time control systems that facilitate a ``bounded trade-off'' between safety and security. In contrast to imposing additional (pessimistic) design-time overhead as considered in some real-time security literature, REPOSE performs security operations in both \textit{proactive} and \textit{reactive} manners based on the task's current behavior. Our evaluations show that REPOSE can effectively add security operations to RT-CPS with a feasibility overhead of $0.06\%$ at $80\%$ utilization, compared to a $ 29\%$ overhead observed in systems with hard constraints. Through a case study of a classic control system, we also demonstrate that REPOSE provides a robust framework to \textit{analyze and calculate} the safety-security tradeoff.

---


### 144. [Running the Gauntlet: Re-evaluating the Capabilities of Agents Beyond Familiar Environments](https://arxiv.org/abs/2606.14397)

**<font color=#1a73e8>作者：</font>** Mykola Vysotskyi, Runqi Lin, Grzegorz Biziel 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As agentic systems continue to evolve and are widely deployed in real-world scenarios, there is a growing demand to faithfully evaluate their capabilities. However, current benchmarks are typically built on popular applications with relatively simple tasks and focus on a narrow set of capabilities while overlooking broader dimensions, resulting in saturated performance on modern agents and failing to probe their limitations. To this end, we introduce GauntletBench, a web-based benchmark for evaluating agent generalisation in challenging scenarios, focusing on three underexplored capabilities (temporal perception, graphical understanding, and 3D reasoning), across five less-covered professional applications (Video Editor, Workflow Builder, 3D Modeller, Flight Analyser, and Circuit Designer), each with 20 vision-intensive tasks (100 in total). Our benchmark provides a modular pipeline that comprises an environment compatible with both open- and closed-source agent frameworks, a controlled web-based application, a well-structured task suite, and an automated evaluation engine with diverse metrics. Contrary to widespread expectations, our empirical results reveal that frontier agentic systems remain far from achieving human-level performance. Even the state-of-the-art agent achieves only a 19.1% success rate on our GauntletBench, highlighting the limitations in these overlooked capabilities and generalisation. By comparison, non-expert human annotators achieve over 80% success on our challenging yet feasible tasks, revealing the substantial gap between current agent capabilities and those required for complex real-world scenarios.

---


### 145. [A theoretical model for task routing in mixture-of-expert transformers](https://arxiv.org/abs/2606.14398)

**<font color=#1a73e8>作者：</font>** Yongli Xiang, Vinoth Nandakumar, Yunzhi Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) layers enable the scaling of transformer models while keeping the inference compute fixed. While task-expert specialization has been observed in empirical studies of frontier MoE transformer models, existing theoretical work analyzes this using continuous mixture models that cannot be used to model natural language effectively. An important open question is to \textit{theoretically explain task-expert specialization in transformer MoE models using discrete models of language}. To address this, we represent structured knowledge via syntactic templates and finite key-value dictionaries, and prove formally that a single-layer MoE transformer can encode knowledge by using experts that specialize in the corresponding tasks. Our construction shows how queries are routed to unique, task-specific experts whose size depends solely on the intrinsic complexity of the given task (i.e. the combined size of its syntactic templates and factual dictionary). Our construction provides a theoretical support for empirical results on localized knowledge circuits in MoE models. We support our theoretical findings with experiments evaluating model performance under varying MoE loss functions.

---


### 146. [Friction in AI-Assisted Clinical Decision-Making: A Case Study on The Role of Questions and 'What-if' Scenarios](https://arxiv.org/abs/2606.14406)

**<font color=#1a73e8>作者：</font>** Simon WS Fischer, Hanna Schraffenberger, Miranda L. van Hooff 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Clinical decision-making is augmented by decision-support systems (DSSs). To counter overreliance on DSSs, several methods have been proposed that create friction in order to promote cognitive engagement and reflection. In this paper, we investigate how two such forms of friction, namely data-driven questions and `what-if' analysis, are perceived by medical experts. For a real-world decision task, we replicated a DSS used in clinical practice and gathered clinicians' feedback on a prototype through in-situ interviews (n=7). Our findings suggest that while the questions were perceived as unhelpful for reflective thinking, they could serve as reminders to consider relevant information. Furthermore, inspecting `what-if' hypotheticals was found useful for potentially improving patient care. Clinicians saw our prototype as a promising training tool for novice clinicians. From the clinicians' feedback, we make recommendations for designing friction in work practices. Our work contributes to human-AI interaction research, which aims to encourage reflection to mitigate AI overreliance.

---


### 147. [Fabula: Building a Narrative Storytelling Sidekick with the Writers' Community](https://arxiv.org/abs/2606.14411)

**<font color=#1a73e8>作者：</font>** Piotr Mirowski, Ben Wedin, Reinald Kim Amplayo 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We design and evaluate Fabula, an interactive app for fiction writers. Fabula uses detailed narrative plans informed by general narratological theory. Stories are structured hierarchically into scenes and beats that can be (re)generated and revised at script and story plan level. Using participatory AI, we critically evaluate and improve Fabula with casual and published writers, via design interviews and writing sessions with 42 experts, and large-scale internal and external testing. We interrogate our design choices: (1) whether a language model-based auto-evaluator, optimized on human experts' preferences, can improve story quality, (2) whether users want UI that exposes the detailed narrative plan alongside the story script, (3) to what extent our narratology assumptions fit localised storytelling traditions and serve screenwriters or playwrights, and (4) whether convergent iteration over the story plan supports writers' creativity. Building on critical feedback and concerns, we use Fabula as a cultural probe in adversarial design, and identify potentials for writing feedback and for interactive storytelling.

---


### 148. [CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning](https://arxiv.org/abs/2606.14415)

**<font color=#1a73e8>作者：</font>** Ayoub Belouadah, Sylvain Kubler, Yves Le Traon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safe reinforcement learning (Safe RL) aims to maximize expected return while satisfying safety constraints, typically modeled as Constrained Markov Decision Processes (CMDPs). While primal-dual methods scale well to deep RL, they often suffer from delayed constraint correction, leading to oscillatory behavior and prolonged safety violations. In this paper, we propose Constraint-Sensitive Policy Optimization (CSPO), a first-order primal-dual method that incorporates local constraint sensitivity into policy updates. CSPO augments the primal objective with a constraint-sensitive correction derived from the shortest signed distance to the safety boundary, enabling smarter recovery steps back to safety, compensating for delayed Lagrange multiplier updates, reducing oscillations near the boundary, and preserving the KKT solutions of the original constrained problem. Experiments on navigation and locomotion benchmarks demonstrate that CSPO achieves faster safety recovery and high reward preservation, resulting in higher constrained returns compared to state-of-the-art primal-dual and penalty-based methods

---


### 149. [Federated Learning for Feature Generalization with Convex Constraints](https://arxiv.org/abs/2606.14416)

**<font color=#1a73e8>作者：</font>** Dongwon Kim, Donghee Kim, Sung Kuk Shyn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) often struggles with generalization due to heterogeneous client data. Local models are prone to overfitting their local data distributions, and even transferable features can be distorted during aggregation. To address these challenges, we propose FedCONST, an approach that adaptively modulates update magnitudes based on the parameter strength of the global model. This prevents over-emphasizing well-learned parameters while reinforcing underdeveloped ones. Specifically, FedCONST employs linear convex constraints to ensure training stability and preserve locally learned generalization capabilities during aggregation. A Gradient Signal to Noise Ratio (GSNR) analysis further validates the effectiveness of FedCONST in enhancing feature transferability and robustness. As a result, FedCONST effectively aligns local and global objectives, mitigating overfitting and promoting stronger generalization across diverse FL environments, achieving state-of-the-art performance.

---


### 150. [Causal Object-Centric Models for Planning with Monte Carlo Tree Search](https://arxiv.org/abs/2606.14418)

**<font color=#1a73e8>作者：</font>** Rodion Vakhitov, Leonid Ugadiarov, Alexey Skrynnik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce COMET (Causal Object-centric Model for Efficient Tree search), a model-based reinforcement learning algorithm that performs Monte Carlo Tree Search in a slot-structured latent space. COMET pairs a frozen unsupervised object-centric encoder with a transformer-based world model, in which actions are bound to objects through a novel action-slot fusion mechanism that is used in slot transition prediction. Policy and value heads use object-causal attention, modulating token interactions by learned per-slot relevance scores so that decision-making concentrates on task-relevant entities. COMET adds an explicit object-level inductive bias to MuZero-style latent planning. Across eight visually and dynamically diverse tasks from the Object-Centric Visual RL benchmark, ManiSkill, Robosuite, and VizDoom, COMET achieves a higher mean normalized score during the early stages of training compared to object-centric and monolithic baselines.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-211](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
