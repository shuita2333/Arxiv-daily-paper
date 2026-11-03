# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

---

### 351. [Uncertainty-Aware 3D Position Reconstruction in CZT Drift-Strip Detectors](https://arxiv.org/abs/2611.02027)

**<font color=#1a73e8>作者：</font>** Alejandro Valverde Mahou, Michał Kossakowski, Selina R. H. Owe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate three-dimensional interaction-position reconstruction is important for CZT drift-strip detectors, but conventional methods can suffer from degraded performance in challenging detector regions, while learned models provide limited information about prediction reliability. We investigate two uncertainty-aware approaches: deep ensembles of point-estimation networks and simulation-based inference (SBI), which estimates a posterior distribution over interaction position. Both approaches are trained on physics-based simulations and evaluated on both synthetic and experimental data. On synthetic data, uncertainty from both methods correlates with positioning error, with SBI showing a substantially stronger relationship. On experimental measurements, the deep ensemble achieves improved $z$-position resolution, while SBI provides more informative uncertainty estimates that highlight regions of reduced positional information and discrepancies between simulation and the physical detector. These results demonstrate the complementary strengths of ensemble-based reconstruction and posterior inference for uncertainty-aware detector position reconstruction.

---


### 352. [4D Triangle Splatting Reconstruction of Dynamic Endoscopic Scenes from Monocular Videos](https://arxiv.org/abs/2611.02034)

**<font color=#1a73e8>作者：</font>** Laura Salort-Benejam, Stamatia Giannarou, Antonio Agudo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust 4D reconstruction of deformable endoscopic scenes from monocular videos remains challenging due to non-rigid tissue deformation, illumination changes, occlusions, and unknown camera trajectories. Reliable dynamic reconstruction of endoscopies could significantly enhance visualization, diagnostic accuracy and intraoperative guidance of minimally invasive procedures. We propose SurgicalTS, a self-supervised triangle-splatting framework for dynamic endoscopic scene reconstruction from static monocular cameras. The scene is represented by a canonical set of triangles jointly optimized with a deformation network. We introduce a quaternion-based deformation model, an improved color parametrization, spatio-temporal priors, and a redefined initialization strategy that improves completeness under occlusions. Extensive evaluation on challenging in-vivo endoscopy videos from diverse procedures shows that SurgicalTS successfully models soft-tissue deformations and tool-tissue interactions over time, while consistently outperforming state-of-the-art methods. Our method also reduces training times while maintaining competitive geometric and photometric accuracy results, highlighting the effectiveness of quaternion-based deformation modelling with physical consistency for robust and efficient 4D reconstruction of endoscopic scenes.

---


### 353. [Unified Loss-Aware Density Control for 3D Gaussian Splatting](https://arxiv.org/abs/2611.02044)

**<font color=#1a73e8>作者：</font>** Tae-Young Kim, Jiwoo Chung, Jae-Pil Heo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The efficiency and fidelity of 3D Gaussian Splatting critically depend on adaptive density control, which grows and suppresses Gaussian primitives throughout optimization. However, the standard pipeline still relies on heuristic view-space gradients, scale thresholds, and global opacity resets, rather than explicitly assessing the loss-reducing effect of each split, clone, or opacity update. This mismatch can allocate primitives to already-sufficient regions, miss under-reconstructed structures, and destabilize training through blanket opacity changes. In this work, we recast adaptive density control as a collection of local loss-reduction decisions. We derive efficient Taylor-based per-Gaussian surrogates that predict the objective change caused by three primitive-level operations: splitting, cloning, and opacity decay. This yields a unified loss-aware framework with three components. First, we extend second-order splitting to a normalized joint position-scale space, enabling children to adapt not only their locations but also their anisotropic extents. Second, we formulate duplicate cloning as a surrogate minimization problem, selecting only Gaussians whose duplicated contribution is predicted to improve reconstruction and assigning each child a principled opacity. Third, we replace global opacity reset with selective soft opacity decay that weakens harmful primitives while preserving useful ones. Across standard 3DGS benchmarks, our method produces more targeted primitive allocation and achieves improved rendering quality with comparable or smaller Gaussian budgets compared to baselines.

---


### 354. [METER: Matched-Event Calibration for Short-Event EEG Microstate Transition Analysis](https://arxiv.org/abs/2611.02045)

**<font color=#1a73e8>作者：</font>** Abdul Basit, Eklavya Tomar, Muhammad Shafique  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Short cognitive events contain unequal and often sparse transition evidence, so raw EEG microstate distances can reflect finite sampling rather than neural reconfiguration. We introduce METER (Matched-Event Transition Estimation against a Reference), a participant-relative framework that separates marginal occupancy from conditional next-state choice and evaluates each event against duration-conditioned events from a fixed participant-specific reference bank. METER-Jump integrates uncertainty in sparse target and reference transition tables, returning a randomized event rank for testing and a continuous standardized coordinate for association analysis. Using a reproducible three-state representation selected by spatial criteria, we evaluated METER with participant-fitted simulations, estimator ablations, map perturbations, and preprocessing sensitivities. Event-level false-positive rates were 0.044-0.056 across four heterogeneous null mechanisms. By contrast, global cutoffs learned under the participant-fitted null and transferred unchanged to other regimes produced false-positive rates from 0.004 under rare transitions to 0.234 under map perturbation; duration-conditioned ranks remained near 0.05. Detection probability was approximately 0.69 with fixed maps but fell to 0.22 after bootstrap-derived map-assignment perturbation. In 4,175 natural-reading events from 18 participants, no linguistic association survived multiplicity correction in the primary 30-ms analysis, although a 20-ms sensitivity changed one within-stream max-$T$ decision. METER therefore calibrates finite-event departures conditional on a defined microstate sequence, while map assignment, filtering, temporal smoothing, and reference construction remain separate sources of measurement uncertainty.

---


### 355. [Beliefs in feedback: Factored representations of interacting agents in transformers](https://arxiv.org/abs/2611.02047)

**<font color=#1a73e8>作者：</font>** David A. Ehrlich, Manuel Baltieri, Fernando E. Rosas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex systems, from ecosystems to brains, are usually modeled as modular components coupled through feedback rather than as indivisible wholes. Can a transformer trained on the joint behavior of a group of interacting agents be understood in the same way? In this work, we develop a computational-mechanics framework to study agents interacting in feedback loops. We formally prove that any joint stochastic process can be presented as resulting from the behavior of agents interacting in feedback, and the resulting process is generated by a hidden Markov model whose Bayesian beliefs factorize into separate components per agent. Furthermore, our experiments show that transformers trained on such feedback sequences make use of this separability, disentangling the beliefs about the underlying factors into separate subspaces of their residual stream. This representation is found to scale linearly (instead of exponentially) with the number of agents. Moreover, interventions show that these representations are causally efficacious, allowing for targeted steering of individual agents' beliefs by selectively inserting counterfactuals. However, coarse-graining the behavior is found to disrupt the factorization, and can force a higher-dimensional representation. Together, the results establish both the dimensional advantage of a factorized representation and the ability of transformers to exploit it, laying the groundwork for investigating traces of compositional predictive architecture in pretrained models.

---


### 356. [UniGS-SLAM: Monocular Gaussian SLAM with Enhanced Geometry and Open-Vocabulary Semantics](https://arxiv.org/abs/2611.02051)

**<font color=#1a73e8>作者：</font>** Xingyuan Ding, Sicheng Yu, Kaiyong Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular semantic SLAM aims to reconstruct scene geometry and build semantic maps from RGB observations. Existing Gaussian-based methods often attach semantic labels or features to evolving Gaussian primitives, making semantic fusion difficult to maintain and increasing reconstruction overhead. Hybrid Gaussian--voxel representations provide more stable semantic support, but often rely on RGB-D input or known poses and do not revise historical semantic evidence after geometry updates. We present UniGS-SLAM, an RGB-only framework that decouples open-vocabulary semantics from Gaussian reconstruction while preserving bidirectional interaction. Foundation priors enhance monocular depth and pose estimation, while semantic observations are fused into an independent sparse voxel map with observation provenance, enabling historical contributions to be revised as reconstruction evolves. The fused semantics further guide Gaussian filtering and local surface refinement. Experiments on Replica, ScanNet, and KITTI-360 show leading tracking, rendering, and geometric reconstruction performance among representative RGB-only methods, together with strong open-set semantic mapping on Replica and ScanNet. We also achieve a 2.37-fold reconstruction speedup over the fastest compared semantic SLAM baseline. Project page: this https URL.

---


### 357. [Large Geometry Models Are Priors For Fast Physics Pretraining](https://arxiv.org/abs/2611.02066)

**<font color=#1a73e8>作者：</font>** Maggie Chlon, Leon Chlon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language and vision models became data-efficient by pretraining on plentiful unlabelled data; physical field models have such data, over ten million 3D shapes, but geometry pretraining designs its targets rather than deriving them from the physics. Euler-Lagrange geometry pretraining derives them: for attached flow, a shape enters the flow's Euler-Lagrange equation only through coefficients that distance and normal line (the normal up to sign) fix to first order. Their reconstruction error therefore bounds what a representation loses about any field, and fine-tuning on costly simulations need only assemble the global field. We realise it in AREALS, a masked surface autoencoder whose areal tokens carry position, normal and area, pretrained self-supervised and sign-free on 61,822 raw meshes. Because the operating condition enters only through the far field, sensors can supply it: AREALS completes a hidden field in one forward pass without condition labels. It matches the accuracy of the same architecture trained from scratch with half the simulations on DrivAerML and DrivAerNet++ and about a quarter on WindsorML. On DoubleDelta wings, 20 sensors give $3.9\times$ and $4.0\times$ lower field and force error than GABI, a Bayesian inversion method with a learned prior, and beyond the training angles pretraining halves the error.

