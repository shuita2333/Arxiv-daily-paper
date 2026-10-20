# 📦 其他研究 | 2026年10月21日

> 本类共 **534** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

---

### 351. [See the Future, Classify the Present: Stochastic Latent World Modeling for Hyperspectral Images](https://arxiv.org/abs/2610.25781)

**<font color=#1a73e8>作者：</font>** Muhammad Ahmad, Gemine Vivone, Ronny Hänsch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral image classification (HSIC) relies on static spatial-spectral representations learned from labeled samples, limiting its ability to model structured dependencies in the latent representation space. To address this limitation, this work proposes Stochastic Latent World Modeling (LWM), a trajectory-based representation-learning framework that enriches classification through stochastic latent-state prediction. Given a hyperspectral patch, LWM tokenizes and encodes spectral and spatial information separately using dedicated transformer branches, then fuses their outputs into a unified representation. This representation is further organized into an environment state that captures center, neighborhood, spectral, and global contextual information. A stochastic latent transition module then predicts multiple future latent states through Gaussian parameterization and reparameterization, with recurrent refinement used to model dependencies across successive states. The resulting latent trajectory is adaptively aggregated by a rollout planner to construct a planned representation, which is integrated with the base representation for final classification. By extending static spatial-spectral encoding with stochastic multi-step latent-state modeling, LWM enables the classifier to exploit structured dependencies in the representation space and provides richer features for HSIC. Across five benchmark datasets, LWM achieves overall accuracies ranging from 89.21% to 99.52%, demonstrating consistent classification performance under limited-label settings.

---


### 352. [Detection Augmented Learning In Non-Stationary Bandit Environments](https://arxiv.org/abs/2610.25782)

**<font color=#1a73e8>作者：</font>** Argyrios Gerogiannis, Yu-Han Huang, Subhonmesh Bose 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of non-stationary bandits without knowledge of the environmental changes. We propose Detection Augmented Learning (DAL) a black-box paradigm that comprises three modular components: a bandit algorithm, a change detector, and a forced exploration schedule. This modular design enables its applicability across a broad spectrum of bandit problems, from classical to highly structured settings. First, we provide theoretical insights into DAL's strong empirical performance: a single regret bound shows that DAL transfers the regret of its stationary input to the piecewise stationary setting, attaining or improving the best known bounds in every setting considered. We further identify conditions under which DAL performs well in drifting environments. Then, we showcase DAL's practical performance and versatility through extensive experimentation in which DAL consistently surpasses all state-of-the-art methods, both prior-free and prior-based, across diverse non-stationary scenarios in nine bandit settings. Finally, we investigate the effectiveness of the forced exploration and show that a bandit-driven strategy improves performance and shortens detection delay.

---


### 353. [UniJev: Separating Accuracy from Calibration in Trimodal System One Decision Models](https://arxiv.org/abs/2610.25784)

**<font color=#1a73e8>作者：</font>** Jianing Wang, Youwen Jian, Derong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> System One models produce probabilistic judgments that software can consume directly, making reliable confidence as important as answer accuracy. Yet joint training across text, images, and video remains underexplored, and the contributions of supervised fine-tuning (SFT) and reinforcement learning for calibrated decisions (RLCD) are difficult to separate. We introduce UniJev, a trimodal framework that scores candidate answers with a shared head under joint supervised training across text, images, and video. Supervised decision models improve accuracy over their backbone readouts across all three modalities, while the existing RLCD algorithms change accuracy little and have inconsistent effects on visual calibration across recipes. These findings motivate a separate supervised objective for confidence calibration. We introduce Cora (Confidence--Outcome Reliability Alignment), which groups current predictions by confidence and optimizes each prediction's confidence toward the empirical accuracy of its bin. At both 2B and 9B, Cora lowers image and video expected calibration error (ECE) while preserving accuracy, without a reinforcement stage. We release our code at this https URL.

---


### 354. [SAR: Learning Global Item-Space Matching and Geometry-Aware Placement Ranking for Buffered Online 3D Bin Packing](https://arxiv.org/abs/2610.25795)

**<font color=#1a73e8>作者：</font>** Xinpeng Lei, Jin Zhang, Yizhe Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online 3D bin packing with a bounded buffer requires irreversible item-selection and placement decisions under limited knowledge of future arrivals. Feasibility alone is insufficient, as feasible actions can produce different residual-space structures and subsequent packing opportunities. A central architectural question is how to allocate spatial reasoning between item selection and placement evaluation. We propose Spatial Affordance Retrieval (SAR), a novel learning-based framework that coordinates global item-space matching with geometry-aware placement ranking. A voxel-token spatial encoder represents 3D container occupancy, enabling a picker to match buffered items to the residual space without requiring item-specific placement proposals as inputs. After item selection, a loader ranks feasible rotation-position candidates using candidate geometry, local geometric features (LGF), and inter-candidate comparison, without directly accessing global spatial tokens. The feasible candidate set connects the two stages, which are jointly optimized under a shared long-horizon packing return. On the Random, JD, and SF datasets, the best SAR variants improve utilization over the strongest evaluated online baselines by 0.96-4.20 percentage points under the no-buffer setting (K=1). With a buffer (K=5), the best utilization rates across SAR variants reach 93.55%, 91.04%, and 90.41%, respectively. Ablations support the complementary roles of global item-space matching and geometry-aware placement evaluation, counterfactual analysis suggests that learned item selection favors greater future packing potential, and experiments demonstrate compatibility with multiple candidate generators.

---


### 355. [PQC Migration of IPsec: Reliable Composite Key Sharing Mechanisms in IKEv2](https://arxiv.org/abs/2610.25799)

**<font color=#1a73e8>作者：</font>** Rahul, Manjesh Kumar Hanawal, Sameer G. Kulkarni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The threat of quantum computers breaking classical cryptographic is accelerating the adoption of quantum- resistant cryptographic algorithms. Several government agencies have set a tight time-line for upgradation of all system to support post quantum cryptographs. We study post-quantum migration of IPSec protocols and their impact on network performance. The large key lengths in Post-Quantum Cryptography (PQC) cannot fit in a single IP packet leading to IP fragmentation. This can cause failure of security associations and degrade performance of IKEv2 under poor network conditions. To tackle this problem, we study a new key- sharing mechanism for IKEv2 and evaluate its performance. Unlike current hybrid key-sharing approaches, which send the classical and quantum keys sequentially over UDP or TCP (as in RFC 9370), the new approach concatenates them into a single composite key and transport them over TCP to ensure a reliable handshake. We implement and benchmark the new composite key-sharing handshake mechanism against existing hybrid algorithms that use either UDP or TCP. Extensive experiments under various network conditions demonstrate that the new approach significantly improves handshake time and energy consumption by avoiding the severe retransmission penalties of the Hybrid handshake mechanism. At 1% packet loss, the handshake time of composite key sharing mechanism is better by atleast 20% than hybrid mechanisms, and the improve- ment get better with higher packet loss reaching 30% at 10% packet loss. Energy consumption follows the same pattern achieving reduction of 29% at 10% packet loss

---


### 356. [Sector-Ring Linear Reservoirs: Sector-Wise Decay-Timescale Allocation With State Reuse Across Candidate Settings](https://arxiv.org/abs/2610.25806)

**<font color=#1a73e8>作者：</font>** Yudai Ebato, Sou Nobukawa, Yusuke Sakemi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In reservoir computing, performance depends on whether the fixed dynamics of the reservoir suit the task, and the appropriate memory length and frequency response differ across tasks. The reservoir settings are found by a search on each task, and driving the reservoir with the input and collecting its states for every candidate setting dominates the cost of the search. In a reservoir with a linear recurrence, the dynamics decompose into modes, one per eigenvalue, and the eigenvalue distribution becomes a design variable. We propose the Sector-Ring Linear Reservoir (SRLR), in which the eigenvalue angles are fixed at evenly spaced positions around a circle and one decay timescale, chosen from a few values, is assigned to each sector of consecutive angles. To keep the scale of each mode's state equal across candidates, the input weights are scaled using the power spectrum of the training input. To reduce the cost of the search, the states of the modes for each decay-timescale value are computed once and reused across candidates. On prediction and reconstruction benchmarks built from chaotic systems, the SRLR achieved, in all eight cases, a lower mean test error than a reference model in which all modes share one decay timescale, and was competitive with nonlinear echo state network and leaky-integrator echo state network baselines. The selected decay-timescale profiles changed with the prediction target and horizon. The state reuse reduced the number of computed mode trajectories in the search by 99.8% relative to per-candidate recomputation.

