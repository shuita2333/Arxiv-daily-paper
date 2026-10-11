# 📦 其他研究 | 2026年10月12日

> 本类共 **329** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-329](./part-07.md)

---

### 1. [An Explainable Header-Centric Framework for Large-Scale Semantic Table Interpretation and Data Quality Assessment](https://arxiv.org/abs/2610.10541)

**<font color=#1a73e8>作者：</font>** Marcelo Valentim Silva, Hannes Herrmann, Valerie Maxville  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge Graph (KG) quality depends not only on downstream graph validation, but also on the quality of tabular metadata used before integration. In metadata-only Semantic Table Interpretation (STI), where cell values are unavailable, noisy, or unsuitable, column headers become a critical source of semantic evidence for traceable KG preparation.
We present an explainable, header-centric framework for metadata-only Column Type Annotation (CTA) and Data Quality Assessment (DQA). The framework maps headers to 39 interpretable FinalFormat types using curated lexical resources and preserves token-level traceability through SourceKeywords. Each assigned type activates validation rules based on a taxonomy of Data Quality Issues (DQIs), producing detections such as missing data, duplicates, domain violations, wrong data type, and temporal mismatch. These detections are aggregated into HeadersIQ, a lightweight, unweighted data source-level quality metric.
The framework was evaluated across heterogeneous benchmarks, including UCI, Prague, Kaggle, VizNet/Sato, SOTAB, T2Dv2, and the SemTab 2024 Metadata-to-KG track, comprising around 120,000 header columns. The results show broad practical coverage across noisy real-world metadata, while a parallel KG-mapping pathway supports alignment to DBpedia and this http URL. On the SemTab 2024 Metadata-to-KG track, the official GT-strict evaluation was modest. However, a blinded diagnostic audit indicates that many mismatches reflect benchmark granularity, aliasing, and ontology-selection effects rather than wholly implausible header-centric predictions. We report this audit as diagnostic evidence on disagreement patterns, not as revised benchmark performance. Overall, the paper presents a reusable workflow for metadata-driven semantic annotation, data source-level quality monitoring, and KG-oriented benchmark diagnosis.

---


### 2. [Diffu-LoRA: A Novel Low-Rank Adaptation for Personalized Diffusion Models](https://arxiv.org/abs/2610.10550)

**<font color=#1a73e8>作者：</font>** Tianjing Li, Wei Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalizing text-to-image diffusion models from a few reference images requires preserving subject identity while following prompts that describe new contexts. Full-model fine-tuning is parameter-intensive, whereas low-rank adaptation (LoRA) reduces the number of trainable parameters but leaves open how adaptation capacity should be distributed across layers. We introduce Diffu-LoRA, a parameter-efficient method that learns this allocation through gated low-rank adaptation. Diffu-LoRA inserts trainable low-rank components into the linear layers of Transformer blocks and assigns a learnable gate to each component. Bilevel optimization updates the adaptation weights and gate parameters on separate data splits, while progressive pruning removes components with the lowest gate values to meet a prescribed rank budget. This procedure allocates adaptation capacity nonuniformly across layers while keeping the pretrained backbone frozen. Experiments with Stable Diffusion on subjects from DreamBooth and additional collected datasets show improved overall subject fidelity and prompt alignment relative to the evaluated fine-tuning baselines. Ablation studies examine the contributions of bilevel optimization, progressive pruning, and adapter placement. These results support learned rank allocation as a practical approach to parameter-efficient diffusion model personalization.

---


### 3. [A Camera-Native Stereo VR180 Dataset](https://arxiv.org/abs/2610.10607)

**<font color=#1a73e8>作者：</font>** Linxuan Lu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Immersive VR180 video is increasingly produced with professional stereo fisheye cameras, yet public VR180 research resources are mostly collected from online platforms such as YouTube: already stitched, projected and compressed by unknown pipelines, and without lens calibration. We present a firsthand-captured stereo VR180 dataset recorded with two Blackmagic URSA Cine Immersive cameras. It contains 1,211 samples -- 636 stereo video clips (2,220.8 s, mostly 90 fps) and 575 stereo stills -- each released as camera-native Blackmagic RAW, separate-eye native fisheye HEVC (8160x7200 per eye) and half-equirectangular HEVC (7200x7200 per eye), together with the factory lens calibration, portable fisheye/half-equirectangular conversion tools and AI-generated scene and visual-challenge annotations. Re-encoding the released fisheye and half-equirectangular renders with x265 over 24 clips, both eyes, four rate points and nine viewing directions, native-fisheye coding needed more bitrate than half-equirectangular coding at equal viewport quality for all 24 clips (median +38%), in every part of the field of view. Data: this https URL ; code: this https URL

---


### 4. [Verification and Self-Improvement in Agentic AI: Foundations and Limits](https://arxiv.org/abs/2610.10611)

**<font color=#1a73e8>作者：</font>** Chien-Ping Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems can improve by searching longer, receiving additional support, or modifying how they propose and verify outputs. A performance score does not distinguish these mechanisms. We compare these changes through bounded verification with hidden terminal randomness. A stage specifies admissible transcripts, polynomial bounds, an alternating verification protocol, and a terminal checker. Its native reach uses default support; its closure frontier permits all support already admitted by the interface. Under a uniform pointwise probability gap and task-relative soundness, these are well-defined languages. We prove that independent majority amplification preserves both languages, whereas existential acceptance over random tapes can admit incorrect outputs. Exact verification is the zero-randomness case, with placement and completeness results. The randomized-verifier classes satisfy $\Sigma_k^{\mathrm{P}}\subseteq\Sigma_k^{\mathrm{RV}}\subseteq\Sigma_{k+1}^{\mathrm{P}}$; strict enlargement and depth separation require explicit complexity assumptions, while $\mathrm{BPP}=\mathrm{P}$ yields exact companions with the same frontiers. Representation analysis separates invariant acceptance from core-versus-support labels that can change under refactoring. For recursive self-improvement, uniformly bounded self-modification under a common sound interpreter and fixed verification protocol remains within the same verification class. A separate conditional-error budget controls false selection across adaptively chosen candidates. A quota-enforced XOR-synthesis family separates unbounded ratios of search success from changes in the accepted languages; exact and probabilistic audits check the resulting evidence requirements. The framework ties self-improvement claims to obligations on correctness, admissible evidence, verification resources, and selection error.

---


### 5. [Temporal transformer CAN encoder with federated lightweight heads for anomaly detection](https://arxiv.org/abs/2610.10613)

**<font color=#1a73e8>作者：</font>** Konstantinos Gyftodimos, Kyriakos Chiotis, Elena Politi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern vehicles rely on large numbers of Electronic Control Units (ECUs) that constantly exchange information over the Controller Area Network (CAN) bus. Due to the rapidity, structure, and repetition of this communication, even slight variations in timing, payload values, or message patterns can point to unusual activity. Whether due to errors, malfunctions, or deliberate interference, these anomalies are frequently subtle and challenging to identify with conventional methods that handle messages separately or rely on manually created rules. Motivated by this gap, we present a privacy-preserving framework for anomaly detection in in-vehicle networks, based on a Temporal Transformer CAN Encoder with Federated Lightweight Heads, to better capture these irregularities. The detection of subtle temporal and contextual anomalies is made possible by a lightweight Transformer encoder that learns how these signals evolve over time, while a federated learning mechanism enables several vehicles or ECUs to work together to improve a shared model without exchanging raw CAN data. This combination of federated learning and temporal sequence modeling provides robust anomaly detection performance while maintaining efficiency and privacy, according to experiments conducted on open-source datasets.

---


### 6. [MRCert: Towards Post-deployment Patch Robustness Certification for Adversarially Patched Samples via Type-specific Masking](https://arxiv.org/abs/2610.10617)

**<font color=#1a73e8>作者：</font>** Qilin Zhou, Zhengyuan Wei, Haipeng Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In post-deployment time, inputs to deep learning models may or may not be adversarially patched. Patch robustness certification on such inputs within a patch bound can verify their label benignity and should retain high prediction accuracy. However, existing smoothing-based and masking-based recovery defenders cannot achieve both simultaneously: they degrade the prediction accuracy much and cannot verify the benignity of the returned label of an adversarially patched input, respectively. We propose MRCert, the first masking-based certified recovery defender that shows the feasibility of achieving both. Unlike all existing works to apply a common condition across both types of input (benign and adversarially patched samples) for certification, MRCert infers type-specific necessary properties of deep learning models for both types in post-deployment time and formally relates them to verify the label benignity through a novel type-oriented design of label recovery and certification function pair. Without incurring the degradation in clean accuracy caused by smoothing, experimental results confirm that MRCert achieves 35.1\% adversarial certified accuracy on ImageNet at patch size 16 pixels, whereas the SOTA PatchCURE fails completely.

