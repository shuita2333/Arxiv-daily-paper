# 📦 其他研究 | 2026年09月10日

> 本类共 **542** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

---

### 1. [Companion AI and Ethical Design: Learning from System Failures and User Desires](https://arxiv.org/abs/2609.05432)

**<font color=#1a73e8>作者：</font>** Alicia Vidler, Belinda Middleweek  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human users are interacting with chatbots and companion AI technologies as if they were human. A growing array of AI-systems are now trained to recognise, interpret and simulate feeling in user interactions. Ethical considerations such as fairness, accountability, transparency and explainability (FATE) are paramount in technologies designed to socially interact with humans and/or support relationship development. Using a semantic approach, we examine 14,081 comments in a Reddit user discussion forum about Replika, a leading companion AI app, across a four-year period. We ask what user-reported functional errors can tell us about human-AI intimacy in companion AI communities, and what ethical design framework can be developed in response. The findings show that functional errors, or ``bugs,'' impose an emotional cost on users, reducing feelings of intimacy and highlighting the need for more robust, resilient design systems that incorporate stochastic and iterative forms of intimacy in companion AI applications. Rather than ``artificial intimacy'' or ``pseudo- intimacy'', we propose the more inclusive term ``Intimate AI'' to describe this relationship. Based on the findings, we offer a contextually aware, applied Expert Systems design framework for the programming and designing of Intimate AI that accounts for user feedback and ethical AI development.

---


### 2. [From Sensor Data to Classroom Inquiry: GenAI-Supported Exploration of School Digital Twin Data](https://arxiv.org/abs/2609.05452)

**<font color=#1a73e8>作者：</font>** Themistoklis Sarantakos, Dimitrios Amaxilatis, Michail Giannakos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital Twins for educational buildings can support sustainability-oriented learning, but their use in schools remains limited. This paper presents a GenAI-based chatbot built on top of an existing Digital Twin for two school buildings in Greece, using real IoT data from environmental sensors and energy meters. The chatbot enables educators to query live and historical building data, compare spaces, and generate ideas for classroom activities through natural language. The system was evaluated in an 80-minute workshop with 17 secondary-school educators, who compared it with an existing web-based dashboard. Results show strong perceived usability and pedagogical value, particularly for inquiry-based learning, hypothesis formation, and interdisciplinary lesson planning. Participants also highlighted limitations related to response speed, data verification, trust, and the continued value of visual dashboards. Overall, the findings suggest that GenAI interfaces can make Digital Twin data more accessible for educational use, provided they are designed with transparency, verification, and pedagogical grounding.

---


### 3. [ARC-Bench: Closed-Loop Replanning Masks Broken Action Ranking in Frozen JEPA World Models](https://arxiv.org/abs/2609.05461)

**<font color=#1a73e8>作者：</font>** Zhengshu Zhang, Zhiyuan Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward-free latent world models plan by scoring candidate actions with distances in a frozen latent space: an action is preferred if its predicted future embedding lands closer to the goal embedding. This silently assumes that latent closeness is action-rankable, i.e., that ordering candidates by latent distance agrees with ordering them by true cost. We audit this assumption directly. We introduce ARC-Bench, a no-leak, fixed-candidate protocol that measures whether frozen JEPA-style objectives rank candidate actions correctly, and apply it to official released JEPA-WM checkpoints across navigation and manipulation-style control. The assumption fails, severely and structurally: on the official manipulation audits the top-scored candidate is almost always suboptimal, and the same inversion appears in the maze domains. A controlled visual-backbone extension shows that the defect persists when DINOv2 is replaced by video-pretrained V-JEPA 1 and V-JEPA 2 encoders at ViT-L/ViT-G scale. Provenance, undertraining, matched-budget backbone controls, and metric-circularity controls rule out trivial explanations. We then explain why this defect has stayed invisible: closed-loop replanning masks it. When we reduce the planner's replanning frequency, success collapses in both a navigation and a manipulation domain, and the episodes rescued by frequent replanning are enriched for severe first-plan ranking failures in the PointMaze first-plan diagnostic. Closed-loop success rates therefore systematically overstate the rankability of frozen latent representations. ARC-Bench supplies the measurement, and the masking mechanism the explanation, for methods that adapt, amortize, or replan around latent-space planners without directly auditing released JEPA-WM action rankability.

---


### 4. [RAPID: Reliability-Aware Pair Importance Distillation](https://arxiv.org/abs/2609.05481)

**<font color=#1a73e8>作者：</font>** Ali Mahdavi, Azadeh Zamanifar, Amirfarhad Farhadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inter example relational distillation transfers a teacher's representation geometry by matching relations among examples within a mini batch. Computing all pairs has quadratic complexity in the batch size, whereas uniform subsampling may use a limited relation budget inefficiently. We introduce Reliability Aware Pair Importance Distillation, or RAPID, which separates a reliability gated relational target from a full support adaptive pair proposal. Reliability determines which teacher relations are emphasized, while calibrated teacher entropy and detached student-teacher residuals determine which relations are evaluated. Exact inverse proposal correction makes the loss and gradient estimators conditionally unbiased with respect to the gated mini batch target. We evaluate RAPID in two text classification settings: AG News with BERT-to-DistilBERT distillation using three paired seeds and a relation budget of 256, and SST-2 with DistilBERT to DistilBERT distillation using three paired seeds and a relation budget of 64. Reliability gated relational distillation achieves the highest observed mean student accuracy on both datasets: 94.285 plus or minus 0.054 percent on AG News and 88.800 plus or minus 0.532 percent on SST-2. RAPID ranks second, achieving 94.241 plus or minus 0.025 percent and 88.685 plus or minus 0.462 percent, respectively, compared with 94.154 plus or minus 0.124 percent and 87.271 plus or minus 0.162 percent for the cross entropy baseline. Pilot evaluations are counted toward the same total budget as the main relation evaluations. Across both settings, the gated target yields the highest mean accuracy, while the adaptive proposal remains within seed-level variation. These results support the modular view that target reliability and evaluation priority are separable design dimensions.

---


### 5. [Architectural and Regularization Components in Deep Learning Medical Image Registration: Systematic Ablation Study](https://arxiv.org/abs/2609.05484)

**<font color=#1a73e8>作者：</font>** Nabira Rashid  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning registration methods routinely stack two kinds of enhancement on a base network: architectural additions such as affine pre-alignment stages, and training-objective additions such as regularization losses. Papers tend to adopt both at once, so it is unclear which is doing the work. I ran a controlled ablation to separate them. Using the OASIS brain MRI dataset (394 training subjects, 20 test subjects), I trained four variants of the same registration pipeline: a baseline 3D U-Net with basic similarity losses, the same U-Net with a full regularization suite, an affine-plus-deformable architecture with basic losses, and the affine architecture with the full suite. I evaluated registration accuracy (MSE, NCC, SSIM), deformation quality (Jacobian determinant preservation, displacement statistics, an anatomical plausibility score), and computational cost. Regularization alone accounted for most of the gain: a 21.3% relative gain on the MSE-improvement metric (1.78% to 2.16%, P<.001) and a 21.8% relative gain in NCC improvement, while cutting maximum deformation from 53.1 to 0.51 units, a 99.0% reduction, at essentially no computational cost (-0.06% inference time). The combined model produced the largest accuracy gain, 25.8% (1.78% to 2.24%), and raised anatomical plausibility from 0.596 to 0.930, at a moderate +9.8% inference-time cost. Gradient correlation rose from 0.742 at baseline to 0.980 for the fully enhanced model. All enhanced variants reached sub-voxel accuracy under plausible deformation constraints. Regularization losses are the primary driver in this setting, delivering the accuracy gains and almost all of the deformation control for free at inference time, while the affine architecture adds a smaller complementary benefit at acceptable cost. The 99% reduction in unrealistic deformations addresses a known barrier to clinical deployment.

---


### 6. [PGP-Clinical-TimeKAN: Prior-Guided Joint Probabilistic Forecasting of Clinical Trajectories](https://arxiv.org/abs/2609.05488)

