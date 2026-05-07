# 📦 其他研究 | 2026年05月08日

> 本类共 **270** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-270](./part-06.md)

---

### 101. [StableI2I: Spotting Unintended Changes in Image-to-Image Transition](https://arxiv.org/abs/2605.04453)

**<font color=#1a73e8>作者：</font>** Jiayang Li, Shuo Cao, Xiaohui Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In most real-world image-to-image (I2I) scenarios, existing evaluations primarily focus on instruction following and the perceptual quality or aesthetics of the generated images. However, they largely fail to assess whether the output image preserves the semantic correspondence and spatial structure of the input image. To address this limitation, we propose StableI2I, a unified and dynamic evaluation framework that explicitly measures content fidelity and pre--post consistency across a wide range of I2I tasks without requiring reference images, including image editing and image restoration. In addition, we construct StableI2I-Bench, a benchmark designed to systematically evaluate the accuracy of MLLMs on such fidelity and consistency assessment tasks. Extensive experimental results demonstrate that StableI2I provides accurate, fine-grained, and interpretable evaluations of content fidelity and consistency, with strong correlations to human subjective judgments. Our framework serves as a practical and reliable evaluation tool for diagnosing content consistency and benchmarking model performance in real-world I2I systems.

---


### 102. [DoGMaTiQ: Automated Generation of Question-and-Answer Nuggets for Report Evaluation](https://arxiv.org/abs/2605.04458)

**<font color=#1a73e8>作者：</font>** Bryan Li, William Walden, Yu Hou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluation of long-form, citation-backed reports has lately received significant attention due to the wide-scale adoption of retrieval-augmented generation (RAG) systems. Core to many evaluation frameworks is the use of atomic facts, or nuggets, to assess a report's coverage of query-relevant information attested in the underlying collection. While nuggets have traditionally been represented as short statements, recent work has used question-answer (QA) representations, enabling fine-grained evaluations that decouple the information need (i.e. the question) from the potentially diverse content that satisfies it (i.e. its answers).
A persistent challenge for nugget-based evaluation is the need to manually curate sets of nuggets for each topic in a test collection -- a laborious process that scales poorly to novel information needs. This challenge is acute in cross-lingual settings, where information is found in multilingual source documents. Accordingly, we introduce DoGMaTiQ, a pipeline for generating high-quality QA-based nugget sets in three stages: (1) document-grounded nugget generation, (2) paraphrase clustering, and (3) nugget subselection based on principled quality criteria. We integrate DoGMaTiQ nuggets with AutoArgue -- a recent nugget-based evaluation framework -- to enable fully automatic evaluation of generated reports. We conduct extensive experiments on two cross-lingual TREC shared tasks, NeuCLIR and RAGTIME, showing strong rank correlations with both human-in-the-loop and fully manual judgments. Finally, detailed analysis of our pipeline reveals that a strong LLM nugget generator is key, and that the system rankings induced by DoGMaTiQ are robust to outlier systems. We facilitate future research in report evaluation by publicly releasing our code and artifacts at this https URL.

---


### 103. [Discovering Sparse Counterfactual Factors via Latent Adjustment for Survey-based Community Intervention](https://arxiv.org/abs/2605.04460)

**<font color=#1a73e8>作者：</font>** Fatima Ashraf, Muhammad Ayub Sabir, Junbiao Pang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transportation surveys are widely used to understand travel preferences and adoption barriers, yet most survey-based analyses remain descriptive or predictive and rarely provide sparse, policy-feasible intervention strategies. We study sparse counterfactual community intervention from survey responses, where the goal is to shift a target respondent group toward a desired reference group through controllable survey-variable adjustments. We formulate this task as a policy-feasible distributional alignment problem using a fixed-basis nonnegative latent representation that preserves pre/post comparability and provides a stable map from latent factors to original variables. To make latent movement actionable, target-relevant latent factors are identified through Shapley-guided attribution and transferred to controllable variables as intervention priorities. Feasible group-level adjustments are then learned by minimizing an entropy-regularized optimal-transport discrepancy between the post-intervention target distribution and the reference distribution, together with a weighted $\ell_{2,1}$ penalty that promotes shared policy-lever sparsity. Experiments on real-world transportation survey datasets show that the proposed framework produces compact and interpretable policy-feasible interventions with explicit adjustment magnitudes, improves population-level conversion, and preserves intervention sparsity. Code and datasets are publicly available at: this https URL

---


### 104. [Stream-T1: Test-Time Scaling for Streaming Video Generation](https://arxiv.org/abs/2605.04461)

**<font color=#1a73e8>作者：</font>** Yijing Tu, Shaojin Wu, Mengqi Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Test-Time Scaling (TTS) offers a promising direction to enhance video generation without the surging costs of training, current test-time video generation methods based on diffusion models suffer from exorbitant candidate exploration costs and lack temporal guidance. To address these structural bottlenecks, we propose shifting the focus to streaming video generation. We identify that its chunk-level synthesis and few denoising steps are intrinsically suited for TTS, significantly lowering computational overhead while enabling fine-grained temporal control. Driven by this insight, we introduced Stream-T1, a pioneering comprehensive TTS framework exclusively tailored for streaming video generation. Specifically, Stream-T1 is composed of three units: (1) Stream -Scaled Noise Propagation, which actively refines the initial latent noise of the generating chunk using historically proven, high-quality previous chunk noise, effectively establishes temporal dependency and utilizing the historical Gaussian prior to guide the current generation; (2) Stream -Scaled Reward Pruning, which comprehensively evaluates generated candidates to strike an optimal balance between local spatial aesthetics and global temporal coherence by integrating immediate short-term assessments with sliding-window-based long-term evaluations; (3) Stream-Scaled Memory Sinking, which dynamically routes the context evicted from KV-cache into distinct updating pathways guided by the reward feedback, ensuring that previously generated visual information effectively anchors and guides the subsequent video stream. Evaluated on both 5s and 30s comprehensive video benchmarks, Stream-T1 demonstrates profound superiority, significantly improving temporal consistency, motion smoothness, and frame-level visual quality.

---


### 105. [Order Flow Exclusivity and Value Extraction Mechanisms: An Analysis of Ethereum Builder Centralization](https://arxiv.org/abs/2605.04471)

**<font color=#1a73e8>作者：</font>** Ao Zhang, Yunwen Liu, Ren Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This study investigates the rapid centralization of the Ethereum builder market under the Proposer-Builder Separation (PBS) architecture. We argue that existing research, by focusing predominantly on influential order flows, lacks a comprehensive evaluation of order flow behavioral patterns and economic purposes. To address this gap, we analyze Ethereum transactions from September 2023 to August 2025 to characterize Exclusive Order Flows (EOFs) and non-atomic Maximal Extractable Value (MEV) -- the missing components corresponding to these behavioral and economic dimensions, respectively. We introduce a novel exclusivity metric based on Kullback-Leibler divergence and employ supervised learning to identify 75 EOFs and 322 non-atomic MEV flows, which account for 71\% and 23\% of trading-related builder revenue. A longitudinal analysis of builder strategies across these dimensions delineates the market's evolution into four distinct eras, revealing that while EOFs were instrumental in establishing early dominance, incumbents have since decoupled market share from immediate EOF dependency by leveraging entrenched network effects. Ultimately, we conclude that builder centralization is an emergent property of the PBS framework itself, as the architecture systematically violates the fundamental prerequisites of a competitive market.

---


### 106. [Geometry-Aware Neural Optimizer for Shape Optimization and Inversion](https://arxiv.org/abs/2605.04474)

**<font color=#1a73e8>作者：</font>** Guoze Sun, Tianya Miao, Haoyang Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geometry is central to PDE-governed systems, motivating shape optimization and inversion. Classical pipelines conduct costly forward simulation with geometry processing, requiring substantial expert effort. Neural surrogates accelerate forward analysis but do not close the loop because gradients from objectives to geometry are often unavailable. Existing differentiable methods either rely on restrictive parameterizations or unstable latent optimization driven by scalar objectives, limiting interpretability and part-wise control. To address these challenges, we propose Geometry-Aware Neural Optimizer (GANO), an end-to-end differentiable framework that unifies geometry representation, field-level prediction, and automated optimization/inversion in a single latent-space loop. GANO encodes shapes with an auto-decoder and stabilizes latent updates via a denoising mechanism, and a geometry-injected surrogate provides a reliable gradient pathway for geometry updates. Moreover, GANO supports part-wise control through null-space projection and uses remeshing-free projection to accelerate geometry processing. We further prove that denoising induces an implicit Jacobian regularization that reduces decoder sensitivity, yielding controlled deformations. Experiments on three benchmarks spanning 2D Helmholtz, 2D airfoil, and 3D vehicles show state-of-the-art accuracy and stable, controllable updates, achieving up to +55.9% lift-to-drag improvement for airfoils and ~7% drag reduction for vehicles.

