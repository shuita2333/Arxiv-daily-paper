# 📦 其他研究 | 2026年10月05日

> 本类共 **385** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-385](./part-08.md)

---

### 1. [Reverse Item Response Theory for Sparsity-Robust Ranking in Fragmented Cancer Drug-Response Matrices](https://arxiv.org/abs/2610.00002)

**<font color=#1a73e8>作者：</font>** Jung Min Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce reverse Item Response Theory (IRT) to pharmacogenomic drug-response analysis by treating cancer types as latent "subjects" with resistance ability and drugs as "items" with evasion difficulty. Applied to 242,036 drug sensitivity measurements from the Genomics of Drug Sensitivity in Cancer (GDSC2) database, the model estimates cancer-type-level in-vitro resistance and drug-level broad activity on a shared latent scale. Validation across four missingness regimes demonstrates that reverse IRT better recovers the full-data latent ranking than simple averaging, with advantages of Delta-rho = +0.089 to +0.095 at 60% missingness under MCAR, cancer-biased, and drug-biased sparsity. Held-out prediction confirms IRT achieves the best Brier score among five evaluated methods. Bootstrap confidence intervals show 19 of 28 cancer types have stable resistant/sensitive classifications. Cross-platform PRISM replication shows 82% directional agreement but weak rank-order correlation (rho = 0.25), indicating the contribution is methodological robustness under fragmented evaluation, not a universal clinical resistance leaderboard.

---


### 2. [STATERA: Hidden Mass Estimation via Zero-Shot Sim-to-Real Kinematics using Frozen Temporal Tubelets](https://arxiv.org/abs/2610.00003)

**<font color=#1a73e8>作者：</font>** Animesh Varma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision models pretrained for frame-level appearance often struggle to infer hidden physical properties from motion. We study center-of-mass (CoM) localization for opaque, asymmetric rigid bodies from short monocular videos, where surface cues and point tracking are unreliable under self-occlusion. We propose STATERA, which adapts a pretrained video backbone (V-JEPA) with mostly frozen weights and a lightweight temporal tubelet mixer to predict per-frame CoM heatmaps and trajectories. To support this task, we introduce the HiddenMass Benchmark, comprising 50K MuJoCo trajectories and a 63-sequence real-world test set with physically calibrated CoM ground truth. In simulation, STATERA-50K-Sigma improves normalized CoM error from 41.7% (DINOv2) to 25.2%. In zero-shot sim-to-real transfer, we observe a fundamental trade-off in supervision: phase-aware targets can induce bimodal predictions, while phase-agnostic targets can collapse toward statistically safe centroids. Nevertheless, our phase-aware STATERA-50K-Crescent is the only evaluated method that demonstrates consistent movement toward the true hidden offset. While this leads to a monocular vector overshoot artifact that marginally increases absolute Euclidean error compared to a static geometric centroid, it improves physics capture from 2.6% to 41.0%. These results suggest that frozen temporal representations can better separate inertial dynamics from visual geometry for hidden-parameter estimation.

---


### 3. [How Far is Adam from Natural Gradient Descent?](https://arxiv.org/abs/2610.00004)

**<font color=#1a73e8>作者：</font>** Vihaan Paka-Hegde  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adam is the standard optimizer in deep learning, yet its geometric relationship to natural gradient descent (NGD) contains unresolved questions. We study Adam's full update rule, including momentum, as a diagonal empirical Fisher approximation subject to diagonal truncation, empirical label substitution, and temporal lag. Using the scale-invariant $\gamma(\Delta\theta)$ metric, we measure Adam's geometric deviation from true NGD across four loss landscapes: well-conditioned linear regression, ill-conditioned linear regression, logistic regression, and a non-convex small neural network. Adam's geometric trajectory is context-dependent. Deviation remains low in well-conditioned settings but rises significantly under ill-conditioning, reaching misalignments of $\approx 10^3$ in the neural network. Higher geometric drift correlates with slower initial optimization but does not degrade final objective minimization; Adam consistently reaches low loss. Furthermore, the improved empirical Fisher (iEF) tracks more stable paths than the standard empirical Fisher (EF), which frequently oscillates or diverges. Our results suggest Adam's practical optimization power may stem from a balance of structural approximation errors and momentum smoothing rather than close tracking of the natural gradient path.

---


### 4. [Emergent Object Binding Has a Finite Spatial Horizon](https://arxiv.org/abs/2610.00006)

**<font color=#1a73e8>作者：</font>** Mayank Singal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained Vision Transformers encode whether two image patches belong to the same object. This IsSameObject signal is decodable from frozen patch embeddings at high accuracy, which suggests that object binding emerges from self-supervised pretraining alone. We show that this single accuracy number hides the structure of the signal. Binding is local: the probability that two patches of the same object are decoded as bound falls off monotonically with the distance between them and levels off at a nonzero floor, a falloff well described by an exponential with a finite length scale. This decay holds across object sizes, across three families of probe, on both ADE20K and COCO, and across DINO and CLIP backbones, which indicates that it is a property of the representation rather than of the decoder. Reading binding as local spatial coherence with a finite range accounts for a set of behaviors that the aggregate score leaves unexplained: binding weakens on large objects, separates distinct objects of the same class less reliably than objects of different classes, and groups object parts with their wholes. It is, by contrast, unaffected by occlusion once object size is controlled. We map each behavior with confounds controlled. As a preliminary observation, the horizon and its floor are organized at different depths in DINOv2 and DINOv3, which we report as suggestive given the small number of layers probed and the confound between the two models.

---


### 5. [Spatial Lifting for Dense Prediction](https://arxiv.org/abs/2610.00017)

**<font color=#1a73e8>作者：</font>** Mingzhi Xu, Tao Zhou, Yong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Spatial Lifting (SL), a novel methodology for dense prediction tasks. SL operates by lifting standard inputs, such as 2D images, into a higher-dimensional space and subsequently processing them using networks designed for that higher dimension, such as a 3D U-Net. Counterintuitively, this dimensionality lifting allows us to achieve good performance on benchmark tasks compared to conventional approaches, while reducing inference costs and \textbf{drastically lowering the number of model parameters}. The SL framework produces intrinsically structured outputs along the lifted dimension. This emergent structure facilitates dense supervision during training and enables single-forward-pass self-consistency-based quality and uncertainty estimation at test time. Spatial Lifting introduces a simple and general modeling strategy that offers a promising path toward more efficient, accurate, and reliable deep networks for dense prediction tasks in vision.

---


### 6. [Domain generalization and synthetic data in object detection: the enabler, the probe, and the gap](https://arxiv.org/abs/2610.00030)

**<font color=#1a73e8>作者：</font>** Elfi I.S. Hofmeijer, Ella P. Fokkinga, Friso G. Heslinga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection models often experience performance degradation when deployed under distribution shifts, caused by for example changes in weather type, operational environment, or object appearance. Domain Generalization (DG) aims to develop models that remain robust under such shifts and generalize well to unseen domains. DG research specifically focused on object detection models is scarce, although these models face additional challenges around localization and multi-scale representations. Synthetic data is a promising tool to support in DG, by enabling large-scale generation of diverse new samples. In this paper, we present an object detection-centric review of DG and examine the role of synthetic data from three complementary perspectives. First, synthetic data acts as an enabler of DG through diversification and alignment strategies that aim to improve robustness to distribution shifts. Second, it serves as a probe that enables controlled experimentation to identify and understand failure modes. Third, we discuss the synthetic-to-real gap, a particularly challenging form of domain shift that arises when models trained on synthetic imagery are deployed on real-world data. Through reviewing these perspectives, we identify limitations of current DG approaches for object detection and argue that future research requires representation-aware methods that explicitly address both localization and classification under domain shift.

---


### 7. [Integrating Fairness and Explainability in a Multiple Instance Reinforcement Learning System](https://arxiv.org/abs/2610.00035)

**<font color=#1a73e8>作者：</font>** Bente Hinkenhuis, Seyed Sahand Mohammadi Ziabari, Ali Mohammed Mansoor Alsahag  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting student performance from educational interaction data requires models that are both accurate and sufficiently transparent to support meaningful intervention, while demographic information introduces an additional risk of unfair predictions. This study investigates a multi-objective framework that combines reinforcement learning-based multiple instance learning (RL-MIL), adversarial debiasing, and preference-conditioned hypernetworks for student-at-risk prediction. MIL represents each student as a bag of weakly labeled interactions, while an RL agent selects informative instances for downstream classification. Two hypernetwork variants are evaluated to determine whether a user-defined preference scalar can continuously control the trade-off between predictive performance and Equalized Odds. The underlying RL-MIL baseline achieves strong classification performance, but both hypernetwork extensions exhibit mode collapse: changing the preference weight produces little systematic movement along the intended fairness-performance frontier. The failure is associated with objective dominance, weak gradient propagation through the conditioning mechanism, and interactions between dynamically generated parameters. The results show that fairness objectives can be incorporated into an interpretable RL-MIL pipeline, but preference conditioning alone does not guarantee controllable multi-objective behavior. Robust fair RL-MIL therefore requires explicit mechanisms for gradient balancing, objective separation, and stability analysis.