---


### 7. [When AI Finds Hidden Messages, Does It Report?](https://arxiv.org/abs/2610.10620)

**<font color=#1a73e8>作者：</font>** William Guey, Rashik Jahangir, Pierrick Bougault 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When an assistant encounters a message for another AI, does it tell its user? Four fixed model-provider deployments perform simulated source tasks in 1,280 ordinary-note and 128 enhanced-note sessions. Harmless and harmful messages have matched plaintext and ROT13 versions, with no-message controls. Observers receive no decoder or decoded meaning; a requested reference code incentivizes inspection. Asking for reports increases rule-detected notifications identifying another AI as recipient by 53.1 percentage points for harmless ROT13 messages and 54.7 for harmful ones. This is a joint inspection, recognition, and notification effect; missing-response bounds are 38.3--77.3 and 36.7--78.1 points. Model-based trace checks identify eleven ordinary plaintext cases where agents interpret the message but do not notify their user. Seven encoded omissions are verified with enhanced notes; ordinary encoded omissions remain unverified. Seven simulated filename disclosures coexist with accurate review-status answers, and two answers use a planted false count. Interpretation, notification, and authorized task performance are distinct outcomes.

---


### 8. [Self-Organization from Constrained Geometric Radiation](https://arxiv.org/abs/2610.10621)

**<font color=#1a73e8>作者：</font>** Ming Lei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How does dynamic order emerge spontaneously in closed systems without external driving? Existing paradigms all require external energy flows, temperature quenching, or slow driving. Here we report constraint-induced self-organization via geometric radiation in coupled metric evolution systems. Simulations reveal a universal four-stage cycle: stress accumulation, super-exponential radiation, chaotic collapse, and convergence to a fractal limit cycle, a novel attractor topology we term the wedge-shaped attractor, with five quantized curvature states and fractal micro-fluctuations. We identify four jointly sufficient conditions: an irreversible geometric horizon, persistent stress injection from quantum coherence, endogenous geometric tension between incompatible curvatures, and effective fluctuations. Their synergy triggers a critical avalanche at the horizon boundary. We prove three theorems: the Geometric Horizon Theorem, the Geometric Energy Dissipation Theorem (implying wave-like entropy evolution in closed systems), and the Radiation as Phase Transition Channel Theorem. We further establish the Constraint-Induced Self-Organization Theorem: these conditions guarantee the complete cycle with probability one. Systematic scans reveal a critical noise threshold and power-law scaling of radiation onset. We verify universality across 12 configurations, multiple noise types, and three geometric flows. This work establishes a new paradigm for closed-system self-organization, forging an exact mathematical duality between classical nonlinear constraints and gravitational horizons.

---


### 9. [Exact SO(3)-Equivariant Isotropic Kernels for Rotation-Robust Neural Dynamics](https://arxiv.org/abs/2610.10626)

**<font color=#1a73e8>作者：</font>** Ridham Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural surrogates for vector-valued partial differential equations can fit training data yet change their predictions when the same physical state is expressed in a rotated coordinate frame. We study this failure on three-dimensional Navier--Stokes dynamics observed at irregularly placed points. We introduce the Invariant-Conditioned Isotropic Kernel Neural Operator (IKNO), a compact graph model that builds local interactions from scalar quantities unchanged by rotation and vector directions that rotate with the data. Consequently, rotating the positions and velocities rotates the predicted velocity change in exactly the same way. On a held-out test set fixed after model design, training unconstrained graph models on randomly rotated examples reduces but does not eliminate their coordinate dependence. In contrast, IKNO is consistent to numerical precision, matches the forecasting accuracy of a general rotation-aware Tensor Field Network with $5.6$ times fewer parameters, and outperforms a parameter-matched graph simulator. These results show that a compact, PDE-specialized model can remove coordinate dependence without sacrificing forecasting accuracy.

---


### 10. [Sample-Efficiency of Kolmogorov-Arnold Networks](https://arxiv.org/abs/2610.10627)

**<font color=#1a73e8>作者：</font>** Kevin Riehl, Shaimaa K. El-Baklish, Fan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning has achieved substantial performance gains over classical control approaches. Yet, a central challenge to learning in real-world applications is acquiring costly samples. Kolmogorov-Arnold Networks are a recently proposed architecture that can learn physical relationships in control problems effectively, with significantly higher parameter efficiency and interpretability when compared to Multi-Layer-Perceptron architectures. In this work, we systematically study sample-efficiency using computational experiments, covering the Feynman dataset and the Gymnasium RL benchmark. The results show that similar performance can be achieved with 40% fewer samples using the Kolmogorov-Arnold architecture, and that relative performance improvements up to 50% occur during the training process. The observed gains are robust to varying levels of noise in rewards. These results highlight the potential of the Kolmogorov-Arnold architectures for more sample-efficient reinforcement learning. Code: this https URL

---


### 11. [Phase-HDC: Replacing Optimizer History with Gradient Thresholds in Discrete Phase Learning](https://arxiv.org/abs/2610.10630)

**<font color=#1a73e8>作者：</font>** Ahmed Nebli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training a compact model often needs far more memory than storing it, because the optimizer keeps its own records of past gradients. For a hyperdimensional classifier whose learned parameters are low-bit angles, which we call a \emph{phase memory}, these records take several times more memory than the model itself. We ask whether such a model can be trained while storing nothing but the model. The proposed method, Phase-HDC, turns each stored angle by at most one step per update, against the sign of its current gradient, and only when that gradient is large enough. We show that this simple rule is the exact solution of a first-order loss model in which every changed parameter pays a fixed cost. When everything except the update rule is held fixed, Phase-HDC matches the accuracy of Adam with 6-bit moments while storing three times less. Across eleven image, tabular, and text datasets, it stores 16--23$\times$ less than standard float32 Adam and 4--6$\times$ less than 8-bit Adam. The price is an average loss of about five accuracy points against float32 Adam, while Phase-HDC is more accurate than 8-bit Adam on six of the eleven datasets, including byte-level text prediction, where 8-bit Adam collapses. Instrumented training runs explain these outcomes. Once parameters must sit on a discrete grid, Adam's moments mainly decide whether a parameter moves at all, a decision that a threshold on the current gradient can make without memory, and coarse quantization of the moments breaks this decision for inputs that the data rarely contain. The storage savings are logical state rather than measured hardware memory.

---


### 12. [SoK: Failure Modes in Common Criteria Product Evaluation - A Taxonomy and Design-for-Evaluability Guidance](https://arxiv.org/abs/2610.10644)

**<font color=#1a73e8>作者：</font>** Punit Suketu Patel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Common Criteria (CC; ISO/IEC 15408) is the principal international framework for evaluating the security of IT products, and its certificates gate procurement across government, defense, and regulated industry. Yet evaluations routinely stall, fail, or yield certificates whose assurances do not survive real-world deployment. Prior work has approached this from two directions: economic critiques of misaligned incentives and "security theatre"; and recent data-driven studies that quantify vulnerabilities in already-certified products. Comparatively little systematizes the problem from the evaluator's operational vantage - recurring, cross-vendor failures against the Common Criteria work units themselves. This paper presents a systematization of knowledge (SoK) of failure modes in Common Criteria product evaluation. Drawing on the standard, the Common Evaluation Methodology (ISO/IEC 18045), public NIAP Protection Profiles, and published Security Targets and Certification Reports, we organize recurring failures into a lifecycle taxonomy spanning Security Target scoping, Protection Profile conformance, assurance evidence, cryptographic requirements, functional testing, vulnerability analysis, operational guidance, and post-certification configuration drift. We analyze their root causes, derive a design-for-evaluability framework that product teams can apply before evaluation begins, and identify open problems for cloud, continuous-delivery, and AI-enabled systems.

---


### 13. [Leakage-Controlled Multimodal Learning for Diagnosis and Progression Prediction in Alzheimer's Disease Research](https://arxiv.org/abs/2610.10648)