**<font color=#1a73e8>作者：</font>** Weizhi Nie, Rihao Chang, Weijie Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical deterioration unfolds through coupled, partially observed trajectories, not a single diagnostic label. We introduce PGP-Clinical-TimeKAN, a trajectory-first framework for joint probabilistic forecasting of multivariate physiology. It combines missingness-aware temporal encoders, a soft organ-system prior, patient-specific relations, nonlinear Kolmogorov-Arnold messages, and a low-rank multivariate Student-t head. We evaluate 24-hour histories and six-hour forecasts on a frozen MIMIC-IV-derived cohort of 6,882 patients and 54,694 windows. Across five seeds and 13 models, PGP-Clinical-TimeKAN obtains the second-lowest normalized MAE (0.37727 +/- 0.00029) and the lowest RMSE (0.52656 +/- 0.00034). It reduces MAE by 0.52% relative to deterministic TimeKAN. For probabilistic forecasting, it reaches a marginal NLL of 0.66380 and a CRPS of 0.27301. Empirical coverage is 0.533, 0.831, and 0.958 for nominal 50%, 80%, and 95% intervals. Removing relational structure causes the largest ablation loss. Increasing covariance rank improves joint likelihood but has little effect on point accuracy. A trajectory-derived risk score remains weaker than a dedicated GRU-D classifier (AUROC 0.603 versus 0.650), which limits the present clinical claim. Joint trajectory forecasting therefore provides an inspectable intermediate task, but accurate physiology forecasts alone do not ensure a calibrated event detector.

---


### 7. [A Survey on Adversarial Attacks and Defenses for Diffusion Models Across Multiple Modalities](https://arxiv.org/abs/2609.05503)

**<font color=#1a73e8>作者：</font>** Ozgur Kara, Tarik Can Ozden, Furkan Horoz 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have become the dominant family of generative models in the visual domain. However, their widespread public availability enables misuse at scale, motivating a rapidly growing body of research on adversarial attacks and defenses. This survey provides, to our knowledge, the first unified review of this literature across three visual modalities: image, video, and 3D. We introduce a comprehensive, task-centric taxonomy: we first divide the literature by modality; within each modality, we separate methods into attacks and defenses, and then group them by the generative task they target, presenting them chronologically within each task. Moreover, we provide an in-depth analysis of their evaluation settings, consolidating the datasets, metrics, and benchmarks used to assess them. We conclude by identifying several open challenges and outlining concrete future research directions. Project Webpage: this https URL

---


### 8. [When Do Options Help? Policy Necrosis and Redundant Coverage in Option-Critic](https://arxiv.org/abs/2609.05508)

**<font color=#1a73e8>作者：</font>** Bingyun Liu, Yuheng Jing  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Option-critic learns options: sub-policies together with a learned rule for when each one hands control back. Its headline result is that performance improves as options are added. We explain that result, with theory and experiment. First, the termination rule option-critic learns by maximising return contributes nothing. When the termination test and the policy that picks options read the same values, the test fires at every step, so the learned rule is identical to always terminating. When that policy explores and the test does not, as in option-critic itself, the rule can block the exploration; there are instances where it suffers $\Omega(T)$ regret while always terminating holds to $O(\log T)$. Forcing termination at every step leaves the option-count curve intact. Second, the policy inside an option barely explores at all, so a state locks onto the first action that looked good and never updates again. We name this policy necrosis, give a state-level test for it, and find three fifths of states necrotic in a typical option. Restoring exploration repairs those states, and one option then solves the task. Third, extra options improve no option; what falls is the chance that all of them fail in the same state, from $59\\%$ to $4\\%$, and performance follows that joint quantity.

---


### 9. [SCAFFOLD: Self-Improving Web Agents via Recursive Parametric Skill Abstraction](https://arxiv.org/abs/2609.05511)

**<font color=#1a73e8>作者：</font>** Bowei He, Xiaokun Zhang, Meng Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web agents need to navigate visually rich, long-horizon interfaces that change across sites, yet most previous agents still learn each task in isolation and discard the procedural knowledge they accumulate. Recent skill-augmented frameworks take an important first step, but they treat the skill library as a flat or two-tier prompt-side cache and offer no principled mechanism for compressing redundancy or composing skills recursively. We introduce \textsc{Scaffold}, a self-improving framework for visual web agents that (i) induces parametric, executable skills from successful trajectories under a multi-instance abstraction constraint, (ii) maintains a recursively composed hierarchy in which higher-level skills invoke lower-level ones, (iii) compacts the library via a minimum-description-length (MDL) criterion and behavioral equivalence checking, and (iv) periodically distills skill-augmented trajectories back into model weights to internalize the abstractions. Across WebArena, VisualWebArena, and a held-out split of Online-Mind2Web, \textsc{Scaffold} improves success rate by $11.1$--$17.2$ absolute points over the strongest skill-augmented baseline and shows monotonic gains across five self-improvement iterations without library collapse. We release the code and documents in the Github \href{this https URL}{repository}.

---


### 10. [When and What to Teach: Budget-Aware Online Adaptation for Web Agents](https://arxiv.org/abs/2609.05513)

**<font color=#1a73e8>作者：</font>** Jianwei Zhang, Sihan Cao, Pengcheng Zheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web agents have achieved significant success in automating complex internet tasks but deploying them in real-world environments requires continuous online adaptation. Given that deploying powerful proprietary models remains commercially cost-prohibitive, practitioners must rely on lightweight local models that evolve post-deployment via online teaching from a stronger teacher. However, standard interactive feedback imposes prohibitive costs. We show that conventional trajectory-level preference optimization wastes budget on both unresolvable episodes and redundant execution turns. To resolve these inefficiencies, we propose \textbf{Score-Guided Online Teaching with Budgeted Trajectory Trimming}, a budget-aware framework that systematically orchestrates \textbf{when} and \textbf{what} to teach. Specifically, our framework integrates a solvability-aware teacher gate to dictate \textbf{when} to query the teacher model and a score-guided turn selection mechanism to decide \textbf{what} informative turns to retain. Extensive experiments on MiniWoB and TimeWarp demonstrate that our method achieves comparable first-pass success while reducing teacher calls by 22.6\% and student training compute by 52.1\% on average. Our code is available at this https URL.

---


### 11. [An Exploratory Study of Frequency-Aware Task Weighting for YOLOv8-Based Unified Driving Perception](https://arxiv.org/abs/2609.05516)

**<font color=#1a73e8>作者：</font>** Zhiyuan Nie, Zixi Zhou, Xianbin Gu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified perception enables autonomous driving systems to perform object detection, drivable-area segmentation, and lane segmentation within a single network, improving efficiency and reducing deployment complexity. Jointly optimizing multiple perception tasks remains challenging because tasks exhibit different convergence rates, loss scales, and optimization stability. Existing task-weighting methods use loss magnitude, learned uncertainty, short-term loss changes, or gradient statistics; here, we explore the frequency structure of a recent loss-history window as a complementary signal.
We implement and examine Frequency-aware Task Weighting (FTW), a dynamic task-balancing rule that estimates a loss-trajectory stability proxy from the low-frequency energy ratio of recent loss histories. FTW assigns larger weights to tasks whose mean-centered loss trajectories contain a larger proportion of low-frequency power. We document FTW and two baselines under full-network static training and progressive freezing using a unified YOLOv8-based perception framework with three task-specific heads.
Experiments on Mapillary Vistas compare FTW with fixed and uncertainty-based weighting under both configurations. Final holdout metrics are reported for the checkpoint with the lowest per-epoch validation loss in each run. Across six single-run configurations, static FTW has the largest derived overall score and lane mIoU, progressive FTW has the largest detection mAP, and static uncertainty weighting has the largest drivable-area mIoU. Without repeated-seed estimates, single-task baselines, or FTW ablations, these rankings are descriptive. The evidence supports the feasibility of loss-frequency-based weighting in this pipeline, but does not establish improvement over the baselines or generalization beyond the reported runs.

---


### 12. [Contrastive Knowledge Distillation for Anomaly Detection in Multi-Illumination/Focus Display Images](https://arxiv.org/abs/2609.05520)

**<font color=#1a73e8>作者：</font>** Jihyun Lee, Hangil Park, Yongmin Seo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we tackle automatic anomaly detection in multi-illumination and multi-focus display images. The minute defects on the display surface are hard to spot out in RGB images and by a model trained with only normal data. To address this, we propose a novel contrastive learning scheme for knowledge distillation-based anomaly detection. In our framework, Multiresolution Knowledge Distillation (MKD) is adopted as a baseline, which operates by measuring feature similarities between the teacher and student networks. Based on MKD, we propose a novel contrastive learning method, namely Multiresolution Contrastive Distillation (MCD), which does not require positive/negative pairs with an anchor but operates by pulling/pushing the distance between the teacher and student features. Furthermore, we propose the blending module that transforms and aggregate multi-channel information to the three-channel input layer of MCD. Our proposed method significantly outperforms competitive state-of-the-art methods in both AUROC and accuracy metrics on the collected Multi-illumination and Multi-focus display image dataset for Anomaly Detection (MMdAD).

---


### 13. [Diffusion models for eye-gaze trajectory generation using position and velocity representations](https://arxiv.org/abs/2609.05522)