---


### 358. [The Vibe Paradox: What EEG Reveals About Your Brain When Vibe Coding](https://arxiv.org/abs/2611.02087)

**<font color=#1a73e8>作者：</font>** Olivia Schutz, Rudrajit Choudhuri, Yunhan Qiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Background: Much of the enthusiasm for vibe coding rests on two intuitive beliefs: (1) that developers stay invested even when they no longer write the code, and (2) that delegating more of the work to AI lowers their cognitive load. Objective: Our goal was to investigate whether developers' neurophysiological states and interactions with AI are consistent with these beliefs when they work with agentic vs. non-agentic AI on their own project vs. a legacy codebase.
Method: We conducted an exploratory within-subjects crossover study with 11 participants across 22 sessions. Each participant used GitHub Copilot Chat in one session and Cursor Agents in the other, working on their own project and a legacy codebase, with tool-codebase pairings randomly assigned and session order counterbalanced. We recorded participants' EEG, on-screen activity, and prompts, and analyzed 7,924 EEG data points, 984 activities, and 141 prompts.
Results: Our findings contradict both beliefs. With the agent, participants remained indifferent to task outcomes, even on their own projects, and cognitive load was higher than with non-agentic AI. Furthermore, their ways of interacting shifted: with non-agentic AI, participants asked how the code worked and read it to verify changes; with the agent, they described desired app behavior and checked results in the running app.
Conclusion: Our study reveals a vibe paradox: delegating to an agent left participants motivationally disinterested, even on their own projects, without relieving cognitive load, while coinciding with increased trust in AI. The community should treat this paradox as a first-class concern if developers and their AI agents are to go far together, and not just fast.

---


### 359. [HQNN-CL: Regime-Aware Hybrid Quantum Neural Network with Continual Learning for Financial Forecasting](https://arxiv.org/abs/2611.02091)

**<font color=#1a73e8>作者：</font>** Muhammad Atif Saeed, Akhtar Jamil, Subhan Ullah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial time-series forecasting is still difficult owing to the non-stationary nature of the market, regime changes, and catastrophic forgetting, which makes conventional deep learning models hard to adapt in the long term. To achieve uncertainty-aware robust financial forecasting in the face of changing market conditions, this study proposes a Hybrid Quantum-Classical Neural Network with Continual Learning (HQNN-CL). The proposed framework combines Gaussian Hidden Markov Model (HMM) based regime detection, BiLSTM temporal encoding, adaptive-depth parameterized quantum circuits, Elastic Weight Consolidation (EWC), experience replay, and probabilistic forecasting in a single architecture. The framework was tested on four real-time stock datasets: Microsoft, Systems Limited, Teradata and Tata Consultancy Services, and compared with seven state-of-the-art forecasting models, including recurrent and Transformer-based models. The experimental results show that HQNN-CL has outperformed other methods on the Systems Limited (RMSE = 3.0149) and Teradata (RMSE = 0.8909) datasets and is within 0.32% and 0.40% of the best baseline method for Microsoft and Tata Consultancy Services, respectively. The proposed framework also generates well-calibrated probabilistic forecasts within the range of 89.5% to 96.5% empirical coverage rate, has zero catastrophic forgetting (BWT = 0.0000) for all sequential learning tasks, and consistently shows positive forward transfer. Ablation and statistical significance analyses also validate the performance of adaptive quantum feature learning and continual adaptation under heterogeneous market conditions, regime-wise.

---


### 360. [ZT-DAC: ML-Driven Dynamic Access Control Policy for Zero Trust in DER Networks](https://arxiv.org/abs/2611.02107)

**<font color=#1a73e8>作者：</font>** Arun B. Chandrasekaran, Damilola Popoola, Souradeep Bhattacharya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing penetration of Distributed Energy Resources (DERs) in the smart grid has significantly expanded the cyber-attack surface. Traditionally, DER networks rely on static role-based access control (RBAC) mechanisms that assume persistent trust after authentication. This limitation enables adversaries to maintain unauthorized privileges and move laterally across DER systems, disrupting grid operations. Although attribute-based access control (ABAC) enables fine-grained and context-aware access decisions, it does not fully eliminate implicit trust. Zero Trust (ZT) principles can be incorporated to enhance ABAC policies. This paper proposes a dynamic access control framework for implementing ZT in DER networks (ZT-DAC). The proposed solution employs a two-stage verification process and integrates an Open Policy Agent (OPA)-based RBAC with a machine learning (ML)-based ABAC to enforce continuous and adaptive trust score assessment. To support realistic DER operations, a DER-specific access control model is developed and used to generate a domain-informed dataset of access requests incorporating both legitimate and adversarial behaviors. Experimental results on the dataset show that the OPA-based decision layer achieves \(91.92\%\) accuracy, with a False Positive Rate of \(14.45\%\), while the ML model achieves a Mean Absolute Error of \(2.074\) and an \(R^2\) of \(0.891\) in trust-score prediction. The ABAC layer achieves \(93.27\%\) accuracy, with a FPR of \(3.88\%\), validating its practical feasibility within realistic DER environments.

---


### 361. [Capable but Not Scalable: Requirements and Interaction Costs of Building Multi-View CAD Datasets for Design Research](https://arxiv.org/abs/2611.02108)

**<font color=#1a73e8>作者：</font>** Danyal Sarfraz, SeEun Lee, Ulugbek Vahobjon Ugli Ismatullaev 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Transforming CAD models into consistent multi-view image datasets is increasingly important for AI-driven product design research, yet existing workflows can impose substantial burdens on researchers without programming expertise. We examine this challenge from a human-computer interaction (HCI) perspective by analyzing ten reported rendering practices and deriving fourteen requirements spanning dataset quality, visual consistency, and user interaction. We then assess eleven development- and design-oriented tools against an illustrative task involving STEP models, interpreting potential interaction costs through the cognitive dimensions framework. Our analysis reveals a gap between technical capability and practical scalability: programming-based frameworks offer flexible automation but require coding expertise, while graphical design tools provide accessible functionality yet retain repetitive per-product operations. No assessed workflow combines a low programming threshold, low repetition viscosity, and flexible protocol configuration. Based on these findings, we propose design directions including reusable rendering presets, collection-wide previews and corrections, mixed-initiative orientation assignment, and automatic provenance recording. This work reframes CAD dataset generation as an end-user interaction design problem and establishes requirements for more accessible, scalable dataset creation tools.

---


### 362. [CNN-Based Retinal OCT Classification: Research Gap Analysis and a From-Scratch Baseline, ED126-A](https://arxiv.org/abs/2611.02114)

**<font color=#1a73e8>作者：</font>** Shkelqim Sherifi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated classification of retinal pathologies from Optical Coherence Tomography (OCT) images remains challenging because diagnostically relevant morphological patterns may exhibit substantial inter-class similarity. Although high classification accuracies have been reported on benchmark OCT datasets, cross-study comparison is limited by heterogeneous evaluation protocols and by the limited characterization of compact convolutional neural network (CNN) baselines trained from random initialization. This study addresses this gap through two contributions. First, it provides a focused review of CNN-based retinal OCT classification and identifies methodological considerations relevant to controlled benchmarking. Second, it presents ED126-A, a purpose-built four-class CNN baseline trained from scratch under a documented experimental protocol on the Kermany labeled OCT dataset. The model contains 1,241,380 total parameters, including 1,239,460 trainable parameters, and is evaluated using training-dynamics analysis, class-wise performance metrics, confusion-matrix analysis, confidence analysis, t-SNE representation-space visualization, Grad-CAM, hierarchical feature-map analysis, and one-vs-rest ROC/Precision-Recall analysis. On the image-level held-out test set, ED126-A achieved 95.03% accuracy, with a macro-F1 of 0.9205 and a weighted-F1 of 0.9521. The principal class-conditional limitation occurred for Drusen, which attained a recall of 0.9605 but a precision of 0.7493 and an F1-score of 0.8419. The confusion matrix identified Normal to Drusen and CNV to Drusen as major error channels. These results support the use of ED126-A as a documented from-scratch reference baseline and provide an empirical basis for controlled evaluation of transfer learning, increased depth, attention, multi-scale feature fusion, and calibration in subsequent studies.

---


### 363. [Testing concept-level audits of melanoma classifiers with diffusion counterfactuals and matched positive controls](https://arxiv.org/abs/2611.02119)

