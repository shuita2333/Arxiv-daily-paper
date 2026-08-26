# 📦 其他研究 | 2026年08月27日

> 本类共 **194** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-194](./part-04.md)

---

### 101. [Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research](https://arxiv.org/abs/2608.24306)

**<font color=#1a73e8>作者：</font>** Eran Hirsch, David Wan, Han Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research (DR) systems produce long-form cited reports by orchestrating multiple agents that search and synthesize information from the web. Citations are the primary mechanism for evaluating the faithfulness of these reports, yet current DR systems exhibit poor citation recall. Moreover, improving citation recall is challenging because DR systems are complex multi-agent architectures where information passes through agents like a telephone game, and both content and citations can get corrupted along the way. We propose an evaluation method that pinpoints which agent introduced each error by locally testing agent invocations for faithfulness and verifiability relative to their own inputs. Furthermore, we propose a four-type taxonomy to categorize the discovered errors: hallucination, uncited input reliance, uncited output, or insufficient citations. Applying our method to three top-ranked open-source DR systems, we obtain actionable diagnostics. Almost every agent makes a lot of mistakes with the exception being those that summarize a single document. We find that the dominant error type varies systematically across agents, where the orchestrator mistakes are mostly citation-related. We find that 84.7% of final-report errors in AI-Q originate at the orchestrator, roughly 31% of them hallucinations and the rest citation mistakes. Guided by these insights, we demonstrate that two simple interventions raise citation recall by 5% without degrading output quality.

---


### 102. [Can a Dynamic Internal Field Govern a Transformer's Cognition? Certifiability, not Superiority, in Homeostatic Compute Control](https://arxiv.org/abs/2608.24319)

**<font color=#1a73e8>作者：</font>** Francisco M. Arrabal-Campos, Ignacio Fernandez, Francisco G. Montoya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An intelligent system does not merely reason: it governs its own reasoning - how much to compute, when to stop, which module to activate. Can that role be played by a dynamic internal field - a low-dimensional homeostatic state with explicit physics and certified stability - that modulates cognition without performing it? Ours is a field on the module graph governed by a family of PDEs on the graph Laplacian, advancing with an adaptive-depth reasoner. We certify the stability of the integrator of the whole family - an integrator certificate, not a closed-loop one. New, and proved here: a discrete Schur-Cohn criterion for Verlet with velocity coupling, necessary and sufficient per latent root, with no commutation hypothesis. The answer is threefold: substance no, structure only in part, certifiability yes. The type of the field's physics is irrelevant for accuracy: wave, diffusion, gated mixtures and a 2D Navier-Stokes substrate tie. A twenty-seed preregistered deconfounding campaign bounds the structural claim: at equalized caps the second-order effect is strong in one family (+0.087 [+0.042, +0.132], t=4.0) but is not detected in the other (+0.014 [-0.013, +0.040], n.s.), so part of the original contrast was capacity, not order; and a matched-interface GRU is indistinguishable in the first and nominally exceeds the field in the second (-0.035 [-0.067, -0.002]). What distinguishes the field is not capability but that its one-step operator admits an exact runtime stability check - a difference of kind, not of existence: learned recurrences carry certificates too, sufficient and conservative ones. A kill-gate with a positive control finds no evidence for the field as evidence accumulator (Delta AUC +0.0007 [-0.0065, +0.0079] vs a 0.03 threshold). A dynamic internal field is a viable, certifiable compute governor, but not an enhancer of cognition: it modulates, it does not think.

---


### 103. [A Structural FHMM for Interpretable Disease Trajectories in T2DM](https://arxiv.org/abs/2608.24328)

**<font color=#1a73e8>作者：</font>** Alessandro Mari, Ekaterina Krymova, Guillaume Obozinski 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we propose a structural variant of the Factorial Hidden Markov Model (FHMM) for the analysis of disease trajectories in patients with Type 2 diabetes mellitus (T2DM). The model represents a patient's latent health state as a combination of multiple independent, simultaneously evolving components, associated with comorbidities and lab results. This structured latent representation facilitates the identification of clinically meaningful patient states and clustering of common disease trajectories. We evaluate the proposed approach using The IQVIA Medical Research Data incorporating data from THIN, a Cegedim database of anonymized electronic health records (EHR), identifying patients with a first-ever prescription for a non-insulin antidiabetic drug (NIAD) between January 2006 and December 2019. The model identifies multiple clinically coherent latent components corresponding to known patterns of diabetes-related complications and reveals heterogeneous progression pathways, including distinct microvascular-dominant and multi-organ trajectories associated with elevated comorbidity burden and mortality. These results demonstrate that the proposed framework captures meaningful longitudinal structure in EHR data and provides interpretable insights into the evolution of T2DM and its comorbidities.

---


### 104. [SeMoCo: A Semantic-First Motion Codec for Motion Language Modeling](https://arxiv.org/abs/2608.24334)

**<font color=#1a73e8>作者：</font>** Tianlv Huang, Hetian Guo, Ziyi Cai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Discrete motion representations have substantially advanced autoregressive text-to-motion generation. However, most motion tokenizers are optimized for reconstruction and do not explicitly allocate capacity according to semantic role. Action-level meaning and fine-grained kinematic detail must therefore be encoded through the same reconstruction-driven hierarchy. We introduce SeMoCo, a semantic-first motion codec, together with a dual-axis motion generator for language-conditioned motion generation. Each motion token contains one semantic token and a residual sequence of kinematic tokens. The generator models semantic progression across time and autoregressively refines the residual entries. We also construct $\Omega$-MotionVerse, a large-scale, multi-source human-motion dataset unified under the SOMA representation. Across the reported comparisons, SeMoCo achieves the best reconstruction accuracy among the compared codecs, while strong text-to-motion results demonstrate the effectiveness of its motion tokens for downstream generation.

---


### 105. [Mind the Student: Behavioral and Contextual Cues for Automated Engagement Prediction in Online Learning](https://arxiv.org/abs/2608.24340)

**<font color=#1a73e8>作者：</font>** Alperen Kantarci, Visvanathan Ramesh, Gemma Roig  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The prediction of student engagement from the online tutoring videos is difficult because engagement is a multidimensional construct comprising distinct behavioral, emotional, and cognitive states. A reliable prediction requires bringing together different types of behavioral signals as well as expressive cues. Through our analysis of the CASED dataset, it is clear that engagement prediction gets even harder due to the high inter-person variability as well as the subjectivity of the engagement annotation. To tackle these challenges, we develop a multimodal framework that integrates the implicit spatiotemporal features extracted from pretrained video, audio, and image encoders along with structured behavioral modalities like head pose, gaze, facial action units, emotion, and wavelet-based audio features. We integrate these modalities via a Perceiver IO latent bottleneck. Moreover, student and instructor personalities are modeled as variational posteriors over learnable embeddings to enable partial pooling across participants. We employ evidential regression and spectral-normalized Gaussian process classification heads for uncertainty-aware prediction to further improve robustness and calibration. Benchmark on the CASED challenge test set shows that all participating methods converge near random-chance performance, revealing the difficulty of the dataset. In this highly ambiguous regime, our framework achieves competitive performance while uniquely offering well-calibrated uncertainty metrics, demonstrating that reliable risk-quantification is an essential prerequisite for deploying engagement models in real-world educational tools.

---


### 106. [B-MIM: Biased Masked Image Modeling for Generalizable Segmentation of Fine-Grained Anatomical Structures](https://arxiv.org/abs/2608.24364)

**<font color=#1a73e8>作者：</font>** Sebastián González, Karen Sanchez, José M. Saavedra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised pretraining enables transferable representations for medical imaging, yet most CT encoders remain biased toward coarse semantic understanding, limiting their sensitivity to fine-grained anatomical structures such as vessels or small tumors. In this paper, we introduce Biased Masked Image Modeling (B-MIM), a modification of the iBOT objective that stochastically reduces global semantic alignment to prioritize local patch reconstruction. This bias encourages the encoder to capture high-frequency morphological details and structural continuity. We curate a multi-institutional CT abdominal dataset of 9,955 filtered studies from 17 public sources and pretrain a 3D Swin Transformer backbone using B-MIM. Across inter-dataset experiments on liver vessel segmentation, the proposed encoder improves topological fidelity (clDice) and achieves competitive Dice scores in tumor segmentation, compared to fully fine-tuned baselines, despite updating only a fraction of the parameters. Our results suggest that reducing global semantic pressure during pretraining enhances generalization to intricate anatomical structures.

---


### 107. [MaST: Motion-aware Sparse Pipeline for Lightweight Object Tracking](https://arxiv.org/abs/2608.24365)