---


### 357. [Do We Need Learned Targets? Classical Gradients as Supervision for 2D Gaussian Initialization](https://arxiv.org/abs/2610.25809)

**<font color=#1a73e8>作者：</font>** Kyungjune Baek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning-based Gaussian image initializers can require costly supervision obtained by per-image optimization. We investigate whether the Pseudo-PPM targets used by Instant GaussianImage can be replaced by classical image gradients. Our framework uses normalized Sobel maps in two tracks. A training-free analytic initializer combines probability boosting, parallel grid-based sampling, and geometric processing, producing initial parameters in 0.32 seconds on average. A neural initializer is trained on DIV2K with online Sobel supervision, which removes offline target optimization and allows training to scale to 10,000 LSDIR images without additional preprocessing. Both tracks achieve competitive long-budget reconstruction on Kodak and DIV2K. Under domain shift, the DIV2K-trained neural initializer surpasses Instant-GI on Manga109 from 500 fitting iterations onward (by 1.40 dB at 5K iterations), and training on LSDIR increases this margin to 1.85 dB. On Kvasir-SEG, the training-free analytic initializer exceeds Instant-GI at every reported budget. A controlled pipeline-time comparison yields an estimated $4.9\times$ reduction for DIV2K. These results establish inexpensive analytic targets as a practical alternative to optimization-derived supervision for scalable Gaussian initialization.

---


### 358. [Hihaze: One-Step Diffusion for High-Resolution Real-World Image Dehazing](https://arxiv.org/abs/2610.25832)

**<font color=#1a73e8>作者：</font>** Zheng Chen, Yuchen Huang, Xiaoyang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently achieved encouraging results in real-world image dehazing. However, restoring high-resolution images remains challenging due to spatially non-uniform haze and inconsistent predictions across local patches. To address these issues, we propose Hihaze, a one-step diffusion framework for high-resolution real-world dehazing. Hihaze adopts two haze-aware modulation modules: attentive skip compensation (ASC) and a spatial degradation adapter (SDA). ASC selectively transfers reliable encoder information to the variational autoencoder (VAE) decoder, preserving structural details while suppressing haze-degraded features. SDA extracts multi-scale spatial degradation representations and injects them into the U-Net to guide restoration according to local haze variations. Furthermore, we design a training-free global-guided patch fusion (GPF) method. It uses a global prediction to align patch appearance and downweight unreliable predictions, followed by structure-guided detail compensation. Notably, this training-free design also makes GPF a plug-and-play module for other dehazing models. Experiments across four real-world benchmarks show that Hihaze surpasses state-of-the-art approaches in both visual quality and inference speed. Specifically, it delivers PSNR improvements of 3.62~dB on Dense-Haze and 3.69~dB on NH-HAZE compared with the strongest baselines. Code: this https URL.

---


### 359. [SWIFT: Self-guided Weak-to-strong dIFfusion models via Target extrapolation](https://arxiv.org/abs/2610.25844)

**<font color=#1a73e8>作者：</font>** Yanjin He, Cuifeng Shen, Wanzhou Lei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training high-quality diffusion models is computationally expensive, and inference-time guidance often adds further sampling cost. In this work, we introduce Swift, a simple yet effective self-guided training method that uses a frozen weak denoiser to improve a stronger model without adding inference overhead. For each noisy input, Swift extrapolates the clean regression target away from the weak denoiser's prediction, amplifying components that remain underfit. The weak guide can be an early training checkpoint, requires no backpropagation during main-model training, and is discarded afterward. The resulting model retains the original sampler and supports both conditional and unconditional generation without label dropout or an unconditional branch. We explain this mechanism through a spectral analysis of finite-time population gradient flow in an RKHS. With an early-stopped weak guide, we prove that a nonempty range of extrapolation strengths yields strictly lower posterior-mean error than matched standard training, despite shifting the regression target away from the posterior mean. Experiments on CIFAR-10 and ImageNet-256 demonstrate improvements across model scales and representations. In one ImageNet-256 configuration, Swift surpasses the baseline's best FID using roughly half the total training compute, including guide preparation and training overhead. On RAEv2, it achieves FID 1.15 without inference-time guidance and 0.99 with guidance. These results establish target extrapolation as an effective approach to weak-to-strong diffusion training with efficient single-model inference.

---


### 360. [Auditing Semantic and Relational Reliability in Open-Vocabulary Human-Object Interaction Evaluation](https://arxiv.org/abs/2610.25849)

**<font color=#1a73e8>作者：</font>** S M Asif Hossain, Ruksat Khan Shayoni, Md Kishor Morol  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary human-object interaction detectors describe interactions in free text, and this creates a problem for evaluation. Category scoring rejects valid paraphrases, while semantic similarity scoring can reward predictions that name the wrong action or reverse the roles of the participants. We present a diagnostic protocol that holds every prediction fixed and scores it under five views, namely official category evaluation, an identity control, lexical normalization, graded semantic credit, and strict propositional equivalence. Comparing these views separates the effect of the matching engine from the effect of semantic credit. The protocol pairs controlled transformations that preserve or break meaning with a blinded audit of natural predictions, and we derive consistency checks that link mean credit, invalid acceptance, and transformation counts. Applied to six systems on HICO-DET, the views disagree on which system leads. GEN-VLKT leads under official evaluation, SL-HOI leads under SHOE, and GEN-VLKT leads again under strict equivalence. Semantic gains range from 1.6 to 20.3 mAP, and AgentHOI keeps less than half of its gain once equivalence is enforced. We recommend that semantic scores be reported together with relational validity and paired uncertainty, so that recovered credit is not read as better interaction understanding.

---


### 361. [Rubrics Beyond Evaluation: Exploiting Rubric Structure in Reinforcement Learning](https://arxiv.org/abs/2610.25850)

**<font color=#1a73e8>作者：</font>** Yuxun Huang, Yunyao Zhang, ZeLiang Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubrics are widely used to evaluate open-ended question answering by breaking overall quality into explicit criteria. These explicit criteria make rubrics a rich source of learning guidance, yet their potential for guiding the training process has been largely overlooked. Existing methods use rubrics mainly as direct feedback signals, without explicitly modeling the capabilities behind their criteria. This leaves their capability structure largely unused in guiding the training process. We introduce Rubric-Structured Reinforcement Learning (RSRL), an RL framework that unlocks the full potential of rubrics by exploiting their structure throughout the training process, rather than treating them simply as direct reward signals. At its core, RSRL builds on three key designs: (1) Rubric-to-Capability Structuring first recovers the capability structure hidden in rubric criteria, (2) Self-Sufficient Capability Learning then uses this structure to bootstrap underdeveloped capabilities into effective learning, (3) Capability-Residual Credit Routing finally preserves capability-specific gains during optimization. Experiments show that RSRL consistently improves both overall performance and underdeveloped capabilities, boosting downstream scientific question-answering performance by up to 7.43 over the initial policy and 7.60 over non-rubric structured RL baselines, showing that reinforcement learning can substantially benefit from the capability structure encoded in rubrics.

---


### 362. [Arabic Financial NLP](https://arxiv.org/abs/2610.25854)

**<font color=#1a73e8>作者：</font>** Mo El-Haj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial communication connects numerical accounts of economic activity with explanations of performance, responsibility and future expectations. Arabic financial natural language processing offers methods for studying these connections across corporate reports, market disclosures, journalism and banking interactions. Its contribution to digital humanities depends on retaining the relationship between a computational representation and the document from which it was made. This chapter follows that relationship from source collection and Arabic text processing to the analysis of vocabulary, evaluation, entities, causal attribution and multilingual reporting. It then examines what financial summaries and retrieval-grounded answers preserve or lose, and how dialectal intent detection changes the perspective from institutions speaking to institutions listening. Published Arabic resources are discussed in relation to the questions they were designed to answer, with a distinction between financial pretraining corpora, annotated datasets and evaluation benchmarks. A running constructed example connects the methodological discussion without presenting illustrative analysis as empirical findings. The chapter argues for an account of Arabic financial NLP in which linguistic context, documentary provenance and interpretive judgement remain part of the evidence throughout the analytical process.

---


### 363. [Statistical Learning Theory for Direct Preference Optimization](https://arxiv.org/abs/2610.25856)

