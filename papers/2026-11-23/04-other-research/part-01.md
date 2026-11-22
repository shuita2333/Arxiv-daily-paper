# 📦 其他研究 | 2026年11月23日

> 本类共 **265** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-265](./part-06.md)

---

### 1. [Quantifying Cultural-Psychological Constructs in Four Centuries of Ottoman Court Registers](https://arxiv.org/abs/2611.24981)

**<font color=#1a73e8>作者：</font>** Sila Mutaf, Enes Yılandiloğlu, Mohammad Atari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Populations vary along cultural dimensions such as individualism, collectivism, and honor. But how can these dimensions be studied in historical societies for which conventional psychological data are unavailable? Here, we introduce a computational text-analytic framework for quantifying psychological constructs in 54,670 Ottoman Turkish court records from 21 Istanbul courts spanning 1513-1911 CE. We develop sentence-embedding models adapted to Ottoman legal language and extend a theory-driven, text-analytic pipeline to capture cultural variation along the dimensions of individualism, collectivism, and honor in this historical corpus. We evaluate our models through multiple methods: document retrieval, semantic textual similarity, questionnaire-item classification, and validation against expert annotations. Our adapted sentence transformer (OTA-BERTurk) achieved a Recall@1 of .843 on the test set for document retrieval, a Mean Reciprocal Rank (MRR) of .806 for semantic textual similarity (meaning the best answer usually appeared as a top result), and classified questionnaire items with 89.58\% accuracy. Document-level performance varied across constructs and methods. Qualitative analysis further showed that high scores reflected historically specific legal and institutional patterns. We publicly release the models, construct representations, scoring pipeline, as well as an interactive web interface to support transparent, reproducible historical-psychological analyses of Ottoman Turkish court records spanning approximately four centuries. These computational tools enable the study of psychological variation across centuries of cultural and institutional change in a diverse empire.

---


### 2. [Ties at the Top: A Point-in-Time Comparison of CVSS and EPSS at a Fixed Budget](https://arxiv.org/abs/2611.24983)

**<font color=#1a73e8>作者：</font>** Gianluca Martinuz, Paolo Ceravolo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Organizations must decide which vulnerabilities warrant further analysis and protective action when the volume of published vulnerabilities exceeds their analytical capacity. We present a methodology for comparing vulnerability-prioritization strategies under an explicit resource constraint, represented by a fixed number of CVEs selected from a common eligible population. We apply this methodology to the Common Vulnerability Scoring System (CVSS) and the Exploit Prediction Scoring System (EPSS). For CVEs published in the National Vulnerability Database (NVD) from 17 March to 31 December 2025 and from 1 January to 31 March 2026 (Q1), we reconstruct each CVE's scores and status 30 days after NVD publication, using archived source data. Each cohort has one ranking per strategy at a 5% budget. Positives are CVEs added to the Known Exploited Vulnerabilities (KEV) catalog within 180 days after their decision day. The catalog is maintained by the Cybersecurity and Infrastructure Security Agency (CISA). EPSS captures 16 of 40 positives in 2025, versus 5 for CVSS; alternative selections among tied CVEs cannot raise CVSS capture above 9. In Q1, CVSS captures 4 of 11 and EPSS 3, but tie-breaking can reverse this ordering. The score alone leaves most of each CVSS list undecided: the tie-breaking rule allocates 1,678 of 1,919 CVSS places in 2025 and 589 of 758 in Q1 among CVEs tied at score 9.8. Most chosen CVSS scores come from non-NVD providers; disabling those scores reduces CVSS capture from 5 to 1 in 2025 and from 4 to 0 in Q1. A fixed-budget comparison should therefore report its decision cutoff, eligible population, score provenance, and tie-breaking rule.

---


### 3. [Signed, Valid, and Unauthorized: Authority Closure at the Trust Boundary Between Agent Commerce Protocols and Crypto Wallets](https://arxiv.org/abs/2611.24989)

**<font color=#1a73e8>作者：</font>** Shengwei You, Aditya Joshi, Andrey Kuehlkamp 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent commerce protocols let software agents pay with stablecoins. A buyer approves a payee, asset, spending cap and time window, but the wallet signs an object whose effects depend on the contracts that consume it. Matching the displayed fields or simulating one payment can miss transfers that the signed object still permits. We define authority closure as the set of transfer sequences that holding the signed object can enable. A wallet object respects the mandate when every such sequence meets the buyer's constraints. We characterize when wallet objects can satisfy this property and implement Closure, a wallet-side checker covering 13 families of signed objects. In an evaluation of 2,130 generated objects and 62,979 execution programs, 265 objects with an observed violation passed both a field-and-expiry check and an address allow-list. Under the test model, Closure rejected all 1,680 objects with an observed violation and accepted the remaining 450. In two local checkouts using the x402 reference client, approved payments settled and Closure refused requests outside the mandate before signing. The median decision time was at most 12 microseconds per family.

---


### 4. [PsyWorld: Profile-Conditioned World Modeling for Human Behavior Prediction](https://arxiv.org/abs/2611.24999)

**<font color=#1a73e8>作者：</font>** Ziyuan Qin, Yang Qiao, Summer B. Frandsen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how stable psychometric traits and time-varying states jointly inform behavior is an important problem in computational behavioral science. Existing personalized agents commonly condition actions directly on a static profile, leaving realized state transitions unused as an explicit source of supervision. We introduce a profile-conditioned state world model that uses observed environment--behavior state transitions to learn transition-informed representations for behavioral prediction. During training, a posterior encoder quantizes realized transitions, while a prior predicts the resulting codes from the psychometric profile and pre-transition context. The prior code and predicted next state then condition macro-level behavior and simulator-grounded execution. Thus, the world model provides structured transition supervision instead of treating personality as a direct action descriptor. We evaluate the framework in VEET, a controlled behavioral simulator with human trajectories, and in AgentSociety as a structurally different synthetic environment. A participant-disjoint split of 240 training, 25 validation, and 48 test participants evaluates generalization to unseen people. On VEET, the model reaches 0.904 Top-1 accuracy (95\% CI: [0.895, 0.913]) and 0.0033 Macro KL. Ablations associate continuous next-state modeling with most of the Top-1 gain, while discrete codes and prior alignment mainly improve Top-3 and distributional alignment. These results establish transition-informed world-model supervision as useful for subject-generalized behavior prediction, without implying causal psychological mechanisms or calibrated long-horizon state dynamics.

---


### 5. [Density Feedback Control for Transferability of Generative Sparse Adversarial Attacks](https://arxiv.org/abs/2611.25001)

**<font color=#1a73e8>作者：</font>** Dongsu Song, Jay Hoon Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generator-based sparse adversarial attacks train encoder--decoder networks to produce transferable sparse perturbations for black-box robustness evaluation. Their perturbation density, however, is set only indirectly by a fixed sparsity coefficient whose mapping to density is unknown and shifts during training, so reaching a target density requires re-tuning; this fixed pressure also yields little transferability gain once density reduction begins. We propose Density Feedback Control (DFC), which tightens or relaxes this coefficient at the end of each epoch according to the gap between the observed hard-mask density and the target, without changing the generator architecture or loss. At a 10\% target density, DFC brings the mean density of three base attacks within one percentage point of the target in a single run and improves the transfer attack success rate (ASR) of two of them on CNN and Transformer targets, including under per-image $\ell_0$ budgets, while perturbing fewer pixels. Tracing GPG's training, we observe that as DFC relaxes the coefficient, the transfer ASR recovers with the density and overtakes the fixed-coefficient baseline with fewer pixels. For EGS-TSSA, which restricts perturbations to source-model feature-importance regions, DFC yields no consistent gain; we analyze how this restriction interacts with density feedback.

---


### 6. [On the Impact of Feature Reduction Techniques on Adversarial Attacks](https://arxiv.org/abs/2611.25004)

**<font color=#1a73e8>作者：</font>** Mohammad Meymani, Roozbeh Razavi-Far  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks have posed significant threats to machine learning models by exploiting their inherent vulnerabilities. Researchers have established an interdisciplinary field called adversarial machine learning to explore these vulnerabilities and develop corresponding defense strategies. Feature reduction strategies are used to decrease the dimensionality of the data in order to reduce training time, avoid the curse of dimensionality, prevent overfitting, and mitigate redundant features. However, their effect on adversarial robustness across different classifiers and attack scenarios remains insufficiently explored. This study aims to analyze the effect of feature reduction techniques on the adversarial robustness of a diverse set of machine learning models under poisoning, backdoor, and universal adversarial perturbation attacks on the APT dataset. These models include support vector machine, decision tree, random forest, multi-layer perceptron, and k-nearest neighbors. The attained results are compared with scenarios where different feature reduction techniques are applied, including principal component analysis, permutation importance ranking, recursive feature elimination, and univariate mutual information. Metrics such as accuracy, F1-score, and mitigation score are employed to evaluate the effect of these techniques on adversarial robustness. The results demonstrate that permutation importance ranking and univariate mutual information generally provide the most consistent robustness improvements, while other methods exhibit more variable effects depending on the classifier and attack scenario.