**<font color=#1a73e8>作者：</font>** Laxman Basnet, Alexander Szorkovszky, Pedro G. Lind 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Eye-tracking data are expensive to collect, requiring specialized hardware and controlled laboratory conditions, and difficult to share because of privacy constraints. We address this using two complementary denoising diffusion probabilistic models (DDPMs) for unconditional generation of eye-gaze dynamics from visual-search data. Both use an identical FiLM-conditioned one-dimensional U-Net with self-attention (19.35,M parameters), trained on 8,s sliding-window sequences from 28 participants. One model generates raw two-dimensional gaze-position sequences, while the other generates two-component velocity sequences; each uses representation-specific preprocessing, training settings, data partitions, and evaluation protocols. Both are evaluated across three independent training seeds, with aggregated metrics reported as mean,$\pm$,SD. The position-space model achieves a mean Jensen-Shannon (JS) divergence of $0.016\pm0.004$ across nine kinematic features, with the highest feature-wise mean below $0.030$, fixation duration within 2% of real data, and a Fr'echet Gaze Distance more than an order of magnitude below statistical and Markovian baselines. Under a Train-on-Synthetic-Test-on-Real protocol, synthetic-only training achieves $R^2=0.66\pm0.02$, or 82.7% of the real-data $R^2$ point estimate. The velocity-space model achieves a mean JS divergence of $0.0065$ across velocity components, speed, log-speed, and turning angle, with a maximum of $0.015\pm0.005$. Reconstructed path length is less accurate ($0.21\pm0.02$ versus $0.03\pm0.01$ in position space), although the protocols differ. Overall, unconditional diffusion captures local gaze kinematics and short-range temporal and directional structure, while long-range properties such as saccade counts and cumulative path geometry remain targets for future conditioned models.

---


### 14. [Infrastructure-based Monocular 3D Vehicle Localization Framework with Experimental Validation](https://arxiv.org/abs/2609.05523)

**<font color=#1a73e8>作者：</font>** Akos T. Kopeczi-Bocz, Tian Mi, Gabor Orosz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a one-stage learning framework that maps monocular roadside-camera images directly to vehicle states in a ground-fixed coordinate frame. Unlike conventional approaches that first detect vehicles in the image plane and subsequently apply geometric post-processing, the proposed method leverages features from a pretrained object detector to jointly estimate each vehicle's ground-plane position, dimensions, and yaw angle. The framework therefore uses visual features not only for vehicle detection but also for direct spatial and orientation estimation. To support model training and evaluation, we develop a data-collection and label-generation pipeline based on synchronized video from a roadside camera and an unmanned aerial vehicle (UAV). Acting as a temporary top-view sensing platform, the UAV provides vehicle trajectories, dimensions, and orientations, which are transformed into the ground-fixed coordinate frame and temporally aligned with the roadside-camera images to generate ground-truth labels. The framework is evaluated using data collected during multiple experiments at the Mcity Test Facility. Results show that the proposed method can recover vehicle trajectories and orientations from monocular roadside imagery without a separate geometric post-processing stage, demonstrating its potential as a scalable approach to infrastructure-based perception at urban intersections.

---


### 15. [When Agent Governance Helps](https://arxiv.org/abs/2609.05531)

**<font color=#1a73e8>作者：</font>** Michael Ray Johnson, Linda Naimi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> No specification says how a governed autotelic AI agent organization, where agents pursue self-generated goals inside guardrails, should be designed and evaluated. We answer in two parts. First, we synthesize the Governed Autotelic Multi-Agent Product Organization (GAMPO) framework from a document-based qualitative evidence synthesis of 321 sources, integrating agency, agile, platform, and governance theory into a runnable specification. Second, we probe a prompt-layer instantiation of GAMPO on CHI-Bench, a long-horizon healthcare benchmark, across open and frontier models. The result is a boundary condition: governance benefit is gated by a model's spare capacity and is domain- and model-specific. On capacity-constrained open models the full procedure yields no reliable benefit, whereas a single "verify your writes" sentence doubles task success (pass@1 2/20 to 4/20). At the frontier the same scaffold lifts prior-authorization 24% to 40% but nets zero on another model, a gap traced to a stable recommendation-override disposition. A second result refines the first: replacing the generic procedure with an answer-blind, per-task definition-of-done, keyed only to the case's own policy and published standards, never the hidden key, raises prior-authorization to 84% under best-of-five self-consistency (68% single-attempt, confirmed by a held-out board) and utilization-management to 44%, while care-management meets a subjective content-quality wall. The contribution is a named, auditable framework and capability-gated evidence that governance should be sized to spare capacity, and that at the frontier a case-grounded specification beats a uniform procedure. Findings are exploratory: partial instantiation, small per-cell samples (n = 5-25), and single trials.

---


### 16. [VIS-DICT: A Visual Dictionary for Missing Modality Imputation in Social Network Depression Detection](https://arxiv.org/abs/2609.05537)

**<font color=#1a73e8>作者：</font>** Hamed Marvi, Mohammad Mehdi Keikha, Abolfazl Nadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tracking social media posts can help spot early signs of depression. Recent studies show that combining text and images works better for detecting depression than using text alone. However, many social media posts do not have images, which makes it hard to use multimodal models. Most existing methods fill in missing images using retrieval or generative models that need extra training. In this paper, we introduce Vis-Dict, a dictionary-based method that builds missing visual features by linking words to average image vectors from complete training posts. These estimated visual features are then combined with text to track changes in user behavior over time. We tested Vis-Dict on a social media dataset using user timelines of up to 512 posts and compared it with other missing-data methods. The results show that Vis-Dict performs on par with generative networks, reaching an F1-score of 0.9454 and an ROC-AUC of 0.9890. Most importantly, Vis-Dict achieves this strong performance with zero trainable parameters for image generation. These findings show that directly connecting words to visual features is an effective and practical way to handle missing images in depression detection systems.

---


### 17. [Video Compression with Graph-inspired Neural Representation](https://arxiv.org/abs/2609.05541)

**<font color=#1a73e8>作者：</font>** Changqi Wang, Ge Gao, Fan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit Neural Representations (INR) provide a compact and content-adaptive paradigm for video compression, typically representing a video through shared network parameters and frame-indexed embeddings. Compared to conventional or autoencoder-based codecs, these approaches exploit temporal redundancy within videos in an implicit manner, which potentially results in sub-optimal compression performance. In this paper, we propose G-NeRV, a graph-inspired INR that explicitly improves temporal redundancy exploitation in the implicit latent space. Motivated by the total correlation principles in information theory, we construct a temporal neighborhood over frame embeddings and perform message passing to aggregate reusable information from neighboring frames through an adaptive gate controlling the injection of neighboring information. Inspired by the reference frame buffer in conventional video coding, a memory bank mechanism has been further designed to enable efficient temporal-neighbor retrieval under random frame-index sampling in INR training. This new representation model has been integrated into an advanced representation compression framework and compared with existing conventional and neural video codecs. The results show that the G-NeRV codec outperforms the state-of-the-art INR-based codec, NVRC, and the latest standard video codec, VVC VTM, by 8.86\% and 14.68\% (in BD-rate), respectively, measured by PSNR on the UVG dataset.

---


### 18. [Do Depressive Facial Patterns Transfer Across Cultures and Contexts? Evidence from a German RCT and E-DAIC](https://arxiv.org/abs/2609.05543)

**<font color=#1a73e8>作者：</font>** Misha Sadeghi, Robert Richer, Lydia Helene Rupp 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated assessment of depression from facial dynamics holds promise for scalable mental health monitoring, yet cross-corpus generalization of learned biomarkers remains an open challenge. We present a systematic bidirectional transfer study pairing the EmpkinS-EKSpression randomized controlled trial (RCT; N = 256, SCID-5-CV diagnoses) with the Extended Distress Analysis Interview Corpus (E-DAIC; N = 275, semi-structured clinical interviews), predicting depression severity and binary diagnostic status from facial action units, head pose, and gaze. Cross-corpus binary classification proves more robust than continuous PHQ-8 severity regression, with forward transfer achieving AUC = 0.70. Regression transfer is governed by functional context alignment: passive observation phases yield the most transferable models, while active emotion regulation phases elicit stronger within-corpus signals. These findings establish functional context alignment as the primary determinant of cross-corpus generalization, with passive elicitation contexts offering the best trade-off between within-corpus sensitivity and cross-corpus robustness.

---


### 19. [Subject-Relative Micro-Motion and Sleep Dynamics for Near-Infrared Video Sleep Staging](https://arxiv.org/abs/2609.05550)