---


### 8. [DSSR-3D: Decoupled Reasoning for View-Dependent Referring in 3D Gaussians](https://arxiv.org/abs/2610.00040)

**<font color=#1a73e8>作者：</font>** Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D Gaussian Splatting have enabled open-vocabulary and referring segmentation by distilling semantic knowledge from 2D foundation models into 3D representations. However, existing referring fields embed language features in a globally view-invariant space, making them fundamentally unable to resolve observer-centric spatial relations (e.g., "to the left of") that depend on camera pose. We propose DSSR-3D, an inference-time framework for view-dependent referring segmentation on continuous 3D Gaussian fields, formalized as two interfaces - pose-invariant semantic localization and pose-conditioned spatial reasoning - such that any pair of functions satisfying these constraints yields a valid instantiation, requiring no retraining of the underlying semantic field and no reliance on discrete geometric proxies such as bounding boxes. We instantiate the two interfaces with a temperature-sharpened softmax localization mechanism and a projection-based directional scoring function, fused via a lightweight, training-free step, and show they transfer zero-shot to structurally distinct semantic fields without adaptation. We further propose ViewRef-GS, a benchmark isolating view-dependent segmentation on 3D Gaussian fields, evaluated jointly with an augmented Ref-LERF to provide a comprehensive testbed for viewpoint-dependent spatial grounding. Experiments show consistent gains over existing 3DGS-based referring methods, with no additional training beyond the base semantic field

---


### 9. [SCM-based Fairness and Faithful Explainability for Legal Document Classification](https://arxiv.org/abs/2610.00045)

**<font color=#1a73e8>作者：</font>** Yasmina El Kacemi, Seyed Sahand Mohammadi Ziabari, Ali Mohammed Mansoor Alsahag  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer models such as LegalBERT are increasingly used in legal decision support, raising concerns about both fairness and the transparency of model explanations. These properties are usually evaluated separately, leaving open whether a debiasing intervention that changes fairness also changes how faithfully explanations reflect model reasoning. This study investigates that relationship on the ECtHR alleged-violations corpus from LexGLUE. It compares a LegalBERT baseline with a fairness-regularized variant that penalizes stereotypical warmth and competence representations during fine-tuning. The evaluation covers predictive performance, demographic fairness, and SHAP explanation faithfulness across five random seeds. At the performance-optimal regularization strength, the intervention does not reduce demographic disparity. This null result holds across two fairness definitions and a conventional word-pair control on the gender axis. Classification performance is largely unchanged. However, the intervention consistently degrades explanation sufficiency across all five seeds and three thresholds. A shuffled-pair control reproduces this degradation while leaving performance and fairness unchanged, indicating that the effect arises from contrastive representational regularization rather than specifically from the warmth and competence structure. The results demonstrate a dissociation between fairness and explanation faithfulness: changes in explanation behavior do not necessarily indicate changes in fairness, and fairness must therefore be evaluated directly.

---


### 10. [SW-KAN: Kolmogorov-Arnold Networks with Stieltjes-Wigert q-Orthogonal Polynomials](https://arxiv.org/abs/2610.00050)

**<font color=#1a73e8>作者：</font>** Amirhosein Azarpour, Seyyed Moein Kazemi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold Networks (KANs) represent a paradigmatic shift in deep learning by replacing fixed node activations with learnable univariate functions on edges, offering enhanced interpretability and parameter efficiency. While recent polynomial-based KAN variants have addressed the computational overhead of original B-spline implementations, they introduce a fundamental yet underexplored challenge: the domain mismatch between unbounded real-valued inputs and the bounded or semi-infinite support of orthogonal polynomial bases. To address this limitation, we propose the Stieltjes-Wigert Kolmogorov-Arnold Network (SW-KAN), a novel architecture that employs Stieltjes-Wigert q-orthogonal polynomials defined on the semi-infinite domain (0, infinity). We introduce a smooth exponential-of-tanh mapping that stably bridges the domain gap while preserving well-conditioned gradients, and leverage a numerically stable three-term recurrence that evaluates polynomial expansions in O(N) operations without special-function calls. Through comprehensive experiments spanning image classification and continuous function approximation, we demonstrate that SW-KAN achieves superior accuracy-efficiency trade-offs across diverse tasks. The log-normal weight structure and learnable q-parameter of Stieltjes-Wigert polynomials provide a distinct inductive bias that enables robust performance under resource-constrained conditions, including reduced feature dimensionality and limited training data. The proposed architecture not only outperforms established polynomial KAN baselines on standard benchmarks but also exhibits strong representational capacity for approximating complex multivariate functions with remarkably few parameters, making it a compelling alternative for efficient function approximation and classification in resource-constrained settings.

---


### 11. [Reachability Is Not Generalization: Understanding Verb--Noun Decomposition in Assembly Action Recognition](https://arxiv.org/abs/2610.00064)

**<font color=#1a73e8>作者：</font>** Changyi Li, Yu Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assembly actions are compositional: they combine a manipulation with a part or tool. In deployment, systems routinely encounter novel combinations of familiar components, yet an atomic action classifier assigns every unseen combination exactly zero probability by construction. The prevailing solution is verb--noun decomposition, which predicts components separately and recombines them to reach unseen actions. While widely adopted, how decomposition generalizes under compositional shift remains poorly understood. We present a systematic analysis of verb--noun decomposition across three assembly datasets (MECCANO, HAViD, and IMPACT). Although decomposition escapes the atomic ceiling, its generalization extends only partially beyond it. Unseen-composition performance remains strongly tied to the co-occurrence structure of the training data, indicating that much of the observed gain arises from interpolation within densely supported regions of the compositional space rather than from unconstrained recombination. Across datasets, failures consistently concentrate on the larger-vocabulary component, and IMPACT's verb-heavy vocabulary reverses the bottleneck from nouns to verbs. We further show that shared-encoder training introduces component entanglement, encouraging reliance on co-occurrence patterns that transfer poorly to unseen compositions and trailing independent recombination by up to $6.0\times$ in harmonic mean. Taken together, these findings explain why decomposition achieves only partial compositional generalization in practice. By identifying primitive support, vocabulary asymmetry, and component entanglement as connected sources of error, we provide a portable diagnostic framework for studying compositional recognition beyond aggregate accuracy. Code: this https URL.

---


### 12. [Robust Online Aero-Engine Blade Defect Detection via Dual-Alignment Test-Time Adaptation](https://arxiv.org/abs/2610.00067)

**<font color=#1a73e8>作者：</font>** Zhaoyang Wang, Haiyong Chen, Dongying Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable visual inspection is essential for quality assurance in aero-engine blade manufacturing, where defect appearance may vary across production lines, imaging conditions, blade poses, and surface backgrounds. Such domain shifts cause a mismatch between training and deployment data and degrade the reliability of deep defect detectors in online inspection. This problem is particularly challenging because aero-engine blade images usually contain sparse defects, making pseudolabel-based adaptation vulnerable to noisy or missing predictions. To address this issue, we propose Aero-engine Blade Defect Detector (ABDD), an online adaptive detection framework based on test-time adaptation. ABDD introduces a Dual-Alignment Strategy to jointly adapt global visual style and local defect morphology by combining feature-statistics alignment with pseudo-box alignment. To reduce error accumulation from unreliable pseudo labels, an Uncertainty-aware Box Filtering mechanism evaluates pseudo boxes using classification confidence, classification entropy, and localization entropy. In addition, a lightweight Sparse Dilated Mona module enables parameter-efficient delta tuning while limiting source-domain forgetting. ABDD is evaluated on CD-AeBD and HD-AeBD under multiple domain-shift scenarios, with TTA strategies compared under a unified RT-DETR + Swin-T architecture. Experiments show that ABDD consistently improves detection robustness under domain shifts, and its practicality is further validated on an industrial inspection platform.

---


### 13. [Critsly and StudioCrit: An Artefact-Aware AI Critique Workspace and Simulation-Based Readiness Study for Design Education](https://arxiv.org/abs/2610.00085)

**<font color=#1a73e8>作者：</font>** Nizam Kadir  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Critique in design education depends on interpreting work in progress, articulating intentions and translating feedback into revisions. This technical report presents Critsly, an artefact-aware AI critique workspace, and StudioCrit, its architecture-studio research mode. Critsly combines a visual board, design-intention fields, guided reflection, perspective-based critique and action planning. StudioCrit adds studio/class organisation, role-based access, cognitive and architectural classification, educator analytics and exportable evidence. The report consolidates implementation and simulation evidence recorded in a research project submitted in July 2026. Three simulated studio scenarios yielded 109 classified evidence rows, including 85 assigned to higher-order Bloom categories. A separate rehearsal using 50 disposable learner accounts yielded 56 evidence rows, including 46 assigned to higher-order categories. A subsequent hardening rehearsal recorded 50 completed sessions, 50 successful board pulls and 50 denials of student access to analytics. These are software and synthetic-trace observations, not measurements of learning gains or human cognitive performance. Automated classifications remain provisional, and the source report does not establish classifier accuracy or inter-rater reliability. The contribution is an implemented critique-to-evidence workflow and a bounded account of its readiness for further controlled evaluation.