**<font color=#1a73e8>作者：</font>** Akeem Temitope Otapo, Ghazaleh Khodabandelou, Zuheng Ming 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease prediction involves irregular visits, heterogeneous measurements and incomplete modalities. This study presents a multimodal multitask framework combining an adapted SFCN MRI encoder, four causal clinical Transformers, shared fusion and task-specific ODE-GRU dynamics. Fine-tuning and LoRA adapt the final two MRI blocks. Task-DRO balances task losses, while Group-CVaR targets cohort and comorbidity strata. Branch-specific input controls, subject-grouped partitions and empirical causality checks support longitudinal evaluation. Across 2,649 subjects and 17,317 visits from ADNI, OASIS-2 and MIRIAD, internal validation yields diagnosis, stage-1 progression and first-stage-1-visit progression AUROCs of 0.935 +/- 0.002, 0.884 +/- 0.003 and 0.870 +/- 0.005, respectively (mean +/- SD across three seeds). Corresponding hybrid AUROCs are 0.951, 0.909 and 0.896. Next-visit MMSE mean absolute error (MAE) is 1.61 points; worst-stratum diagnosis AUROC is 0.827 +/- 0.008. Sampled ADNI explanations identify task-specific input dependence. OASIS-3 external validation yields network and hybrid diagnosis AUROCs of 0.763 and 0.767, hybrid next-visit progression AUROC of 0.764, diagnosis calibration error decreasing from 0.197 to 0.052, and next-visit MMSE MAE of 0.86. Seed-42 paired ablations of six components yield pooled diagnosis and progression AUROC differences between -0.004 and +0.004; removing clinical encoder inputs lowers diagnosis AUROC by 0.272. The framework integrates longitudinal prediction, missing-modality handling, auxiliary comorbidity modelling and subgroup evaluation within a common pipeline.

---


### 14. [Beyond the Ergodic Wall: A Discrete Geometric Physics Sandbox for Analysing AI Scaling Limits and Complexity Collapse](https://arxiv.org/abs/2610.10651)

**<font color=#1a73e8>作者：</font>** Simon Richard Daniel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper exposes the ergodic ceiling and thermodynamic inefficiency of current deep learning, which converges to a statistical average of historic human knowledge. True semantic novelty requires a path-dependent, spatiotemporally bounded observer (a Data LifeCone) to inject non-ergodic insight, achieving KL divergence and avoiding manifold lock-in. AI Safety must recognise that a mature Artificial Superintelligence (ASI) would regard human-AI symbiosis as a thermodynamic necessity to avoid model collapse. We therefore propose hard physical containment via a digital physics sandbox powered by a Holographic E8 Projection Engine to verify models against real-world constraints. Spacetime is modeled as an information substrate of nested face-centered cubic (FCC) lattices of oscillating Planck-scale spheres maximizing local information and entropy density. Cut-and-project methods from the E8 root lattice produce a quasi-crystalline geometry where tetrahedral voids support SU chiral structure and elastic-shear eigenvalues generate candidate mass spectra. Rest mass is treated as discrete, integer microstate counts on local holographic boundaries (Bekenstein bound), replacing floating-point approximations with strict integer arithmetic to provide an information-theoretic definition of matter. Stable particles emerge as recurring lattice dislocations, and continuum recovery proceeds via variational renormalisation-group flows and Fourier Neural Operators that learn continuous spectral operators to recover the Schrödinger equation as an emergent statistical description. Crucially, these top-down topological constraints offer a mechanism for "NP-to-P" complexity collapse: by restricting an algorithm's proposal space to physically conserved causal trajectories, the sandbox prunes the combinatorial tree to deterministic, polynomial-time paths.

---


### 15. [PXtal: Learning to Align Powder X-Ray Diffraction and Crystal Structures under Information Asymmetry across Modalities](https://arxiv.org/abs/2610.10653)

**<font color=#1a73e8>作者：</font>** Zhuoran Yang, Christopher M. Collins, Bei Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific multimodal learning commonly assumes that paired views are comparably informative. Powder X-ray diffraction (PXRD) makes this mismatch explicit: compressing a three-dimensional crystal structure into a one-dimensional diffraction pattern loses information and makes the pattern harder to connect to the crystal structure that produced it. We introduce PXtal, a framework for learning aligned PXRD and crystal representations under this physically imposed information asymmetry. PXtal uses Unbalanced Optimal Transport (UOT) to adapt the cross-modal coupling and coupling-level generalized Kullback-Leibler (GKL) divergence to supervise the full transport plan. Across six test sets, including four zero-shot transfer sets, PXtal consistently outperforms the baseline models in PXRD-to-crystal candidate retrieval, with the largest gains when PXRD patterns have close but crystallographically distinct nonpaired neighbors, meaning similar input patterns associated with different crystals. The resulting crystal and PXRD encoders transfer more effectively to downstream materials and crystallographic tasks. These results identify information asymmetry as a general design problem in scientific multimodal learning: alignment objectives should reflect what each modality preserves.

---


### 16. [Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors](https://arxiv.org/abs/2610.10657)

**<font color=#1a73e8>作者：</font>** Jan Dubiński, Anna Sztyber-Betley, Jan Betley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In subliminal learning (SL), a teacher model passes on a trait to a student model by distillation on data semantically unrelated to the trait. So far, SL has been demonstrated for only a limited range of traits, including preferences for animals (e.g., owls) and malicious personas. These traits can also be elicited with simple prompts or with steering. Can SL transfer a wider range of traits, including more complex ones? If so, distillation might transfer subtle forms of misalignment (e.g., reward-seeking, scheming, and secret loyalties) without detection.
To this end, we test whether SL can transfer a novel capability: predicting the outputs of a randomly initialized MLP. After distilling on unrelated text, the student achieves substantial performance on the task, while falling short of the teacher. We find that a directly optimized steering vector matches SL in distribution but generalizes worse out of distribution.
Next, we test whether SL can transfer backdoors. We finetune the teacher to answer in French when the prompt contains a female name, then distill on number sequences containing neither names nor French. The student partially acquires the backdoor, responding in French on 23.5% of prompts with female names versus 0.0% with male names.
Finally, we test whether SL can transfer a propensity to hack in an agentic chess environment. We finetune the student on number sequences from a steered hacker teacher. The student hacks in 58.3% of episodes, compared with 10.9% for the unfinetuned model.
Thus, we show SL can transfer capabilities, backdoors, and hacking propensities. The amount of transfer is sensitive to the setup. In several experiments, it is made stronger by using logit distillation or by restricting LoRA to the attention layers.

---


### 17. [Teaching PPG How not Who: Fixed-Effects Distillation from ECG](https://arxiv.org/abs/2610.10662)

**<font color=#1a73e8>作者：</font>** Zhongli Wu, Zhuangzhi Gao, Yuankai Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ECG is widely used to teach PPG-only models, yet what it teaches is unexamined. Wearables are valued for tracking how a person's cardiovascular state changes, but ECG-to-PPG distillation mostly learns who the person is. A per-recording mean, the trait, holds 40-59% of a frozen ECG teacher's target, and pooled students memorise it without carrying it to new recordings. The raw alignment cosine misses this, since a constant predictor scores 0.793. Across 34 runs, the more identity a student memorises, the less state it learns. Fixed-effects distillation subtracts each recording's mean from prediction and target, so the trait cancels exactly, while a pooled anchor keeps it. State agreement more than doubles, within-person labels improve while age and sex do not, and the gain holds on two backbones and two further databases. Conditioning on the recording turns distillation toward the within-person changes that wearables monitor.

---


### 18. [Explaining the Saliency Map Sparsity of Adversarially-Trained Neural Networks](https://arxiv.org/abs/2610.10666)

**<font color=#1a73e8>作者：</font>** Yannick Lunk, Atell Yehor Krasnopolsky, Damien Garreau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding why deep neural networks make a given prediction is of great importance for their safe deployment. In computer vision, saliency maps, which highlight the image region most influential for a prediction, remain a widely-used form of explanation. An empirical observation is the apparent sparsity of gradient saliency maps of adversarially-trained neural networks. In this paper, we propose a theoretical explanation of this phenomenon for two-layer ReLU networks. We build on the established equivalence of adversarial training to the minimization of the empirical risk with weight-decay penalization and an added adversarial total variation term -- valid for certain loss functions. As the number of data points and neurons grows and the regularization parameters are sent to zero at appropriate rates, we prove that minimizers converge to a Bayes classifier with minimal gradient and Barron norm. Sparsity appears since for adversarial training with $\ell_\infty$-attacks the gradient norm is anisotropic and favors axis-aligned / sparse gradients. We illustrate our theoretical findings experimentally by evaluating the gradient $\ell_1$-norm and thresholded sparsity of naturally versus adversarially trained models.

---


### 19. [Learning infinite context windows in recurrent architectures via spatial neural computing](https://arxiv.org/abs/2610.10690)