---


### 7. [Near-Quadratic Sample Compression for All VC Classes](https://arxiv.org/abs/2611.25011)

**<font color=#1a73e8>作者：</font>** Yang Cai, Vineet Gupta, Yanchen Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The sample compression conjecture is a longstanding open problem in learning theory, originating in the work of Littlestone and Warmuth in the 1980s. At its heart is a connection between simplification and generalization: if a predictor consistent with a training sample is defined using only a small part of that sample, then it is likely to generalize. Sample compression schemes formalize this idea, and many natural learning algorithms can be analyzed this way.
The sample compression conjecture of Floyd and Warmuth (1995) asserts that every binary concept class of VC dimension $d$ admits a sample compression scheme of size $O(d)$; a weaker conjecture asks only for size polynomial in $d$. Both have remained open: the first bound depending only on $d$, due to Moran and Yehudayoff (2016), is exponential in $d$. We prove the weaker conjecture by constructing a sample compression scheme of size $O(d^2 \log^2 d)$.

---


### 8. [Closing the Analyze-to-Design Gap: An Authorization-Bounded Agent for Self-Driving Laboratories](https://arxiv.org/abs/2611.25043)

**<font color=#1a73e8>作者：</font>** Yimeng Liu, Eric Isbrandt, Felix Katzenburg 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) agents are increasingly integrated into self-driving laboratories (SDLs) to plan experiments and interpret results. However, analytical reasoning alone does not make a laboratory autonomous: autonomy in an SDL is achievable only when the agent can be trusted to act on physical hardware unsupervised and knows when to defer to a human. Here, we present an architecture that integrates an agent at the Analyze-Design interface of the Design-Make-Test-Analyze (DMTA) cycle, enabling agent-driven measurement selection and data interpretation while ensuring that state-changing operations are authorized, validated, and auditable. We demonstrate this architecture on a liquid chromatography-mass spectrometry (LC-MS) instrument in an oxidant-screening campaign for synthesizing an organic dye. Within human-defined campaign limits, the agent submitted measurement jobs, interpreted mass spectrometry (MS) and diode-array detection (DAD) data, flagged failed experiments, and produced an oxidant ranking. This ranking matched that obtained from scripted peak integration, and organic chemists confirmed the agent's spectral interpretations and failure assignments. In a simulated environment that replays the archived LC-MS data, where the agent chose which wells to inject under varying injection limits, it measured the highest-yielding condition at about its seventh injection, against 14.5 on average for a random order, and identified it in every campaign with a limit of eight or more injections. An agent can therefore close the analysis-to-design gap while its actions stay bounded and verifiable, which is a step toward greater autonomy for SDLs.

---


### 9. [Infer3D: Inverse Generative Modeling Enables Robust 3D Reconstruction](https://arxiv.org/abs/2611.25061)

**<font color=#1a73e8>作者：</font>** Amani Kiruga, Mark Hamilton, Joshua B. Tenenbaum 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans can understand the 3D structure of scenes even from highly unfamiliar or extreme viewpoints. Cognitive science suggests this generalization stems from a top-down generative inference strategy. In contrast, state-of-the-art 3D reconstruction neural networks typically rely on amortized, feedforward inference. While fast, this pattern-matching approach degrades when faced with out-of-distribution (OOD) scene conditions unseen during training. Inspired by the generative nature of human vision, we propose Infer3D, an inverse generative modeling framework that recovers the latent variables of a generative model to best match the monocular input. To prevent degenerate flat outputs, we couple the generative image prior with a frozen 3D lifting network that constrains the optimization space to a valid, multi-view-consistent 3D manifold. Across a variety of controlled synthetic and real-world tasks, Infer3D demonstrates superior OOD reconstruction accuracy compared to feedforward networks trained on equal or larger datasets. Furthermore, mirroring how human perception requires more time to process confusing stimuli, we introduce an adaptive inference strategy that expends more test-time compute on ambiguous OOD examples while efficiently routing in-distribution inputs. Project website: this https URL

---


### 10. [A Human-Centric Adaptive Multi-Fidelity Digital Twin Framework for Cyber-Physical Systems](https://arxiv.org/abs/2611.25082)

**<font color=#1a73e8>作者：</font>** Clarisa Grijalva-Lugo, Yu-Zheng Lin, Shalaka Satam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital twins of cyber-physical systems must operate with scarce data, on assets that change after deployment, and for humans whose needs differ, yet existing implementations fix fidelity at design time and do not match the representation to the human or the task. This paper proposes a human-centric adaptive multi-fidelity digital twin framework that models the evolving human, the physical twin, and the digital twin core, and adds a human inference and adaptation function that estimates the human state, predicts the response, and adapts the representation. The framework defines low-, medium-, and high-fidelity tiers distinguished by adaptivity and by coupling, quantified as the ratio of the digital twin latency to the duration of the process step it follows. Three proof-of-concept instantiations are evaluated: a virtual reality tutor, a computer numerical control milling model, and an industrial training station. The low tier estimated learner sentiment with an accuracy of 0.86. The forecasters of the milling model and the training station, both medium-tier, showed a normalized error decline of 0.39 to 0.89 and a human adaptation gain of 1.16 to 1.51, but their latency exceeded the physical process step by 25 to 87 times. Only the station's vision model met the physical step. The tiers are separated by which functions adapt and where the latency constraint lies, not by a monotone increase in gain or coupling.

---


### 11. [Long-Range Video Presentation Attack Detection: A Three-Class Benchmark Across 1-100 m and Two Sensor Types](https://arxiv.org/abs/2611.25108)

**<font color=#1a73e8>作者：</font>** Lambert Igene, Mohammad Zahir Uddin Chowdhury, Afzal Hossain 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Face presentation attack detection (PAD) systems deployed in border control and airport surveillance are constrained by a critical assumption: subjects are captured at close range, typically under one meter. No existing benchmark systematically addresses multi-distance capture, diverse environmental conditions, and concurrent spoofing and occlusion-based attacks, leaving deployed models underprepared for real-world scenarios. We introduce a video-based PAD dataset of 374,000+ frames from 261 unique identities collected across five standoff distances (1 m-100 m) under indoor and outdoor conditions using a DSLR camera (C) and a mobile sensor (M), with three-class labels: live, spoof, and props (occlusions); models are trained and evaluated on video clips rather than single frames. We fine-tune and benchmark four CNN architectures: MobileNetV3, MobileNet, EfficientNet, and ResNet-50. The higher-resolution DSLR maintains near-perfect spoof classification rate across all distances, while the lower-resolution mobile sensor degrades sharply beyond 50 m, with props classification rate dropping to 55% at 75 m for MobileNetV3. EfficientNet achieves the best overall performance (98.48% accuracy, ACER 2.01%). Generalization tests on unseen attack datasets yield 89-94% accuracy, validating cross-domain robustness. These results establish capture distance and sensor resolution as critical but underexplored axes of PAD difficulty. The dataset will be publicly released under an End-User License Agreement to support reproducible long-range PAD research.

---


### 12. [Do Deep Stereo Models Learn Shape Priors?](https://arxiv.org/abs/2611.25113)

**<font color=#1a73e8>作者：</font>** Linbo Tang, Aneel Damaraju, Todd Zickler  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Localizing object boundaries is important for embodied visual systems, since small boundary errors can change the inferred geometry of physical surfaces. We study whether deep stereo models produce boundaries consistent with simple shape priors when local image and disparity cues are weak. We create a synthetic stereo dataset consisting of objects drawn from a highly constrained family of shapes, with randomized depth, slant, color and texture. Despite the simplicity of this shape space, we find that several state-of-the-art stereo models retain systematic boundary errors, even when finetuned or trained from scratch on the dataset. We then introduce a simple generative stereo model that jointly predicts disparity and a distance field representing object boundaries. The model improves boundary localization and produces contours that adhere more closely to the underlying shape space. These results expose limitations in the boundary predictions of current stereo architectures when local evidence is weak, and motivate further study of whether generative models can better combine regional grouping evidence with global geometric structure.