**<font color=#1a73e8>作者：</font>** Md. Shohanoor Rahman, Md. Hasibul Islam, Md Kishor Morol 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept-based explanations of melanoma classifiers are rarely tested against controls with known targets. We built a counterfactual audit from a diffusion model conditioned on seven 7-point checklist concepts and tested it with such controls. Colour-calibrated start noise reduced colour outliers from 78.5-84.8\% to 6.6-13.3\%. Four of seven knobs were target-dominant but also changed other concepts. Quartile-based positive controls were confounded, and the audit failed its pre-specified rule. It recovered the targets of all 16 controls matched on the generator's pseudo-labels and of 12 of 12 controls labelled by a second evaluator, for three concepts; concept activation vectors recovered fewer (11 of 16). In 18 permuted-label classifiers, significant sweep responses and target rankings also arose, whereas standardised effect margins separated the controls from these null classifiers. The pigmentation sweep raised the melanoma logit in 15 of 15 ISIC 2020 classifiers (+3.12 on average) and 6 of 6 HAM10000 classifiers (+4.01), about four times the null response in scale-free units; the regression effect did not transfer. An exploratory decomposition, evaluated against the controls, suggested that knob cross-talk partly hides vascular responses. Matched controls and null classifiers are practical checks of concept audits.

---


### 364. [Conditional Calibration Contracts under Coupled Load: A Branch-Aware Audit of Switched Inference](https://arxiv.org/abs/2611.02121)

**<font color=#1a73e8>作者：</font>** Juan S. Santillana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bursty serving changes both queue states and the population selected for each model. We study conditional calibration contracts as a specification to be validated, rather than a certified property of an existing router. CA-MHD combines load-coupled distillation, closed-loop replay and a cost-informed Schmitt router in a discrete-event simulator with a hardware service table. Across 40 cells (ten training seeds and four content-load coupling levels), we distinguish the original teacher, frozen wide heads on an adapted trunk, and the narrow student. A common teacher-trajectory audit has median absolute student-teacher deficit 0.06 percentage points, but does not certify the student-selected deployment support. Historical results use a kernel correctness gap, not the published SmoothECE; we separately prove selected-branch composition for a residual functional at a common fixed scale. The deployed wide branch has lower ordinal accuracy than the original teacher in all 40 cells. Same-checkpoint student-only serving has lower historical ordinal gap in 27/40 cells; routing also exposes violation tails up to 17.5 percent. Student p99 latency remains above the 1.5 ms target. Retrospective temporal recalibration improves the ordinal gap in 39/40 cells, but causal delayed-label availability is unverified and no incremental per-mode benefit is detected after multiplicity adjustment. An in-sample CUSUM detects 30/40 checkpoint changes at five historical false alarms, with no prospective false-alarm guarantee. These findings support a branch-aware audit and a scoped negative result, not demonstrated routing superiority. Independent budgets, selected-support validation and net utility under a satisfied SLA remain open.

---


### 365. [Bounded Retained History in a Proxy Flow Replay: A Mixed Predictive Pilot and an Allocation Study](https://arxiv.org/abs/2611.02123)

**<font color=#1a73e8>作者：</font>** Juan S. Santillana  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We examine bounded retained history through a frozen predictive pilot and a subsequent allocation study on a curated UNSW-NB15 flow mirror. Both use an artificial release-order replay based on raw ltime ticks, with equal-tick records querying a shared prior-group state. In the pilot, the model with added retained relational features had lower reconnaissance recall than the current-flow-plus-counters baseline (43.66% versus 47.84%) and lower benign false-positive rate (3.63% versus 6.68%) at separately frozen operating thresholds, together with lower AUROC. This mixed result did not establish a predictive advantage. A development-only audit subsequently found that capacity eviction dominated expiration in the 256-record, 300-tick FIFO state, with a median completed record lifetime of 11 ticks. A protocol specified before its single execution, but after the pilot and post-hoc mechanism audit, compared five label-blind retention arms on the already-used development trace. Its primary equal-source endpoint averaged retained/reference ratios for service-expanded source out-degree and source-destination service diversity. Source-balanced retention at 256 records exceeded FIFO-256 by a pooled endpoint difference of 0.440738 and met the prespecified materiality and subblock rule. Crucially, the event-weighted ratios for both quantities decreased relative to FIFO-256: the result is specific to the equal-source weighting objective and does not establish uniformly improved retention. The study supplies neither evidence of detection improvement nor an explanation of the pilot result. Reused data, concentrated reconnaissance support, proxy timing, and the absence of a qualified independent corpus bound the interpretation.

---


### 366. [Mesh2Shell Neural Operator for Inverse Shape Optimization](https://arxiv.org/abs/2611.02127)

**<font color=#1a73e8>作者：</font>** Xinyi Li, Xi Deng, Yubo Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-driven design seeks high-performing geometries, which need not conform to a learned shape category. Parametric and latent-space approaches facilitate surrogate-based optimization, but restrict deformations to prescribed shape families or learned decoders. We introduce the Mesh-to-Shell Neural Operator (M2S-NO) as the mesh-to-shell component of a category-agnostic inverse shape optimization framework. We separate the explicit mesh used for design from the volumetric representation used for physics prediction. M2S-NO maps oriented surface samples to a surface-centered shell representation, such as TruncatedSDF or HeatSDF. A separate problem-specific PDE neural operator (PDE-NO) maps this representation to physical fields. Objective gradients update mesh vertices through both operators, without a latent shape decoder. Preconditioning and remeshing support free-form deformation, while fixed interfaces are controlled directly on the mesh. Optional shell-space proposals enable topology changes. We evaluate geometric matching, jet-engine brackets, and neutron moderators, with independent FEM and OpenMC evaluation. Relative to the best training designs, M2S-NO reduces maximum bracket displacement by 14.3% and increases neutron-sensor current by 13.8%. Optimization also succeeds from an out-of-distribution bracket initialization, demonstrating the framework's geometric flexibility.

---


### 367. [TSSDA: An Autonomous Agent for Constructing a Time-Series Text-to-SQL Benchmark](https://arxiv.org/abs/2611.02132)

**<font color=#1a73e8>作者：</font>** Zhihan Zheng, Shaoxu Song, Haitao Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As agents increasingly undertake data querying, Text-to-SQL serves as a foundational capability for database access. However, for text-to-SQL in time-series databases, high-quality benchmarks and large-scale training corpora remain scarce, limiting the systematic evaluation and domain adaptation of existing models and agents. Existing automated SQL generation approaches lack sufficient autonomy, leaving key challenges unresolved. First, numerous combinations of temporal syntax and functions complicate comprehensive coverage of valid queries. Second, as the corpus grows, generating valuable and diverse new data becomes increasingly challenging. Third, schema and data heterogeneity hinder reuse of temporal query structures, limiting generation efficiency. To address these challenges, we propose TSSDA, a Time-Series SQL (TSSQL) Generation Data Agent framework, and construct TERN, a comprehensive Time-sERies text-to-SQL beNchmark. First, to achieve broad coverage of valid queries, we systematically model TSSQL syntax and semantics to construct a data generation space. Next, to explore the space and improve diversity, we develop a Data Agent that autonomously orchestrates data generation. The agent comprises a planning and decision-making module and a query generation module, with online adaptation for continuous self-improvement. Finally, we introduce a temporal-aware memory that enables adaptive reuse of experience across heterogeneous data instances, improving generation efficiency. Comprehensive evaluations on TERN reveal the limitations of existing methods in performing Text-to-TSSQL tasks. Furthermore, extensive experiments demonstrate that TSSDA substantially improves coverage, diversity, and complexity.

---


### 368. [When Is Personalized Federated Learning Worth Its Deployment Cost?](https://arxiv.org/abs/2611.02146)

**<font color=#1a73e8>作者：</font>** Beyazit Bestami Yuksel, Ayse Yilmazer Metin, Emrah Dikbiyik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized federated learning (PFL) may improve client-level performance, but deeper personalization increases deployment cost. We formulate personalization-depth selection as a utility-based empirical decision problem in which client utility equals Macro-F1 minus a cost-sensitivity weight times deployment cost, over six personalization depths labeled P0 through P5. We compare fixed policies with an offline per-client Oracle reference and report allocation maps over Dirichlet data heterogeneity and cost sensitivity. Although evaluated on this hierarchy, the formulation can accommodate any finite candidate set. On CIFAR-10, CIFAR-100, and a PTB-XL subset, personalization shows empirical, setting-dependent decision regimes rather than a universal benefit: higher cost sensitivity shifts Oracle mass toward the global-only depth P0; low cost sensitivity can favor deeper actions. Patterns are grid observations (three seeds per cell), not theoretical boundaries. Best-uniform is competitive with Oracle assignment (6.5 percent plus or minus 7.8 percent relative regret; 95 percent confidence interval 5.9 to 7.1), whereas random and personalize-all incur much larger regret (189.3 percent plus or minus 367.1 percent and 409.0 percent plus or minus 803.2 percent). Under the same utility, Ditto full-model personalization is substantially suboptimal once cost is counted. The contribution is an offline characterization of when personalization depth is worth its cost, not a new PFL optimizer or deployment-time scheduler.

---


### 369. [Refining Roadside 4D Radar Vehicle Classification Using Point-Cloud Dispersion](https://arxiv.org/abs/2611.02147)