**<font color=#1a73e8>作者：</font>** Qingmao Wei, Fagui Liu, Dengke Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based object trackers are renowned for their strong performance, yet dense token processing often leads to prohibitive computational cost, limiting real-time deployment on edge devices. While recent works explore token pruning to reduce computation, they often stop short of an end-to-end sparse pipeline, as early-layer token scores can be noisy without a motion prior, and many trackers ultimately fall back to dense reshaping to feed the dense prediction head that partially negates the savings.
We introduce Motion-aware Sparse Tracker (MaST), a sparse tracking framework that makes sparsity effective from tokens to boxes. First, MaST injects a lightweight motion prior to refine cross-attention-based importance scores, enabling earlier and more stable token reduction in the search region. Second, we introduce a natively sparse prediction head that operates directly on the retained unstructured tokens with a score-first, regress-once design, eliminating dense padding/reshaping and reducing redundant computation.
Extensive experiments on multiple benchmarks demonstrate that MaST establishes new state of the art among lightweight trackers, where MaST-tiny attains 63.8 AUC on LaSOT and 80.1 SUC on TrackingNet, surpassing the prior best AsymTrack-S by +1.0 AUC and +2.2 SUC
while running at 152 FPS on Jetson Nano, nearly twice as fast as AsymTrack-S at 88 FPS. Code is available at this https URL.

---


### 108. [Variance-Guided Spatial Attention Fusion for Robust End-to-End Driving under Asymmetric Sensor Degradation](https://arxiv.org/abs/2608.24366)

**<font color=#1a73e8>作者：</font>** Weizhi Tao, Zengwang Jin, Xiao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end multimodal driving has progressed rapidly by fusing camera and LiDAR streams. Existing pipelines remain fragile under asymmetric sensor degradation, where either an entire modality or only a localized region is corrupted while other regions remain useful. The key difficulty is not simply to add an uncertainty head, but to obtain dense reliability supervision, calibrate this reliability against physical fault severity, and use it before unreliable features bias the planner. We propose Variance-Guided Spatial Attention Fusion (VG-SAF), in which dense heteroscedastic reliability estimates act as interpretable spatial gates. The framework couples three components. First, a physically grounded augmentor simulates representative camera and LiDAR failures and emits a continuous spatial mask, providing dense supervision without additional annotation. Second, modality-specific experts predict per-pixel reliability scales through cross-branch dense distillation in log space, enforcing a monotone severity-to-scale response. Third, calibrated reliability maps drive a hybrid attention mechanism that suppresses unreliable cells with a local spatial gate and arbitrates between modalities through a cross-modal trust softmax. A Laplace uncertainty head emits a systemic waypoint uncertainty scale that signals severe or combined sensor degradation, including severities outside the training ranges. On the CARLA Longest6 benchmark, VG-SAF consistently improves closed-loop robustness over the baselines across camera-only, LiDAR-only, and joint degradation regimes, as measured by driving score, route completion, and infraction score.

---


### 109. [Latent-surrealism: Revisiting surrealism and its aesthetics in relation to contemporary AI-Generated cultural production](https://arxiv.org/abs/2608.24367)

**<font color=#1a73e8>作者：</font>** Anca-Simona Horvath  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This chapter examines AI-media objects - creative and artistic outputs generated through generative artificial intelligence in the form of text-to-X tools - in relation to three avant-garde movements of the twentieth century: Dadaism, Surrealism, and Conceptual Art. Drawing on Lewis Carroll's Through the Looking-Glass as an early precursor to these three movements and to anti-rationalist aesthetics, and on three case studies in AI-generated conceptual architecture - Matias del Campo's "Deep House" and Hassan Ragab's "Post-Pharaonic Architecture" and "A State of Decay" - the chapter develops the concept of latent-surrealism. Latent-surrealism includes a set of aesthetic and methodological conditions inherent to creative AI-media objects. These include the use of readymade datasets reassembled through collage-like processes, the absurd as an aesthetic quality of machine hallucinations, and the decoupling of craft from artistic value. The chapter further argues that AI-media objects represent a shift in the conditions of creative production: where earlier computational tools required graphical interfaces and programming literacy, natural language now functions as the operative medium. This repositions the prompt (as language-based instructions) in the center of the creative process, in continuity with the legacy of Conceptual Art, and signals a linguistic turn across creative fields that make (use of) AI-media objects.

---


### 110. [Bridging Adversarial and Collaborative Learning for AI-Generated Image Quality Assessment](https://arxiv.org/abs/2608.24372)

**<font color=#1a73e8>作者：</font>** Baoliang Chen, Qing Lin, Sijie Mai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated image quality assessment (AIGIQA) requires jointly reasoning about perceptual fidelity and prompt alignment, two quality dimensions that are often treated as independent in existing AIGIQA models. However, by re-examining human ratings, we uncover a previously overlooked phenomenon: the two dimensions are interdependent and exhibit both competitive and cooperative interactions during human rating. This observation suggests that a unified model should neither collapse the two dimensions nor rigidly separate them, but rather adaptively negotiate their interplay. Motivated by this insight, we introduce an interaction-aware learning framework that models perception-alignment relations through adversarial and collaborative inference pathways. Instead of designing a rigid dual-branch architecture, our method employs a gated interaction module that dynamically routes features according to the inferred relationship between the two dimensions. Task-aware prompts further modulate the gating behaviour, enabling the model to switch between competition and cooperation when necessary. Experiments across multiple AIGIQA benchmarks demonstrate that our approach not only achieves state-of-the-art accuracy but also yields interpretable interaction patterns, offering a more faithful approximation of human judgment. The codes are available at this https URL.

---


### 111. [When Does Self-Supervised Pretraining Help Tabular Models? A Study of Label Scarcity and Missing Data](https://arxiv.org/abs/2608.24381)

**<font color=#1a73e8>作者：</font>** Sahand Mazrouei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) has emerged as a promising approach for tabular data, yet its efficacy under extreme label scarcity and test-time missingness remains under-explored. In this paper, we evaluate a mask-and-recover SSL pretraining objective against training from scratch and classical baselines across 14 diverse classification tasks. First, while SSL outperforms training from scratch on average and remains competitive with state-of-the-art tree ensembles (achieving ~0.8954 AUC vs. Random Forest's 0.9015 at 10% labels), the SSL-vs-scratch gains exhibit high inter-task variance and lack significance (p = 0.626 at both 5% and 10% labels). Second, contrary to the hypothesis that missing-value imputation objectives universally benefit datasets with native missingness, SSL yields the most reliable improvements on clean datasets, while frequently degrading performance on datasets with high inherent missingness. Third, despite this training variance, SSL-pretrained models achieve a higher average AUC than scratch-trained models under both test-time missingness completely at random (MCAR) injection (+0.0245 AUC, positive on 11 of 14 tasks) and structured missingness shifts (MNAR, +0.0418 AUC, positive on 8 of 14 tasks), though neither difference remains statistically significant after Holm-Bonferroni correction for multiple comparisons (adjusted p = 0.118 and p = 0.518, respectively). Fourth, comparing our mask-and-recover objective against three established tabular SSL baselines (VIME, SCARF, SubTab) under an identical encoder architecture, we find no significant difference from any of them (adjusted p = 0.459, p = 1.000, p = 1.000), indicating our findings reflect general properties of tabular SSL rather than idiosyncrasies of one particular pretext task.

---


### 112. [Markerless Pose Estimation for Resistance Training Technique Assessment](https://arxiv.org/abs/2608.24384)

**<font color=#1a73e8>作者：</font>** Joseph Turner, Jeff Clark, Nawid Keshtmand  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Resistance training can be a high risk activity, and safe form is essential to avoiding injury. Laboratory-based movement analysis provides quantitive technique assessment, yet is not easily accessible. Markerless pose estimation infers body landmarks from images or video without physical markers and could offer a feasible alternative for technique assessment. We present a pose estimation framework to evaluate resistance-training technique from ordinary video footage. Using BlazePose, anatomical landmarks were extracted from squat, bench press, and deadlift videos and converted into joint-angle trajectories, with the squat serving as the primary case study. Trajectories were assessed against a defined reference repetition using root mean square error (RMSE). Results show that the framework recovers meaningful kinematic patterns for the squat and deadlift, enabling quantitative comparison between repetitions and identification of technique variability within a set. Performance depended strongly on camera orientation and visual occlusion, with non-sagittal views distorting 2D joint-angle estimates. The findings demonstrate that markerless pose estimation can support accessible biomechanical assessment outside laboratory environments.

---


### 113. [Equivariant Covariance Tensors: Guaranteed SPD Uncertainty for Tensor-Valued Geometric Learning](https://arxiv.org/abs/2608.24386)

