# 📦 其他研究 | 2026年10月28日

> 本类共 **446** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-446](./part-09.md)

---

### 1. [Whispering Wisely: Smart Subset Selection for ASR Fine-Tuning](https://arxiv.org/abs/2610.32997)

**<font color=#1a73e8>作者：</font>** Roi Yozevitch, Or Haim Anidjar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition (ASR) models such as OpenAIs Whisper have substantially improved speech recognition quality but remain expensive to fine-tune, especially when large amounts of transcribed audio are available. This makes it challenging for many practitioners to adapt these models to new languages or domains. In this work, we introduce an embedding-based subset selection approach for selecting smaller training sets for ASR fine-tuning. Using Whispers pretrained encoder, we map each audio sample into a fixed-dimensional embedding space and apply a greedy k-center algorithm to select diverse and representative subsets of the training data. We evaluate this approach on both Hebrew and Danish, showing that k-center selection often improves upon random sampling, particularly at smaller subset sizes. An analysis of lexical diversity reveals that k-center subsets capture a broader range of linguistic content than random subsets of the same size, which may help explain their observed effectiveness. Overall, our results demonstrate that embedding-based subset selection provides a practical strategy for ASR subset selection in the two evaluated languages, with the clearest recognition benefits observed at smaller sample budgets.

---


### 2. [From Writing Advice to Manuscript Governance: A Constrained-Transformation Framework for Academic Revision](https://arxiv.org/abs/2610.33001)

**<font color=#1a73e8>作者：</font>** Simon Rudkin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Academic revision presents a governance problem when legitimate writing objectives conflict. Writing-process and social-science research show that revision is recursive and that wording carries epistemic and disciplinary commitments. Those literatures identify important constraints but do not settle which objective should prevail when concision, outlet form or stylistic variation conflicts with evidence and claim boundaries. This paper models revision as an admissibility problem under ordered constraints. Task-relative invariants, contextual constraints and mutable presentation choices define the admissible space; a claim-preservation contract links evidence and judgement to an authorised claim boundary. Four governance propositions specify preservation, precedence, context and sufficiency. The Academic Writing Filter implements the model by screening candidate revisions; it is not a universal definition or classifier of good academic writing. The contribution is a technology-independent mechanism for changing presentation without silently changing the research argument.

---


### 3. [Intuition with Evidence: Adaptive Dual Memory for Multimodal Agents](https://arxiv.org/abs/2610.33019)

**<font color=#1a73e8>作者：</font>** Qiuhe Hong, Jingya Wang, Cuzhen Geng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As multimodal agents engage in sustained interactions, long-term memory serves two distinct but complementary functions: fine-grained evidence recall and internalized interpretation for global understanding. Although episodic and latent memory address these demands through explicit historical records and internalized experience, neither paradigm alone can accommodate the diverse memory affinities across tasks, owing to limitations in episodic evidence coverage and integration, and in latent factual grounding. To bridge this divide, we propose a dual-memory framework, unifying a model-native latent memory as an intuitive prior with a multi-indexed episodic memory for exact evidence reconstruction via retrieval-conditioned joint alignment. At inference, the framework adaptively composes these memories through a training-free routing mechanism driven by Jensen-Shannon Divergence (JSD) sensitivity and confidence proxies for query-dependent memory affinity. Extensive evaluations across multimodal benchmarks demonstrate state-of-the-art performance, outperforming single-paradigm baselines overall (+4.67\% over vanilla Episodic), with further analysis highlighting episodic strengths in evidence-localized tasks and latent contributions to integrating dispersed information and compensating for imperfect retrieval.

---


### 4. [Feature Scaling Beats Architecture Choice in Offline Respiratory Screening for Low-Resource Clinics](https://arxiv.org/abs/2610.33030)

**<font color=#1a73e8>作者：</font>** Abubakar Chilala, Cleophas Kadima, Innocent Anyaele 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep models are the usual choice for respiratory sound classification, but in clinics without GPUs or connectivity that choice carries a cost. We compare classical and deep classifiers on a five-class respiratory-sound corpus of 1,211 clips (asthma, COPD, pneumonia, Bronchial, healthy) from 201 patient groups, with a 3.86:1 class imbalance, using pre-registered patient-grouped cross-validation (25 runs per configuration). An SVM over 30 summary features (MFCC, ZCR and RMS statistics) reaches macro recall 0.78 and 0.71 recall on the rarest class. A 1.13M-parameter convolutional recurrent network over log-Mel spectrograms reaches 0.75 to 0.77, and no difference between model families is resolved. The largest single effect we measure is a preprocessing effect rather than an architectural one. Standardizing the SVM's features, a routine step for RBF kernels, moves its macro recall from 0.51 to 0.78, a 27-point swing wider than any gap between model families here. Augmentation did not help: SMOTE, waveform augmentation and SpecAugment have no measurable effect. Latency does not separate the models (51 to 74 ms per clip on a CPU-only laptop), but the classical models avoid a 449 MB PyTorch runtime. Clip-level splits, which let a patient's recordings fall on both sides, inflate macro recall by 7.5 to 9.8 points. Recording source is strongly tied to label (Cramer's V = 0.65 between native sampling rate and class), and in an exploratory analysis clips recorded at a class's minority rate are mostly assigned to classes typical of that rate; we state this confound as the paper's main limitation.

---


### 5. [Detection of false positives by human reviewers depends on the face recognition algorithm and its security configuration](https://arxiv.org/abs/2610.33045)

**<font color=#1a73e8>作者：</font>** Esha Edakoth, John J. Howard, Isabelle M. Shuggi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Integration of artificial intelligence (AI) technology into identity workflows, such as automated face recognition (FR), has enhanced operational capabilities, with FR algorithms achieving super-human scale and accuracy. However, these gains can make human oversight of FR more difficult, raising questions about the effectiveness of these human-AI teams. We measured human reviewers' ability to detect false positive errors made by commercial FR algorithms across varying security configurations. Using a novel dataset, the Difficult Facial Image Comparison Test (DFICT), derived from false positives made by four comparable commercial face recognition algorithms, we measured the ability of 801human reviewers to detect algorithmic false positives across three security configurations, representing operationally relevant biometric thresholds. Our findings show that human reviewers can reduce algorithmic false positives, but performance declines at stricter security thresholds. Further, reviewer performance varied by algorithm indicating that some algorithms are more compatible with human oversight. We suggest that biometric systems should be designed to account for human reviewers' variable effectiveness, particularly in high-security applications. Our findings should be considered during algorithm selection and inform human oversight strategies to minimize AI-related risks in operational FR deployments.

---


### 6. [TRACER: An RDC-Triggered Trajectory Recovery Framework for Cyberattack-Resilient Adaptive Cruise Control](https://arxiv.org/abs/2610.33052)

**<font color=#1a73e8>作者：</font>** Yicheng Yang, Tianyu Liu, Omar Tahri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing connectivity of adaptive cruise control (ACC) systems exposes vehicle-state information to cyberattacks, potentially causing irrational car-following behavior and unsafe longitudinal dynamics. Existing trajectory recovery methods generally lack an interpretable criterion for recovery activation and remain vulnerable to attack-induced distribution shifts. To address these challenges, this paper proposes TRACER, a rational driving constraint (RDC)-triggered trajectory recovery framework for cyberattack-resilient ACC systems. TRACER employs a rationality-aware triggering (RAT) mechanism that activates recovery when the observed driving state violates the calibrated RDC bounds. It also introduces cross-branch robust imitation learning (CRIL), which combines a clean branch for learning nominal driving behavior with a noise-enhanced branch for improving robustness to corrupted observations. Cross-branch fine-tuning further aligns the robust recovery policy with the nominal driving-state distribution. Experiments across six cyberattack scenarios show that TRACER achieves reliable recovery triggering and outperforms state-of-the-art recovery baselines in terms of accuracy, stability, and safety. State-space analysis further confirms that TRACER mitigates attack-induced distribution shifts and restores coupled spacing-velocity dynamics, highlighting the effectiveness of robust policy learning for cyberattack-resilient ACC.

---


### 7. [Saga: an in silico ontology for a multimodal patient world model](https://arxiv.org/abs/2610.33054)

**<font color=#1a73e8>作者：</font>** Youcheng Li, Fa Tian, Binbin Su  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Simulating an individual's disease course requires connecting patient history to future events, clinical timing and disease morphology. Longitudinal prediction and multimodal representations exploit this information, but organizing future readouts around a common patient state and advancing trajectories without real intermediate observations remain central challenges. Here we introduce Saga, a multimodal patient world model that learns a shared state from patient histories to predict clinical events and generate multimodal images. Generated events and times are appended to the history and re-encoded to advance prediction. We studied 461,370 patients with 12 cancer types across 112 centres. Modality-specific paired evaluations linked future images to observed follow-up. With historical images held fixed, removing patient conditioning reduced event F1 from 0.716 to 0.591 and increased lesion-burden error from 11.8% to 21.3%. In free rollouts, eight-step event F1 was 0.672, compared with 0.553 for a longitudinal Transformer evaluated from the same origins, and timing error was lower by 8.7 days. In the internal test set, one-year progression AUROC was 0.882, with values of 0.871 and 0.856 in temporal and geographical external evaluations. These results show that shared patient states connect future phenotypes across observational scales with event-driven trajectory progression, sustaining comparative predictive advantages during rollout and discrimination in external clinical evaluation. Saga makes patient-level disease simulation a multimodal prediction task that can be tested against observed follow-up.