---


### 13. [Fast and Memory-Light Evaluation of Density-Based Clusterings with the DISCO Index in R](https://arxiv.org/abs/2611.25114)

**<font color=#1a73e8>作者：</font>** Amin Entezari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> DISCO is a recent internal cluster validity index for density-based clustering that, unlike earlier indices, also evaluates the quality of noise labels. The discoCVI package makes DISCO available in R. This article describes the design of the package and a typical workflow, in which DISCO is used to compare clusterings and to choose the parameters of HDBSCAN without ground truth, followed by the implementation introduced in version 0.2.0. DISCO is defined through density-connectivity distances between all pairs of points, so direct implementations store several n-by-n matrices. We show that every quantity DISCO needs can be read off the single-linkage merge tree of the mutual-reachability minimum spanning tree, so that the index can be computed exactly with memory that grows linearly with the number of points, while the running time remains quadratic as in the original definition. The implementation is tested against the previous version, agrees with the original Python implementation to within $3 \times 10^{-13}$, and corrects the score of singleton clusters to match the published definition. In benchmarks, discoCVI is 23 to 138 times faster than its previous version for 500 to 4,000 points and 3 to 9 times faster than the Python reference for 500 to 8,000 points, using a fraction of the memory of both, and it scores 100,000 points in about 50 seconds with less than 200 MB of memory.

---


### 14. [Auditing Learned Dynamics in Weather Models](https://arxiv.org/abs/2611.25119)

**<font color=#1a73e8>作者：</font>** Skylar Gu, Christina Last  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned weather models are experimentally accessible computational systems whose internal representations can be inspected and manipulated. Using sparse autoencoder features from GraphCast, DeepMind's autoregressive weather forecasting model, we test whether causal relevance requires physical semantics, a question that matters for auditing whether AI forecasters used in high-assurance settings rely on reliable mechanisms. We also look at whether physically associated latent directions can be steered to improve extreme-event forecasts, where interventions are applied to the model's internal activations during the rollout. We find that ablating a feature locked to GraphCast's computational mesh increases global geopotential height error despite lacking conventional physical semantics. Second, suppressing convection- and low-level-vorticity-associated features weakens predicted tropical-cyclone deepening (the fall in central pressure during intensification), while amplifying them reduces intensity error, with amplification of convection features through feature scaling achieving a median of 51\% error reduction over seven storms. Together, these results separate interpretable, physical association from causal utility and establish sparse features as experimental coordinates for auditing and intervening on learned weather dynamics.

---


### 15. [TALD: Transferability-Aware Logit Disentanglement for Cross-Modal Knowledge Distillation](https://arxiv.org/abs/2611.25126)

**<font color=#1a73e8>作者：</font>** Hui Li, Pengfei Yang, Xinyi Feng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal knowledge distillation can incur negative transfer when source-modality supervision conflicts with the target modality's discriminative characteristics. We propose TALD, a two-stage framework for Transferability-Aware Logit Disentanglement in class-aligned logit space. Guided by task-dependent self-benefiting and cross-modal exclusivity criteria, a Residual Disentangler decomposes logits from a teacher and an independently trained target-modality reference student into modality-general and modality-specific components. A Sample-Adaptive Modulator regulates decomposition constraints and sample-specific fusion weights. The learned modality-general components are then adaptively fused to supervise the final student. Across five benchmarks spanning vision, audio, and text, TALD achieves the largest mean accuracy gain and highest positive-transfer frequency among the compared methods. Across ten transfer directions with five runs each, TALD improves over training without distillation in 84% of evaluations, compared with at most 70% for the baselines, while offering a favorable accuracy-efficiency trade-off. We plan to release the code.

---


### 16. [Temporal Extrapolation of Elastic Seismic Wave Propagation in Layered Media Using Neural Operators](https://arxiv.org/abs/2611.25130)

**<font color=#1a73e8>作者：</font>** Dibyajyoti Nayak, Yuze Pu, Kami Mohammadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal prediction of seismic velocity fields beyond the time interval represented in training remains challenging for neural operator models. This study develops a coupled neural operator framework for stress-conditioned temporal prediction in layered elastic media. A time-integrator-embedded Deep Operator Network (TI-DeepONet) advances the velocity field through an embedded fourth-order Runge-Kutta (RK4) scheme, while a Fourier Neural Operator (FNO) learns a residual correction to the predicted spatial field. The two components are trained jointly in a predictor-corrector configuration. Prediction is initialized with reference velocity fields at the first two time levels and proceeds autoregressively, with reference stress fields and prescribed excitation supplied throughout rollout, including beyond the training interval. Four cases consider horizontally polarized shear (SH) waves in four-layer soil columns with fixed total depths of 50 and 280 m, excited by third-order Gaussian-derivative (DOG3) wavelets with central frequencies between 0.5 and 6 Hz. Layer thicknesses and shear-wave velocities vary across profiles. Evaluations on test profiles extend beyond the training interval by up to twice its duration. The predictions reproduce principal velocity arrivals and depth-dependent response patterns, with accuracy varying across profiles. Across the four cases, mean peak-normalized root-mean-square errors (NRMSEs) range from 0.53% to 2.31% over the full evaluation windows and from 0.61% to 2.82% over the extrapolation intervals. Both metrics use each profile's peak absolute reference velocity over the full evaluation window as the normalizer. These results demonstrate temporal velocity prediction under reference-stress conditioning for the tested configurations; autonomous continuation of the coupled velocity-stress wavefield remains to be established.

---


### 17. [Mutable State in Enrich-by-Need Security Protocol Analysis](https://arxiv.org/abs/2611.25142)

**<font color=#1a73e8>作者：</font>** Joshua D Guttman, Paul D Rowe, Eben Blaisdell  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security protocol analysis has emphasized message-passing, as this is how different principals interact in authentication, key exchange, and similar functionalities. However, in many protocols a principal also maintains mutable state that limits what actions its local sessions may take; this cross-session state is altered by other local sessions.
In this paper we show how to represent this cross-session mutable state in the strand space approach to symbolic protocol analysis, and how to implement the resulting ideas in the Cryptographic Protocol Shapes Analyzer CPSA. The key theory is expressed in two axioms characterizing state, plus protocol-specific rules. It leads to tight, specific characterizations of protocol behavior in relevant cases, and aids in developing correct protocols relying on cross-session mutable state.

---


### 18. [Bayesian $κ$-Explorer for Minimax Model Estimation in MDPs](https://arxiv.org/abs/2611.25160)

**<font color=#1a73e8>作者：</font>** Xihe Gu, Urbashi Mitra, Tara Javidi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study active exploration for minimax transition estimation in unknown Markov decision processes (MDPs). Frequentist $\kappa$-Explorer~\citep{gu2026kappa} addresses this problem through a parameterized family of exploration objectives, but requires confidence-bound constructions and joint optimization over plausible transition kernels and occupancy measures, introducing a computational burden that limits its practical applicability. We develop Bayesian $\kappa$-Explorer, which simplifies this procedure by placing Dirichlet priors on the transition distributions. Under the posterior mean estimator, the posterior expected squared $\ell_2$ error equals the total posterior variance, providing a closed-form exploration signal. The algorithm plans under the posterior mean model, eliminating confidence-set optimization. Under the stated assumptions, this simpler planning procedure retains the $\widetilde{O}(T^{-1/3})$ surrogate convergence rate of frequentist $\kappa$-Explorer. We further bound the maximum posterior variance relative to the optimal asymptotic minimax allocation benchmark. Experiments on Pendulum, Mountain Car, and Taxi demonstrate lower worst-case transition-estimation errors than the tested baselines.

---


### 19. [CoRelate: Coordinated Human-Object Motion Synthesis through Interaction Relations](https://arxiv.org/abs/2611.25166)

**<font color=#1a73e8>作者：</font>** Zhiwen Qiu, Daisy Lin, Diyu Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-object motion synthesis requires coordinated human participation as objects move toward specified goals. However, reaching object targets does not ensure that contact is established and maintained, while adjustments that improve contact may interfere with task completion. We introduce CoRelate, a diffusion framework that coordinates full-body human-object motion through explicit interaction relations and task feedback for rigid and articulated objects. We represent intended participation through hand-part relations that specify the participating hand, its part-relative reference position, and participation interval. These relations serve both as generation conditions and as references for measuring interaction realization. At each denoising step, a temporal refiner trained jointly with the generator combines relation deviations, task residuals, and motion features from the current prediction to jointly update human and object motion across the sequence. After generation, temporal motion correction addresses remaining contact failures by optimizing local motion segments while preserving object trajectories and protected human motion. Experiments demonstrate improved object-goal satisfaction, contact F1, and complete interaction success over the evaluated baselines. Ablation studies support the benefits of relation conditioning and the complementary roles of task and relation feedback.