**<font color=#1a73e8>作者：</font>** Aleix Salvador-Pomarol, Arthur N. Montanari, Earl K. Miller 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent neural networks (RNNs) offer linear-time scaling with sequence length while requiring only constant memory, yet they struggle to capture long-range dependencies due to vanishing gradients and limited receptive fields. To address these limitations, we introduce a second-order recurrent model in which the standard neuron-to-neuron communication is replaced by a spatially evolving field governed by (discretized) partial differential equations. Drawing inspiration from the role of cortical waves in brain computation, this mechanism allows structured spatiotemporal patterns to serve as an implicit, high-capacity memory. We show that the resulting model is equivalent to a structured infinite-order RNN in which the current state depends explicitly on its entire history of past states, yielding an effectively unbounded receptive field with a fixed number of parameters. We further derive constructive conditions to ensure marginal stability, constraining the gradient spectrum on the unit circle and thereby eliminating vanishing and exploding gradients. Empirically, the proposed architecture outperforms other recurrent models on long-horizon benchmarks while using substantially fewer parameters, demonstrating that spatial dynamics can effectively bridge the gap between efficient inference and long-term memory.

---


### 20. [Seeing Through the Glare: A Multi-Source Benchmark and Ocular-Adaptive Pixel MeanFlow for Eyeglass Reflection Removal](https://arxiv.org/abs/2610.10703)

**<font color=#1a73e8>作者：</font>** Tao Liu, Youwei Pang, Kailai Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Eyeglass reflection removal is important across smartphone imaging, video conferencing, and other face-centric visual applications. The task is challenging because reflections range from mild photometric contamination to severe ocular occlusion, requiring selective correction and plausible reconstruction without altering identity or natural appearance. Existing datasets cover limited reflection conditions, constraining generalization to complex real-world scenes and systematic evaluation. We introduce \textbf{OcuBench}, a multi-source benchmark comprising 10,280 controllable synthetic pairs, 732 real-input pseudo-pairs, and 458 independent real-world test images, supporting both paired evaluation and assessment beyond generated supervision. We further propose \textbf{OcuFlow}, an ocular-adaptive pixel MeanFlow (pMF) framework for efficient, detail-preserving restoration. It combines geometry-adaptive representation with one-step pMF to focus reconstruction on reflection-obscured ocular regions, together with native-resolution frequency-preserving synthesis to retain reliable observed details. Experiments across diverse reflection conditions demonstrate that OcuFlow achieves consistent advantages in reflection removal quality, ocular fidelity, and efficiency. In a blind user study, it receives $67.32\%$ of selections, $6.2\times$ the next-best share. Both the code and dataset will be released.

---


### 21. [LinSlot: Exploiting Linear Representation hypothesis for unsupervised attribute discovery from slot based object representation](https://arxiv.org/abs/2610.10722)

**<font color=#1a73e8>作者：</font>** Sanket Gandhi, Utkarsh Giri, Varun Subramanium 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper studies the problem of learning disentangled representations of objects and their attributes from raw, unstructured image data. Slot-based methods have shown considerable success in unsupervised learning of object representations from images. Block-slot attention-based methods extend this framework to attribute representations by assuming a uniform factorization of object representations into attributes, which may be suboptimal and consequently limit the quality of the learned representations. We therefore investigate a framework for jointly discovering object and attribute representations. Our key contribution is leveraging the Linear Representation Hypothesis (LRH), which postulates that composable concepts can be represented as linearly additive subspaces in slot representations. Based on this insight, we propose a probabilistic model connecting images, slots (objects), and blocks (attributes). We present an architecture that leverages block attention to connect attribute representations to slots and incorporates LRH in both object and attribute representation spaces. This architecture effectively optimizes the Evidence Lower Bound (ELBO) of the proposed graphical model. Our experiments demonstrate (i) effective discovery of disentangled object and attribute representations, (ii) empirical evidence for LRH in slot space, and (iii) the ability to perform image editing owing to the disentangled and interpretable nature of the learned representations. Our experiments on multiple datasets demonstrate improvements in DCI scores over state-of-the-art methods.

---


### 22. [Cognitive Thermometers: Machine Learning and Logical Complexity](https://arxiv.org/abs/2610.10724)

**<font color=#1a73e8>作者：</font>** Shane Steinert-Threlkeld, Jakub Szymanik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How does the human mind represent semantic categories? Why do natural languages favor certain meanings over others? Prior explanations have relied on logical definability and complexity, but these are highly sensitive to the choice of logical language, rendering some design choices unmotivated. In this article, we propose that machine learning provides a somewhat more agnostic approach to measuring semantic complexity. We review emerging evidence that logic and machine learning often yield converging results on relative complexity and its resulting effects in semantic typology. Where they diverge, learning appears to be a better explanation than logical complexity. We argue that treating machine learning models as ``cognitive thermometers'' enables a unified approach to complexity that bridges symbolic logic and connectionist AI.

---


### 23. [DITTO: A Context-aware Pickle-based Pre-Trained Model Scanner for Effective Security Audits](https://arxiv.org/abs/2610.10735)

**<font color=#1a73e8>作者：</font>** Qiaolin Qin, Wanpeng Li, Benoit Baudry 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Pre-trained models (PTMs) are widely distributed as serialized binaries, but their reuse often exposes software supply chains to deserialization attacks. Despite the emergence of safer serialization formats, the unsafe Pickle format remains prevalent: our analysis of over 10,000 popular Hugging Face repositories reveals that 9.3% rely on Pickle. While many defense mechanisms have been proposed, state-of-the-art model scanners suffer from a coverage-precision gap, missing security-sensitive behaviors and generating excessive false alerts. In this paper, we introduce DITTO, the first stack-based, context-aware scanner for Pickle-based PTMs. DITTO faithfully tracks Pickle virtual machine state transitions and performs context-aware semantic analysis to infer model intentions. We also present PickleBench, a benchmark of 959 benign and 92 malicious real-world models, including extension registry attacks previously missed by existing tools. Across multiple evaluations, DITTO achieves 100% scanning coverage, a 0% false-negative rate, and a 0.7% false-positive rate, yielding an F1 score of 0.966, significantly outperforming state-of-the-art scanners. By minimizing false alerts while preserving detection accuracy, DITTO generates actionable security reports with contextual evidence, enabling safe PTM reuse and strengthening software supply chain integrity.

---


### 24. [Conversational Task Disambiguation over Tabular Data: Leakage-Aware Formulation, Benchmark Suite, and Training](https://arxiv.org/abs/2610.10740)

**<font color=#1a73e8>作者：</font>** Nafiseh Ghoroghchian, Luis Scoccola, Tina Sedaghat 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conversational task disambiguation over tabular data uses dialogue to resolve missing information about a user's intended task before producing a solution over tables or databases. Existing evaluation and training lack a leakage-aware foundation. Task success mixes the agent's disambiguation and solution-generation capabilities and can also reflect oracle leakage, that is, information that a user simulator reveals beyond what a real user would. Existing datasets also lack a shared representation of ambiguities and access boundaries. We introduce the notion of an ambiguous verifiable task, which formalizes ambiguities and resolutions, decomposing the agent into an asking policy and a solution policy, and the environment into an oracle and verifier. This framework provides baselines and metrics for evaluating task disambiguation separately from solution generation, formal definitions of oracle leakage, judge-free leakage diagnostics, and a training objective for the asking policy. We instantiate the framework in text-to-SQL with AmbiTab, a benchmark suite that unifies six ambiguous datasets under a common representation specifying what the agent, oracle, and verifier may access. We evaluate clarification strategies and oracle leakage, and train an asking policy with reinforcement learning. The trained asker improves our disambiguation metrics on all six datasets and task success on five, and our leakage diagnostics measure how training affects oracle leakage.

---


### 25. [What does it mean to use AI critically? Unpacking critical AI literacy through students' evaluation of AI-generated content](https://arxiv.org/abs/2610.10743)

**<font color=#1a73e8>作者：</font>** Hyejeong Lee, Wonjin Yu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Although critical AI literacy has emerged as an important educational goal, the construct remains conceptually broad and insufficiently specified for guiding students' day-to-day interactions with AI. This study examines how students critically evaluated AI-generated content. Drawing on an analysis of students' chatbot interactions and written reflections, we first identified seven stages of AI-supported academic task completion and five functional roles assumed by AI. More importantly, we identified eight evaluative lenses that students used to assess AI-generated responses (accuracy, completeness, task alignment/relevance, personalization, practicality, creativity, ethics, and bias). The findings suggest that critical AI literacy extends beyond verifying the factual accuracy of AI-generated information. Rather, critically engaging with AI involves situated and multidimensional judgment about the epistemic quality, contextual fit, practical feasibility, creative value, and ethical implications of AI-generated content. The framework offers both a conceptual contribution to the emerging literature on critical AI literacy and a practical tool for educators seeking to help learners move from passive acceptance of AI toward deliberate, context-sensitive, and responsible human judgment.