---


### 8. [DRA-SAM: Disagreement-Driven Referential Active SAM for Low-Altitude Drone Referring Segmentation](https://arxiv.org/abs/2610.33057)

**<font color=#1a73e8>作者：</font>** Jisheng Dang, Huaiyuan Peng, Wencan Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring segmentation in low-altitude drone imagery requires distinguishing small, visually similar instances under complex linguistic and spatial constraints. Global inference may yield multiple plausible masks or leave the intended referent insufficiently represented, motivating selective local re-inference. We propose DRA-SAM, a disagreement-driven framework that allocates an additional inference pass according to competing referential hypotheses and an unresolved state. A lightweight EvidenceScorer estimates beliefs over existing candidates and the unresolved state. A training-free Referential Disagreement LOOK policy balances belief-weighted candidate competition and unresolved-region coverage to select a crop for local re-inference. The same benchmark-adapted SAM3-I backbone processes the selected region, and the resulting evidence updates existing hypotheses and introduces new candidates. Among the compared methods, DRA-SAM achieves state-of-the-art performance on six of seven test metrics on both RIS-LAD and UAVid-RIS, including mIoU and P@0.5-P@0.9, and on all seven RIS-LAD validation metrics. On RIS-LAD, DRA-SAM improves the matched global SAM3-I baseline from 49.55 to 52.34 mIoU and from 46.80 to 58.05 P@0.5. On UAVid-RIS, the independently adapted DRA-SAM achieves 73.26 mIoU and 86.86 P@0.5. Controlled crop-policy comparisons demonstrate the effectiveness of disagreement-guided crop selection, while target-size analysis reveals particularly pronounced gains for aerial targets occupying less than 1% of an image. These results establish referential disagreement as an effective criterion for allocating local inference. Code is available at this https URL.

---


### 9. [KDHNet: A Knowledge-Driven Hybrid Network for Limited-Calibration SSVEP Decoding](https://arxiv.org/abs/2610.33058)

**<font color=#1a73e8>作者：</font>** Zhentao He, Ziwei Wang, Dongrui Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Steady-state visual evoked potential (SSVEP)-based brain-computer interfaces (BCIs) achieve high information transfer rates but often require sufficient subject-specific calibration data for reliable decoding. Analytical spatial filters are effective with limited data, but their linear formulations constrain representation capacity. Deep models learn more flexible representations but are prone to overfitting when calibration data are scarce. We propose KDHNet, which combines knowledge-driven analytical processing with data-driven representation learning. After filter-bank preprocessing, cascaded task-discriminant component analysis (TDCA) and task-related component analysis (TRCA) extract discriminative and trial-reproducible components. Learnable sub-band weighting then fuses spectral information, and an SSVEPformer decoder learns temporal and spectral representations for classification. For inter-subject decoding, a target-guided least-squares transformation aligns source trials using one labeled target trial per class. Extensive experiments were performed on three public datasets, covering intra- and inter-subject protocols, five analysis windows, and multiple calibration ratios. In intra-subject evaluation, KDHNet achieved the highest mean accuracy and information transfer rate in 14 of 15 window settings and all ten calibration-ratio settings. In inter-subject evaluation, KDHNet obtained the best or second-best performance, and the gains were generally larger with less calibration data. Ablation studies indicated that the estimated TDCA projection performed better when fixed than when optimized from analytical or random initialization. Combining fixed knowledge priors with trainable neural modules is effective for low-calibration SSVEP decoding. This framework supports more practical, robust, and plug-and-play BCIs. Code is available at this https URL.

---


### 10. [MARC: Mechanism-Aware Reflective Correction for Articulated Object Code Generation](https://arxiv.org/abs/2610.33060)

**<font color=#1a73e8>作者：</font>** Xiong Yang, Junkun Hao, Zijian Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating an articulated object from images and text requires more than plausible parts and movable joints: the assembled mechanism must execute the intended motion. This is particularly challenging for closed-chain and coupled mechanisms, where an error in one connection can block motion or separate connected parts. We introduce MARC, Mechanism-Aware Reflective Correction, which shares an executable kinematic graph across program construction, motion solving, and correction. The graph binds physical connections to local attachment frames and represents loop closures and joint-coordinate couplings. Given prescribed driver inputs, a numerical solver computes follower motion and associates errors with specific connections and configurations. The agent uses these diagnostics to probe possible causes, revise connections or geometry, and retest the mechanism along the original motion paths. On a 20-object test set, MARC with Kimi-K3 achieves 67.8% valid motion coverage and 60.0% overall success, outperforming six baselines. Starting from the same initial candidates, correction improves these scores by 13.7 and 20.0 percentage points, respectively. Ablations further show the benefits of graph-based mechanism support and graph-guided repair. Project homepage: this https URL.

---


### 11. [A Canary in the Neural Mine: Catching an Image Classifier's Silent, Confident Failures](https://arxiv.org/abs/2610.33063)

**<font color=#1a73e8>作者：</font>** Wonseok Shin, Songkuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deployed vision models auto-accept confident predictions, so high-confidence errors propagate silently. Maximum Softmax Probability (MSP), the standard failure predictor, has a structural blind spot: as a scalar read from the classifier head, it is first-order blind to feature variation orthogonal to its confidence gradient. Through a factorial analysis of feature-space detectors, we identify a conditional-redundancy principle explaining why they fail to complement MSP: the class-separability geometry they measure is already encoded in MSP and collapses under fusion. The signal that survives is class-conditional typicality on the off-manifold residual---and because this residual's distribution varies by backbone, from near-Gaussian to heavy-tailed, it must be estimated non-parametrically. We instantiate these findings as CANARY, a training-free detector that computes a per-class kNN distance on the PCA residual of the penultimate feature, percentile-calibrates it on validation data, and fuses it with MSP through a single validation-tuned weight. CANARY's benefit follows a headroom law: gains grow as baseline MSP quality falls, so a single clean-validation number forecasts the improvement. With every parameter selected on in-distribution data alone, CANARY matches or improves 382 of 385 shift cells (e-AURC; 379 on AUROC) across five backbones, with worst-case regression within seed noise ($-0.0002$ AUROC) and the largest gains on natural distribution shifts (ImageNet-A/R, ObjectNet)---where deployed models are most exposed.

---


### 12. [ProtoEEG: Structured Prototype Alignment for EEG Visual Decoding](https://arxiv.org/abs/2610.33065)

**<font color=#1a73e8>作者：</font>** Kieren Yu, Chang Huang, Ziyang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> EEG visual decoding remains difficult because scalp recordings are noisy, spatially coarse, and variable across trials and subjects. Most systems align each trial with a dense image embedding, although that embedding mixes semantic content with instance-specific texture, pose, and background. This target can demand details absent from EEG and provides no explicit account of the visual factors supporting a prediction. We propose \textbf{ProtoEEG}, a prototype-mediated framework that reformulates EEG--image alignment as soft composition over a shared learnable visual codebook. A trainable EEG encoder and a frozen visual teacher produce assignment distributions over the same $K=64$ prototypes. Their weighted reconstructions form a structured representation for retrieval and image generation. Prototype contrast supplies the main cross-modal training signal, distribution alignment coordinates codebook use across modalities, an instance anchor preserves fine-grained discrimination, and diversity regularization prevents redundant prototypes. The shared assignment profile also makes the learned bottleneck directly testable through prototype retention, random selection, and identity shuffling. Across five seeds, ProtoEEG reaches 64.0\% Top-1 and 91.5\% Top-5 on THINGS-EEG2 200-way retrieval. After retraining on EEG-ImageNet, it obtains 44.8\% Top-1 and 73.8\% Top-5 in 80-way retrieval. ProtoEEG also ranks first on all seven reconstruction metrics. Removing prototype contrast lowers Top-1 by 56.9 percentage points, while shuffling prototype identities reduces it to 0.5\%. Prototype analyses further show distributed assignments and broad codebook use rather than one-prototype routing. These results support structured alignment targets as a practical alternative to increasing encoder or teacher capacity alone.

---


### 13. [Decentralized Multi-View, Multi-Zone Tracking for Scalable Camera Networks](https://arxiv.org/abs/2610.33069)