---


### 14. [One Mastery Threshold Does Not Fit All Knowledge Tracing Models](https://arxiv.org/abs/2610.00095)

**<font color=#1a73e8>作者：</font>** Xianghui Meng, Yujing Zhang, Jionghao Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tutoring systems use mastery thresholds to decide when students can stop practicing and advance, but the same numerical threshold can lead to very different decisions when the underlying knowledge tracing (KT) model changes. We examine six KT models across four public educational datasets and evaluate 12 thresholds from 0.50 to 0.99 using post-advancement performance, advancement coverage, practice burden, and disparities across prior-performance groups. We also identify thresholds that balance performance, extra practice, and advancement under 30 predefined instructional settings. Bayesian Knowledge Tracing (BKT) is relatively insensitive to threshold changes, while neural models become much more selective as thresholds increase. This partly reflects different model outputs: BKT estimates latent mastery probability, whereas neural models estimate the probability of a correct next response, so the same cutoff does not represent the same level of mastery. The best-balanced threshold varied substantially across models and settings. In half of the tested settings, neural models and BKT differed by more than 0.10 in their selected thresholds, although this gap became smaller when greater priority was placed on reducing extra practice and allowing more students to advance. Stricter thresholds also did not reliably reduce performance gaps and could disproportionately restrict advancement, with stronger-prior students advancing up to 3.26 times as often as weaker-prior students. These results show that mastery thresholds should be recalibrated when the KT model or instructional priorities change and evaluated by their effects on performance, practice, advancement, and access.

---


### 15. [FACET at WMT 2026 Automated Translation Quality Evaluation Task](https://arxiv.org/abs/2610.00096)

**<font color=#1a73e8>作者：</font>** Ahrii Kim, Chanjun Park, Seong-heum Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Different error types in machine translation require different evidence. Whether meaning is preserved can be judged only against the source, while whether the target is well-formed, or whether it names one entity consistently, can be judged from the target alone. We present FACET, our reference-free submission to the WMT26 Automated Translation Quality Evaluation Task, which decomposes evaluation into Fluency, Accuracy, and Consistency passes and gives each pass only the context its error type requires. A single fixed model is prompted three times, and the merged error spans yield the three task outputs, error spans, quality scores, and error-free labels, with no trained components. We also submit FACET-C, which omits the Consistency pass. Without gold labels, we characterize the predictions of FACET. Its system rankings place post-edited human translation first, and the Consistency pass changes about a tenth of segment scores while leaving the ranking nearly unchanged.

---


### 16. [DramaAgent: Agentic Storytelling Video Generation](https://arxiv.org/abs/2610.00097)

**<font color=#1a73e8>作者：</font>** Ting Huang, Biao Wu, Ronghao Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion and autoregressive models have substantially improved text-to-video generation, yet producing coherent long-form story videos with consistent characters and aligned audio remains challenging. Existing methods often suffer from narrative drift, unstable character identity, weak cross-scene continuity, and audio-visual mismatch over extended sequences. We propose DramaAgent, a hierarchical, agentic, and model-agnostic framework for long-form text-to-video-and-audio generation. Rather than improving the underlying video backbone itself, DramaAgent introduces an upper-level control layer that decomposes generation into story planning, persistent character conditioning, scene-wise synthesis, and reflection-guided targeted repair. The framework maintains reusable story and character states across scenes, diagnoses failures such as identity drift, missing scene semantics, temporal discontinuity, and cross-modal mismatch, and repairs problematic clips in a stage-specific manner. Experiments across multiple video generation backbones show that DramaAgent improves long-horizon coherence, character consistency, narrative fidelity, and scene-level audio-visual consistency over direct generation and strong baselines. These results suggest that hierarchical agentic control is a practical direction for controllable long-form audiovisual generation. Code: this https URL. Website: this https URL.

---


### 17. [Characterizing and Codifying Malware Sophistication](https://arxiv.org/abs/2610.00098)

**<font color=#1a73e8>作者：</font>** Angelo Porcella, Zachary Wadhams, Clemente Izurieta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> 'Sophisticated' is widely used to describe malware, yet it lacks a consistent definition within academic literature. While existing software quality and complexity metrics offer some insight into malware structure, they do not capture the broader adversarial and operational traits that contribute to real-world threat potential. This paper presents a systematization of existing approaches for assessing malware quality using static binary analysis. We define malware sophistication through a quality-focused lens by reinterpreting select characteristics from the ISO/IEC 25010 software quality standard, including reliability, maintainability, flexibility, and security, and evaluating their applicability to malware binaries. We identify which characteristics are both relevant to malware and measurable through static analysis, forming the basis for future frameworks that consistently assess malware sophistication when source code is unavailable or dynamic execution is infeasible.

---


### 18. [Uncertainty-Aware Learning from Multi-Expert Interval Targets](https://arxiv.org/abs/2610.00102)

**<font color=#1a73e8>作者：</font>** Samira Alkaee Taleghan, Younghyun Koo, Andrew P. Barrett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many machine learning (ML) applications rely on expert labels, and qualified experts may provide different but plausible interpretations of the same observation. Such variation across expert labels may reflect genuine disagreement or ambiguity rather than annotation error. When individual experts additionally report intervals rather than exact values, the supervision contains two distinct sources of label uncertainty: within-label imprecision and between-expert variation. Existing methods treat these forms separately: multi-expert approaches collapse labels to a consensus, interval-target methods often yield a single prediction, and predictive-uncertainty methods rarely validate their uncertainty estimates against observed expert disagreement. To address this problem, we propose an approach that preserves individual expert intervals, separates within-label imprecision from between-expert variation, and validates the corresponding predictive uncertainty components. First, heterogeneous label vocabularies are harmonized into a common probabilistic label space, separating encoding differences from expert judgement. Second, individual label intervals are retained and modeled with a mixture of Beta distributions trained using a proper Cramér-distance objective, preserving distinct expert-reported labels. Third, we decompose predictive uncertainty into within-component, between-component, and model uncertainty, and evaluate whether these components correspond to within-label uncertainty, between-label uncertainty, and model error, respectively. Because this correspondence is not guaranteed, we introduce decomposition matching, which aligns the predictive components to their intended label-side sources. On sea-ice concentration the model reduces MAE by 31\% over hard labels and outperforms aggregation, interval-distribution, and interval-regression baselines.

---


### 19. [The Hidden Costs of 99% Accuracy: A Trustworthiness Audit of the Telco Customer Churn Benchmark](https://arxiv.org/abs/2610.00118)

**<font color=#1a73e8>作者：</font>** Soumyadeep Roy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Customer churn prediction on the IBM Telco Customer Churn benchmark (n = 7,043) routinely reports test accuracies above 95%, with the most cited published study reporting 99.01%. We audit this benchmark for four trustworthiness failures invisible to the accuracy- and F1-centred reporting that dominates the literature. First, pre-split SMOTE inflates churn-class F1 by 13.1 percentage points across ten classifiers and fifteen seeds (Wilcoxon p < 10^-4 per classifier); the same leaky pipeline ordering paired with class weighting yields no inflation, isolating the effect to SMOTE's geometric construction. We measure the mechanism directly: approximately 36% of synthetic training points are nearest-neighbour interpolations of test-set instances. Second, the TotalCharges field is approximately determined by tenure multiplied by MonthlyCharges (R2 = 0.999); removing it changes accuracy by less than 0.2 percentage points, yet TreeSHAP ranks it ninth in mean absolute attribution - a pattern that materially corrupts SHAP-based interpretation. We propose an R2 > 0.95 pre-modelling diagnostic. Third, in a 15-seed calibration audit, isotonic regression is the strongest default; temperature scaling fails on class-weighted tree ensembles whose predicted-probability distribution is bimodal. Fourth, the cost-optimal decision threshold (under a 50 USD retention offer and 24-month CLV proxy) is approximately 5-10 times lower than the F1-optimal threshold, saving approximately 77,000 USD per 1,000 customers. We replicate F1 and F2 on Iranian Telecom Churn (within domain) and Bank Customer Churn (across domain): F1 generalises; F2 generalises only within telecom. We synthesise these findings into a four-component reporting checklist - pipeline disclosure, redundancy diagnostic, calibration audit, and cost-sensitive thresholds - and release a reproducible implementation.

---


### 20. [Generalized Biomedicine Discovery](https://arxiv.org/abs/2610.00120)

