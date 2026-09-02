# 📦 其他研究 | 2026年09月03日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-236](./part-05.md)

---

### 151. [Figures as Programs: Recursive Generation of Editable Scientific Figures](https://arxiv.org/abs/2609.01006)

**<font color=#1a73e8>作者：</font>** Yepeng Liu, Dasen Dai, Chengzhi Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific methodology figures are essential for communicating complex methods clearly, yet creating them remains labor-intensive and typically requires multiple rounds of refinement. Recent image-generation models can synthesize visually appealing raster figures, but producing a human-satisfactory result in a single generation step remains difficult. Moreover, precise edits to raster figures are challenging for both humans and models. We formulate scientific figure generation as recursive SVG program construction and propose \textsc{FigTree}, a \textit{multi-agent} system that automatically transforms a scientific paper into a structured vector figure. \textsc{FigTree} grounds figure content in the source paper, decomposes a figure into a hierarchy of local regions, generates each region as a short SVG program, and assembles the resulting fragments. A render-critic refinement loop jointly inspects the rendered figure and its underlying program, enabling visual defects to be traced to specific statements and accurately repaired. We conduct extensive evaluations of \textsc{FigTree} on figure quality and editability, showing that \textsc{FigTree} produces high-quality figures, while also enabling more effective editing than existing raster-based methods.

---


### 152. [Low-Quality Face Recognition using Center Aligned Representations and Local Margin Constraints](https://arxiv.org/abs/2609.01014)

**<font color=#1a73e8>作者：</font>** Vedat Can Dilaver, Benjamin S. Riggan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-quality face recognition (LQFR) remains challenging due to the difficulty of matching degraded query (probe) images against low-quality (LQ) enrollment (gallery) imagery and the scarcity of training data for large-scale models. While recent face recognition (FR) models perform well on high-quality (HQ) imagery, their accuracy drops significantly on LQ images with extremely low signal-to-noise ratio (SNR). Moreover, fine-tuning HQ-pretrained models on LQ data often improves LQ recognition at the expense of HQ generalization. This trade-off becomes more pronounced in modern evaluation settings spanning multiple datasets with varying image quality levels. To address these limitations, we propose a unified framework that combines three main components: (1) Local Probability Margin (LPM), which estimates per-sample difficulty directly from the model's discriminative landscape; (2) Nested Attention Module (NAM), a new low-rank adapter module that embeds a self-attention mechanism within selected transformer layers; and (3) Quality Gating Protocol (QGP), where an off-the-shelf image quality estimator modulates the adapter contribution at test time, enabling a single model to handle the full quality spectrum without sacrificing HQ performance. Experiments on surveillance (TinyFace, SurvFace) and standard (IJB-B, IJB-C) face recognition benchmarks demonstrate consistent gains in both identification and verification. Code and models will be released at this http URL.

---


### 153. [Phrase-Localized Language-Contrastive Guidance: Training-Free Localized Accent Control for Code-Switching Text-to-Speech](https://arxiv.org/abs/2609.01016)

**<font color=#1a73e8>作者：</font>** Che Hyun Lee, Sangkwon Park, Donghun Kang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current speech synthesis struggles with code-switching, which mixes a foreign language phrase into a primary language utterance, causing the phrase to be spoken with the primary language's accent rather than its native one. We propose Phrase-Localized Language-Contrastive Guidance (LCG), a training-free inference framework that restores a native accent to code-switched phrases in cross-lingual text-to-speech. LCG replaces the single language guidance applied across the whole utterance with a separate guidance for each region, so each part is guided by its own language. To choose where to apply this localized guidance, we propose a self-attention probing technique that finds the phrase boundaries without external alignments. Together, these components generate speech in which each region carries the accent of its own language, requiring no fine-tuning or auxiliary models. Across diverse language pairs, LCG robustly increases the nativeness of the code-switched phrase while suppressing accent leakage, and preserving overall speaker identity and naturalness.

---


### 154. [Beyond Technological Solutionism: Rethinking XR in Healthcare](https://arxiv.org/abs/2609.01028)

**<font color=#1a73e8>作者：</font>** Md Haseen Akhtar, Cecilia Landa-Avila, Shital Desai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The healthcare industry's enthusiastic adoption of Extended Reality (XR) technologies obscures a concerning reality: we were building increasingly sophisticated ways to perpetuate fundamentally broken healthcare systems. Through three deeply personal narratives - a rural patient cut off from care infrastructure, an urban professional navigating fragmented services, and a first-generation immigrant confronting cultural barriers - this provocation paper exposes how our obsession with technological innovation often worsens rather than resolves healthcare disparities. By applying the SEIPS 3.0 model to examine diabetes-CVD care coordination, we identify an "innovation paradox" where advanced technology creates new barriers to effective care. Our care interdependencies framework reveals that healthcare outcomes are shaped primarily by human relationships (50-60%), organizational coordination (25-30%), and sociocultural factors (15-20%), not technological sophistication. This research challenges the HCI community to confront its role in perpetuating healthcare inequities, demands a fundamental rethinking and proposes a new framework for healthcare innovation that prioritizes human relationships over technical capability, systemic change over feature sets, and actual care delivery over technological ambition. For healthcare providers, technology developers, and policymakers, our findings suggest that effective care coordination requires us to step back from our techno-solutionist mindset and engage

---


### 155. [The Multiple Timescales of Gradient Descent on the Edge of Stability: A Perturbative Derivation of the Central Flow](https://arxiv.org/abs/2609.01034)

**<font color=#1a73e8>作者：</font>** Raphaël Berthier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The central flow of Cohen et al. (2025) is an empirically accurate continuous-time model of gradient descent at the edge of stability in deep learning, However, its derivation is heuristic. We propose a perturbative regime in which the central flow is the limit of gradient descent: we assume that the loss decomposes as $f = g + \varepsilon h$; in the limit $\varepsilon \to 0$, the dynamics of gradient descent with learning rate $\eta$ converge to the gradient flow of $h$ constrained to the minimizers of $g$ of sharpness at most $2/\eta$. Our approach is formal rather than rigorous; it treats gradient descent as a singularly perturbed dynamical system in $\varepsilon$. Three timescales emerge: a fast timescale of oscillations along the sharpest direction, an intermediate timescale of the self-stabilization mechanism, and a slow timescale of the dynamics along the minimizers of $g$-the central flow. Using the method of multiple scales, a classical formal method from singular perturbation theory, we derive the expansion of the dynamics in $\varepsilon$: the central flow emerges as the leading-order term in the expansion, while the self-stabilization mechanism appears in the next-order term. We study this mechanism beyond previous analyses: with a single eigenvalue at the edge of stability, we compute the slow drift of the energy of the fluctuations; with several eigenvalues at the edge of stability, we derive the self-stabilization system and explain why fluctuations persist.

---


### 156. [MultiGait: A Multi-Sensor Multi-Perspective Multi-Session Biometric Inference Benchmark and its Dataset](https://arxiv.org/abs/2609.01036)

**<font color=#1a73e8>作者：</font>** Julian Todt, Felix Morsbach, Philip Dissert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A lack of suitable datasets has limited the research into the privacy risks of novel smart city sensors, such as thermal cameras, depth cameras, and lidar. Given the number of unsubstantiated privacy claims and their potential widespread deployment into many people's everyday life, understanding the privacy risks of these sensors -- in isolation and in like-for-like comparisons -- is crucial. With MultiGait, we collected the first multi-sensor, multi-perspective, multi-session gait-focused dataset, for the corresponding, and additional more far-reaching investigations. The dataset, validated with multiple state-of-the-art recognition systems, comprises various walking modes and annotated personal attributes for 199 individuals, to ensure the benefit for advanced studies including cross-sensor recognition and anonymization at the edge. MultiGait represents a foundation for rigorous privacy investigations, demonstrated through an extensive identity inference benchmark across eight sensors, four perspectives, and three recording sessions. Our benchmark incidentally reveals that sensors often assumed to be privacy-friendly do still entail considerable identity inference risks, while the poor cross-session generalization of existing methods underscores an important research gap.

---


### 157. [ViTAMINS: An Empirical Study of Training Self-Supervised Vision Transformers with Synthetic Hard Negatives](https://arxiv.org/abs/2609.01041)