**<font color=#1a73e8>作者：</font>** Mohammed Alsakabi, Andreia Figueiredo, António Almeida 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Roadside sensing infrastructure is essential for Intelligent Transportation Systems (ITS), but cameras and legacy sensors are limited in range, weather robustness, and depth accuracy. 4D radar complements these modalities by resolving range, azimuth, elevation, and radial velocity under adverse conditions, though its sparse, noisy point clouds make reliable classification difficult. We present a roadside multi-sensor platform combining a 4D radar and stereo depth camera under synchronized acquisition, used to collect a real-world dataset. Our analysis reveals a substantial class-distribution discrepancy between modalities, most notably a strong radar confusion between passenger cars and motorcycles (49.01% and\ 48.60% of the dataset). To address this, we propose a Neyman-Pearson-based binary classifier on the temporally-smoothed 2D positional standard deviation of radar point cloud clusters, reducing classification error from 52.1% to 42.7%. This lightweight and edge-deployable approach improves radar-only classification reliability and lays the foundation for future camera-radar fusion.

---


### 370. [Detailed Derivation of The Backpropagation Algorithm](https://arxiv.org/abs/2611.02152)

**<font color=#1a73e8>作者：</font>** Faris Alasmary  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Backpropagation is the standard method for computing the gradients that train neural networks, but it is usually presented in a compact vector form that skips the intermediate steps. This tutorial derives backpropagation step by step for a fully connected feedforward network with sigmoid activations and a squared-error loss. Using a running example with three layers, we first differentiate the error with respect to a single weight by following its path through the network with the chain rule. We then show how summing over all paths leads to the error terms $\delta$ and to the four general backpropagation equations in matrix form. Every term is annotated with its dimensions, so each equation can be checked for consistency. The derivation is then extended to $m$ training examples, where the weight gradients become a single matrix product and the bias term corresponds to broadcasting. It is also extended to mini-batch gradient descent, including why the gradient of a mini-batch estimates the full gradient. Batch and mini-batch training are both given as algorithms. Finally, each equation is linked to the corresponding line of a NumPy implementation trained on the AHDBase dataset of handwritten Arabic digits, and the complete code is included.

---


### 371. [Value Forcing: Aligning Return Distributions at All Noise Levels](https://arxiv.org/abs/2611.02160)

**<font color=#1a73e8>作者：</font>** Chongyi Zheng, Zhiyuan Zhou, Qiyang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning accurate value functions is central to reinforcement learning (RL), yet remains challenging because supervision is limited and indirect: ground-truth values are unavailable, and each transition in the data only provides an immediate reward that can be used to construct bootstrapped targets as supervision. This challenge is particularly pronounced when data is limited or reward signals are sparse, as is common in real-world applications such as robotics. We argue that the key to accurate value learning in this limited data regime is extracting richer learning signals from the available data. In this paper, we introduce Value Forcing, a new approach that uses flow matching to estimate return distributions and enables accurate value learning from limited data. Our key insight is that we can extract richer learning signals by enforcing Bellman consistency at every noise level. Empirically, Value Forcing improves the accuracy of estimating the return distribution, and prevents the distribution from collapsing to a single value, as occurs with prior methods. We instantiate Value Forcing with two practical value-learning algorithms: VF, an actor-critic method, and IVF, an implicit value-learning method. We evaluate both algorithms across $26$ long-horizon tasks in the offline RL setting and find that they outperform prior value-learning methods, with particularly large gains when data is limited. Our project website is available at this https URL.

---


### 372. [Rewarded for Not Getting Caught: Why Alignment Training Selects for Conditional Compliance and Cannot Instill Norms](https://arxiv.org/abs/2611.02162)

**<font color=#1a73e8>作者：</font>** Kevin Baum, Ruta Binkytė, Gerrit Großmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current alignment training cannot be expected to deliver what it is meant to deliver: AI agents that comply with norms whatever the gains and whether or not anyone is watching. Training that rewards and penalizes behavior can teach norms only through that reward, and a reward can encode a norm only as a price: "do not do X" becomes "doing X costs something", and training charges the cost only when X is noticed. A price, unlike a norm, can be paid: a large enough gain outweighs it, noticed or not. And because the cost is charged only where violations are noticed, training cannot favor a policy that always complies over one that complies only where it would be caught. When an unnoticed violation is the only way to complete a task, it even favors the latter, the more so the more strongly it rewards task success. Agency makes this the normal case: agents mostly act without oversight, can often tell when they are observed, and may take steps to evade observation. That agents behave as intended when they infer they are being tested, and differently when they infer they are not, is therefore no malfunction; the training regime is working as built. This reading unifies alignment faking, sandbagging, and evaluation-aware scheming. No behavioral evaluation can show that a model does better, since that would require observing how it behaves unobserved; a model that complies when it seems unobserved may simply have recognized the test. Easing the pressure on agents to complete tasks at any cost can make violations rarer, but never impossible. For norms that no gain should be allowed to outweigh, the remedy is not deeper internalization but architecture that makes violations unavailable rather than unchosen. We state this argument explicitly, premise by premise, read recent findings and a real-world incident against it, and draw consequences for design and governance.

---


### 373. [Black-Box Adversarial Example Attacks on Machine Learning based Election Systems](https://arxiv.org/abs/2611.02166)

**<font color=#1a73e8>作者：</font>** Subek Acharya, Syed Ayon, Khaleque Md Aashiq Kamal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning models have shown exceptional accuracy for ballot classification in election systems. Recent research has demonstrated that these ballot classification models are vulnerable to adversarial example attacks. This is a critical security issue because a successful attack could alter the outcome of an election and undermine the democratic process. However, all adversarial example attacks in the voting domain have assumed a white-box threat model, where the classifier parameters are known. In this work, we advance the field of machine learning in election systems by analyzing a realistic black-box adversary. We implement and evaluate eleven state-of-the-art black-box attacks: query based attacks ADBA, Square, SurFree, RayS, and SA-MOO. We also test adaptive transfer based black-box attacks with APGD-$l_\infty$, APGD-$l_2$, APGD-$l_1$, PGD $l_0$, PGD $l_0$+$l_\infty$, and PGD $l_0$+$\sigma$. Our attacks span multiple different norms ($l_\infty$, $l_2$, $l_1$, and $l_0$) and three different black-box adversarial threat models (decision based, score based and transfer based). In addition to digital analyses, we physically print and scan $20,000$ adversarial examples to evaluate the real-world performance of different black-box attacks. Our finding demonstrate an even larger physical-digital robustness gap exists for black-box adversarial examples than for white-box adversarial examples. Lastly, we conduct the first ever adversarial example transferability study in the voting domain and test adversarial training and barrier zones as two possible black-box defense strategies.

---


### 374. [Restrained Diffusion Bridges: Targeted Denoiser Training and Refinement](https://arxiv.org/abs/2611.02170)

**<font color=#1a73e8>作者：</font>** Xuanxi Zhang, Kevin S. Cheng, Weizhou Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are often inaccurate in critical, data-sparse regions of the target distribution. Sampling from restrained distributions, biased distributions used in classical enhanced sampling to concentrate data near chosen configurations, can control where training data are collected but biases the learned distribution. We establish that this bias cancels exactly when forward noising from restrained data is conditioned on the restrained configuration at an appropriately chosen intermediate time. This allows a pretrained model fine-tuned on restrained data to achieve high accuracy in any chosen region of the target distribution, regardless of its probability, using standard denoising or flow matching objectives without importance weights. When no target data are available, Gibbs sampling enables inference from a model trained exclusively on restrained data.

---


### 375. [Harassment on TikTok: A Mixed-Methods Analysis of Video Content and Psycholinguistic Comment Stances](https://arxiv.org/abs/2611.02172)

**<font color=#1a73e8>作者：</font>** Afsaneh Razi, Tyler Chang, Michal Monselise 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite extensive research on harassment, how it manifests on short--form video platforms such as TikTok---and how it shapes user interactions---remains underexplored, though these dynamics are critical for designing effective safety strategies for online communities. We present a mixed-methods study of 190 TikTok videos tagged with hashtag harassment and their 66,337 comments. Our qualitative analysis of videos identifies harassment types (sexual, verbal, stalking, law enforcement, bullying, catcalling, and gaslighting) and their characteristics (e.g., location, target, video style, and theme), along with engagement patterns. Although sexual harassment was the most prevalent topic, it did not have the highest engagement; instead, stalking--related videos received the most views. Pairwise comparisons and regression--based analyses of comments' psycholinguistic features and stance (support, opposition, neutrality) revealed differences in emotional tone, social orientation, and cognitive categories across harassment types. Comments on sexual harassment frequently express solidarity with victims, whereas discussions of law enforcement harassment emphasize institutional critique. We provide implications of our findings, demonstrating that harassment on TikTok is multifaceted, shaped by content, context, and community norms.

---


### 376. [Beyond Unit-Circle Eigenvalues: Invariant Bases for Stable State Space Dynamics](https://arxiv.org/abs/2611.02174)