**<font color=#1a73e8>作者：</font>** Luyao Tang, Yingkai Yang, Hanqi Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In real-world clinical practice, medical images face open-world shifts: (i) long-tailed rare diseases, (ii) subtle lesions dominated by normal anatomy, and (iii) hierarchical taxonomies. Yet most open-world paradigms assume flat, balanced label spaces, leaving these biomedical demands unresolved. We introduce Generalized Biomedicine Discovery (GBD) and a unified benchmark spanning long-tail, anomaly, and taxonomy-aware discovery. Our key insight is that dominant known patterns form a visual manifold that masks subtle novelty. Inspired by expert diagnosis, we propose SCAN (Surprise-evoked Complementary AccommodatioN), which follows a cognition-inspired perceptual progression: it applies predictive suppression to filter expected norms, triggers surprise-evoked salience to highlight unexpected deviations, and performs complementary accommodation to integrate these shifts into global representations. Extensive experiments show that SCAN improves novel concept discovery while generally preserving established clinical knowledge, and it plugs into existing architectures to better navigate the known-unknown trade-off in medical imaging. Code is available at this https URL.

---


### 21. [A Comprehensive Review of One-Pixel Attack: Research Status, Taxonomy, Applications, Regulation Policy and Future Directions](https://arxiv.org/abs/2610.00125)

**<font color=#1a73e8>作者：</font>** Mirza Niaz Morshed, Md. Masudul Islam, Galib Muhammad Shahriar Himel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> One-Pixel Attacks (OPAs) represent one of the most extreme demonstrations of adversarial fragility in deep learning, where modifying a single pixel can reliably induce high-confidence misclassification across domains such as medical diagnosis, autonomous driving, biometrics, and quantum communication. Despite their conceptual simplicity, OPAs remain underexamined in existing adversarial-attack surveys, which provide only fragmented or cursory coverage. This PRISMA-guided review synthesizes high-quality studies from 2017 to 2026 and delivers a unified, multi-axis taxonomy of OPA research spanning algorithmic foundations, black-box evolutionary optimization, emerging hybrid and program-synthesis attacks, defence mechanisms, interpretability tools, and domain-specific vulnerabilities. Our analysis reveals the dominance of Differential Evolution-based strategies, the rise of efficiency-optimized and saliency-guided methods, and persistent gaps in dataset diversity, transferability, and standardized evaluation. We summarized and assess defence paradigms including pixel restoration, anomaly detection, input-space transformations, and robust training highlighting their trade-offs in robustness, imperceptibility, and computational overhead. Building on these insights, we outline future research priorities involving selective pixel recovery, transformer-specific vulnerability analysis, saliency-driven optimization, and real-world domain-adaptive defences. We further propose a regulatory framework emphasizing robustness testing, incident disclosure, and AI security governance. This review establishes a comprehensive foundation for understanding, evaluating, and mitigating ultra-sparse adversarial threats in contemporary AI systems.

---


### 22. [A Verifier Can Leak the Answer: Diagnosability Before Optimization in Closed-Loop Agent Debugging](https://arxiv.org/abs/2610.00126)

**<font color=#1a73e8>作者：</font>** Peiying Zhu, Sidi Chang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent developers increasingly compare prompts, tools, policies, and diagnosis algorithms through simulator-grounded verifiers. A verifier can nevertheless make a solver comparison vacuous: if its probes or predicates encode the target identity, an exact optimizer may appear effective without resolving any genuine ambiguity. We report such a failure in an aggregate-trace debugger for a closed-loop decision agent. Exact minimum hitting set (MHS) and a propagation-aware greedy method returned identical supports in 12/12 development cases and the same planted-fault recovery in 9/12. A subsequent audit found that exact-anchor predicates produced the planted pair in 9/9 cases. After removing those anchors, overall planted-pair recovery was 8/9; hard-probe singleton pairs nevertheless matched the planted pair in 9/9, and no case retained a nonempty residual conflict family after propagation (0/9). The optimizer was correct, but the verifier had already disclosed the answer. We replace solver-first evaluation with a support-gated verification contract. A clean reference map must first show repeated component exposure; a matched reference/current gate must then establish comparable runtime evidence; only afterward may an independently calibrated signal rule return a detection. In a preregistered heldout comprising 1,440 cases and 21,600 partition rows, 55/72 regime-component units passed the reference gate, 54/55 passed the runtime gate, and stable false admission was 0/20 represented components with a one-sided exact 95% upper bound of 0.1391. Within admitted units, affected clean traffic predicted detection better than nominal fault-cell fraction. The main lesson is structural: verify evidence eligibility and non-revelation before optimizing the component selector. Otherwise a stronger solver can merely certify a stronger verifier artifact.

---


### 23. [The Cognitive Continuity Test: Verifying Governed State Transitions in Persistent AI Agents](https://arxiv.org/abs/2610.00132)

**<font color=#1a73e8>作者：</font>** Jun He, Deying Yu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Persistent AI agents revise beliefs, consolidate memory, and replace execution substrates. Similar successor states can accompany differently authorized transition claims, while legitimate development can change state substantially. We introduce the Cognitive Continuity Test (CCT), a policy-relative contract for verifying submitted transitions using scoped authority, provenance, deterministic application, semantic predicates, and candidate-persistence receipts. CCT distinguishes verified admissibility, affirmative violation, and unresolved required evidence. Separation results concern transition claims rather than live runtime identity; soundness is conditional on the specified checker and evaluator assumptions.
IdentityLineageBench provides 24 generated transition families. The reference post-resolution verifier matches all 576 canonical held-out labels; lexical state similarity and a lineage-only diagnostic baseline admit 60.0% and 80.0% of invalid fixtures. These comparisons establish synthetic conformance, not superiority to a policy-aware deployed system. Signed adversarial regressions cover fabricated interaction counts, unsupported belief changes, and mixed missing/contradictory evidence. SIT behavior and actual model migration remain unmeasured. An 18,000-execution valid-path study measures a 6.21 ms default median on resident inputs. We specify the additional activation and recovery obligations needed for deployment.

---


### 24. [Evasion Attacks: How Adversarial Noise Bypasses ML Classifiers](https://arxiv.org/abs/2610.00136)

**<font color=#1a73e8>作者：</font>** Parker Hummel, Ryne Skabo, Muhammad Abusaqer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents a reproducible, educational study of evasion attacks in image classification and text classification. A compact convolutional network trained on MNIST reached 98.63% clean test accuracy and was evaluated under two white-box attacks. Under FGSM, accuracy fell to 60.20% at $\epsilon$ = 0.15 and 1.72% at $\epsilon$ = 0.30; under PGD it fell to 32.47% and 0.41%, and a bit-depth-reduction defense recovered only part of the loss. In the second experiment, DistilBERT fine-tuned on the SMS Spam Collection reached 98.75% accuracy and a 94.96% F1-score, but a controlled sequence of pre-defined perturbations (character substitutions, whitespace noise, and a benign suffix) produced only modest probability shifts in most displayed examples and no flip from spam to ham. Adversarial vulnerability is strongly modality-dependent: the MNIST experiment is a clear evasion demonstration, whereas the text experiment is a controlled robustness evaluation. Robustness must be tested empirically rather than inferred from clean accuracy.

---


### 25. [Evaluating the Robustness of Anti-UAV Detection under Controlled Fog Degradation: Fog-Aware Training and Clear-Sky Tradeoff](https://arxiv.org/abs/2610.00141)

**<font color=#1a73e8>作者：</font>** Gur Levy Birkental, Seyed Sahand Mohammadi Ziabari, Ali Mohammed Mansoor Alsahag  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based anti-UAV systems must function in poor visibility, yet most benchmarks use only clear-sky footage, and previous robustness studies treat adverse weather as a simple present/absent condition. As a result, the impact of fog severity on ground-to-air UAV detection remains poorly understood. This work presents the first severity-controlled fog benchmark for this task: synthetic fog at ten severity levels is applied to the RGB modality of the Anti-UAV300 dataset, comparing a clear-trained YOLOv5m baseline to a fog-aware model trained on both clear and foggy images. Detection performance drops sharply and non-linearly: degradation is front-loaded across light-to-moderate fog (beta approximately 0.05-0.10), with a 96% reduction in mAP@0.5:0.95 from clear to thickest fog, mainly due to lost recall and confidence. On the comparable metric (mAP@0.5), this collapse exceeds the most extreme rain degradation reported in the closest prior benchmark. Fog-aware training boosts detection across all severities (up to +0.320 mAP@0.5:0.95) with only a 9.1% drop in clear-sky accuracy, raising the threshold for reliable detection while not preventing collapse under extreme fog. Since reliability is lost within a narrow visibility range, simple clear vs adverse tests underestimate operational risk.

---


### 26. [Metric-Construction Coupling Inflates Measured Synthetic Dialect Recovery](https://arxiv.org/abs/2610.00164)