**<font color=#1a73e8>作者：</font>** Nikos Giakoumoglou, Andreas Floros, Kleanthis-Marios Papadopoulos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce ViTAMINS, a method that integrates synthetic hard negatives into unsupervised vision transformer pretraining to improve representation quality. Our approach is thoroughly benchmarked on ImageNet and transfer learning, image retrieval, copy detection, and image, video segmentation tasks. Notably, our proposed negatives give rise to emergent properties, where learned representations contain explicit information about the semantic content of an image and serve as excellent classifiers (up to +11.3% over baselines). ViTAMINS achieves these benefits through simple modifications to existing contrastive frameworks and outperforms competing methods while being more resource efficient, e.g., our ViT-B surpasses V-JEPA with ViT-L. Our findings motivate reconsidering contrastive learning as a simpler yet powerful alternative to dominant generative and self-distillation approaches.

---


### 158. [From Truncation to Commitment: Persistent Context in Uniform Discrete Diffusion](https://arxiv.org/abs/2609.01043)

**<font color=#1a73e8>作者：</font>** Satoshi Hayakawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uniform-state discrete diffusion models update all tokens in parallel while keeping every position revisable. Even when the commonly used top-$p$ rule leaves only one candidate at a position, that choice affects only the current reverse step and can be revised at the next sampling step. We ask what changes when selected hypotheses instead become persistent context for later predictions. We therefore propose committed reveal sampling (CRS), a training-free sampler that stores selected argmax tokens and inserts them into subsequent model inputs. Our analysis gives a rationale for selecting later and for keeping selected tokens visible. Under the exact forward process, the Bayes error of selecting a clean token cannot increase as noise decreases, while in a simple latent-mode model, keeping the selected token visible helps later parallel predictions agree on the same sequence-level choice. Empirically, paired experiments on Duo-distilled then separate this persistent effect from single-step top-$p$ restriction and scalar temperature scaling. Under the same finalization rule, CRS without top-$p$ truncation reaches lower generative perplexity (GenPPL) than fixed $p=0.95$ and $p=0.9$ baselines across budgets of 8--64 function evaluations (NFE). At 64 NFE, the comparison at matched unigram entropy also gives lower GenPPL for CRS, yielding a more favorable GenPPL--entropy tradeoff. Base Duo shows the same direction in a descriptive comparison, while other diversity and continuation metrics can rank these operating points differently. These results identify support restriction and persistent context as distinct controls of that tradeoff.

---


### 159. [Lagged Coupling: Internal Representations Become Readable Before They Become Causal](https://arxiv.org/abs/2609.01048)

**<font color=#1a73e8>作者：</font>** Xining Xun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Across the full Pythia suite (160M-12B, eight checkpoints, four task families), a linear probe can read a target variable from the residual stream as early as step 1,000 at every scale -- yet steering along that same reading direction remains null-equivalent in 43 of 48 model-checkpoint cells. Internal readability systematically outruns causal efficacy, and the lag does not shrink with scale. We call this structure lagged coupling and decompose it into three dissociable tracks: (i) internal readability, saturated (AUROC >= 0.990) from the first checkpoint everywhere; (ii) behavioral readability, which develops gradually and progressively later at larger scales (12B reaches 0.909 only at the final checkpoint); (iii) causal efficacy, almost always null-equivalent, occasionally counterproductive early, with one isolated positive pulse (12B, step 8,000, z = +2.49) our grid cannot resolve. The ordering is dominantly read-before-write (11/11 units, no inversion). Representation headroom along the probe direction grows up to 57x with training and scale while causal write-in stays below 0.11% of headroom -- the variable is increasingly written into the representation and increasingly ignored by the readout. Under a fully pre-registered protocol, both single-onset hypotheses resolve INDETERMINATE (scale slope +0.24, 95% CI [-0.60, +0.87]; time vote 3:3) -- a disciplined negative explained by the three-track decomposition. A pre-registered OLMo-2 replication preserves the direction at attenuated magnitude. Our results caution against inferring steerability from probe accuracy and establish a developmental bottleneck: representation formation reliably outpaces causal readout consolidation.

---


### 160. [QILP-0: Constructing Observational Declarative Twins of Quantum Circuits](https://arxiv.org/abs/2609.01049)

**<font color=#1a73e8>作者：</font>** Marina de la Cruz Echeandía, César Luis Alonso, Tony Ribeiro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces QXymb, a general framework for constructing observational declarative twins of quantum circuits, and develops QILP-0, its first complete order-0 specialization. QILP-0 constructs a finite multi-valued propositional logic program from observed circuit behaviour within a declared observational scope.
The pipeline traverses a declared family of quantum observables incrementally according to a reproducible structural grading and a declared observational reference horizon. Progress is quantified through reference-relative coverage against a fixed target-independent reference. Observable responses are organized through target-independent geometry, while retained latent structure is mapped deterministically back to original observable columns before symbolic processing, preserving observational semantics and provenance.
Selected observable profiles are converted into a finite relation through admissible target-independent discretization. The target is used only afterwards to audit twin-admissibility and induce the declarative theory. A theory is certified as an exact observational declarative twin when it completely and correctly reconstructs the resulting finite task-conditioned discrete relation. Logical exactness is therefore separated from numerical, backend, provider, and discretization uncertainty, which is retained as audit metadata.
Validation uses two complementary QML settings. Exhaustive Bars & Stripes experiments compare product and grid-CZ embeddings from 16 to 100 qubits and exercise the native-discrete branch. Low-Depth MNIST analyses all 14,708 digit-0/1 instances before and after a trained variational quantum transformation and exercises continuous discretization. In every reported relation, the induced QILP-0 theory achieves complete, conflict-free reconstruction with strict accuracy equal to one.

---


### 161. [What Limits Robustness in Deep Image Watermarking: An Analysis of Mechanisms and Their Scaling Across Capacities](https://arxiv.org/abs/2609.01050)

**<font color=#1a73e8>作者：</font>** Marta Bistroń, Zbigniew Piotrowski  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Robustness remains the principal open problem in deep image watermarking, and what limits it becomes sharper as payload grows. This paper asks whether capacity is itself the limit or only makes other limits visible, and answers in two parts. The first organizes the distortions a watermark must survive and the strategies developed to resist them, ordering each by the axis that governs it: payload capacity for the distortions, differentiability for the strategies. The second identifies and measures three mechanisms that limit robustness in schemes mapping the payload onto a spatial block grid with extraction trained separately from a frozen embedder: desynchronization of the payload grid, the resistance of codec-induced distortion to training, and the narrowing of the usable embedding-strength window. Payloads from 64 to 16384 bits are measured, well beyond the range those strategies address. Training the extraction stage against a codec proves not merely ineffective but harmful, degrading the reading at the operating points used in training. The limits follow the class of distortion rather than capacity itself, and none is removed by further training on the extraction side, because all three arise before extraction. An evaluation protocol making claims of generalization verifiable is also contributed. The conclusions are properties of a class of designs rather than of one implementation.

---


### 162. [SAGE: Subpopulation-Aware Generative Enhancement for Mitigating Spurious Correlations](https://arxiv.org/abs/2609.01051)

**<font color=#1a73e8>作者：</font>** Yiming Luo, Rongqiang Zhao, Jie Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spurious correlations pose a significant challenge to the robustness of modern machine learning. The inherent imbalance in dataset distributions often leads traditional Empirical Risk Minimization (ERM) models to rely on majority spurious attributes for classification, resulting in poor performance on minority groups. This problem becomes particularly challenging when the spurious attributes are unavailable. Existing group-label-free methods often upsample minority groups or misclassified real training examples; repeating the same instances can reduce effective diversity and encourage overfitting. To mitigate these spurious correlations from a data-centric perspective in the absence of prior knowledge, we introduce Subpopulation-Aware Generative Enhancement (SAGE), a two-stage generative augmentation framework. Using cluster-derived sub-labels and class labels, we fine-tune a conditional generative model and text encoder, generating targeted synthetic data to fill underrepresented regions in the training set and construct a balanced validation set for last-layer reweighting. We experimentally show that SAGE achieves 89.5%, 85.7%, and 79.1% worst-group accuracy on Waterbirds, CelebA, and MetaShift, respectively, outperforming the best group-label-free baselines by up to 7.7 percentage points.

---


### 163. [User Representation via Cross Multi-source Behavior Pre-training for Mobile Games](https://arxiv.org/abs/2609.01057)

**<font color=#1a73e8>作者：</font>** Chengqi Yang, Yiran Qiao, Feng Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> User representation pre-training has become a fundamental paradigm for alleviating data sparsity in downstream personalization tasks. However, existing studies predominantly focus on single-app or app-level behaviors, overlooking the inherently cross-source and multi-granular nature of user activities on mobile devices. At the device level, user intent emerges from complex interactions among heterogeneous behavior sources and hierarchical action structures, posing challenges that cannot be addressed by conventional app-centric modeling. To tackle this issue, we propose CM-PTM, a novel Cross Multi-source Behavior Pre-Training Model tailored for mobile game user representation learning on device-level behavioral logs. CM-PTM employs hierarchical cascaded mask-then-predict proxy tasks that first infer the source of the next behavior and then progressively refine predictions at the app-action level. This design enables unified modeling of cross-source dependencies and fine-grained behavioral dynamics within a single pre-training paradigm. Extensive experiments on large-scale real-world mobile datasets demonstrate that CM-PTM effectively captures users' endogenous interests and consistently delivers significant performance gains on downstream mobile game recommendation tasks.