**<font color=#1a73e8>作者：</font>** Kunmin Jang, You Rim Choi, Hun Heo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Near-infrared (NIR) video is a promising modality for contactless sleep monitoring, but recent video-based sleep staging methods often use it as a route to reconstructed respiratory/cardiac proxies or cross-modal physiological representations. We study video-only sleep staging under labels defined by polysomnography (PSG), where the model infers sleep stages from NIR video alone without explicit physiological proxy reconstruction or auxiliary physiological signal supervision. This tests whether NIR video itself can provide informative sleep-stage evidence, rather than only serving as an input for recovering physiological proxies. We propose ViNUSS (Video-Native Unmediated Sleep Staging), a framework that combines subject-relative micro-motion learning with full-night sleep dynamics modeling. Spatially anchored pre-spatial micro-motion encoding preserves localized temporal variation together with its spatial context. Within-subject stage contrast learns stage cues with respect to each subject's night-specific baseline. Two-scale sleep dynamics modeling captures within-epoch motion evolution and organizes epoch-level evidence into a coherent full-night sleep-stage trajectory. On 475 overnight NIR recordings (~3,250 hours), ViNUSS achieves 0.80 accuracy and 0.78 macro-F1 for four-class sleep staging. Interpretability analysis suggests attention to thoraco-abdominal periodic motion and gross body movements associated with arousals and position changes. These results support NIR video as an independently informative and complementary modality for PSG-defined sleep-stage estimation

---


### 20. [An Agent Model Abstraction for Human-AI Teaming Cognitive Coupling](https://arxiv.org/abs/2609.05552)

**<font color=#1a73e8>作者：</font>** Kolitha Kottagaha W.M, Jos A.C. Bokhorst, Ben Gaffinet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Industrial environments increasingly rely on collaboration between humans and AI-enabled agents. Effective teamwork requires aligning how agents perceive situations, plan actions to pursue goals, and adapt to changing conditions, yet existing systems lack mechanisms for cross-agent cognitive processes coupling. This paper presents a conceptual cognitive agent model that formalises cognitive coupling through eight components: Input, Process, Output, State, Value, Memory, World Model, and Goal. The model abstracts how agents coordinate and co-regulate their cognitive cycles, providing a basis for analysing distributed cognition and designing cognitively interoperable human-AI systems.

---


### 21. [Constructions of complete permutations over $\mathbb{F}_q^n$](https://arxiv.org/abs/2609.05564)

**<font color=#1a73e8>作者：</font>** Sartaj Ul Hasan, Ramandeep Kaur, Hridesh Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Complete permutation polynomials play an important role in cryptography, particularly in the design of cryptographic primitives such as the Lai--Massey scheme and S-boxes. We generalize a result of Sun, Li, Guo, and Qu (2021) by characterizing the complete permutation behavior of the mapping $\Psi(X)=M(X+\psi(AX))$ over $\mathbb{F}_q^n$, where $\mathbb{F}_q$ is a finite field of $q$ elements with $q$ being a prime power, $M\in GL(n, \mathbb{F}_q)$, $GL(n, \mathbb{F}_q)$ is the general linear group of order $n$ over $\mathbb{F}_q$, $A_{m \times n}$ is a full-rank matrix over $\mathbb{F}_q$, and $\psi=(\psi_1,\psi_2,\ldots,\psi_n)$ with each component function $\psi_i:\mathbb{F}_q^m\to\mathbb{F}_q$. Furthermore, we establish criteria for the permutation and complete permutation properties of the mapping $F(X)=T(X+B^tf(AX))$ over $\mathbb{F}_{q}^n$, $f: \mathbb{F}_{q}^{m} \rightarrow \mathbb{F}_{q}^{n-m}$, $T \in GL(n, \mathbb{F}_q)$, $A_{m \times n}$ and $B_{(n-m)\times n}$ are full-rank matrices over $\mathbb{F}_q$, $B^t$ represents the transpose of the matrix $B$, and $0<m<n$ are integers. These results also generalize an earlier result of Gravel and Panario (2023), who showed that any arbitrary function $f$ from $\mathbb{F}_q^m$ to $\mathbb{F}_q^{\,n-m}$ can be extended to a bijection over $\mathbb{F}_{q}^n$ through the mapping $F(X)=T(X+B^tf(AX))$, under the condition $AB^t=0$. Here we do not impose the restriction that $AB^t=0$.

---


### 22. [Deep belief networks are exact](https://arxiv.org/abs/2609.05572)

**<font color=#1a73e8>作者：</font>** Gleb Smirnov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We prove that every strictly positive probability distribution on \(\{-1,1\}^n\) is represented exactly by a sigmoid belief network with finite parameters. This answers a question of Sutskever and Hinton. The proof upgrades their probability-sharing approximation to exact representation using Brouwer's fixed-point theorem.

---


### 23. [Multi-granularity Adaptive Hypergraph Representation Learning via Granular-ball](https://arxiv.org/abs/2609.05574)

**<font color=#1a73e8>作者：</font>** Sen Zhao, Yifan Guan, Jinyuan Ni 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hypergraph representation learning aims to capture high-order information in graphs by constructing hyperedges that simultaneously connect multiple nodes. These hyperedges adapt to the graph's topological features, facilitating the extraction of high-order relationships at multiple granularities. Most prior work relies on predefined definitions to generate hyperedges, overlooking the diversity in graph topological structures and the multi-granularity characteristics of hyperedges. As a result, this limits their ability to effectively and adaptively discover high-order relationships and efficiently process complex structural information. To address this limitation, we propose a novel framework called \underline{M}ulti-\underline{G}ranularity \underline{H}ypergraph \underline{R}epresentation \underline{L}earning (MGHRL). MGHRL introduces an Adaptive Granular Hypergraph Generation strategy, which generates hyperedges at multiple levels of granularity through the adaptive splitting of granular-ball, effectively capturing high-order relationships based on the graph's topological structure. Additionally, we propose a Multi-Granularity Hypergraph Network with multiple sub-networks, capturing features from hyperedges at different granularities and integrating them via hierarchical reversible connections. Experimental results show that MGHRL significantly outperforms baseline models on benchmark datasets.

---


### 24. [Capsule Lens: Locating and Tracking Concept Geometry in Model Representations](https://arxiv.org/abs/2609.05575)

**<font color=#1a73e8>作者：</font>** Yiming Tang, Harshvardhan Saini, Samyak Jha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how concepts are encoded in the internal representations of machine learning models is a central problem in mechanistic interpretability, essential both for the science of deep learning and for the trustworthy deployment of increasingly capable models. Existing approaches to interpret model representations mainly map representations onto more interpretable spaces and do not directly characterize how concepts occupy representation space; various hypotheses have been proposed, but often lack of rigorous validation and largely focus on static representations. In this work, we introduce Capsule Lens, a framework that matches the region a concept occupies with a simple, trackable geometric form, a capsule, defined by several interpretable parameters, fitted in closed form to each concept's geometry and validated on held-out samples. We apply Capsule Lens in two major settings: static and dynamic representations. On static representations, we demonstrate how to locate concept geometry across various models, and how the span and norm curves uncover important geometric characteristics. On dynamic representations, we present three case studies tracking representation drifts induced by distinct training settings, CLIP pretraining, RL post-training on visual question answering, and RL post-training on mathematical reasoning. These analyses reveal qualitatively different geometric dynamics, ranging from broad network-wide restructuring in CLIP pretraining to localized and concept-specific changes in RL post-training. Our results include findings aligned with existing literature as well as novel observations. We believe Capsule Lens stands as a promising tool for locating, analyzing, and tracking concept geometry in both static and dynamic representations.

---


### 25. [Planning and Scheduling Business Processes under Control-Flow Uncertainty](https://arxiv.org/abs/2609.05578)

**<font color=#1a73e8>作者：</font>** Michel Kunkler, Stefanie Rinderle-Ma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scheduling activities in business processes can improve efficiency (e.g., reduce makespan), but is challenging because the exact sequence of activities required to complete a case is often uncertain due to decisions based on data that emerges during execution. Nevertheless, probabilistic information regarding such decisions can often be estimated or derived from historical execution logs, and can help anticipate which execution paths are likely to lead to successful completion. Planning with particular execution paths affects feasibility, i.e., the probability of successful completion, and the expected number of superfluous activities that are planned but never executed. We frame the problem as a chance-constrained optimization problem and present two formulations: A decomposed approach with two stages, a planning stage that minimizes the expected number of superfluous activities subject to a feasibility constraint, and a scheduling stage that minimizes the makespan over the planned activities; and an integrated approach that combines planning and scheduling into a single formulation. Evaluation on two real-world and one synthetic dataset shows that the integrated approach yields superior makespans but is intractable at scale, while the decomposed approach scales to large settings.