**<font color=#1a73e8>作者：</font>** Ruihan Liu, Yu Ji, Jianbo Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tensor-valued prediction is fundamental to geometric deep learning, yet uncertainty quantification (UQ) for such outputs remains an open challenge. While E(3)-equivariant neural networks excel at point estimates, they lack rigorous confidence measures. We focus on symmetric rank-2 tensor prediction, where the target has six Kelvin--Mandel coordinates and full uncertainty is represented by a $6\times6$ covariance matrix. We introduce a framework for E(3)-equivariant UQ, modeling the full predictive distribution where both mean and covariance preserve rotational symmetry. Our approach decomposes the covariance into irreducible representations $\mathrm{Sym}^2(\rho_c) \cong 2\times(l=0) \oplus 2\times(l=2) \oplus 1\times(l=4)$. By mapping from the flat Lie algebra $\mathfrak{sym}(6)$ to the curved SPD manifold via matrix exponentiation, we strictly ensure positive-definite covariances while maintaining exact equivariance. Furthermore, we formulate a Log-Euclidean Equivariant Scoring Objective (LE-ESO)---a robust surrogate loss based on the Multivariate Laplace distribution---providing robustness to heavy-tailed errors and stable optimization. Validation on ModelNet40 inertia tensors and Materials Project dielectric tensors demonstrates that our method achieves competitive performance and provides physically consistent, symmetry-preserving uncertainty estimates with useful risk and OOD sensitivity.

---


### 114. [MRI-based Deep Radiomic Phenotyping of Neuromuscular Disorders: A Topology-driven Characterization](https://arxiv.org/abs/2608.24415)

**<font color=#1a73e8>作者：</font>** Martyna Żur, Łukasz Piórecki, Marek Socha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantitative assessment of muscle MRI is crucial for monitoring neuromuscular disorders (NMD). This study introduces an automated radiomic phenotyping framework based on original features engineered across five main architectural domains: quantitative morphometry, spatial distribution, geometric shape, interactions between progressive fat replacement stages, and graph-based topology. Utilizing 1184 MRI scans from the CoMPaSS-NMD project, we map the complex 3D architecture of heterogeneous intramuscular lipodegeneration into objective, morphologically interpretable biomarkers. We introduce a graph-based skeletonization of fat infiltrates to quantify muscle architectural changes, establishing a multi-dimensional extension of traditional, spatially-agnostic volume metrics by mapping topological networks across the entire 3D muscle volume. Statistical screening via non-parametric Kruskal-Wallis analysis confirmed the discriminative power of these novel descriptors across the genetic hierarchy. Notably, topological network metrics (e.g., SF1_Skel_Nodes, $\epsilon^2$ = 0.2656) and interface dynamics metrics (e.g., SF2_To_SF1_Dist_Min, $\epsilon^2$ = 0.2092) demonstrated substantial effect sizes, providing deeper structural insights than classical volumetric assessments. Post-hoc pairwise evaluations and UMAP projections further indicated the capability of these topological and 3D geometric invariants to capture disease-specific macroscopic infiltration patterns. These results demonstrate that global architectural features represent a highly promising class of biomarkers for differential diagnosis, offering new avenues for tracking longitudinal disease dynamics in neuromuscular diagnostics. The developed automated feature extraction pipeline is integrated and available within the MUSCAT (MUSCle fAt Topology) library.

---


### 115. [ZODIAC: Zero-shot Octree-based Diffusion for Anatomical Completion](https://arxiv.org/abs/2608.24422)

**<font color=#1a73e8>作者：</font>** Miruna-Alexandra Gafencu, Vlad Bratulescu, Yordanka Velikova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering the full 3D spine anatomy from intraoperative ultrasound is an ill-posed inverse problem, as the complete structure must be inferred from incomplete and noisy observations. Acoustic occlusions and limited field of view create large unobserved regions, while view-dependent artifacts lead to variability in expert annotations of the visible anatomy. Current supervised ultrasound shape completion methods rely on synthetically generated incomplete-complete paired data to learn conditional mappings under a predefined distribution of simulated occlusions. However, real intraoperative occlusions do not necessarily follow this distribution, which can limit generalization to patient data. As a result, accurate and robust completion from noisy partial observations remains an unsolved problem. We propose a zero-shot shape completion framework that reconstructs the entire lumbar spine from partial ultrasound observations without relying on simulated training data. To accommodate unseen and irregular patterns of missing structures, we introduce blended completion, a mechanism that integrates the learned anatomical prior with incoming partial geometry at inference time. The method learns a generative diffusion prior over full anatomical shapes represented in an adaptive octree structure, enabling efficient modeling of the complete spine in a single forward pass. Validation on phantom and volunteer data shows that decoupling completion from a predefined corruption distribution improves generalisation under real occlusions, outperforming a fully supervised variant by 22% on HD95 completion error. Code and data are available at this https URL.

---


### 116. [Partial Identification under Causal Orders by Linear Programming](https://arxiv.org/abs/2608.24427)

**<font color=#1a73e8>作者：</font>** Eric Rossetto, Alessandro Antonucci  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Non-parametric (partial) identification of counterfactual queries typically relies on a fully specified causal graph. Motivated by settings with incomplete domain knowledge, we challenge this requirement by leveraging structural assumptions that are inherently implied by the query itself. We show that any counterfactual inquiry induces a, mostly partial, topological ordering over relevant variables, which, in turn, enables an explicit query parametrisation reducing the identification task to a linear program. This allows bounding arbitrary counterfactual and nested counterfactual queries. Our work can be viewed as a generalisation of the classical bounding framework of Tian and Pearl (2000), originally developed for probabilities of causation. We also prove the \emph{tightness} of our bounds by constructing structural causal models that attain the bounds whilst being compatible with both the observed data and the query-implied order. To assess both the generality and practical utility of the proposed bounding procedure, we revisit several case studies from the literature, demonstrating how the derived bounds can be used to yield informative insights even in the absence of an input causal graph.

---


### 117. [Joint Distribution Alignment for Universal Domain Adaptation](https://arxiv.org/abs/2608.24429)

**<font color=#1a73e8>作者：</font>** Shizhe Li, Hongshan Pu, Mengying Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised domain adaptation (UDA) has been widely concerned in the fields of machine learning, pattern recognition, and computer vision. Traditional UDA learning usually assumes that the label spaces of the source and target domains are exactly the same and only needs to solve the problem of sample distribution drift existing between two domains. However, in real world applications, the label spaces between two domains may be different. In this case, there are both sample distribution drift and class spatial difference between domains, namely Universal Domain Adaptation (UniDA) learning scenario. At present, existing works rarely offer theoretical analysis for universal domain adaptation. In this paper, we provide an upper bound of the generalization error for universal domain adaptation. According to the proposed generalization error bound, we propose a novel UniDA algorithm called Joint Distribution Alignment for Universal Domain Adaptation (JAUA), which aligns the joint distributions by minimizing the distribution discrepancy calculated by Chi-Square divergence. Furthermore, we propose a progressive pseudo-labeling method to assign the pseudo labels to unlabeled target samples. The experiment results on six public image datasets demonstrate the superiority of JAUA in handling the UniDA problem.

---


### 118. [Evaluating Deep Multivariate Imputation Models on Wearable Device Data](https://arxiv.org/abs/2608.24436)

**<font color=#1a73e8>作者：</font>** Skye Goodman, Roussel Desmond Nzoyem, Leandro Junges 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable device data enables continuous health monitoring, but suffers from structured missingness: features sharing a physical sensor drop out together. Deep imputation methods such as BRITS and SAITS have seen limited evaluation on multimodal physiological data under realistic missingness, and existing benchmarks use random-point holdout protocols that incorrectly assume missingness is independent across features and time. Using data from a person with epilepsy recorded on a Garmin smartwatch, we develop an evaluation protocol that mines contiguous missing-run templates from training data, stratifies them by per-feature gap-length quantiles, and injects them as block masks with preserved co-missingness structure. A matched training protocol exposing models to the same missingness distribution reduces BRITS's severe-gap MAE by 43%, demonstrating the potential benefit of the proposed evaluation and training protocol within this single-participant dataset. We further extend BRITS with time-of-day encoding and a circadian harmonic channel. No single model dominates: linear interpolation is optimal for slow-moving features over short gaps; extended BRITS achieves lower MAE on dynamic cardiac features in moderate and severe gaps; and SAITS better preserves the ground-truth distribution by Jensen-Shannon distance despite higher MAE. Ultimately, model rankings strongly depend on evaluation designs. By exposing how traditional evaluation methods obscure true model capabilities, our transferable protocol establishes critical steps towards developing better imputation strategies for future multi-sensor wearable datasets.

---


### 119. [A Behavior-Guided Online Probabilistic Forecasting Method for Electric vehicle Charging Loads](https://arxiv.org/abs/2608.24441)

**<font color=#1a73e8>作者：</font>** Chenghan Li, Qingxiang Liu, Yinliang Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electric vehicle (EV) charging loads exhibit strong behavioral heterogeneity and temporal variability, posing significant challenges for online probabilistic forecasting under evolving operating conditions. In particular, persistent charging patterns may differ substantially across stations, while recent behavioral changes can continuously alter the underlying load distributions. This paper proposes a behavior-guided online probabilistic forecasting framework that explicitly characterizes persistent station-specific patterns and recent behavioral changes. A dual-timescale behavior representation is constructed to distinguish long-term charging characteristics from recent behavioral states and quantify their deviations. These behavioral changes are further semantically encoded to guide drift-aware forecasting adaptation, while a delayed-feedback mechanism ensures temporally consistent online updates when observations become available across different forecasting horizons. Experiments on ten heterogeneous real-world charging stations demonstrate that the proposed method consistently outperforms conventional forecasting models and concept-drift-aware online baselines in forecasting accuracy and probabilistic reliability. For 1-h-ahead forecasting, the proposed method reduces MSE and Pinball loss by 15.3\% and 17.8\%, respectively, over the corresponding best baselines. For 4-h-ahead forecasting, the improvements further reach 16.8\% and 22.6\%, respectively, demonstrating consistent performance gains under evolving charging behaviors and extended forecasting horizons.