---


### 164. [ARISE-RL: Agentic Rubric-Grounded Iterative Self-Evolution with Reinforcement Learning](https://arxiv.org/abs/2609.01058)

**<font color=#1a73e8>作者：</font>** Fanrui Zhang, Ruixue Ding, Qiang Zhang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training open-ended agents via reinforcement learning (RL) is hindered by the lack of verifiable gold answers and scalable rubrics. Moreover, even near the model's capability boundary, long-horizon open-ended agentic tasks often yield brittle and unstable rewards, resulting in weak or noisy rollout contrast that obscures fine-grained optimization signals for group-based policy learning. To address these challenges, we propose ARISE-RL, a novel full-cycle self-evolution framework that couples a task/rubric Generator and a reasoning Solver through rubric-mediated co-evolution. The Generator grounds tool-related rubric criteria in real tool observations and is rewarded for producing valid, intermediate-difficulty tasks aligned with the Solver's evolving capability boundary. The Solver, in turn, learns from fine-grained rubric satisfaction signals through multi-step reasoning and tool use. We further introduce Reward-Gated Self-Evolution Distillation (RG-SED), which selectively distills a memory-augmented variant of the same policy back into itself only when the memory yields empirical reward improvement, thereby reducing distribution mismatch and avoiding blind imitation of noisy guidance. Finally, to support rigorous evaluation, we present ECR-Bench, an expert-calibrated rubric benchmark suite covering single-tool deep research and multi-tool travel planning. Extensive experiments demonstrate that ARISE-RL consistently achieves robust and stable overall state-of-the-art performance across all evaluated benchmarks.

---


### 165. [Let Confidence Change, Not the Prediction: Prediction-Preserving Repair for Post-hoc Calibration](https://arxiv.org/abs/2609.01072)

**<font color=#1a73e8>作者：</font>** Daehwan Kim, Haejun Chung, Ikbeom Jang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc calibration corrects reported confidence, yet a multiclass calibrator can also change the associated top-1 prediction. Accuracy captures only the net effect of these changes on correctness, not how often predictions change; the Top-1 Prediction Change Rate (TPCR) instead measures this frequency. We propose Calibrator-Output Repair for Top-1 Decision Preservation (CORD), the first post-fit adapter to impose exact prediction preservation by repairing the full calibrated probability vector. From the original and calibrated outputs alone, CORD determines the mass assigned to the original top-1. The calibrated conditional distribution allocates the remaining mass over the other classes, yielding a repaired vector whose own argmax recovers the original prediction. On the calibration split, CORD coordinates the repaired masses to retain the calibrated outputs' mean mass on original predictions whenever attainable. The adapter alters neither the fitted calibrator nor its direct output, fits no additional supervised map, and requires no user- or validation-tuned hyperparameter. Across CIFAR-10/100 and ImageNet-1K, CORD attains zero TPCR by construction and lowers mean ECE, NLL, and Brier relative to the corresponding direct outputs in every dataset; paired gains persist under distribution shift and across calibration-set sizes. CORD thus removes the preservation constraint from calibrator fitting and assigns exact recovery of the original decision to subsequent output repair. Our code is available at this https URL.

---


### 166. [JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability](https://arxiv.org/abs/2609.01077)

**<font color=#1a73e8>作者：</font>** Valentin Abgrall, Marcello Traiola, Ruben Salvador 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety-critical real-time systems must satisfy multiple dependability requirements, notably time predictability and security. In such systems, tasks must complete within bounded and known execution times, typically characterised through Worst-Case Execution Time (WCET) analysis. At the same time, DRAM-based platforms are increasingly sensitive to the RowHammer read-disturbance security vulnerability, which has motivated the development of numerous hardware and software countermeasures in both academia and industry. However, the impact of these defences is generally evaluated in terms of average-case performance, a metric that is insufficient for safetycritical real-time systems, where worst-case behaviour is the primary concern. In this paper, we study the impact of RowHammer countermeasures based on hardware counters on the timing behaviour of real-time systems. We use a Per-Row-Activation-Counter (PRAC) countermeasure as a case study, standardised for recent DDR5 memories, and show that it can introduce significant timing variations. Based on this observation, we introduce JENGA, an attack in which an attacker-controlled task manipulates the internal state of the RowHammer countermeasure mechanism to increase the execution time of a victim real-time task beyond its expected WCET. We implement JENGA in a gem5 and Ramulator 2.0 simulation environment and evaluate its impact on TACLeBench workloads. We show that such an attack can delay tasks up to 200% of their WCET, making the initial timesafety assumptions unsafe. To address this issue, we derive a safe analytical bound that accounts for mitigation-induced delays in WCET analysis for DRAM systems protected by hardware countermeasures, such as PRAC-N.

---


### 167. [IT-TextFusion: Iterative Text-Image Interaction with Text-Guided Residual Refinement for Degradation-Aware Image Fusion](https://arxiv.org/abs/2609.01092)

**<font color=#1a73e8>作者：</font>** Siyang Liu, Peiyi Zhou, Tianle Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided image fusion has recently emerged as an effective paradigm for integrating multi-modal information while enabling flexible and task-oriented fusion control. However, existing text-guided fusion methods often rely on shallow semantic-visual interaction and limited attention mechanisms, which restrict their ability to robustly handle complex degradations and fully exploit textual guidance. In this paper, we propose an iterative text-guided image fusion framework that incorporates text-conditioned feature interaction across multiple fusion and refinement stages. The proposed method integrates deepest-level Cross-Attention, multi-scale Cross-Gate Fusion, and stage-specific text-conditioned modulation, allowing the global text embedding to condition hierarchical feature fusion and residual refinement. By repeatedly injecting the pooled text embedding across hierarchical decoder and refinement stages, the proposed framework provides degradation-aware global semantic conditioning while preserving complementary information from the visible and infrared modalities. Experiments on several benchmark datasets show that the proposed method improves several information-preservation and perceptual-quality metrics, while exhibiting metric-dependent trade-offs on some datasets.

---


### 168. [CRSF: Collusion-Resilient Privacy-Preserving Sensor Fusion with Byzantine-Robust Participation](https://arxiv.org/abs/2609.01096)

**<font color=#1a73e8>作者：</font>** Chao Yin, Haihong Tian, Zheng Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving sensor fusion enables an untrusted server to compute an aggregate result over distributed sensor measurements without learning either individual inputs or the final output. Recent garbled-circuit-based protocols provide an efficient realization of this functionality in a sensor--server--client architecture, but remain vulnerable to sensor--server collusion and Byzantine manipulation of sensor participation. These weaknesses can compromise honest-sensor privacy, incorrectly exclude honest sensors, and corrupt the computed fusion result, thereby undermining the security guarantees expected from the protocol.
We present CRSF, a collusion-resilient sensor-fusion protocol that addresses these weaknesses while providing privacy, correctness with explicit abort, and liveness. CRSF introduces a Practical Byzantine Fault Tolerance (PBFT)-based agreement phase for sensor submissions and uses server-specific, status-dependent label release with threshold protection of circuit-input labels. This design prevents any Byzantine server from unilaterally manipulating sensor participation and prevents any admissible sensor-server coalition from obtaining enough secret material to compromise honest-sensor privacy.
We implement CRSF and compare its online execution time with the most relevant state-of-the-art baseline. Our Google Cloud evaluation measures the total computation and communication cost of the online protocol under fault-free and representative faulty executions. Across a range of fault-tolerant fusion circuits and up to 261 sensors, CRSF demonstrates a highly practical trade-off between robust security and protocol performance.

---


### 169. [Neural Symbollic Regression Using Deep Learning and Sparse Modelling](https://arxiv.org/abs/2609.01102)