---


### 107. [Information Coordination as a Bridge: A Neuro-Symbolic Architecture for Reliable Autonomous Driving Scene Understanding](https://arxiv.org/abs/2605.04475)

**<font color=#1a73e8>作者：</font>** Shuo Liu, Lei Shi, Haowen Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable autonomous driving requires scene understanding that is semantically consistent across heterogeneous sensors and verifiable at the reasoning stage. However, many recent LLM-driven driving systems attach the language model as a post-processor and force it to reason over redundant or conflicting perception outputs, which can amplify hallucinated entities and unsafe conclusions. This paper proposes InfoCoordiBridge, a BEV-centric neuro-symbolic architecture that inserts an explicit coordination bridge between perception and language reasoning. InfoCoordiBridge comprises (i) a unified multi-agent perception layer that outputs typed structured facts together with modality-focused synopses, (ii) an ICA module that aligns and fuses multi-source outputs into a single SceneSummary, and (iii) an SSRE module that performs SceneSummary-grounded reasoning with verification. Experiments on nuScenes and Waymo show that ICA preserves competitive 3D detection accuracy while substantially improving fusion consistency, reducing redundancy to below 1% and achieving about 98% attribute agreement. On NuScenes-QA and a template-aligned Waymo-QA benchmark, SSRE improves factual grounding and reduces hallucinated entity mentions compared with representative VLM and agentic baselines. Overall, by coordinating multi-sensor outputs into a single conflict-aware SceneSummary before prompting, InfoCoordiBridge prevents redundant and cross-modally inconsistent perception evidence from propagating into high-level reasoning.

---


### 108. [Quadrature-TreeSHAP: Depth-Independent TreeSHAP and Shapley Interactions](https://arxiv.org/abs/2605.04497)

**<font color=#1a73e8>作者：</font>** Ron Wettenstein, Rory Mitchell, Peng Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shapley values are a standard tool for explaining predictions of tree ensembles, with Path-Dependent SHAP being the most widely used variant. Despite substantial progress, existing methods still exhibit trade-offs between depth-dependent runtime, numerical stability, and support for higher-order interactions. To address these challenges, we introduce Quadrature-TreeSHAP, a quadrature-based reformulation of Path-Dependent TreeSHAP that is numerically stable, naturally extends to any-order Shapley interaction values and is practically insensitive to tree depth. Our implementation supports both CPU and GPU and is integrated into XGBoost.
Our method is based on a weighted-Banzhaf interaction polynomial, which expresses Banzhaf interaction values as expectations under a feature participation probability $p$. Shapley values and any-order interaction values are then recovered by integrating these polynomials over $p$ from 0 to 1. We evaluate these integrals using Gauss-Legendre quadrature, and show that, in practice, only 8 fixed quadrature points are sufficient to reach machine precision. In fact, Quadrature-TreeSHAP with 8 fixed points achieves greater numerical stability than TreeSHAP. This fixed-point formulation removes depth dependence from the inner computation and enables efficient SIMD execution.
We confirm these advantages empirically. On 12 XGBoost benchmarks, Quadrature-TreeSHAP computes Shapley values 1.06x-10.59x faster than TreeSHAP on CPU and 1.84x-6.95x faster than GPUTreeSHAP on GPU. Shapley pairwise interactions are 3.80x-58.11x faster on CPU, with higher-order interactions achieving speedups of up to 1200x compared to TreeSHAP-IQ.

---


### 109. [Harnessing Linguistic Dissimilarity for Language Generalization on Unseen Low-Resource Varieties](https://arxiv.org/abs/2605.04500)

**<font color=#1a73e8>作者：</font>** Jinju Kim, Haeji Jung, Youjeong Roh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-resource language varieties used by specific groups remain neglected in the development of Multilingual Language Models. A great deal of cross-lingual research focuses on inter-lingual language transfer which strives to align allied varieties and minimize differences between them. However, for low-resource varieties, linguistic dissimilarity is also an important cue allowing generalization to unseen varieties. Unlike prior approaches, we propose a two-stage Language Generalization framework that focuses on capturing variety-specific cues while also exploiting rich overlap offered by high-resource source variety. First, we propose TOPPing, a source-selection method specifically designed for low-resource varieties. Second, we suggest a lightweight VACAI-Bowl architecture that learns variety-specific attributes with one branch while a parallel branch captures variety-invariant attributes using adversarial training. We evaluate our framework on structural prediction tasks, which are among the few tasks available, as proxy for performance on other downstream tasks. Using VACAI-Bowl with TOPPing yields an average 54.62% improvement in the dependency parsing task, which serves as a proxy for performance on other downstream tasks across 10 low-resource varieties.

---


### 110. [Example-Based Object Detection](https://arxiv.org/abs/2605.04501)

**<font color=#1a73e8>作者：</font>** ZhiXin Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, object detection has achieved significant progress, especially in the field of open-vocabulary object detection. Unlike traditional methods that rely on predefined categories, open-vocabulary approaches can detect arbitrary objects based on human-provided prompts. With the advancement of prompt-based detection techniques, models such as SAM3 can even outperform some category-specific detectors trained on particular datasets without requiring additional training on those datasets. However, despite these advancements, false positives and false negatives still occur. In practical engineering applications, persistent misdetections or missed detections of the same object are unacceptable. Yet retraining the model every time such errors occur incurs substantial costs in terms of human effort, computational resources, and time. Therefore, how to leverage existing false positive and false negative samples to prevent such errors from recurring remains a highly challenging and urgent problem. To address this issue, we propose EBOD (Example-Based Object Detection), which integrates a prompt-based detector (SAM3) with robust feature matching modules (DINOv3 and LightGlue). The proposed framework effectively suppresses the repeated occurrence of false positives and false negatives by leveraging previous error examples, without requiring additional model retraining. Code is available at this https URL.

---


### 111. [Gradient Scaling Effects in Adaptive Spectral PINNs for Stiff Nonlinear ODEs](https://arxiv.org/abs/2605.04502)

**<font color=#1a73e8>作者：</font>** Isabela M. Yepes, Pavlos Protopapas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) often struggle to train reliably on stiff and oscillatory dynamical systems due to poor optimization conditioning. While prior work has emphasized representational remedies such as spectral parameterizations, the optimization implications of initial-condition (IC) embeddings in adaptive spectral PINNs have not been well characterized. In this work, we show that the choice of IC gating function induces explicit time-dependent gradient scaling, which interacts with spectral representations during training. Using a nonlinear stiff spring-pendulum ODE as a controlled benchmark, we compare exponential and linear IC gates in combination with fixed and adaptive Fourier spectral trunks. We observe stiffness-dependent changes in relative dominance for adaptive PINNs: at moderate stiffness ($k=20$), exponential gating often yields lower error but exhibits heterogeneous behavior across random seeds, whereas at higher stiffness ($k=60$), linear gating becomes preferable, with additional reversals observed at larger $k$. These trends hold for both relative $L^2$ error and maximum pointwise error and are confirmed by paired Wilcoxon signed-rank tests with Holm correction. Overall, our results demonstrate that IC embeddings are not a neutral design choice in PINNs: the induced gradient scaling materially shapes optimization conditioning in stiff regimes, with distinct sensitivity patterns in baseline and adaptive spectral models.

---


### 112. [SpecPL: Disentangling Spectral Granularity for Prompt Learning](https://arxiv.org/abs/2605.04504)

**<font color=#1a73e8>作者：</font>** Jingtao Zhou, Xirui Kang, Feiyang Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing prompt learning for VLMs exhibits a modality asymmetry, predominantly optimizing text tokens while still relying on frozen visual encoder as holistic extractor and neglecting the spectral granularity essential for fine-grained discrimination. To bridge this, we introduce Disentangling Spectral Granularity for Prompt Learning (SpecPL), which approaches prompt learning from a novel spectral perspective via Counterfactual Granule Supervision. Specifically, we leverage a frozen VAE to decompose visual signals into semantic low-frequency bands and granular high-frequency details. A frozen Visual Semantic Bank anchors text representations to universal low-frequency invariants, mitigating overfitting. Crucially, fine-grained discrimination is driven by counterfactual granule training: by permuting high-frequency signals, we compel the model to explicitly distinguish visual granularity from semantic invariance. Uniquely, SpecPL serves as a universal plug-and-play booster, revitalizing text-oriented baselines like CoOp and MaPLe via visual-side guidance. Experiments on 11 benchmarks demonstrate competitive state-of-the-art performance, achieving a new performance ceiling of 81.51\% harmonic-mean accuracy. These results validate that spectral disentanglement with counterfactual supervision effectively bridges the gap in the stability-generalization trade-off. Code is released at this https URL.