**<font color=#1a73e8>作者：</font>** David Voihanski, Mor Sinai, Ben Zion Bobrovsky  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a decentralized multi-view tracking system for scalable camera networks. Single-view detections are projected to bird's-eye-view (BEV) coordinates and fused by independent multi-view trackers, each managing a dynamic spatial zone. To support scalability across spatially partitioned camera networks, we introduce a decentralized layer for trajectory unification, utilizing a locking protocol and periodic track-merging operations termed global collate. This process is supported by a delayed-output buffering mechanism that retroactively applies history corrections. The configurable delay window absorbs asynchronous coordination latency and helps stabilize cross-zone identity consistency. We detail the design of dynamic zone polygons, consensus-based coordination, and the validation framework, which together maintain global ID consistency with minimal accuracy loss compared to a single-instance baseline in the evaluated configurations.

---


### 14. [PhaseBreak: Proactive Temporal Protection against Unauthorized Image-to-Video Animation](https://arxiv.org/abs/2610.33070)

**<font color=#1a73e8>作者：</font>** Jiashu Zhang, Xuanyou Li, Qixin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-Video (I2V) diffusion models can animate a single portrait or photograph, enabling shared images to be repurposed for motion synthesis without the subject's authorization. We study proactive visual protection against such use: before an image is released, its owner applies a bounded perturbation that preserves the sharing workflow but disrupts downstream motion generation. Existing spectral disruption objectives globally attenuate temporal representations and therefore provide limited control over subtle or spatially localized motion. Our key idea is that generated dynamics depend not only on temporal feature strength, but also on the order in which feature events occur. We propose PhaseBreak, a white-box spectral retiming protection method that matches intermediate denoiser features to a constrained temporal rearrangement of their clean counterparts. PhaseBreak operates along the true temporal axis and uses a subject-aware mask to confine the protective perturbation to the depicted subject. Evaluations on Stable Video Diffusion and DynamiCrafter show that protected images induce greater short-term motion variation and lower temporal regularity, impeding stable motion customization from the released image.

---


### 15. [DuoPIC: Uncertainty-Aware Voxel-Level Digital Twins of Cerebral Perfusion with Transport PDEs in Acute Stroke](https://arxiv.org/abs/2610.33071)

**<font color=#1a73e8>作者：</font>** Anh Duong Tran, Quang-Anh N. D., Toan Sy Pham 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital twins of cerebral perfusion relate tracer dynamics to cerebral blood flow (CBF), blood volume (CBV) and mean transit time (MTT), but must be data-driven, physically consistent and uncertainty-aware. We introduce DuoPIC, a digital twin that needs no reference maps, in which a Windkessel flow model drives a tracer transport partial differential equation (PDE). A population-level neural closure divides each region into fast and slow pathways with tracer mass and MTT conserved by construction, and a tempered posterior quantifies the uncertainty of every estimate. Its voxel maps set the state of the art for lesion detection on ISLES'17 MR (AUC 0.745) and ISLES'24 CT (0.743). On held-out patients, the neural PDE reduced the compartment's reconstruction error by 19% and lifted 95% MTT interval coverage from 88% to 94%. Code: this https URL

---


### 16. [Rethinking Video Storage for AI Training: Breaking Cross-Frame Dependencies for Efficient Random Access](https://arxiv.org/abs/2610.33079)

**<font color=#1a73e8>作者：</font>** Zetian Song, Qize Yu, Yue Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale AI training increasingly relies on massive video datasets with random temporal sampling patterns. However, existing video storage paradigms are optimized for sequential playback and employ sophisticated inter-frame reference structures to maximize compression efficiency. When applied to the random-sampling workloads of AI training, these paradigms face substantial decoding-efficiency bottlenecks. Workarounds such as independent JPEG frames and short groups of pictures (GOPs) reduce decoding work at the cost of larger storage and transfer volumes. In this paper, we identify two sources of decode amplification: sequential reconstruction of unrelated frames and reconstruction of the reference chains required by sampled targets. We address both sources by co-designing the decoding schedule and video reference structure. Dependency-aware sparse decoding reconstructs only requested frames and their required references, skipping unrelated reconstruction without transcoding the source videos. Optional offline Dependency-Decoupled Random Access (DDRA) encoding further reduces reference reconstruction by restricting each interior frame to two bounding intra-coded anchors. Together, sparse decoding and DDRA retain inter-frame prediction while bounding reconstruction to at most three frames per requested target, independent of the intra period. Experiments on a large-scale robotics corpus show that, at comparable reconstruction quality, our method achieves $1.45\times$ the loading throughput of LeRobot v3 with 58.7% less media payload.

---


### 17. [SWIFT-Cell: Segmentation Without Iterative Flow Tracking](https://arxiv.org/abs/2610.33081)

**<font color=#1a73e8>作者：</font>** Devansh Lalwani, Swapnil Bhat, Muralikrishna H H 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalist segmenters such as Cellpose-SAM (CPSAM) outline cells accurately across stains but slowly; watershed detectors such as QuPath's are fast but less accurate. In time-critical use, such as interactive retrieval of cells from a user-drawn region, CPSAM at the reference settings takes 58-303 s per measured 8192 x 8192 region on an RTX 4500 Ada GPU, beyond a seconds-scale interactive target. We distil CPSAM into SWIFT-Cell (SWIFT), a 0.63M-parameter U-Net trained only on CPSAM masks of 1,202 H&E and IHC tiles. On three 8192 x 8192 development regions SWIFT takes 2.0-5.2 s on 4 CPU cores in int8, 2.5-5.1x faster than QuPath's detector on the same cores, and 0.36-0.49 s on a GPU. Against human annotations on eight H&E, IHC and ISH sets it keeps 95% of CPSAM's panoptic quality (PQ) on PanNuke (0.593 vs. 0.627) and is level on NuCLS (0.546 vs. 0.540). On Ki-67 IHC masks scored to the outline centre it is 0.205 PQ above QuPath's better mode, 0.079 below CPSAM and 0.027 below InstanSeg (CI includes 0; at the outer edge 0.008 below CPSAM); on 212 pathologist-outlined nuclei in Ki-67 fields of 12 untouched patients its recall is 0.925 (CPSAM 0.920, InstanSeg 0.901; paired difference CIs include 0); one method-blinded pathologist accepted its outlines in 96% of 100 fields (60 from two development tissue patients, 40 hematology; CPSAM 83%, QuPath 53%; tissue 100% for SWIFT and CPSAM); on ER/PR points from 12 patients its detection F1 is 0.882 (CPSAM 0.896, InstanSeg 0.857), and on 4-reader PD-L1 points 0.83 (CPSAM 0.85, readers 0.87). SWIFT is close to CPSAM in accuracy and faster than watershed detection.

---


### 18. [Inverse Modeling for Laser Pulse Shape Design in Inertial Confinement Fusion](https://arxiv.org/abs/2610.33096)

**<font color=#1a73e8>作者：</font>** Ricardo Luna Gutierrez, Vineet Gundecha, Rahman Ejaz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The achievement of practical fusion energy remains one of the most pressing unsolved scientific challenges, with immense implications for carbon-free power. A critical factor in the success of Inertial Confinement Fusion (ICF) is the design of a Laser Pulse Shape (LP) that can optimally drive implosions under stringent physical constraints. Traditional LP design relies on computationally expensive simulations and manual iterative refinement. We introduce the ICF Laser Pulse Shape Design System (LPDS), a generative inverse modeling framework that maps desired outcomes and target pellet configurations directly to optimized LPs. Crucially, we design a multi-objective loss function to ensure the generated LPs satisfy fundamental physical constraints and experimental requirements. Furthermore, we present constraint-conditioning, inpainting, and gradient-based LP editing mechanisms for fine-grained control over specific pulse characteristics during generation. Moreover, we study the transfer of our framework to a limited set of real experimental shots. Our method establishes a data-driven inverse design framework for LP design in ICF, contributing to the advancement of practical and sustainable fusion energy.

---


### 19. [Artificial Intelligence in Mechanical Engineering: Foundations, Opportunities, Challenges, and Responsibilities](https://arxiv.org/abs/2610.33105)

**<font color=#1a73e8>作者：</font>** A. Cunha Jr, C. Nataraj, L. M. Lorenzo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) is reshaping mechanical engineering (ME), from modeling, simulation, and optimization to diagnostics, design, and technical communication. Drawing on a round-table at the 28th ABCM International Congress on Mechanical Engineering (COBEM 2025), this article presents a structured perspective for the Brazilian and international ME communities. Rather than an exhaustive survey, it examines how AI can enhance engineering practice without compromising scientific rigor. We distinguish statistical learning from human cognition and discuss the capabilities, limitations, and emerging agentic forms of AI. We then consider industrial adoption, workforce changes, and AI-assisted scientific discovery, alongside the energy and infrastructure demands of AI computation and their implications for sustainability and thermal management. The discussion emphasizes the integration of physical knowledge, structured reasoning, and domain expertise into AI systems, particularly in safety-relevant applications. Topics include physics-informed and hybrid learning, physically constrained modeling, validation, uncertainty quantification, and certification. We also examine educational, epistemological, and ethical challenges, including curriculum reform, human-agent collaboration, professional accountability, and the preservation of engineering knowledge. We conclude with principles for responsible AI adoption in ME: physical consistency, rigorous validation, explicit treatment of uncertainty, energy sustainability, human oversight, and ethical responsibility. AI should complement, not replace, engineering judgment.