**<font color=#1a73e8>作者：</font>** Ravi Kumar U, Sumitra S  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic Regression (SR) seeks to find succinct mathematical expressions that represent the fundamental relationships within data, providing interpretability and scientific understanding that exceeds that of black-box models. Nevertheless, traditional methods like Genetic Programming face challenges with scalability and are highly sensitive to noise, while sparse regression techniques such as SINDy rely significantly on predetermined feature libraries. In this work, we present a Neural Symbolic Regression (NSR) framework that treats neural networks as functional preconditioners for symbolic discovery. Our approach uses a decoupled pipeline: a neural network first learns a smooth, noise-robust approximation of the target function in an interaction- aware nonlinear feature space. LASSO is then applied to extract sparse, interpretable closed-form expressions. To improve predictive accuracy and symbolic fidelity by integrating distributed hyperparameter optimization with Ray Tune and ASHA scheduling. Experiments on the Nguyen benchmark suite show that our approach consistently outperforms SINDy and non-tuned neural baselines in RMSE, noise robustness, and out-of-distribution generalization. Ablation studies confirm the significance of feature interactions, neural depth, and tuning strategies. In general, this study presents a scalable and understandable neural-symbolic framework, creating a solid link between neural approximation and the discovery of sparse equations for scientific machine learning.

---


### 170. [When Modality Gap Reduction Fails: Prediction-Level Hubness in CLIP](https://arxiv.org/abs/2609.01103)

**<font color=#1a73e8>作者：</font>** Shota Sato, Hajime Kiyama, Tosho Hirasawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reducing the modality gap between image and text representations in CLIP is widely expected to improve cross-modal alignment and downstream performance. However, a smaller average image-text gap does not necessarily lead to consistent accuracy gains. We analyze this mismatch from the perspective of the decision structure in zero-shot classification, i.e. selecting the most similar class-text prototype for an input image. Zero-shot accuracy depends not only on average image--text alignment, but also on class-wise decision margins. Using Linear correction as an analytically tractable case, we show that modality gap correction can alter the relative decision structure among classes and cause predictions to concentrate on a small subset of classes. We refer to this output-space failure mode as prediction-level hubness. Furthermore, experiments across multiple datasets show that accuracy degradation under gap correction is consistently associated with increased prediction concentration, both for Linear correction and for learning-based correction methods. This provides a systematic explanation of why modality gap reduction does not consistently improve CLIP zero-shot accuracy from the perspective of downstream decision structure. Our results suggest that gap correction should be evaluated not only by average alignment, but also by its impact on downstream prediction structure.

---


### 171. [Replicating TRACE: A Practitioner's Guide to Its Threshold and Particle Budget](https://arxiv.org/abs/2609.01108)

**<font color=#1a73e8>作者：</font>** Alex Chadyuk, Alicia Zhang, Roy Kucukates  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> TRACE (Math & Lienhart, arXiv:2602.01135) reads causal graphs over event types out of a pretrained autoregressive sequence model by thresholding a per-position conditional-mutual-information estimate at a fixed tau. We independently replicate its headline synthetic result: with tau selected on a validation split, mean per-sequence F1 against exact interventional truth reaches 0.90-0.91 at vocabulary size 1000 (paper: 0.91) and 0.86-0.91 from 100 to 2000. First, the optimal threshold is pinned to the truth margin, not to any constant: at every size the errors at tau* straddle the delta = 0.05 margin defining ground truth (missed true edges lie just above it, accepted false ones just below), and the blind optimum lands near delta/2 times the estimator's calibration, confirmed out of sample at 5000. Second, at a single global threshold TRACE mostly recovers a direct, adjacent-influence graph: lag-1 true edges are recalled at 0.97-0.99, while true edges at lag 2 or more read orders of magnitude lower---the reading-scale price of randomizing mediating positions, which an exact test of direct causal effect requires when the truth is unknown. A per-lag threshold family recovers a third to a half of lag-2 truth; on lag-uniform data one validated threshold recalls every lag at 0.40-0.87, 8-26 pp below an atomic-intervention control at lags 3-6. Third, the default lag decay of the paper's synthetic benchmark concentrates about 85% of interventional truth at lag 1 and pushes the rest below the estimator's noise floor, so headline F1 there certifies lag-1 recovery only and conflates the benchmark's skew with the algorithm's own limit; a flatter decay separates the two. Fourth, F1 saturates from N = 2 particles at the selected threshold---a property of the threshold's margin over the noise floor, not of the estimator, which converges as N^(-1/2). We distill five practitioner rules.

---


### 172. [P-PatchDiff: Progressive Patch Diffusion Models for Low-light Image Enhancement](https://arxiv.org/abs/2609.01123)

**<font color=#1a73e8>作者：</font>** Ruoyu Guo, Haonan Zhong, Maurice Pagnucco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in low-light image enhancement have leveraged diffusion models for their strong ability to generate perceptually realistic, detailed images. Patch diffusion models further offer a promising solution to size-agnostic image restoration while improving efficiency. However, existing methods typically rely on small, fixed patches (e.g., 64$\times$64) that cannot capture image-level brightness context, whereas enlarging the receptive field improves brightness and colour estimation but substantially increases computational cost. Moreover, low-light images often exhibit uneven brightness across regions, making it necessary to ensure that locally enhanced patches remain visually coherent when combined into the full image. To address these limitations, we propose P-PatchDiff, a scalable progressive patch diffusion framework for low-light image enhancement that dynamically adjusts patch size throughout the denoising process, enabling a gradual shift from local to global views. A Multi-Patch Alignment strategy is also introduced to normalise features across varying patch scales using an estimated global brightness proxy. Rather than pursuing pixel-level reconstruction accuracy, P-PatchDiff focuses on scalability and coherent brightness across the whole image, allowing the model to perceive multi-scale information and better enhance regions with varying brightness. We empirically demonstrate that P-PatchDiff effectively enhances images ranging from 400 $\times$ 600 to 4K and is 80$\times$ faster than existing patch diffusion models while using less than 9GB of memory. The code is available at this https URL.

---


### 173. [When Does Online Adaptation Pay on the Edge? A Leakage-Free Evaluation of Warmup, Learning-Rate Selection, and Resource Trade-offs for Time-Series Forecasting](https://arxiv.org/abs/2609.01126)

**<font color=#1a73e8>作者：</font>** Takumi Fujimoto, Hiroaki Nishi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online adaptation can help edge time-series forecasting under distribution drift, but its measured benefit is sensitive to evaluation choices. We study six public multivariate streams, including building-sensor and smart-meter data, under a leakage-free streaming protocol. We identify two additional sources of comparison bias. First, the warmup budget of the static baseline has a two-sided effect: insufficient warmup undertrains the baseline, whereas excessive warmup can degrade its pre-drift generalization. Across six dataset-backbone settings, the estimated adaptation benefit changes by 3.0 to 18.8 percentage points (pp) over the 1,000-20,000-step warmup range. Second, comparing SGD with momentum (SGD+m) and Adam at a shared default learning rate conflates optimizer quality with rate sensitivity. We select both the warmup budget and each optimizer's online rate using a held-out pre-drift validation slice without accessing test data. Under this validation-only procedure, Adam outperforms SGD+m in 310 of 360 evaluated cells, while 4 Adam cells remain below the static baseline. We further characterize accuracy against adaptation-state memory and A100-measured per-update latency for full, head-only, and calibration-based adaptation. In the evaluated PatchTST frontier settings, several parameter-efficient variants are nondominated on the adaptation-state-memory axis. Smart-meter analyses also show that reported gains depend on meter-selection rules. These findings support a validation-only commissioning procedure, while target-device latency and energy remain to be measured. Code, data, and all reported numbers: this https URL.

---


### 174. [Scaled Idempotence in Transformer Attention: Paired OV Geometry and Shared-Value Algebras](https://arxiv.org/abs/2609.01129)

**<font color=#1a73e8>作者：</font>** Jiming Feng, Junliang Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We identify a recurrent algebraic regularity in Transformer attention: a sparse subset of effective OV operators $T=OV^\top$ nearly closes under composition, $T^2\approx\alpha T$. Across six pretrained endpoints spanning 2.8B--235B parameters, 3.98--8.00% of heads reach squared closure alignment $\mathcal{P}\geq0.9$, while no matched within-layer O/V mismatch does. An exact principal-coordinate factorization, $T=Q_OKQ_V^\top$ and $T^2=Q_O(KDK)Q_V^\top$, separates within-support transport from read--write return geometry. Across all 7,304 heads in nine MHA/GQA models, scrambling only the orientation of $K$ while preserving singular values, norms, factor spans, and principal angles reduces median closure from 0.336 to $1.04\times10^{-4}$; trained orientation wins for 98.64% of heads and in every layer. Constructive searches show that high closure is feasible in every surveyed layer, but usually not attained. Retrospective trajectories in three independently trained lineages further separate broadly available capacity from the orientations attained by final strong heads. Under exact value sharing, headwise closure extends to a right-action algebra, $T_iT_j=\alpha_jT_i$. Seven-model experiments verify the approximate law and reveal distinct oblique projections with a shared value-defined kernel. These results characterize scaled idempotence as a sparse trained orientation within broadly available geometric capacity and show how value sharing extends a headwise relation into a local operator algebra.