---


### 113. [Ilov3Splat: Instance-Level Open-Vocabulary 3D Scene Understanding in Gaussian Splatting](https://arxiv.org/abs/2605.04506)

**<font color=#1a73e8>作者：</font>** Binh Long Nguyen, Kien Nguyen, Sridha Sridharan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Ilov3Splat, a novel framework for instance-level open-vocabulary 3D scene understanding built on 3D Gaussian Splatting (3D-GS). Most prior work depends on 2D rendering-based matching or point-level semantic association, which undermines cross-view consistency, lacks coherent instance-level reasoning, and limits precision in downstream 3D tasks. To address these limitations, our method jointly optimizes scene geometry and semantic representations by augmenting Gaussian splats with view-consistent feature fields. Specifically, we leverage multi-resolution hash embedding to efficiently encode language-aligned CLIP features, enabling dense and coherent language grounding in 3D space. We further train an instance feature field using contrastive loss over SAM masks, supporting fine-grained object distinction across views. At inference time, CLIP-encoded queries are matched against the learned features, followed by two-stage 3D clustering to retrieve relevant Gaussian groups. This enables our framework to identify arbitrary objects in 3D scenes based on natural language descriptions, without requiring category supervision or manual annotations. Experiments on standard benchmarks demonstrate that Ilov3Splat outperforms prior open-vocabulary 3D-GS methods in both object selection and instance segmentation, offering a flexible and accurate solution for language-driven 3D scene understanding. Project page: https://csiro-robotics.github.io/Ilov3Splat.

---


### 114. [DALight-3D: A Lightweight 3D U-Net for Brain Tumor Segmentation from Multi-Modal MRI](https://arxiv.org/abs/2605.04518)

**<font color=#1a73e8>作者：</font>** Nand Kumar Mishra, Dhruv Mishra, Dr Manu Pratap Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic brain tumor segmentation from multi-modal MRI remains challenging because volumetric models often incur substantial computational cost. This paper presents DALight-3D, a compact 3D U-Net variant that combines depthwise separable 3D convolutions, identifier-conditioned normalization, cross-slice attention, and adaptive skip fusion. The method is evaluated on the Medical Segmentation Decathlon Task01 BrainTumour benchmark under matched optimization settings against standard 3D U-Net, Attention U-Net, Residual 3D U-Net, and V-Net baselines. In the reported 50-epoch comparison, DALight-3D achieves a mean Dice of 0.727 with 2.22M parameters, compared with 0.710 Dice and 3.20M parameters for Residual 3D U-Net. Component-wise ablations show consistent performance degradation when SepConv, identifier-conditioned normalization, CSA, or SSFB is removed. These results indicate that DALight-3D offers a favorable accuracy-efficiency trade-off within the present benchmark setting.

---


### 115. [FL-Sailer: Efficient and Privacy-Preserving Federated Learning for Scalable Single-Cell Epigenetic Data Analysis via Adaptive Sampling](https://arxiv.org/abs/2605.04519)

**<font color=#1a73e8>作者：</font>** Guangyi Zhang, Yi Dai, Yiyun He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-cell ATAC-seq (scATAC-seq) enables high-resolution mapping of chromatin accessibility, yet privacy regulations and data size constraints hinder multi-institutional sharing. Federated learning (FL) offers a privacy-preserving alternative, but faces three fundamental barriers in scATAC-seq analysis: ultra-high dimensionality, extreme sparsity, and severe cross-institutional heterogeneity. We propose FL-Sailer, the first FL framework designed for scATAC-seq data. FL-Sailer integrates two key innovations: (i) adaptive leverage score sampling, which selects biologically interpretable features while reducing dimensionality by 80%, and (ii) an invariant VAE architecture, which disentangles biological signals from technical confounders via mutual information minimization. We provide a convergence guarantee, showing that FL-Sailer converges to an approximate solution of the original high-dimensional problem with bounded error. Extensive experiments on synthetic and real epigenomic datasets demonstrate that FL-Sailer not only enables previously infeasible multi-institutional collaborations but also surpasses centralized methods by leveraging adaptive sampling as an implicit regularizer to suppress technical noise. Our work establishes that federated learning, when tailored to domain-specific challenges, can become a superior paradigm for collaborative epigenomic research.

---


### 116. [DAO-enabled decentralized physical AI: A new paradigm for human-machine collaboration](https://arxiv.org/abs/2605.04522)

**<font color=#1a73e8>作者：</font>** Mark C. Ballandies, Florian Spychiger, Uwe Serdült 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We propose DAO-enabled decentralized physical AI (DePAI), a democratic architecture for coordinating humans and autonomous machines in the operation and governance of physical-digital systems. We (1) synthesize foundations in blockchains, decentralized autonomous organizations (DAOs), and cryptoeconomics; (2) connect DAO design with digital-democracy research on deliberation and voting, showing how each can advance the other; (3) position DAO-governed decentralized physical infrastructure networks (DePIN) within a vertically integrated stack that links energy and sensing to connectivity, storage/compute, models, and robots; (4) show how these elements specify workflows that couple machine execution with human oversight, enabling enhanced self-organization of techno-socio-economic systems, which we call DePAI; and (5) analyze risks, including security, centralization, incentive failure, legal exposure, and the crowding-out of intrinsic motivation, and argue for value-sensitive design and continuously adaptive governance. DePAI offers a path to scalable, resilient self-organization that integrates physical infrastructure, AI, and community ownership under transparent rules, on-chain incentives, and permissionless participation, aiming to preserve human autonomy.

---


### 117. [High-Fidelity Single-Image Head Modeling with Industry-Grade Topology](https://arxiv.org/abs/2605.04524)

**<font color=#1a73e8>作者：</font>** Yunmu Wang, Zoubin Bi, Bowen Cai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a single-image head mesh reconstruction framework that addresses the longstanding challenge of simultaneously preserving facial identity and producing industry-grade topology. Our framework adopts a coarse-to-fine optimization pipeline that refines a rigged template across three stages -- rig, joint, and vertex -- achieving stable convergence and consistent topology. To mitigate the ill-posed nature of single-image 3D face reconstruction and ensure identity preservation, we employ a normal consistency objective jointly with landmark alignment. To further preserve local surface structure and enforce topological regularity, we introduce geometry-aware constraints based on Gaussian curvature and conformal consistency, along with auxiliary regularizations that correct fine artifacts such as lip seams and eyelid discontinuities. Our hierarchical optimization with geometry-aware regularization yields meshes with semantically meaningful edge flow and industry-grade topology. After geometry reconstruction, we extract UV-space texture and normal maps to preserve appearance details for visualization and downstream use. In a user study with 22 professional technical artists, our results were assessed as approaching industry-grade usability, and 95% of participants ranked our method as the top-performing approach, underscoring its effectiveness for real-world digital human production.

---


### 118. [Velox: Learning Representations of 4D Geometry and Appearance](https://arxiv.org/abs/2605.04527)

**<font color=#1a73e8>作者：</font>** Anagh Malik, Dorian Chan, Xiaoming Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a framework for learning latent representations of 4D objects which are descriptive, faithfully capturing object geometry and appearance; compressive, aiding in downstream efficiency; and accessible, requiring minimal input, i.e., an unstructured dynamic point cloud, to construct. Specifically, Velox trains an encoder to compress spatiotemporal color point clouds into a set of dynamic shape tokens. These tokens are supervised using two complementary decoders: a 4D surface decoder, which models the time-varying surface distribution capturing the geometry; and a Gaussian decoder, which maps the tokens to 3D Gaussians, helping learn appearance. To demonstrate the utility of our representation, we evaluate it across three downstream tasks -- video-to-4D generation, 3D tracking, and cloth simulation via image-to-4D generation -- and observe strong performances in all settings.

---


### 119. [From Video-to-PDE: Data-Driven Discovery of Nonlinear Dye Plume Dynamics](https://arxiv.org/abs/2605.04535)