---


### 20. [Hidden Backdoor Attack on Deep Contrastive Clustering](https://arxiv.org/abs/2610.33116)

**<font color=#1a73e8>作者：</font>** Zifeng Zhou, Shengda Zhuo, Jiahui Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep contrastive clustering has become a representative paradigm for unsupervised image clustering, yet its security under training-time poisoning remains largely unexplored. This paper investigates a hidden backdoor threat against deep contrastive clustering and proposes HBDCC, a Hidden Backdoor attack for Deep Contrastive Clustering. Here, hidden does not indicate that the trigger is visually imperceptible, but rather that the malicious trigger-cluster association remains behaviorally dormant on clean inputs and is activated only when the trigger appears at inference time. HBDCC poisons only a small fraction of unlabeled training samples and exploits an inherent structural weakness of contrastive clustering: augmentation-persistent triggers can be repeatedly aligned across different views at the instance level and further reinforced by cluster-level consistency objectives. As a result, the poisoned model preserves normal clustering behavior on clean data, while producing severely distorted cluster assignments for triggered inputs. We provide a dual-level analysis of the backdoor implantation mechanism and evaluate HBDCC on ImageNet-10, ImageNet-Dogs, and STL-10 with representative contrastive clustering frameworks. Extensive experiments demonstrate that HBDCC can substantially degrade triggered clustering performance in a dataset-dependent manner while maintaining sufficient clean-data utility to evade standard evaluation protocols. We further conduct comprehensive studies on poisoning ratio, attack scope, trigger type, trigger size, and a lightweight knowledge-distillation-based mitigation strategy.

---


### 21. [The Paired Thermal Channel Is Two Orthogonal Axes: A Controlled Attribution Study of Calibration Cost and Detection Gain in Infrared Person Detection](https://arxiv.org/abs/2610.33118)

**<font color=#1a73e8>作者：</font>** Tian Zhang, Yang Chen, Bing Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The calibrated thermal channel in infrared person detection comprises two structurally orthogonal axes. True calibrated $\Delta T$ outperforms scale-matched grayscale pseudo-$\Delta T$ by $+0.0221$ mAP (paired Wilcoxon $p=0.0098$, Cohen's $d=+1.08$), confirming that the calibrated channel carries information the grayscale channel lacks. The calibration axis is driven by the joint pairing-scale condition. Preserving both paired correspondence and absolute calibrated scale raises expected calibration error (ECE) from $\approx 0.05$ to $0.142$. The $2\times 2$ interaction ($p=0.0059$) localizes the rise to this condition. Breaking either factor alone returns ECE to the broken-factor level (true-vs-const $p=0.002$; true-vs-shuffled $p=0.002$). Under post-hoc temperature scaling, the pairing cost survives recalibration ($p=0.002$), while the scale cost is largely absorbed ($p=0.16$). As regards the detection axis, the gain stems from structural de-structuring. Phase randomization, which destroys spatial structure while preserving per-sample variance, yields $+0.0185$ mAP over true $\Delta T$ on FLIR ADAS ($p=0.014$, $d=+0.96$). The FLAME~3 gain is $+0.0064$ mAP ($p=0.078$, n=8). On the calibration axis, the same intervention is insignificant on FLIR ADAS ($p=0.47$) but significant on FLAME~3 ($p=0.0078$). These findings rest on a five-arm controlled attribution with temperature-evidential learning (TEL) as the testbed. TEL obtains a single evidence-derived routing scalar together with a complementary diagnostic entropy, and establishes a finite-evidence degeneracy theorem proving that the acquisition product degenerates to this scalar with a closed-form bound. A physical $0.5^\circ$C threshold admits cross-dataset physical readings, whereas a gray threshold of $20$ inverts without physical interpretation.

---


### 22. [Benchmarking Classical and Quantum Machine Learning for Intrusion Detection Across Multiple Datasets](https://arxiv.org/abs/2610.33119)

**<font color=#1a73e8>作者：</font>** Taha M. Mahmoud, Naima Kaabouch  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Intrusion detection is examined through a comparative benchmark of classical and quantum machine learning models on three datasets: NSL-KDD, UNSW-NB15, and MQTTEEB-D2025. The analysis focuses on how preprocessing decisions, feature selection strategies, and quantum encoding schemes shape model performance on data with differing levels of noise and complexity. A single unified pipeline is applied, covering normalization, class-imbalance handling, dimensionality reduction, and two feature selection methods: Random Forest importance and a quantum-aware approach that combines Quantum Kernel Alignment with Mutual Information (QKA-MI). Four classifiers are compared: Support Vector Machine, Random Forest, Quantum Support Vector Machine, and Pegasos Quantum SVM. The classical models perform consistently across all three datasets, whereas the quantum models depend more strongly on feature representation and kernel alignment. Quantum-aware feature selection yields marked gains for the quantum models, especially on cleaner datasets, while heterogeneous traffic remains difficult. Pegasos Quantum SVM offers a good trade-off between accuracy and computational cost, underscoring the role of preprocessing alignment in practical quantum intrusion detection.

---


### 23. [Inference-Time Prior Adaptation for Imbalanced Data Streams under Concept Drift](https://arxiv.org/abs/2610.33126)

**<font color=#1a73e8>作者：</font>** Tobias Callies, Eirini Ntoutsi, Arthur Zimek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data stream classification under concept drift and class imbalance requires models to adapt continuously while maintaining strong minority-class performance. Many existing approaches rely on active memory management, in- cluding instance removal, memory restructuring, resampling, and synthetic data generation. We present PAI-KNN, a k-nearest neighbor classifier that adapts via inference-time prior adjustment rather than memory modification. PAI-KNN main- tains a simple sliding-window buffer and dynamically adjusts its decision rule using class prior estimates derived from recent observations. Evaluated on a mul- titude of synthetic data streams covering various imbalance and drift scenarios, PAI-KNN achieves competitive performance with state-of-the-art methods, per- forming particularly well under scenarios involving dynamic class imbalance and concept drift. These findings highlight the potential of inference-time adaptation in challenging non-stationary environments and suggest that adaptation in memory- based stream classifiers need not rely exclusively on memory modification.

---


### 24. [Ampe-DB: A Dataset for Human Activity and Interaction Analysis Using the Ghanaian Game Ampe](https://arxiv.org/abs/2610.33130)

**<font color=#1a73e8>作者：</font>** Ruth Senior Biney, Isaac Kojo Yedonu Aboah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human activity recognition benchmarks underrepresent culturally situated forms of movement and interaction. We introduce Ampe-DB, a multimodal dataset based on Ampe, a traditional Ghanaian game involving coordinated jumping, leg movements, and two-person interaction. It contains 637 canonical clips from 15 participants, with RGB video, two-person pose representations, participant and pair metadata, four-class movement labels, and derived binary movement-relation labels.
We evaluate four-class movement recognition and binary movement-relation classification using three protocols: a duplicate-safe fixed benchmark, four-fold pair-held-out evaluation, and participant-held-out diagnostics for participants with complete class coverage. Baselines comprise a frozen Kinetics-400-pretrained R(2+1)D-18 RGB encoder, a two-layer bidirectional GRU for pose sequences, and validation-selected RGB-pose late fusion.
For four-class recognition, RGB macro-F1 falls from 0.955 on the fixed benchmark to 0.418 under pair-held-out evaluation and 0.384 under participant-held-out evaluation. Pose is more robust, achieving 0.957, 0.811, and 0.839 across the same protocols. Fusion reaches 0.976 on the fixed benchmark and 0.824 under pair-held-out evaluation, but does not consistently improve on pose under participant shift. Binary movement-relation recognition also becomes substantially harder under held-out evaluation, especially for different-leg configurations.
These findings show that strong fixed-benchmark scores can mask failures to generalize across people and pairings. Ampe-DB supports research on fine-grained movement recognition, human-human interaction, multimodal learning, and identity-aware generalization.

---


### 25. [Physics Informed Neural Networks for Solving the Drift-Diffusion Equations](https://arxiv.org/abs/2610.33133)