---


### 175. [Overfitting Mitigation via Singular Value Decomposition in Minimum Bayes Risk Decoding](https://arxiv.org/abs/2609.01135)

**<font color=#1a73e8>作者：</font>** Riza Setiawan Soetedjo, Yusuke Sakai, Hidetaka Kamigaito 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Minimum Bayes Risk (MBR) decoding enables high-quality text generation by selecting the hypothesis that maximizes a utility metric over sampled pseudo-references. However, it is highly susceptible to metric overfitting: it can irregularly inflate the chosen utility metric at the direct expense of other unoptimized evaluation metrics. To mitigate this, we introduce SVD-MBR, which frames the pairwise utility matrix as a noisy information signal. By computing a low-rank approximation via Singular Value Decomposition (SVD) and retaining only the top-$k$ components, we effectively decouple true consensus from metric noise. Experiments demonstrate that SVD-MBR successfully regularizes decoding, yielding substantial gains across a range of generalized metrics. Furthermore, we reveal that this denoising is metric-dependent: neural metrics encode a robust low-rank consensus ideal for SVD, whereas surface-level metrics struggle to separate signal from metric noise.

---


### 176. [Different Changes Require Different Reasoning: Change-Type-Specialized Experts for Robust Change Captioning](https://arxiv.org/abs/2609.01136)

**<font color=#1a73e8>作者：</font>** Jiyoung Park, InJae Oh, Jung Uk Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Change captioning is the task of generating natural language descriptions that explain the changes between a pair of images. Although different change types (e.g., color shifts, object additions) exhibit distinct visual cues and require specialized reasoning processes, existing methods often overlook these distinctions. To address this limitation, we propose Multi-Expert Diagnosis for Image Change (MEDIC), a novel framework that introduces change-type awareness by explicitly modeling change categories. MEDIC employs type-specialized memory experts that dynamically retrieve type-relevant visual patterns conditioned on the input. This design enables each expert to capture diverse variations within its change type while focusing on the most informative visual cues. By softly routing inputs across type-specialized experts and learning dedicated representations for each change category, MEDIC generates more precise and type-aware change descriptions. Extensive experiments demonstrate that the proposed MEDIC consistently outperforms existing methods across diverse and challenging datasets. The code is available at \href{this https URL}{GitHub}.

---


### 177. [StainPresetNet: Stain Preset Network for Fast Multi-to-Multi Stain Normalization](https://arxiv.org/abs/2609.01146)

**<font color=#1a73e8>作者：</font>** Hongtao Kang, Die Luo, Li Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stain normalization reduces color variations caused by variations in staining protocols and imaging conditions, thereby enhancing computer-aided diagnostic system performance. Traditional methods derive mapping relationships from individual or limited reference images through pixel-wise transformation, offering style flexibility but suffering from inaccurate color mapping extraction. While existing deep-learning-based approaches achieve accurate dataset-wide color mapping through complex neural networks, they face challenges including computational inefficiency, artifact generation, and fixed normalization directions requiring model retraining for directional changes. To address these limitations, we propose StainPresetNet - a novel framework that combines structural preservation with dataset-level color mapping while maintaining computational efficiency. Our method implements pixel-wise normalization guided by preset reference images, enabling multi-directional adaptability without retraining. Evaluations on cytopathology and histopathology datasets demonstrate that StainPresetNet achieves superior color mapping accuracy compared to conventional methods, effectively improves classifier generalization in diagnostic tasks, and reduces computational overhead by 90\% versus existing deep learning approaches. The proposed preset-guided mechanism facilitates flexible adjustment of normalization directions through simple reference image replacement, overcoming the directional rigidity of current deep-learning-based solutions.

---


### 178. [Subword Segmental BabyLMs: Learning to Tokenise for Sample-Efficient Pretraining](https://arxiv.org/abs/2609.01151)

**<font color=#1a73e8>作者：</font>** Francois Meyer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In the standard LM training pipeline, subword tokenisation is applied as a preprocessing step. Subword segmental language modelling is an alternative paradigm in which tokenisation is learned during training, allowing the model to discover subword units that optimise its training objective. In this paper, we present our submission to the 2026 BabyLM Challenge, for which we develop two new subword segmental LMs: SubSegGPT and SubSegDeBERTa. SubSegGPT is a decoder-only model that learns tokenisation during autoregressive pretraining. SubSegDeBERTa is an encoder-based model that jointly learns to generate and tokenise masked words. We train both for the Strict and Strict-small tracks. Our top submission to Strict is SubSegDeBERTa, which achieves notable gains in zero-shot evaluation. Our top submission to Strict-small is SubSegGPT, which outperforms tokenisation-based baselines. Our results show that learnable subword tokenisation can improve sample-efficiency for BabyLM pretraining. We analyse the subword learning dynamics of our models and find that tokenisation gradually converges on subword units that balance morphological alignment and fine-grained segmentation.

---


### 179. [Superposed Latent Autoencoder](https://arxiv.org/abs/2609.01158)

**<font color=#1a73e8>作者：</font>** Quanling Zhao, Jiaying Yang, Tianqi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoencoders typically meet tight latent-memory budgets by making each latent representation smaller, sacrificing representational capacity. We ask a different question: can multiple wider latents be stored together instead? We introduce the Superposed Latent Autoencoder (SLAE), which preserves high-capacity latent representations while sharing storage through learned superposition. SLAE transforms latents into storage-friendly codes, binds them with randomized keys, superposes multiple codes into a single memory tensor, and learns to recover each latent before decoding. Under the same storage budget, SLAE replaces irreversible dimensional bottlenecks with structured interference that can be suppressed. Across CIFAR-10/100, SVHN, STL-10, Tiny ImageNet, and a wide range of memory budgets, SLAE substantially improves the reconstruction--memory tradeoff, reducing reconstruction error by up to 56% over conventional autoencoders at matched storage. Further analysis shows that SLAE's advantage comes from making wider representations usable under the same storage budget. These gains also extend beyond reconstruction: the information preserved by SLAE improves downstream classification by up to 16.79 percentage points under the same memory budget. Our results suggest a new principle for representation compression: instead of making every latent smaller, keep representations wide and let them share memory.

---


### 180. [Johnny Still Receives Spam SMS: Assessing the Robustness of SMS Spam Detection](https://arxiv.org/abs/2609.01171)

**<font color=#1a73e8>作者：</font>** Muhammad Salman, Muhammad Islam, Muhammad Ikram 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> SMS spam detection systems often achieve high accuracy in controlled environments but struggle against adversarial attacks and increasingly sophisticated spam tactics in real-world deployments. In this paper, we evaluate the robustness of SMS anti-spam systems that end users actually rely on, including commercial messaging applications, third-party anti-spam services, and publicly available open-weight models hosted on Hugging Face. We evaluate these systems under both standard and adversarial conditions, considering perceptible and state-of-the-art imperceptible attacks. We include only perturbations that we verify survive real SMS or RCS delivery, rather than lab-only artifacts. Our experiments reveal significant gaps in existing spam detectors' ability to identify adversarially manipulated messages. We further demonstrate that adversarial training alone is insufficient. Using an explicit held-out evaluation protocol, we find that robustness transfers well within a perturbation family but degrades sharply against structurally distinct, encoding-level attacks. To address these weaknesses, we propose a multi-model ensemble that combines adversarial training with spam classifiers diverse in architecture and tokenization. Our results show that this ensemble, particularly when using a minority-voting strategy, substantially improves robustness against both perceptible and imperceptible adversarial attacks while maintaining competitive classification accuracy. We also characterize the resulting precision-recall trade-off and recommend operating points for false-positive-sensitive and recall-critical deployments. These findings highlight the need for comprehensive robustness evaluations and ensemble-based defenses for building more secure SMS spam detection systems in real-world settings.

---


### 181. [Monocular Depth Estimation from a Single Image: Progress and Opportunities](https://arxiv.org/abs/2609.01172)