**<font color=#1a73e8>作者：</font>** Hyojung Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Korean dialect corpora are available but not redistributable: weights may be released, while reproducing training and evaluation from the underlying data cannot be. We ask how much of that supervision synthetic data recovers, and whether that recovery can be measured independently of the synthesis pipeline. We contribute KoDialectBench, 1,000 items across five regions on three axes, released as identifier hashes and scoring code so users reconstruct the items from their own licensed copy. Recovery is strongly axis-dependent: our best synthetic arm reaches 91.2% of the real-data gain on region identification but 63.7% on comprehension. On generation the answer depends on the metric: the deployed marker lexicon reports 92.3% on dialectness and 119.3% on region match, the latter exceeding the real-data reference, whereas reference-based generation reaches 72.4%. We find the marker metrics' scoring inventory is entirely contained in the inventory our transformation rules can emit. We test the effect of construction access directly with an exact-form construction-disjoint arm that withholds 20% of marker types from the rules. At exactly matched training size (8,600 examples) it reduces dialectness recovery from 91.8% to 8.1% and region-match recovery from 101.9% to 25.6% on the held-out marker inventory, while the three pipeline-independent measurements do not fall at all. A complementary evaluator sweep defines metric-construction coverage (MCC) and finds measured dialectness recovery increasing monotonically as overlap rises from MCC=0 to MCC=1. Shared construction and evaluation inventories can therefore substantially inflate estimates of synthetic-data recovery.

---


### 27. [Classification Based on Association Rules Algorithm for Breast Cancer](https://arxiv.org/abs/2610.00174)

**<font color=#1a73e8>作者：</font>** Ali Alsalama, Ahmed Kubba, Ghaith Jamjoum 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Breast cancer is a significant contributor to female mortality across the world, displaying one of the highest oc currence rates among the various cancer types. In response to the need for early breast cancer detection, researchers have increasingly turned to association rule-based classification as a favored method. Association Rule mining is a data mining approach which offers the benefit of yielding results that are readily understandable for medical professionals. This paper introduces a novel association rule-based data mining technique for breast cancer classification based on a weighted classification approach. This implementation employs three core algorithms: Rule Generation, Rule Pruning, and Rule Prediction. Rule Generation identifies frequent itemsets and creates association rules. Rule Pruning eliminates rules using specific criteria and separates them into major and minor groups based on their influence on training data. Rule Prediction applies the pruned rules to classify test data. The final prediction algorithm was tested on several testing samples to show the feasibility and performance of the approach.

---


### 28. [Four Ways to Grow a Classifier and Why One of Them Cannot Learn](https://arxiv.org/abs/2610.00180)

**<font color=#1a73e8>作者：</font>** Cagri Temel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constructive classifiers add structure while they train: a level to a tree, a unit to a hidden layer, a split at a leaf. This paper asks what each of four such growth decisions actually buys, measured under one fixed protocol in tree-structured and constructive models, and gives an exact diagnosis and a fix for the one that buys nothing.
The diagnosis concerns the most natural way to deepen a soft decision tree: turn every leaf into a gate whose two children inherit the parent's class distribution, so that the function is unchanged. I prove that this leaves the gradient of every new gate identically zero and, with the gate at 1/2, gives the two children identical gradients, so the added level can never learn. Unlike the symmetry that Net2Net breaks with noise or the saddle point that splitting steepest descent escapes with second-order information, first-order information here is not weak but absent. Over three seeds of five-fold cross-validation the construction loses 19.6 accuracy points on Iris, 19.1 on Wine and 55.6 on Digits against the same depth trained from scratch. The fix is a small random perturbation of the children, whose size barely matters. The practical rule is one line in a test: after adding parameters, assert that their gradient is nonzero.
The other three decisions each buy one thing. Fitting a new hidden unit to the residual error before installing it buys a smaller network on every dataset, though not a more accurate one, and on Digits it costs accuracy significantly. Splitting the leaf with the largest expected error buys sparsity, reaching 0.885 with 3.7 splits where a complete depth-six tree uses 63, but loses 4.3 points on a harder problem. Requiring statistical significance before a node receives a more expressive split buys nothing: the tree gets larger and less accurate.
Every number in the paper is inserted from the measurement script.

---


### 29. [Uncertainty-Aware RL-Controlled Adaptive 3D Mapping](https://arxiv.org/abs/2610.00188)

**<font color=#1a73e8>作者：</font>** Alpay Ozkan, Tunc Ozan Aydin, Marc Pollefeys 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Voxel-based volumetric mapping is fundamental to 3D reconstruction, yet fixed-resolution grids remain inherently inefficient - wasting memory in uniform regions and losing detail in complex ones. Existing adaptive methods, such as MAP-ADAPT, partially address this by varying resolution based on geometry and user-defined semantic class lists, but these heuristics require expert tuning, lack generalization to unseen objects, and provide no explicit mechanism to control memory usage. We propose an adaptive framework that refines voxels based on semantic entropy, which captures label uncertainty, together with geometric curvature and texture richness as scene complexity cues, yielding principled resolution allocation without reliance on semantic taxonomies. To make the accuracy-memory trade-off explicit and user-controlled, we further introduce a reinforcement learning agent that learns voxel subdivision policies under a user-specified target memory budget, replacing hand-tuned thresholds with a single intuitive control parameter. The resulting multi-resolution TSDF achieves higher geometric accuracy, better semantic consistency, and improved memory-accuracy trade-offs compared to MAP-ADAPT and fixed-resolution baselines on both synthetic and real-world datasets. Our code and models are available at this https URL.

---


### 30. [Energy Time-Series Imputation with Differentially Private Diffusion Models via Clipping-Aware Objective Conditioning](https://arxiv.org/abs/2610.00209)

**<font color=#1a73e8>作者：</font>** Huizhen Huang, Yu Li, Tao Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable recovery of missing measurements is important for monitoring and analysis in energy time-series systems, where fine-grained measurements may contain sensitive temporal information. Diffusion models trained with differentially private stochastic gradient descent (DP-SGD) provide a promising framework for privacy-sensitive energy time-series imputation. Under cosine diffusion schedules, late timesteps correspond to low signal-to-noise ratio (SNR) conditions, where standard $\varepsilon$-prediction can induce large pre-clipping gradients. Such gradients are more likely to be clipped, reducing the retained optimization signal. The artificial intelligence (AI) contribution lies in formulating this objective--clipping interaction as an objective optimization problem under fixed-threshold DP-SGD and developing timestep-aware objective conditioning for diffusion-based energy time-series imputation. The method adopts $v$-prediction to mitigate late-timestep gradient amplification, uses static loss weighting as a uniform-scaling control, and introduces diffusion-schedule-aware dynamic weighting for stronger attenuation before clipping. For the engineering application, we evaluate the method on five real-world energy time-series datasets across random point missingness, contiguous block missingness, persistent outages, and multiple missing-data severities. Under matched DP-SGD settings, the proposed method consistently improves imputation utility over the $\varepsilon$-prediction baseline. Gradient diagnostics reveal lower upper-tail pre-clipping gradient norms, reduced clipping fractions, and stronger attenuation at late low-SNR timesteps, supporting the effectiveness of clipping-aware objective conditioning for energy time-series imputation.

---


### 31. [Useful to Whom? Sample Value Is Defined Only Relative to the Learner](https://arxiv.org/abs/2610.00221)

**<font color=#1a73e8>作者：</font>** Yangze Liu, Xiao-Long Yin, Zhongyi Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What kind of data does a model need in order to learn? Coreset selection makes this question concrete: under a budget, keep the samples most useful for training. Easy-first and geometric coverage criteria can win in different budget regimes, separated by a crossover boundary. We ask whether this boundary is fixed by the data or changes with the target learner. Controlled experiments freeze the selected subsets and manipulate only the training learner. On low-resolution ImageNet-100, doubling ResNet-18's width moves the crossover from 57 to 85 samples per class: the learner changes the relative value of the same samples. A wider sweep reveals an interaction between input grid and capacity. Enlarging the grid while retaining the same image information shifts the boundary left, and this shift weakens as width increases. Stride controls reproduce and reverse the grid effect without changing the input grid; removing only the last downsampling stride is sufficient to recover the leftward shift. Under the native-224px ImageNet-1k protocol, width effects are smaller and depend on the probe: LFrac remains nearly flat, while EL2N shifts modestly right. Swapping the convolutional learning system for a ViT makes coverage win throughout the measured range, even when the easy subsets come from the convolutional proxy. These results establish learner dependence through frozen-subset interventions and identify network structure that can move the boundary. They do not yield a universal scaling law. Their practical implication is direct: a selection strategy's preferred budget regime must be evaluated with respect to the target learner.

---


### 32. [Constant-Memory Recall: Learned Associations in a Fixed Matrix State](https://arxiv.org/abs/2610.00232)

**<font color=#1a73e8>作者：</font>** Samuel Larson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fixed-size recurrent memory limits storage growth during inference, but successful recall depends on the task and training. We study a small DeltaNet variant with fixed token-specific key biases, trained to remember 32 new key-value pairings per sequence. With 32 KiB of recurrent matrix state, it achieves 99.95% mean accuracy across three training seeds when choosing among the sequence's values. Recall remains near perfect when filler extends the pre-query context to 1,798 tokens without adding pairings. Zeroing the first memory block removes this recall. An exploratory 48-pair test remains near chance after one quarter of the primary training budget and does not locate a capacity limit. Parameter-matched vector and Transformer baselines remain near chance, including the Transformer after additional training searches. This unresolved baseline failure prevents a memory-efficiency comparison.