**<font color=#1a73e8>作者：</font>** Cesar Acosta-Minoli, Sayantan Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring continuum models directly from video is hampered by two facts: the recorded field is uncalibrated image intensity rather than a physical state, and direct numerical differentiation of noisy frames is unstable. We develop a video-to-PDE pipeline that converts grayscale recordings of an ink plume into a normalised scalar field $u(x,y,t)$, isolates a bulk drift $\mathbf{v}(t)$ from intrinsic spreading via the intensity-weighted centroid, and identifies an effective transport law by weak-form sparse regression. Conditioning, threshold-sweep and random-centre diagnostics show that overcomplete libraries are strongly collinear; the search is therefore restricted to compact gradient-based libraries. Coefficients are refined by an inverse physics-informed network and recalibrated against forward rollouts, with a chronological block bootstrap quantifying uncertainty. The selected reduced model $u_t+\mathbf v(t)\!\cdot\!\nabla u = 9.005\,|\nabla u|^{2}+0.666\,\Delta u$ outperforms advection--diffusion baselines on held-out frames, retains a positive Laplacian coefficient, and admits a Cole--Hopf reduction to a linear advection--diffusion equation. The framework demonstrates that uncalibrated visual data can yield compact, predictive and structurally interpretable continuum models when discovery, calibration and uncertainty are treated as distinct stages.

---


### 120. [Angle-I2P: Angle-Consistent-Aware Hierarchical Attention for Cross-Modality Outlier Rejection](https://arxiv.org/abs/2605.04541)

**<font color=#1a73e8>作者：</font>** Muyao Peng, Shun Zou, Pei An 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-point-cloud registration (I2P) is a fundamental task in robotic applications such as manipulation,grasping, and localization. Existing deep learning-based I2P methods seek to align image and point cloud features in a learned representation space to establish correspondences, and have achieved promising results. However, when the inlier ratio of the initial matching pairs is low, conventional Perspective-n-Points (PnP) methods may struggle to achieve accurate results. To address this limitation, we propose Angle-I2P, an outlier rejection network that leverages angle-consistent geometric constraints and hierarchical attention. First, we design a scale-invariant, crossmodality geometric constraint based on angular consistency. This explicit geometric constraint guides the model in distinguishing inliers from outliers. Furthermore, we propose a global-tolocal hierarchical attention mechanism that effectively filters out geometrically inconsistent matches under rigid transformation, thereby improving the Inlier Ratio (IR) and Registration Recall (RR). Experimental results demonstrate that our method achieves state-of-the-art performance on the 7Scenes, RGBD Scenes V2, and a self-collected dataset, with consistent improvements across all benchmarks.

---


### 121. [UniVer: A Unified Perspective for Multi-step and Multi-draft Speculative Decoding](https://arxiv.org/abs/2605.04543)

**<font color=#1a73e8>作者：</font>** Yepeng Weng, Qiao Hu, Takehisa Yairi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates Large Language Models via draft-then-verify, where verification can be framed as an Optimal Transport (OT) problem. Existing approaches typically handle multi-draft and multi-step aspects in isolation, applying either flat OT to single-step drafts or per-token rejection sampling to tree-structured candidates. This separation leaves the joint regime (where multi-step dependencies meet multi-draft branching) poorly optimized, as local verification rules fail to exploit the coupling between horizontal and vertical dimensions of candidate trees. In this paper, we propose a unified perspective that casts tree-based verification as a conditional OT problem. Our key insight is that vertical dependencies can be abstracted through prefix acceptance probabilities, which act as dynamic scaling factors to actively guide horizontal draft selection. Based on this principle, we introduce UniVer, a verification algorithm that jointly optimizes across tree levels by composing local optimal transport plans under prefix constraints. We prove that UniVer remains lossless and achieves the optimal acceptance rate under the proposed conditional framework. Extensive experiments across different tasks and models demonstrate that UniVer improves acceptance length by 4.2% to 8.5% over standard recursive rejection sampling without replacement, while maintaining exact distributional alignment with the target model.

---


### 122. [Event-Based Early Warning of Vineyard Disease Risk from Environmental Time Series](https://arxiv.org/abs/2605.04548)

**<font color=#1a73e8>作者：</font>** Ivica Dimitrovski, Ivan Kitanovski, Danco Davcev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate early warning of vineyard disease risk from environmental observations is essential for timely intervention and more sustainable crop protection. However, many existing studies formulate disease prediction as daily presence classification, which can favor persistence-driven predictions and provide only limited support for actionable short-horizon warning. In this paper, we present an event-based approach for early warning of vineyard disease risk from environmental time series and evaluate it through a vineyard case study. Rather than predicting daily disease status, the task is reformulated to predict transitions into annotated disease-risk periods within a future window of 3-7 days. To reduce fragmentation caused by short interruptions in the binary labels, new events are defined only after a minimum disease-free gap. This formulation encourages models to capture environmental precursors associated with upcoming risk periods instead of merely reproducing temporal persistence. Using multi-year agro-meteorological data, we construct input representations that capture humidity dynamics, rainfall accumulation, temperature variability, and seasonal structure through cyclic temporal encoding. We evaluate representative methods from classical machine learning and deep learning, including XGBoost, Long Short-Term Memory (LSTM) networks, and Temporal Convolutional Networks (TCNs), using both standard classification metrics and an event-oriented early warning protocol. The results show that the event-based formulation supports practical short-horizon warning, while the compared models exhibit distinct trade-offs between event recall, lead time, and false-alert behavior. Overall, the study underscores the importance of problem formulation in environmental time-series learning and demonstrates the value of event-based prediction for vineyard disease warning systems.

---


### 123. [The Newsworthiness of Brazilian Distress: A Peak Analysis on Time Series of International Media Attention to Disasters in Brazil](https://arxiv.org/abs/2605.04552)

**<font color=#1a73e8>作者：</font>** Brielen Madureira, Andreas Niekler, Marc Keuschnigg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Media coverage influences disaster response, yet the drivers of international media attention to local events remain unevenly understood. Brazil offers a compelling case: some of its natural and technological disasters occasionally hit the international headlines. However, systematic analyses of what makes these events be discussed abroad are still missing. Addressing this gap requires representative, validated and country-specific news datasets. This paper presents a peak analysis of 2k news about Brazilian fires and landslides in German newspapers from 2000 to 2024. Using time series segmentation to detect news event peaks, we examine the extent to which they can be temporally aligned with observations in national and global disaster databases.

---


### 124. [InterMesh: Explicit Interaction-Aware End-to-End Multi-Person Human Mesh Recovery](https://arxiv.org/abs/2605.04554)

**<font color=#1a73e8>作者：</font>** Kaili Zheng, Kaiwen Wang, Xun Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans constantly interact with their surroundings. Existing end-to-end multi-person human mesh recovery methods, typically based on the DETR framework, capture inter-human relationships through self-attention across all human queries. However, these approaches model interactions only implicitly and lack explicit reasoning about how humans interact with objects and with each other. In this paper, we propose InterMesh, a simple yet effective framework that explicitly incorporates human-environment interaction information into human mesh recovery pipeline. By leveraging a human-object interaction detector, InterMesh enriches query representations with structured interaction semantics, enabling more accurate pose and shape estimation. We design lightweight modules, Contextual Interaction Encoder and Interaction-Guided Refiner, to integrate these features into existing HMR architectures with minimal overhead. We validate our approach through extensive experiments on 3DPW, MuPoTS, CMU Panoptic, Hi4D, and CHI3D datasets, demonstrating remarkable improvements over state-of-the-art methods. Notably, InterMesh reduces MPJPE by 9.9% on CMU Panoptic and 8.2% on Hi4D, highlighting its effectiveness in scenarios with complex human-object and inter-human interactions.

---


### 125. [Counter-Dyna: Data-Efficient RL-Based HVAC Control using Counterfactual Building Models](https://arxiv.org/abs/2605.04555)

**<font color=#1a73e8>作者：</font>** Jan Marco Ruiz de Vargas, Fabian Raisch, Zoltan Nagy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning (MBRL) offers a promising approach for data-efficient energy management in buildings, combining the strengths of predictive modeling and reinforcement learning. While previous MBRL methods applied to HVAC control have reduced training data requirements, they still require several months of interaction with the building to learn a satisfactory control policy. A key reason is that existing surrogate models attempt to predict the entire state-space, including weather and electricity prices that are unaffected by control actions, or completely ignore these variables. Addressing these issues, we propose Counter-Dyna, a method that enhances the data-efficiency of Dyna, an MBRL method. We create data-efficient counterfactual surrogate models (CSM) by leveraging invariances in the state-space. Using a CSM in Dyna speeds up RL training measured in environment interaction data compared to previous results. In comparison with previous state-of-the-art that used 6-12 months of environment interactions, our method needs only 5 weeks. We evaluate our method in a large simulation study using the literature standard BOPTEST framework and proximal policy algorithm (PPO) as the RL algorithm. Our results show cost-saving potentials of 5.3% to 17.0% in a hypothetical deployment scenario. Our work is a significant step towards making real-world deployment of RL algorithms in HVAC control practically viable.