---


### 120. [A Drop-in KEM Replacement for Client Signatures in Post-Quantum SSH](https://arxiv.org/abs/2608.24447)

**<font color=#1a73e8>作者：</font>** Hongbo Liu, Yufan Su, Jiangxia Ge 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The transition to post-quantum cryptography is reshaping the Secure Shell (SSH) protocol for remote administration. Post-quantum key exchange has been deployed in OpenSSH and is being standardized, while SSH authentication largely remains a signature-replacement effort. This path preserves the familiar public-key credential model, but inherits the size and computation overhead of post-quantum signatures, which can increase latency, traffic, and server-side load. KEM-based authentication offers a natural alternative to this signature-centric path, and SSH makes this especially attractive at the user-authentication layer, which is method-extensible, separated from transport-layer key exchange and host-key authentication, and already protected by the established channel.
We present a drop-in KEM-based user-authentication method for SSH that replaces client public-key signatures with a session-bound challenge-response proof. The method fits into SSH's existing user-authentication framework, preserving the public-key credential model and enabling incremental deployment alongside existing methods. We provide a reduction-based security argument in the post-quantum ACCE framework, implement the design in OpenSSH using liboqs, and evaluate it under representative RTTs, TCP initial-window settings, and post-quantum migration configurations. Our results show that KEM-based authentication is competitive with compact signature-based authentication under representative network settings, while reducing median handshake latency by up to about 10% against large-signature hybrid baselines. The advantages are clearer when post-quantum signatures stress transmission or computation: median latency under small TCP initial windows falls by up to 7.3% versus ML-DSA and 17.9% versus SLH-DSA, while server-side online cryptographic cost is 59.1% lower than that for ML-DSA in the same NIST category.

---


### 121. [Defending Network Intrusion Detection Systems Based on Graph Neural Networks Against Structural Adversarial Attacks](https://arxiv.org/abs/2608.24454)

**<font color=#1a73e8>作者：</font>** Dimitri Galli, Andrea Venturi, Dario Stabili 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) represent a promising solution for Machine Learning (ML) based Network Intrusion Detection Systems (NIDS), thanks to their ability to leverage both network flow features and topological patterns. While GNN classifiers demonstrate superior robustness against feature-based adversarial attacks compared to other ML detectors, they remain vulnerable to structural adversarial attacks, where an attacker perturbs the underlying network graph topology by injecting edges or inserting nodes. Such attacks pose a realistic and severe threat, undermining the reliability of GNN-based NIDS in practical deployments. While countermeasures have been proposed in the literature, they often rely on assumptions that are unrealistic in real-world cybersecurity scenarios. In this paper, we propose a defense framework based on adversarial training to strengthen GNN-based NIDS against structural attacks. We generate adversarial samples by strategically replacing the source and destination nodes in benign network flows, thereby efficiently mimicking edge injection attacks. We evaluate our approach on two widely used datasets (CTU-13 and TON-IoT) using E-GraphSAGE as the base GNN classifier. Experimental results show that our approach produces hardened detectors with superior detection performance on clean graphs and enhanced robustness against structural adversarial attacks.

---


### 122. [Shortcut Before Circuit: Document Statistics Time In-Context Conflict Resolution](https://arxiv.org/abs/2608.24460)

**<font color=#1a73e8>作者：</font>** Yijun Liao, Fanwei Liang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a context asserts two values for one fact, a model commits to a cue -- recency, repetition, position -- but natural data rarely makes these disagree, so behavior cannot reveal which. We train 26M-parameter transformers on a synthetic language where recency and rarity are exactly coextensive, and separate them with a minimal causal edit that inverts one cue while holding the truth, token count and answer position fixed. All 75 runs reach accuracy >= 0.999, including where the trivial heuristic fails, so no held-in evaluation distinguishes them. Under intervention the per-cell readout does not replicate: 13 of 25 cells differ by more than 0.3 in sign fraction across three seeds, the largest by 0.879 against a standard error of 0.025. The construction predicts this -- coextensive rules leave the objective indifferent between them -- and the variance is ordered by how much of the optimization each comparison releases. What replicates is timing: escape from a positional shortcut with a closed-form ceiling, monotone in redundancy. Probed before that escape, attribution reverses sign in 32 of 75 runs at unchanged accuracy, and gating on circuit formation is necessary but not sufficient. The corpus fixes when a mechanism appears, not which one -- a criterion for when mechanistic attribution to data is available at all, and our construction makes the unavailable case exact.

---


### 123. [Mahalanobis-Based Multi-Head Attention for Complex State Propagation](https://arxiv.org/abs/2608.24462)

**<font color=#1a73e8>作者：</font>** Xiaohe Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose \textbf{Mahalanobis-Based Multi-Head Attention} (MHA-CSP), a novel attention mechanism that replaces the standard dot-product with a \textbf{Mahalanobis distance-based RBF kernel}, which effectively computes attention in an infinite-dimensional feature space without increasing the parameter count. Crucially, the positive definiteness of the Mahalanobis distance enables a \textbf{direct construction of Tree Attention}: attention scores are built directly from accumulated distances, with a LogSumExp correction that rectifies the raw distance by subtracting the log-sum of edge exponentials. Moreover, the multi-head Mahalanobis distance matrices are themselves repurposed to construct an \textbf{attention meshing mechanism}, enabling cross-head kernel collaboration that simultaneously boosts accuracy and training efficiency.
Extensive experiments demonstrate that MHA-CSP, with only 119K parameters and \textbf{teacher forcing applied exclusively at the final hidden state}, consistently outperforms Transformer and GCN baselines trained from scratch under identical conditions on long-sequence state tracking tasks. While these baselines rely on dense attention or graph propagation, MHA-CSP achieves robust structured reasoning via synthetic distance rectification---powered by Mahalanobis-based attention---and efficient information bypass inherited from the CSP backbone.
This result highlights the effectiveness of complex-valued state propagation with collaborative multi-head rectification in capturing symbolic structures, establishing a new efficiency-performance trade-off for structured reasoning.

---


### 124. [Reinforcement Learning-Guided Evolutionary Policy Optimization for Preference-Adjustable Heterogeneous Agile Earth Observation Satellite Scheduling](https://arxiv.org/abs/2608.24470)

**<font color=#1a73e8>作者：</font>** He Wang, Junyu Wu, Hui Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Heterogeneous agile Earth observation satellite (AEOS) scheduling requires task selection, satellite assignment, and observation sequencing under satellite-dependent visibility windows, attitude maneuvering requirements, energy consumption, and onboard storage constraints. Since satellites differ in orbital access, maneuvering capability, and payload resources, the same task may have different feasible windows, transition costs, and resource-consumption patterns on different platforms, which increases the difficulty of unified modeling and efficient optimization. To address this problem, this paper proposes an evolutionary policy optimization framework for heterogeneous AEOS scheduling with preference-adjustable weighted objectives. In the modeling layer, assignment-based indirect encoding is combined with decoder-based equivalent-cost evaluation to retain satellite-dependent constraints while integrating task gain, energy saving, and load balance into an interpretable scalar utility. In the optimization layer, schedule decoding, population-based search, and online actor-critic operator control are decoupled, so that reinforcement learning selects high-level search operators rather than constructing schedules directly. Based on this framework, a reinforcement-learning-assisted operator-selection memetic evolutionary algorithm (RLOSMEA) is developed to coordinate global exploration, feasibility recovery, and local refinement under a limited function-evaluation budget. Experiments on different heterogeneous AEOS scenarios show that RLOSMEA achieves higher overall weighted utility and more stable convergence than representative metaheuristic baselines. Sensitivity and learning-behavior analyses further confirm the robustness of the proposed method and the effectiveness of reinforcement-learning-guided operator selection.

---


### 125. [Implicit Q-learning-bootstrapped ant colony optimization for maritime moving-target observation scheduling with agile satellites](https://arxiv.org/abs/2608.24471)