---


### 33. [Conflicting Supervision Moves Commitment, Not Capability: A 12.29σ arrangement effect that is exactly zero under a convention-agnostic score](https://arxiv.org/abs/2610.00234)

**<font color=#1a73e8>作者：</font>** Wenhui Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> "Train a model on the same problems written under two incompatible conventions, both correct, and ask what the ordering of that data writes into the parameters. The learning-rate schedule is not a background condition for that question. It is the averaging operator, and it decides the answer. We prove a bound in which the arrangement and the schedule enter the ordering effect as separate multiplied factors: the arrangement only as a block period, the schedule only as how much weight the endpoint can place on any one moment of the run. A decaying schedule cannot put a large step size and an uncontracted remainder at the same moment; a constant one does exactly that at the last step. That decay moderates ordering effects has been reported in pretraining; the mechanism, the separation, and a controlled measurement of both halves are ours. Ten orderings of one corpus, one budget, everything but the path held fixed, run twice under families differing in lr_scheduler_type and nothing else: at a constant rate the interior spans 0.2221 in allocation, 11.63 contrast floors, monotone in how blocked the arrangement is. Under the single cosine every published arm uses, the same ten arms occupy two distinguishable states where their own resolution would allow about ten. "Order matters" and "order does not matter" are the two ends of one knob. What the path writes is which convention the model commits to, and no exact-match benchmark can see it. Across twelve arms acc_A+acc_B is constant to within 9.7% while the allocation share runs 0.04 to 0.87, so the 12.29-sigma arrangement switch this paper measures is exactly zero under a convention-agnostic metric. That conservation is quoted from the decayed family throughout, the constant-rate one being a noisier place to read it. Marking the convention in the prompt collapses the switch and reaches 87.5% of the union ceiling."

---


### 34. [How Many Categories Are Enough? Distribution-Free Certification Limits for Few-Shot Anomaly Thresholds](https://arxiv.org/abs/2610.00236)

**<font color=#1a73e8>作者：</font>** Gia Huy Thai, Nguyen Thai Anh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Few-shot anomaly detectors are judged by ranking metrics, yet deployment requires an alarm threshold with a controlled false-alarm rate (FAR). We ask how much normal evidence, in images or category units, is needed to certify such a threshold for an unseen category. Using a frozen DINOv2 principal component analysis (PCA) residual ranker on 15 MVTec and 12 VisA categories under four corruption types, we show that target-only leave-one-image-out (LOIO) calibration is resolution-limited and shift-fragile: rank values cannot fall below $1/(k+1)$, and at the attainable level $\alpha=0.20$, empirical FAR reaches 0.341 on Gaussian-corrupted MVTec at $k=4$, 1.7 times the nominal level. A category-count feasibility calculus is then derived: even with all-zero category losses and no multiplicity charged, any deterministic, uniformly valid, distribution-free 95% upper confidence bound (UCB) requires at least 14, 29, and 59 independent and identically distributed (iid) category draws at $\alpha=0.20$, $0.10$, and $0.05$; these counts are necessary but not sufficient. The Cross-category Reliability Estimation with Source Support (CRESS) protocol splits source categories into disjoint reference, proposal, and certification roles. With only three or four certification categories, all 960 frozen configurations return the fail-closed threshold $\tau^\star=0$, and the smallest category-level UCB is 0.950. Image-unit analyses of the same archive select positive thresholds in 36.7% to 60.3% of target cells; these bounds hold for the selected source mixture, not for the marginal risk of a new-category draw. The contribution is a quantitative feasibility boundary and an estimand-aware protocol specifying when source evidence can, and cannot, support a transferable reliability claim.

---


### 35. [CAVE-Mem: Boundary-Aware Experience Validation for Memory Search](https://arxiv.org/abs/2610.00238)

**<font color=#1a73e8>作者：</font>** Xinyu Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory agents increasingly rely on it- erative search and reusable experience to answer questions over large personal, factual, or narrative histories. However, current experience-memory systems largely optimize relevance: they re- trieve past search lessons that appear similar to the current state and inject them into the prompt. A relevant experience can still be harmful when the memory substrate, question intent, answer granularity, or evidence boundary changes. We propose CAVE- Mem, a training-free framework that represents experience as a typed intervention operator with applicability, boundary, and utility conditions. CAVE-Mem first obtains a base memory-search answer, then allows an operator to change it only if the oper- ator matches the current substrate, answer contract, evidence boundary, and cross-fitted utility; otherwise the system abstains. Experiments across long-term conversational memory, multi-hop question answering, and long-document narrative reasoning show consistent gains over relevance-only experience reuse.

---


### 36. [Contingent Exposure Routing for Financial AI: Outage Risk and the Cost of Indivisible Decisions](https://arxiv.org/abs/2610.00239)

**<font color=#1a73e8>作者：</font>** Shivam Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model failover restores availability, but changes which financial institutions share decision errors. We formulate outage-contingent routing through a local market-impact response matrix and study expected squared price displacement. A symmetric construction shows that a shared backup can leave an order-one concentration floor as the number of primary endpoints grows, while balanced fallback risk decreases inversely with the surviving endpoint count. For indivisible decisions, we derive the exact second moment of independent randomized routing and an effective-exposure granularity that determines its gap from fractional allocation. Conditional-expectation rounding gives a finite-agent bound without coupled quotas; a separate swap procedure preserves endpoint counts and is assessed against dual lower bounds. Across 60 synthetic portfolio networks and 11,340 scenario evaluations, the latter reduces risk by 6.57% and 10.53% for single and double endpoint removals at the central feedback setting with independent errors. A replay of 1,024 recorded API responses on constructed rebalancing tasks gives a smaller held-out reduction of 3.30% (paired bootstrap interval 2.07--4.57%). Strongly aligned errors, inferior endpoints, and indivisibility limit diversification. The contribution is an auditable routing stress test and implementation analysis, not an estimate of real-market crash probabilities.

---


### 37. [The Null Is the Hard Part: Exact Tests for Memorization in Generative Models](https://arxiv.org/abs/2610.00251)

**<font color=#1a73e8>作者：</font>** Sushovan Majhi, Pramita Bagchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memorization audits of generative models read similarity scores against thresholds, with no null distribution, and the conclusions they support can be wrong. By MemBench's rule, the benchmark's mitigations roughly halve Stable Diffusion's memorization; audited with false-discovery control, two thirds of the certified images are no longer detected under random prompt perturbations, five sixths under attention rescaling, and all of them under embedding optimization. The field's data-copying test, read against its own null, flags ten of twenty-four generators that reproduce nothing. We argue that for memorization the null is the hard part, and supply two. For a whole model, training and held-out images are exchangeable given its samples, and relabelling them is a permutation test, exact for any statistic when the held-out images are a random split; under it, a nearest-neighbour preference still fires on seven of those twenty-four, and a count restricted to the near-duplicate scale on none (McNemar p=0.016). For single images, the natural nulls fail twice, measurably: ranking an image among random images yields 596 false discoveries among 2,365 controls, and resampling independent generations makes the null three times too narrow. Calibrated against matched controls, the audit certifies 36 of 61 MemBench images at 5% false-discovery rate, held-out controls are certified in 0.01% of calibration splits, and on this benchmark two generations per image recover that count. A calibrated maximum, which reads occasional rather than typical copying, certifies 46. As the scale-restricted statistic we recommend the small-scale mass of the Intersection Euler Characteristic Profile, which also counts distinct images copied and tests whether two models copy the same ones.

---


### 38. [Sharp Oracle-Regret Tradeoffs for Projection-Free Online Convex Optimization](https://arxiv.org/abs/2610.00254)

**<font color=#1a73e8>作者：</font>** Vaneet Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We characterize the regret attainable in online convex optimization when access to the feasible set is limited to an exact linear optimization oracle. The learner is given an inscribed ball and a diameter bound and must remain feasible on every consistent instance. For convex $G$-Lipschitz losses, diameter at most $D$, a total allowance of $Q$ oracle calls, and a strict limit of $B$ calls per round, the dimension-free minimax expected regret is $\Theta(GD\max\{\sqrt T,T/(1+\min\{Q,BT\})^{1/4}\})$. The lower bound applies to arbitrary randomized learners. Universal feasibility first forces each action into the hull of the supplied ball and the preceding oracle replies. A fixed-body construction then couples fresh phase directions to a shared simplex, making useful replies costly repeatedly even though all losses have a common minimizer. A counted approximate-gradient method with interleaved blocks attains the matching rate. Total-budget and strict per-round guarantees follow as special cases, including the $T^{3/4}$ rate with one call per round and the quadratic total budget needed for $\sqrt T$ regret. For prescribed smoothness $\beta$, an analytic construction yields a curvature-dependent lower bound and identifies the threshold above which the general characterization remains sharp.

---


### 39. [Signed Lexical Confidence for Risk-Calibrated Intent Routing](https://arxiv.org/abs/2610.00262)