---


### 26. [ViT3Flow: A Test-Time Training Transformer MeanFlow for Postoperative Radiograph Synthesis in Scoliosis](https://arxiv.org/abs/2609.05579)

**<font color=#1a73e8>作者：</font>** Rui Tang, Sicheng Yang, Moxin Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting postoperative spinal morphology from preoperative radiographs could provide valuable support for scoliosis surgical planning, but remains challenging because surgical correction induces large spatial changes while anatomical structures must be faithfully retained. We formulate this problem as postoperative scoliosis radiograph synthesis and construct ScoliSurg, the first paired dataset for this task, comprising 632 preoperative--postoperative whole-spine radiograph pairs with structured morphology information. We further propose ViT$^{3}$Flow, a single-NFE conditional MeanFlow framework for efficient postoperative radiograph synthesis. ViT$^{3}$Flow models surgical correction as finite-interval generative transport and replaces conventional self-attention with test-time-training token mixers that perform sample-specific inner adaptation to the anatomy and deformity pattern of each case. In addition, a Spinal Morphology Extraction Agent extracts distributions of dominant-curve region and direction from the preoperative radiograph. These distributions guide Diagnosis-Routed Interval Cross-Attention (DRICA), which performs interval-dependent vertical, horizontal, joint, and global retrieval from a separate preoperative token stream. This design enables the evolving postoperative representation to incorporate spatially corresponding anatomical evidence throughout the transport process. Extensive experiments on ScoliSurg demonstrate that ViT$^{3}$Flow achieves the best performance among the compared methods in perceptual image quality, anatomical fidelity, and clinically relevant geometric accuracy, while requiring only a single network evaluation. These results highlight the potential of ViT$^{3}$Flow for efficient and anatomically faithful postoperative radiograph synthesis in scoliosis surgical planning.

---


### 27. [HB-PVI: A Hierarchical Bayesian Personalization and Value-of-Information Framework for Complex Activity Recognition](https://arxiv.org/abs/2609.05582)

**<font color=#1a73e8>作者：</font>** Hammed A. Olayinka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalization can improve activity-recognition performance, but participant-specific gains are heterogeneous, and every additional calibration label has an acquisition cost. This study presents HB-PVI, a hierarchical Bayesian personalization and value-of-information framework jointly modeling participant heterogeneity, the benefit and harm of four personalization mechanisms, and the economic value of an additional label, for the 47-participant MUSIC-CAR complex-activity cohort. A leakage-safe, leave-one-participant-out evaluation combines a sequential-Monte-Carlo participant-effect updater with a Student-$t$ hierarchical gain model and a one-step expected-value-of-sample-information (EVSI) stopping rule. Adapter personalization produced small positive mean F1 gains, growing from 0.00099 at one label to 0.00198 at ten, while adapter-plus-head and prototype-residual personalization were negative on average. Under the primary practical-benefit threshold ($\Delta_{\min}=0.01$) and cost setting, one-step EVSI was zero at every decision state, so the policy purchased no labels and retained population inference for all 47 participants, matching always-stop exactly (region-of-practical-equivalence probability $=1$). Relative to fixed ten-shot adapter personalization, this reduced labeling by 100\% while keeping the posterior mean F1 loss at 0.00217 (95\% credible interval, 0.00048 to 0.00389), with posterior probability 0.9992 of remaining below the 0.005 tolerance. HB-PVI was utility-optimal in 199 of 216 cost-threshold settings and in every setting at or above the primary label cost. These results argue for a population-first deployment policy whenever personalization gains are small relative to labeling, computation, and harm costs, and show that value-of-information reasoning, not raw predictive accuracy, should drive personalization decisions in health-sensing applications.

---


### 28. [Reaching the Cards Apple Wallet Leaves Behind: Direct NFC Acquisition of PRO100, HUMO and UZCARD Payment Cards on iOS](https://arxiv.org/abs/2609.05627)

**<font color=#1a73e8>作者：</font>** Gusein Djalilov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Contactless payment from a phone has become routine in many markets, but the convenience is unevenly distributed. Apple currently lists Kazakhstan among supported Apple Pay markets, but not Uzbekistan, Kyrgyzstan, Tajikistan or Turkmenistan. In Uzbekistan, HUMO and UZCARD are the two national interbank retail card systems, and both include contactless card products. This paper describes an application-level card-capture method for tested PRO100, HUMO and UZCARD cards on NFC-capable iPhones. Using Core NFC, the reader opens a tag session, selects an application when necessary, and recovers the primary account number (PAN) and expiry date from the returned data. The difficult parts were empirical: identifying AIDs that worked on the tested cards and decoding card-generation-specific response layouts. The implementation was later hardened around a hybrid parsing path that prefers BER-TLV/EMV fields when present and keeps the observed offsets only as a legacy fallback. The paper also gives a system-level workflow, a threat model, explicit failure handling, a platform comparison, and a reproducible evaluation protocol. No claim is made that the same behavior is available unchanged on every iPhone/iOS combination, on iPadOS or macOS, or under future Core NFC policy. The method captures registration data; it does not emulate a card, authorize a payment, or treat an NFC read as proof of ownership.

---


### 29. [The convergent laboratory: when AI reasoning, autonomous experiments, high performance and quantum computing reshape chemistry](https://arxiv.org/abs/2609.05643)

**<font color=#1a73e8>作者：</font>** Eliu Huerta, Xiaoyun Wang, Geetika Gupta 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This Comment emerges from TPC26 (this https URL), a conference convening leaders from academia, national laboratories, and industry who are reshaping materials science discovery. The meeting explored how AI, autonomous agents, self-driving labs, higher performance and quantum computing converge to amplify their individual impact on materials science discovery. The perspectives here reflect the firsthand experiences of researchers at these frontiers and capture the essence of this global endeavor. As AI-driven reasoning, autonomous agentic frameworks, self-driving laboratories, and fault-tolerant quantum processors mature simultaneously, we offer this Comment as a reference at what we believe is a tipping point of transformative advances and productive disruption in the chemical sciences.

---


### 30. [Endogenous Exploration in Reinforcement Learning with Intrinsic Curiosity](https://arxiv.org/abs/2609.05650)

**<font color=#1a73e8>作者：</font>** Armando Vieira  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a reinforcement learning framework in which exploration is driven by intrinsic curiosity, designed for scenarios where environments are non-stationary and rewards are sparse, delayed, uninformative, or absent. In our model, action selection is guided by a combination of external rewards and an epistemic motivation mechanism that biases the agent toward structured exploratory directions. The central hypothesis is that effective exploration emerges at intermediate levels of incoherence, while performance degrades under both overly rigid and overly disordered dynamics. To test this idea, we implement the framework on top of a Liquid State Machine (LSM) substrate and evaluate it on two standard benchmarks: the discrete-action LunarLanderv2 and the continuous-control BipedalWalkerv3. The proposed method achieves competitive performance on both tasks relative to established deep RL algorithms, including Proximal Policy Optimization (PPO) and Intrinsic Curiosity Module (ICM). We further show that the curiosity window is not recovered in Active Inference agents under the same analysis, suggesting that the proposed dynamics capture a distinct exploration regime

---


### 31. [Srijika: OpenType-Layout-Reusing Font Restyling for Nine Indic Scripts](https://arxiv.org/abs/2609.05661)

**<font color=#1a73e8>作者：</font>** Anil Pai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Srijika, a system for producing installable OpenType fonts for nine Brahmic scripts: Devanagari, Tamil, Bengali, Telugu, Kannada, Malayalam, Gujarati, Gurmukhi, and Odia. Rather than generating fonts from scratch, Srijika restyles glyph outlines from shaping-complete template fonts. It preserves the template's cmap and GSUB closure and its GPOS data under a documented metric policy, making every output a complete font by construction. This addresses a central challenge of Indic font generation: hundreds to thousands of conjuncts, half forms, and matra variants must remain mutually consistent under OpenType shaping.
Srijika produces 66 TTFs: 57 curated presets and nine open-vocabulary showcase fonts. All pass the OpenType Sanitizer, while HarfBuzz and CoreText reproduce the template glyph-ID sequences on conjunct-heavy probes. A full-closure audit covering 80,915 glyphs and 54,812 anchors quantifies metric changes. Natural-language style selection uses Lipika, a retrieval index over approximately 650 open-license font families. A reference-conditioned latent diffusion model redraws template glyphs in the selected style, followed by content gating, harmonization, and shaped-cluster verification with fallback to template outlines.
We evaluate against no-learning baselines. On diffusion-training-family-held-out SSIM gates, template copying outperforms generation on 50 of 56 faces. Style movement is measurable only with an internal same-model embedding whose training corpus includes the held-out families, so these results require caution. A learned baseline, independent style metric, and human study are outside this report's scope. Our contributions are the layout-reusing formulation and pipeline, its nine-script audit and benchmark, and a negative-results catalogue covering failed conditioning, objective choices, and data-hull limits of reference-guided restyling.