---


### 126. [Efficient Geometry-Controlled High-Resolution Satellite Image Synthesis](https://arxiv.org/abs/2605.04557)

**<font color=#1a73e8>作者：</font>** Vlad Vasilescu, Daniela Faur, Teodor Costachioiu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution satellite images are often scarce and costly, especially for remote areas or infrequent events. This shortage hampers the development and testing of machine learning models for land-cover classification, change detection, and disaster monitoring. In this paper, we tackle the problem of geometry-controlled high-resolution satellite image synthesis by adding control over existing pre-trained diffusion models. We propose a simple yet efficient method for controlling the synthesis process by leveraging only skip connection features using windowed cross-attention modules. Several previously established control techniques are compared, indicating that our method achieves comparable performance while leading to a better alignment with the geometry control map. We also discuss the limitations in current evaluation approaches, amplifying the necessity of a consistent alignment assessment.

---


### 127. [SAMIC: A Lightweight Semantic-Aware Mamba for Efficient Perceptual Image Compression](https://arxiv.org/abs/2605.04560)

**<font color=#1a73e8>作者：</font>** Jiaqian Zhang, Hao Wei, Chenyang Ge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perceptual image compression focuses on preserving high visual quality under low-bitrate constraints. Most existing approaches to perceptual compression leverage the strong generative capabilities of generative adversarial networks or diffusion models, at the cost of substantial model complexity. To this end, we present an efficient perceptual image compression method that exploits the long-range modeling capability and linear computational complexity of state space models, with a particular focus on Mamba. Unlike existing methods that rely on an inherently fixed scanning order and consequently impair semantic continuity and spatial correlation, we develop a semantic-aware Mamba block (SAMB) to enable scanning guided by dynamically clustered semantic features, thereby alleviating the strict causality constraints and long-range information decay inherent to Mamba. Inspired by singular value decomposition, we design an SVD-inspired redundancy reduction module (SVD-RRM) that performs a low-rank approximation on the latent features by introducing a learnable soft threshold, leading to channel-wise redundancy information reduction. The proposed SAMB is integrated into both the encoder and decoder of the compression framework, whereas the SVD-RRM is incorporated only in the encoder. Extensive experiments demonstrate that our method performs favorably against state-of-the-art approaches in terms of rate-distortion-perception tradeoff and model complexity. The source code and pretrained models will be available at this https URL.

---


### 128. [Dream-MPC: Gradient-Based Model Predictive Control with Latent Imagination](https://arxiv.org/abs/2605.04568)

**<font color=#1a73e8>作者：</font>** Jonathan Spieler, Sven Behnke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-of-the-art model-based Reinforcement Learning (RL) approaches either use gradient-free, population-based methods for planning, learned policy networks, or a combination of policy networks and planning. Hybrid approaches that combine Model Predictive Control (MPC) with a learned model and a policy prior to leverage the advantages of both paradigms have shown promising results. However, these approaches typically rely on gradient-free optimization methods, which can be computationally expensive for high-dimensional control tasks. While gradient-based methods are a promising alternative, recent works have empirically shown that gradient-based methods often perform worse than their gradient-free counterparts. We propose Dream-MPC, a novel approach that generates few candidate trajectories from a rolled-out policy and optimizes each trajectory by gradient ascent using a learned world model, uncertainty regularization and amortization of optimization iterations over time by reusing previously optimized actions. Our results on 24 continuous control tasks show that Dream-MPC can significantly improve the performance of the underlying policy and can outperform gradient-free MPC and state-of-the-art baselines. We will open source our code and more at this https URL.

---


### 129. [Lightning Unified Video Editing via In-Context Sparse Attention](https://arxiv.org/abs/2605.04569)

**<font color=#1a73e8>作者：</font>** Shitong Shao, Zikai Zhou, Haopeng Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video editing has evolved toward In-Context Learning (ICL) paradigms, yet the resulting quadratic attention costs create a critical computational bottleneck. In this work, we propose In-context Sparse Attention (ISA), the first near-lossless empirical sparse framework tailored for ICL video editing. Our design is grounded in two key insights: first, context tokens exhibit significantly lower saliency than source tokens; second, we theoretically prove and empirically validate that Query sharpness correlates with approximation error. Motivated by these findings, ISA implements an efficient pre-selection strategy to prune redundant context, followed by a dynamic query grouping mechanism that routes high-error queries to full attention and low-error ones to a computationally efficient 0-th order Taylor sparse attention. Furthermore, we build \textbf{\texttt{LIVEditor}} , a novel lightning video editing model via ISA and a proposed video-editing data pipeline that curated a 1.7M high-quality dataset. Extensive experiments demonstrate that LIVEditor achieves a $\sim$60% reduction in attention-module latency while surpassing state-of-the-art methods across EditVerseBench, IVE-Bench, and VIE-Bench, delivering near-lossless acceleration without compromising visual fidelity.

---


### 130. [PINSIGHT: A Comprehensive Threat Exploration of Domain-Adaptive Wi-Fi based PIN Code Inference](https://arxiv.org/abs/2605.04570)

**<font color=#1a73e8>作者：</font>** Johannes Kortz, Paul Staat, Christof Paar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Wi-Fi signals can be exploited by adversaries as a sensing side channel to eavesdrop on physical information. By monitoring propagation effects of radio waves within the victim's environment, attackers can remotely infer sensitive information. One particularly concerning example is PIN code inference, where the attacker faces the challenge of mapping Wi-Fi physical-layer channel estimations back into typed digits. While effective in their training environment, such attacks typically fail as soon as they are deployed in unseen environments. The current state-of-the-art attack, WiKI-Eve, attempts to overcome this problem using a deep-learning approach, reporting high PIN code inference accuracy independent of environments, devices, and users. While this suggests a significant real-world threat, it is not well understood how far the attack actually reaches, nor what its underlying generalization performance is based on. In this work, we close this gap by presenting PINSIGHT, a novel methodology that separates the effects of environmental variation and PIN code typing. This enables the first rigorous threat assessment of such attacks, evaluating their generalization capabilities and limitations. Our approach leverages a robotic typing platform that produces highly repeatable keystroke events across systematically varied environment changes [...]. This dataset constitutes the first benchmark for environment generalization in Wi-Fi PIN code inference attacks. Evaluating several state-of-the-art methods, we find that attacks generalize reliably across changes in the surrounding environment but degrade substantially when the channel's encoding of typing itself shifts - precisely the condition that defines a realistic attack scenario. We conclude that the reported performance of current state-of-the-art Wi-Fi PIN inference attacks is not representative of the actual real-world threat.

---


### 131. [VL-UniTrack: A Unified Framework with Visual-Language Prompts for UAV-Ground Visual Tracking](https://arxiv.org/abs/2605.04574)

**<font color=#1a73e8>作者：</font>** Boyue Xu, Ruichao Hou, Tongwei Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UAV-ground visual tracking (UGVT) aims to simultaneously track the same object from both the UAV and the ground view. However, existing two-stream methods suffer from isolated feature extraction and rely heavily on implicit appearance matching, which struggles to establish reliable correspondence under drastic view differences, leading to tracking unreliability. To address these limitations, we propose VL-UniTrack, a fully unified framework enhanced by visual-language prompts. By encoding features from both views within a single shared encoder, our method breaks the barrier of feature isolation to facilitate sufficient cross-view interaction. To overcome the ambiguity caused by relying solely on appearance matching, we design visual-language geometric prompting module, which fuses language descriptions with visual features to generate learnable prompts. These prompts are then fed into our prompt-guided cross-view adapter module to enable sufficient cross-view feature interaction and to guide the learning of view-specific feature representations. Furthermore, a confidence-modulated mutual distillation loss is proposed to regularize the training by mitigating noise propagation. Extensive experiments demonstrate that our method achieves state-of-the-art performance on the latest benchmark. The code can be downloaded in this https URL

---


### 132. [Benchmarking POS Tagging for the Tajik Language: A Comparative Study of Neural Architectures on the TajPersParallel Corpus](https://arxiv.org/abs/2605.04576)