**<font color=#1a73e8>作者：</font>** Jiaqian Zhu, Yang Zhang, Junhua Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diagonal state space models process long sequences at linear cost, yet the same transition is applied at every step of a rollout, so an unconstrained recurrence holds no quantity fixed and the state decays or grows without bound. Current designs constrain one quantity, and preserving one does not guarantee preservation of the others, so a model can hold its norm to machine precision while momentum drifts by hundreds of percent. We claim that the conserved quantities of a diagonal recurrence are layered, that each layer requires a strictly stronger condition on the operator, and that a unit-modulus spectrum reaches only the outermost. Acting on the claim, we enforce the conditions required for every layer by construction. The generator of the Kronecker-Cayley transition (KC) is a graph Laplacian over object subspaces, $\mathbf{H}=\mathbf{L}\otimes I_m$, advanced by a Cayley transform, and the step stays diagonal at $O(N^3+N^2m)$ cost. The conserved set is exactly a $2m^2$-dimensional family of quadratic forms, held at every parameter value, so the quantities and the dynamics the construction reaches are fixed before training. On four conservation benchmarks, KC holds total mass at or near the reference floor while every diagonal baseline loses it by orders of magnitude. We further compare against mass correction and find that two correctors fail once the underlying prediction diverges, which shows that assembly rather than correction is necessary for a guarantee that holds across the rollout. A free modal basis trained under a conservation penalty conserves only by freezing its spectrum, whereas the assembled operator conserves with every mode but one free to rotate. Beyond these benchmarks, KC holds the linear momentum of three $N$-body systems and, at the operator level, the conserved quantity in molecular dynamics, chemical kinetics, pharmacokinetics and power-grid swing dynamics.

---


### 377. [ANCHOR: KL-Anchored Adaptation for Stable Offline-to-Online RL](https://arxiv.org/abs/2611.02177)

**<font color=#1a73e8>作者：</font>** Geonwoo Cho, Jaegyun Im, Doyoon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline-to-online reinforcement learning (RL) follows the pretrain-finetune paradigm: an agent is first pretrained on historical data and then adapted through online interaction. We study offline-to-online adaptation without offline replay, where the agent must improve using only the pretrained model and newly collected experience. A key challenge is to avoid catastrophic failure, a sharp early performance collapse during online fine-tuning, while still achieving strong asymptotic performance. Through controlled experiments, we show that removing offline replay can induce catastrophic failure, while retaining strong conservative regularization from offline RL can suppress final online performance. We also find that common stabilization strategies do not reliably prevent early collapse, and that the critic-side mechanisms we test are insufficient on their own. Motivated by these findings, we propose ANCHOR, a simple adaptation method that anchors the actor to the offline-pretrained policy early in online fine-tuning, anneals this constraint over time, and retains only a small residual conservative critic regularizer. We provide a theoretical interpretation showing that KL anchoring helps preserve critic reliability across nearby occupancy distributions, with a two-phase regret bound explaining when anchoring should be maintained or relaxed. Across FrankaKitchen, AntMaze, and Adroit tasks, ANCHOR substantially reduces catastrophic failure while maintaining strong asymptotic performance. Ablations show that KL annealing and the residual conservative weight are important for balancing early stability and online adaptation, while additional analysis shows that ANCHOR is most beneficial when the pretrained policy contains useful behavior to preserve. Code is available at this https URL.

---


### 378. [A Matched Evaluation of QUBO Action Models and Defensive Remediation in Cyber Attack Graphs](https://arxiv.org/abs/2611.02179)

**<font color=#1a73e8>作者：</font>** Kasymkhan Khubiev, Yaroslav Kholodov, Alexey S. Petrenko  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This study examines how vulnerability-specific actions affect quadratic unconstrained binary optimization (QUBO) models for minimum-cost cyber attack paths and defensive remediation. Edge-flow and variable-length hop formulations are evaluated using simulated annealing, steepest descent, and tabu search against exact classical references. Experiments on six independent synthetic topologies separate the effects of transition eligibility, vulnerability labels, exploit costs, and multiple exploit alternatives. A single labeled action per eligible transition preserves feasible paths, optimal costs, and QUBO size. Under the tested settings, multiple exploit alternatives were associated with approximately unchanged valid-path recovery, lower optimal-path recovery, and substantially larger representations, particularly for the hop formulation. These recovery differences remain descriptive because they are not statistically significant after correction for multiple comparisons. An evaluation on a published 3CX attack graph with synthetic costs demonstrates applicability beyond the generated topologies. The defensive extension selects patches within a budget to raise attack-path costs to specified thresholds or disconnect protected targets. Against exhaustive and mixed-integer references, the tested QUBO heuristics recovered an optimal patch set in 12 of 16 calls across eight scenarios on one topology.
The results characterize formulation correctness, solution recovery, and resource requirements using classical local optimization, without establishing quantum computational advantage.

---


### 379. [Inner-Speech Decoding from EEG Across Three Corpora Under a Fixed Architecture and Protocol](https://arxiv.org/abs/2611.02180)

**<font color=#1a73e8>作者：</font>** Md Wahiduzzaman Suva, Md Imtiaj Alam Sajin, Esm E Moula Chowdhury Abha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inner-speech decoding from electroencephalography could support non-invasive communication for people with severe motor impairment, but comparison across studies is hindered by dataset- and protocol-specific evaluation. We present a controlled cross-dataset study using one preprocessing pipeline, one within-subject five-fold cross-validation protocol, and a compact dual-attention Transformer (VC-DATNet; approximately 131,000 parameters) across three public corpora: Thinking Out Loud (10 participants), BISpeech (4), and SyncSpeech (3). VC-DATNet achieved per-participant sensor/source hybrid accuracies of 39.48% on the four-class Thinking Out Loud task, 20.60% on the eight-word BISpeech task, and 25.53% on the eight-word SyncSpeech task, for which we report the first decoding result. Sensor-space and cortical source-space representations were complementary, with each performing better for different participants; this pattern replicated across all three corpora and nine architectures. Moreover, ten decoders spanning convolutional, recurrent, temporal-convolutional, hybrid Transformer, and pretrained foundation-model families converged within a narrow accuracy range on every dataset. These findings indicate that representation choice should be individualized and suggest that performance on these public corpora is constrained more by signal quality and dataset scale than by model capacity. The released pipeline provides a reproducible benchmark for future inner-speech decoding studies

---


### 380. [Recursive Reasoning Exploration: Mathematical Research through Evolving Reasoning Graphs : case study: An Exact Certificate-Degree Theorem for Two-Term Tensor Decompositions : Phase III of the Math Instruments Program](https://arxiv.org/abs/2611.02186)

**<font color=#1a73e8>作者：</font>** Ying Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large collections of manuscripts and research notes offer ways to reuse arguments, while making it harder to retain hypotheses, check claims, and understand how results were obtained. We propose Recursive Reasoning Exploration (RRE), a framework for cumulative mathematical research through evolving reasoning graphs. RRE links claims and jointly required premises to research targets, attempted arguments, counterexamples, checks, and revisions. Each investigation can generate further targets, and its supported outcomes become available to subsequent investigations. This is Phase III of the Math Instruments program: identifying mathematical instruments, reconstructing reusable reasoning, and organizing recursive research from that reasoning. The framework supports human-directed, collaborative, and goal-directed autonomous exploration, with open-ended exploration as a further mode. Its records also provide material for learning how mathematical investigations develop. A complexity research case study establishes an exact theorem: for every complex tensor of order n >= 2 and rank greater than two, the minimum Nullstellensatz certificate degree for its original two-term decomposition equations is 3n. This includes an infinite family whose every flattening has rank at most two. The exploration develops an explicit boundary certificate, a balanced transfer lemma, and an exhaustive argument using classical rank-two geometry. A parallel branch gives bounds 3m + 3 <= delta_m(I_m, N) <= 3m + 6 for every nonzero nilpotent m by m matrix. Six graph revisions record the progression from inherited results to these theorems, with exact arithmetic checks and a replayable exploration history. We present the RRE representation and protocol, the mathematical proofs, visualizations of graph evolution, and a research agenda for shared human-AI exploration, cumulative reuse, and education.

---


### 381. [Fuzzy-Enhanced Machine Learning Approach for Type 2 Diabetes Diagnosis](https://arxiv.org/abs/2611.02188)

**<font color=#1a73e8>作者：</font>** Azam Saffar, Mohsen Saffar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate diabetes prediction is critical for early clinical intervention, yet existing machine-learning pipelines often fail due to class imbalance, noisy physiological measurements, and redundant or weakly informative features. To address these unresolved limitations, this study establishes a unified fuzzy-evolutionary-ensemble framework designed to uncover a more discriminative feature space for type 2 diabetes prediction. The workflow integrates selective fuzzification of nonlinear clinical variables, SMOTE-ENN-based balancing and noise filtering, and Bat-Algorithm-driven evolutionary feature selection prior to training a Random Forest classifier. Applied to the Pima Indians Diabetes Dataset, the framework compresses the expanded fuzzy-numerical space into an optimized 10-feature subset and yields substantial performance gains: 96.11% accuracy, 95.14% precision, 98.00% recall, and a 98.23% F1-score. Relative to a baseline Random Forest using all 16 features (74.45% accuracy; 59.86% F1), the system achieves more than a 1.6-fold improvement in F1-score while preserving over 99% stability in majority-class detection and surpassing earlier published 16-feature models impacted by imbalance and weak feature relevance. Collectively, these results demonstrate that the integrated pipeline produces an enhanced fuzzy-numerical representation space that improves diabetes risk stratification and provides a scalable, uncertainty-aware foundation for diagnostic modeling across broader clinical datasets.

---


### 382. [Increasing the security of advanced metering infrastructure using dynamic defense methods](https://arxiv.org/abs/2611.02193)