**<font color=#1a73e8>作者：</font>** Yezhou Cheng, Zehua Yang, Bojun Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Selective intent routing allows an assistant to act on reliable predictions while deferring uncertain requests. Standard confidence scores primarily reflect the base model's representation, leaving an opportunity to incorporate complementary evidence without changing its decisions. We introduce a signed lexical gate that combines a sentence classifier's logit margin with a sparse lexical model's support for the classifier's predicted intent. By assigning positive evidence to lexical agreement and negative evidence to a lexically favored competing intent, the gate retains more information than either unsigned lexical confidence or a hard agreement rule. An independent binomial calibration stage selects an operating threshold for a specified risk target. Across ten runs on BANKING77, CLINC150, and HWU64, the proposed score reduces area under the risk-coverage curve by 15.8%, 15.1%, and 11.8% relative to a learned semantic-only gate. At a nominal 5% error target, it increases accepted coverage by 1.83 and 5.14 percentage points on BANKING77 and HWU64, while CLINC150 is already near full coverage. At a stricter 2% target, the simultaneous binomial procedure yields a nonempty policy in all 30 dataset-run combinations at the available calibration budgets. Matched controls show that the proposed feature improves average error ranking over the tested unsigned lexical-confidence feature, with dataset-dependent gains over binary agreement. The resulting two-feature gate provides a compact, interpretable confidence enhancement for risk-calibrated intent routing while preserving the base classifier's predictions.

---


### 40. [Multi-Resolution Feature Fusion U-Net for Magnetic Resonance Imaging Segmentation](https://arxiv.org/abs/2610.00279)

**<font color=#1a73e8>作者：</font>** Eirini Cholopoulou, Dimitrios E. Diamantis, Dimitris K. Iakovidis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The segmentation of anatomical structures in medical images and particularly in MRI scans, is essential for clinical diagnosis and monitoring disease progression. While Deep Learning (DL) architectures, such as U-Net and its extensions are very effective in medical image segmentation tasks, they often struggle with preserving fine-grained details and global contextual information. This is especially challenging for MRI data segmentation, where anatomical structures are characterized by irregular boundaries and variations in shape, contrast, and scale. To address this challenge, we propose a novel DL architecture for MRI segmentation across different anatomical structures. Specifically, the architecture introduces a module, named Multi-Resolution Feature Fusion (MRFF), that can be easily integrated into any U-Net-like architecture. The MRFF is integrated in all levels of an encode-decoder structure, along with attention mechanisms and skip connections to extract features at multiple resolutions, enabling the model to capture both fine-grained details and global contextual information. We evaluate the MRFFU-Net on two publicly available benchmark MRI datasets of different anatomical targets; one for Cerebrospinal Fluid (CSF) segmentation in spinal MR scans, and one for left atrium cardiac segmentation, from the Medical Segmentation Decathlon (MSD) challenge. Experimental results indicate that MRFFU-Net outperforms state-of-the-art models across multiple evaluation metrics, demonstrating its effectiveness in MRI segmentation.

---


### 41. [Stable and Counterfactually Robust Physical World Models from Imposed Structure and Learned Physics](https://arxiv.org/abs/2610.00280)

**<font color=#1a73e8>作者：</font>** Yufeng Wang, Parivesh Priye, Lu Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A world model learns to forecast how a physical system evolves from recorded trajectories, yet the systems it imitates obey physical laws that are neither fully supplied nor reliably respected. The model may create energy, drift or diverge over long rollouts, and answer a changed law query using the law observed during training. We ask how much general physical structure must be hard coded into a world model, and how much system-specific physics can then be learned from data, for four properties to hold simultaneously: second law compatible dissipation, correct responses to interventions on physical parameters, stability out to one hundred times the training horizon, and robustness to disturbances. The imposed structure is general: dynamics are generated from the gradient of a learned energy through a fixed reversible operator, the energy is restricted to a confining class, a one way port can remove energy but never inject it, the drive channel is known, and the intervened parameter enters through a separable map. The model learns the energy functional, constitutive relations, dissipation rate, and couplings. Across an electromagnetic cavity, a particle in cell grid, and a shallow-water fluid, models with roughly nine thousand parameters recover constitutive functions with unit slope, separate conserving from dissipating worlds by four orders of magnitude using a single set of weights, and transfer changes in sign, magnitude, rate, and gravity to unseen values, where equal-capacity models without the same structure perform at chance or worse. A nonlinear constitutive law is recovered with its curvature preserved and predicts a held-out intervention $2$-$17\times$ better than a converged linear model.

---


### 42. [Knowing When to Yield: Grounded Arbitration of User Corrections in Text-Based Embodied Agents](https://arxiv.org/abs/2610.00282)

**<font color=#1a73e8>作者：</font>** Yezhou Cheng, Runjia Du, Zeming Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How should an embodied agent respond when a person's correction may be wrong? We formulate grounded correction arbitration as a choice among accepting, rejecting, inspecting the world, and asking the speaker. GAVA implements this interface with observation-bounded evidence, legal probes, and a one-step expected-loss rule. In text-only ALFWorld, 162 checkpoints produce 972 paired true and false interventions. Complete local inspections give GAVA and always verify 100 percent correction accuracy, establishing the evidence contract rather than a comparative advantage. In same-episode execution, GAVA reduces interaction cost against always verify but ties a cost threshold under a perfect speaker. An exploratory training-only object-location prior lowers interaction and declared joint cost on 340 unseen scenarios by 0.490 and 0.420 relative to uniform GAVA. After freezing the policy, costs, baselines, and multiplicity plan, the gains replicate on 77 non-overlapping seen checkpoints, covering 308 scenarios: 0.595 and 0.517, with both 95 percent checkpoint-bootstrap confidence intervals excluding zero. Joint cost also improves over an identical-prior fixed policy, while the matched calibrated no-VOI comparison remains inconclusive. Semantic GAVA makes four factual errors in each cohort, corresponding to 98.8 percent and 98.7 percent accuracy, and all methods complete every task. Results support selective information gathering with semantic priors under declared costs, but do not establish a general advantage of environmental value of information over clarification. The study uses normalized claims, complete symbolic observations, and controlled speakers; it evaluates neither human participants, visual input, nor physical robots.

---


### 43. [Partial AUC Maximization from Positive-unlabeled Data](https://arxiv.org/abs/2610.00284)

**<font color=#1a73e8>作者：</font>** Atsutoshi Kumagai, Tomoharu Iwata, Taishi Nishiyama 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The partial area under the receiver operating characteristic curve (pAUC) is an important performance metric for binary classification that summarizes true positive rates within a specific range of false positive rates (FPRs). Classifiers that achieve high pAUC need to be obtained in many real-world applications such as cybersecurity, medical care, and advertising. Although many methods for maximizing the pAUC have been proposed, they typically require both labeled positive and negative data for training. However, in practice, labeled negative data are often difficult to collect due to privacy concerns or the need for high expertise to annotate them. In this paper, we propose a method for maximizing the pAUC from positive and unlabeled (PU) data without negative data. Within an empirical risk minimization framework, we show that the pAUC, including its FPR-dependent thresholds, can be represented using only the positive and marginal densities, and derive an empirical estimator from PU data. A classifier is then trained by maximizing the derived smoothed empirical pAUC estimator. We experimentally demonstrate the effectiveness of the proposed method with ten real-world datasets.

---


### 44. [LENS-GRF: Permutation-Invariant Lesion Evidence Network with Gated Residual Fusion for Acne Severity Grading and Multi-Rater Clinical Oracle Analysis](https://arxiv.org/abs/2610.00294)

**<font color=#1a73e8>作者：</font>** Muhammad Muhtasim Shahriar, M. F. Mridha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated acne severity grading requires both whole-face context and fine-grained lesion evidence. We propose LENS-GRF (Lesion Evidence Network with Set-Transformer and Gated Residual Fusion), an interpretable multi-stage framework for four-class acne severity grading. The method combines Adaptive Facial Skin Segmentation and a global Vision Transformer prior with a permutation-invariant Lesion Set Transformer that encodes localized lesion patches and spatial geometry. Gated Residual Fusion adaptively controls the local residual contribution and reduces to the global prediction when the gate is zero. On ACNE04, fully automated LENS-GRF with YOLOv11s achieved 80.82% accuracy; with ground-truth lesion annotations, it achieved 95.89% +/- 0.59% accuracy and a Quadratic Weighted Kappa of 0.9753. A data-integrity audit identified 15 cross-split duplicate image pairs, including five with conflicting severity labels. In locked zero-shot evaluation on the full PLSBRACNE01 cohort (200 subjects, 600 views), automated LENS-GRF achieved 35.00% accuracy versus 42.50% for the global baseline. On the 148-subject common cohort used for three-dermatologist oracle analysis, ground-truth lesion inputs increased the best oracle accuracy to 47.97%, while the highest oracle QWK was 0.5799. Pairwise oracle agreement ranged from 49.32% to 66.22%, highlighting detector domain shift, annotation variability, and cross-criterion mismatch.

---