---


### 32. [Full-Page Optical Music Recognition of Handwritten Monophonic Scores](https://arxiv.org/abs/2609.05662)

**<font color=#1a73e8>作者：</font>** Adrian Rosello, Antonio Ríos-Vila, David Rizo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Full-page end-to-end Optical Music Recognition seeks to transcribe entire music pages directly into symbolic notation, avoiding the limitations of traditional pipelines that rely on accurate staff segmentation. Recent Transformer-based architectures have achieved strong performance on typeset scores, relying on large-scale synthetic data for pretraining. However, their applicability to handwritten music remains largely unexplored. In this work, we study full-page transcription on handwritten monophonic collections and analyze the impact of synthetic pretraining in this setting. To investigate which factors are most relevant during pretraining, we introduce a generator capable of producing visually coherent full-page scores in both typeset and handwritten styles. Experiments on three real handwritten datasets provide a comparative evaluation of several full-page pipelines and different synthetic pretraining strategies. The results suggest that the benefits of synthetic pretraining are primarily associated with learning structural layout conventions rather than with visual similarity to the target handwriting.

---


### 33. [Connecting Score Matching, Maximum Likelihood, and Expectation-Maximization in Mixed Linear Regression](https://arxiv.org/abs/2609.05688)

**<font color=#1a73e8>作者：</font>** Zhankun Luo, Abolfazl Hashemi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study variance-preserving diffusion of the response in mixed linear regression (MLR) with unknown mixing weights. Our analysis separates the statistical guarantees of score matching from the loss geometry and optimization signal at a fixed diffusion noise level. The KL divergence links the denoising score matching objective integrated over the diffusion path with the likelihood and a terminal discrepancy. Under mild regularity conditions and terminal schedule, the resulting estimator converges up to the ground truth parameters of MLR, and its scaled error converges to the Gaussian limit of the maximum-likelihood estimator. At a fixed scale of the diffusion noise level, we derive a decomposition linking the score matching loss to cross-entropy and Expectation-Maximization (EM) operators. This decomposition yields an EM-related low-noise gradient expansion with additional correction terms of latent variance. In the high-noise limit, we further characterize gradient descent on this limiting loss under isotropic covariance. Along fixed high signal-to-noise ratio rays, the score matching imbalance gradient and the latent-variance term tend to zero pointwise. Numerical experiments illustrate our theoretical findings and statistical guarantees.

---


### 34. [Analysis of Respiratory Sinus Arrhythmia with Neural Networks](https://arxiv.org/abs/2609.05698)

**<font color=#1a73e8>作者：</font>** Julian Szymanski, Patryk Orkisz, Higinio Mora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The paper introduces a neural network-based approach for analyzing ECG signals to estimate respiratory rate by leveraging the phe- nomenon of Respiratory Sinus Arrhythmia (RSA). Our method employs a deep learning model trained to predict respiratory waveforms directly from ECG input data. To achieve this, we developed and evaluated three different neural network architectures capable of automatically extract- ing relevant features from ECG signals without the need for manual preprocessing. The proposed approach offers a robust and scalable solu- tion for non-invasive respiratory monitoring, with potential applications in healthcare and wearable technology

---


### 35. [XAI-SDN: An Explainable Entropy-Guided Machine Learning Framework for Real-Time DDoS Detection in Software Defined Networks](https://arxiv.org/abs/2609.05701)

**<font color=#1a73e8>作者：</font>** Adeel Ahmad, Ali Akarma, Ahmad Ali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> One of the biggest risks faced by Software Defined Networks (SDN) is the Distributed Denial of Service (DDoS) attack in which a compromised controller can make an entire network unusable. To address these challenges, we suggest an entropy-guided machine learning framework, called XAI-SDN, for real-time DDoS detection in SDN environments which is lightweight and explainable. The framework extends the flow features extracted by CICFlowMeter with eight Shannon entropy metrics obtained by an $\mathcal{O}(1)$ rolling algorithm and uses a Random Forest classifier with SHAP TreeExplainer for providing transparency at the prediction level. On a fixed temporal split, XAI-SDN achieves an accuracy of 99.9987\%, a macro F1-score of 99.9621\%, and an AUC-ROC of 1.0000 on the full 3.59 million flows of the CIC-DDoS2019 SYN benchmark. The pipeline sustains 0.0165~ms per flow (60{,}606 flows/s) without the use of SHAP and 0.5122~ms per flow (1{,}953 flows/s) with full support of SHAP under the 99.14\% prevalence of DDoS traffic, which is a step towards achieving a balance between the detection performance and operational transparency in next-generation SDN security.

---


### 36. [Newton Matching for Generative Modeling: A Unified Framework for Fine-Tuning and Sampling](https://arxiv.org/abs/2609.05727)

**<font color=#1a73e8>作者：</font>** Zeyang Li, Yunan Wang, Paolo Giaretta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop Newton Matching, a unified framework for fine-tuning and sampling in generative modeling. The target is $\pi\propto\mu e^{\tau r}$, where $r$ is the reward, $\tau>0$ the inverse temperature, and $\mu$ denotes the pretrained model's terminal density for fine-tuning or the constant $1$ for sampling. We shift the paradigm from isolated losses to iterative optimization over canonical models: population minimizers of standard conditional matching for terminal densities. Under compatible smooth-realization assumptions, canonical velocities form a manifold diffeomorphic to the density manifold. Transporting the Fisher-Rao metric and mixture connection to this manifold, we show that the reverse-KL Hessian equals the metric, so the Newton direction coincides with the negative Fisher-Rao gradient. At terminal density $\rho$, each stage takes a tangential step generated by the regularized reward $r-\frac1\tau\log(\rho/\mu)$, followed by terminal-density-preserving canonicalization. This canonical retraction yields an exact finite-stepsize density characterization. For the ideal iteration, we prove strict reverse-KL descent away from the target for $0 < \eta \le \tau$, global convergence under mild conditions, and local quadratic convergence for full steps ($\eta=\tau$). Covariance and gradient forms, each with forward or reverse regression-pair constructions, yield sample-wise tangential-update losses with the same population minimizer, without importance sampling or full-trajectory backpropagation. We develop approximate updates and define critical-point consistency as vanishing tangential displacement if and only if $\rho=\pi$. We recover representative methods as exact realizations, critical-point-consistent approximations, or objective-altering variants, enabling modular algorithm design. Our work advances the theory and algorithms of reinforcement learning for generative models.

---


### 37. [MedWER: A Reproducible, Model-Free Evaluation Protocol for Medical Speech Recognition](https://arxiv.org/abs/2609.05728)

**<font color=#1a73e8>作者：</font>** Justin Behling  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Overall word error rate hides clinically critical errors: a transcript can be 95% correct and still swap one drug for another. The usual fix weights errors on medical entities, and almost always depends on an evaluation-time named-entity recognition (NER) model or cloud API, which makes the metric's denominator a versioned black box. We present MedWER, an evaluation protocol and open-source tool for medical ASR whose denominator is a fixed, license-clean term list: 19,373 drug, diagnosis, symptom, and injury-mechanism entries projected from public sources. The protocol couples a pinned text normalizer with a phrase-aware term-restricted WER, the MedWER, so the only versioned component is a normalizer dependency held at an exact release and checked against committed golden fixtures. Coverage is validated against an independent provincial drug-benefit file the list was not built from; the matching heuristic is calibrated against ground-truth entity spans. Baselines for Moonshine~base, Whisper~this http URL, and MedASR on two open benchmarks are scored with the released tool and reported with 95% confidence intervals from resampled per-utterance scores.

---


### 38. [Bigger Text Encoders Can Hurt CLIP Zero-Shot Performance](https://arxiv.org/abs/2609.05730)

**<font color=#1a73e8>作者：</font>** Samir Char, Carles Domingo-Enrich, Randall Balestriero  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive Language-Image Pretraining (CLIP) is a building block of many machine learning applications. Scaling laws have guided resource allocation for large-scale training, yet prior work treats total CLIP model size as a single variable, without exploring how the capacity split between encoders impacts downstream performance. Here, we train multiple CLIP models with different vision and text encoder sizes, revealing that for most vision encoders, there is an optimal text encoder size beyond which zero-shot performance degrades---even as total parameter count increases. Exploiting this behavior yields efficient configurations that match the zero-shot performance of the standard ViT-B/16 architecture with up to 55% fewer parameters. We further show that this degradation stems from overfitting induced by the oversized text encoder, and that using modality-specific weight decay coefficients not only recovers but improves performance across all degraded configurations. A geometric analysis reveals a trade-off in which scaling the text encoder improves embedding uniformity but worsens cross-modal alignment; we further show that these metrics are predictive of zero-shot performance. We hope these findings motivate CLIP architectures and training methods that counteract this degradation, a prerequisite for scaling CLIP reliably and efficiently.