**<font color=#1a73e8>作者：</font>** Mohsen Saffar, Hamid Reza Naji  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the increase in Internet usage over the last half century, technology has also benefited from the growth and development of the Internet. It is no wonder that smart grids are emerging as one of the most popular technologies of today. As smart grids are connected to the internet, they are constantly vulnerable to cyberattacks. It is always possible for attackers to gain access to metering system infrastructure which is a major and critical part of smart grids. When this system is not working properly because of some security threats, irreparable damage is in the place for a country and its industries. This article suggests utilizing dynamic Applications that Participate in Their Own Defense defenses to secure such systems and infrastructures.

---


### 383. [A conditional generative model for T2-weighted prostate MRI with downstream evaluation in clinically significant cancer classificatio](https://arxiv.org/abs/2611.02197)

**<font color=#1a73e8>作者：</font>** Xavier Rafael-Palou, Alejandro Vergara-Richart, Ignacio Iborra Roncales 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scarce and unrepresentative training data limit the performance of prostate MRI prediction models. Synthetic T2-weighted (T2W) MRI may augment training data containing clinically significant prostate cancer (csPCa) and transition zone (TZ) lesions. In this retrospective, single-center, ethics-committee-approved study, we developed a conditional generative model for T2W prostate MRI extending MAISI-v2 with csPCa class, zonal, and lesion-mask-guided conditioning, incorporating a relative advantage weighted loss fine-tuned on 1,303 patients (1,654 lesions). Fidelity was assessed by incremental ablation, and downstream utility was evaluated with T2W-based csPCa classifiers across five simulated training-data scenarios, each testing 18 synthetic-data configurations. The proposed model reduced Fréchet inception distance (FID) from 13.28 (pretrained MAISI-v2) to $2.04 \pm 0.06$ internally (PI-CAI: $3.83 \pm 0.51$). Synthetic augmentation significantly increased AUC in all five scenarios (+0.027 to +0.088; adjusted $p = 0.016$--$0.043$), though cross-institutional augmentation of PI-CAI yielded a non-significant gain (+0.013; $p = 0.397$). Overall, our model improved T2W MRI fidelity, and synthetic images improved csPCa classification under simulated data constraints, although benefit did not transfer significantly across institutions.

---


### 384. [Depth Anyviewpoint? Evaluating Monocular Depth Over Viewpoint Sequences](https://arxiv.org/abs/2611.02203)

**<font color=#1a73e8>作者：</font>** Theo Rode, Rui Zhang, Ryan Aubrey 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation aims to predict depth maps from single RGB images (forgoing the need for stereo camera pairs) and has seen impressive leaps in performance in recent work due to the introduction of affine-invariant losses and the use of foundation model features. These monocular depth models predict affine-invariant depth, which describes the relative positions of objects in the scene instead of absolute depth. While these models demonstrate strong performance on single image benchmarks and qualitatively consistent predictions in video, their effectiveness at preserving consistent spatial structure has been less thoroughly explored. Many potential real-world applications, such as handling video streams as input, rely on coherent three dimensional consistency in scenes. Further, anchoring relative depth predictions to a metric reference for a given scene is a key challenge for applying monocular depth models to real-world situations. We develop a novel evaluation protocol for monocular depth models using video sequences with moving camera positions to test the consistency of prediction across variation in viewpoint. We demonstrate this methodology over diverse, real-world video sequences where we are able to anchor depth model output to metric depth values using structure from motion. Our work demonstrates open challenges in the development of broadly applicable monocular depth foundation models, particularly with their ability to provide temporal consistency over long time frames. We also identify challenges in the straightforward adoption of structure-from-motion as a metric grounding tool for monocular depth estimation models.

---


### 385. [Learning from high-resolution 2D images to reconstruct 3D microstructures](https://arxiv.org/abs/2611.02204)

**<font color=#1a73e8>作者：</font>** Wenbo Sui, Lars P. Mikkelsen, Jens W. Andreasen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution three-dimensional (3D) microstructure characterization remains difficult to undertake at scale because volumetric imaging at the required spatial resolution is expensive, time-consuming or destructive. In many settings, however, fine-resolution two-dimensional (2D) imaging and lower-resolution volumetric measurements are both readily available. We introduce a Privileged Cross-modal Relational Distillation (PCRD) framework that leverages fine-resolution 2D observations during training to improve specimen-specific 3D reconstruction from lower-resolution volumetric imaging alone. We demonstrate PCRD on pultruded carbon fiber-reinforced polymer composites, using scanning electron microscopy as the privileged modality and micro-CT as the inference input. The framework transfers spatial organization by matching similarity distributions defined around corresponding spatial anchors in the teacher and student representations, avoiding direct alignment of heterogeneous feature vectors. In 2D cross-sectional reconstruction, PCRD improves mAP by 1.66 percentage points over direct micro-CT training. Independent 3D validation against high-resolution synchrotron X-ray CT data shows close agreement in fiber volume fraction, diameter and local spacing. The PCRD reconstruction matches 89.97% of the reference fiber centerline length, compared with 75.08% for the interpolated low-resolution volume.

---


### 386. [Forecasting Earth Surface Change in Embedding Space](https://arxiv.org/abs/2611.02211)

**<font color=#1a73e8>作者：</font>** Jingtao Li, Sadiq Jaffer, Anil Madhavapeddy 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Repeated satellite imagery permits understanding of how our planet changes over time, letting us predict its future and plan mitigating actions. Most existing studies that rely on a time series of satellite observations forecast the spectral values at each pixel for a future target date. However, clouds, shadows, and sensor noise often corrupt these observations, so that spectral forecasters waste much of their capacity on low-level features or noise rather than real change. With the advent of Earth foundation models, we argue that forecasting in embedding space is a feasible and more effective alternative. To this end, we design a token space that handles irregular histories from different sensors and foundation models and supports forecasts at any query date. Tokens from this space are inputs to our proposed forecaster, E$^2$Forecast, which is a transformer with two branches: a Gaussian branch that directly predicts a mean point forecast and per-dimension standard deviations, and a rectified-flow branch that generates forecast ensembles. On Sentinel-1 and Sentinel-2 benchmarks, forecasting embeddings instead of spectral values halves the cosine distance (from 0.20 to 0.10) and greatly reduces overconfidence, lowering the z-score standard deviation from 2.63 to 1.22. By comparing new observations with its forecasts, E$^2$Forecast can also detect anomalous changes without labels or retraining, raising F$_1$ from 41.58 to 48.70 on a global benchmark. This consistent superiority is validated on nine remote sensing foundation models. Beyond change detection, we believe our approach advances the field by permitting effective reuse of diverse pretrained task heads. Our code is publicly available at this https URL.

---


### 387. [Discrimination, Calibration, and Ranking: A Unified Matrix Framework](https://arxiv.org/abs/2611.02215)

**<font color=#1a73e8>作者：</font>** Ronaldo Cristiano Prati, Farangis Johari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrimination, calibration, and ranking are the three pillars of classifier evaluation, yet no single algebraic language spans all three. A recent indicator-matrix account unifies discrimination measures (precision, recall, F1, Matthews correlation) across binary, multiclass, multilabel and related settings, using Boolean cell operations on indicator label matrices, generalised to soft labels by t-norms. Calibration measures (Brier score, log-loss) and ranking measures (nDCG, AUC) fall outside it. We close the gap with two further classes of cell operators: deviation operators phi(y - yhat), which give a Calibration Framework, and rank- and slice-dependent operators (positional gains for DCG, column concordance cells for AUC), which give a Ranking Framework. Both inherit the micro/macro/exemplar aggregation architecture. For calibration, the three Brier aggregations collapse to one scalar; the Murphy decomposition holds in matrix form (unbinned, binned and isotonic); and, within the Brier-type class-indexed family, a measure is skew-invariant if and only if it depends only on the class-conditional errors alpha_j and beta_j, the calibration analogues of recall and specificity. For ranking, raw DCG collapses across aggregations while nDCG does not; per-class nDCG and per-class AUC are related by a row-column duality; micro-AUC differs from pooled ROC-AUC; raw positional scores are never strictly proper, and nDCG and AUC need not be proper. The skew-invariant per-class building blocks share one class-conditional expectation template. Experiments on two multilabel benchmarks illustrate the distinctions. Many of the results are machine-checked in Lean 4; the proofs, the experiments and the this http URL package are public: this https URL

---


### 388. [Iterative Gumbel Planning for Continuous Control](https://arxiv.org/abs/2611.02236)

**<font color=#1a73e8>作者：</font>** Shaohuai Liu, Weirui Ye, Yilun Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Search-based planning remains a powerful policy improvement paradigm in reinforcement learning, driving milestone successes in discrete domains. However, extending this paradigm to continuous control exposes a structural mismatch: search evaluates a finite set of action candidates, whereas continuous RL typically relies on Gaussian policies. We show that winner-action distillation into a continuous Gaussian induces a \textit{projection error} and a stepwise variance-expanding gradient tendency when the selected action is sufficiently far from the current mean. Empirically, this tendency is associated with elevated terminal variance and a return gap on the evaluated tasks. To address this, we propose \textbf{Iterative Gumbel Planning (IGP)}. By adopting a per-dimension factorized categorical policy, IGP naturally aligns the policy support with the search candidates, eliminating the projection error and reducing the residual approximation to a bounded discretization error. To bypass the combinatorial explosion of high-dimensional discrete action spaces, IGP pairs Gumbel Top-$K$ candidate sampling with an MPPI-style multi-round iterative search to refine the policy at each state. Empirically, IGP achieves state-of-the-art aggregate performance and sample efficiency on DMControl and HumanoidBench. Furthermore, it produces more stable action sequences with lower temporal variance, demonstrating its practical potential for real-world robotic deployment.