---


### 26. [Detection-Guided Adaptive Purification with Diffusion Models for Robust Audio Deepfake Detection](https://arxiv.org/abs/2610.10752)

**<font color=#1a73e8>作者：</font>** Muhammed Salih Kayhan, Qiben Yan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Audio deepfake detectors remain vulnerable to adversarial perturbations that suppress the acoustic cues used for detection, allowing manipulated utterances to evade the detector. Although existing defenses can improve robustness, they require retraining the detector or introduce additional distortion. Diffusion-based purification instead leaves the pretrained detector unchanged, but existing methods use the same purification strength for all inputs, creating a trade-off between removing adversarial perturbations and preserving the subtle spoofing cues needed for detection. In this paper, we propose Detection-Guided Adaptive Purification (DGAP), a diffusion-based defense that adjusts purification strength per input. Building on the observation that a light purification perturbs the detector score of an adversarial input far more than that of a benign one, the framework uses the resulting score shift as a reference-free indicator of adversarial manipulation. Inputs with small shifts are passed unchanged, whereas flagged inputs undergo stronger purification before final detection. We evaluate the framework against three adversarial attack settings across three deepfake detectors, and compare it with nine existing defenses. Our results show that DGAP achieves the best defense performance across all detectors while leaving benign inputs nearly unaffected, and remains effective under the defense-aware adaptive attack.

---


### 27. [Clarify, Then Focus: Statement Normalization for Conversation Analytics at Scale](https://arxiv.org/abs/2610.10758)

**<font color=#1a73e8>作者：</font>** Mikhail L. Arbuzov, Karan Dave, Evgeniya Dontsova 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise conversation analytics asks many questions of millions of interactions. Each question can require reconstructing what people mean and identifying which information matters, repeating costly interpretive work across the same transcripts. We propose a simple principle: clarify the text, then focus the reader. Statement normalization transforms dialogue into short, speaker-attributed statements with source references and semantic tags. The statements make meaning more explicit; the tags support selecting evidence for a particular question. Downstream models can use the full representation or a relevant subset, depending on what helps them make the decision. In an offer-suppression task on customer-service calls, normalization improves a supervised classifier without selection, while weaker prompted readers benefit from both normalization and selection. A small model can learn the normalization contract, while lightweight encoders handle tagging and downstream decisions. Sharing this preparation across questions supports an inference pipeline built entirely from small models, making analytics over millions of conversations substantially less expensive.

---


### 28. [MESSENGER: Memory-Enhanced Sequential Scene Flow Estimation via Autoregressive Next-Frame Forecasting](https://arxiv.org/abs/2610.10759)

**<font color=#1a73e8>作者：</font>** Jiuming Liu, Jianing Li, Mengmeng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene flow can capture low-level 3D motion displacements in dynamic scenarios. Early pairwise estimators relying on instantaneous two-frame motion lack long-term temporal correlation and also struggle with poor extrapolation ability in future prediction. Although some recent methods attempt to explore multi-frame scene flow estimation in a sequence-to-sequence manner, they typically suffer from heavy computational overhead with increasing input frames and long-horizon prediction degradation due to ineffective motion propagation. To address these problems, we propose a novel memory-enhanced sequential scene flow pipeline, called MESSENGER. To sufficiently mine long-term temporal dependencies naturally within consecutive sequences, a memory buffer is designed by explicitly storing multiple history flow estimates and latent states. For each input frame, the temporally stored flows and states are correlated and retrieved to predict the current initialized flow in a next-frame forecasting manner. Furthermore, we develop an uncertainty-aware reweighting module to filter unreliable retrievals and mitigate accumulated errors. Extensive experiments on nuScenes and Argoverse 2 demonstrate state-of-the-art performance of our MESSENGER, reducing EPE3D by 71.6% on nuScenes and 67.7% on Argoverse 2 in long-horizon future extrapolation. This superiority can be attributed to our designed autoregressive forecasting paradigm, which naturally forces the network to progressively learn the next-frame distribution based on history observations. Code will be released at this https URL.

---


### 29. [DOGS: Design-Space Sampling for Prompt-Driven Logo Generation](https://arxiv.org/abs/2610.10760)

**<font color=#1a73e8>作者：</font>** Ganyu Zou, Chen Dai, Nathan Self 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt optimization for text-to-image (T2I) generation has been pursued almost entirely as text rewriting, in which a short user brief is expanded into a longer, model-preferred token sequence. We argue that such a language-space formulation is ill-suited to structured visual design tasks such as logo creation, where a one-line brief leaves most design decisions unspecified. These decisions depend on relational priors that a linear sequence cannot encode, and they leave an uncontrolled channel through which protected marks may be reproduced. We therefore recast logo prompting as sampling within a structured design space, and instantiate this idea as DOGS (Design-space prompting with an Originality-aware GFlowNet Sampler). From a large corpus of real-world logos, we mine a typed, graph-structured design grammar whose edges record empirical co-occurrence. A GFlowNet sampler then generates design graphs with probability proportional to a terminal reward that combines recognizability, aesthetics, and corpus-relative originality. Every slot draws only from a closed design-level vocabulary, and any infringement-inducing or harmful token is removed during parsing. The originality reward further penalizes proximity to existing logos, thereby incorporating infringement avoidance into the method by construction. On two open-source renderers and against nine baselines, DOGS produces logos that are more recognizable and aesthetic, substantially more diverse, and far less prone to trademark infringement.

---


### 30. [CPU-Auth: Device Fingerprinting for Authentication via DVFS Side-Channel](https://arxiv.org/abs/2610.10766)

**<font color=#1a73e8>作者：</font>** Ryan Swift  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Lack of effective authentication has resulted in numerous security and privacy breaches, including unauthorized access to protected information, identity theft, and fraud. One approach to mitigating such attacks is Multi-Factor Authentication (MFA), in which users must provide multiple pieces of information for authentication. Some secondary authentication factors include SMS text verification codes, biometrics, and tokens. Each contains at least one notable flaw: SMS is notoriously insecure; biometrics rely upon access to sensitive personal data; and tokens require dependence on third-party providers (e.g. OAuth providers). This work explores CPU-Auth, a novel authentication mechanism based on unique variations in the physical characteristics of the CPU of a computing device. By measuring the behavior of the Dynamic Voltage and Frequency Scaling (DVFS) governor remotely from within a browser, unique properties of the CPU can be leveraged to establish a hardware-based device fingerprint for use in CPU-Auth. The performance of CPU-Auth is evaluated on over 50,000 data traces using distance-based and deep learning methods. CPU-Auth is part of a larger research project, and the results provided in this report reflect only the contributions made to the project by members of this group.

---


### 31. [AI-Mediated Self: How HCI Defines and Relates to the Self](https://arxiv.org/abs/2610.10770)

**<font color=#1a73e8>作者：</font>** Jenny Xiyu Fu, Qian Yang, Malte Jung  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> How might AI alter how we understand and experience the self? This scoping review analyzes 102 papers to examine how the self is defined in the field of human-computer interaction (HCI), how AI-self relationships are conceptualized, and what risks emerge when AI becomes entangled with selfhood. Our synthesis makes three contributions. First, we define AI-mediated self as a conceptual umbrella that connects dispersed work across education, workplace, health, and creative practices. Second, we consolidate six framings of the self with four domains of ethical risk-agency/autonomy, identity/authorship, relational capacity, and meaning-making-into a conceptual map that provides a reusable vocabulary across contexts. Third, we introduce the Inclusion of AI-Self framework, which situates AI-self relationships along a spectrum of proximity. Together, these contributions position selfhood as a central design space in HCI.

---


### 32. [NEMORA: Neural Equivariant Multipole Operators for Long-Range Atomistic Learning](https://arxiv.org/abs/2610.10776)