---


### 20. [Game-Theoretic Data Allocation for Expert Specialization and Routing](https://arxiv.org/abs/2611.25167)

**<font color=#1a73e8>作者：</font>** Mark Lovett, Denis Lim, Soroush Vosoughi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can the allocation used to train experts also predict which expert will perform best on a prompt? Such a connection would make the intended division of labor inspectable before training and allow the allocation itself to guide inference. We introduce InflEns, a mixture of LoRA experts whose training weights and inference routes come from the same location game in a fixed prompt-trait space. Players choose positions to maximize their expected shares of the prompt distribution, without using expert losses. We utilize the game's kernel-general theoretical criterion for when co-located positions become locally unstable to separation. We evaluate InflEns on a corpus assembled from seven safety-related benchmarks, which demonstrates that the highest-share expert has the lowest held-out response negative log-likelihood (NLL) on approximately 90% of prompts across four kernels under a sharpened simplex representation, compared with approximately 15% after permuting allocations across prompts. We demonstrate that the method performs comparably to published learned gates without having to train an explicit gate on the experts. Because the router is fixed, we can trace harmful behavior to a single expert and retrain only that expert, which lowers HarmBench attack success from 0.51 to 0.02 while keeping instruction following. The game also gives us several controls over how the experts specialize, including the kernel choice and its parameters, the trait-space geometry, and the number of experts. Importantly, InflEns is a general framework that can be extended to any encoder and data distribution.

---


### 21. [What a Calibrated Probability Hides: Belief-Level Post-Training for Decision Models](https://arxiv.org/abs/2611.25168)

**<font color=#1a73e8>作者：</font>** Xinye Li, Zirui Song, Huaxing Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A calibrated decision model can predict how often each answer is chosen. The same prediction can reflect disagreement among people who are confident in their choices or uncertainty among people who share a belief. Disagreement calls for identifying whose perspective applies, while uncertainty calls for gathering more evidence. Standard post-training scores a single prediction against one observed choice at a time, learning the pooled distribution without distinguishing these two sources of uncertainty. We introduce Belief-Grouped Policy Optimization (BGPO). The policy proposes a list of beliefs, estimates their prevalence, and predicts a choice distribution for each. During training, BGPO uses Bayes' rule to estimate how likely each belief was to generate an observed choice. These estimates weight the choice's contribution to each belief's log-score reward. To discover rare beliefs, the policy also proposes lists after seeing a few observed choices and retains them only if they predict held-out choices well. At inference, the policy uses only the question and combines the belief-specific distributions by prevalence to produce a calibrated aggregate prediction. On benchmarks covering opinions, conversation safety, emotions elicited by artwork, and photo aesthetics, BGPO achieves the lowest conditional, worst-group, and overall Jensen-Shannon divergence across model initializations. It improves conditional divergence on both text and image tasks. On a synthetic image task with known beliefs, BGPO recovers the underlying groups more accurately than baselines trained with belief labels.

---


### 22. [Open Response Explorer: a Structured Collaborative Writing System for Peer-Informed Open-Response Assignments](https://arxiv.org/abs/2611.25169)

**<font color=#1a73e8>作者：</font>** Ziwei Gu, Ruixuan Chen, Elena Glassman  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Peer-informed open-response assignments (where students view, connect, and learn from peer contributions) hold the potential to foster collaborative knowledge building, yet the unstructured nature of free-form prose prevents students from effectively comparing and making sense of peers' work. We present Open Response Explorer, an interface that recenters open responses on structured idea units through purpose-based writing and peer response exploration, augmented by common-role text segment highlighting for easy comparison. A within-subjects lab study (N=12) validated the usefulness and usability of the system, demonstrating how it shaped the open-response drafting and peer exploration practices. We discuss implications for purpose-centered authoring and exploration that transform free-form prose into structured, comparable, and collectively navigable knowledge artifacts.

---


### 23. [MV-JEPA: Post-Training Video Encoders for Cross-View Understanding](https://arxiv.org/abs/2611.25172)

**<font color=#1a73e8>作者：</font>** Yangchen Zhao, Ali Payani, Caiwen Ding  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> JEPA-based video encoders learn strong representations for video and image understanding through prediction in latent space. However, their standard pretraining predicts features within individual images or video clips, without explicitly exploiting paired camera views of the same object or moment. Consequently, the learned representations may not reliably support matching across different camera viewpoints. To solve this problem, we introduce multi-view predictive post-training to strengthen cross-view instance and temporal correspondence while retaining independent single-view inference. A shared encoder processes masked context views independently, and a training-time predictor jointly predicts latent tokens for masked context regions and a fully held-out view. We alternate cross-view prediction with single-view masked prediction on general image and video data to help retain the encoder's pretrained capabilities. After only 9,000 post-training updates on a single GPU, MV-JEPA improves cross-view instance retrieval and coarse cross-camera moment retrieval on various datasets, with further gains in zero-shot action-phase retrieval and frozen-feature classification on AE2. Frozen-probe evaluations further indicate that post-training largely preserves motion recognition, image recognition, and dense semantic segmentation performance on the evaluated benchmarks. Together, these results demonstrate that multi-view predictive post-training can strengthen instance and coarse temporal correspondence in JEPA video encoders without modifying the encoder architecture or single-view inference interface.

---


### 24. [PDE-State Conditioning for Learned Optimization Using Physics-Informed Neural Networks](https://arxiv.org/abs/2611.25185)

**<font color=#1a73e8>作者：</font>** Farzana Yasmin, Ricardo Vilalta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural network (PINN) optimization depends on global properties of the underlying PDE and how the physics residual evolves across the domain. Standard optimizers such as Adam use fixed gradient-based statistics, while learned PINN optimizers replace the fixed rule with a learned update built from local parameters and optimization-history features. However, none explicitly use PDE-level information. We study two coupled design questions: what PDE-level information should a learned optimizer observe, and how should that information influence its update? We introduce an 11-dimensional PDE state-capturing operator structure, residual geometry, and short-horizon update response, and use it to condition a structured meta-learned optimizer through bounded feature-wise modulation. Repeated design studies identify the compact residual-geometry state G2 and bounded FiLM as the strongest overall choices among those tested. The resulting PDE-State-conditioned optimizer improves all evaluation metrics (relative-L2, L1, solution MSE, and physics MSE) over Adam and the unconditioned learned optimizer on Linear Advection, KdV, and Burgers.

---


### 25. [User Perceptions of Deceptive In-Vehicle Infotainment User Interfaces](https://arxiv.org/abs/2611.25195)

**<font color=#1a73e8>作者：</font>** Pedram MohajerAnsari, Iwinosa Aideyan, Anna Galeano 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern vehicles collect extensive data about drivers, passengers, and vehicle use, with privacy and consent decisions increasingly mediated through infotainment software. Although dark patterns have been widely studied in web, mobile, and e-commerce interfaces, little is known about how they appear in automotive infotainment systems or how users perceive them. We study this problem through Android Automotive OS (AAOS), conducting a three-phase empirical analysis. First, 26 HCI and privacy annotators audit four OEM AAOS emulators (Honda, Volvo, GM, and Polestar), documenting 17 dark-pattern types across 65 observations. Second, a user study with 100 participants compares OEM-specific implementations of five dark patterns across GMC, Honda, and Volvo, finding that implementation choices affect user perceptions. Third, an independent study with 49 participants compares automotive and e-commerce dark-pattern clips before and after a brief tutorial, showing that automotive's initial rating advantage largely collapses after instruction. Together, the studies identify a sophistication paradox: subtler dark patterns are less likely to trigger user suspicion and may therefore be harder to identify. These findings indicate that oversight should evaluate not just the presence but also the specific implementation of dark patterns.

---


### 26. [Identity World Model: Recognizing People in an Imagined Latent World](https://arxiv.org/abs/2611.25204)