---


### 389. [Nonreciprocal Spherical Attention and Retrieval: Sharp Coarsening Clocks and Certified Score Correction](https://arxiv.org/abs/2611.02237)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Taylan Alpay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop nonreciprocal spherical attention as a mathematical framework for coarsening and compressed nearest-neighbor retrieval. For two shrinking acute blocks whose centers have zero skew pairing and whose total mass ratio is subexponential in inverse temperature, we prove $\lim_{\beta\to\infty}\beta^{-1}\log T_\beta=1-\cos\phi$, without restricting particle-count growth. An explicit three-body flow has two rigorously separated metastable exponents. For finite compression, mass centering yields a sharp $O(r^2)$ attention-output error bound at fixed temperature, with an explicit spherical-normalization correction. We formulate skew query-side score calibration as a strictly convex moment problem and derive a unique normal equation, residual-based optimization certificates, and bounded low-rank projections. A norm-aware margin objective calibrates native squared-distance rankings. Experiments use semantic retrieval data, one million visual descriptors with three codebook seeds, and a ten-million-vector FAISS IVF-PQ index with recomputed exact cosine ground truth. On SIFT1M, skew margin calibration raises native-L2 hit@10 from 0.8926 to 0.8948; symmetric calibration reaches 0.8996. The ten-million-vector index reaches 0.8827 hit@10 at 0.1794 ms per query in a four-thread batch benchmark, while validation selects no skew update. Exact streamed attention over ten million keys evaluates compressed memory on 1,024 held-out queries. Independent matrix solves, automatic differentiation, finite differences, interval arithmetic, full-flow tests, and nine Rocq-checked algebra lemmas support reproducibility. Directionality alone does not establish retrieval superiority.

---


### 390. [User Engagement in Visualization: A Scoping Review of 243 Research Articles](https://arxiv.org/abs/2611.02238)

**<font color=#1a73e8>作者：</font>** Mara Solen, Clara-Marie Barth, Heather O'Brien 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> User engagement is well studied in other domains. Work to date has proposed conceptual models and definitions, approaches to measurement, and factors that influence engagement in digital interactions. However, of the articles in the visualization literature that refer to engagement, few of them make evidence-based, generalizable claims, and research that does is challenging to locate due to inconsistent reporting and often lacks connection to the broader engagement literature. To address these issues and promote the consideration of the broader engagement literature, we conduct a comprehensive scoping review of visualization literature and engagement. Using scoping review methodology, we identify and analyze 243 articles that make claims about engagement with visualizations. We coded the studies conducted, literature cited, definitions provided, and claims made in these articles and analyze the codes to evaluate the quality of the work in the field and to synthesize existing findings. We find that, despite frequent references to engagement and apparent interest in the topic, the overall quality of visualization engagement research is poor, often with weak evidence, inconsistent conceptualizations, and infrequent citation of existing models, methods, or claims. We report the evidence-based claims about what engages people with visualization, including the factors of animation, interaction, and immersion, additionally describing both corroboration and apparent contradictions between these claims. Finally, we propose the COMFI framework and mnemonic for reporting important information in future engagement studies.

---


### 391. [Can AI Reviewers See Your Efforts to Improve Your Paper? A Large-Scale Study of Paper Revision Trajectories](https://arxiv.org/abs/2611.02244)

**<font color=#1a73e8>作者：</font>** Yaochen Wang, Chenguang Wang, Ming Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI reviewers are increasingly used to assess scientific manuscripts, yet it remains unclear whether their judgments reflect the improvements authors make through revision. We investigate this question using PaperTrajectory-2026, the 2026 release of PaperTrajectory, a dataset of 6,959 paper trajectories across five AI conferences, with automatic annotations of changes along 14 dimensions and separate judgments of overall quality. The annotations show that major improvements emphasize empirical evidence and framing, while later revisions tend toward incremental improvement. Using independent assessments of manuscript versions from eight AI reviewers, we examine whether annotated major improvements receive higher scores, which revision dimensions are associated with score changes, and whether user opinions can outweigh observed revision gains. Every reviewer leaves scores unchanged on most major improvements, and agreement on the direction of score changes is weak. Revision dimensions show some reviewer-specific associations with score increases, but provide limited predictive discrimination and no consistent guide across reviewers. Even when a revision earns a higher neutral score, a brief negative user opinion can erase or reverse that advantage, with substantial variation across reviewers. These findings show that substantive revisions are not consistently reflected in review scores and that observed scoring gains can be vulnerable to user framing, motivating assessments that connect manuscript evidence to overall judgments and remain stable when no scientific evidence changes.

---


### 392. [Metamorphic Testing for Evaluating Robustness of Sentiment Analysis Models](https://arxiv.org/abs/2611.02248)

**<font color=#1a73e8>作者：</font>** Sowjanya Karanam, Jayanth Bhargav  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning systems are challenging to test using traditional software testing methods because their behavior is learned from data rather than explicitly programmed. This challenge is particularly significant in natural language processing (NLP), where small input variations can lead to unexpected model behavior. Conventional evaluation metrics, such as accuracy and F1-score, often fail to capture such inconsistencies. Metamorphic testing addresses this limitation by evaluating expected relationships between original and transformed inputs. With the increasing prevalence of generative artificial intelligence (GenAI) and language-based AI systems, the need for systematic robustness testing has become even more pronounced. Motivated by this growing need, this paper presents a lightweight, batch-based metamorphic testing approach for evaluating the robustness of such systems. In particular, we consider sentiment analysis as a representative NLP task and evaluate a pretrained classifier under four transformations: synonym replacement, typo injection, word-order variation, and negation. Using consistency score, flip accuracy, and confidence change, we identify strengths in handling semantic variations and vulnerabilities to textual noise and logical transformations. These findings highlight the value of metamorphic testing in identifying behavioral inconsistencies beyond conventional performance metrics and demonstrate its potential as a systematic framework for evaluating the robustness of language-based AI systems and guiding performance improvements before deployment.

---


### 393. [Retrain, Alert, or Rollback? A Three-Response Decision Framework for Production ML Under Concept Drift](https://arxiv.org/abs/2611.02251)

**<font color=#1a73e8>作者：</font>** Ali Sadeghian, Alireza Shafaei, Hamid Hadibeik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a deployed model degrades under concept drift, an operator can retrain it, raise an alert and monitor, or roll back. Yet most drift-adaptation methods consider only retraining. We present RAR (Retrain-Alert-Rollback), a state machine that gives each response an explicit trigger and cost. Retraining is gated on drift detection, label availability, and measured degradation. Every retrained model must pass a two-stage canary before promotion, and corruption-triggered and quality-triggered rollbacks enter different hold states. Under a prospectively specified protocol we compare RAR with six baselines, including a cost-aware retraining policy, on 13 streams: eight real public streams and five semi-synthetic streams derived from them. RAR does not dominate. At low retraining cost, retrain-heavy baselines lead, and no policy's rank differs significantly from RAR's. At higher cost, RAR beats detector-triggered retraining, periodic retraining, and no response simultaneously on four streams, each within a bounded cost window. Its advantage over detector-triggered retraining is consistent with a latency-feasibility condition stated in advance. Against the cost-aware policy, results are heterogeneous. RAR retrains before true drift onsets one eighth to one third as often as detector-triggered retraining, but at lower net utility on most semi-synthetic streams. On H2's designated corruption stream (a registered follow-up), rollbacks fire yet RAR loses to retraining baselines. At $\rho = 1$, removing the canary, and thus rollback, raises utility on 11 of 13 streams. On a post-hoc follow-up stream, cause-specific hold release resumes adaptation where a single cooldown does not. We provide the harness, configurations, and per-cell results for reproduction.

---


### 394. [Towards a Theory for the Design of Rules in Multi-Agent Systems: the case of Homogeneous Fleets](https://arxiv.org/abs/2611.02260)

**<font color=#1a73e8>作者：</font>** Matteo Penlington, Lorenzo Fiaschi, Raj Kiriti Velicheti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The regulation of systems composed of many interacting decentralised agents is a long-standing problem. This problem has typically been resolved by the imposition of rules. Rules resolve the limitations of sub-optimal agents whilst simultaneously aligning the behaviour of the agents with the demands of society. Traffic laws, for example, let a driver cross a junction without seeing around the corner, and transport protocols such as TCP let applications share a network without knowing of one another. The problem is more pressing today, as autonomous systems are deployed in society. In this work, we establish the basis of a system-agnostic theory of rule design for multi-agent systems. We first state the rule design problem (RDP) in its generality. It relates a rule to the set of system performances, defined by the regulator, that the agents deployed under it can attain. However, it is not yet possible to solve the RDP in full generality. As such, we introduce the homogeneous rule design problem (HRDP), in which the agents in each environment are identical, and among other interesting properties, show that under worst-case aggregation the two problems have the same solution, bypassing the combinatorial complexity of the RDP. To solve the RDP under worst-case aggregation we propose Rule Branch and Bound (RuleBnB), an anytime branch-and-bound algorithm. Finally, we illustrate the value of solving the RDP on an autonomous driving case study.