**<font color=#1a73e8>作者：</font>** Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation has long stood as a fundamental challenge in computer vision, enabling a wide range of applications including 3D reconstruction, robotics, autonomous driving, and augmented reality. This survey traces the field's evolution from early learning-based methods to the emergence of transformative foundation models. We begin by framing the problem, distinguishing between relative and metric depth estimation, and highlighting the key challenges that have shaped a decade of research. We then present common problem formulations and introduce the most widely used datasets, covering indoor, outdoor, and synthetic data. Following this, we review major advances prior to the foundation model era, distilling core insights from influential methods that contributed to improvements in accuracy, efficiency, and robustness. The survey then turns to the recent surge of foundation-model-based approaches, categorizing them into discriminative and generative paradigms and emphasizing the critical roles of large-scale pretraining (e.g., DINOv3) and synthetic data. We compare representative models using both quantitative benchmarks and qualitative examples, and discuss natural extensions to video-based depth estimation. Further, to illustrate real-world impact, we highlight the integration of depth estimation into applications such as visual SLAM, content generation, and robot perception. Finally, we outline open challenges and promising research directions as the field advances further into the era of foundation models.

---


### 182. [Smart Contracts Claimed Vulnerable by the CVE Database, with Labels and Source Locations](https://arxiv.org/abs/2609.01186)

**<font color=#1a73e8>作者：</font>** Monika di Angelo, Gernot Salzer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Common Vulnerabilities and Exposures (CVE) database catalogs vulnerability claims in hard- and software, among them those pertaining to blockchain programs a.k.a. smart contracts. We present CVE-Smart-Contracts, a curated dataset of CVE records up to July 2026 referring to Ethereum smart contracts. The dataset contains the vulnerable artifacts (source code and runtime bytecode), labels according to three taxonomies, and function-level locations. The retrieval of CVE records, collection of additional evidence, validation of the correspondence between records and artifacts, label assignment, and vulnerability localization are automated, leaving 15% to manual analysis. The dataset does not validate the original vulnerability claims, but marks a few records obviously wrong as `refuted'. For the sake of reproducibility, all external inputs are retained, so that rerunning the pipelines results in the same outputs. The dataset comprises 491 records linked to deployed contracts, 26 referring to projects (mostly libraries), 45 without validated artifacts, and six records with refuted claims. The dataset supports empirical security research, in particular the evaluation of code analysis and repair techniques.

---


### 183. [Identification of Compositional Risks in Data Protection Impact Assessments and Beyond](https://arxiv.org/abs/2609.01201)

**<font color=#1a73e8>作者：</font>** Henrik Graßhoff, Meiko Jensen, Malte Hansen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When personal data is processed in a distributed manner by cooperating service providers, privacy risks may emerge solely from the choice of data processors included in the composition. For instance, different data processors may unknowingly rely on the same cloud provider, allowing for unintended linkability of personal data at that very provider. As such compositional risks to privacy are beyond the scope of each individual risk assessment, they are likely to be overseen when performing a data protection impact assessment. In this paper, we propose a novel protocol to detect and manage such compositional risks to privacy. Following an initial problem definition and requirements elicitation, we elaborate how our protocol identifies candidates for compositional risks and how this information may be used to improve the results of a data protection impact assessment over service compositions including multiple data processors.

---


### 184. [Towards AI-Assisted Clinical Trial Matching: Practical Considerations, Multicenter Evaluation, and Real-World Deployment](https://arxiv.org/abs/2609.01202)

**<font color=#1a73e8>作者：</font>** Yin Fang, Qiao Jin, Shubo Tian 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical trials are essential for advancing cancer care and drug development, but many fail because of insufficient patient enrollment. While there is growing interest in using AI to support patient recruitment, existing systems largely perform eligibility assessment alone and have rarely been evaluated in real-world oncology workflows. Here we present TrialGPT 2.0, an AI-assisted clinical trial recommendation system designed for real-world deployment. Rather than asking only whether a patient may qualify, the system also assesses which trials warrant further consideration given the patient's current clinical needs and local workflow priorities, and provides structured, inspectable explanations for expert review. Importantly, we evaluated TrialGPT 2.0 retrospectively and prospectively across multiple oncology-focused settings, spanning government, academic cancer-center, patient-advocacy, and NIH referral workflows. In retrospective multicenter cohorts comprising 288 cases, TrialGPT 2.0 retrieved at least one clinician-recommended trial in its top 10 recommendations for approximately 91% of cases while reducing clinician screening time by 55.0%. In a six-month prospective evaluation embedded in an active precision oncology tumor board, TrialGPT 2.0 contributed additional trial opportunities missed by the routine workflow, expanding patient access to clinical trial participation by 90.9%. To support scientific reproducibility, we also introduce NIH-TrialBench, a clinician-authored dataset comprising 126 diverse synthetic patient vignettes and matching scenarios from 11 NIH Institutes and Centers. Together, these results support the value of AI to assist clinical trial matching by improving clinician efficiency and identifying frequently overlooked trial opportunities, ultimately helping to expand and accelerate accrual to cancer trials.

---


### 185. [Recent Developments in Transformer Inference Deployment on FPGA Platforms: A Survey](https://arxiv.org/abs/2609.01212)

**<font color=#1a73e8>作者：</font>** Arjan Blankestijn, Uraz Odyurt, Amirreza Yousefzadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the rapid and continuous growth in the incorporation of machine learning models based on the Transformer architecture, capable deployment is in high demand. In this context, capable deployment refers to operational performance aspects, e.g., throughput and latency, as well as efficiency aspects, e.g., energy consumption. When it comes to the task of inference using such models, purpose-built hardware accelerators provide a lucrative alternative to common deployment choices, such as Central Processing Units (CPUs) and Graphics Processing Units (GPUs). The Field Programmable Gate Array (FPGA) platforms category is an example of such alternative accelerators, promising implementation flexibility, energy efficiency, improved latency and suitability for on-site deployment. We investigate the most recent advances, trends, and design choices for Transformer inference on FPGA platforms. We perform a systematic literature review, extracting and delving into preferred techniques for implementation and optimisation. This study and the provided taxonomy of topics could act as a guide for researchers from the academia and industry alike.

---


### 186. [Multi-Head Self Attention is a Parameter Identification Mechanism](https://arxiv.org/abs/2609.01231)

**<font color=#1a73e8>作者：</font>** W. Ross Morrow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove that a multi-head scaled dot product attention can be viewed as a parameter identification strategy. The ratio of unidentified parameters to the total number of parameters scales like the reciprocal of the number of heads ($1/2 \to 1/(2H)$), meaning models with more heads are structurally more identified. A subtle side effect of the mathematics observation that attention can never be fully identified. Similarly we also show that some bias terms can have no effect on softmax-based attention layers in both the single- and multiple-head settings, though this is mostly a curiosity that should have a marginal effect on model size and model training/prediction efficiency. We also touch on modern improvements to transformers including RoPE and GQA from this perspective, illustrating how those as well can improve the ratio of ``meaningful'' parameters to all parameters. Simple numerical examples demonstrate that training can indeed involve updates that overlap model-invariant subspaces that arise from a lack of identification. As part of our experiments we use a ``rebalancing'' approach that can ``fix'' updates that overlap unindentified subspaces but do not try to present evidence this should actually be adopted. Instead we simply view our numerical results as exploring and confirming the theoretical results. As a whole we discuss a purely mathematical/statistical explanation, identification, for why specific architectural choices in transformers may have improved performance.

---


### 187. [Position Matters: Feature Inversion Attacks in ViT Split Inference with Token Reduction and Shuffling](https://arxiv.org/abs/2609.01232)

**<font color=#1a73e8>作者：</font>** Stefano Leggio, Giulio Rossolini, Alessandro Biondi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) are increasingly used in split-inference systems, where edge devices transmit intermediate token representations to a remote cloud. In this setting, token reduction lowers computation and communication costs, while token shuffling disrupts the spatial organization of the transmitted tokens, potentially limiting information leakage. However, their privacy benefits remain unclear against feature inversion attacks, which attempt to reconstruct the input from the transmitted embeddings. In this work, we show that, despite disrupting the spatial structure required by conventional reconstruction attacks, transmitted token embeddings retain substantial positional information. Based on this observation, we introduce the Spatially Aligned Reconstruction Attack (SARA), a unified pipeline that predicts token positions, restores their spatial layout, reconstructs missing embeddings using a feature-space masked autoencoder, and recovers the input image. Our results demonstrate that token shuffling provides only apparent privacy, as SARA largely reconstructs the original token organization. Token reduction offers stronger protection, but significant leakage persists when the retained tokens preserve sufficient semantic and positional information. Finally, we introduce a lightweight edge-side defense that removes positional embeddings and progressively adapts the edge-side transformer blocks through knowledge distillation. It substantially reduces attack performance against SARA, while preserving downstream task accuracy and requiring no changes to the cloud-side model.

---


### 188. [One Prompt Is Enough: Watermark Laundering Through Foundation Image Models](https://arxiv.org/abs/2609.01249)