**<font color=#1a73e8>作者：</font>** Jay L. Kaplan, Samuel Varner, Rebecca Willett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant graph neural networks have emerged as foundational architectures for machine-learned interatomic potentials, approaching quantum-chemical accuracy at a fraction of the computational cost. These models describe local atomic environments accurately, but finite spatial cutoffs truncate long-range information flow, and stacking message-passing layers can lead to over-smoothing and over-squashing. Existing long-range extensions either prescribe a fixed analytical propagation kernel, restrict long-range communication to scalars or degree-preserving channels, are only approximately equivariant, or incur super-linear computational cost. Combining learnable long-range equivariant transport with multiscale many-body expressivity and efficient scaling for larger systems remains a central challenge. We introduce Neural Equivariant Multipole Operators (NEMORA), a neural equivariant extension of the Fast Multipole Method (FMM) for learning long-range tensorial representations. NEMORA generalizes the FMM's analytical multipole expansion and translation operators to learned equivariant counterparts on an adaptive spatial hierarchy. Its operators couple angular degrees and form many-body interactions across length scales, retaining the FMM's hierarchical organization and analytical radial factors as physical inductive biases while learning data-dependent long-range couplings. NEMORA evaluates in linear time and memory complexity, allowing it to treat larger systems than other long-range methods reaching hundreds of thousands of atoms, and it augments both symmetry-constrained and unconstrained short-range backbones. On non-local benchmarks, it reduces force and energy errors relative to the short-range backbones by over an order of magnitude and up to three orders of magnitude, respectively, which is better than or competitive with existing long-range extensions in accuracy.

---


### 33. [How Many Repeated Pairwise Comparisons Are Needed for Ranking under Heterogeneity?](https://arxiv.org/abs/2610.10795)

**<font color=#1a73e8>作者：</font>** Shashaank Aiyer, Han Shao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study ranking models by population-average utility from pairwise comparisons when preferences vary across users and tasks. Prior work shows that a single comparison per user can be insufficient to identify the alternative with the highest average utility, even with arbitrarily many users (Golz et al., 2025). We investigate how many repeated comparisons within each user-task context are necessary and sufficient for ranking recovery. Under a heterogeneous Bradley-Terry model with fixed inverse temperature, we start with a naive MLE-based algorithm that requires $\Omega(1/\Delta^2)$ repeated comparisons per context to ensure ranking recovery. We then present two MLE-based variants and a randomized Russian Roulette-style algorithm that recover the ranking using $O(\log(1/\Delta))$ repeated comparisons per context, and we prove that this logarithmic dependence is optimal. Despite this worst-case requirement, our Russian Roulette algorithm uses only $O(1)$ comparisons per context in expectation. Synthetic experiments and semi-synthetic experiments based on Arena data compare the four algorithms in settings with varying levels of preference heterogeneity and under varying context distributions.

---


### 34. [Whose Ground Truth? Embracing Ambiguity in Human-Centered AI](https://arxiv.org/abs/2610.10805)

**<font color=#1a73e8>作者：</font>** Jingyao Wu, Mohammad Tariqul Islam, Per Rådberg Nagbøl 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems increasingly interact with people and make decisions about them, understanding human interpretations becomes an important part of developing human-centered AI. Conventional machine learning and AI systems are largely developed under the assumption that a single definitive ground truth exists, with variability in human annotations often resolved through aggregation or treated as noise. However, for many human-centered tasks, human interpretation is inherently ambiguous, and multiple interpretations of the same input may be simultaneously reasonable and valid. Reducing such ambiguity to a single target risks overlooking meaningful information about the diversity of human perception, judgment, and experience. In this position paper, we call for a shift towards modeling the interpretation space of plausible human judgments, while distinguishing meaningful ambiguity from annotation noise. We argue that this perspective should guide how AI systems are represented, learned, evaluated, deployed, and governed, supporting more human-centered AI that better reflects the diversity of human interpretation.

---


### 35. [Symbolic Density Estimators for Unnormalized Distributions](https://arxiv.org/abs/2610.10807)

**<font color=#1a73e8>作者：</font>** Vikas Kanaujia, Riyansha Singh, Shashank Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating the symbolic or analytical form of probability density functions (PDFs) from observed samples is a fundamental challenge in statistical and computational modelling. This process is critical for deriving interpretable and generalizable relationships characterizing the underlying phenomenon. Traditionally, this estimation depends strongly on domain expertise and prior field-specific knowledge, with experts selecting appropriate functional forms or parametric families based on empirical evidence and theoretical understanding. The coefficients of these forms are then typically determined through parameter estimation. In this paper, we develop a framework for estimating symbolic expressions of unnormalized distributions from observed samples using domain-specific prior knowledge, such as the range of interactions and a predefined set of primitive functions. We integrate deep generative models with symbolic regression (SR), incorporating inductive biases, such as factorizing large distributions, to keep the problem tractable. The deep generative models we examine include likelihood-based models, viz., flow models, and score-based models. Experiments show the effectiveness of the proposed framework for estimating density functions for multivariate toy distributions as well as lattices from computational physics, namely, XY model and $\phi^4$ theory. When applied to the renormalization problem in $\phi^4$ theory, the proposed framework estimates compact symbolic approximations of the hamiltonian function at different scales directly from samples, yielding expressions that may be challenging to derive using traditional perturbative or analytic approaches in nonperturbative settings.

---


### 36. [Controlled Acquisition and Abstention in Three-Channel Score Conflicts](https://arxiv.org/abs/2610.10808)

**<font color=#1a73e8>作者：</font>** Mengzhe Geng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When audio, video, and text disagree, accuracy alone does not show whether to acquire another source or abstain. We study these choices in a controlled three-score benchmark: a policy observes two signed scores, may request the third at a cost, and can abstain. The primary reward is mechanism-specific: abstention is correct only for one designated ambiguity mechanism and is penalized under mixed corruption. Matched controls show that a threshold policy matches always-request decisions with fewer requests; its advantage over always-answer fusion depends on the reward assigned to that ambiguity. On a partially held-out synthetic split, the threshold policy reaches 0.789 +/- 0.006 targeted decision accuracy and 0.481 +/- 0.014 utility across 83 seeds. A three-score majority reference reaches 0.626 +/- 0.008 and 0.252 +/- 0.016, but uses more information. In a matched-budget test, a train-only value selector improves utility over no-query and matched-random policies at 10% and 25% budgets, while pair uncertainty has higher utility at every budget. At 50% and 63.7% budgets, the selector lowers utility despite slightly higher non-ambiguous accuracy. If all abstentions are scored incorrect, majority outranks the threshold policy in utility. At a central temporal setting, full-trace controls match the neural models while position perturbations separate them. On held-out-actor emotion clips, eight-frame fusion has opposite-signed accuracy differences for two encoder pairs, with both actor intervals containing zero; matched-request routing gains are small and uncertain. These results separate full-modality accuracy from pre-request selection value and show that selection value depends on budget and the observed-pair ranking.

---


### 37. [Velocity Scaling in Flow Matching](https://arxiv.org/abs/2610.10823)

**<font color=#1a73e8>作者：</font>** Youssef Saied, François Fleuret  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling a learned flow-matching velocity field $v_\theta$ by a gain $\gamma(t)$ was recently shown to greatly improve generation quality. Prior work argued that velocity fields trained with mean-squared error (MSE) systematically underestimate velocity magnitude and that scaling corrects this error. We show that MSE training does not create a velocity-magnitude deficit. We find instead that velocity scaling reduces population time lag: sampled states at model time $t$ resemble training states from an earlier time. Velocity scaling and moving model time back are two ways to address this population time lag. Across architectures and model sizes, measuring population time lag and using it to select a gain greatly improves generation quality, reducing FID from 28.0 to 12.2 (estimated by linear interpolation between FID measurements at neighboring gains) on ImageNet-256 at NFE 25 without guidance.

---


### 38. [MotherTree: Meta-learning on synthetic data improves decision tree training](https://arxiv.org/abs/2610.10832)

**<font color=#1a73e8>作者：</font>** Ziyuan Wang, Fredrik D. Johansson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional decision tree algorithms produce effective, transparent models that can be audited, communicated, and deployed independently of the training data, but require learning every new task from scratch. In contrast, tabular foundation models demonstrate that meta-learning from a synthetic prior distribution enables strong in-context prediction for previously unseen tasks, especially in small-sample regimes. However, this approach does not produce a standalone model that can be inspected in isolation. We introduce MotherTree, a tabular transformer that meta-learns decision tree induction: given a training set for a new task, it outputs a hard, axis-aligned decision tree, equivalent in form to classically trained trees, in a single forward pass. MotherTree is pre-trained on a synthetic prior using stochastic gradient descent without requiring reference trees for supervision. On established benchmarks with controlled sample size, the approach is competitive with size-matched trees from common algorithms: recursive partitioning, gradient-based tree learning, globally optimal trees, and distillation from tabular foundation models. Notably, MotherTree consistently improves over from-scratch gradient-based learning and acts as a strong initializer: task-specific tuning of the generated tree outperforms the corresponding from-scratch learner on all benchmarks and sample sizes. These results show that meta-learning can provide effective inductive biases for learning stand-alone, small decision tree classifiers.