**<font color=#1a73e8>作者：</font>** Joel Wills, Yuanfan Li, Yiming Ying 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) learns from pairwise preferences through a logistic objective whose score-difference parameterization follows the Bradley--Terry model. We study how failure of this modeling assumption limits DPO, distinguishing structural misspecification from limited model capacity and finite-sample estimation. Our main contribution is a characterization of structural approximation error through the triangle-curl of the preference log-odds, which vanishes exactly when preferences admit a Bradley--Terry representation. We upper bound the achievable excess logistic risk by a score-class approximation term and a triangle-curl term, and establish a lower bound proportional to triangle-curl under additional boundedness assumptions. For ReLU score models, including clipped models, we derive explicit approximation rates showing that increasing capacity can eliminate the score-approximation term while leaving the structural obstruction unchanged. We further establish finite-sample bounds for clipped empirical risk minimizers that separate network approximation, structural misspecification, and estimation error. We place these results within a surrogate-risk framework by identifying contextual preference accuracy (CPA) as a natural measure of agreement between preference judgments and changes in pairwise probability ratios relative to the reference policy. Standard logistic consistency and calibration results connect DPO's objective to this policy property and transfer our excess-risk upper bounds to CPA, without treating CPA as a complete measure of generated-response quality.

---


### 364. [Adaptive Decoding Methods for Token-Efficient Reinforcement Learning](https://arxiv.org/abs/2610.25860)

**<font color=#1a73e8>作者：</font>** Zhaonan Li, Zelei Cheng, Amritansh Mishra 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rollout decoding affects both which trajectories are used for reinforcement learning with verifiable rewards (RLVR) and how many completion tokens are spent collecting them. We study whether candidate-token support should remain fixed or widen during training in the context of rollout sampling efficiency. Our main schedule moves from top-K=10 to K=20 and then to full support as the attempted-token budget increases. In a 4B code-RLVR setting, the schedule has a higher interpolated 150M-token validation value than its matched fixed-K=10 continuation in all three runs, with a mean gain of $1.80{\pm}0.42$ points. The schedule also performs comparably to a separately trained fixed-K=20 baseline, the strongest fixed-support setting in our sweep. Follow-up experiments suggest that late widening to full support is the most promising variant, although the evidence remains noisy, and mixed-reward-group diagnostics do not clearly explain the gain. An exploratory single-run test replay yields identical point estimates for the schedule and fixed $K=10$. Overall, our results show that rollout support is an important control for sampling efficiency in RLVR and motivate further study of adaptive support schedules.

---


### 365. [ActionRoPE: action as coordinates for spatially consistent control in planar-camera game world models](https://arxiv.org/abs/2610.25861)

**<font color=#1a73e8>作者：</font>** Zhiyang Deng, Yuzhe Wu, Zijun Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Game world models have made rapid progress toward real-time interactive generation. Yet action control is still predominantly implemented as feature conditioning, leaving the model to learn from training data how each action should move the visual world. This formulation is poorly matched to a broad class of planar-camera worlds, such as top-down and isometric games. In these worlds, player motion induces a geometrically well-defined planar camera displacement. We observe that the key to spatially consistent control in such worlds is to represent the effect of each action directly in world coordinates. To this end, we introduce ActionRoPE, a parameter-free action interface that converts action-driven camera displacement into world-coordinate rotary positions. As a result, tokens corresponding to the same world location retain the same positional address across time. These world coordinates further expose a spatial asymmetry in generation: regions covered by the initial observation are geometrically known, while newly revealed regions remain to be synthesized. We therefore propose Coordinate-Conditioned Noise Scheduling (CNS), which assigns token-wise denoising schedules according to this known-new structure. It allows observed regions to stabilize earlier, while new content is generated with reference to them. Compared with four representative action-conditioning mechanisms, our approach follows the commanded motion more faithfully and reduces the revisit drift by 66% over the strongest baseline. The same interface transfers across video backbones from 1.3B to 33B parameters and to out-of-distribution scenes. Project Page: this https URL

---


### 366. [Minimum-Cost Robust Evidence Certificates for Horn Reasoning under Correlated Source Failures](https://arxiv.org/abs/2610.25865)

**<font color=#1a73e8>作者：</font>** Yukun Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A small justification for a rule-based conclusion may disappear when a source is withdrawn, and multiple derivations need not provide independent evidence. We study minimum-cost certificates that preserve a Horn conclusion under every withdrawal of at most k source domains. Evidence records remain distinct from asserted facts, supporting replicated attestations and overlapping failure dependencies. Transversals of minimal-support footprints characterize robustness and explain why disjoint-proof requirements can reject valid certificates. An exact procedure alternates weighted evidence selection with a source-failure oracle. A rule-closed counterinterpretation yields a globally valid selection cut without enumerating supports or failure scenarios. We prove correctness, finite termination, and cost optimality, establish coNP-completeness of unrestricted verification and NP-completeness of synthesis for every fixed budget, and identify a tractable reachability restriction. Experiments on controlled benchmarks, reachability graphs, and ontology-derived instances demonstrate that our counterinterpretation-guided synthesis achieves up to 92% optimum coverage within practical resource bounds, outperforming scenario expansion and general abduction while confirming the necessity of transversal-based reasoning over proof-packing heuristics.

---


### 367. [Residual-Guided Adaptive Tucker Rank Allocation for Parameter-Efficient MCI Conversion Prediction](https://arxiv.org/abs/2610.25873)

**<font color=#1a73e8>作者：</font>** Guanghua He, Hancan Zhu, Gaohang Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Allocating limited trainable capacity across convolutional layers is a central challenge in parameter-efficient fine-tuning (PEFT) of pretrained three-dimensional (3D) networks. We propose Residual-Guided Adaptive Tucker Rank Allocation, which jointly selects input- and output-channel ranks under a fixed adapter-parameter budget while preserving the spatial kernel modes. To guide rank selection, we learn task-specific proxy updates from downstream training data and approximate them using candidate Tucker rank pairs. A perturbation analysis bounds the output discrepancy between the fixed proxy network and its Tucker approximation in terms of layerwise reconstruction residuals, motivating residual-based allocation. We normalize each squared residual by the corresponding proxy-update energy to compare relative approximation errors across layers. Dynamic programming minimizes their sum under a global budget constraint that accounts for both channel factors and the Tucker core. This yields a globally optimal allocation over the specified candidate rank pairs. We evaluate the method on the Alzheimer's Disease Neuroimaging Initiative (ADNI) cohort for predicting conversion from mild cognitive impairment to Alzheimer's disease within 36 months, using hippocampal segmentation pretraining. Across five random seeds, the proposed method achieves a mean area under the receiver operating characteristic curve (AUC) of 0.7706, compared with 0.7239 for fixed-ratio Tucker adaptation and 0.7430 for full fine-tuning. The total number of trainable parameters is limited to approximately 0.618 million, accounting for only 1.45% of the full model. Adaptive Tucker rank allocation thus provides an effective approach to parameter-efficient transfer learning in 3D medical imaging.

---


### 368. [Cling: Supporting Cross-Page Coordination with Human-Directed, In-Situ, and Small-Step Automation](https://arxiv.org/abs/2610.25879)

**<font color=#1a73e8>作者：</font>** Zhicheng Huang, Yining Cao, Haijun Xia  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Web-based information work spans independently developed pages, with goals and coordination needs often emerging through browsing. Manual coordination requires repeated low-level actions, yet explicitly specifying operations for automation can interrupt engagement with information that shapes users' next steps. Our approach constructs reusable, schema-based page representations and identifies coordination actions through correspondences across schemas. We instantiate this approach in Cling, which surfaces coordination opportunities in situ for users to select, configure, and execute incrementally while directing the broader task. A technical evaluation demonstrates accurate identification of useful opportunities across diverse domains. A 12-participant study found that Cling reduced task durations by more than half compared with both manual interaction and an end-to-end AI agent, while requiring 61% fewer clicks and 80% fewer tab switches than manual interaction. Its small-step automation supported control and verification as actions unfolded, while accommodating intent as it emerged and evolved through information encountered on the page.

---


### 369. [Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention](https://arxiv.org/abs/2610.25887)