**<font color=#1a73e8>作者：</font>** Jidong Yang, Qi Li, Wei Zong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Invisible watermarks are typically evaluated against predefined perturbations such as compression, blur, noise, cropping, and denoising. Public foundation image models expose a distinct threat: an attacker can submit a watermarked image with a single reconstruction prompt and obtain a visually faithful output from which the invisible watermark can no longer be decoded reliably. We formalize this failure mode as watermark laundering and evaluate it using a joint payload-fidelity profile that combines bit error rate (BER) with visual and semantic preservation. Across six OpenAI and Google image editing models, three representative watermarking schemes, and 1,800 reconstructed outputs, we identify two complementary laundering regimes: OpenAI models produce the strongest payload disruption across the evaluated schemes, whereas Nano Banana 2 shows that DwtDct remains vulnerable under high-fidelity reconstruction. Prompt ablations show that no single removal-oriented instruction is necessary for payload disruption, indicating that the effect is primarily induced by the reconstruction pathway rather than by explicit attack wording. Comparisons with conventional attacks further show that prompt-conditioned reconstruction constitutes a distinct operational attack interface. These findings motivate foundation-model reconstruction as a missing robustness condition in invisible watermark evaluation.

---


### 189. [MeRoPE: Metric Rotary Position Embedding for Camera-Controlled Video Generation](https://arxiv.org/abs/2609.01252)

**<font color=#1a73e8>作者：</font>** Zhijian Qiao, Xinjiang Wang, Jiajie Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In camera-controlled video generation, geometry-aware positional encodings condition tokens on camera extrinsics and per-token viewing rays. Existing schemes, however, have a scale-dependent failure mode on real-world metric camera trajectories: homogeneous projective encodings cause attention logits and feature norms to grow unbounded with physical translation baselines. We propose MeRoPE (Metric Rotary Position Embedding), a norm-preserving relative camera encoding for attention. MeRoPE encodes relative orientations between calibrated viewing rays with orthogonal rotation blocks, maps raw metric displacements into multi-frequency rotary phases, and adds a disparity-anchored correspondence prior along the epipolar arc. This design strictly preserves feature norms, bounds pre-softmax attention logits regardless of the physical translation scale, and maintains exact invariance to global rigid coordinate changes. Across nuScenes and PanShot, which cover large-baseline trajectories and diverse camera optics, respectively, MeRoPE achieves stronger camera control than prior encodings, with the best consistency between generated camera motion and conditioning poses in both rotation and translation. Code will be made publicly available.

---


### 190. [Dual Process Motion Planning](https://arxiv.org/abs/2609.01260)

**<font color=#1a73e8>作者：</font>** Jiayi Yan, Francesco Fabiano, Alessandro Abate  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robotic systems are deeply embedded in both industry and everyday life, where they are expected to act with speed, precision, and reliability. Classical control and planning methods have long delivered strong guarantees, but often at the cost of computational efficiency and adaptability. More recently, learning-based approaches have shown promise in overcoming these limitations, enabling agents to leverage experience to accelerate decision-making and address previously intractable problems. In this work, we bridge these two approaches through a neuro-symbolic perspective on nonlinear motion planning. Inspired by the Thinking Fast and Slow paradigm, we introduce a dual-process architecture that combines the strengths of robust reasoning and learning. Our framework integrates state-of-the-art symbolic solvers as a ``System-2'' component with experience-driven ``System-1'' modules. A metacognitive controller dynamically orchestrates their interaction, selecting when to rely on fast intuition versus slower, more precise reasoning. By evaluating the framework across diverse nonlinear benchmark environments, we demonstrate that this architecture yields consistent gains in planning efficiency, accuracy, and generalization, while promoting reuse across tasks. The results suggest that tightly coupling learning with structured reasoning offers a scalable path toward more capable and adaptive robotic systems.

---


### 191. [Solving In-Table Prediction Problems by Deep Neural Networks with Performance Evaluation Using Synthetic Data](https://arxiv.org/abs/2609.01262)

**<font color=#1a73e8>作者：</font>** Xiao Zhao, Daniela Oelke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular deep learning (TDL) leverages neural networks (NN) to extract patterns from tabular data. Traditional TDL methods follow a supervised learning paradigm, where a target feature is explicitly given. In this work, however, we explore a different approach by employing deep NNs to learn relationships among individual columns within a given table. We investigate whether NNs can predict the values of arbitrarily selected columns in a given table based on the remaining known columns. We call this problem In-Table Prediction (ITB), which is slightly different from table imputation methods and the pretraining task of TDL. Three potential usage scenarios are identified, which, to our best knowledge, have not been extensively studied in the literature. A self-supervised learning approach is applied to address this problem by randomly selecting columns to be masked out and used as learning targets. This work focuses on tabular datasets containing only continuous features. To handle missing values in continuous features, a novel neural layer is proposed to embed both numerical and empty values. Synthetic data is generated based on predefined column relationships, with empty values inserted using two distinct mechanisms. Additionally, an adapted masking strategy is employed to create test data. Performances of three NN architectures, namely MLP, Resnet and Transformer, are evaluated using the generated synthetic data. We conclude that, the attention-based structure outperforms the other two networks, when a sufficiently large number of training examples is available and a relatively large embedding length is chosen. We stress that these findings are obtained under controlled, synthetic conditions with a small number of columns and it should therefore be regarded as an initial, narrowly-scoped investigation rather than a general characterization of ITP on real-world tabular data.

---


### 192. [Position: Privacy Is a Claim, Not a Property of Synthetic Data](https://arxiv.org/abs/2609.01273)

**<font color=#1a73e8>作者：</font>** Jiachen Zhao, Antonia Januszewicz, Taeho Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic data has become a common component of machine learning research. While widely adopted, its use in privacy-sensitive contexts has quietly shifted from a claim of residual inference risk under stated assumptions to an appearance-based property inferred from data generation itself. In this position paper, we argue that this shift reflects an implicit change in community standards for what counts as sufficient privacy evidence, rather than a misunderstanding of well-established privacy principles. Drawing on an empirical analysis of recent publications across major ML venues, we show that synthetic data is frequently used in privacy-sensitive settings without explicit articulation of threat models, inference risks, or falsifiable privacy claims. As a result, privacy assurance often remains implicit, difficult to verify, and unevenly distributed, with heightened exposure for rare and minority records. We argue for treating privacy as an explicit, evidence-based scientific claim and recommend that ML venues adopt norms requiring privacy-relevant assertions to be clearly scoped, testable, and contestable.

---


### 193. [Seeing the World and the Self from Egocentric Video](https://arxiv.org/abs/2609.01276)

**<font color=#1a73e8>作者：</font>** Kai Guan, Minchao Jiang, Ruichen WangLi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Complete 3D perception from egocentric video requires recovering the surrounding scene and the wearer's full-body motion in a shared metric frame. Existing methods typically address scene reconstruction and motion estimation separately: scene reconstruction methods ignore the wearer, whereas motion estimation methods lack explicit scene geometry and often depend on external trajectories. Joint recovery is challenging because the two tasks exhibit asymmetric visibility and require different prediction paradigms. The largely visible scene supports deterministic geometric regression, whereas the severely occluded body requires generative motion inference. We therefore propose RESELF (REconstructing the Scene and the sELF), a unified framework that couples deterministic metric geometry reconstruction with geometry-conditioned motion generation. RESELF adapts a geometry foundation model pre-trained on large-scale exocentric data to egocentric video using frame-wise scale and relative-pose consistency objectives. The resulting camera trajectory and latent geometric features condition a diffusion model that recovers the wearer's motion. A subsequent closed-loop kinematic feedback stage further refines the camera head while preserving the reconstructed scene geometry. To support training and evaluation, we curate EE4D-JSM from EgoExo4D by aligning egocentric video, sparse metric scene geometry, camera trajectories, and full-body motion annotations. Experiments show that RESELF outperforms state-of-the-art methods designed for the individual tasks across depth estimation, camera tracking, and full-body motion estimation. Code, models, and datasets will be available at this https URL.

---


### 194. [TimeSteer: Inference-Time Speech Scheduling in Joint Audio-Visual Diffusion Models](https://arxiv.org/abs/2609.01277)