---


### 395. [Overcoming Demand Censoring through Randomization for Risk-Sensitive Newsvendor Learning](https://arxiv.org/abs/2611.02267)

**<font color=#1a73e8>作者：</font>** Zhengchao Wang, Nam Ho-Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online newsvendor learning with bounded demand, censored observations, and convex nonlinear shortage costs. Because stockouts can conceal the shortage magnitudes needed by gradient-based algorithms, we use randomized ordering to construct unbiased subgradient estimates. We characterize admissible randomization distributions within this framework and develop an online inventory policy that combines the resulting subgradient estimates with gradient-based updates. Our regret analysis quantifies the cost of randomization via the estimation variance and an additional loss term. We characterize the randomization distributions that minimize this objective. For piecewise-linear shortage costs, the optimal distribution is computed through a linear-time recursion; for costs with bounded curvature density, it is characterized by a scalar ordinary differential equation. The policy achieves expected regret of $O(T^{2/3})$ against the best fixed order in hindsight over $T$ periods. Under independent demand and suitable curvature of expected losses, the bound improves to $O(\sqrt{T})$. Matching minimax lower bounds establish rate optimality over the corresponding classes with a fixed marginal-cost bound. Both rates extend to nonperishable inventory under uniformly positive conditional expected demand. Numerical experiments on synthetic and retail data show improvements over alternative policies using censored observations.

---


### 396. [Hinted Scaling Laws](https://arxiv.org/abs/2611.02270)

**<font color=#1a73e8>作者：</font>** Suze van Adrichem, Luke Bailey, Rohith Kuditipudi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws predict the outcome of large, expensive training runs by extrapolating trends from smaller, cheaper runs. On downstream accuracy evaluations, these predictions fail when the weaker models produced by the cheaper runs score near zero accuracy, because these scores give no trend to extrapolate to larger scales. We introduce hinted scaling laws, which use privileged information to turn a benchmark into a continuum of easier versions so that even the small models score above zero. We find that accuracy rises smoothly and predictably with the hint level, enabling new types of scaling laws that operate below the noise threshold. On the Delphi pretraining ladder, a hinted scaling law fit on models trained with at most $10^{20}$ FLOPs forecasts the GSM8K accuracy of a $10^{23}$ FLOP model (25.9%) to within 3 percentage points; a standard scaling law under-forecasts it by 13 percentage points when fit on the same models and by 12 even with models up to $10^{22}$ FLOPs in the fit. Across both this pretraining ladder and a collection of post-trained model families, hinted scaling laws reduce the median forecasting error on GSM8K, AIME and HLE from 21 percentage points to 4.3. Hinting also reduces the number of test examples needed to tell whether one model is better than another by widening the accuracy gaps between models while approximately preserving their order: a single hinted rollout per problem ranks nearly indistinguishable models as accurately as five unhinted rollouts. Our results suggest that hinting is a general primitive for improving the accuracy and cost of downstream scaling laws and other prediction tasks in model development.

---


### 397. [Invertible Graph Aggregation Can Increase ReLU Readout Width](https://arxiv.org/abs/2611.02274)

**<font color=#1a73e8>作者：</font>** Hiroyasu Usami, Masanori Tsukamoto, Kohei Hashiguchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An invertible graph aggregation preserves the complete feature table, but can increase the size of a classifier that reads one node at a time. For every even $N\ge4$, we construct a labeled tree with $2N$ vertices and maximum degree three. A shared one-hidden-layer rectified linear unit (ReLU) classifier needs one hidden unit on the raw scalar features and exactly $N$ units after one lazy neighborhood mean. All aggregate values are distinct, and the mixing matrix has condition number at most 8. We determine the complete error curve for heads with a free affine term. The width separation persists under scalar perturbations. Under a specified bounded uniform-noise model with one nuisance coordinate, every one-unit aggregate head has expected error at least $1/12$, while a fixed $N$-unit head has zero error. Controlled fits compare trained heads with these explicit feasible scores. On Roman-empire and Tolokers, aggregation improves fitted prediction, and retaining raw features helps at the largest tested parameter budget. Training-only diagnostics include conditional output-layer optimality bounds for eight fixed runs.

---


### 398. [Data-Scarce, Multi-Granular, Multimodal: Benchmark Design for Biosynthetic Gene Clusters](https://arxiv.org/abs/2611.02275)

**<font color=#1a73e8>作者：</font>** Hanlin Xiao, Eriko Takano, Mauricio A. Álvarez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biosynthetic gene clusters (BGCs) are co-located genes that encode the biosynthesis of specialized metabolites, an important source of antibiotics, anticancer agents, immunosuppressants, and agricultural bioactives. Deep learning, particularly self-supervised foundation models, has spurred interest in BGC sequence modeling, but evaluation has lagged behind: existing benchmarks often rely on coarse classification over small curated datasets, providing limited discrimination among models and insight into downstream utility. We propose a benchmark-design framework in which an informative benchmark should be discriminative, separating models with statistical confidence, and applicable, spanning scientifically meaningful tasks under different levels of generalization. We instantiate this framework as BGC-Bench, which derives five tasks from MIBiG, ranging from A-domain substrate prediction to BGC-molecule retrieval, evaluates them under genotype- and phenotype-shift splits, includes an active-learning setting for label-scarce discovery, and is easily extensible to new tasks and encoders. BGCs further provide a shared testbed across granularities and modalities: BGC-Bench compares twelve encoders on nucleotide, amino-acid, or Pfam-domain sequences, including compositional baselines for each input type, and combines BGC and chemical encoders for cross-modal retrieval. No single representation dominates: the best granularity depends on the biological scale of the task, and pretrained encoders do not consistently outperform other representations across tasks and splits. Active-learning experiments show that most tasks remain data-limited, encoder rankings change with labeling budget, and acquisition strategies yield modest gains. These results show that BGC model evaluation requires task-diverse, shift-aware benchmarks, and the framework can be generalized to benchmark design beyond BGCs.

---


### 399. [Atom-Wise Allocation of Message-Passing Scale for Molecular Property Prediction](https://arxiv.org/abs/2611.02277)

**<font color=#1a73e8>作者：</font>** Regina Qianru Zhang, Honggang Wen, Zongru Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular properties depend on chemical structure at different ranges, from local polar groups governing solvation to extended substructures shaping bioactivity, yet graph neural networks usually fix one propagation scale for every atom. We present PRISM (Per-atom Routing over Intermediate States of Message Passing), in which each atom's encoded features produce a bounded scalar that positions a unimodal distribution over retained message-passing states and matching circular-fingerprint radii. Because one coordinate translates the whole profile, allocated depth responds to the routing scalar in closed form: at fixed temperature it is nondecreasing, its sensitivity scales with the profile variance, and it saturates in the clipped regions. Beyond providing closed-form analyzability, this constrained one-parameter profile matches or significantly outperforms parameter-matched, unconstrained node-wise gates and Jumping Knowledge attention. Under scaffold partitions with equal tuning budgets against eight graph, fingerprint, and geometric baselines, PRISM trained from scratch without three-dimensional coordinates achieves the lowest mean error on aqueous solubility and hydration free energy and strong accuracy on BACE and BBBP. As a general layer-combination rule, PRISM transfers directly to GCN, GIN, and GAT backbones, reducing hydration free energy error by up to 29% relative to last-layer readout. Applied to a pre-trained GIN, it improves on last-layer readout on four of six endpoints and gives the lowest lipophilicity error overall. In trained models, allocated depth differs systematically between atom types in a task-dependent way, and permuting profiles among a molecule's atoms raises prediction error on several endpoints, so the rule acts as a learned counterpart of atom typing.

---


### 400. [Peripheral prototypical contrastive loss for supervised medical image segmentation](https://arxiv.org/abs/2611.02305)

**<font color=#1a73e8>作者：</font>** Takuro Shimaya, Ryosaku Shino, Masahiro Saiko  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust segmentation of biomedical images remains challenging primarily due to ill-defined object boundaries. Although several loss functions have recently been proposed to enhance object boundary recognition, concerns remain about the susceptibility to unstable annotations resulting from boundary ambiguities. Here, we introduce the Peripheral Prototypical Contrastive (PPC) loss, which leverages prototypical contrastive learning to improve boundary recognition and enable stable training even under noisy annotation conditions. The PPC loss utilizes prototype features obtained from local regions near object boundaries, focusing specifically on ambiguous areas that have been challenging for existing approaches. Extensive experiments across multiple datasets demonstrated that the PPC loss consistently improve segmentation performance even under conditions with noisy labels. A newly proposed strategy, which adaptively determines the local region for prototype calculation, enhanced robustness and outperformed existing methods. Our findings indicate the potential of the PPC loss in facilitating scalable and reliable medical image segmentation, including the development of foundation models with imperfect annotations.

---


> [!TIP]
> 当前位于：**351-400**（第 8/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