**<font color=#1a73e8>作者：</font>** Lejia Ye, Bin Wu, Jingjing Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view novel view synthesis (NVS) is essential for AR/VR and real-time communication applications, yet remains challenging when reconstructing 3D scenes from limited viewpoints. While 3D Gaussian Splatting (3DGS) excels in dense-view scenarios, it suffers from overfitting and geometry degradation under sparse inputs. Current approaches often tackle these problems from a local perspective, addressing either data quality or training regularization individually, lacking a unified and interpretable framework for systematic improvement.
We introduce a new perspective that reframes sparse-view 3DGS from a few-shot learning viewpoint, treating each Gaussian primitive as a neuron and leveraging deep learning regularization techniques. Under this unified framework, our approach generates more effective supervision from scarce observations through two strategies: (1) data-related supervision enrichment via optical flow-guided pseudo-view synthesis and joint camera-scene optimization; and (2) training-time regularization via motion-aware dropout and early stopping, which suppress overfitting while preserving dynamic-scene stability. Extensive experiments on the SIGGRAPH Asia 2025 volumetric video challenge sparse-view dataset demonstrate significant improvements over state-of-the-art optimization-based and feed-forward baselines. Our system won first place in the sparse-view track of the SIGGRAPH Asia 2025 challenge.

---


### 370. [Motor compound fault diagnosis using an attention-based cross-talk architecture](https://arxiv.org/abs/2610.25893)

**<font color=#1a73e8>作者：</font>** Wonjun Yi, Wonho Jung, Junho Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As physical AI increasingly relies on sensing to understand physical systems, reliable condition monitoring of industrial machinery has become more important. Motors are ubiquitous in industrial systems, and increasing system complexity raises the likelihood of simultaneous faults. Accordingly, compound fault diagnosis that identifies multiple fault components and their severities is increasingly required. Because different fault components jointly affect the same vibration signal, their severity classification can be formulated as related tasks, making multi-task learning (MTL) suitable for exploiting shared information. However, conventional shared-trunk architectures force tasks to share a common representation, potentially causing negative transfer because fault components are characterized by different time-frequency regions. To address this issue, this study proposes a Residual Neural Dimension Reductor with Time-Frequency Channel Attention (RNDR-TFCA), an attention-enhanced cross-talk architecture for multi-output compound fault diagnosis. RNDR-TFCA preserves task-specific feature extractors while selectively exchanging information across tasks. Time-frequency attention emphasizes informative intra-task regions, while channel attention enhances useful inter-task information after nonlinear feature fusion. Experiments on a rotor-bearing system with inner-race fault, outer-race fault, misalignment, and unbalance showed that RNDR-TFCA achieved a macro F1 score of 0.898, outperforming single-task, multi-class, shared-trunk, and cross-talk baselines. Ablation experiments confirmed the benefit of jointly applying both attention mechanisms. RNDR-TFCA required 713 K parameters and 170.42 MMACs, only slightly higher than RNDR. Channel-expanded baselines still underperformed RNDR-TFCA, indicating that the gain was not simply attributable to increased model capacity.

---


### 371. [When Should AI Chime In? Benchmarking Timely Contribution of Proactive Agents in Multi-Party Chat](https://arxiv.org/abs/2610.25896)

**<font color=#1a73e8>作者：</font>** Ruotong Wang, Brian S. Yu, Xinyi Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proactive agents can support group collaboration by surfacing useful information without waiting to be asked, but even relevant contributions can be disruptive if poorly timed. In this work, we isolate the timing question: given a fixed candidate contribution such as a clarification or relevant fact, when should an AI agent chime in? We introduce PITCH (Proactive Intervention Timing in CHat), to our knowledge the first benchmark with large-scale human judgments of proactive agent timing collected from participants in the same unscripted multi-party conversations they took part in. To collect high-quality judgments, we design a novel interface in which 2-4 people chat synchronously, author candidate AI contribution messages, place their own and others' contributions into the chat history, and then deliberate as a group about the best placement for each message. PITCH contains 384 candidate contributions and 1,091 judgments, each marking an ideal turn, an acceptable window, or that a contribution should not appear, from 89 participants engaged in 35 conversations. Evaluating 15 models across 28 configurations, we find that while models can place contributions well when given the entire conversation history, they systematically chime in too early when asked to decide live as the conversation unfolds: best-turn accuracy falls from 57.8% to 19.0%, with nearly half of placements occurring before every participant's acceptable window. In comparison, lay humans deciding live are more accurate (23.7% vs 19.0%), and fewer of their placements are premature (39.7% vs 46.4%). Model reasoning traces show that 93% of intervention justifications cite relevance, while almost none consider waiting. By providing a human-grounded benchmark, our work reveals gaps in agents' ability to integrate into group settings and points towards proactive agents that can reason explicitly about appropriate timing.

---


### 372. [Out-of-Distribution Detection in Continual Learning](https://arxiv.org/abs/2610.25901)

**<font color=#1a73e8>作者：</font>** Nimeshika Udayangani, Flora D. Salim, Christopher Leckie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution detection in continual learning (OOD-CL) is highly challenging, as it requires (i) learning a sequence of tasks without catastrophic forgetting, and (ii) identifying unknown samples (OOD) without access to known (in-distribution (ID)) data from past tasks, where standard confidence-based OOD scores tend to degrade. Existing methods largely rely on a rehearsal buffer of past data or assume closed-world settings, limiting their scalability and reliability in real-world scenarios. In this paper, we propose a novel OOD detection framework for rehearsal-free continual learning, inspired by Kolmogorov-Arnold Networks (KAN), which mitigate catastrophic forgetting via their inherent local neuroplasticity. To better leverage KAN in OOD-CL, we introduce a task-adaptive classifier architecture, TA-KAN, which mitigates recency bias and enhances ID--OOD separability through task-specific control of activation locality. Furthermore, we propose a geometry-guided OOD score that complements TA-KAN classifier confidence without relying on past ID data. Our method significantly improves OOD detection while maintaining strong ID classification performance, achieving state-of-the-art results in OOD-CL.

---


### 373. [LEAP: Accelerating ODE-based Diffusion Sampling with Optimal Linear Leaps](https://arxiv.org/abs/2610.25918)

**<font color=#1a73e8>作者：</font>** Haowei Zheng, Zhenyu Zhou, Jiawei Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models primarily rely on general-purpose ODE-based numerical methods for training-free accelerated sampling, but performance degrades with coarse time discretization. In this paper, we propose optimal linear leaps (LEAP), a specialized method grounded in theoretical and empirical investigations of sampling trajectory geometry. Built upon low-dimensionality and cross-trajectory consistency, LEAP formulates a supervised least-squares optimization problem within the local trajectory subspace, achieving a precise approximation of future states without model evaluations. Extensive experiments demonstrate that LEAP outperforms previous methods across diverse modalities, including text-to-image (Stable Diffusion 3.5, FLUX.1-dev) and image-to-3D (TRELLIS.2) generation. Furthermore, LEAP can be seamlessly integrated into existing solver-based methods, offering a plug-and-play enhancement for modern diffusion models. Code is available at this https URL.

---


### 374. [Global probabilistic forecasting of air pollution](https://arxiv.org/abs/2610.25941)

**<font color=#1a73e8>作者：</font>** Ammar Kheder, Michael Boy, Zhi-song Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine particulate matter (PM2.5) refers to particulate matter with an aerodynamic diameter of 2.5 micrometre or less. It comes from human activities, such as traffic and industry, and from wildfires, desert dust and gases emitted by vegetation. Short-term exposure to it accounts for about a million deaths a year. Operational forecasts run on grids tens of kilometres wide, which hide the pollution breathed by nearly two hundred million people a day. Machine learning has transformed weather forecasting, but data-driven forecasts of air pollution still blur extremes and lose skill as the air travels. Here we introduce Foehn, a generative model that learns from global kilometre-scale estimates of PM2.5 and computes where the air comes from. Over a year of retrospective forecasts, it outperforms the operational forecast at three stations in four and forecasts at the scale of this hidden exposure. Its ensembles are calibrated, and their mean detects local pollution extremes four days ahead as well as the operational forecast does one day ahead. Such forecasts could warn the millions whom coarse maps miss, once kilometre-scale data are available in real time.

---


### 375. [Claim Laundering: When Agent Decision Models Trust Records Over Reality](https://arxiv.org/abs/2610.25947)