**<font color=#1a73e8>作者：</font>** Luke Ragan, Matteo G. C. Alasio, Enrico Bellotti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The drift-diffusion equations are the fundamental building block for the modeling, design, and optimization of modern semiconductor devices. Solutions of the drift-diffusion equations rarely give way to analytical forms, and exhibit strong nonlinearity, with the solutions ranging over several orders of magnitude. These attributes have led to research into numerical solvers, and while many commercial Technology Computer Aided Design (TCAD) packages now exist, they may require long simulation times, exhibit sensitivity to initial guesses, and rely on mesh generation. Further, these solvers are not well suited for inverse problems where the design parameters of a device are retrieved from its desired functional characteristics. To address all these challenges, this work demonstrates the usage of Physics Informed Neural Networks (PINNs) for the solution of the drift-diffusion equations with errors comparable to traditional simulation software using advanced training techniques to solve problems beyond the well-behaved equilibrium regime. For this study, we specifically choose an abrupt PN-junction in both one and two dimensions that features extreme gradients of the carrier concentrations at the Ohmic contacts and an abrupt discontinuity in the doping profile. Using the proposed PINN architecture, we are able to retrieve accurate results for all observables under all bias conditions. Additionally, we apply the PINN solver towards the inverse problem of retrieving doping profiles directly from desired electric field distributions or electrostatic potentials under non-zero applied biases. Our work establishes a powerful PINNs-based approach for semiconductor device modeling with the ability to solve inverse problems under non-equilibrium conditions for microelectronics research and discovery.

---


### 26. [WorldCast: World-Consistent Character Video Generation with Large-Angle Camera Control](https://arxiv.org/abs/2610.33135)

**<font color=#1a73e8>作者：</font>** Lei Cao, Yu Liu, Wenhua Liao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise camera control is essential for cinematic character video generation, yet existing methods struggle to follow large-angle trajectories with combined rotation, translation, and radius variation from arbitrary initial azimuths. Such viewpoint changes also reveal character regions unseen in the initial frame, causing geometric distortions, appearance degradation, and identity drift. To systematically study these coupled challenges, we introduce CLACT, a large-scale Character-centric dataset and benchmark covering diverse Large-Angle Camera Trajectories, with accurate camera geometry and multi-view character observations for training and evaluation. We further propose WorldCast, a framework for world-consistent character video generation under diverse large-angle camera motions. Specifically, we back-project the initial frame into a 3D point cloud using estimated depth, align the point-cloud scale with the target camera trajectory, and render it along the trajectory to obtain explicit geometric guidance and coverage masks. To complement the incomplete character information, we introduce Geometry-Aligned Memory Attention (GAMA). Using relative camera poses estimated jointly from the initial frame and multi-view character anchors, we express anchor and target-view geometry in a common coordinate frame. GAMA uses this geometric alignment to guide the retrieval and injection of view-relevant character features during generation. Evaluations across diverse large-angle camera trajectories demonstrate accurate trajectory following while preserving character geometry, appearance, and identity.

---


### 27. [Optimal Correction Sets for Provable Redress of Contestable Causal Discovery](https://arxiv.org/abs/2610.33138)

**<font color=#1a73e8>作者：</font>** Fabrizio Russo, Giuseppe Mazzotta, Carmine Dodaro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constraint-based causal discovery relies on conditional-independence (CI) tests that may conflict in finite samples, leaving no causal graph that satisfies them all. Causal Assumption-based Argumentation (ABA) makes these tests explicit as defeasible commitments, and offers correspondence guarantees with a subset of them, but its existing repair procedure releases facts heuristically and offers no formal response to a user's contestation of a release. We argue that contestable causal discovery requires an inspectable repair object, a justification for it, and a predictable revision procedure for such contestations. We therefore formulate CI-fact repair as a minimum-cost correction problem and implement it in Answer Set Programming (ASP). Building on Causal ABA, we provide a compact and efficient ASP encoding of causal consistency, with soundness and completeness guarantees, and a two-way projection correspondence between optimal stable models and minimum-cost correction sets. These results establish fidelity to retained facts, subset-minimality and cost optimality of the repair, conflict-based justifications for released facts, and formally guaranteed redress under user contestations. An empirical evaluation supports the formal account: OptABA-PC retains more correct facts, reduces ambiguity in the compatible outputs, and improves graph reconstruction over Causal ABA on common benchmarks.

---


### 28. [GlanceAR: Repurposing Phone Sensors via Low-Cost Reflectors for Always-On Obstacle Awareness](https://arxiv.org/abs/2610.33142)

**<font color=#1a73e8>作者：</font>** Boyang Zhou, Xizhe Hao, Minbeom Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Smartphone use while walking reduces environmental awareness and can lead to accidents and injury, yet existing obstacle-awareness systems remain unadopted because they require users to hold the phone upright and aimed forward, conflicting with how people actually hold their devices. We introduce GlanceAR, an always-on mobile obstacle-awareness system designed for natural phone-holding postures. GlanceAR utilizes a low-cost passive mirror attachment to redirect the phone's rear LiDAR and RGB camera forward without additional electronic components. In a within-subjects study with N=11 participants navigating indoor and outdoor obstacle courses while engaged in a primary on-phone task, we evaluated three sensing configurations: GlanceAR, a LiDAR-only variant for privacy, and an attachment-free ultra-wide camera baseline. Our findings reveal trade-offs among sensing fidelity, obstacle cue design, and social acceptability, and surface insights around AI complacency and the tension between on-screen task focus and physical safety.

---


### 29. [Learning Pathology-Sensitive Representations for Unsupervised Retinal OCT Anomaly Detection](https://arxiv.org/abs/2610.33143)

**<font color=#1a73e8>作者：</font>** Tania Haghighi, Sina Gholami, Behafarin Emam 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning approaches for retinal optical coherence tomography (OCT) predominantly rely on predefined disease categories, limiting their ability to detect rare or previously unseen abnormalities. While visual foundation models provide transferable representations, their effectiveness in identifying pathological deviations from normal retinal anatomy remains insufficiently understood. In this work, we introduce an unsupervised framework for retinal OCT anomaly detection and localization that adapts pretrained visual representations to normal retinal anatomy through anatomy-aware reconstruction and contrastive triplet learning guided by synthetic structural perturbations, without requiring disease-specific annotations. We systematically investigate the influence of pretraining strategies, anatomy-aware representation adaptation, and anomaly scoring mechanisms on the detection and localization of unseen retinal abnormalities. Our findings demonstrate that adapting pretrained representations to normal retinal structure improves anomaly sensitivity, while pixel-space reconstruction errors and feature-space deviations provide complementary signals for identifying pathological changes. These findings underscore the importance of anatomy-aware representation learning and offer insights into developing generalizable retinal anomaly detection frameworks beyond predefined disease categories.

---


### 30. [Neural-DISCO: Source-Conditioned Counterfactual Editing of Neural Population Activity](https://arxiv.org/abs/2610.33145)

**<font color=#1a73e8>作者：</font>** Nico Policzer, James Ho, Joseph Soo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how neural activity encodes behavioral and sensory variables is a key challenge in systems neuroscience. This requires models that go beyond predicting activity from labels and instead support source-conditioned counterfactual editing: given a recorded source response, we should be able to edit one measured behavioral or stimulus label and predict how neural activity would change while preserving other observed labels and source-specific variability not explained by the labels. Here, we introduce \textbf{Neural-DISCO}, a disentangled representation learning framework for counterfactual modeling of neural activity. Neural-DISCO partitions the latent space into label-specific components, each associated with an observed behavioral or stimulus label, together with a residual latent that captures variability not supplied through observed labels. Across simulated and real neural recording datasets, we show that this structure enables selective editing of measured labels to generate counterfactual neural responses while preserving the remaining content of the original activity. Further, to gain insight into how behavioral and stimulus labels are encoded at single-neuron resolution, we pair this disentangled framework with feature attribution methods that identify which neurons are most important for each label. We find that disentanglement enhances the recovery of known functional cell roles in both synthetic and real data. Together, these results support Neural-DISCO as a framework for counterfactual modeling of neural activity and provide a practical interface for probing how neural populations encode behavior and sensory information. Code is available at this https URL.

---


### 31. [Gaussian Episodic Memory for Long-Term Spatiotemporal Reasoning](https://arxiv.org/abs/2610.33158)

**<font color=#1a73e8>作者：</font>** Ling-Chia Chen, Abdelrhman Werby, Kaan Aytekin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world environments undergo continual semi-static changes, requiring a memory representation that captures both the spatial and temporal evolution of a scene. Existing spatio-temporal memories for robots typically rely either on structured representations, which are limited to the entities and attributes captured during construction, or on image-based memories, which are constrained to previously observed viewpoints. We introduce GEMS, a framework that combines a persistent spatio-temporal 3D Gaussian Splatting (3DGS) map with an agentic reasoning pipeline. The 3DGS map is reconstructed once and subsequently updated only in regions where the scene changes, storing only these modifications while preserving visual detail across time. The agentic pipeline leverages this map to render novel views on demand, iteratively accumulating evidence to answer spatio-temporal questions and ground objects from natural-language queries. To advance future research, we introduce GEMS-Bench, a spatiotemporal question-answering benchmark focused on semi-static environments. It comprises 3 real-world and 12 synthetic environments, spanning 473 question-answer pairs. We evaluate GEMS on novel-view synthesis quality across scene updates, 3D object grounding, spatiotemporal question answering, and storage efficiency. GEMS outperforms recent baselines in 3D object grounding and spatiotemporal question answering, while achieving rendering quality on par with dedicated scene-update methods. Code and data: this https URL