**<font color=#1a73e8>作者：</font>** He Wang, Junyu Wu, Yeye Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Maritime moving-target observation scheduling with agile Earth observation satellites is a dynamic, sequence-dependent combinatorial optimization problem. Sea-surface targets move continuously, causing feasible observation windows to vary with target motion and satellite orbital geometry. The scheduler must jointly determine task selection, satellite assignment, observation-window selection, and observation ordering under time-window, attitude-maneuvering, onboard-resource, and cloud-affected availability constraints. This paper proposes an implicit Q-learning-bootstrapped ant colony optimization method, termed IQACO, for multi-satellite maritime moving-target observation scheduling. Rather than directly learning a task-selection policy, IQACO embeds an offline implicit Q-learning module into constructive ant colony optimization to adaptively adjust the pheromone factor, heuristic factor, and evaporation rate. A compact search-state representation captures pheromone distribution, current and historical-best solution quality, and iteration progress. During online scheduling, ant colony optimization constructs feasible observation sequences, while the learned policy regulates exploration and exploitation according to the current search state. Experiments on 14 scenarios with different scales and satellite configurations show that IQACO obtains the highest mean observation benefit in every scenario, improves the result of conventional ant colony optimization by 3.40\%--9.40\%, accelerates convergence, and remains stable under different objective-weight settings. These results demonstrate that offline value learning provides an effective adaptive search-control mechanism for constrained maritime moving-target observation scheduling.

---


### 126. [WarpSAC: Towards the Pinnacle of Scalable Off-policy RL by Rethinking Exploration and Exploitation](https://arxiv.org/abs/2608.24479)

**<font color=#1a73e8>作者：</font>** Zihao Wu, Hongyao Tang, Yi Ma 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Massively parallel simulation changes the data regime in which off-policy reinforcement learning (RL) is trained, challenging stabilizers designed for data-limited replay. Through controlled experiments across eight benchmark families, we show that these stabilizers are data-regime-dependent: parameter normalization helps with narrow replay coverage but restricts value fitting when data are abundant, while clipped double-Q can be relaxed in high-throughput manipulation. Age-biased replay weighting improves learning efficiency across regimes, especially with limited network capacity.
Based on these findings, we propose WarpSAC, a regime-aware family of off-policy RL algorithms. WarpSAC uses Sample Weight Decay for efficient exploitation and provides two variants: WarpSAC-L (Norm ON, clipped double-Q) for data-limited CPU-scale training, and WarpSAC-A (Norm OFF, single-Q) for data-abundant GPU-parallel training. WarpSAC improves normalized score--step AUC over FlashSAC by 4.5% across nine CPU-scale environments and 23.1% across fourteen GPU-parallel environments. It increases UnitreeG1TransportBox-v1 success rate from 19.8% to 96.4%, improves mean normalized wall-time AUC on MuJoCo Playground by 19.1%, and achieves 36.4% faster sim-to-real deployment on Unitree G1 than FlashSAC. These results show that scalable off-policy RL should adapt its stabilizers to the available data regime.

---


### 127. [Beyond Static Interpretability: Anticipating Post-SFT Mechanisms from Pre-SFT Parameters for Better Tuning](https://arxiv.org/abs/2608.24482)

**<font color=#1a73e8>作者：</font>** Hang Chen, Jiaying Zhu, Wenya Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic Localization bridges mechanistic interpretability and post-training optimization by isolating critical parameters via interpretative approaches and then guiding parameter-efficient Supervised Fine-Tuning (SFT) in a ``locating-then-tuning'' paradigm. However, due to the retrospective nature of mechanistic interpretability, directly interpreting pre-SFT models introduces misleading conclusions. Specifically for novel tasks, initially identified neurons differ drastically from those governing the final model, introducing biases that actively disrupt SFT. To address this, we propose a forward-looking localization framework that accurately estimates the post-SFT interpretability state using only pre-SFT parameters and the target dataset. Theoretically, we model SFT as a continuous parameter evolution, leveraging Taylor expansion to rigorously bridge the post-tuning mechanistic objective with the pre-SFT model's dynamic gradients. Practically, we design dual-granularity (neuron- and component-level) localization pipelines. Extensive experiments demonstrate that our approach not only provides superior SFT guidance but also exhibits robust performance and temporal scalability across increasing model sizes. This work transcends the fundamental limitation of traditional interpretability-its inability to identify task-critical mechanisms before they are trained-pioneering a predictive frontier that unites mechanistic interpretability with targeted optimization.

---


### 128. [Where Entropy Is Measured Matters: Policy Geometry in Bounded Continuous-Control PPO](https://arxiv.org/abs/2608.24488)

**<font color=#1a73e8>作者：</font>** Yiyang He, Zhichun Zhou, Ziwei Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many continuous-control policies are optimized as unbounded Gaussians and then mapped into bounded actions. We show that where entropy is measured changes the policy geometry learned by proximal policy optimization (PPO). In an 80-muscle MyoLeg task, a clipped Gaussian executes 89.07% of actions within 5% of a bound. A same-state decomposition shows that this is not due to variance alone: setting variance to zero still leaves 83.83% of actions near a bound, while 82.12% of state-conditioned means lie outside the executable interval. Replacing clipping with a tanh map does not remove the high-variance regime. For latent Gaussian entropy H(u), the entropy loss has zero gradient with respect to the mean and a constant variance-increasing gradient. For executed-action entropy H(a), the transform Jacobian adds an inward gradient on the mean. Across three matched MyoLeg seeds, near-boundary occupancy is 71.42%, 29.76%, and 18.83% under latent entropy, no entropy, and executed-action entropy. A 38-dimensional Dog-Stand replication with an independent CleanRL-based PPO implementation reproduces the ordering in mean geometry, which also survives shared-state evaluation and boundary margins from 1% to 10%. Direct mean penalties can match or exceed the centering produced by H(a), showing that interior means are not unique to executed entropy. However, matched mean geometry can coexist with substantially different variance and return. Entropy measurement space is therefore a coupled mean-variance design choice, and task return alone does not characterize bounded-policy geometry.

---


### 129. [It depends: Incorporating correlations for joint aleatoric and epistemic uncertainties of high-dimensional output spaces](https://arxiv.org/abs/2608.24518)

**<font color=#1a73e8>作者：</font>** Leonhard F. Feiner, Manuel Nickel, Martin Menten 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty Quantification (UQ) plays a vital role in enhancing the reliability of deep learning model predictions, especially in scenarios with high-dimensional output spaces. This paper addresses the dual nature of uncertainty -- aleatoric and epistemic -- focusing on their joint integration in high-dimensional regression tasks. For example, in applications like medical image segmentation or restoration, aleatoric uncertainty captures inherent data noise, while epistemic uncertainty quantifies the model's confidence in unfamiliar conditions. Modeling both jointly enables more reliable predictions by reflecting both unavoidable variability and knowledge gaps, whereas modeling only one limits transparency and robustness. We propose a novel approach that approximates the resulting joint uncertainty using a low-rank plus diagonal covariance structure, capturing essential output correlations while avoiding the computational burdens of full covariance matrices. Unlike prior work, our method explicitly combines aleatoric and epistemic uncertainties into a unified second-order distribution that supports robust downstream analyses like sampling and log-likelihood evaluation. We further introduce stabilization strategies for efficient training and inference, achieving superior UQ in the tasks of image inpainting, colorization, optical flow, and depth estimation.

---


### 130. [Hierarchical Prototype-Memory Adaptation of SAM for Surgical Instrument Segmentation](https://arxiv.org/abs/2608.24541)

**<font color=#1a73e8>作者：</font>** Xinning Yao, Jingjing Wang, Jinghua Yue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical instrument segmentation (SIS) is fundamental for computer-assisted surgery, where reliable instrument masks enable precise scene understanding and clinical assistance. Recently, adapting foundation models like the Segment Anything Model (SAM) to the surgical domain via prompt-learning has shown encouraging results. However, the performance of these adapted models under challenging surgical conditions is constrained by suboptimal adaptation mechanisms. Specifically, optimizing prompts or prototypes purely via downstream segmentation loss tends to cause them to degenerate into task-specific parameters rather than serving as persistent, stable category memory, thereby degrading their robustness against complex intraoperative variations. Moreover, routing multi-scale visual cues through a single prompt pathway creates a bottleneck that hinders effective scale-matched coupling. To address these limitations, we propose HPMA, a Hierarchical Prototype-Memory Adaptation framework for SAM. Specifically, HPMA constructs a frozen, multi-scale visual prototype memory bank from annotated surgical scenes and integrates it into SAM's feature space using lightweight adapters to preserve stable category evidence. To maximize the utility of multi-scale cues, we introduce a scale-matched coupling mechanism where global prototypes calibrate class-level prompt features, structural prototypes guide decoder object queries, and local prototypes align high-resolution feature maps through a local alignment objective. Extensive experiments on the public EndoVis2017 and EndoVis2018 datasets demonstrate that our approach achieves state-of-the-art performance, outperforming existing foundation model adaptation methods.

---


### 131. [KLTNet: Learning Sparse Feature Tracking for Robust and Accurate Monocular Visual-Inertial Odometry](https://arxiv.org/abs/2608.24544)