**<font color=#1a73e8>作者：</font>** Dingqiang Ye, Kartik Narayan, Vishal M. Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-body human recognition has advanced rapidly with large vision models. However, existing methods remain fragile under real-world variations, as they tie identity to transient cues such as clothing, texture, pose, or viewpoint. We argue that a robust recognizer should not merely learn to ignore these cues, but imagine how a person would be represented if they changed. To this end, we propose IDWorld, an identity world model: just as a latent world model predicts the features of a scene after an action, IDWorld predicts how a person would be represented under a changed condition. In a single forward pass, IDWorld imagines these counterfactual features under shared canonical conditions, such as the same outfit, a fixed view, or a bare silhouette, without rendering any pixels. Compared with explicit imagination in pixels, this latent imagination keeps nearly the same accuracy while being over 11x faster, at 5.9 ms per frame. Since each imagined condition has its own strengths, IDWorld then fuses them adaptively, weighting each condition for every probe-gallery pair. Extensive experiments show that IDWorld achieves state-of-the-art results on CCPG and CCGR-MINI, outperforms the compared methods on MEVID, and generalizes best to CASIA-B* and SUSTech1K, with the best mAP on CCVID. These results suggest identity world models offer a simple yet effective path to robust recognition. Code will be released.

---


### 27. [ϕTD: Distributional Reinforcement Learning using Characteristic Functions](https://arxiv.org/abs/2611.25208)

**<font color=#1a73e8>作者：</font>** Thomas Mousseau, Tyler Kastner, Davide Baldelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributional Reinforcement Learning methods aim to learn the entire distribution of returns, yet current algorithmic approaches are limited to a narrow class of distributions. We propose $\varphi$TD, a method to overcome this limitation by computing the loss in the frequency domain. We demonstrate that this further unifies quantile and categorical approaches to distributional RL, and enables the learning of distributions that were previously impossible to capture, such as mixtures of continuous distributions. We empirically study $\varphi$TD, across synthetic benchmarks and large-scale deep RL environments and demonstrate that the flexibility obtained from wider parametric families can lead to improved performance.

---


### 28. [Reject and Report: Forgery-Evident Undetectable Watermarks for Generative Image Models](https://arxiv.org/abs/2611.25226)

**<font color=#1a73e8>作者：</font>** Yihan Wang, Haochen Sun, Xi He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Provenance schemes such as those based on content watermarks let images from a generative model be traced back to it. A practical watermarking scheme must be accurate at a low false-positive rate (FPR), robust under content-preserving processing, and undetectable. In addition, it must resist forgery; otherwise, even from a single watermarked image and a surrogate model, an adversary can imprint the watermark onto an arbitrary image or regenerate new content that carries it, falsely attributing harmful content to a model or making authentic photographs appear AI-generated. We argue that a watermarking scheme should not only reject forgeries but also report them: a forgery rejected as unwatermarked leaves no trace of the attempt. State-of-the-art forgery-resilient undetectable watermarking schemes, such as SemBind, fall short on both counts. External anomaly detectors that do report forgeries either miss most of them or falsely flag genuine images after common processing. We propose Tripwire-WM, the first forgery-evident framework for undetectable watermarks. It commits the semantics of the generated image to the magnitudes of the initial latent noise, which the sign-based watermarks leave unused, through a distribution-preserving embedding; a forged image carries a valid watermark but with a commitment that does not match its content, so the detector both rejects it and reports it as forged. Built on the pseudorandom code (PRC) watermark and Gaussian Shading++, Tripwire-WM provably preserves their undetectability. On MS-COCO, with the owner's own model as the surrogate, it accepts no imprinting forgery, compared with up to 55.0% for SemBind, and reports all of them as forged; it also accepts at most 1.8% of reprompting forgeries, against up to 46.2% for SemBind. Meanwhile, it accepts at least 99% of genuine watermarked images at 10^{-6} FPR and matches the robustness of the base schemes.

---


### 29. [Release-Bound Withdrawal Authorization for Bitcoin Custody](https://arxiv.org/abs/2611.25231)

**<font color=#1a73e8>作者：</font>** Jian Cui, Rui Zhu, Haixu Tang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A compromised cryptocurrency withdrawal backend can request signatures on unauthorized payments. Previously signed transactions may remain spendable after pause or become spendable again after a reorganization. Release-Bound Withdrawal Authorization (RBWA) orders permits against pause in a replicated journal and restores exposure when its closing evidence disappears from Bitcoin's active chain. An optional route delays large payouts and permits independent cold recovery. Direct payments confirm in one block on regtest, and staged payments confirm in three or seven at delays of two or six. After rollback, a replayed recovery can win or lose to an already exported mature payout. Authenticated receipts can revoke one signing lease in a shared wallet. In matched synthetic schedules, probes reduce permits through compromised leases from 20 to 9 out of 33, with one false fence. Two held-out HTTP workloads find equal fixed-threshold precision for boosted audit and probe-augmented detectors. The audit fields already expose the probe authentication outcome. Live tests verify an exact maintenance exception and add a file marker as a distinct source. The marker fences a compromised lease that RPC-only audit misses. Audit with the same file-read evidence also fences a reader who bypasses the probe. The results tie the benefit of active probing to which evidence the operator can obtain.

---


### 30. [Beyond Restoration: Content-Degradation Factor Unfolding for Real-World Concealed Object Segmentation](https://arxiv.org/abs/2611.25239)

**<font color=#1a73e8>作者：</font>** Rihan Zhang, Fengyang Xiao, Yuhan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable visual perception under degradation requires distinguishing task-relevant content from degradation-induced variations, especially in concealed object segmentation (COS), where foreground cues are inherently weak. The central challenge is not merely improving visibility, but identifying reliable content evidence amid degradation-induced variations. RGB-space segmentation often entangles content and degradation cues, while restoration-based methods primarily focus on image recovery and task interaction. This motivates explicit factorization to distinguish content evidence from degradation effects and assess its reliability. Retinex provides a spatially aligned basis for this separation but remains illumination-centric. We therefore extend it to content-degradation formation with task-asymmetric factor roles. The Factor Unfolding Network (FUN) uses the content factor R as the sole source of direct semantic evidence for segmentation, while the degradation factor L captures degradation-related variations and generates a spatial reliability map to calibrate this evidence. A unified energy couples observation formation with reliability-weighted foreground-background separation, and its alternating updates yield a coarse-to-fine network without clean-image supervision. In this way, FUN factorizes degradation for perception rather than removing it. Extensive experiments across clean and degraded conditions and diverse segmentation tasks demonstrate robust performance and generalization. Code will be released.

---


### 31. [Towards Restorative Urban Spaces: An Exploratory Field Study of Nature Videos on Public Multi-Display Signage](https://arxiv.org/abs/2611.25259)

**<font color=#1a73e8>作者：</font>** Yuri Mikawa, Takumi Yokosaka, Yuki Kubota 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In recent years, multi-display signage (MDS) has become increasingly common in urban stations, plazas, and other public spaces, where it is primarily used to present advertisements and information. Beyond these conventional applications, MDS offers opportunities to shape people's experiences of public environments through spatially distributed and dynamic visual content. Motivated by the potential of mediated nature to support restorative experiences in urban environments, we conducted a nine-day exploratory field study in a free-admission area of a science museum, presenting artificial intelligence (AI)-generated nature videos across four displays and collecting 1,263 questionnaire responses. We combined three complementary analyses. First, structural equation modeling identified strong associations among perceived consistency across displays, presence, and self-reported restorative responses, consistent with our theoretically motivated model. Second, exploratory comparisons across video-presentation configurations revealed modest differences in consistency and restoration ratings, although these AI-generated videos did not significantly outperform the advertisement reference. Third, qualitative analysis of open-ended responses identified fascination, immersion, and restorative feelings, alongside concerns about naturalness, visual quality, and motion-related discomfort. Together, these findings provide empirical insights into MDS-mediated nature experiences, with implications for nature-video design and questionnaire refinement. They also inform a tentative conceptual extension of the model incorporating additional perceptual and evaluative factors.

---


### 32. [Design and Evaluation of a Body-Machine Interface as an Alternative Control Paradigm for Pedal-based Sewing Machines](https://arxiv.org/abs/2611.25261)