**<font color=#1a73e8>作者：</font>** Tina Khezresmaeilzadeh, Seyedarmin Azizi, Erfan Baghaei Potraghloo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent decision models select actions in a single forward pass from inputs that combine environmental observations with the agent's own record of previous actions. When an action fails silently, these sources can conflict: the record reports success, but the environment shows that the step did not take effect. We ask which source determines the next decision. Across Android screen traces, ALFWorld, and WebShop, we construct paired states that independently vary the observation, the logged action, and an explicit success claim. In all 12 configurations of four decision models and three domains, records have a larger average effect on commitment decisions than observations; after claimed-but-failed steps, the models still stop, advance, or purchase in 53-100% of cases. Yet the relevant evidence is often represented internally: linear probes on intermediate hidden states distinguish successful from failed steps on held-out apps, tasks, and goals (AUROC 0.77-1.00), and activation patching reveals increasing influence from records in later layers. We use this signal in EVIGATE, an intermediate-layer veto that requires no additional forward pass and adds 0.04-2.0% serving latency. Under injected silent failures, EVIGATE improves task success by 18.7 points in live ALFWorld agents, 5.0 in WebShop, and 5.1 in a phone simulator, and in WebShop and the simulator it also outperforms random vetoes at the same rate. Its effectiveness depends on representative calibration states: gates calibrated on offline counterfactual states do not transfer reliably to live agent trajectories.

---


### 376. [EmbodiedWorld-200K: Toward Embodied World Agents via Embodied-Planning Dataset and Interactive World Models](https://arxiv.org/abs/2610.25959)

**<font color=#1a73e8>作者：</font>** X. Feng, J. Tang, Z. Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building embodied agents that can perceive, reason, and act across diverse 3D worlds is a central research direction toward artificial general intelligence. Yet most existing work remains confined to specific tasks in a single scene and transfers poorly to new environments, leaving general embodied agents for open-world settings under-explored. We refer to such agents as Embodied World Agents (EWAs), whose defining property is the ability to understand diverse visual environments and execute general actions in open-world conditions. To advance EWA research, we study open-world embodied navigation-planning and release EmbodiedWorld-200K, a large-scale dataset of over 200K samples spanning diverse scenes. Each example is equipped with multi-level annotations, ranging from low-level camera-motion trajectories to high-level semantic instructions. The dataset also provides unified evaluation splits and task-specific metrics, supporting offline pretraining and fair evaluation of EWAs. Beyond offline supervision, a defining characteristic of an EWA is its interaction with the environment; training solely on offline data is therefore insufficient, especially for generalizing to scenes not covered in the training distribution. Building dedicated real interactive environments, however, is often prohibitively expensive. To address this, we propose a novel training scheme that employs a video world model as a low-cost environment proxy and performs interactive reinforcement-learning (RL) post-training of the EWA within it. Empirically, pretraining on EmbodiedWorld-200K substantially improves the open-world embodied planning ability of the EWA, and further RL post-training inside a world model yields clear gains on out-of-distribution scenes. The dataset, baseline checkpoints, and training and evaluation code are available at this https URL.

---


### 377. [HORIA: 4D Human and Object Reconstruction from a Monocular Video with Interaction-Aware Re-Rendering](https://arxiv.org/abs/2610.25960)

**<font color=#1a73e8>作者：</font>** Hyeongjin Nam, Taeryung Lee, Daniel Sungho Jung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint 4D reconstruction of a human and object from a monocular video is essential for understanding how people interact with their environment. While recent methods have made noticeable progress, capturing such human-object interactions remains difficult due to two main challenges. First, a video typically contains composite semantic context spanning multiple interaction phases, making it difficult to track the temporal changes of the interaction in the reconstruction. Second, under human-object occlusion, a single-view observation contains incomplete visual information about the interaction, resulting in geometrically inconsistent reconstructions. To address these challenges, we introduce HORIA, built upon two core designs. First, we decompose the entire input video into temporally grounded and semantically distinct interaction phases with motion-aware captioning, obtaining a specific text description for each phase. Second, conditioned on these text descriptions of the interaction, we propose an interaction-aware re-rendering that compensates for the limited single-view observation. Specifically, we render the initially reconstructed 4D human and object from novel viewpoints and refine the renderings with a text-to-video diffusion prior, which provides auxiliary novel-view supervision beyond single-view cues. As a result, our framework produces temporally coherent and accurate 4D reconstructions under diverse interaction scenarios, achieving state-of-the-art performance.

---


### 378. [On the Benefits of Uncertainty Estimation for Species Classification: A Case Study on Optimizing Expert re-Annotation](https://arxiv.org/abs/2610.25977)

**<font color=#1a73e8>作者：</font>** Kamenan N'Gadi, Martin Laviale, C{é}dric Pradalier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated identification of diatoms from microscopic images is a cornerstone of large-scale freshwater biomonitoring, yet the high diversity of species and strong class imbalance pose significant challenges for reliable classification. In this study, we develop a ResNet-18 baseline for a 759-class diatom dataset and investigate how calibrated confidence estimates support selective classification to reduce expert workload without sacrificing taxonomic integrity. While the initial model exhibits overconfidence with an Expected Calibration Error (ECE) of 0.117, post-hoc temperature scaling (T = 2.12) dramatically improves reliability, lowering the ECE to this http URL leveraging these calibrated probabilities within a triage framework, we demonstrate that a Selective Macro-F1 score of 99.01% can be maintained at 66.2% coverage (rejection threshold $\tau$ = 0.934). Qualitative analysis reveals that the system effectively functions as an intelligent filter, consistently deferring rare taxa-such as AAMB and AASI-and ambiguous morphologies for expert review. Our findings, supported by the torch-uncertainty framework, highlight the potential of simple calibration techniques to make automated diatom identification practical and robust, prioritizing the preservation of rare species metrics essential for ecological assessment. To support reproducibility, our code, environment specifications, and calibration results are available anonymously at https://anonymous.4open. science/r/greenprwksp-B53D/README.

---


### 379. [Graph-to-Table Interfaces Control Relational Generalisation](https://arxiv.org/abs/2610.25993)

**<font color=#1a73e8>作者：</font>** Alessandro Cagiano, Lorenzo Molfetta, Gianluca Moro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-to-table systems combine three design choices: an encoder that maps relational evidence to feature rows, a context constructor that selects labelled examples, and a tabular decoder. We investigate whether these components can be evaluated independently through matched comparisons that change one component while holding the rest of the pipeline and the evaluation constant. Across logistic regression, CATBOOST, and TABPFN-3 on CLUTRR, 57 GraphLog worlds, and 57 knowledge graphs, we show that conclusions about one component can change when the others change. On CLUTRR, absolute positional encodings maintain all distinctions among the evaluated queries and fit the short-path setting nearly perfectly; yet, they generalise worse than relation-count features because the supported prefix acts as a shortcut that breaks down on longer paths. On GraphLog, encoder preference depends on the decoder, while the relation-count representation degrades as CatBoost tree depth increases. Across different knowledge graphs, adding the frozen ULTRA score to local features is consistently useful, whereas adding local features to the score has a smaller and less stable effect. A pointwise TABPFN-3 readout using the full encoder underperforms native ULTRA on 48 of 57 datasets. These results show that encoder assessment depends jointly on context and decoder, while panel-level conclusions can also depend on evaluation and aggregation protocols.

---


### 380. [PnP-CF: A Consensus Flow-Matching Solver for General Inverse Problems](https://arxiv.org/abs/2610.26000)

**<font color=#1a73e8>作者：</font>** Dibyanshu Kumar, Magda Gregorova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Plug-and-Play (PnP) methods using continuous-time deep generative models as learned data distribution priors enable synthesizing high-quality solutions of model-based inverse problems. The quality of the solutions depends critically on the interplay and consensus between the inverse problem solver and the generative model sampler. We revisit a recently introduced flow-based PnP framework, which we refer to as PnP-CF (Consensus Flow), and extend its application to nonlinear inverse problems, including those with learned neural-network forward operators. PnP-CF combines a flow-matching denoiser with (i) ADMM-like dual variable updates and (ii) a time-adaptive pullback onto the intermediate flow probability path that combines a stochastic and a deterministic component. We discuss how these two features stabilize the algorithm and promote consensus, and demonstrate on a set of experiments that PnP-CF not only solves standard linear inverse problems with quality at least comparable to state-of-the-art baselines, but also extends gracefully to nonlinear inverse problems, including forward operators realized by pretrained neural networks, for which existing methods produce unsatisfactory results or fail completely.

---


### 381. [Curvature as a Baseline: Monocular Pose Measurement of Cylindrical Objects with Dual Colour Stripe Markers](https://arxiv.org/abs/2610.26003)