**<font color=#1a73e8>作者：</font>** Chao Zhou, Yiling Chen, Qi Chu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although pretrained joint audio-visual diffusion models offer rich control over \emph{what} to generate, they provide no explicit control over \emph{when} an utterance should occur. To address this, we study \emph{inference-time speech scheduling}, a novel task that places coupled speech and visual articulation within user-specified begin--end intervals without finetuning the backbone model. We uncover two intrinsic properties of the denoising process that enable this task. First, a timing-sensitive text-to-audio cross-attention head exposes each utterance's model-implied source span along the latent timeline. Second, the predicted clean latent already organizes coupled speech and visual articulation, allowing their temporal placement to be edited without regenerating the content. Building on these discoveries, we propose \textbf{TimeSteer}, a training-free framework that localizes each utterance's source span through \textbf{Source Span Localization} and transfers the associated audio-visual latent content from the source interval to the specified target interval through \textbf{Region-Aware Latent Remapping}. We further introduce \textbf{SpeechShift}, the first benchmark for interval-level speech scheduling in joint audio-visual generation. Experiments across two representative backbones show that TimeSteer substantially improves interval controllability over training-free baselines while maintaining competitive overall generation quality.

---


### 195. [HiLRP: Toward One Trustworthy Explanation for Vision Transformer: Conservation-Valid Attribution via Attention Primitives](https://arxiv.org/abs/2609.01282)

**<font color=#1a73e8>作者：</font>** Sathiyamohan Nishankar, Pubudu Sanjeewani, Asanka Perera 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformer (ViT) design has become increasingly diverse, with backbones combining convolutional stems, windowed, linear, or multi-axis attention, patch merging, and spatial reduction in various configurations. This diversity poses challenges for existing attribution methods, whose assumptions often do not hold across ViT variants: Grad-CAM requires a terminal spatial feature map, attention rollout assumes global softmax attention, and layer-wise relevance propagation (LRP) requires module-specific rules. To the best of our knowledge, no existing method provides a unified attribution framework across this architectural space. We show that this architectural diversity can be captured by a simpler underlying structure. The attention and resolution-reduction operators in current ViTs can be decomposed into four operation types: linear maps, bilinear mixing, normalization or gating, and reindexing. Each operation admits a relevance rule that satisfies conservation. Based on these rules, HiLRP supports new backbones by construction rather than by architecture-specific derivation, and its attribution maps decompose the prediction rather than relying on heuristic assumptions. We prove conservation and conditional equivariance and verify both to machine precision. Across 14 attribution methods and 10 architectures, we find that no prior method remains reliable across ViT families, while Faithfulness Correlation becomes uninformative for backbones robust to spatial masking. HiLRP alone preserves conservation across windowed, spatial-reduction, multi-axis, and linear-attention models, where naive extensions can produce zero or inflated relevance. It also localizes attribution failures in class activation mapping, achieving 0.97 Pointing compared with 0.55 for competing methods on EfficientViT.

---


### 196. [One-Layer Transformer Provably Learns Multiclass One-Nearest Neighbor in Context](https://arxiv.org/abs/2609.01311)

**<font color=#1a73e8>作者：</font>** Skanda Athreya, Yutong Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We extend recent work establishing an equivalence between one-layer transformers and nearest-neighbor classifiers in the binary setting to the multiclass case. By leveraging the simplex encoding, we show that one-layer transformers with an argmax classification head behave identically to a one-nearest-neighbor classifier in the multiclass setting. This closes a gap left by prior work, whose multiclass result relied on a non-standard rounding-based approach rather than the typical argmax head used in practice.

---


### 197. [Exploring Sparse Autoencoders in Text-Based Causal Confounding Adjustment](https://arxiv.org/abs/2609.01322)

**<font color=#1a73e8>作者：</font>** Mian Zhong, Katherine A. Keith, Anjalie Field  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In many settings, studying causal questions based on text data requires adjusting for confounding information within texts. Yet there is a tradeoff in constructing text representations for adjustment: they must be sufficiently large and/or dense to preserve the confounding variables necessary for unbiased effect estimation, but sufficiently small and/or sparse to satisfy finite-sample overlap and yield low-variance estimates. To address this tradeoff, we turn to sparse autoencoders (SAEs), and propose a novel causal adjustment pipeline that iteratively selects a minimal set of SAE features via conditional independence tests. We find that SAE representations achieve better adjustments (lower bias and and higher coverage) than alternative representations in standard semi-synthetic evaluations with binary confounders, and their interpretability offers opportunities for falsification. We also introduce a more realistic semi-synthetic evaluation that uses multi-label data as the unobserved confounders and find off-the-shelf adjustment methods require increased investigation for these more complex settings. Code: this https URL

---


### 198. [VerTox: Verifiable Reward-Guided Corpus Poisoning Against Neural Ranking Models](https://arxiv.org/abs/2609.01325)

**<font color=#1a73e8>作者：</font>** Zhiqi Huang, Vivek Datla, Zhichao Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural ranking models have become core components of modern information retrieval systems and important building blocks of AI systems such as retrieval-augmented generation (RAG) pipelines. However, their robustness remains insufficiently understood in the presence of large language models (LLMs), which can generate fluent and deceptive content at scale. This work investigates the vulnerability of neural ranking models to corpus poisoning attacks, in which an adversary injects a small number of maliciously crafted documents into the corpus to distort ranking behavior. We propose VerTox, the first framework to formulate corpus poisoning as a verifiable reward-guided reinforcement learning (RLVR) problem. By explicitly coupling ranking distortion with factual corruption through specialized reward shaping, we fine-tune compact LLMs into adversarial generators. Experiments demonstrate that our method achieves near-perfect attack success rates, producing adversarial documents that frequently rank higher than target documents across major neural ranking architectures, as well as a proprietary commercial embedding model. The generated adversarial documents are fluent and exhibit low perplexity, making them difficult to detect. Furthermore, by explicitly encouraging factual corruption, our adversarial documents significantly degrade the performance of a downstream RAG application.

---


### 199. [Hidden Services Protocol for Mixnets](https://arxiv.org/abs/2609.01326)

**<font color=#1a73e8>作者：</font>** Nicolas Constantinides, Mahdi Rahimi, Stavros Nonis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mix networks (mixnets) provide network-level privacy by routing each communication packet through a sequence of intermediaries, called mixnodes, that randomly delay and cryptographically transform packets before forwarding them, making it difficult for observers to link mixnet entries to exits. While this mechanism protects sender privacy from both external adversaries and the receiver, existing mixnets lack a secure and practical protocol that simultaneously protects receiver (destination) privacy, particularly from the sender. We close this gap.
We introduce the first practical and secure hidden-service protocol for mixnets, providing receiver privacy alongside sender anonymity. Our design builds on Single-Use Reply Blocks (SURBs), which enable anonymous replies without revealing the receiver's address. We show, however, that existing approaches to using SURBs expose two practical attacks that can compromise sender or receiver anonymity when the opposing party controls only a single mixnode. We develop defenses against both vulnerabilities.
Building on these defenses, we introduce NymHS, a secure and practical hidden-service protocol for mixnets that supports anonymous service discovery, authenticated bidirectional sessions, and asynchronous SURB replenishment. We implement NymHS on the open-source Nym codebase and evaluate its practicality through web-browsing experiments across 118 websites, measuring each of the 27 configurations three times (9,558 page loads). Our results demonstrate that hidden services can be deployed efficiently over mixnets. In particular, increasing the Sphinx payload from 2 KiB to 10 KiB reduces mean page-load latency by approximately 5.2x and decreases communication overhead from 21.7% to 4.3% relative to the current Nym baseline.

---


### 200. [Where the Verifier Fails: A Category-Level Audit of Reward Signals in RLVR](https://arxiv.org/abs/2609.01354)

**<font color=#1a73e8>作者：</font>** Esther Xin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) and standard benchmark evaluation both rely on an automatic verifier that turns a free text answer into a binary reward. Prior work reports that one evaluation harness accepts only about 94% of its own ground truth answers, blaming LaTeX parsing. That is an aggregate: it does not say which answer forms consume the error budget. We supply the decomposition. We apply metamorphic testing to the verifier rather than the model, generating certified equivalent answer variants, that is, rewrites that preserve mathematical meaning by construction, so that any rejection is a provable false negative needing no human adjudication. We then measure rejection per answer category across four widely used verifiers over 307,420 verdicts. We find three things. (1) Self validation ranges from 53.8% to 95.2% on identical inputs, a spread of 41.3 points. The published figure describes one implementation, not the task; two configurations of the same library disagree on 49.9% of pairs. (2) The residual is not spread across parsing categories but concentrated in whitespace and punctuation, which account for 93.0% of in contract failures for the default LaTeX configuration. A trailing period or newline dominates the budget. (3) Separating rejection from execution failure shows that verifiers with similar aggregate error fail for opposite reasons, and that a reference numeric cascade accepts off by one wrong answers as a step function of magnitude, from 0% below 10^4 to 100% at or above, because its relative tolerance is scale invariant.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-236](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