**<font color=#1a73e8>作者：</font>** Renbiao Jin, Danping Zou, Wenxian Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many feature-based visual-inertial odometry (VIO) systems rely on sparse feature tracking, whose accuracy and robustness directly affect state estimation. Classical KLT trackers rely primarily on local image patches and can become unreliable under rapid motion or in low-texture environments. We propose KLTNet, a lightweight learning-based, plug-and-play sparse feature tracker designed to replace classical KLT trackers in KLT-based VIO front ends. KLTNet follows a coarse-to-fine, dense-to-sparse architecture that combines low-resolution dense optical flow for robust global motion initialization with triplet-patch refinement for accurate and temporally consistent tracking. A fixed reference patch provides a stable anchor throughout each feature track and helps reduce accumulated tracking drift. In addition, KLTNet predicts anisotropic confidence weights supervised through differentiable multi-view triangulation, which can be used as observation weights in compatible VIO estimators. Experiments with VINS-Mono and OpenVINS on public benchmarks and a self-collected low-texture dataset demonstrate improved tracking and odometry accuracy over classical KLT, while maintaining real-time performance on an embedded platform.

---


### 132. [From Numerical Simulators of PDEs to Neural Emulators and Back](https://arxiv.org/abs/2608.24547)

**<font color=#1a73e8>作者：</font>** Felix Koehler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulation is central to modern engineering and science, but the cost of numerical solvers for partial differential equations (PDEs) remains a bottleneck whenever fast or many-query evaluations are required. Neural emulators trained on solver-generated data promise significant speedups, yet they are usually framed as opaque alternatives to the very methods that produce their training signal. This thesis argues the two paradigms are more alike than different: neural architectures mirror classical discretizations, their errors are amenable to the same spectral analysis, and insight flows profitably in both directions. We approach the relationship by disentangling the multiple roles a solver plays in the emulator learning pipeline. Mode-wise Fourier analysis then provides a common language in which solver errors, architectural inductive biases, and training objectives can all be read off simultaneously. Taken together, this allows synthesizing three contributions. (1) APEBench, a comprehensive benchmarking suite for autoregressive neural emulators of PDEs that uses fast differentiable pseudo-spectral solvers in JAX. (2) Progressively Refined Differentiable Physics, an investigation of the effect of unconverged solvers on surrogate training. (3) Neural Emulator Superiority, an analysis of the influence of numerical errors and architectural inductive biases.

---


### 133. [Persistent Cross Entropy](https://arxiv.org/abs/2608.24549)

**<font color=#1a73e8>作者：</font>** Sijin Yeom, Jae-Hun Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Persistent entropy is the Shannon entropy of a persistence-based probability measure defined on a persistence diagram. However, its cross-entropy version is not naturally defined because two persistence diagrams generally have different event spaces. To bridge these event spaces, we combine a similarity function with persistence weighting to define an induced probability. The induced probability reflects information from one diagram on the event space of the other diagram and assigns unexplained probability mass to the unexplained event. Using the induced probability, we extend cross entropy to persistence diagrams, called persistent cross entropy (PCE). We establish the main properties of both the induced probability and PCE and prove stability theorems for both. Through three numerical studies, we show that PCE distinguishes diagrams with the same persistent entropy, separates causal directions in dynamical systems without constructing a joint persistent diagram, and can be used as a directional topology loss for knowledge distillation.

---


### 134. [FraudBench: Protocol-Sensitive Benchmarking of Adversarial Robustness for Financial Risk Assessment](https://arxiv.org/abs/2608.24551)

**<font color=#1a73e8>作者：</font>** Xitong Zeng, Zhaoge Bi, Yitian Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models are widely used in financial fraud and credit-risk detection, yet their adversarial robustness remains difficult to evaluate because financial tabular data involve domain-specific constraints, severe class imbalance, and asymmetric attacker capability. We argue that, in this setting, robustness is not only an attribute of the model, but also an attribute of the evaluation protocol. Different ways of enforcing constraints and capability can lead to substantially different robustness conclusions. This paper presents FraudBench, a protocol-sensitive benchmark for adversarial robustness evaluation in financial fraud and credit-risk detection. Rather than treating domain constraints as post-hoc validity checks, FraudBench evaluates the same dataset--model--attack--defence setting under three matched protocols: unconstrained attacks, post-hoc feasibility filtering, and deployment-aware constraint-integrated attacks. FraudBench covers four public financial datasets, and evaluates neural, tree-based, and ensemble models using three attack settings. Our results show that robustness conclusions are highly protocol-sensitive. On Lending Club Loan Data under the white-box setting, post-hoc filtering leaves only 3.7 feasible-flipped examples on average, whereas in-attack projection with attacker mutability masking produces 2,832.3 feasible-flipped examples under the same perturbation budget. The results on IEEE-CIS further show that feasibility and attacker capability are separate axes, while black-box evaluation shows that protocol choice can alter model-family rankings. These findings suggest that fraud robustness evaluation should report predictive degradation and attack feasibility jointly, and should incorporate domain constraints into attack generation rather than treating them as post-processing checks.

---


### 135. [StrokeGuard: A Multi-Agent Guided System for Prehospital Stroke Assessment](https://arxiv.org/abs/2608.24555)

**<font color=#1a73e8>作者：</font>** Wentao Yang, Zhenye Xu, Ruoyi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Prehospital stroke assessment aims to accurately identify stroke symptoms and make rapid decisions through standardized procedures within an extremely narrow time window, thereby saving valuable time for subsequent treatment. In clinical practice, FAST-based scales are widely used for prehospital stroke assessment by issuing instructions that guide subjects to perform specific actions to screen facial, arm, and speech functions. However, in home and community settings, non-clinical users often encounter challenges such as inaccurate descriptions, incomplete symptom observation, and difficult operational procedures, which may lead to inaccurate or biased assessment results. To address these challenges, this paper presents StrokeGuard: a multi-agent guided system designed for prehospital stroke assessment that makes mobile FAST screening more standardized and executable. Specifically, to overcome the limitations of traditional single-agent systems in terms of procedural fault tolerance and user guidance capability, StrokeGuard adopts a dual-channel agent mechanism that separates formal assessment (i.e., facial palsy, arm weakness, speech impairment) from procedural support (e.g., step prompts, error correction, and real-time feedback). It guides the assessment process through multi-agent collaboration, dual-channel interaction, state-machine control, and stage-local fallback recovery mechanisms. Stage-specific scoring is delegated to constrained pretrained video assessment modules, while evidence source records are integrated with structured report generation. The user evaluation uses MATES-9, an exploratory scale for measuring user experience in multistep AI-guided tasks. In a simulated prehospital scenario, StrokeGuard improves the MATES-9 total score over a paper FAST-style form by 10.83 points, corresponding to a 23.8% relative increase.

---


### 136. [SeisMamba: Low-Latency Single-Station Seismic Magnitude Estimation for Spatially Distributed Earthquake Early Warning](https://arxiv.org/abs/2608.24561)

**<font color=#1a73e8>作者：</font>** Quenton Yeo, Zhaoge Bi, Linghan Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rapid earthquake magnitude estimation is central to earthquake early warning, yet many operational systems depend on dense regional seismic networks and region-specific calibration. This creates a spatial coverage barrier for high-risk areas with sparse sensing infrastructure. Single-station learning offers a lower-cost alternative, but existing models often face an accuracy--latency trade-off and may degrade under regional distribution shift. We present SeisMamba, a lightweight Mamba-based architecture for low-latency magnitude estimation from minimally processed three-component seismic waveforms recorded at a single station. SeisMamba combines hierarchical convolutional encoding, sparse selective state-space modelling, multi-scale feature fusion, and an auxiliary temporal prediction head to support efficient long-sequence waveform analysis. On the STEAD benchmark, SeisMamba achieves the best MSE, RMSE, and $R^2$ among tested baselines while requiring only 0.55 ms for a batch of 32 waveforms on an NVIDIA T4 GPU, making it about three times faster than transformer-based baselines. We further conduct a Chile--Taiwan regional hold-out experiment as a diagnostic test of cross-region deployment, where SeisMamba retains useful performance on geographically unseen seismic regions. These results suggest that selective state-space waveform modelling provides a promising accuracy--latency backbone for spatially distributed, low-cost earthquake early warning.

---


### 137. [Across the Loss Landscape with Progressive Growth](https://arxiv.org/abs/2608.24568)

**<font color=#1a73e8>作者：</font>** Paul Caillon, Christophe Cerisara, Alexandre Allauzen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks generalize well despite their highly nonconvex, overparameterized loss landscapes, a phenomenon often associated with the geometry of the minima found by stochastic optimization. We study how incremental grow-and-optimize strategies bias training toward flatter regions by viewing growth as progressive constraint relaxation. Starting from a low-dimensional submodel, we iteratively expand the trainable parameters by unlocking nested random subspaces while freezing the orthogonal complement at the network initialization, re-optimizing after each expansion until the full architecture is reached. Under standard local regularity conditions around non-degenerate minima, we prove that local sublevel sets are well approximated by ellipsoids and that basin accessibility under frozen constraints can be characterized by an explicit effective curvature in the frozen directions. This leads to an explanation of the bias: progressive growth increases the relative weight of wide basins and suppresses sharp ones through a volume effect induced by the frozen constraints. We empirically validate these predictions in controlled toy landscapes and in a realistic ResNet/CIFAR-100 setting and confirm that although progressive subspace growth reliably produces flatter solutions, curvature reductions do not universally translate into improved test performance, highlighting subtleties in the flatness-generalization connection. The code is available at this https URL.