**<font color=#1a73e8>作者：</font>** Jaesung Hong, Dong Won Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thin cylindrical objects offer little space for planar markers. We propose a dual-colour-stripe marker that uses the known curvature of an object to improve pose measurement with a single camera. The boundary between two colours provides a long centre line, while dots and printed edges supply features at different depths. We analyse how this depth separation improves the estimation of rotation about the cylinder axis, or roll. For a camera-facing marker at 15 cm, the Cramér-Rao lower bound on roll standard deviation is 2.00°for a flat marker, 0.38°for a single curved marker and 0.21°for a wrap-around marker. Monte Carlo roll RMS errors are within about 10% of the corresponding standard-deviation bounds. A first-order relation connects the sagitta of the curved marker to the roll sensitivity provided by a stereo baseline. The analytical and simulation results explain how curvature improves monocular measurement and provide a basis for designing marker geometry.

---


### 382. [Scenario Generalization and Sector Transfer in Real Surface Irrigation Surrogate Modelling with Tabular Models](https://arxiv.org/abs/2610.26005)

**<font color=#1a73e8>作者：</font>** Alessandro Cagiano, M. Aybars Seyhan, Fabiola Gangi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surface irrigation planning requires screening many operating conditions and spatial configurations, while high-fidelity shallow-water-equation (SWE) simulations are expensive. We study tabular surrogate models for predicting maximum water height from drone-derived field morphology, terrain, hydrological, spatial, and scenario descriptors, where each row represents a spatial cell under one irrigation scenario. To assess deployment feasibility, we evaluate gradient-boosted trees, neural tabular models, AutoML, and tabular foundation models (TFMs) under two regimes: same-sector generalization, where a model predicts unseen scenarios after observing a limited set of configurations in the same sector, and sector-out transfer, where knowledge learned from source sectors is transferred to an unseen sector. The main findings are twofold: a) under the evaluated fixed 8/32 same-sector split, surrogates achieve strong performance, especially with raw spatial coordinates; b) sector-out transfer is substantially harder because the target sector has different coordinates and geometry. Sector-frame normalization of spatial coordinates improves transfer across similarly structured sectors, but does not solve cross-shape generalization. Overall, tabular surrogates appear useful for same-sector scenario screening under this fixed split, while robust transfer to unseen sectors remains open.

---


### 383. [ProtGlycanDock: Towards Accurate Protein-Glycan Docking with Tailored Dataset, Benchmark and Model](https://arxiv.org/abs/2610.26009)

**<font color=#1a73e8>作者：</font>** Minghao Xu, Jiaze Song, Jinyu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Performing accurate protein-glycan docking is critical to understanding protein-glycan interactions which govern many biological processes. However, this important task is hampered by the lack of tailored datasets, benchmarks and models for protein-glycan docking. To fill this blank, we first curate a standard benchmark ProtGlycanDock for training and evaluating protein-glycan docking models under both protein and glycan generalization settings. On this benchmark, we evaluate ten models in three categories, physics-based docking methods, machine-learning-based docking models and molecular structure prediction models. To obtain more precise binding poses, we further propose two finetuning techniques to inject the knowledge of glycan conformations into a general-purpose molecular structure prediction model. These two techniques respectively augment model inputs with glycan topological features and refine glycan binding pose with a glycan energy loss. Benchmark results show the superiority of AlphaFold 3 among existing methods, and the two proposed finetuning techniques can be well combined to achieve a state-of-the-art model for protein-glycan docking. Also, we perform stratified benchmark analysis and case studies to better understand the strengths and weaknesses of current models, providing insights for future model improvements. We maintain datasets at this https URL and source codes at this https URL

---


### 384. [TamedFlow: Trajectory-Aware Distillation\\for Teacher-Assisted Diffusion Sampling](https://arxiv.org/abs/2610.26025)

**<font color=#1a73e8>作者：</font>** Shuaiqi Cheng, Jiahao Zhang, Boyuan Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) deliver high-fidelity image and video generation, but inference requires many sequential model evaluations. Two acceleration strategies are increasingly important: model compression makes each evaluation cheaper, while adaptive inference avoids selected teacher computation through reuse, forecasting, or speculative execution. Their combination, however, is brittle: directly applying the evaluated adaptive methods to a compressed student can degrade quality, an observed failure mode we call the \textbf{Combination Gap}. We link this gap to a mismatch between pointwise distillation and short-horizon execution: a student trained at teacher states need not remain reliable when its own predictions are chained. We propose \textbf{TamedFlow}, which trains a compressed DiT for this deployed role through cross-architecture feature alignment, a near-identity Velocity Alignment Head, and randomized rollout supervision. At inference, a lightweight Learnable Trajectory Estimator routes completed drafts: accepted drafts bypass the teacher, while rejected drafts roll back and receive one teacher rescue step. Distilling DiT-XL/2 into DiT-B/2, TamedFlow reaches FID $2.58$ at $2.25\times$ measured speedup over DDIM-50 on ImageNet $256\times256$. Ablations support trajectory supervision, and routing controls favor LTE over random decisions at nearly matched latency. Evaluations on ImageNet $512\times512$, MS-COCO, and Latte/FaceForensics extend the empirical scope.

---


### 385. [After the Federation: Benchmarking Knowledge Portability to Heterogeneous Newcomers](https://arxiv.org/abs/2610.26026)

**<font color=#1a73e8>作者：</font>** Xinyuan Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Once historical clients become unavailable, a federation must serve newcomers through the artifact it leaves behind. How much of its knowledge remains useful in an architecture chosen afterward? We introduce FEDNBO, a seven-dataset benchmark that separates knowledge supply, policy identification, and private-model compilation under disjoint data roles. Controlled studies expose inflated oracle gains, architecture-dependent transfer reversals, and a gap between teacher accuracy and private-model utility. Ordinary public-response distillation provides a competitive reference without public task labels or newcomer samples: gains over strengthened local training are 23.52 and 16.62 percentage points on 300 CelebA identities and 300 FedEMNIST writers, respectively. In a complete-pipeline FedEMNIST comparison, this reference reaches 97.13% accuracy with 12.4 seconds of compilation per architecture, versus 97.03% and 67.5 seconds for a HeteroFedTTA reconstruction at the same epoch budget. Equal-count public-input interventions extend support sensitivity to trainable visual backbones. Together, these results establish an auditable benchmark and a strong reference for evaluating the utility, cost and reliability of post-federation knowledge transfer.

---


### 386. [Truncate or Not? A Scaling Study of Looped Transformers with Truncated Backpropagation](https://arxiv.org/abs/2610.26030)

**<font color=#1a73e8>作者：</font>** Xuyuan Xiong, Siyu Chen, Zihan Shao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers reuse a shared block of layers to increase computational depth without increasing the number of trainable parameters. They are trained with backpropagation through time (BPTT). To save training compute, BPTT is often truncated to the last few loops, although this may weaken the benefit of looping. To study this tradeoff systematically, we jointly vary model size, training tokens, and forward and backward loop counts across nearly 600 training runs and fit a unified scaling law that captures the effects of looping and truncation through effective parameters. Despite the training-compute savings of truncation, our fitted law favors full BPTT when forward and backward loop counts are jointly optimized. In matched-compute runs, full BPTT through fewer loops consistently outperforms truncated settings of the same compute. The law further shows that at fixed model size, the compute-optimal loop count and training-token budget both grow with compute. When model size is also free, the law identifies two fully trained loops as the best looped setting. Experimentally, this setting achieves lower loss than the compute-optimal non-looped model with about 27% fewer non-embedding parameters and only 8% more training compute.

---


### 387. [AVTime: Reinforcing Dense Audio-Visual Captions with Bidirectional Alignment](https://arxiv.org/abs/2610.26046)

**<font color=#1a73e8>作者：</font>** Mingyang Wu, Kaituo Feng, Bohao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense temporal audio-visual captioning is important for multimodal video understanding and generation. However, prior work is constrained by three main limitations: (1) the lack of a dataset combining high temporal resolution, longer videos, and bidirectional alignment between time and events; (2) the reliance of most existing RL methods on checklists; and (3) the lack of a benchmark that bidirectionally evaluates event semantic correctness and temporal accuracy. To address these challenges, we propose: (1) AVTime-50K, a high-quality 50K-scale dataset with temporally precise, semantically accurate captions and longer videos; (2) AVTime, a state-of-the-art model optimized with a novel Bidirectional Temporal-Semantic Alignment (BiTSA) reward that imposes explicit bidirectional constraints between time and events; and (3) AVTime-Bench, a specialized benchmark that introduces a novel bidirectional evaluation of temporal accuracy and semantic correctness. Our code, models, and datasets are available at this https URL.

---