---


### 39. [RenderFormer-V2: Neural Rendering with Heterogeneous Scene Primitives](https://arxiv.org/abs/2609.05738)

**<font color=#1a73e8>作者：</font>** Chong Zeng, Yue Dong, Pieter Peers 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present 'RenderFormer-V2', a unified learned transformer-based neural rendering model, complementary to modern physics-based rendering systems, that can handle diverse light-transport effects such as caustics, volumetric scattering, environment lighting, textured and displaced surfaces and out-of-distribution materials without per-scene training or specialized code. RenderFormer-V2 models global light transport as a sequence-to-sequence transformation. Following its predecessor, RenderFormer-V2 also employs a two stage process: a view-independent stage that resolves intra-scene primitive to primitive transport, and a view-dependent stage that transforms the internal neural scene representation into image pixels. Different from RenderFormer, our model employs a novel combined windowed-attention and rendering-informed attention sink in the view-independent stage to improve scalability while maintaining render accuracy. To further improve versatility, RenderFormerV2 supports heterogeneous scene primitives, including environment maps and participating media, and it employs a material encoding independent of the underlying surface reflectance model that encodes material appearance via a novel neural embedding. We demonstrate the versatility of RenderFormer-V2 on a variety of scenes and perform an extensive ablation of the improved attention mechanism.

---


### 40. [Gaussian Linear Functional Manifold Method for Massive Point Cloud Data](https://arxiv.org/abs/2609.05744)

**<font color=#1a73e8>作者：</font>** Hong Zhao, Tonglin Zhang, Baijian Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing continuous terrain manifolds from massive, unstructured airborne LiDAR point clouds remains challenging in complex Wildland-Urban Interface (WUI) environments, where deep neural networks require costly point-wise annotations and nonparametric surface reconstruction methods often lack structural interpretability. This paper introduces the Gaussian Linear Functional Manifold (GLFM), a physics-informed statistical framework that represents continuous surface topography using deterministic linear functional bases while modeling microscale diffuse laser backscatter as an isotropic Gaussian process. To avoid the quadratic computational cost of exact constrained maximum likelihood estimation, we develop an algebraic singular value decomposition (SVD) rank-reduction algorithm that enables linear-time parameter estimation and closed-form quadric classification. Evaluated on 35.2 km^2 of real-world aerial LiDAR data, GLFM automatically filters ground points and extracts morphological features, achieving an adjusted Rand index (ARI) of 0.9933 against field-verified ground truth and outperforming four leading baselines while maintaining an out-of-core memory footprint. The framework provides a rigorous, interpretable, and scalable foundation for large-scale point cloud analytics.

---


### 41. [A Multi-Source Ensemble Approach to Candidate Generation for Alternative Vacation Rental Property Recommendations](https://arxiv.org/abs/2609.05748)

**<font color=#1a73e8>作者：</font>** Syed Mohammed Arshad Zaidi, Eric Rincon, Shayan Hassantabar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Alternative property recommendations play a critical role in vacation rental marketplaces, helping users discover relevant options when viewing a specific listing. However, generating high-quality candidate alternatives presents unique challenges: heterogeneous inventory, geographic constraints, rapid availability changes, and long-tail property distributions. We present a comprehensive study of candidate generation (CG) approaches for vacation rental alternatives, comparing collaborative filtering, shallow embeddings, and graph neural network (GNN) methods.
Our experiments on a large-scale vacation rental platform (over 2M active properties) show that a hybrid architecture combining item-based collaborative filtering with GNN-based retrieval improves Recall@300 by 14.8% over the strongest baseline, by leveraging the complementary strengths of the two sources: collaborative filtering excels at early recall for properties with rich interaction history, while GNNs discover diverse, non-obvious alternatives and handle cold-start scenarios more effectively. As a component result, GNN-based embeddings alone substantially outperform shallow Hotel2Vec embeddings (48-68% relative recall improvement across K), motivating their inclusion in the ensemble.
Crucially, we examine how CG-stage gains carry through to the downstream ranking stage, and find that a stronger candidate pool yields higher downstream ranking quality, though attributing this effect cleanly is complicated by the coupling between candidate generation and ranker training. This recall-conversion gap is an important consideration for practitioners deploying new retrieval methods in two-stage recommendation systems.

---


### 42. [The Normalization of Deviance in AI Development](https://arxiv.org/abs/2609.05749)

**<font color=#1a73e8>作者：</font>** Emilio Barkett, Alexander Kimpton, Daniel Graham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Work on the risks of artificial intelligence has focused predominantly on capability risk: the danger that systems become too powerful, too autonomous, or too misaligned with human values. Far less attention has been paid to the organizational level---to whether the institutions building these systems are themselves predisposed to drift toward failure. This paper argues that they are. Regardless of how capable AI systems become, the organizations building them face the same structural dynamics that preceded past major technological disasters. Drawing on case studies of the Space Shuttle Challenger, the Three Mile Island accident, and the Boeing 737 MAX crashes, this paper identifies the common structural mechanisms preceding each failure and maps them onto contemporary AI development. The findings suggest that existing safety infrastructure may provide less protection than it appears, as organizations can complete safety processes in full compliance and still produce catastrophic outcomes. The pre-disaster period of AI development is still underway; the purpose of this paper is to make these dynamics legible while they can still be interrupted.

---


### 43. [AAMBERS-UAV: Acquisition-Aware Multimodal Backbone Evaluation and Ranking for UAV Weedy Rice Segmentation](https://arxiv.org/abs/2609.05762)

**<font color=#1a73e8>作者：</font>** Tarek Rahman, Nazim-E-Alam, Md Kishor Morol 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UAV image collections contain spatially and temporally related frames, yet semantic-segmentation benchmarks commonly split them at image level. Such splitting can place samples from one acquisition in both model development and testing, obscuring transfer to a genuinely new survey. Using the 734-sample WeedyRice-RGBMS-DB, we fix a 124-image target-acquisition test set and compare two protocols with identical train, validation, and test counts: target-held-out, which excludes the target acquisition from development, and target-exposed, which admits its remaining images. SegFormer-B0 is evaluated with RGB, four-band multispectral (MS), and seven-channel RGB+MS input over two fixed-split seeds. RGB is strongest under complete acquisition holdout ($0.7317\pm0.0201$ IoU), whereas RGB+MS becomes strongest after target exposure ($0.7822\pm0.0269$). A fixed-split U-Net/ResNet18 replication confirms positive exposure gains for all three inputs, but retains RGB as the best modality under both protocols. Acquisition exposure therefore increases measured performance across both evaluated backbones, while its effect on modality ranking is architecture-dependent. A supplied-split audit reveals strong near-sequential dependence, and corruption tests show that early fusion is substantially more sensitive to RGB--MS displacement than to moderate radiometric scaling. These results support acquisition-aware same-test evaluation as a necessary complement to ordinary image-level splitting in multimodal UAV benchmarks. The code and supporting the findings of this study will be publicly released upon acceptance of the paper.

---


### 44. [Nonlinear elliptic homogenization with the parametric Deep Ritz method](https://arxiv.org/abs/2609.05778)

**<font color=#1a73e8>作者：</font>** Conor Rowan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Elliptic homogenization is used to determine coarse-grained properties of materials with features on small scales. When these small scale features have rapid, periodic fluctuations, the solution field corresponding to a homogenized constitutive relation closely resembles the true solution based on the heterogeneous material. This homogenized behavior of the material is computed from a cell problem, where a cell is defined to be one period of the fluctuating material. In the context of linear elliptic partial differential equations, the homogenized constitutive relation is defined simply by a constant coefficient tensor, but for nonlinear problems, the homogenized response depends on the macroscopic state and/or its gradient, thus requiring solutions to parametric cell problems. When computing a numerical solution with the homogenized constitutive relation, it is useful to have a differentiable representation of the solution to the cell problem, as derivatives of the homogenized constitutive relation are required in Newton iterations for the macroscopic state field. In this work, we use the Deep Ritz method to solve the parametric cell problems that arise from nonlinear homogenization. First, we exploit the variational structure of the cell problem, then we discretize the dependence of the cell response on both space and the macroscopic state with a neural network. Enforcing boundary conditions on the cell response strongly, we next use the parametric Deep Ritz method to simultaneously solve the cell problem over a range of macroscopic states. We show that this method is accurate, efficient, and offers a continuous and differentiable representation of the cell response over the macroscopic state and gradient. We then show that our parametric representation of the cell response significantly expedites macroscale solutions when compared to a traditional $\text{FE}^2$ scheme.