**<font color=#1a73e8>作者：</font>** Mullosharaf K. Arabov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents the first benchmark for the task of automatic part-of-speech (POS) tagging for the Tajik language. Despite the existence of multilingual language models demonstrating high effectiveness for many of the world's languages, their capacity for grammatical analysis of Tajik has remained unexplored until now. The aim of this study is to fill this gap through a systematic comparison of classical neural network architectures and modern multilingual transformers.
Experiments were conducted on the TajPersParallel corpus, a parallel lexical resource comprising approximately 44,000 dictionary entries. Due to the absence of full-fledged example sentences in the current version of the corpus, the task was performed at the level of isolated lexical units, representing a challenging case of context-independent classification. The study compares the following architectures: a recurrent BiLSTM-CRF model, as well as multilingual models XLM-RoBERTa (large), mBERT, ParsBERT (Persian), and ruBERT (Russian), adapted using the parameter-efficient fine-tuning method LoRA.
The testing results showed that the best performance is achieved by the mBERT + LoRA model (macro F1-score = 0.11, weighted F1-score = 0.62). It was established that in the absence of syntactic context, all models experience significant difficulty in resolving morphological ambiguity, successfully classifying primarily high-frequency classes ("noun," "adjective") while demonstrating zero effectiveness for rare function words. Zero-shot evaluation revealed the greatest typological proximity of Tajik to Persian (ParsBERT) and Russian (ruBERT). The obtained results form a foundation for further research and development in the field of automatic processing of the Tajik language.

---


### 133. [GTF: Omnidirectional EPI Transformer for Light Field Super-Resolution](https://arxiv.org/abs/2605.04581)

**<font color=#1a73e8>作者：</font>** Kunyu Li, Fei Wang, Lichao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Light field (LF) image super-resolution benefits from Epipolar Plane Images (EPIs), whose line slopes explicitly encode disparity. However, existing Transformer-based LF SR methods mainly attend to horizontal and vertical EPIs, leaving diagonal epipolar geometry underexplored. We present GTF, an omnidirectional EPI Transformer that explicitly models horizontal, vertical, 45-degree, and 135-degree EPIs within a unified reconstruction framework. GTF combines directional EPI processing, MacPI-based prior injection, adaptive directional fusion, and a topology-preserving feed-forward network to better exploit LF geometry. For the NTIRE 2026 fidelity tracks, we use GTF as the main model, while a lightweight GTF-Tiny variant targets the efficiency track. On five standard LF SR benchmarks covering both real-captured and synthetic scenes, GTF reaches 32.78 dB without inference-time enhancement, and stronger inference settings with EPSW and test-time augmentation further improve performance. Under the NTIRE 2026 efficiency constraint, GTF-Tiny attains 32.57 dB with only 0.915M parameters and 19.81 GFLOPs. In the NTIRE 2026 Light Field Image Super-Resolution Challenge, our submissions rank 3rd on Track 1 and Track 3 and 4th on Track 2. Architecture-evolution, channel-width, and inference analyses further support the effectiveness of diagonal EPI modeling, directional fusion, and the lightweight design.

---


### 134. [TajikNLP: An Open-Source Toolkit for Comprehensive Text Processing of Tajik (Cyrillic Script)](https://arxiv.org/abs/2605.04583)

**<font color=#1a73e8>作者：</font>** Mullosharaf K. Arabov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Tajik language, written in Cyrillic script, remains severely under-resourced in terms of publicly available natural language processing (NLP) toolkits, hindering both linguistic research and applied development. This paper introduces TajikNLP, an open-source Python library that provides the first comprehensive pipeline for processing authentic Tajik text while preserving the original Cyrillic orthography. The library implements a modular architecture centered around a unified Doc object, enabling sequential application of components for cleaning, normalization, tokenization (including subword BPE), morphemic segmentation, part-of-speech tagging, stemming, lemmatization, and sentence splitting. A novel unified morphology engine is introduced, offering controlled and deep analysis modes that significantly improve handling of Tajik's agglutinative nominal and verbal inflections. The release further incorporates a lexicon-based sentiment analyser and pre-trained Word2Vec/FastText embeddings loaded directly from the Hugging Face Hub. To ensure reproducibility and facilitate future research, four accompanying linguistic datasets -- a POS-tagged corpus (52.5k entries), a sentiment lexicon (3.5k entries), a toponym gazetteer (5.6k entries), and a personal names dataset (3.8k entries) -- have been openly published under permissive licenses. The library's reliability is validated by an extensive test suite of 616 automated tests achieving 93% source code coverage. TajikNLP thus establishes a foundational technological infrastructure for Tajik language processing, lowering the barrier to entry for both academic and industrial applications in low-resource Cyrillic-script environments.

---


### 135. [From Diffusion to Rectified Flow: Rethinking Text-Based Segmentation](https://arxiv.org/abs/2605.04590)

**<font color=#1a73e8>作者：</font>** Zishen Qu, Xuesong Li, Haijian Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-based image segmentation aims to delineate object boundaries within an image from text prompts, offering higher flexibility and broader application scope compared to traditional fixed-category segmentation tasks. Recent studies have shown that diffusion models (e.g., Stable Diffusion) can provide rich multimodal semantic features, leading to studies of using diffusion models as feature extractors for segmentation tasks. Such methods, however, inherit the generative natures of diffusion models that are harmful to discriminative segmentation tasks. In response, we propose RLFSeg, a novel framework that leverages Rectified Flow to learn direct mapping from the image to the segmentation mask within the latent space. The model is thus freed from the noise-denoise process and the need to optimize the time step of diffusion models, resulting in substantially better performance than previous diffusion-based methods, especially on zero-shot scenarios. By introducing label refinement and an Adaptive One-Step Sampling strategy, the model achieves higher accuracy even on a single inference step. The framework redirects a pretrained generative model to the discriminative segmentation task with zero modification to model structure, thus reveals promising application potential and significant research value.

---


### 136. [DiCLIP: Diffusion Model Enhances CLIP's Dense Knowledge for Weakly Supervised Semantic Segmentation](https://arxiv.org/abs/2605.04593)

**<font color=#1a73e8>作者：</font>** Zhiwei Yang, Pengfei Song, Yucong Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly Supervised Semantic Segmentation (WSSS) with image-level labels typically leverages Class Activation Maps (CAMs) to achieve pixel-level predictions. Recently, Contrastive Language-Image Pre-training (CLIP) has been introduced to generate CAMs in WSSS. However, previous WSSS methods solely adopt CLIP's vision-language paired property for dense localization, neglecting its inherently limited dense knowledge across both visual and text modalities, which renders CAM generation suboptimal. In this work, we propose DiCLIP, a novel WSSS framework that leverages the generative diffusion model to enhance CLIP's dense knowledge across two modalities. Specifically, Visual Correlation Enhancement (VCE) and Text Semantic Augmentation (TSA) modules are proposed for dense prediction enhancement. To improve the spatial awareness of visual features, our VCE module utilizes diffusion's reliable spatial consistency to mitigate the over-smoothing issue in CLIP's attention. It designs the Attention Clustering Refinement (ACR) module to reliably extract diverse correlation maps from the diffusion model. The correlation maps act as a diversity bias for CLIP's self-attention, recursively pushing its visual features towards a more discriminative dense distribution. To augment the semantics of text embeddings, our TSA module argues that a single text modality is insufficient to encompass the variability of visual categories. Thus, we leverage diffusion's generative power to maintain a dynamic key-value cache model, shifting CAM generation from a patch-text matching mechanism to a novel visual knowledge retrieval paradigm. With these enhancements, DiCLIP not only outperforms state-of-the-art methods on PASCAL VOC and MS COCO but also significantly reduces training costs. Code is publicly available at this https URL.

---


### 137. [HeterSEED: Semantics-Structure Decoupling for Heterogeneous Graph Learning under Heterophily](https://arxiv.org/abs/2605.04594)

**<font color=#1a73e8>作者：</font>** Xinyi Li, Ming Li, Lu Bai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world heterogeneous graphs exhibit pronounced heterophily, where connected nodes often have dissimilar labels or play different semantic roles. In such settings, standard heterogeneous graph neural networks that aggregate messages along metapaths or meta-relations primarily based on feature similarity can propagate misleading information, since feature similarity may be misaligned with underlying relational semantics. In this paper, we propose HeterSEED, a semantics-structure decoupling framework for heterogeneous graph learning under heterophily. HeterSEED decouples representation learning into a heterogeneous semantic channel that captures type- and relation-aware local semantics and a structure-aware heterophily channel that separates homophilic and heterophilic neighborhoods via pseudo-label-guided partitioning and aggregates them using metapath-based structural weights. A node-level adaptive fusion mechanism then combines the two channels to produce context-dependent node representations. Theoretically, we establish that, on heterogeneous graphs under heterophily, HeterSEED is strictly more expressive than standard heterogeneous graph neural networks that rely primarily on feature similarity and provably reduces the prediction bias introduced by heterophilic neighbors. Experiments on five real-world heterogeneous graphs, including two large-scale networks at the million-node and hundred-million-edge scale, demonstrate that HeterSEED consistently outperforms representative heterogeneous graph neural networks and recent heterophily-aware baselines, especially in strongly heterophilic regimes.