### 388. [Learning the Dose Manifold: A Latent Diffusion Framework for Volumetric Dose Prediction in Automated Radiotherapy Treatment Planning](https://arxiv.org/abs/2610.26064)

**<font color=#1a73e8>作者：</font>** J. Boyer-Chammard, R. Vauclin, M.C. Biston 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated treatment planning (ATP) aims to reduce the unwarranted inter-planner variability of manual planning, while improving treatment quality and efficiency. Most ATP pipelines rely on the prediction of the achievable three-dimensional dose distribution for a given anatomy and the subsequent optimization of machine parameters to reproduce it. Diffusion-based methods are largely slice-wise due to the high dimensionality of radiotherapy data, and assume a one-to-one mapping between anatomy and optimal dose despite the multi-objective nature of treatment planning. They are evaluated on their ability to match reference doses and rarely on their integration in ATP frameworks. We present LaDose, a latent diffusion framework for fully volumetric dose prediction. An autoencoder learned on dose distributions, trained so that perturbed latents decode to plausible doses, compresses dose maps 128-fold and enables 3D diffusion on a single GPU. Prescription values are represented as exact scalar vectors that bypass the image encoder, avoiding resampling and latent compression. Multiscale classifier-free guidance allows for the modulation of clinical trade-offs at inference, without retraining or additional labeled data. On 900 clinically delivered head-and-neck volumetric modulated arc therapy plans from five centers, LaDose reached a median absolute error of 1.18 Gy (1.4--1.8\% of the prescription) and was the only one of six frameworks free of systematic bias with respect to the reference distribution. Guidance scales acted predictably on target coverage and organ-at-risk sparing. Integrated with direct aperture optimization, the pipeline generated plans in 15.2 minutes; in a blinded review, senior clinicians rated 14 of 15 plans acceptable without editing.

---


### 389. [PhysSkin++: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning](https://arxiv.org/abs/2610.26067)

**<font color=#1a73e8>作者：</font>** Yuanhang Lei, Baofei Liu, Xingxuan Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalizing real-time physics-based animation across diverse 3D shapes and spatial discretizations remains challenging. In this paper, we introduce PhysSkin++, a physics-informed framework that learns continuous neural skinning fields from static geometries to construct compact deformation subspaces. Specifically, we propose a Neural Skinning Fields Autoencoder that predicts shape-dependent deformation subspaces without per-object network training. To learn these subspaces without simulation trajectories, we develop a Physics-Informed Self-Supervised Learning strategy that combines skinning-field normalization with conflict-aware gradient correction, stabilizing joint optimization under physical and orthogonality constraints. The learned representation supports efficient reduced dynamics with user control and contact interactions, together with direct animation binding to meshes, point clouds, and 3D Gaussians. For prescribed rig animation, we further introduce a self-supervised complementarity objective to learn complementary elastic responses without enforcing complementarity constraints at runtime. Experiments demonstrate cross-shape generalization of the learned skinning fields, real-time reduced simulation, and applications to controllable, collision-aware, and rig-complementary animation.

---


### 390. [Risk Decomposition for Hallucination-Aware Video Sampling](https://arxiv.org/abs/2610.26069)

**<font color=#1a73e8>作者：</font>** Chenyan Zheng, Fan Wu, Ruibo Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite achieving high visual fidelity, video models still suffer from physical hallucinations, limiting their reliability as world simulators. Existing methods leverage model-internal or external signals to improve physical plausibility, but their roles and limitations require a unified explanation. We propose a two-dimensional physical-hallucination risk framework that defines low-density sampling risk and high-density drifting risk. The first risk captures generations assigned low likelihood by the video model, for example, a ball suddenly teleporting despite the model favoring continuous motion, while the second risk captures physical inconsistencies in high-likelihood generations, for example, a ball bouncing progressively higher without additional energy. Our analysis explains how model-internal signals steer sampling toward higher-density regions of the learned distribution to address low-density sampling risk. However, higher model likelihood does not guarantee physical plausibility, motivating external guidance to address high-density drifting risk. Based on this framework, we develop Hallucination-Aware Sampler (HA-Sampler), which applies external physical guidance within latent refinement to generate physically plausible videos, and HA-Scorer, which derives a likelihood-based signal from the generator itself for evaluating generated videos using continuous normalizing flow (CNF), with coarse ODE integration and finite-difference divergence estimates. Experiments on Physics-IQ and VideoPhy benchmarks support our theoretical analysis and demonstrate that our methods outperform the compared sampling and scoring SOTA baselines.

---


### 391. [Not All Similarity Is Leakage: Distribution-Aware Identity Leakage Assessment in Synthetic Face Datasets](https://arxiv.org/abs/2610.26077)

**<font color=#1a73e8>作者：</font>** Paweł Borsukiewicz, Daniele Lunghi, Wendkûuni C. Ouédraogo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic data provides the means for more ethical and less biased facial recognition. Nonetheless, the limitations of generative models and the conditioning process they rely on pose a risk of identity leakage, resulting in synthetic samples that are overly similar to those seen in a generator's training set, mitigating privacy benefits. In this work, we show that previously proposed approaches are affected by two key limitations: high classifier dependence and a tendency to identify leakage with respect to real datasets that were not used in training. To address these shortcomings, we propose a novel metric called Scaled Overlap (SO), which adapts a non-parametric data-copying test for facial recognition and extends it to the identity level. By leveraging a multi-model setup that compensates for errors in individual classifiers, it provides insights into the true strength of identity leakage. Our analysis identifies leaking datasets (CemiFace, SFace2, IDNet) with the most acute leakage introduced by generative model conditioning in CemiFace, demonstrates that real datasets do not contribute equally to generator training, and shows that the majority of synthetic images are drawn from multiple identities rather than relying on a single identity. Ultimately, our study provides new insights into the quality of synthetic datasets and gives more reliable techniques to help the community ensure the trustworthiness of synthetic data.

---


### 392. [Toolkit for Facial Deidentification](https://arxiv.org/abs/2610.26079)

**<font color=#1a73e8>作者：</font>** Esteban Leiva-Montenegro, Matthieu Pillot, Manfred Gonzalez-Hernandez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents a novel open-source toolkit designed for the evaluation of face deidentification techniques with available evaluation models. The framework provides a complete evaluation pipeline, including preprocessing, deidentification, and performance assessment, based on data utility, image quality, and identity protection metrics. It supports a variety of datasets, enabling researchers to easily benchmark new deidentification techniques. Results show the effectiveness of some techniques on maintaining privacy while preserving image utility. The toolkit is aimed at unifying future research by providing a standard evaluation framework for privacy-enhancing technologies in facial biometrics. Implementation is available at this http URL.

---


### 393. [DeOverlay: A Benchmark and Source-Anchored Flow for Video Overlay Removal](https://arxiv.org/abs/2610.26081)

**<font color=#1a73e8>作者：</font>** Deshui Miao, Yuhang Ma, Shaoyong Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video overlay removal aims to recover scenes obscured by subtitles, titles, and logos while preserving surrounding content. Existing methods use temporal propagation or source-conditioned generation, but can leave residual overlays and distort scene structure when useful source information is obscured. We propose DeOverlay, a source-anchored flow model that reconstructs the clean video from the source latent with fixed source guidance. Specifically, we train a shared velocity network along paired source-to-clean paths using region-weighted flow matching, enabling successive cor- rections from intermediate states. To select local source cues, we develop visibility-normalized temporal aggregation that excludes masked positions and averages the remaining observations. Global source context and edit-region embeddings complement these cues through additive condi- tioning, retaining a single video-token sequence. To evaluate scene recovery across diverse overlay conditions, we introduce DVTE-Bench, comprising 1,631 paired videos across eight text-overlay categories, with OCR-screened clean targets, frame-aligned pixel masks, and a common evaluation protocol. Experiments on the complete release show that DeOverlay outperforms four baselines on all five reconstruction and perceptual metrics, reducing Mask LPIPS and Mask VFID by 58.3% and 70.3%, respectively, relative to the strongest evaluated baseline. Additional qualitative examples demonstrate the removal of graphic logos and stickers. We will make the complete benchmark, evaluation code, and test outputs availabl. Project page:this https URL

---


### 394. [Context-Aware Topological Distillation Graph Network for Asymmetric EEG-Eye Movement Emotion Recognition](https://arxiv.org/abs/2610.26084)