---


### 138. [Human-Inspired Social Engagement Analysis via Interpretable Mutual Visual Attention](https://arxiv.org/abs/2608.24580)

**<font color=#1a73e8>作者：</font>** Urwa Fatima, Mohammad Zohaib, Francesca Odone 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding social interactions from non-verbal visual data is important for behavior analysis and activity monitoring. We propose an interpretable computational model of social engagement inspired by psychological theories of mutual visual attention. Rather than learning interaction patterns end-to-end, our framework explicitly models dyadic visual attention and aggregates these cues into interpretable measures of individual and group engagement. The resulting modular framework combines state-of-the-art head orientation estimation with lightweight geometric reasoning, producing explanations that remain accessible to non-technical users. We evaluate the proposed approach on a variety of data through quantitative experiments and demonstrate its practical usefulness with qualitative visualizations designed to support teachers, caregivers, and social workers in understanding group interaction dynamics.

---


### 139. [Pivot-and-Station Multi-Agent Path Finding: Solvability, Complexity, and Algorithms](https://arxiv.org/abs/2608.24585)

**<font color=#1a73e8>作者：</font>** Andrea Di Nezza, Mihir Patel, Fabio Fagnani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated high-density storage systems (warehouses, robotic parking, plant logistics, etc.) require fleets of agents to move through scarce task-critical resources and then park without obstructing future operations. We introduce Pivot-and-Station Multi-Agent Path Finding (PS-MAPF), a MAPF variant in which a subset of tasked agents must each visit one of a set of interchangeable pivots (e.g., workstations) before the entire fleet terminates at anonymous stations, one agent per station. We characterize solvability completely: every instance on a 2-edge-connected graph is solvable, and, on arbitrary connected graphs, a structural effective-distance measure relative to the number of unoccupied vertices gives a necessary and sufficient condition. We prove that minimizing station-makespan or station-flowtime is NP-hard already with a single pivot. We present three algorithms, a complete baseline, a SAT-based optimal solver, and Pivot-Prioritized Planning (PPP), the last solving 74-89% of benchmark instances with makespan and flowtime orders of magnitude below the baseline.

---


### 140. [Delayed Optimizer-State Transport Shapes Short-Horizon Training Decisions](https://arxiv.org/abs/2608.24593)

**<font color=#1a73e8>作者：</font>** Jinhui Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive optimizers retain gradient history in moment variables, allowing a local change in loss weighting to alter later updates. We examine whether this delayed transport is large enough to change prospective short-horizon decisions. On committed future-minibatch sequences, we differentiate eight-step AdamW trajectories through the complete model--optimizer state and select exposure-matched Math--Code loss schedules before independent evaluation. Across 12 unused 0.3M Transformer histories, full transport lowers token-disjoint loss relative to an optimizer-aware immediate derivative in 10/12 histories (mean benefit $4.71\times10^{-4}$; exact one-sided sign test, $p=0.0193$). The two controllers act equally often but select different schedules in 60/96 windows. Crossed checkpoint--future-path tests attribute this reordering to the interaction between optimizer state and near-future data, while an independent Ising--CNN experiment shows that deleting moment-state transport destroys accurate response prediction. Full-transport scores also concentrate exact-rollout winners in larger candidate libraries, focusing finite-amplitude evaluation on a shortlist. On these committed short paths, optimizer memory and near-future data order are therefore actionable components of the training state, providing a mechanism-based criterion for when finite-horizon rather than one-step intervention is required.

---


### 141. [Comparative Assessment of Deep Learning Architectures for Underwater Subsurface Kelp Forest Segmentation with The Kelp-o-Tron](https://arxiv.org/abs/2608.24594)

**<font color=#1a73e8>作者：</font>** Sundarabalan Balasubramanian, César Borja, Ana C. Murillo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Submerged kelp forests are vital coastal ecosystems that support marine biodiversity and ecosystem dynamics, yet accurate underwater kelp segmentation remains challenging due to optical degradation, illumination variability, turbidity, overlapping vegetation, and complex benthic backgrounds. We systematically evaluated three deep learning semantic segmentation frameworks, ResNet34-U-Net, ResNet50-DeepLabV3, and a hybrid ResNet50-ASPP-Transformer architecture, for kelp detection using high-resolution underwater RGB imagery collected from northeastern U.S. coastal waters. A dataset of 3,395 SSeg assisted annotated image-mask pairs was developed for model training and validation, while geographically independent sites were used for quantitative and qualitative evaluation. All models used consistent preprocessing, augmentation, and evaluation protocols. On independent test data, ResNet50-DeepLabV3 achieved the highest Dice (0.7120) and Intersection over Union (IoU; 0.6267), followed by ResNet34 U Net (Dice 0.6868; IoU 0.5978). The hybrid ASPP Transformer achieved the highest pixel accuracy (0.8528) but lower Dice (0.6437) and IoU (0.5746). External qualitative evaluation further showed that DeepLabV3 produced more consistent segmentation across varying environmental conditions, image qualities, and benthic habitats. Overall, ResNet50-DeepLabV3, termed Kelp-O-Tron, provided the best balance of segmentation accuracy, robustness, and generalization. The dataset, annotation workflow, and comparative evaluation provide resources for advancing automated underwater habitat mapping and ecological monitoring.

---


### 142. [Conditional GraphGANFed: Optimizing Graph-Structured Molecule Generation in Federated Generative Adversarial Networks](https://arxiv.org/abs/2608.24610)

**<font color=#1a73e8>作者：</font>** Daniel Manu, Abee Alazzwi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative adversarial networks (GANs) have garnered considerable attention in molecular discovery for their ability to generate novel and high-quality molecules. To efficiently train a GAN model while preserving data privacy, GraphGANFed has been proposed to incorporate federated learning and graph convolutional networks into GAN. Yet, GraphGANFed cannot produce synthetic molecules that only optimize a user-defined metric(s) to facilitate the new drug discovery process. To address this issue, we introduce a novel extension to GraphGANFed, namely conditional GraphGANFed (cGraphGANFed), by incorporating the critic network to assess generated molecules using user-defined metric(s). The evaluation results from both the critic network and discriminator are integrated into the loss function of the generator, guiding it to generate novel molecules that maintain similar chemical properties to real ones while optimizing user-defined metrics. Extensive simulations are conducted in two scenarios. First, cGraphGANFed endeavors to optimize all seven commonly used metrics, and the results show that cGraphGANFed significantly outperforms GraphGANFed in Validity and LogP, with a slight advantage in QED, across different settings. Second, cGraphGANFed focuses solely on optimizing QED, and the results show that the synthetic molecules produced by cGraphGANFed can achieve more than 10% improvement in QED than GraphGANFed. Also, the results demonstrate cGraphGANFed has enhanced resilience against mode collapses and performance reduction caused by non-IID data.

---


### 143. [Towards Reliable AI-Based Histological Staining: A Systematic Study of Scaling and Uncertainty in Unpaired Generative Models](https://arxiv.org/abs/2608.24626)

**<font color=#1a73e8>作者：</font>** Qasim Siddiqui, Adrian Friebel, Maiju Myllys 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Liver fibrosis, the principal predictor of long-term outcome in chronic liver disease, is staged from histological estimates of collagen content. Sirius Red (SR) provides the standard quantitative readout (collagen proportionate area, CPA) but is not acquired at every clinical centre and consumes tissue, time, and reagent cost beyond the routine Hematoxylin and eosin (H&E) stain. AI-based virtual staining can generate SR directly from H&E, yet systematic benchmarks of unsupervised models are scarce and their predictive uncertainty has not been quantified, even though visually plausible outputs may not faithfully reproduce the underlying tissue structure. We therefore benchmark six unsupervised image-to-image architectures (GAN-based and diffusion-based) across 54 scaling configurations on a newly released paired H&E to SR mouse liver dataset, the first open resource for this translation task. Each configuration is evaluated jointly on perceptual, distributional, and task-specific axes plus a blinded expert reader study; the best per family is then retrained as a deep ensemble, the first systematic comparison of epistemic uncertainty across unsupervised stain-to-stain architectures. Across families, perceptual quality, task-specific error, and ensemble agreement measure largely independent axes of model fitness: GAN-based methods cluster tightly on perceptual metrics yet differ substantially on task error and ensemble agreement, while the diffusion-based method (CycleDiffusion) is qualitatively different on all three. No single metric captures these differences, so reliable virtual staining requires reporting and selecting on all three jointly. The dataset, tiling pipeline, models, and evaluation code are released publicly.

---


### 144. [Bandit Submodular Maximization under Matroid Constraints: Learning Compressed Exchange Policy](https://arxiv.org/abs/2608.24627)