**<font color=#1a73e8>作者：</font>** Ashrut Aryal, Rajiv Ranganathan, Ranjan Mukherjee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Body-machine interfaces (BoMIs) exploit body movements to control assistive devices; they have been evaluated primarily in tasks such as cursor control or robotic manipulation where the entire movement repertoire is devoted toward device control. However, tasks with multiple concurrent processes require the user to share the movement repertoire used for device control with other body movements for task execution. This issue is examined here in the context of sewing, where the sewing machine is typically controlled by a pedal in coordination with hand movements for guiding the fabric. We evaluated the learning of a trunk-controlled BoMI for sewing machine control, and compared it with conventional pedal control. Twenty-four novice participants (12 BoMI, 12 Pedal) completed 10 trials of a standardized sewing assessment followed by 3 trials of a transfer task. The BoMI mapped trunk movements to the sewing machine's full functional repertoire, which included continuous speed control of the needle, and discrete actions such as presser-foot and needle lifts. The two groups learned at comparable rates, showing similar completion times and error counts; for both groups, completion time reduced by approximately 30\%. Additional analyses showed that the BoMI group had fewer presser-foot lift errors during training and fewer errors on the first transfer trial. Both groups also exhibited similar subjective workload. These findings collectively demonstrate that a BoMI interface can support sewing-machine control during concurrent manual activity, highlighting the potential for using BoMIs for increasing accessibility in industrial workplace contexts.

---


### 33. [Process-Knowledge-Guided Latent Diffusion for Generative Design of Porous Architectures: A Case Study in Aerosol Jet Printing](https://arxiv.org/abs/2611.25264)

**<font color=#1a73e8>作者：</font>** Ngoc Dang Khoa Nguyen, Hyunwoong Ko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Printed porous layouts interleave functional material with open channels, and the layout that uses the material best depends on how the process settings shape the deposit. Generative models propose layouts quickly, but a generator that does not receive the process setting samples from the same distribution at every setting, even when the process-dependent score ranks candidate layouts differently. This paper examines whether process knowledge can steer a latent diffusion generator toward layouts suited to a given process setting in a prescribed design domain. We formulate a process-dependent utilization score in which a process model sets the length over which the utility of printed material decays with distance from a channel. The generator combines a vector-quantized variational autoencoder (VQ-VAE) latent representation, a topology U-Net, a ControlNet domain branch, and a separately trained regressor that predicts the score from noised latents; the domain branch conditions each denoising step and the regressor gradient steers it. The method is applied to aerosol jet printing, where the atomizer and sheath gas flows enter the score through the flow-focusing relation. Across seven modeled flow settings, the lowest-scoring candidate layout of a domain differed between settings in 191 of 500 domains. In a sampling study, the mean directly computed score on three validation domains and one test domain was 0.642 with domain conditioning alone, 0.636 at a weight of 300, and 0.450 at 12,000 (112 scores per weight; lower is better). The results support process-knowledge-guided generation as an approach to process-specific porous design under the stated assumptions.

---


### 34. [Real Cameras are Radiometric](https://arxiv.org/abs/2611.25265)

**<font color=#1a73e8>作者：</font>** Ties Harder, Felix Seegräber, David Nakath 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose the radiometric camera, a model that lifts any central geometric camera model to a radiometric one. The lifted model keeps the projection of the geometric model and adds a finite aperture, a free-form focus surface and a generic vignetting function. We calibrate it by inverse rendering directly on the relative irradiance of the sensor, from the same images of standard calibration targets used in geometric calibration. Geometric calibration absorbs the bias of its feature detections. The proposed radiometric calibration uses no features, and our radiometric cameras have lower reprojection errors on held-out test sets. The focus surface extends defocus modeling from the thin lens to any central camera, and we use it in a first multi-view radiometric reconstruction, which recovers the in-focus reflectance of a texture from defocused images. The vignetting is estimated jointly and accurately reproduces a flat field measured through a diffuser. Because every standard camera model lifts to a radiometric one, the radiometric camera naturally and directly extends generative scene models beyond multi-view geometry to multi-view radiometric ones, where phenomena such as lighting and attenuation can be accurately estimated.

---


### 35. [Learning to Verify: Signature-Guided Training for Adaptive Adversarial Detection](https://arxiv.org/abs/2611.25271)

**<font color=#1a73e8>作者：</font>** Arash Vashagh, Roozbeh Razavi-Far  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial example detectors often fail when attackers explicitly attempt to bypass them. We propose a dual-model approach that keeps the original classifier fixed and trains a separate verifier to assess its predictions. During training, we identify patterns of internal neural network activations that distinguish genuine examples of each class from adversarial examples targeting that class. These patterns, called activation signatures, guide the generation of challenging adversarial examples that mislead the classifier, challenge the verifier, and internally resemble the target class. The verifier learns to recognize these examples while preserving its performance on clean inputs through knowledge distillation. At inference, the verifier evaluates the classifier's prediction without requiring activation signatures. We evaluate the approach on publicly available datasets against several adaptive attacks, including attacks unseen during training. The proposed verifier substantially outperforms directly attacked confidence-based and feature-based detectors under the evaluated L-infinity attacks. Ablation studies show that adaptive verifier training is the main source of this improvement, while signature guidance primarily benefits clean accuracy. Additional L2 evaluations reveal limitations in robustness across perturbation types.

---


### 36. [TRACE-5G: Trust-Aware Runtime Attestation and Continuous Enforcement for 5G User Equipment](https://arxiv.org/abs/2611.25272)

**<font color=#1a73e8>作者：</font>** Al Nahian Bin Emran, Rajendra Paudyal, Rajendra Upadhyay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The standard 5G Authentication and Key Agreement protocol (5G-AKA) authenticates subscriber credentials but does not verify the integrity of user equipment (UE). Existing literature includes admission-time device-certificate authentication and Trusted Platform Module (TPM)-based measured-boot attestation, which can additionally verify that the UE presents enrolled device credentials and boots into an approved state. However, these checks do not reveal whether harmful unauthorized software is executed after admission. We present TRACE-5G, which continuously verifies the UE's runtime software state and uses the resulting trust state to control network access. TRACE-5G retains the pre-admission certificate and boot checks, and in addition places the admitted UE in restricted connectivity while runtime integrity is verified. Linux Integrity Measurement Architecture (IMA) records runtime software measurements, TPM PCR (Platform Configuration Register) cryptographically accumulates them, and Keylime, a remote-attestation framework, repeatedly evaluates TPM and IMA evidence against enrolled references. A Trusted result grants full access on the existing PDU session, but an Untrusted result withholds or removes full access and causes network deregistration. We implement TRACE-5G on an srsRAN/Open5GS testbed with a hardware TPM2.0 UE and core-side firewall enforcement. Across ten trusted trials, Level 2 access was established in 9--12s. Across ten untrusted trials, promotion was consistently withheld; in a representative trace, restrictive policy was applied within 5ms of the Untrusted decision and UE-context release completed within 1.670s. TRACE-5G extends UE trust beyond admission without any modification of the standardized 5G protocols.

---


### 37. [Scone: Symmetry-aware Neural Combinatorial Optimization for Graph Coloring](https://arxiv.org/abs/2611.25273)

**<font color=#1a73e8>作者：</font>** Paolo Pellizzoni, Melanie Weber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph coloring, which entails assigning colors to nodes such that no adjacent nodes have the same color, is a fundamental combinatorial optimization problem. In general, however, finding a node coloring with no monochromatic edges given a fixed palette is NP-hard. This motivates learning-based methods that can learn to exploit recurring structure across instances to efficiently produce high-quality colorings. Crucially, the validity of a coloring is invariant to permutations of the colors, and we show that exploiting this symmetry reduces the size of the effective state space over which the model has to learn its policy. At the same time, the coloring algorithm must be able to break some symmetries, for example to assign different colors to two adjacent nodes belonging to the same automorphism orbit. In this paper, we introduce Scone, a model that uses a color-equivariant graph neural network to construct colorings sequentially, allowing information from previous assignments to propagate and break node symmetries. Scone achieves perfect solution quality with low inference times across several graph coloring tasks, including on sudoku_extreme and register allocations, and showcases generalization to graph families not encountered during training.

---


### 38. [DS3M: Deep structured state space models for nonlinear system identification on modern hardware](https://arxiv.org/abs/2611.25274)

**<font color=#1a73e8>作者：</font>** Marco Roschkowski, Hannes Gernandt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural state-space identification learns dynamical models from measured inputs and outputs. SUBNET combines this task with an encoder that estimates initial states from short measurement histories. Its continuous-time version requires many successive neural-network evaluations during numerical integration, resulting in slow training speed which is a major limitation for practical use cases. We propose deep structured state space models (DS3M), which combine compact nonlinear dynamical components in parallel and in series. Custom GPU kernels implemented with Triton reduce the launch and memory overhead of their sequential evaluation. We explain this construction, describe a port-Hamiltonian variant, and present various benchmark comparisons of accuracy and training time.

---