**<font color=#1a73e8>作者：</font>** Peijun Shi, Xiujin Zhu, Zhenguo Lao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> EEG-eye movement emotion recognition can support mental-health monitoring and adaptive interfaces, but most fusion models treat the two signals as parallel features, classify each window alone and degrade when eye data are lost. We propose the Context-Aware Topological Distillation Graph Network (CTD-GNet), in which EEG features form the nodes of an electrode graph, and eye movements and preceding windows modulate its edges, nodes and readout, the edges through electrode-specific prompts. Bidirectional distillation of the graph, node relations and predictions couples this multimodal teacher with a single-window EEG student, improving the teacher and aligning the two graphs 35-fold. In leave-one-subject-out tests on SEED and SEED-IV against 17 baselines, CTD-GNet has the highest mean accuracy, 84.91% and 76.17%, significantly above 9 and 6 of 13 eye-based baselines after Holm correction, the smallest cross-subject spread among multimodal models and the highest worst-subject accuracy. It is the most accurate model at every rate of missing eye data on SEED-IV, keeps 66.1% on SEED without eye data, more than any EEG-only model, and stays 9.3 and 11.9 points above all single-window fusion models under eye-movement noise of one standard deviation. On film clips unseen in training, it leads on SEED with 77.1%.

---


### 395. [RGB--Event Object Detection Across Operating Frequencies via Reliability-Supervised Routing and Asymmetric-Resolution Fusion](https://arxiv.org/abs/2610.26090)

**<font color=#1a73e8>作者：</font>** Peijun Shi, Jiannan Zhao, Xiujin Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles must detect objects faster than a frame camera delivers images. Event cameras record brightness changes with microsecond resolution, so RGB--event detectors can decide between frames, at an operating frequency, the rate of decisions, far above the frame rate. As this rate rises, each decision receives a sparser event window, and the reliability of the events relative to the frame varies over the scene and over time. Existing detectors weight the sensors per sample and encode the frame at the reduced event resolution. Reliability-supervised routing assigns a fusion weight to every location and supervises it with targets from the losses of two single-modality classifiers used only in training, moving loss-based supervision of fusion weights from whole samples to individual locations. Asymmetric-resolution fusion lets the frame carry the decision where the events fail: it encodes the frame at native resolution and pools every feature level onto the event grid, reusing all pretrained weights. On the DSEC-Det dataset, routing halves the accuracy loss from 20 to 180 Hz, from 6.3 to 3.1 mAP, and lowers it in every seed. The resulting detector, ERA-Det, sets a new state of the art at 63.2 mAP, 3.7 mAP above FlexEvent, leads at every operating frequency, and at 180 Hz is more accurate than FlexEvent at 20 Hz. On two DAVIS346 datasets, the router lowers the frame weight at night and in low light and raises it when the events vanish. ERA-Det upgrades released FlexEvent weights in 5,000 iterations on one GPU.

---


### 396. [GeoNaviDiff: Transferring Disentangled Semantic Controls to Diffusion Features via Local Riemannian Navigation](https://arxiv.org/abs/2610.26091)

**<font color=#1a73e8>作者：</font>** Tao Sun, Huanting Guo, Baao Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Disentangled real-image manipulation requires factor-specific semantic control while preserving image fidelity and non-target content. StyleSpace $S$ provides interpretable controls but is limited by GAN inversion, whereas diffusion models offer stronger image realization without an explicit factorized control basis. We introduce GeoNaviDiff, an unsupervised cross-space framework that transfers disentangled StyleSpace interventions to local Riemannian trajectories in diffusion $h$-space. GeoNaviDiff constructs reconstruction-decoupled supervision by extracting a spherical Log-map tangent from a matched StyleGAN reconstruction-edit pair and parallel-transporting it to the real-image diffusion state. A shared, factor-conditioned Navigator predicts this tangent at inference, while norm-preserving geodesic realization and source-anchored rollout stabilize the reverse process without edited references or factor-specific models. Experiments across multiple datasets show that GeoNaviDiff outperforms the compared methods in fidelity, factor selectivity, edit locality, and trajectory smoothness.

---


### 397. [How Robust Are Prognostic Radiomic Features? Comparing Selection Techniques on Pooled Glioblastoma Cohorts](https://arxiv.org/abs/2610.26095)

**<font color=#1a73e8>作者：</font>** Yannick Sodonougbo, Marlene Schnieders, Alexia Rizoudis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiomic survival studies in glioblastoma report heterogeneous prognostic features, but how much of this stems from the methodology itself is rarely examined. We analysed the association of 463 radiomic, anatomical and clinical features from pre-treatment MRI with overall survival in 705 IDH-wildtype glioblastoma patients from three public cohorts, using three techniques: a log-rank test after median split, univariate Cox regression (both Benjamini-Hochberg corrected) and an XGBoost regressor interpreted with SHAP. The log-rank test selected 99 features, Cox regression 72 and SHAP its top 20; five were selected by all three: age, a peritumoural T2 texture feature, the number of connected peritumoural mask components and two image-level intensity maxima. The two survival tests shared 51 features, about half of the SHAP top 20 were also selected by either test, and where selections overlapped, effect directions agreed. Many selections were PyRadiomics diagnostic descriptors that are not restricted to tumour voxels. Analytical pipeline choices, including ranking method, pre-filtering and descriptor handling, can substantially influence which features appear prognostic.

---


### 398. [PnP-Transformer: A Neural Pose Solver for 6D Object Pose Estimation](https://arxiv.org/abs/2610.26096)

**<font color=#1a73e8>作者：</font>** Emirkan Burak Yilmaz, Yakup Genc  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PnP-Transformer, a neural pose solver designed as an iterative-free, differentiable alternative to classical PnP-RANSAC algorithms. PnP-Transformer regresses the 6D object pose by processing predicted semi-dense 2D-3D correspondence fields alongside confidence scores, while mapping geometric inputs into a continuous latent space. To evaluate its practical utility, we integrate PnP-Transformer into a zero-shot 6D pose estimation pipeline, where the correspondence module and pose solver are trained separately. PnP-Transformer achieves a 41.2% mean AR score with low latency (0.46 s/obj) on seven core BOP benchmark datasets, surpassing all prior baselines (such as RayPose with 39.1% AR) but one (Co-op with 58.4% AR). When the pose solver is replaced with EPnP-RANSAC (similar to Co-op) while keeping the correspondence module unchanged, the RANSAC alternative outperforms PnP-Transformer on six of the seven datasets by reaching 52.2% mean AR at a cost of an additional 60 ms per object, revealing an accuracy-latency trade-off. Code and pretrained models are available: this https URL

---


### 399. [Learning from a Bandit Learner](https://arxiv.org/abs/2610.26103)

**<font color=#1a73e8>作者：</font>** Michela Petriconi, Nicolas Menet, Claire Vernade  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical inverse bandit methods typically aim to recover true reward parameters. In contrast, we infer a demonstrator's subjective beliefs, specifically its internal estimates of suboptimality gaps. We consider no-regret demonstrators that follow randomized policies, such as Thompson sampling, and characterize a family of algorithms for which per-step inversion is possible. This enables gap estimates to be recovered directly from the arm-selection distribution. Our analysis identifies an inherent stability-coverage trade-off: inversion becomes ill-conditioned as the demonstrator concentrates its probability mass on a single arm, while the number of informative rounds depends on the rate at which its policy converges. We establish conditions under which inversion is reliable and provide theoretical guarantees on the resulting estimation error. Experiments on simulated data support the analysis and illustrate how these conditions affect gap recovery in practice.

---


### 400. [Declarative Explanations for Graph Neural Networks: A Demonstration](https://arxiv.org/abs/2610.26104)

**<font color=#1a73e8>作者：</font>** Cibo Yu, Haitong Tang, Yinghui Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have proven effective for graph analytical tasks, yet their "black-box" nature complicates the understanding of their layer-wise behavior and hinders their application to large graphs. We demonstrate SliceGXQ, an end-to-end declarative and interactive system for querying and exploring layer-wise explanations for GNNs over large-scale graphs. In particular, SliceGXQ provides (1) an interactive graphical user interface for dataset, model, and explanation configuration; (2) a lightweight SPARQL-like parser that allows users to specify target nodes, layers, explanation modes, and constraints; and (3) an integrated execution and visualization workflow that invokes SliceGX as its underlying explanation engine. We demonstrate how users can diagnose a misclassified node, identify problematic layers and influential messages, and perform targeted model debugging, together with large-scale graph interpretation and fraud-detection analysis. Our demonstration video and source code are available at this https URL.

---


> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