---


### 138. [Reference-based Category Discovery: Unsupervised Object Detection with Category Awareness](https://arxiv.org/abs/2605.04606)

**<font color=#1a73e8>作者：</font>** Yichen Li, Qiankun Liu, Ying Fu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional one-shot detection methods have addressed the closed-set problem in object detection, but the high cost of data annotation remains a critical challenge. General unsupervised methods generate pseudo boxes without category labels, thus failing to achieve category-aware classification. To overcome these limitations, we propose Reference-based Category Discovery (RefCD), an unsupervised detector that enables category-aware\footnotemark[1] detection without any manually annotated labels. It leverages feature similarity between predicted objects and unlabeled reference images. Unlike previous unsupervised methods that lack category guidance and one-shot methods which require labeled data, RefCD introduces a carefully designed feature similarity loss to explicitly guide the learning of potential category-specific features. Additionally, RefCD supports category-agnostic detection without reference images, serving as a unified framework. Comprehensive quantitative and qualitative analysis of category-aware and category-agnostic detection results demonstrates its effectiveness, and RefCD can learn category information in an unsupervised paradigm even without category labels.

---


### 139. [SensingAgents: A Multi-Agent Collaborative Framework for Robust IMU Activity Recognition](https://arxiv.org/abs/2605.04608)

**<font color=#1a73e8>作者：</font>** Naiyu Zheng, Tianlong Yu, Haochen Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human Activity Recognition (HAR) using Inertial Measurement Unit (IMU) sensors is a cornerstone of mobile health, smart environments, and human-computer interaction. However, current deep learning-based HAR models often struggle with heavy reliance on labeled data, position-specific ambiguity, and a lack of transparent reasoning. Inspired by the advanced agents framework, which emulates a collaborative agent using Large Language Models (LLMs), we propose SensingAgents, a novel multi-agent system for robust IMU activity recognition. SensingAgents organizes LLM-powered agents into specialized roles: a group of Analyst Agents for position-specific sensor analysis (arm, wrist, belt, pocket), a pair of Advocate Agents that resolves sensor conflicts through dynamic and static dialectical debates, and a Decision Agent that ensures reliability under sensor drift or failure. Evaluation on the Shoaib dataset demonstrates that SensingAgents significantly outperforms state-of-the-art single-agent and multi-agent LLM models, achieving an accuracy of 79.5% in a zero setting--29% higher than existing agent models and 9.4% higher than deep learning baselines--particularly in complex scenarios where multi-sensor data is conflicting or noisy. Our work highlights the potential of multi-agent collaborative reasoning for advancing the robustness and interpretability of ubiquitous sensing systems.

---


### 140. [Temporal Structure Matters for Efficient Test-Time Adaptation in Wearable Human Activity Recognition](https://arxiv.org/abs/2605.04617)

**<font color=#1a73e8>作者：</font>** Zishu Zhou, Zaipeng Xie, Xuanyao Jie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wearable human activity recognition (WHAR) models often suffer from performance degradation under real-world cross-user distribution shifts. Test-time adaptation (TTA) mitigates this degradation by adapting models online using unlabeled test streams, yet existing methods largely inherit assumptions from vision tasks and underexploit the inherent inter-window temporal structure in WHAR streams. In this paper, we revisit such temporal structure as a feature-conditioned inference signal rather than merely an output-space smoothing prior. We derive the insight that temporal continuity and observation-induced feature deviations provide complementary cues for determining when to preserve or release temporal inertia and where to route prediction refinement during likely transitions. Building upon this insight, we propose SIGHT, a lightweight and backpropagation-free TTA framework for WHAR, enabling real-time edge deployment. SIGHT estimates predictive surprise by comparing the current feature with a prototype-based expected state, and then uses the resulting feature deviation to guide geometry-aware transition routing based on prototype alignment and stream-level marginal habit tracking. Evaluations on real-world datasets confirm that SIGHT outperforms existing TTA baselines while reducing computational and memory costs.

---


### 141. [Library learning with e-graphs on jazz harmony](https://arxiv.org/abs/2605.04622)

**<font color=#1a73e8>作者：</font>** Zeng Ren, Maddy Bowers, Xinyi Guan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans can acquire a highly structured intuitive understanding of musical patterns, yet these patterns often require multiple iterations of reflection and re-listening to internalize fully. To capture such an internalization process, we present a computational model for the learning of jazz harmonic patterns based on library learning. Given a corpus of harmonic progressions, our model searches over a space of programs composed of primitive harmonic relations in order to discover concise generative explanations of the corpus. The model first enumerates possible programs for each piece, and then jointly learns a library of harmonic patterns and refactored programs. To efficiently navigate the vast joint space of programs and libraries, we integrate deductive parsing with library learning on e-graphs. We explore how well our model captures aspects of human musical pattern learning by evaluating the intuitiveness of both programs and libraries, as well as similarities to human-written harmonic derivations.

---


### 142. [AuditRepairBench: A Paired-Execution Trace Corpus for Evaluator-Channel Ranking Instability in Agent Repair](https://arxiv.org/abs/2605.04624)

**<font color=#1a73e8>作者：</font>** Yuelin Hu, Zhenbo Yu, Zhengxue Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent-repair leaderboards reorder under evaluator reconfiguration, and a measurable share of the reordering is produced by methods that consult evaluator-derived signal during internal selection of candidate repairs. We document this failure mode on a public leaderboard and release AuditRepairBench, a paired-execution trace corpus of 576,000 registered cells (96,000 executed) that operationalizes evaluator-channel-blocking ranking instability within a declared observability boundary. A modular screening architecture decides pathway-blocking through four interchangeable implementations, a learned influence proxy, a rule-based channel-exposure ratio that uses no trained model, a counterfactual sensitivity proxy, and a sparse human-audit proxy, combined into a screening posterior that feeds a cell-level flip functional, a set-valued label, a stratified system score, and a set-valued leaderboard. The resource is supported by mechanism-anchored validation on an 80-case source-level channel-surgery subset, an independent-discovery protocol under which two annotator groups separated from the pipeline developers discover coupling patterns blinded to the screening design and the frozen ensemble attains pooled AUROC 0.83 on their 79 cases, implementation robustness, uncertainty propagation that raises 95% coverage from 0.81 to 0.95, and forward transfer with pooled community-evaluator Spearman \r{ho} = 0.65. Screening-guided blinding patches reduce rank displacement by 55--74% (mean 62%) at fewer than 50 lines of code, whereas random channel blinding produces at most 7% reduction and generic retraining at most 13%. AuditRepairBench-Lite, a rule-only configuration on a 12,000-cell subset, preserves the leaderboard at Kendall {\tau} = 0.88 under twenty-four GPU-hours and is the primary release artifact at 42 GB.

---


### 143. [Autonomous Synchronization of Discrete-Time Heterogeneous Multiagent Systems](https://arxiv.org/abs/2605.04627)

**<font color=#1a73e8>作者：</font>** Wei Hu, Quanyi Liang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper investigates the autonomous synchronization problem for discrete-time heterogeneous multiagent systems.
The synchronization problem is transformed into the asymptotic decoupling problem of stable modes in a class of discrete-time linear time-varying systems,
for which we provide a sufficient condition.
Leveraging this condition, synchronization conditions are established.
The synchronization conditions are based on the average of the agents' initial dynamic matrices,
without requiring the differences among these matrices to be small.
This approach reduces the conservativeness of existing conditions and achieves a unification of both homogeneous and heterogeneous systems.
Numerical simulation results are provided to support the theoretical findings.

---


### 144. [UniPCB: A Generation-Assisted Detection Framework for PCB Defect Inspection](https://arxiv.org/abs/2605.04635)

**<font color=#1a73e8>作者：</font>** Huan Zhang, Lianghong Tan, Yichu Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Printed Circuit Board (PCB) defect inspection faces two compounding challenges: scarce and imbalanced defect samples that limit model training, and insufficient feature representation under complex circuit backgrounds. Existing generation methods rely on single-modality conditions with coarse structural control, while detection methods improve architectures without addressing the data bottleneck. To resolve both challenges jointly, we propose a generation-assisted PCB defect inspection framework that integrates controlled defect synthesis with task-specific defect detection. On the generation side, a Multi-modal Condition Generator extracts complementary edge, depth, and text conditions in parallel. A ScaleEncoder then embeds these conditions into the diffusion U-Net at four resolutions, and a Condition Modulation applies FiLM-style spatially-adaptive modulation at each scale, enabling structurally aligned and defect-aware sample synthesis. On the detection side, an Inverted Residual Shift Attention couples self-attention with shift-wise convolution to jointly capture global context and local texture, and a Cross-level Complementary Fusion Block generates pixel-level gates for selective cross-level feature fusion. The synthesized samples directly enrich the detection training set, so that improvements in generation compound with improvements in detection. Extensive experiments on DsPCBSD+ demonstrate that UniPCB achieves mAP@0.5 of 98.0% and mAP@0.5:0.95 of 61.8% on defect detection, surpassing all compared methods, while the generation branch attains an FID of 129.61 and SSIM of 0.619, outperforming existing conditional generation approaches.