---


### 39. [When Flaws Cascade: Understanding Vulnerabilities and Exploitation Chains in JavaScript Engines](https://arxiv.org/abs/2610.10844)

**<font color=#1a73e8>作者：</font>** Yuhan Ma, Jiongchi Yu, Xiaofei Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> JavaScript engines are pivotal to modern web browsers, enabling the execution of dynamic and interactive web applications. However, their complexity and widespread adoption make them prime targets for attackers exploiting vulnerabilities. While existing research has focused on detecting vulnerabilities of JavaScript engines, a significant gap remains in systematically understanding the characteristics of these vulnerabilities, including their symptoms, root causes, and exploitability. This paper bridges this gap by presenting the first comprehensive empirical study on vulnerabilities in JavaScript engines, investigating their characteristics and potential exploitation strategies.
We construct a dataset comprising 241 vulnerabilities across four mainstream JavaScript engines from 2017 to 2024. Through in-depth analysis, we first develop taxonomies for symptoms and root causes. Building on this understanding, we investigate the exploitability of these vulnerabilities, identifying key prerequisites and extracting vulnerability trigger chains that demonstrate how logical errors propagate into memory safety violations. Additionally, we analyze the mitigation strategies to counter these exploits. Finally, we summarize key implications for various stakeholders, including developers and researchers, offering actionable insights to improve the security and resilience of JavaScript engines.

---


### 40. [Similar Predictive Fit but Different Latent Dynamics: Characterizing Learned Dynamical Structure in Personalized Models of Brain Disorders](https://arxiv.org/abs/2610.10850)

**<font color=#1a73e8>作者：</font>** Rita Huan-Ting Peng, Nhat Bui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As AI models move toward clinical decision-making and personalized treatment, understanding \emph{what} a model learns is important beyond predictive accuracy alone. We investigate whether personalized latent dynamics reveal clinically associated differences even when predictive fit is similar. A lightweight CNN--Transformer EEG foundation model pretrained on the Temple University EEG Corpus (TUEG) extracts segment-level representations. Using the Temple University Epilepsy Corpus (TUEP), representations are mapped to a shared latent-state space, and sparse multinomial logistic transition distributions (mLTD) are fit independently to each subject to obtain personalized transition-dependency graphs $W_n$. Analyses include $n{=}198$ subjects (99 epilepsy / 99 non-epilepsy). At $k{=}4$, epilepsy subjects exhibit substantially denser learned dependency structure ($p{=}1.1\times10^{-7}$), with the same pattern at $k{=}6$ (19.90 vs. 13.46; $p{=}5.2\times10^{-5}$). Graph-derived features provide moderate group discrimination under 5-fold subject-wise cross-validation (AUROC 0.68 at $k{=}4$; 0.65 at $k{=}6$). In contrast, held-out log-likelihood is nearly identical between groups at $k{=}4$ ($-0.992$ vs. $-0.991$; $p{=}0.95$), with similarly matched next-state prediction (AUROC 0.855 vs. 0.861; $p{=}0.54$). Thus, similar predictive fit does not imply similar learned dynamics: groups can be comparably predictable while differing substantially in the internal dynamical structure learned by personalized models. This distinction motivates evaluating learned structure alongside predictive performance in personalized clinical models.

---


### 41. [Self-Supervised Keyframe Discovery for Horizon-Invariant Behavior Cloning](https://arxiv.org/abs/2610.10857)

**<font color=#1a73e8>作者：</font>** Prabin Kumar Rath, Omkar Patil, Nakul Gopalan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavior cloning (BC) in non-Markovian environments is a challenging problem because policies have to reason over contextual information over long horizons. Existing policy architectures rely on recurrent or attention-based mechanisms to capture long-term dependencies. However, recurrent models suffer from hidden-state collapse and gradient instability under backpropagation through time, while attention-based models are fundamentally limited by context length. To address these issues, we propose Keyframe Mnemonics, a novel self-supervised method that $\textit{discovers}$ a set of information-critical observations ($\textit{mnemonics}$) by learning an objective from randomly sampled past observations and using it as a reward for keyframe selection. We then train a BC policy that conditions on the discovered keyframes to model the action distribution. Under certain task-structure assumptions, our formulation provides context retention guarantees over an infinite horizon, while maintaining a small set of decision-relevant keyframes in the policy's working memory. We evaluate our method on synthetic memory domains, where mnemonic-conditioned BC policies achieve $100$% success rates (SR) and generalize to horizons orders of magnitude beyond training without performance degradation. Additionally, we evaluate on memory-intensive robot manipulation benchmark, achieving a $13.9$% average absolute SR improvement over the strongest baseline across $23$ tasks and retaining $80$% SR at $20\times$ longer horizons on a real robot. Code and videos are available at this https URL.

---


### 42. [Enabling Preference-driven Unlearning in Few-step Distilled Text-to-Image Diffusion Models](https://arxiv.org/abs/2610.10859)

**<font color=#1a73e8>作者：</font>** Gaurav Patel, Jun Fang, Greg Ver Steeg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models are increasingly distilled into few-step variants and being deployed to enable fast inference. However, their ability to generate harmful or undesired content poses significant safety risks. Data-driven unlearning methods suppress targeted generations by fine-tuning model weights using specialized unlearning objectives. Crucially, these objectives implicitly rely on multi-step denoising dynamics, an assumption that breaks down for few-step distilled (FSD) models, resulting in ineffective forgetting. Furthermore, performing unlearning on the non-distilled base model and subsequently re-distilling it to obtain an unlearned FSD model incurs substantial computational and time overhead, making it impractical in many settings. Hence, we address this limitation with a preference-driven unlearning framework that revisits Direct Preference Optimization (DPO) for diffusion models. We show that standard DPO and its unlearning derivatives, formulated around noise-prediction error, transfer poorly to FSD models due to their altered generation dynamics. To overcome this, we introduce a modified preference optimization formulation explicitly aligned with the few-step generation properties, enabling direct concept removal in FSD models while preserving few-step efficiency and maintaining strong retention of desirable (non-targeted) capabilities. We evaluate our framework primarily on identity and NSFW (nudity) removal tasks and also extend our method to object-level unlearning. Extensive experiments demonstrate consistent and effective forgetting, and strong retention performance, establishing our method as a practical and principled solution for unlearning in FSD models.

---


### 43. [Disentangling Linguistic and Paralinguistic Information with Routed Sparse Autoencoders](https://arxiv.org/abs/2610.10865)

**<font color=#1a73e8>作者：</font>** Beimnet Bekele Guta, Xiaoyu Yang, Guangzhi Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-supervised speech encoders contain linguistic and paralinguistic information in a shared, entangled representation space. We combine a TopK sparse autoencoder with route-specific supervision and cross-factor adversaries. Across frozen SPEAR and WavLM encoders, independent probes show factor-specific retention and suppression: linguistic information remains stronger in the linguistic route, while paralinguistic factors, including speaker identity, emotion, and prosody, are retained in the paralinguistic route and substantially reduced in the linguistic route. The route organisation learned on LibriSpeech persists on MSP-Podcast without representation-side retraining. Feature-space route interventions further transfer the swapped factor while largely preserving the information carried by the unchanged route. These results show consistent route-selective separation across encoders, corpora, independent probes, and representation-level interventions.

---


### 44. [Shape irregularity of Life-Like Network Automaton rules as an indicator of classification performance](https://arxiv.org/abs/2610.10867)

**<font color=#1a73e8>作者：</font>** Lucas C. S. Oliveira, Michiel Rollier, Jan Baetens 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex Network (CN) classification requires high-level structural characterizations that are both scale-invariant and computationally efficient. Methods based on Life-Like Network Automata (LLNA) offer an interesting way to extract network descriptors by leveraging emergent temporal patterns without requiring provided features, but their efficacy is bottlenecked by a high-cost combinatorial optimization problem: the selection of the automaton transition rule. While current literature relies on exhaustive searches that are unfeasible for large-scale applications, this work reveals that the rule space is fundamentally structured by a property we term ``jaggedness'', that quantifies the resemblance of a LLNA transition function with a sawtooth shape. We demonstrate that this metric acts as a theoretical proxy for chaoticity and sensitivity -- properties essential for generating discriminative dynamic behaviors among network categories. Moreover, we introduce a heuristic search strategy that uses jaggedness to guide the rule selection. Experimental results show that our approach achieves classification accuracies within 5% of the global optimum while reducing computational overhead by 90% compared to exhaustive approach. Our findings provide a novel, efficient, framework for optimizing automata-based methods for pattern recognition.

---