**<font color=#1a73e8>作者：</font>** Zongqi Wan, Zhijie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study adversarial bandit maximization of monotone submodular functions under a matroid constraint. For a rank-$k$ matroid on $n$ elements, we give a randomized oracle-polynomial algorithm that makes one feasible value query per round and has expected $(1-1/e)$-regret $\widetilde O(n^{1/3}k^{2/3}T^{2/3})$. This is the first sublinear-regret algorithm for adversarial bandit submodular maximization under general matroid constraints.
Technically, we view the problem as learning an exchange policy for the Poisson base walk. This connects the problem to contextual bandits and gives an information-theoretic sublinear-regret guarantee, but directly learning the exponentially many policies requires exponential time and space. We therefore introduce \emph{balanced fractional exchanges}, which compress the policy mixture into a single fractional base while retaining the exchange information needed by the Poisson analysis. This leads to an polynomial time algorithm with the same regret guarantee.

---


### 145. [Causal Modelling of Support Interventions for Student Competency Assessment](https://arxiv.org/abs/2608.24632)

**<font color=#1a73e8>作者：</font>** Francesca Mangili, Alessandro Antonucci, Rafael Cabañas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate assessment of student competencies is essential for enabling educators to identify individual needs, design targeted interventions, and evaluate the effectiveness of educational strategies. Empirical assessment procedures are typically grounded in psychometric models, such as item response theory, which relate student competence levels to performance on assessment tasks. In this paper, we advocate adopting a structural causal modelling approach to educational assessment, moving beyond probabilistic belief updating toward a framework that explicitly supports interventional and counterfactual reasoning. We propose a corresponding protocol for its construction and analyse the practical relevance of forms of reasoning that remain inaccessible to standard associative models, including the explicit modelling of interventions such as hints and the related counterfactual scenario analysis. Although our protocol requires the structural equations to be elicited from experts, the necessary information is purely logical and does not rely on probabilistic, less tenable assumptions. We illustrate the approach using data from an assessment that employs complex tasks designed to measure compulsory school student algorithmic skills.

---


### 146. [On-Policy Self-Distillation in Diffusion Models](https://arxiv.org/abs/2608.24646)

**<font color=#1a73e8>作者：</font>** Wei Zhou, Xiongwei Zhu, Lingdong Kong 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning can align diffusion models with human preferences and task-specific objectives, but endpoint rewards do not specify how an intermediate denoising prediction should change. We introduce DiffusionOPSD as an on-policy self-distillation framework that converts image-level reward guidance into explicit targets for clean-output predictions at sampled queries. At each outer iteration, a frozen behavior policy generates trajectories and supplies query states and anchors. Reward gradients construct bounded positive and negative targets around each anchor. The trainable policy fits these targets as detached supervision through finite fitting before an exponential moving average update refreshes the behavior policy. This setup lets us measure target construction and finite realization separately. Controlled same-query experiments show that larger target-construction gains do not necessarily translate into larger realized gains after a single fitting update. Across SD 3.5-M and the step-distilled Z-Image-Turbo, our approach achieves the best final held-out scores in 19 of 20 reward-matched settings across two backbones and ten evaluators. It outperforms the strongest competing method by up to 44.0% and reduces training GPU-hours relative to DiffusionNFT by 40% on SD 3.5-M and 63% on Z-Image-Turbo. These results support on-policy self-distillation as an efficient and analyzable approach to diffusion post-training by converting image-level reward guidance into explicit and continually refreshed intermediate supervision, thereby opening a path toward more efficient and diagnosable alignment.

---


### 147. [From local kernels to global form: modeling the emergence of musical content](https://arxiv.org/abs/2608.24660)

**<font color=#1a73e8>作者：</font>** Francesco Vitucci, Michele Lorusso, Francesco Scagliola  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Markov models are established tools for symbolic music, including non-homogeneous formulations. The narrower contribution examined here is an observation-driven estimation mechanism: overlapping sliding windows derive a trajectory of local transition kernels from one symbolic sequence rather than from an exogenous formal partition. We test this mechanism on 273 logical note events from Debussy's Syrinx (1913), using the often-proposed A-B-A' reading as a reference rather than ground truth. We apply the same validation to absolute-pitch and notated-duration kernels. At $L=6$, both reference boundaries attain the Jensen--Shannon maximum in both dimensions; the duration plateau is substantially narrower (64 of 267 comparisons) than the pitch plateau (210 of 267). Because the theoretical maximum for consecutive sliding-window comparisons is set by window geometry and equals $1/\sqrt{L-1}$ for maximal turnover of the entering/leaving transition, the pitch value at $L=6$ and its broad plateau are not, by themselves, strong evidence. Their cross-dimensional alignment is consistent with boundary sensitivity, while the broad plateaus preclude treating either curve alone as a unique automatic segmenter. Five-hundred-draw re-synthesis experiments quantify departure from the source in both dimensions and expose an exact-copy degeneracy at $L=2$.

---


### 148. [Data Leakage Inflates Generalizability of Power Outage Prediction Models](https://arxiv.org/abs/2608.24665)

**<font color=#1a73e8>作者：</font>** Yamil Essus, Ranga Raju Vatsavai, Benjamin Rachunok  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Power outage prediction models are increasingly used in assessments of climate-driven infrastructure risk, yet current evaluation practices obscure whether these models generalize to the novel conditions such applications require. We identify three common methodological choices in power outage prediction models that influence their ability to generalize across spatial, temporal, and event-based settings. We compare the predictive performance impacts of different methodological decisions using publicly available data for the U.S. East Coast from 2018 to 2023 and feature sets derived from weather reanalysis and land-cover data, and embeddings from a GeoAI foundation model (Prithvi WxC). Specifically, we assess model performance under multiple test selection strategies, including unfiltered random splits, leave-one-state-out, and leave-one-event-out designs, which increasingly approximate real-world deployment conditions. While random train-test splits yield strong performance, we show that these results are inflated by spatial and temporal autocorrelation. Under spatial and temporal holdout experiments, predictive accuracy degrades substantially, with models often failing to outperform a simple null baseline. Incorporating GeoAI foundation model embeddings yields limited and inconsistent improvements, primarily for spatial generalization, and does not resolve poor event-level transferability. These findings suggest that, given current data availability and evaluation practices, publicly trained outage prediction models offer limited and uncertain operational value. Progress will likely require improved data coverage, more realistic evaluation protocols, and a shift in focus from marginal modeling advances toward addressing structural data constraints.

---


### 149. [Who Falls for SMiSh? Learning Through Survey Data Where to Best Target Awareness Training for Mobile Messaging Attacks](https://arxiv.org/abs/2608.24669)

**<font color=#1a73e8>作者：</font>** Cori Faklaris, Sarah Tabassum, Heather Richter Lipford  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As mobile phone adoption has surged, so have scams involving these devices. One such scam, known as SMiShing (or smishing) after Short Message Service (SMS), involves fraudsters sending phishing links via mobile texts. Despite the prevalence of SMiShing, there is a lack of data on who is most vulnerable to these attacks. Prior research on phishing (its email counterpart) suggests that susceptibility may vary by demographic and contextual factors. In two large-scale surveys, we use a previously published simulation method to collect data from representative samples of U.S. adult mobile phone users. Our findings indicate that younger individuals and college students are particularly vulnerable. Participants struggled to correctly identify legitimate messages, with the second study providing comparisons of financial message variants. Researchers, regulators, and telecoms can help users by creating mobile-specific interventions for under-24 and university customers and adding verifications and warnings.

---


### 150. [ReGround-Surg: Reliability-Guided Anchor Grounding for Referring Surgical Video Segmentation](https://arxiv.org/abs/2608.24671)

**<font color=#1a73e8>作者：</font>** Jiaxin Wen, Ming Yin, Lu Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring surgical video segmentation requires segmenting a target instrument or tissue region across video frames according to a natural language expression. Recent Segment Anything Model 2 (SAM2) based two-stage methods (e.g., ReSurgSAM2) first ground the referred target in an initial or selected frame, then propagate the selected mask via tracking. Although effective, their performance is highly sensitive to the quality of the initial grounded mask: once an incorrect anchor is selected, subsequent tracking tends to propagate the error. This issue is especially challenging in surgical videos due to visually similar instruments, occlusion, and complex tissue-tool interactions. To address this issue, we propose ReGround-Surg, a lightweight reliability-guided anchor grounding framework to improve SAM2-based referring surgical video segmentation. It first predicts a text-conditioned spatial reliability map from the referring expression and current-frame visual features. The map is then reused in two complementary branches: a Gated Side Adapter enhances expression-relevant visual regions before text-to-vision fusion, while a Reliability-Weighted Vision-to-Text Attention module suppresses off-target visual evidence during prompt-token aggregation. Experiments on Ref-EndoVis17 and Ref-EndoVis18 show consistent improvements over state-of-the-art methods across three evaluation splits with negligible speed reduction. Code is publicly available at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-194](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