---


### 145. [SWE-WebDevBench: Evaluating Coding Agent Application Platforms as Virtual Software Agencies](https://arxiv.org/abs/2605.04637)

**<font color=#1a73e8>作者：</font>** Siddhant Saxena, Nilesh Trivedi, Vinayaka Jyothi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The emergence of "vibe coding" platforms, where users describe applications in natural language and AI agents autonomously generate full-stack software, has created a need for rigorous evaluation beyond code-level benchmarks. In order to assess them as virtual software development agencies on understanding business requirements, making architectural decisions, writing production code, handling iterative modifications, and maintaining business readiness, we introduce SWE-WebDev Bench, a 68-metric evaluation framework spanning 25 primary and 43 diagnostic metrics across seven groups, organized along three dimensions: Interaction Mode (App Creation Request (ACR) vs. App Modification Request (AMR)), Agency Angle (Product Manager (PM), Engineering, Ops), and Complexity Tier (T4 multi-role SaaS, T5 AI-native).
Our evaluation (six platforms, three domains, 18 evaluation cells) reveals four recurring shortcomings in the current generation of AI app builders: (1) A specification bottleneck, where platforms compress rich business requirements into oversimplified technical plans, (2) A pervasive frontend-backend decoupling, where visually polished UIs mask absent or broken backend infrastructure, (3) A steep production-readiness cliff, where no platform scores above 60% on engineering quality and post-generation human effort varies substantially across platforms and (4) Widespread security and infrastructure failures, with no platform exceeding 65% Security Score against a 90% target and concurrency handling as low as 6%. These observations are descriptive of our sample and require larger-scale replication to establish generality. We release SWE-WebDev Bench as a community benchmark to enable such replication and help platform builders identify and address these gaps.
Code and benchmark resources are available at: this https URL and this https URL.

---


### 146. [Securing the Web with HSTS-Enforced](https://arxiv.org/abs/2605.04642)

**<font color=#1a73e8>作者：</font>** Aaron van Diepen, Adrian Zapletal, Fernando Kuipers  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> TLS stripping attacks expose sensitive web traffic by forcing secure HTTPS connections to fall back to unencrypted HTTP. At present, protection against these attacks relies on website operators explicitly opting into security by deploying mechanisms such as HTTP Strict Transport Security (HSTS) headers. These mechanisms have significant limitations: some are weak or difficult to configure, which raises the risk of misconfiguration and reduces practical adoption; others violate HTTP backward compatibility; at least one can even be abused to enable unintended user tracking.
We introduce HSTS-Enforced, a mechanism that eliminates the remaining attack surface for TLS stripping while still allowing operators to securely specify that their websites need to be accessed over HTTP when necessary, thereby maintaining accessibility. To achieve this, we flip the current opt-in security model to an opt-out model: all connections default to HTTPS, and operators can explicitly opt out if their websites require HTTP using so-called HTTP-Required indicators. We propose two such HTTP-Required indicators: a new DNS record and an HTTP-Required Preload list. We evaluate HSTS-Enforced under multiple deployment scenarios, demonstrating that it blocks all practical TLS stripping attempts while maintaining compatibility for sites that require HTTP - without introducing overhead in the typical case. Finally, we outline a practical transition path to accelerate global adoption.

---


### 147. [FAAST: Forward-Only Associative Learning via Closed-Form Fast Weights for Test-Time Supervised Adaptation](https://arxiv.org/abs/2605.04651)

**<font color=#1a73e8>作者：</font>** Guangsheng Bao, Hongbo Zhang, Han Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting pretrained models typically involves a trade-off between the high training costs of backpropagation and the heavy inference overhead of memory-based or in-context learning. We propose FAAST, a forward-only associative adaptation method that analytically compiles labeled examples into fast weights in a single pass. By eliminating memory or context dependence, FAAST achieves constant-time inference and decouples task adaptation from pretrained representation. Across image classification and language modeling benchmarks, FAAST matches or exceeds backprop-based adaptation while reducing adaptation time by over 90\% and is competitive to memory/context-based adaptation while saving memory usage by up to 95\%. These results demonstrate FAAST as a highly efficient, scalable solution for supervised task adaptation, particularly for resource-constrained models. We release the code and models at this https URL.

---


### 148. [CHE-TKG: Collaborative Historical Evidence and Evolutionary Dynamics Learning for Temporal Knowledge Graph Reasoning](https://arxiv.org/abs/2605.04652)

**<font color=#1a73e8>作者：</font>** Shuai-long Lei, Xiaobin Zhu, Jiarui Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Temporal knowledge graph (TKG) reasoning aims to predict future events from historical facts. A key challenge lies in jointly capturing two sources of predictive information in TKGs: historical evidence and evolutionary dynamics. However, existing methods typically focus on only one of these sources, which limits the ability to fully exploit the complementary predictive signals in TKGs. To address this, we propose CHE-TKG, a novel collaborative dual-view learning framework for TKG reasoning. CHE-TKG explicitly separates and jointly models historical evidence and evolutionary dynamics, aiming to learn and exploit their complementary predictive signals. Specifically, CHE-TKG constructs a historical evidence graph to capture long-term structural regularities and stable relational constraints, alongside an evolutionary dynamics graph to model temporal transitions and recent changes, with dedicated encoders for each view. We further employ relation decomposition and a contrastive alignment objective to better capture the predictive signals across the two views. Extensive experiments demonstrate that CHE-TKG achieves state-of-the-art performance on multiple benchmarks.

---


### 149. [Threshold-Guided Optimization for Visual Generative Models](https://arxiv.org/abs/2605.04653)

**<font color=#1a73e8>作者：</font>** Jinbin Bai, Yu Lei, Qingyu Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligning large visual generative models with human feedback is often performed through pairwise preference optimization. While such approaches are conceptually simple, they fundamentally rely on annotated pairs, limiting scalability in settings where feedback is collected as independent scalar ratings. In this work, we revisit the KL-regularized alignment objective and show that the optimal policy implicitly compares each sample's reward to an instance-specific baseline that is generally intractable. We propose a threshold-guided alignment framework that replaces this oracle baseline with a data-driven global threshold estimated from empirical score statistics. This formulation turns alignment into a binary decision task on unpaired data, enabling effective optimization directly from scalar feedback. We also incorporate a confidence weighting term to emphasize samples whose scores deviate strongly from the threshold, improving sample efficiency. Experiments across both diffusion and masked generative paradigms, spanning three test sets and five reward models, show that our method consistently improves preference alignment over previous methods. These results position our threshold-guided framework as a simple yet principled alternative for aligning visual generative models without paired comparisons.

---


### 150. [Contact Matrix: Enhancing Dance Motion Synthesis with Precise Interaction Modeling](https://arxiv.org/abs/2605.04662)

**<font color=#1a73e8>作者：</font>** Xuhai Chen, Zhi Cen, Huaijin Pi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating realistic reactive motions, in which one person reacts to the fixed motions of others, is challenging due to strict interaction constraints and a limited feasible solution space. This paper focuses on a typical scenario: duet dance, where high-quality data is scarce, motion patterns are complex, and the details of human interactions are both intricate and abundant. To tackle these challenges, we propose a novel two-stage framework. In the first stage, we introduce a motion VQ-VAE with separate body-part encoders and a joint decoder, enabling specialized codebooks to enhance representation capacity while dynamically modeling dependencies across body parts during decoding, thereby preventing inconsistencies in the generated motions. In the second stage, we propose a contact-aware diffusion model for reactive motion generation that jointly generates motion and a contact matrix between individuals, enabling explicit interaction modeling and providing guidance toward more precise and constrained interaction dynamics during sampling. Experiments show that our method outperforms Duolando with lower $\text{FID}_k$ (8.89 vs. 25.30) and $\text{FID}_{cd}$ (8.01 vs. 9.97), as well as a higher BED (0.4606 vs. 0.2858), indicating improved interaction fidelity and rhythmic synchronization.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-270](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