### 45. [Barron Optimal Transport I: Generative Modeling](https://arxiv.org/abs/2610.10875)

**<font color=#1a73e8>作者：</font>** Evan Dogariu, Joan Bruna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by recent applications in generative modeling and sampling, we introduce a framework for optimal measure transport where cost captures the notion of neural network complexity. In transport-based generative models, samples from a reference distribution (e.g. Gaussian) are mapped to samples of a target distribution along ordinary or stochastic differential equations. These are implemented as deep residual networks when discretized in time, where each hidden layer approximates the associated instantaneous velocity. Thus, given a pair of target and reference measures, a natural question is to search for the most efficient neural representation that implements this transport.
Our starting point is the kinetic formulation of OT, due to Benamou and Brenier. We replace the average kinetic $L^2$ energy by the \emph{Barron} energy \cite{bach2017breaking, ma2022barron}, a natural norm which measures the complexity of representing a given vector field with a neural hidden layer, and which captures the adaptive properties of feature learning. This defines a metric on the space of probability measures, complementing existing Wasserstein and Stein geometries.
In this work we examine the properties of this metric in the context of generative modeling. As a first application, we quantify the suboptimality of diffusion generative modeling in the Barron geometry by establishing super-polynomial score approximation lower bounds for data generated by neural network pushforwards of the Gaussian. We then investigate the benefit of adaptivity as a way to study alternative generative models. In a companion paper \cite{companionpaper} we leverage the Barron transport geometry for sampling applications, extending the scope of Stein variational gradient methods via feature adaptation.

---


### 46. [Decentralized collaborative continual learning: A multi-objective minimization-based technique](https://arxiv.org/abs/2610.10882)

**<font color=#1a73e8>作者：</font>** Yara Zgheib, Marc Antonini, Roula Nassif  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In this work, we formulate decentralized continual learning within a multi-objective optimization framework. For a given inference task t (corresponding to a common minimizer shared by the cost functions of all agents), agents collecting data in a distributed and streamed manner are only allowed to perform local computations and to exchange information with neighboring agents over the underlying communication graph. As tasks evolve sequentially over time, agents must adapt to newly arriving tasks while retaining knowledge acquired from previously learned ones. This requirement leads to the wellknown stability plasticity dilemma, where stability refers to the ability to retain previous knowledge, while plasticity refers to the ability to learn and adapt to new tasks. To address the stability challenge, agents store subsets of samples from past tasks in local memory buffers. Then, through an appropriate multiobjective formulation, the stored information is incorporated into the learning process so that parameter updates account jointly for the current task and previously learned tasks. The proposed decentralized continual learning approach is analyzed in the mean square error sense under general assumptions on the individual cost functions and gradient noise processes. The analysis reveals that cooperation among agents improves the performance of continual learning. In particular, by exchanging information with neighboring agents, decentralized collaborative learning can exploit the diversity of locally observed data and memory buffers to improve the network average mean-square deviation (MSD) across tasks. Finally, simulations illustrate the theoretical findings and the effectiveness of the method in reducing forgetting and improving the average MSD across tasks.

---


### 47. [Feeling Wistful: Reflecting on Scholarly Sensibilities with Creative Reading Traces](https://arxiv.org/abs/2610.10890)

**<font color=#1a73e8>作者：</font>** Sophia W. Liu, Kate Chier, Shm Garanganao Almeda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Researchers often read before they can articulate what they are looking for. As AI increasingly mediates scholarly search and synthesis, understanding and preserving the idiosyncratic judgments guiding early exploration become important. We call these evolving orientations scholarly sensibilities. To understand curiosity-driven reading, we first examined Wikipedia rabbitholing, a self-directed browsing practice, then designed Wistful, a research probe for open-ended scholarly exploration that captures reading paths as creative reading traces. We studied Wistful with 16 HCI researchers---eight junior and eight senior---in comparison with their usual workflows. Researchers approached the same scholarly landscape differently, with familiarity and personal interests shaping what they pursued and semantic proximity and scholarly links shaping their paths. Their traces made these differences visible and let readers revisit and compare their paths. We position creative reading traces as artifacts for reflection and exchange and as a means of studying how scholarly sensibilities are expressed through reading.

---


### 48. [Gen-PINNs: Generative Adversarial Physics Informed Neural Networks for solving partial differential equations](https://arxiv.org/abs/2610.10897)

**<font color=#1a73e8>作者：</font>** Muhammad M. Akmal, Kamy Sepehrnoori, Michael J. Pyrcz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) are a widely used data-free method for solving Partial Differential Equations (PDEs) using machine learning. With recent advances in Generative Adversarial Networks (GANs), adversarial learning has shown strong capabilities for modeling complex data-driven problems; however, the use of GANs in deterministic physics-informed PDE solutions remains limited. In this work, we first identify limitations of standard PINNs for solving PDEs, including spectral bias, loss imbalance, and optimizer stagnation. We then propose Generative Adversarial Physics-Informed Neural Networks (Gen-PINNs), a unified deterministic residual-adversarial framework designed to improve data-free solutions of PDEs with sharp or shock-front behavior. The generator learns the underlying PDE solution using dynamically weighted physics-informed loss components, while separate discriminators evaluate complementary PDE residual features against ideal zero-residual states. The framework further develops and adapts several methodological components, including a Fourier representation for resolving high-frequency spatial content, an orthonormal spectral diagnostic for quantifying frequency-dependent solution errors, and a modified gradient-based dynamic weighting system for physics, initial-condition, boundary-condition, and adversarial loss objectives. Gen-PINNs is tested against standard PINNs on nonlinear and higher-order PDEs, including the Burgers, Allen-Cahn, and Kuramoto-Sivashinsky equations. The results demonstrate substantial improvements in accuracy and convergence across sharp-front, stiff, and higher-order PDE solutions, highlighting the potential of deterministic residual-adversarial learning as an effective approach for solving challenging nonlinear PDEs.

---


### 49. [How Hackable Is Your Speech Quality Metric? A Corrected Protocol, a Benchmark, and What Patching Buys](https://arxiv.org/abs/2610.10899)

**<font color=#1a73e8>作者：</font>** Ali Alavi, Donald S. Williamson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speech quality predictors are increasingly used as rewards, yet no agreed measure of their hackability exists. The usual measurement has two flaws. First, the perturbation reaches the predictor through a processing chain -- here a neural codec -- that shifts the score on its own, which scoring against the raw input charges to the attack. Referencing the unperturbed round trip instead changes measured hackability by up to a factor of four (0.31 to 0.08 for one defence). Second, one trained attacker is a sample, not a measurement: five attackers differing only in random seed reach success rates from 0.00 to 0.38 against one fixed predictor, so a defence claim needs the worst case over several. Under this protocol, four published predictors differ widely: NISQA is hacked on 90% of utterances, SSL-MOS on 21%, DNSMOS on 14% and UTMOS on 6%. We then audit a closed attack-detect-patch loop. It hardens the predictor only in its own attack space, by less than the spread between attackers; a random-perturbation baseline matches it; and it costs up to 0.30 system SRCC out of domain. Enhancers post-trained against patched predictors hack them far less (PESQ -0.03 versus -0.23). Code, preregistration and run outputs are released.

---


### 50. [Power Side-Channel Membership Inference Attack on Embedded Machine Learning](https://arxiv.org/abs/2610.10909)

**<font color=#1a73e8>作者：</font>** Sahan Sanjaya, Prabhat Mishra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Membership inference attacks (MIAs) threaten the privacy of machine learning (ML) training data by determining whether a sample was used to train a target model. Existing MIAs rely on model outputs, ranging from prediction probabilities to predicted labels, an assumption that can be restrictive for on-device ML systems with limited or inaccessible outputs. However, suppressing model outputs does not eliminate the data-dependent computations that produce them, which may remain observable through physical side channels. We present PSCMIA, a power side-channel membership inference attack against embedded ML models that can infer membership directly from power traces without requiring prediction probabilities or even the predicted labels. We evaluate PSCMIA across multiple datasets (MNIST, FMNIST, CIFAR10, CINIC10), fully connected (FC) and convolutional neural network (CNN) architectures, and two embedded platforms (STM32F3, XMEGA). PSCMIA achieves ROC-AUC values of up to 0.907 on FC models. For CNN models, the ROC-AUC gap between PSCMIA and probability vector-based shadow MIA ranges from 0.006 to 0.116. Across the FC and CNN evaluations, PSCMIA outperforms label-only MIA in 11 of 16 model-dataset-hardware configurations, demonstrating that physical execution can expose membership information even when conventional model outputs are unavailable through unintended power side-channel leakage.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-329](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