### 39. [Accord: Universal Online Metric Localization and Dense Mapping from one Camera and an IMU](https://arxiv.org/abs/2611.25279)

**<font color=#1a73e8>作者：</font>** Jaafar Mahmoud, Arthur Movsesyan, Cuong Huynh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense metric mapping from a single camera and IMU remains challenging: visual-inertial odometry (VIO) provides metric motion but sparse geometry, whereas feed-forward depth models predict dense structure without ensuring metric scale. We present Accord, which constructs an accurate online dense metric map from any camera with an IMU. A VIO filter publishes metric poses, a depth foundation model conditioned on them predicts depth for short keyframe windows, and a factor graph fuses the resulting submaps. Recent work has explored several approaches to this problem. What is essential is the multi-view agreement (Accord), which is considered in SLAM as a source of geometric self-consistency. Accord anchors each keyframe window to metric 3D points triangulated from the filter poses, then exploits bidirectional dense depth agreement between co-visible images to estimate and correct per-image scale errors while preserving the metric scale established by the anchors. Context keyframes further improve depth prediction, and the resulting submaps are fused in a factor graph. We evaluate a single mapping configuration across five public camera-IMU setups and a new Phone-rig/GoPro dataset. With nothing tuned per dataset/setup and every map aligned only by Accord's own trajectory, Accord achieves consistently best/second-best mean F-score at 5 cm on every platform. Accord is open-source along with the phone-rig dataset for the benefit of the research community

---


### 40. [MS-Point: Multi-Modal Hierarchical Spectral Learning for Point Cloud Understanding](https://arxiv.org/abs/2611.25282)

**<font color=#1a73e8>作者：</font>** Hai-tao Yu, Jun Xia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Point-image alignment learns useful object representations, but different local feature patterns can produce the same pooled descriptor and receive the same alignment signal. We introduce MS-Point, a cross-modal pretraining framework that directly supervises intermediate point features and their neighborhood responses. At selected encoder stages, we compute neighborhood averages and residuals before pooling and align their branch descriptors with image features. Branch-level objectives align each representation with its visual target, while cross-level consistency and adaptive fusion coordinate information across branches. A common interface of intermediate features and spatial neighborhoods supports both graph encoders and point Transformers. Evaluations across object classification, few-shot adaptation, dense prediction, and low-label scene learning demonstrate the transfer value of this design. Same-backbone comparisons and capacity-matched and computation-matched controls connect these improvements to the structure of supervision. Together, our findings support directly supervising intermediate features and neighborhood variation to learn transferable, geometry-aware representations across modalities.

---


### 41. [Persistent Identity in Person Tracking: Online Enrollment and Registered Recognition](https://arxiv.org/abs/2611.25283)

**<font color=#1a73e8>作者：</font>** Ratha Siv, Matei Mancas, Bernard Gosselin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We extend PoseTReID with online appearance-bank matching (Gallery) and a residual-conflict guard for registered SVM recognition. All methods use supplied ground-truth (GT) person boxes. We average all-box assessment IDF1/HOTA equally across videos. On six SportsMOT clips, StrongSORT leads standalone trackers (79.44/84.72%) and exceeds both Gallery variants. Over eleven videos, Gallery AIN (83.29/85.44%) and COPE (84.66/86.38%) exceed standalone trackers with complete results. This lead depends on two retrospectively added GTA development compilations and is absent on the original nine videos. Registered SVMs lead both cohorts among complete results, with AIN at 95.72/94.82% over eleven videos. They use every GT crop from approximately 20% of frames, including future appearances. On MOT20-03, registered AIN reached 96.80% IDF1 and assigned the correct enrolled name to 90.72% of assessment GT observations. Gallery and standalone trackers receive no per-video labelled enrollment. Both identity routes restore identities across internal title cards, but Gallery trails SORT on three videos (four in HOTA) and both SVMs trail SORT on MOT16-04/MOT20-03. Under six-clip persistent-only scoring, native Gallery gains 2.39 percentage points in mean IDF1 over a matched control, with lower correct-P coverage and 5.02 times as many encoder attempts. Pose gating is mixed; the guard's metric effect is not isolated.

---


### 42. [Intelligent Embedding Pruning for Large-Scale Recommendation Models](https://arxiv.org/abs/2611.25288)

**<font color=#1a73e8>作者：</font>** Anish Khazane, Alex Saad-Falcon, Guanchu Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern recommendation systems face substantial memory pressure, largely from the sparse embedding layer that maps high-cardinality categorical features into dense vectors. In-training embedding pruning (ITEP) removes less important embedding rows during training, yielding end-to-end memory savings but sometimes degrading accuracy because per-table pruning ratios are set by size-based heuristics. We use feature importance (FI) to guide these ratios (FI-ITEP), assigning higher pruning to tables tied to less important features. Across three large-scale recommendation models, FI-ITEP achieves 20--40% total memory reduction while matching or improving accuracy relative to percentile-based ITEP. Because the feature-importance signal requires minimal resources to compute, these memory savings translate into concrete systems benefits: the same models train on fewer GPU trainers (e.g., 112 to 80) with higher per-GPU throughput, saving 1,000+ GPU-hours per model launch. We reproduce these trends on the open-source DLRM (Criteo 1TB) and quantify the end-to-end training-time and GPU-cost tradeoff---including the burden of computing FI---offering practical guidance for embedding pruning in real-world systems.

---


### 43. [Modeling Learner-Technology Interaction Through Multilevel Gaze Transition Dynamics to Inform Usability in Online Learning](https://arxiv.org/abs/2611.25294)

**<font color=#1a73e8>作者：</font>** Yueqi Weng, Jie "Jennifer" Lu, fan Yang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Gaze data provide fine-grained evidence of how learners engage with instructional content and interface elements, complementing conventional usability evaluation methods. However, eye-tracking analyses often examine within-slide visual attention and across-slide navigation separately, limiting understanding of learner interaction throughout extended learning experiences. This exploratory multi-method study integrated area-of-interest transitions, gaze entropy, slide-level navigation, and network-based representations to analyze seven eye-tracking recordings of high school students interacting with an AI-supported online biology lesson, complemented by three post-intervention focus groups. Results showed individual differences in within-slide gaze allocation and switching patterns. Learners followed shared navigation pathways but differed in revisiting and immediate return behaviors. The focus group findings highlighted positive perceptions of interactive materials and AI-generated feedback, alongside usability concerns related to navigation, interface clarity, and assessment guidance. Together, these outcomes show how integrating multilevel gaze analytics with learner perspectives can provide complementary evidence for identifying interaction trends relevant to usability evaluation. Future research should test this approach with larger, more diverse samples and examine relationships among gaze patterns, usability, and learning outcomes.

---


### 44. [Federated Learning of Car Aerodynamics Surrogates with Spectral Optimizers](https://arxiv.org/abs/2611.25300)

**<font color=#1a73e8>作者：</font>** Arman Bolatov, Nikolay Spitsyn, Daniil Medyakov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural surrogates predict the aerodynamic forces on a car in seconds, compared with hours for a CFD simulation, but training them requires thousands of CFD simulations of different car designs, which car manufacturers keep proprietary. Federated learning allows several manufacturers to train a shared surrogate without exchanging data. We study which federated optimizer brings such a surrogate closest to one trained on pooled data. On DrivAerNet++, we train a Transolver surrogate across six clients that each hold cars of a single body type, and we compare three spectral optimizers, which orthogonalize the update of each weight matrix (FedMuon and two methods we propose, FedMARS-M and FedOLion), with three non-spectral ones (FedAvg, SCAFFOLD-Adam and FedLion), all tuned with the same protocol. FedMuon and FedMARS-M reach a drag error within 2% of centralized training with Muon, using two to four local epochs per round. The non-spectral methods perform best with sixteen local epochs, the largest number we tested, and still have a 17 to 37% higher drag error than FedMARS-M. We relate this gap to the low stable rank of the weight gradients, for which an orthogonalized step yields about twice the first-order decrease of a gradient step of the same spectral norm. Code: this https URL

---


### 45. [SplitReAlign: Partition-Aware Representation Realignment for Split Federated Unlearning](https://arxiv.org/abs/2611.25301)