---


### 32. [How Much Fresh Data Should CTR Recalibration Use? A Temporal Evaluation of Post-hoc Calibration](https://arxiv.org/abs/2610.33168)

**<font color=#1a73e8>作者：</font>** Rui Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline evaluation of click-through rate (CTR) models still defaults to random splits, although deployed models score future traffic and downstream systems consume calibrated probabilities. On Avazu (40.4M impressions) we train logistic regression (LR), DeepFM, and DCN-v2 under two rolling temporal origins and a random split, three seeds per arm, and recalibrate each test day with Platt scaling and isotonic regression fitted on the preceding hours. At origin 1's nearest test day, random splits report LR's expected calibration error (ECE) at 55-62% of the temporal value in every seed (the deep models' ratio is seed-unstable), and no model's ECE is monotone in temporal distance. With a 6-hour fitting slice, recalibration removes up to 61% of ECE in badly miscalibrated cells but increases it in about a third of applications (14-17 of 48 across seeds). On fixed evaluation sets, a 12-hour slice cuts harm from 13-17 to 3-5 of 36 applications, and 24 hours raises it again. The 12-hour slice subsampled to the 1-hour slice's size (5% of the impressions; 20-25x faster to fit) recovers 88% of the full slice's gain, so impression count alone does not explain it. A slice-ECE gate shows no benefit out-of-origin, and in a simulated auction recalibration moves profit by only about -0.21% to +0.26%. Offline protocols should measure calibration temporally, over multiple origins and seeds; in this data, recalibration fitted on a wide time span beat the freshest few hours, which other logs must confirm.

---


### 33. [World-in-Context: Interactive Video World Modeling with In-Context Conditioning](https://arxiv.org/abs/2610.33169)

**<font color=#1a73e8>作者：</font>** Harold Haodong Chen, Rui Peng, Rongjin Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video world models require coordinated control over viewing perspectives, character actions, and camera motion. Existing methods typically leave view modes implicit in text captions, conflate action with camera motion, and inject controls through fragmented architectural pathways that capture interdependencies only indirectly. In this work, we present World-in-Context, an interactive world modeling framework powered by In-Context Conditioning (ICC). Rather than relying on specialized conditioning pathways, World-in-Context unifies view, action, and camera controls into explicit tokens contextualized directly within a shared self-attention space. Our formulation reveals that (i) explicit view tokens disentangle conflicting dynamics and unlock emergent view switching from single-view data, while (ii) action and camera inputs play complementary roles in governing local responsiveness and global stability. To preserve temporal continuity across execution intervals, we further introduce Interaction-Transport RoPE (IT-RoPE), parameterizing temporal attention with accumulated control transitions. On WBench, World-in-Context-5B achieves navigation performance on par with 22B EchoWM ($81.5$ vs. $81.6$) and attains a $93.8\%$ perspective-switching success rate, substantially outperforming existing 5B baselines ($18.8\%$). Controlled analyses further demonstrate compounding advantages of World-in-Context under richer conditioning mixtures, favorable data efficiency, and natural applicability to causal rollouts.

---


### 34. [Whale You Go Green? Immediate and Longitudinal Effects of Embodied Conversational AI Avatars on Sustainable Behavioral Tendencies and Pro-Environmental Attitudes](https://arxiv.org/abs/2610.33191)

**<font color=#1a73e8>作者：</font>** Rachel Poonsiriwong, Pat Pataranutaporn  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Embodied conversational AI can be persuasive, but can it motivate people to develop sustainable behavioral tendencies and increase pro-environmental attitudes? We conducted a randomized experiment (N = 576) comparing four embodied avatars--a beluga whale, Greta Thunberg, Emma Watson, and a generic human--with a text chatbot and no-intervention control. All embodied conditions increased immediate sustainable product selection relative to the control (beta = .401-.609, all q <= .0126) and chatbot (beta = .398-.604, all q <= .007), without differing significantly from one another. Only the Beluga condition increased immediate pro-environmental attitudes relative to the control after correction. Among 287 returners assessed two months later, following an intermediate assigned-condition session, Beluga also showed significantly higher pre-booster sustainable product choice compared to the control (beta = .657, q = .0176). Although it did not significantly outperform other embodied agents, these findings establish the immediate potential of nonhuman embodied avatar interfaces as a promising direction for memorable environmental interventions.

---


### 35. [Support-guided OOD Removal with Diffusion](https://arxiv.org/abs/2610.33194)

**<font color=#1a73e8>作者：</font>** Alireza Kheirandish, Sara Fridovich-Keil  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many real-world signals are corrupted by localized, structured perturbations whose distribution is unknown: an intermittent background noise in a music recording, a watermark stamped on a photograph, a cast shadow. We study the task of recovering a clean signal $x$ from an observation $y$ containing such a localized out-of-distribution (OOD) corruption. We propose Support-guided OOD Removal with Diffusion, SORD, an iterative algorithm to recover $x$ using only two ingredients: a binary map of the corruption support and a single diffusion model pretrained on clean signals. SORD does not require any paired data or any statistical model of the corruption. We evaluate SORD on natural images and human faces with spatially localized corruptions including handwritten digits, other images, watermarks, and shadows, as well as audio recordings of different musical instruments with temporally localized corruptions including other instruments and human speech. SORD is competitive with, and often outperforms, posterior-sampling inpainting given the same diffusion prior and the same mask, source-separation baselines that require a separate diffusion model for each source, and, on several benchmarks, supervised networks trained on paired clean and corrupted signals. The code is released here: \href{this https URL}{this https URL}.

---


### 36. [Isharah-Selfie: Continuous Sign Language Recognition Dataset for One-handed Signing](https://arxiv.org/abs/2610.33200)

**<font color=#1a73e8>作者：</font>** Ahmed Abul Hasanaath, Murtadha Aljubran, Sarah Alyami 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current sign language recognition and translation benchmarks are commonly collected in controlled settings using fixed or studio-style cameras, particularly limiting their ability to reflect how signers communicate in everyday mobile scenarios. As such, this gap becomes increasingly evident when considering the Arabic Sign Language (ArSL), which is a primary sign language used across Arab countries. In this work, we introduce Isharah-Selfie, a large-scale ArSL dataset collected entirely using front-facing smartphone cameras under unconstrained selfie conditions. The dataset comprises 8,997 video clips performed by 16 signers across 1,493 unique sentences, covering several domains such as healthcare, education, and transportation. Unlike conventional datasets dominated by fixed-camera, two-handed signing, Isharah-Selfie captures realistic mobile communication characterized by one-handed signing, close-range viewpoints, partial body visibility, camera motion, unconstrained environments, and heterogeneous device resolutions. Each video is annotated with both gloss sequences for continuous sign language recognition (CSLR) and Arabic sentence translations for sign language translation (SLT). Moreover, we define signer-independent and unseen-sentences evaluation protocols to assess generalization across unseen signers and novel sentence compositions. Extensive benchmarks using RGB-based and pose-based data show that current CSLR and SLT methods remain challenged by selfie-style signing conditions, particularly under unseen-sentence evaluation, where compositional generalization remains weak. By releasing Isharah-Selfie, we aim to support research toward robust, user-centered sign language technologies that operate reliably in realistic smartphone-based communication settings. The Isharah-Selfie dataset is available on this https URL.

---


### 37. [A-GE: Privacy-Preserving Age Assurance via Fine-Grained Motion](https://arxiv.org/abs/2610.33206)

**<font color=#1a73e8>作者：</font>** Mohammed Gharib, Giovanni Cascone, Martin Zizi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Age assurance faces a fundamental privacy dilemma: meaningful assurance typically requires revealing identity or other sensitive information, whereas privacy-preserving alternatives often provide little assurance. Existing approaches either disclose sensitive information directly or shift the disclosure and trust requirement to an identity provider, while self-declared age provides little meaningful assurance. Thus, a fundamental gap remains between establishing an age property and revealing information beyond what is necessary to establish that property. We present \textit{A-GE} (Age-Grounded Evidence), a privacy-preserving age assurance system that derives age-related evidence from fine-grained motion captured by commodity inertial measurement units (IMUs). A-GE exploits subtle motion dynamics that we hypothesize reflect underlying neuromuscular and physiological processes during ordinary device interaction. It requires neither identity information nor government identification and operates across available sensor sampling rates, including the approximately 60~Hz limit of web-based sensing, with configurable minimum-age thresholds ranging from 14 to 21 years. We evaluate A-GE on more than 600 participants, with separate participant-disjoint cohorts for model development and final evaluation. At a 16-year minimum-age threshold, A-GE achieves up to 93.8\% accuracy with a comparable F1 score across the evaluated configurations. We further demonstrate client-side deployment on Android, iOS, and the web, and examine unintended attribute inference and residual privacy risks, characterizing both the privacy benefits and limitations of deriving age evidence from commodity motion.