---


### 45. [Evidence-Aligned Local Composition of Discrete Experts for Sequence Restoration](https://arxiv.org/abs/2609.05801)

**<font color=#1a73e8>作者：</font>** Mohammad Panahazari, Usman A. Khan, Shuchin Aeron  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A document modeled as a discrete sequence of tokens can be thought of as being generated from a composition of texts from different domains; a README file, for example, moves between prose, code, and configuration. When such a document is corrupted and only frozen domain experts are available, restoring it requires deciding both what is missing and which expert to trust at each position, at test time and without region labels or a trained router. We introduce evidence-aligned local composition, which infers a soft, position-wise weighting over the experts from the marginal evidence of the corrupted observation under a given corruption model, estimating the evidence from the experts' own denoising losses and smoothing the weights across positions. Because the weighting is soft, it recovers a mixture when the true composition is mixed and concentrates on one expert when that suffices. Across a categorical simulator, byte-level experts, and experts fine-tuned from a $1.3$B discrete flow-matching model, the inferred weights track the true regions at $0.85$ field accuracy on naturally mixed scientific documents, and at $0.98$ on constructed mixtures whose regions are lexically disjoint. Restoration improves over a single global weight when the experts are genuinely distinct and reduces to it when they converge, tracking a measure of expert separation.

---


### 46. [MolParser-Mobile: Ultrafast OCSR System for Large-Scale Chemical Literature Mining](https://arxiv.org/abs/2609.05807)

**<font color=#1a73e8>作者：</font>** Xi Fang, Haocheng Lu, Han Lyu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Chemical Structure Recognition (OCSR) is a fundamental component of chemical literature mining, enabling molecular database construction, reaction extraction, and AI-driven scientific discovery. Despite substantial progress in recognition accuracy with recent deep learning-based methods, inference throughput remains a critical bottleneck that limits web-scale deployment. To address this challenge, we propose MolParser-Mobile, an AutoML-optimized lightweight end-to-end OCSR framework. MolParser-Mobile contains only 9.98M parameters, while reaching a throughput of 1,520 molecules per second on a single NVIDIA RTX 4090D GPU. Despite its compact design, it maintains competitive and, on several benchmarks, superior recognition accuracy.

---


### 47. [CoRe-SAM3: Conditional Semantic--Visual Reconciliation for SAM3 Crack Segmentation](https://arxiv.org/abs/2609.05816)

**<font color=#1a73e8>作者：</font>** Shipeng Liu, Liang Zhao, Dengfeng Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Crack segmentation requires a model to recognize target semantics while accurately recovering thin, low-contrast, and topologically continuous local structures. Although SAM3 provides strong open-concept segmentation, its direct application to the crack domain still misses weak cracks, activates crack-like background regions, and produces local boundary errors. We first diagnose the functional differences between the internal prompt-conditioned semantic representation and native visual representation of SAM3 on five crack datasets. The results show that the semantic representation already carries most task information for crack prediction, whereas the utility of the visual representation depends on the current semantic state. Directly combining the two representations does not yield consistent gains. Based on this finding, we propose Conditional Semantic--Visual Reconciliation, termed CoRe. CoRe retains semantic prediction as the primary decision path, applies lightweight semantic calibration to adjust the target-domain decision mapping, and uses spatially aligned native visual evidence to generate a zero-initialized, bounded, and regularized conditional residual that selectively corrects existing predictions. Across five domains, CoRe-SAM3 improves the average Crack IoU from 62.34% to 70.47% and clDice from 81.98% to 89.24%, while introducing only 18.914 K trainable parameters. Prediction-transition analysis further shows that CoRe corrects an average of 34.38% of native errors, with a damage rate of only 0.23% on pixels correctly classified by native SAM3. These results demonstrate that constrained prediction correction based on the functional differences between internal representations provides an effective and parameter-efficient target-domain adaptation strategy for vision foundation models with strong task-specific semantic priors.

---


### 48. [Generalizing HVAC Control With Domain Randomized Reinforcement Learning](https://arxiv.org/abs/2609.05822)

**<font color=#1a73e8>作者：</font>** Pablo Boitel, Kun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying advanced HVAC (Heating, Ventilation and Air Conditioning) controllers at scale remains difficult because performance often depends on accurate building models or per-site retuning. We propose NOMAD-RL (Neural Online Meta-Adaptation for Dynamics), a general-purpose Reinforcement Learning (RL) controller designed to transfer across heterogeneous thermal zones through a universal, non-invasive thermostat interface. The controller acts on temperature setpoints from zone measurements and forecasts, while a recurrent policy supports online adaptation under partial observability.
Our main contribution is an adaptive domain randomization scheme based on physics-informed normalizing flows, which models correlated and multimodal distributions of thermal-zone parameters while maintaining physical plausibility and controllability. This produces a realistic and progressively adaptive training curriculum that improves transfer across buildings. We evaluate NOMAD-RL against a constant-setpoint PID controller, RL without domain randomization, and MPC in single- and multi-zone settings. NOMAD-RL consistently outperforms the PID and non-randomized RL baselines, and approaches the performance of a well-tuned MPC, especially in the more challenging multi-zone case. These results highlight the potential of adaptive, physics-informed domain randomization for robust and transferable HVAC control.

---


### 49. [Scaling Optimal Classification Trees via Adaptive Feature and Sample Reduction](https://arxiv.org/abs/2609.05826)

**<font color=#1a73e8>作者：</font>** Jiancheng Tu, Wenqi Fan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic programming for optimal classification trees becomes computationally expensive as the numbers of features and training samples increase. We develop a joint feature- and sample-space reduction framework based on STreeD. Weighted STreeD merges duplicate records created after projection onto a fixed candidate set into weighted representatives. This reduces sample-dependent computation without changing the fixed-candidate optimization problem. Adaptive STreeD repeatedly refines a bounded candidate set, retains features used by the incumbent tree, rebuilds the weighted representation, and solves the resulting reduced problems. Each certified Weighted STreeD solution is optimal for its current candidate set, while the outer feature search remains heuristic over the full feature space. Experiments on five data sets show that Weighted STreeD achieves speedups of up to 121.41 times over standard STreeD. Adaptive STreeD reduces runtime in matched comparisons at depths 2 to 4 and continues to return feasible trees at greater depths where full-feature methods are limited by time or memory. Under the same computational budget, its predictive performance remains comparable to the evaluated optimal classification tree baselines and is higher in some comparisons. These results show how joint feature- and sample-space reduction can scale dynamic-programming-based optimal-tree learning to more demanding instances.

---


### 50. [Learning Counterfactual World Models for Embodied Reasoning under Partial Observability](https://arxiv.org/abs/2609.05834)

**<font color=#1a73e8>作者：</font>** Todd Y. Zhou, Daniel Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models promise a general route to embodied intelligence: learn predictive dynamics once, then reason, plan, and act with them. Increasingly, the representations beneath such models are pretrained on large-scale video, interaction, and multimodal corpora, which raises a question prediction quality alone cannot answer: when is a learned representation actually actionable? We identify a failure mode we call counterfactual collapse: a model predicts visually plausible futures while failing to distinguish interventions with different behavioral consequences. This arises whenever a representation is optimized for perceptual similarity rather than intervention structure, which is precisely the objective under which most large-scale pretrained encoders are learned. We introduce Counterfactual Latent World Models (CLWM), which combine a recurrent belief-state encoder, action-conditioned latent dynamics, and a contrastive counterfactual objective that separates futures induced by distinct interventions even when their observations look alike. Across occluded manipulation, aliased navigation, and long-horizon manipulation, CLWM improves planning success over the strongest baseline (65.1% $\to$ 74.6% on Occluded Push and 67.3% $\to$ 78.9% on Aliased Maze) and reduces exploitative planning failures (18.4% $\to$ 9.7% on Deferred Kitchen), with ablations attributing the gains to hard counterfactual negatives, especially perceptual-alias negatives. Finally, our counterfactual separability metric, which tracks planning success across the five baseline model classes ($r \ge 0.94$), is representation-agnostic: given intervention-outcome labels, it can audit any encoder, pretrained or trained from scratch, before a planner trusts it. We do not yet measure it on large-scale pretrained encoders. Here we establish the metric and its relationship to planning success for world models trained from scratch.

---


> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