**<font color=#1a73e8>作者：</font>** Jia Chen, Yecheng Lv, Xinrong Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split federated learning (SFL) distributes neural networks across clients and a server, coupling class-specific knowledge across their representations. This coupling complicates split federated unlearning (SFU), where class-wise forgetting must remove target knowledge while preserving retained utility under heterogeneous representation spaces and asymmetric update constraints. We propose SplitReAlign, a partition-aware representation realignment framework for class-wise SFU. It constructs endpoint-specific discriminative subspaces coordinated through a shared semantic anchor, selectively realigning forgotten representations while penalizing changes outside the active subspaces. To accommodate asymmetric update constraints, SplitReAlign leverages gradients through frozen servers for Client-only updates and fixed client-feature statistics for Server-only guidance, while Joint updates optimize both partitions. Experiments on CIFAR-10 and CIFAR-100 under heterogeneous client distributions demonstrate that SplitReAlign achieves the lowest average gap to retraining among all compared methods across six settings. Notably, Server-only achieves the closest agreement with retraining on both datasets, highlighting the effectiveness of partition-aware guidance under restricted updates.

---


### 46. [Prescribed Bayesian Efficiency under Lifetime Adjustment Costs](https://arxiv.org/abs/2611.25311)

**<font color=#1a73e8>作者：</font>** Viet Bac Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A Bayesian learner may retain an issued action while updating its posterior, trading predictive loss against adjustment charges. We assume population curvature, boundary control, an order-$1/n$ lower bound on expected posterior uncertainty about the optimal action, and an observable unbiased gradient witness whose squared norms are uniformly integrable. Sample losses may be unbounded or nonconvex. Cumulative expected excess measures the loss increase relative to current predictive Bayes actions. For bounded nonnegative nondecreasing charges $c$ with $c(0)=0$ and nondecreasing profiles $G: \mathbb{N} \to [1,\infty)$ with $G(J)=o(J)$, we characterize joint attainability of cumulative expected excess $O(G(J))$ at horizons $T=2^J$ and finite expected lifetime charge. Here $J$ indexes logarithmic time. The criterion is finiteness of a prefix-constrained allocation of tracking-error allowances across action-distance scales, equivalently its decreasing-weight dual. Adaptive timing and private randomization do not enlarge the attainable region. For each feasible pair, a horizon-independent deterministic checkpoint policy attains the profile with lifetime-cost moments of every positive order. For excess $O((\log T)^r)$, $0<r<1$, every policy needs $\Omega((\log T)^{2-r})$ revisions in expectation, and a charge-independent schedule achieves a matching pathwise upper bound for every feasible charge. We verify the assumptions for logistic decision models with nondegenerate covariates, finite second moments and a locally positive smooth prior density, including fixed-ridge models with unbounded parameter priors.

---


### 47. [When Should Deployed BCI Decoders Adapt? A Resource-Priced Ladder for Frozen EEG Trunks](https://arxiv.org/abs/2611.25315)

**<font color=#1a73e8>作者：</font>** Sergey Musienko  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When should a deployed MI decoder spend adaptation resources-not only how to adapt under shift? We study a thin control layer outside a frozen encoder: a resource ladder (factory -> Bayesian head -> affine map, with full fine-tune as an escape hatch) governed by regime-aware gating under a utility that prices accuracy, fit time, and label cost. The head is Bayesian in the conjugate sense: a Normal-Inverse-Wishart prior over the class conditional Gaussians in embedding space, updated in closed form (no gradients) as labelled trials arrive. Full estimators, constants, and the reanalysis code are in the companion paper and the ancillary bundle of this submission. Thesis: adaptation should be gated and capped, not always-on and not blindly fine-tuned. Evidence: (i) utility-max gating over-adapts on clean data that already carries session drift; a clean-referenced gate restores low false-entry rates (e.g. dropping the adaptation rate from 0.56 to 0.11 on field-like sessions, with the cascade staying on the factory decoder for ~87% of clean cells). (ii) Under severe synthetic stress, a lightweight LDA head matches or exceeds the frozen trunk's accuracy across five encoder architectures (n=155 subject x trunk cells, pooled across shared subjects), at ~23x lower fit time than full warm-start fine-tuning. Always-on baselines favor capping the default below full fine-tune. (iii) In two no-perturbation BNCI session checks the factory model transferred without intervention (no reliable head gain), so the control layer's value under natural drift is cost-efficiency and clean-safety rather than demonstrated accuracy gains. (iv) Adaptation severity does not follow a universal ordinal ladder across datasets, highlighting the need for dynamic gating over fixed adaptation policies.

---


### 48. [Improving Imitation Policies for Multi-Phase Tasks through Residual Learning Allocation](https://arxiv.org/abs/2611.25320)

**<font color=#1a73e8>作者：</font>** Clinton Enwerem, Saleh Kemal, John S. Baras 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual reinforcement learning corrects an imitation-trained base policy using a limited budget of environment interaction. In a task with several phases, this budget must be divided among the phases, and the phase in which the base policy fails is not necessarily the phase in which a correction most improves task completion. We formalize this distinction through the completion gain: the change in full-task completion probability when, during a single phase, a state-feedback controller replaces selected components of the base policy's action. We decompose the completion gain into the probability of reaching the phase and the conditional improvement in completion from the start of the phase, and we estimate it from paired episodes. The positive estimates determine which action components the residual policy corrects and how training episodes are distributed across phases. In stochastic point-mass docking experiments, most failures occurred in the final docking phase, whereas the largest completion gain occurred in the preceding channel phase; gain-based allocation improved completion over allocation proportional to failure counts and, in a variant with a longer approach, over uniform allocation at half of the budget. In simulated bimanual robotic assembly, the completion-gain estimates were positive only for insertion and release, although few failures occurred during release; in a second assembly configuration, a residual policy trained in the release phase improved completion from held-out states at the start of release by 16.9%.

---


### 49. [Now You See Me Now You Don't: A Framework To Detect and Reduce Proxy Capacity](https://arxiv.org/abs/2611.25327)

**<font color=#1a73e8>作者：</font>** Nirek Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In regulated domains such as lending, the two most salient fairness concepts are disparate impact and disparate treatment: disparate impact is generally defined by differential rates of adverse outcomes between demographic groups, while disparate treatment is generally defined by the use of demographic information or proxies to issue decisions. There already exist established methods to quantitatively detect and mitigate disparate impact; however, there has been less research on doing the same for disparate treatment. From a practitioner's perspective, the manner in which a conditional independence test is formulated and operationalized to identify proxies is nuanced and underexplored. As Machine Learning (ML) systems increase in scope and application in regulated domains, practitioners need a defensible framework to identify proxies at scale. Current disparate treatment frameworks typically rely upon some combination of quantitative and qualitative review of models' inputs to identify proxies. Features that are identified as proxies are then typically removed from the model in practice, and predictive performance degrades in favor of fairness through unawareness. Here, we propose a two-part framework that reduces the disparate treatment risk of a feature and keeps the predictive performance that removal of the feature loses. First, we propose a quantitative test for proxy capacity that identifies whether some of a feature's values reveal membership in a particular demographic group. Second, we propose a pre-processing methodology that adjusts those proxy features to reduce their proxy capacity. We show empirically on synthetic and public datasets that this framework identifies features that proxy for demographic information and reduces their proxy capacity while the adjusted feature retains task-relevant signal (i.e. improves predictive performance versus removal).

---


### 50. [VideoRNG: Relightable Neural Gaussians from Generative Video Models](https://arxiv.org/abs/2611.25338)

**<font color=#1a73e8>作者：</font>** Bowen Xue, Saeed Hadadan, Fabrice Rousselle 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating realistic 3D assets remains constrained by classical representations: surface meshes and compact physically based materials struggle to express objects whose appearance arises from fine geometry or complex light transport, while existing Gaussian-splatting generators typically bake fixed illumination into appearance. We introduce VideoRNG, a two-stage method that generates complete, relightable 3D assets from a text prompt or a single image without prescribing a mesh or analytic material model. A video generator fine-tuned from a pretrained video diffusion backbone first produces a structured RGBA turntable sequence under a known pose, camera, and illumination. A feed-forward large reconstruction model initialized from a pretrained video diffusion backbone then maps the video-VAE latent frames of selected turntable frames directly to millions of anisotropic Gaussians with learned neural appearance features. A shared directional decoder and stochastic Gaussian ray tracer turn this representation, which we call ray-traced Relightable Neural Gaussians (rtRNG), into radiance under novel viewpoints and illumination. To preserve high-frequency appearance while learning geometry, we introduce depth-anchored appearance training, and we make million-Gaussian reconstruction practical through foreground token selection and cost-aware distributed sampling. VideoRNG generates complex assets such as fur, feathers, and spider webs that can be interactively rendered, relit, and integrated into scenes.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-265](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