---


### 38. [Lower expected Fisher rank implies better PAC generalization](https://arxiv.org/abs/2610.33208)

**<font color=#1a73e8>作者：</font>** Marco Miani, Albert Kjøller Jacobsen, Albert Lopez i Serrano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning architectures tend to generalize well to unseen data, but explaining this capability is still an open area of research. Under the assumption of i.i.d. data, PAC-Bayes provides a bound on generalization error, and its tightness relies on a parameter distribution that covers a large volume of low-loss solutions. The Fisher information metric endows the parameter space with a geometry for which distances reflect functional changes, and whose zero-component captures functional invariances. We define and study a Fisher-aligned parameter distribution for which we can simultaneously guarantee (1) a low-loss, thanks to the exploration constrained on the functional invariances and (2) a large log-volume of parameters, proportional to the number of zero eigenvalues. This distribution results in a high-probability generalization error bound, which scales with the expected rank of the Fisher information matrix, shedding light on the relevance of this quantity.

---


### 39. [Model-agnostic predictability quantification of multivariable time series](https://arxiv.org/abs/2610.33209)

**<font color=#1a73e8>作者：</font>** Yuxuan Shu, Vasileios Lampos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariable time series forecasting plays an important role in various domains, where predictions depend on complex interactions among covariates. Forecasting models are commonly evaluated across numerous benchmark datasets. However, forecasting accuracy reflects both model capability and task predictability, making it difficult to characterise the difficulty of a task independently of the model used. Existing predictability measures often fail to capture nonlinear dependencies or are limited to univariate series. In this work, we propose Multivariable Predictability Score (MAPS), a model-agnostic metric for measuring the intrinsic predictability of multivariable time series forecasting tasks. MAPS uses covariate information to assess predictability across different lookback windows and forecasting horizons, and provides a quantitative assessment of the predictive information available for forecasting. We evaluate MAPS across synthetic and real-world forecasting datasets against 6 baseline predictability measures. The former confirms that our method closely aligns with the expected reference predictability (r=0.963). Empirical results further corroborate that MAPS yields more reliable projections in the majority of experimental configurations.

---


### 40. [The Locality Trade-off in Masked Patch Self-Distillation](https://arxiv.org/abs/2610.33223)

**<font color=#1a73e8>作者：</font>** Xi Weng, Zhaoyu Liu, Lianyu Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Masked patch self-distillation is a key component of modern vision foundation models, including DINOv2 and DINOv3, yet its implications for local visual information remain unclear. We show that its semantic benefits can coexist with a scale-dependent locality cost. Using two annotation-free diagnostics, we distinguish recoverable local appearance from spatial correspondence. In smaller models, adding iBOT substantially weakens patch correspondence while largely preserving appearance decodability. In larger models, correspondence improves, but pixel and texture evidence becomes less linearly accessible in deep features. Thus, scaling changes the form of the locality cost rather than uniformly eliminating it. Our analysis of Gram anchoring further shows that preserving patch relations does not guarantee simultaneous improvements in both properties. These findings motivate evaluating and designing visual representations around the complementary demands of semantic abstraction, appearance preservation, and spatial correspondence. Our code is available at this https URL.

---


### 41. [Holo-NN: Holographic Nearest Neighbor Search via Compressive Sensing](https://arxiv.org/abs/2610.33224)

**<font color=#1a73e8>作者：</font>** Bryant Gipson  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the age of AI, privacy-preserving approximate nearest neighbor (ANN) search over high-dimensional embeddings has emerged as a critical yet frustratingly challenging domain, dominated by tradeoffs between speed, privacy, and accuracy. Traditional tree and graph-based indexing structures (e.g., HNSW, ScaNN) rely fundamentally on non-linear operations that are computationally intractable under Fully Homomorphic Encryption (FHE) or blind server-side constraints.
In this paper, we introduce Holo-NN (Holographic Nearest Neighbor Search), an algebraic framework that replaces data-dependent branching with a single linear projection. Our key observation is that while distances across a database are dense, neighborhood membership is inherently sparse: only a handful of points ever lie close to a query. By pairing locality-preserving feature transforms with Compressive Sensing, Holo-NN folds the entire database offline into a compact holographic sensing matrix. At query time, encrypted search reduces to a single, non-interactive matrix-vector multiplication---requiring no FHE bootstrapping, no multi-round interaction, and no client-side index state. This turns private retrieval into an embarrassingly parallel, accuracy-tunable computation that runs out of the box on both CPUs and GPUs, scaling efficiently to production databases. We offer a comparison against other state-of-the-art Private ANN algorithms to help situate the method in the broader context of production-grade private retrieval.

---


### 42. [Distilling Expert Judgment at Scale](https://arxiv.org/abs/2610.33233)

**<font color=#1a73e8>作者：</font>** Robbie Goldfarb, Andrew B. Hall, Jillian Fisher 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier AI models are increasingly deployed on topics where the stakes are high and expert judgment is required, including healthcare, defense, finance, governance, and politics. We present a general methodology for distilling expert human judgment into automated evaluation systems that operate at scale. Our approach assembles networks of domain experts and develops techniques for extracting not just their conclusions but their reasoning processes, encoding those processes into structured editorial standards that automated judges can apply continuously. We ground our approach in a long tradition of research on the nature of expertise and the conditions under which expert judgment is reliable and more effective than other approaches, and argue that independent, expert-calibrated evaluation is necessary not only on epistemic grounds but as a matter of accountability and public trust. We validate the methodology on AI news reporting as a first application domain. On source quality, two independent domain experts achieve Krippendorff's $\alpha = 0.83/0.69$ on a held-out test set when applying the editorial standards, and our automated judge reaches $F1 = 0.81/0.97$ against expert consensus. On neutrality, experts achieve $\alpha = .72$ on the test set, and the automated judge reaches $F1 = 0.86$ against expert consensus. Additionally, a controlled comparison shows that expert-calibrated judges substantially outperform uncalibrated frontier models on every source-quality metric, demonstrating that encoding expert reasoning is the critical step that prompt engineering alone cannot replace. We present this benchmark as a proof of concept for a broader evaluation infrastructure applicable to any domain where judgment matters and expertise is scarce.

---


### 43. [Alignment of Autonomous Cyber Defense Agents via Adaptive Policy Shaping](https://arxiv.org/abs/2610.33234)

**<font color=#1a73e8>作者：</font>** Dena Mujtaba, Bharadwaj Ravichandran, Brian Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity operators increasingly encounter sophisticated and fast-paced attacks, making autonomous cyber defense (ACD) a critical approach for supporting timely and effective decision-making. Reinforcement learning (RL)-based ACD agents have the ability to autonomously observe network states and take actions to defend and recover system assets, making them well suited for ACD. However, these agents often face critical trade-offs, such as improving network security while inadvertently degrading service availability or violating other operational priorities such as confidentiality and integrity, raising the core challenge of aligning agent behavior with human-specified goals and intent. In this work, we study the problem of aligning RL-based ACD agents with human-specified operational objectives without requiring costly retraining. We formalize alignment for ACD as a policy shaping problem, where a pretrained RL decision-making policy can be adjusted at test time using predicted attributes over agent actions. We also propose an adaptive approach that dynamically controls the alignment--performance trade-off as operational priorities shift during an ongoing cyber attack. We evaluate our method in a simulated cyber defense environment, CybORG, analyzing performance across multiple alignment objectives using the Confidentiality, Integrity, and Availability (CIA) information security triad. Our results show that adaptive test-time policy shaping can significantly improve alignment while preserving core cyber defense performance, offering a practical and scalable alternative to training-time alignment methods in RL. Our code is publicly available at this https URL.

---


### 44. [NewsBench: Expert-Grounded Evaluation of Epistemic Quality in AI News Reporting](https://arxiv.org/abs/2610.33240)

**<font color=#1a73e8>作者：</font>** Matt Wilde, Jillian Fisher, Andrew B. Hall 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As frontier AI systems increasingly serve as sources of political and current-events information, evaluating the epistemic quality of their responses is now especially consequential. Existing evaluations often focus narrowly on ideological alignment, rely on measures not validated for this setting, or depend on reference labels derived from public opinion or non-expert annotation, potentially producing misleading or miscalibrated results. To address these limitations, we introduce NewsBench, an expert-grounded benchmark that reframes evaluation around editorial standards developed by senior practitioners in journalism, policy, and intelligence analysis. NewsBench operationalizes quality across three dimensions, source quality, factuality, and neutrality, using a two-phase pipeline in which domain experts first define and calibrate evaluation guidelines, which are then transferred to automated AI judges validated against expert-adjudicated gold labels. The benchmark includes approximately $3,000$ evaluation prompts, with roughly $500$ refreshed monthly to capture emerging current events, roughly $2,500$ human expert-annotated items for calibration and validation, and a suite of AI judges designed to enable scalable evaluation. To validate our methodology, we report both inter-rater reliability among human experts and AI judge--human agreement across all three dimensions. Finally, we apply NewsBench to four frontier models, revealing distinct and non-overlapping failure profiles in sourcing, factuality, and neutrality.