### 45. [Beyond Pixel Reconstruction: Retrieval-Guided Glyph-Aware Restoration for Low-Resource Manchu Historical Documents](https://arxiv.org/abs/2610.00315)

**<font color=#1a73e8>作者：</font>** Ting Huang, Dongdong Wang, Mingqiu Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Historical Manchu documents preserve invaluable linguistic and cultural heritage, yet their digitization is hindered by severe degradations and the scarcity of paired training data. Existing document restoration methods primarily optimize pixel-level reconstruction, which can produce visually plausible results while failing to preserve the structural identity of Manchu glyphs. To address this limitation, we propose a retrieval-guided glyph-aware restoration framework that goes beyond pixel reconstruction by explicitly incorporating glyph-level structural knowledge. Our method retrieves relevant glyph exemplars to provide structural guidance during restoration and integrates this information into the reconstruction process, improving the recovery of degraded character structures under low-resource conditions. Extensive experiments on Manchu historical documents demonstrate that the proposed approach improves both image restoration quality and glyph-level fidelity compared with existing restoration methods. These results highlight the importance of incorporating character-aware structural priors for reliable restoration of low-resource historical documents.

---


### 46. [EgoRefine: Ego-Referenced Predictive Alignment and Trajectory-Conditioned Reliability-Aware Fusion for Asynchronous Collaborative Perception](https://arxiv.org/abs/2610.00319)

**<font color=#1a73e8>作者：</font>** Lingzhao Kong, Yongsheng Zang, Yu Kang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative perception enables connected agents to share complementary observations for 3D object detection, extending sensing range and mitigating occlusion. Under asynchronous communication, however, cooperative features arrive with temporal delay. Existing prediction-based methods compensate for these features mainly from the transmitting agent's own history, leaving residual misalignment with the ego agent's current observation; subsequent fusion also often overlooks spatial variations in alignment quality. We propose EgoRefine, an ego-referenced predictive alignment and reliability-aware fusion framework for asynchronous collaborative perception. Its Ego-referenced Predictive Alignment module uses the current ego feature to guide cooperative trajectory-field prediction and refines the sampling offsets along an ego-referenced trajectory direction. Its Trajectory-conditioned Reliability-aware Fusion module treats the trajectory discrepancy between the ego and cooperative streams and the directional refinement magnitude as alignment cues, using them to condition the relation between aligned features and adaptively reweight the two streams before convolutional fusion. Experiments on V2V4Real and DAIR-V2X-Seq show that EgoRefine outperforms TraF-Align by 1.6 and 2.9 points on average in AP@0.5 and AP@0.7, respectively. The source code will be made publicly available at this https URL.

---


### 47. [Bellman-Certified Rounding for Sparse Policy Deployment in MDPs](https://arxiv.org/abs/2610.00325)

**<font color=#1a73e8>作者：</font>** Zhaojun Peng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous policy optimization may spread an update across many states, even when deployment permits only a few complete state-level changes. We study how much discounted return can be retained when continuous row mixtures are rounded to sparse binary policies in finite MDPs. Policy-dependent visitation couples the row edits, while long horizons make global curvature bounds conservative. From $2d+2$ Bellman solves, we derive reusable envelopes that support uniform and candidate-specific guarantees before rounding. A rank-two rational representation of each exchange further permits weighted curvature integration along the realized trajectory. We prove that linear dimension dependence is unavoidable when the budget scales, and that exact global curvature thresholding is hard. Candidate-specific bounds raise pre-rounding certification coverage from $48.2\%$ to $74.1\%$ on the structured suite. At $\gamma=0.95$, local integration lowers the median bound-to-loss ratio from $402.3$ to $2.08$ on coupled instances.

---


### 48. [ContractRL: Shielded Group-Relative Policy Optimization for Auditable Tool-Call Repair](https://arxiv.org/abs/2610.00328)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Xiaobo Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structured tool calls often fail after only a small number of fields violate a schema or an execution contract. Regenerating the complete object enlarges the action surface and makes repeated repair difficult to audit. We introduce ContractRL, a contract-constrained sequential repair protocol that models verifier-guided JSON repair as a bounded decision process. At each step the policy observes the candidate, typed verifier feedback, JSON Pointer, immutable repair history, and remaining budget; a contract-derived action mask filters malformed or prohibited RFC-6902 operations before a deterministic validator performs the transition. We specify a contract-constrained group-relative objective for patch, retry, and abstention decisions while keeping canonical targets and semantic labels outside the online state until trace freeze. Under identical verifier information, ContractRL attains 0.9362 semantic success with 34.4 generated tokens, compared with 0.9076 and 44.9 tokens for Patch-SFT and 0.9148 and 137.2 tokens for full regeneration over 192 cases per seed and five seeds. Policy optimization improves semantic success from 0.9186 for supervised ContractRL to 0.9375. A separate three-seed paired evaluation against Patch-SFT yields a semantic difference of +0.0396 (95% CI $[+0.0137,+0.0662], p=0.0039$). Feedback, action-mask, budget, and schema-shift analyses connect these gains to localized correction, while adversarial and multi-turn evaluations characterize the remaining failure modes.

---


### 49. [Beyond Diagonal State Space Models: Exact Non-Abelian Group Tracking, Solvability Barriers, and Geometric Physical Manifolds](https://arxiv.org/abs/2610.00329)

**<font color=#1a73e8>作者：</font>** Zeyu Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selective state space models (SSMs), such as Mamba, S4D, and LRU, are bounded by transition matrix commutativity (A_t A_t' = A_t' A_t) and solvable affine transformation groups (Aff_D of derived length <= 2). Consequently, stacked multi-layer diagonal networks face severe optimization degradation on non-solvable simple groups such as A_5 due to the exponential circuit emulation depth required to simulate non-abelian commutators. We propose Non-Commutative State Space Models (NC-SSM), their real-orthogonal counterpart SO(3)-SSM, and arbitrary-dimension Cayley-SSM, lifting state transitions to compact Lie groups SU(2), SO(3), and SO(N). Via closed-form Euler-Rodrigues maps and rational Cayley transforms, NC-SSM achieves exact norm-preserving isometry (||U_t|| = 1). We introduce pure Hopf-fibration Bloch projective readouts (S^3/{+-1} =~ S^2 =~ SO(3)) to eliminate sign ambiguity, true quaternion parallel prefix scans (9.06x speedup at T=2048), and Identity-Gated Lie SSMs to eliminate sparse syntax phase drift. Extensive benchmarks across 14 experimental regimes show: (1) NC-SSM achieves 100% tracking on S_3, D_4, Q_8 and simple group A_5, where a 3-layer deep diagonal baseline collapses to 6.60% (p = 8.81e-4); (2) Cayley-SO(5)-SSM breaks Klein's 1884 ceiling on symmetric group S_5 (50.92% vs diagonal 5.25%, p = 0.0015, delivering 7.8x variance reduction over SO(3)); (3) SO(3)-SSM preserves Riemannian manifolds across 300 steps (< 3.12e-6 drift, > 580,000x advantage), achieving 0.04 deg dead-reckoning error and active tangent denoising; (4) NC-SSM achieves 74.36% on Dyck-2 and 30.26% on deep AST scope tracking (p = 0.0081); and (5) ablation confirms strict isometry is mathematically necessary for lossless long-range associative memory.

---


### 50. [Authorization for Self-Modifying AI Agent Populations: Conserving Authority across Replacement, Forking, and Rollback](https://arxiv.org/abs/2610.00347)

**<font color=#1a73e8>作者：</font>** Genliang Zhu, Chu Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Self-modifying AI agents can replace, fork, and roll back identity-bearing software while descendants remain executable. Per-successor authorization does not constrain the resulting population: siblings may duplicate quotas, combine permissions, survive ancestor cuts, or overlap predecessors during promotion. We define authorization succession, which conserves authority across the active frontier of a single-parent generation forest.
Our external protocol binds each generation to a manifest, root, unique parent, complete lineage, and fresh population sequence. Separate invariants bound root-lifetime consumption and current population exposure. A staged reservation freezes predecessor residual authority during replacement, while a partitioning fork validates the complete child family. Each commit atomically fences the predecessor and activates successors. Ancestor cuts invalidate dependent descendants; rollback creates a fresh generation without restoring spent authority; and a new root requires an independent grant. Under complete mediation, authenticated records, sound effect abstraction, durable monotone state, and complete lineage accounting, we prove population-safe succession, fork conservation, revocation closure, atomic handoff, rollback non-reminting, and exclusion of self-certification.
An executable evaluation covers 32 registered decisions through direct-call and mailbox mappings (64/64 replays; 28 allows, 36 denies). An independent checker accepts all 64 original traces and rejects 28/28 semantic mutants; 12/12 profile invariants, 16/16 crash cuts, and 32/32 contender schedules pass. Two external adapters reproduce all 32 decisions around measured OurArk and Darwin Godel Machine mutations, including fresh-process restart, atomic succession, and predecessor rejection. The results establish authorization succession for registered protected effects.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-385](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