---


### 45. [Automated identification of ivory carvings using machine learning: A proof-of-concept approach to detecting the illegal wildlife trade](https://arxiv.org/abs/2610.33243)

**<font color=#1a73e8>作者：</font>** Andrius Tamosiunas, Simone Mozzon, David Bacon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite a ban on the international trading of recently poached ivory, elephants are still killed for their tusks. Ivory and its products are mainly sold in online marketplaces. However, due to the huge volume and variety of adverts and the similarity of ivory with other materials that can be legally sold, it is hard for enforcement officials to identify illicit trading and prosecute sellers. Existing techniques for identifying elephant ivory, such as Fourier-transform infrared spectroscopy and microscopy, can reliably distinguish ivory from other materials, but require physical access to the item and cannot be applied to photographs alone. As a result, these methods are unsuitable for screening the large volume of images posted in online marketplaces, leaving a gap for automated, image-based identification tools. In this proof of concept work, we investigate the potential of machine learning techniques for image analysis to automatically distinguish ivory objects from bone. We employ a semantic segmentation framework using a U-Net architecture with a ResNet34 backbone, leveraging transfer learning on an augmented dataset of 541 original images. Using a dataset of images of ivory and items resembling carved ivory, several models were trialled. On a distinct test set, the classifier achieved an Area Under the Curve (AUC) of 0.81 and an overall classification accuracy of 81% on confident samples. The paper presents the best-performing model as a proof of concept for developing a system that can effectively identify ivory and its products when indicative features of elephant ivory are present in an image. This work provides initial steps towards a machine learning-based framework designed to advise law-enforcement in detecting illegal elephant ivory trade.

---


### 46. [Reinforcement Learning for Controller Parameters in the Auto-Bidding System at Pinterest](https://arxiv.org/abs/2610.33248)

**<font color=#1a73e8>作者：</font>** Yichu Zhou, Qinyi Chen, Fei Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auto-bidding systems in online advertising must balance competing objectives-maximizing budget delivery while minimizing cost per action-across heterogeneous campaigns under non-stationary market conditions. This trade-off evolves over campaign lifespans: early on, cost optimization dominates when budgets roll over; near deadlines, budget delivery becomes urgent. While PID controllers are widely used in production for their stability and interpretability, fixed tunings cannot adapt to diverse campaigns and shifting traffic patterns. We present RLBP (Reinforcement Learning for Bidding Parameters), a hybrid architecture deployed at Pinterest that uses RL as a meta-controller to select campaign-specific PID parameters daily while retaining PID for high-frequency bid adjustments. RLBP trains a multi-head Q-network using a relative-lift reward formulation normalized against the production baseline, and performs inference-time fusion that adapts the cost-delivery trade-off to campaign states without retraining. Through online A/B testing at Pinterest, RLBP achieves a statistically significant reduction in effective cost-per-click (eCPC) with no revenue degradation, and two months of post-rollout measurements against a holdout also show consistent cost reductions. These results demonstrate that meta-controller RL can successfully augment production control systems at scale.

---


### 47. [RadonBench: A Benchmark of Classical and Learning-Guided Search Techniques for Problems in Combinatorial Geometry](https://arxiv.org/abs/2610.33259)

**<font color=#1a73e8>作者：</font>** Xiaoan Xu, Ethan X. Fang, Jesus A. De Loera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical optimization and learning-guided search offer complementary approaches to open problems in discrete mathematics, but their outputs are difficult to compare when search spaces, validity checks, and stopping rules differ. We present \emph{RadonBench}, a benchmark for constructing maximum-cardinality Radon-free lattice configurations: finite subsets of $\mathbb{Z}^d$ admitting no integral Radon partition. It remains open whether Radon-free configurations with $11$ points in $\mathbb{Z}^3$ or $21$ points in $\mathbb{Z}^4$ are possible. If they exist, they would improve the corresponding lower bounds on the integer Radon numbers. We compare exhaustive extension, greedy local search, PatternBoost, AlphaZero, and AlphaEvolve. All outputs use one success predicate: a convex target-sized configuration succeeds exactly when its number of integral Radon points is zero. PatternBoost and AlphaZero construct verified Radon-free configurations of sizes $10$ and $20$, one point short of the respective targets; AlphaZero's best convex target terminals have two integral Radon points in both dimensions. Exhaustive extension over fixed seeds and declared finite search boxes likewise reaches a minimum of two integral Radon points. Greedy local search and AlphaEvolve each produce target-sized near misses with one integral Radon point. No audited run reaches zero. These results establish reproducible near-miss baselines over explicitly scoped search domains.

---


### 48. [Explaining Basketball Shot Classifications with Grad-CAM: An Investigation of Shortcut Reliance with Spatiotemporal Correlations](https://arxiv.org/abs/2610.33263)

**<font color=#1a73e8>作者：</font>** Hongyi Tian, Robin Cohen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Basketball action recognition is used in high-stakes scenarios to inform such tasks as specialized coaching, yet the evidence used by its deep-learning models is poorly understood. This paper investigates whether there is evidence that an R(2+1)D-18 model trained on the Basketball-51 dataset relies on spurious spatiotemporal correlations when classifying basketball shot outcomes. Gradient-weighted Class Activation Mapping (Grad-CAM) was used to generate spatiotemporal saliency maps, whose faithfulness was evaluated by progressively blurring the most salient pixels. Twenty saliency maps were then visually reviewed for recurring salient regions. Grad-CAM highlighted spatially central regions of clips including the shooter, net, and occasionally the courtside crowd. Blurring interventions were conducted to support these patterns. Blurring the central region resulted in an accuracy of 43.7%, compared to the original test accuracy of 69.3% and random-blurred accuracy of 50.9%. The additional 7.2 percentage-point reduction from central blurring compared to random blurring suggests that the model relies on task-relevant visual regions; this highlights the need for continual audits to ensure trustworthy, equitable sports analytics.

---


### 49. [Individual Fairness via Local Predictive Consistency](https://arxiv.org/abs/2610.33285)

**<font color=#1a73e8>作者：</font>** Zhouting Zhao, Tin Lok James Ng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Individual fairness in machine learning requires that similar individuals receive similar predictions. Most existing definitions are pairwise in nature, imposing a Lipschitz constraint that must hold either globally across all pairs of data instances or locally within specified neighborhoods. In practice, however, such pairwise constraints may be overly restrictive and may not directly identify which individuals receive locally inconsistent predictions. We study local predictive consistency as a node-level relaxation of pairwise individual fairness, where each prediction is compared with a similarity-weighted average of predictions in its local neighborhood. This yields an interpretable node-level fairness score and a corresponding regularized learning approach based on local residuals. Since graph-based individual fairness depends critically on the underlying similarity structure, we make the construction of the neighborhood graph explicit and discuss threshold selection through graph-coverage diagnostics. Our approach applies to binary classification, regression, and time-to-event prediction. We further compare this formulation with pairwise constraint-based approaches and analyze the resulting fairness--performance trade-offs.

---


### 50. [The As-If Machine: Personalized counterfactuals make distant policy risks feel close](https://arxiv.org/abs/2610.33301)

**<font color=#1a73e8>作者：</font>** Joshua Ashkinaze, Yubo Zhou, Pengyu Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Life experiences can shape policy attitudes, but we only live one life. Citizens may therefore fail to support policies addressing risks they have never personally experienced. Narratives can make such risks immediate and personal, but personalized stories remain difficult to produce at scale. Here we ask whether AI can make distant scenarios feel concrete by simulating a participant's life as if that scenario occurred. We present the As-If Machine (AIM), a multi-agent system through which people co-write personalized counterfactual narratives---stories about their own lives under different policy futures. In two pre-registered and quota-matched experiments on science funding (N=1,007) and satellite cybersecurity (N=894), we compared AIM with two controls: reading an expert-written vignette on the same topic and co-writing with AIM about an unrelated topic. AIM increased psychological closeness---how close a risk feels to the self---by nearly identical margins in the two domains (0.36 and 0.38 standard deviations (SDs) against the vignette, 0.80 and 0.90 against unrelated writing). AIM increased psychological closeness even among participants with unfavorable views of AI. For policy attitudes, AIM's effects were 0.16 SDs against the vignette and 0.10 SDs (n.s.) against unrelated writing for science funding; the corresponding effects for satellite cybersecurity were 0.54 and 0.67 SDs. Across 23,496 human-AI autocomplete interactions, participants and the system played distinct roles: AIM supplied concrete detail that grounded the scenario, and participants supplied first-person perspective and emotion. Co-writing with the As-If Machine makes distant policy risks feel close.

---


> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-446](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
