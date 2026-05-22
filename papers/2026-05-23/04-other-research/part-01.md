# 📦 其他研究 | 2026年05月23日

> 本类共 **347** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-347](./part-07.md)

---

### 1. [Temporal Contrastive Transformer for Financial Crime Detection: Self-Supervised Sequence Embeddings via Predictive Contrastive Coding](https://arxiv.org/abs/2605.21490)

**<font color=#1a73e8>作者：</font>** Danny Butvinik, Yonit Marcus, Nitzan Tal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Temporal Contrastive Transformer (TCT), a representation learning framework designed to capture contextual temporal dynamics in sequences of financial transactions. The model is trained using a self-supervised contrastive objective to produce embeddings that encode behavioral patterns over time, with the goal of supporting downstream fraud detection tasks. We evaluate TCT in a realistic setting by using the learned embeddings as input features to a gradient boosting classifier. Experimental results show that embeddings alone achieve meaningful predictive performance (AUC 0.8644), indicating that the model captures non-trivial temporal structure. However, when combined with domain-engineered features, no measurable improvement is observed over the baseline (AUC 0.9205 vs. 0.9245), suggesting that the learned representations largely overlap with existing feature abstractions. These findings position TCT as a promising representation learning approach that captures relevant behavioral signal, while highlighting the challenges of achieving additive value over strong domain features. The results reflect an intermediate stage in the development of temporal representation learning for financial crime detection and motivate further research on model architecture, training objectives, and integration strategies. At this early stage, achieving performance comparable to a strong feature-engineered baseline is itself a meaningful outcome, indicating that learned representations approximate domain-specific features without manual engineering. While not yet production-ready, these results point to a promising direction for reducing reliance on feature engineering in financial crime detection.

---


### 2. [The Attribution Impossibility: No Feature Ranking Is Faithful, Stable, and Complete Under Collinearity](https://arxiv.org/abs/2605.21492)

**<font color=#1a73e8>作者：</font>** Drake Caraker, Bryan Arnold, David Rhoads  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> No feature ranking can be simultaneously faithful, stable, and complete when features are collinear. For collinear pairs, ranking reduces to a coin flip. We prove this impossibility, quantify it for four model classes, resolve it via ensemble averaging (DASH), and machine-verify it with 305 Lean 4 theorems. We characterize the complete attribution design space: exactly two families of methods exist -- faithful-complete methods (unstable, with rankings that flip up to 50% of the time) and ensemble methods like DASH (stable, reporting ties for symmetric features) -- and no method lies outside this dichotomy. The impossibility is quantitative: the attribution ratio diverges as 1/(1-rho^2) for gradient boosting, is infinite for Lasso, and converges for random forests. DASH (Diversified Aggregation of SHAP) is provably Pareto-optimal among unbiased aggregations, achieving the Cramer-Rao variance bound with a tight ensemble size formula. In a survey of 77 public datasets, 68% exhibit attribution instability. Switching to conditional SHAP does not escape the impossibility when features have equal causal effects. The framework includes practical diagnostics -- a Z-test workflow and single-model screening tool -- and has direct consequences for fairness auditing: SHAP-based proxy discrimination audits are provably unreliable under collinearity. The design space theorem, diagnostics, and impossibility are mechanically verified in Lean 4 (305 theorems from 16 axioms, 0 sorry) -- to our knowledge, the first formally verified impossibility in explainable AI.

---


### 3. [Don't Collapse Your Features: Why CenterLoss Hurts OOD Detection and Multi-Scale Mahalanobis Wins](https://arxiv.org/abs/2605.21493)

**<font color=#1a73e8>作者：</font>** Rahul D Ray  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ability to detect out-of-distribution (OOD) inputs is fundamental to safe deployment of machine learning systems. Yet, current methods often rely on feature representations that are optimised solely for classification accuracy, neglecting the distinct requirements of epistemic uncertainty. We introduce GOEN (Geometry-Optimised Epistemic Network), a simple pipeline that combines multi-scale features, L2 normalisation, Mahalanobis distance, and a calibration head trained with real hard OOD examples. Through systematic ablation we uncover a counter-intuitive finding: CenterLoss, a popular regulariser for feature compactness, significantly degrades OOD detection performance, reducing average OOD AUROC from 0.9483 to 0.9366 despite improving classification accuracy. The best variant, GOEN-NoCenterLoss, achieves an average OOD AUROC of 0.9483, surpassing all baselines including deep ensembles (0.8827), KNN (0.8967), and ODIN (0.8870) on CIFAR-10 benchmarks, while maintaining competitive in-distribution accuracy. Our results challenge the prevailing assumption that better classification geometry automatically leads to better epistemic uncertainty. Instead, we show that overly tight feature clusters compress inter-class margins and distort the covariance structure needed for effective OOD detection. GOEN is efficient, training in under 20 minutes on a single GPU, and provides a practical blueprint for building AI systems that reliably recognise their own limitations.

---


### 4. [Double descent for least-squares interpolation on contaminated data: A simulation study](https://arxiv.org/abs/2605.21494)

**<font color=#1a73e8>作者：</font>** Tino Werner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Overparametrized models can exhibit an excellent generalization performance, although they should be prone to overfitting according to classical statistical theory. The discovery of the "double descent", indicating that the generalization error decreases after a certain model complexity has been reached, opened a new line of research. Robust statistics considers statistical estimation on contaminated data, which, due to assumptions that do not hold on real data, let data points appear as outliers w.r.t. the assumed "ideal" distribution, potentially severely distorting any classical estimator. We address the question whether a double descent phenomenon can be observed in a linear regression setting with contaminated training data. We compare the performance of the highly non-robust least-squares interpolation estimator with several robust alternatives. It turns out that large overparametrization indeed allows for a double descent phenomenon, resulting in a very good generalization performance of the least-squares interpolator, surpassing that of the robust alternatives.

---


### 5. [Chain Reactions: How Nonce Collisions in ECDSA Compromise Polygon MEV Searchers](https://arxiv.org/abs/2605.21498)

**<font color=#1a73e8>作者：</font>** Yash Madhwal, Andrey Seoev, Raffaele Della Pietra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> ECDSA signatures form the bedrock of blockchain transaction authentication, yet their security critically depends on proper nonce generation. We uncover a critical vulnerability in the Polygon MEV ecosystem: systematic nonce reuse that enables complete private key recovery. Analyzing on-chain data reveals that searchers, driven by the need for sub-second response times in sealed-bid auctions, employ predictable nonce patterns. These patterns create linear relationships between signatures, allowing passive attackers to recover private keys using elementary algebra. We provide a compact linear-system formulation for such attacks, including the dangerous case of cross-wallet nonce collisions, and present concrete evidence of exploitable patterns on Polygon. Our findings demonstrate how protocol-induced latency pressures can lead to catastrophic cryptographic failures in production blockchain systems, where a single implementation error compromises multiple accounts simultaneously.

---


### 6. [Predicting Performance of Symbolic and Prompt Programs with Examples](https://arxiv.org/abs/2605.21515)

**<font color=#1a73e8>作者：</font>** Chengqi Zheng, Keya Hu, Shuzhi Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM prompting is widely used for naturally stated tasks, yet it is unreliable it may succeed on a few test cases but fail at deployment time. We study performance prediction: given a program, either symbolic (e.g. Python) or a prompt executed on an LLM, and a few in-domain examples, predict its performance on unseen tasks from the same domain. We use a simple coin-flip model, treating each pass/fail program execution as a Bernoulli random variable, whose success probability is the programs unknown performance. In this model, performance depends entirely on: 1) the observed execution outcomes on test cases, and 2) a prior over performances. We compile empirical performance priors from a corpus of diverse programs and tasks, and find that performance for symbolic programs (e.g., Python) are all or nothing, while prompt programs have a diffuse prior with many nearly-correct programs. This difference explains why a few passing tests can certify symbolic programs but not prompt programs. Building on this insight, we develop RAP (Retrieved Approximate Prior), which retrieves similar tasks and prompt programs from an existing corpus to construct a proxy prior, which is then used to predict performance. We show RAP achieves solid performances.

---


### 7. [A Reproducible Log-Driven AutoML Framework for Interpretable Pipeline Optimization in Healthcare Risk Prediction](https://arxiv.org/abs/2605.21528)

**<font color=#1a73e8>作者：</font>** Rui Huang, Lican Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate and reproducible disease risk prediction remains challenging due to heterogeneous features, limited samples, and severe class imbalance. This study introduces yvsoucom-iterkit, a deterministic and log-driven automated machine learning framework that formulates pipeline optimization as a fully reproducible, configuration-level system. Each pipeline is encoded as a traceable log entity, enabling analysis of component attribution, interactions, similarity, and cross-seed robustness. Experiments on the Pima Indians Diabetes and Stroke datasets across more than 18,000 pipeline configurations reveal a structured and partially redundant search space, where performance is governed by a small subset of interacting components. Random Forest importance analysis identifies augmentation (0.454), model choice (0.198), and imbalance handling (0.101) as key drivers on Pima, while imbalance handling dominates Stroke (0.406). Component similarity analysis shows strong redundancy, with feature selection variants (biMax-biMean) exhibiting low RMS distance (0.0252), mixup closely matching no augmentation (0.0279), and TomekLinks aligning with no imbalance handling (0.0325), whereas Gaussian noise shows greater divergence from no augmentation (0.10). The framework achieves strong and stable performance using ensemble models (Weighted-F1 0.89, Macro-F1 0.88 on Pima; Weighted-F1 0.94 on Stroke), while Macro-F1 remains lower on Stroke (0.67) due to class imbalance. Cross-seed analysis reveals a performance-robustness trade-off, with ensembles showing lower variability (0.023-0.026) than SVM. These results indicate that effective AutoML optimization can focus on a reduced set of high-impact components.

---


### 8. [Discovering Entity-Conditioned Lag Heterogeneity: A Lag-Gated Neural Audit Framework for Panel Time Series](https://arxiv.org/abs/2605.21542)

**<font color=#1a73e8>作者：</font>** Andi Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Country-level temporal panels are widely used in empirical analysis. Researchers often need to audit how different entities respond to historical signals over different time horizons. Current approaches typically do not provide directly auditable entity-specific lag summaries. We formulate entity-conditioned heterogeneous lag discovery as a temporal panel mining task and propose AC-GATE, an Adaptive-Conditioning Encoder with a Scale-Invariant Lag Gate. It instantiates conditional Moderated Distributed Lag by using observable entity-level proxies to condition lag-weight distributions over historical observations, thereby making effective lags structural outputs of the model rather than post-hoc explanations. The evaluation is based on a layered audit protocol that separates predictive calibration from lag discovery. A synthetic panel with known ground-truth lags is used for mechanism recovery testing, and two real-world country-level panels are used for external audit and stress testing. The results show that AC-GATE can recover heterogeneous lag structure in synthetic data, and generates non-degenerate, externally structured effective lags in real data.

---


### 9. [PeakFocus: Bridging Peak Localization and Intensity Regression via a Unified Multi-Scale Framework for Electricity Load Forecasting](https://arxiv.org/abs/2605.21550)

**<font color=#1a73e8>作者：</font>** Wangzhi Yu, Peng Zhu, Qing Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electricity load peak forecasting (ELPF), simultaneously predicting peak timing and intensity, is a prerequisite for effective grid scheduling and risk management. However, existing methods face three limitations. First, they adopt a two-stage predict-then-locate paradigm, which severs the link between temporal localization and intensity regression. Second, they still struggle with the multi-scale representation conflict, leading to peak misjudgment and timing misalignment. Third, the lack of explicit peak timing context during intensity regression causes intensity smoothing because predictions are dominated by global smoothing trends. To address these limitations, we propose PeakFocus, a unified framework for ELPF. (i) A Unified Peak-Aware Pipeline (UPAP) utilizes a triple hybrid loss to jointly supervise temporal localization and intensity regression, alongside a tolerance-based evaluation protocol. (ii) A Multi-Scale Mixing Peak Locator (MSM-PL) exploits coarse-grained features to mitigate peak misjudgment caused by local fluctuations, and injects them into fine-grained features via a cascade mechanism to resolve timing misalignment. (iii) A Location-Aware Decoder (LAD) injects peak timing context into the intensity regression process, providing explicit guidance to counteract intensity smoothing and improve peak intensity estimation. Extensive experiments on the public Electricity (ELC) dataset and our industrial-scale World Large-scale Electricity Load (WLEL) dataset show that PeakFocus outperforms baselines in both timing precision and intensity estimation.

---


### 10. [Expectation Consistency Loss: Rethink Confidence Calibration under Covariate Shift](https://arxiv.org/abs/2605.21552)

**<font color=#1a73e8>作者：</font>** Jinzong Dong, Zhaohui Jiang, Bo Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Confidence calibration for classification models is vital in safety-critical decision-making scenarios and has received extensive attention. General confidence calibration methods assume training and test data are independent and identically distributed, limiting their effectiveness under covariate shifts. Previous calibration methods under covariate shift struggle with class-wise or canonical calibrations and often rely on unstable importance weighting when density ratios are large or unbounded. Given the above limitations, this paper rethinks confidence calibration under covariate shifts. First, we derive a necessary and sufficient condition for confidence calibration under covariate shifts, named Expectation consistency condition, which reveals covariate shifts do not necessarily lead to uncalibrated confidence and provides a weaker condition for confidence calibration than global covariate distribution alignment. Then, utilizing Expectation consistency condition, this paper proposes an unsupervised domain adaptation loss to calibrate confidence of the target domain, named Expectation consistency loss (ECL), which is compatible with canonical calibration, class-wise calibration, and top-label calibration. Third, we prove that computing ECL loss has the same sample complexity as Expected Calibration Error (ECE) and provide a theoretically grounded mini-batch trainable scheme for ECL loss. Finally, we validate the effectiveness of our method on both simulated and real-world covariate shift datasets.

---


### 11. [TONIC: Token-Centric Semantic Communication for Task-Oriented Wireless Systems](https://arxiv.org/abs/2605.21553)

**<font color=#1a73e8>作者：</font>** Sige Liu, Kezhi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tokens are becoming the basic units through which foundation models represent and process information for understanding and inference. However, traditional wireless communication, centered on bit-level fidelity, faces a mismatch between what is transmitted reliably and what downstream models actually consume. This mismatch calls for a communication design that directly accounts for token-level task relevance and downstream model requirements, rather than treating all transmitted bits as equally important. In this paper, we propose TONIC, a token-centric semantic communication framework for task-oriented wireless systems. The transmitter converts each source sample into a sequence of tokens, estimates token-level task relevance, and allocates protection through utility-aware unequal error protection under a fixed channel-use budget. At the receiver, token-level confidence is used to gate unreliable decisions, turning harmful substitutions into recoverable erasures before a Transformer-based completion model restores the masked tokens for final task inference. Our framework combines transmitter-side semantic-aware protection with receiver-side confidence-aware gating in a modular and interpretable architecture, rather than relying solely on fully black-box end-to-end learning. We further establish a utility-aware Bayes-risk interpretation for the receiver-side gating rule and study its interaction with unequal protection and completion. Experimental results on image classification show that TONIC consistently outperforms separation-based schemes, the pixel-domain DeepJSCC baseline, and token-domain baselines under matched communication budgets over AWGN, Rayleigh, and Rician channels.

---


### 12. [Beyond Single Slot: Joint Optimization for Multi-Slot Guaranteed Display Advertising](https://arxiv.org/abs/2605.21556)

**<font color=#1a73e8>作者：</font>** Zhaoqi Zhang, Jiaming Deng, Miao Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Guaranteed display advertising is crucial for platform monetization, yet existing methods often operate under a single-slot assumption, limiting their ability to optimize allocation across multi-slot page views. In this paper, we propose a novel joint optimization framework for multi-slot GD allocation, addressing key challenges such as slot-level redundancy, contract imbalance, and exposure concentration. Our approach formulates the allocation as an offline bipartite matching problem with a contract roulette mechanism for slot exclusivity and Page View constraints for impression control, and incorporates a scalable allocation optimization algorithm for efficient large-scale deployment. Extensive online tests on the Meituan advertising platform demonstrate that our method significantly improves merchant ROI, platform revenue efficiency, and contract fulfillment robustness. Specifically, online A/B tests show a 28.99% increase in Average Revenue Per User under 70% traffic, and DID analysis further indicates improved contract stability, demonstrating the strong applicability and effectiveness of our framework in real-world advertising deployments.

---


### 13. [Objective-Induced Bias and Search Dynamics in Multiobjective Unsupervised Feature Selection](https://arxiv.org/abs/2605.21561)

**<font color=#1a73e8>作者：</font>** Mathieu Cherpitel, Thomas Bäck, Martijn R. Tannemaat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised feature selection is commonly formulated as a multiobjective optimisation problem that jointly optimises subset quality and subset size. Yet the behaviour of this formulation depends critically on the choice of evaluation objective, the direction of subset-size regularisation, and the initialisation strategy. We study these factors in a controlled setting using a synthetic dataset with known informative, redundant, and irrelevant feature types. Six formulations are compared by combining three evaluation objectives: accuracy, silhouette score, and PCA reconstruction loss with subset-size minimisation or maximisation. The results show that formulation strongly affects both search dynamics and the quality of the resulting Pareto front. Silhouette-based formulations exhibit a strong bias toward trivial low-cardinality solutions and remain weak proxies for predictive performance. In contrast, the proposed PCA loss objective produces compact subsets with test accuracy comparable to subsets obtained by directly optimising supervised accuracy. Overall, the study shows that objective design is central to effective multiobjective unsupervised feature selection.

---


### 14. [Embedding-Based Federated Learning with Runtime Governance for Iron Deficiency Prediction](https://arxiv.org/abs/2605.21563)

**<font color=#1a73e8>作者：</font>** Fan Zhang, Simon Deltadahl, Majid Lotfian Delouee 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent reviews find that the vast majority of published healthcare federated learning (FL) studies never reach real-world deployment. We developed an embedding-based FL pipeline for iron deficiency prediction from routine full blood count (FBC) data and deployed it across real institutional environments at Amsterdam University Medical Centre (AUMC) and NHS Blood and Transplant (NHSBT), two clinical environments that differ markedly in iron deficiency prevalence, ferritin distribution, and subject populations. A frozen domain-specific haematology foundation model, DeepCBC, performs site-local representation extraction, restricting federated training to a compact downstream classifier and substantially reducing recurrent communication relative to full-encoder federation. The two clinical datasets are structurally not independent and identically distributed (non-IID), with heterogeneity arising from distinct population differences rather than sampling artefacts. Runtime governance is enforced by FLA$^3$, a healthcare-oriented FL platform providing study-scoped execution, policy-based authorisation, and signed audit logging. Standard sample-size-weighted aggregation (FedAvg) reduced the area under the receiver operating characteristic curve (ROC-AUC) at both sites relative to local-only training, as the global update was biased towards the larger AUMC distribution. FedMAP, a personalised aggregation method, raised ROC-AUC from 0.9470 to 0.9594 at AUMC and from 0.8558 to 0.8671 at NHSBT relative to local-only training, achieving the highest macro ROC-AUC of 0.9133 and the best macro balanced accuracy overall. These results support personalised aggregation in clinical federations where client sample size and task relevance diverge substantially.

---


### 15. [Calibration, Uncertainty Communication, and Deployment Readiness in CKD Risk Prediction: A Framework Evaluation Study](https://arxiv.org/abs/2605.21566)

**<font color=#1a73e8>作者：</font>** Michael O. Eniolade  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models for chronic kidney disease (CKD) risk prediction often post strong discrimination scores on internal test sets. Calibration and uncertainty quantification get far less attention, leaving clinicians without reliable information about whether the probability outputs are accurate.
We trained five classifiers on the UCI CKD dataset (400 patients, 62.5% CKD prevalence): logistic regression, random forest, XGBoost, SVM with Platt scaling, and Gaussian naive Bayes. We evaluated each across calibration quality, conformal prediction coverage, and an eight-criterion deployment readiness framework. A distributional stress-test applied the best-calibrated variant of each model to the open-access MIMIC-IV demo cohort (97 patients, 23.7% CKD) to assess behaviour under prevalence shift and feature missingness. We measured calibration before and after Platt scaling and isotonic regression using Expected Calibration Error and Brier Score, and quantified uncertainty through split conformal prediction targeting 90% marginal coverage.
All five models reached AUROC 1.00 on the UCI test set. Isotonic recalibration reduced internal ECE to 0.000-0.022. On MIMIC-IV, AUROC fell to 0.48-0.58, ECE rose to 0.68-0.76, and conformal coverage dropped from 0.80-0.98 to 0.21-0.25 against a 90% target. No model scored above 4 out of 16 on the deployment readiness checklist.
Near-perfect internal performance did not transfer. Calibration stability and conformal coverage should be evaluated on external data before any clinical prediction model moves toward deployment.

---


### 16. [Equilibrium Propagation and Hamiltonian Inference in the Diffusive Fitzhugh-Nagumo Model](https://arxiv.org/abs/2605.21568)

**<font color=#1a73e8>作者：</font>** Jack Kendall  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we extend the Equilibrium Propagation framework to skew-gradient systems and show an equivalence between deep Energy-Based Models and Hamiltonian neural networks. We focus on networks of diffusively coupled Fitzhugh-Nagumo neurons as a prototypical example. We show that since stationary solutions of the Fitzhugh-Nagumo model are described by self-adjoint operators, the methods of equilibrium propagation for performing credit assignment can be applied. Furthermore, for Fitzhugh-Nagumo networks with the topology of a deep residual network, we show that the steady state solutions admit a (spatial) Hamiltonian, and thus the methods of Hamiltonian Echo Backpropagation can be applied. We end by deriving an explicit layer-wise Hamiltonian recurrence relation governing inference for stationary solutions of both deep Fitzhugh-Nagumo networks and deep Energy-Based Models.

---


### 17. [PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects](https://arxiv.org/abs/2605.21572)

**<font color=#1a73e8>作者：</font>** Ziang Cao, Yinghao Liu, Haitian Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Simulation-ready physical 3D assets have emerged as a promising direction owing to their broad applicability in downstream tasks. However, most existing 3D generation methods either neglect physical properties or are limited to a single asset category, e.g., rigid, deformable, or articulated objects. To address these limitations, we introduce PhysX-Omni, a unified framework for simulation-ready physical 3D generation across diverse asset types. Specifically, we develop a novel and efficient geometry representation tailored for Vision-Language Models, which directly encodes high-resolution 3D structures without compression, significantly improving generation performance. In addition, we construct the first general simulation-ready 3D dataset, PhysXVerse, covering diverse indoor and outdoor categories. Furthermore, to comprehensively and flexibly evaluate both generative and understanding capabilities in the wild, we propose PhysX-Bench, which encompasses six key attributes: geometry, absolute scale, material, affordance, kinematics, and function description. Extensive experiments with conventional metrics and PhysX-Bench show that PhysX-Omni performs strongly in both generation and understanding. Moreover, additional studies further validate the potential of PhysX-Omni for applications in simulation-ready scene generation and robotic policy learning. We believe PhysX-Omni can significantly advance a wide range of downstream applications, particularly in embodied AI and physics-based simulation.

---


### 18. [Lens: Rethinking Training Efficiency for Foundational Text-to-Image Models](https://arxiv.org/abs/2605.21573)

**<font color=#1a73e8>作者：</font>** Dong Chen, Fangyun Wei, Ziyu Wan 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Lens, a 3.8B-parameter T2I model that achieves performance competitive with, and in several cases surpassing, state-of-the-art models with more than 6B parameters across various benchmarks, while requiring significantly less training compute. For example, Lens requires only about 19.3% of the training compute used by Z-Image. The training efficiency of Lens stems from two key strategies beyond its compact model size. First, we maximize data information density per training batch by (i) training on Lens-800M, a dataset of 800M densely captioned image-text pairs whose captions are generated by GPT-4.1 and contain approximately 109 words on average, providing richer semantic supervision than conventional short captions, and (ii) constructing each batch from images with multiple resolutions and diverse aspect ratios, thereby enlarging the effective visual coverage of each optimization step. Second, we improve convergence speed through careful architectural choices, including adopting a semantic VAE that provides better latent representations and employing a strong language encoder that accelerates optimization while enabling multilingual generalization from English-only training data. After pre-training, we apply RL with taxonomy-driven prompts (Lens-RL-8K) and structured reward rubrics to suppress artifacts and improve visual quality, a reasoner module with training-free system prompt search to better align user requests with the model, and distillation-based acceleration for 4-step inference. Through efficient training and systematic optimization, Lens generalizes to arbitrary aspect ratios from 1:2 to 2:1 and resolutions up to 1440^2, and supports prompts in several commonly used languages. Thanks to its compact size, Lens generates a 1024^2 image in 3.15 seconds on a single NVIDIA H100 GPU, while its distilled turbo version performs 4-step generation in 0.84 seconds.

---


### 19. [ConTact: Contact-First Antibody CDR Design via Explicit Interface Reasoning](https://arxiv.org/abs/2605.21600)

**<font color=#1a73e8>作者：</font>** Mansoor Ahmed, Spencer VonBank, Nadeem Taj 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computational antibody CDR design methods condition on antigen structure to generate binding loops, yet existing architectures conflate two fundamentally distinct sub-problems: identifying which CDR positions will contact the antigen, and selecting amino acids at those positions. This conflation forces models to learn contact reasoning implicitly through uniform message passing, diluting antigen signal across all positions equally. We introduce ConTact, a contact-then-act architecture that explicitly decomposes CDR design into three cascaded stages: learning surface complementarity fingerprints, predicting CDR-antigen contacts, and injecting contact-gated antigen features into the sequence head. A distance-biased cross-attention module encodes geometric priors favoring spatial neighbors, while a contact-weighted cross-entropy loss concentrates gradient signal on binding-critical positions. On CHIMERA-Bench dataset, ConTact achieves the best structural quality (7% RMSD improvement over the next-best baseline), best epitope awareness (10% F1 score over GNN baselines), and competitive sequence recovery (AAR 0.38) among several CDR-H3 design baselines.

---


### 20. [GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual Experience Distillation](https://arxiv.org/abs/2605.21605)

**<font color=#1a73e8>作者：</font>** Sixiang Chen, Zhaohu Xing, Tian Ye 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-ended image generation is no longer a simple prompt-to-image problem. High-quality generation often requires an agent to combine a model's internal generative ability with external resources. As requests become more diverse and demanding, we aim to develop a general image-generation agent that can self-evolve through trajectories and use tools more effectively across varied generation challenges. To this end, we propose GenEvolve, a self-evolving framework based on Tool-Orchestrated Visual Experience Distillation. In GenEvolve, each generation attempt is modeled as a tool-orchestrated trajectory, where the agent gathers evidence, selects references, invokes generation skills, and composes them into a prompt-reference program. Unlike existing agentic generation methods that mainly rely on image-level scalar rewards, GenEvolve compares multiple trajectories for the same request and abstracts best-worst differences into structured visual experience, provided only to a privileged teacher branch. Inspired by on-policy self-distillation, Visual Experience Distillation provides dense token-level supervision, helping the student internalize better search, knowledge activation, reference selection, and prompt construction. We further construct GenEvolve-Data and GenEvolve-Bench. Experiments on public benchmarks and GenEvolve-Bench show substantial gains over strong baselines, achieving state-of-the-art performance among current image-generation frameworks. Our website is as follows: this https URL

---


### 21. [When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning](https://arxiv.org/abs/2605.21606)

**<font color=#1a73e8>作者：</font>** Xiaogeng Liu, Xinyan Wang, Yingzi Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) trains a student on its own rollouts using a privileged teacher, but its standard objective weights all generated tokens equally, implicitly treating the privileged teacher target as equally reliable at every student-visited prefix. Existing entropy-based OPD methods relax this uniformity by modulating token-level supervision with teacher entropy, but high teacher entropy in reasoning has an ambiguous reliability meaning: it can reflect either non-viable uncertainty or benign solution diversity. To identify this phenomenon, we introduce a branch-viability diagnostic. Specifically, we record next-token alternatives from the privileged-answer teacher prompt, force each alternative after the student prompt plus its on-policy spine prefix, and test whether the resulting student-template continuation recovers the correct answer. On Qwen3-4B, we find that an oriented within-sequence position score is the strongest tested predictor of teacher-token reliability, reaching an area-under-ROC-curve (AUROC) of 0.83; local uncertainty scores are at most 0.57. Motivated by this trajectory-level structure, we propose Position-Weighted On-Policy Self-Distillation (PW-OPSD), which applies an increasing position weight while keeping the same student rollout, privileged teacher pass, and clipped forward-KL target as OPSD. In our comprehensive evaluations with different random seeds, the diagnostic-derived PW-OPSD improves AIME 2024 and AIME 2025 Avg@12 by +1.0 and +1.1 points, and a generalization evaluation on two larger-scale models from different families, DeepSeek-R1-Distill-Llama-8B and Olmo-3-7B-Think, also demonstrates consistent aggregate Avg@12 improvements. These results show that teacher-token reliability in reasoning distillation is trajectory-structured and can be utilized without additional teacher computation.

---


### 22. [AgForce Enables Antigen-conditioned Generative Antibody Design](https://arxiv.org/abs/2605.21610)

**<font color=#1a73e8>作者：</font>** Mansoor Ahmed, Murray Patterson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Antibody design methods condition on antigen structure to generate complementarity-determining regions (CDR), yet a systematic evaluation of baseline methods reveals that they largely ignore the antigen input. We identify three failure modes that explain this behavior. Antigen blindness arises because models derive predictions from antibody framework context rather than antigen information, producing nearly identical CDRs regardless of the target. Vocabulary collapse reduces predicted amino acids to three to five per position, far below the ground truth distribution in native sequences. Moreover, any model trained with standard per-position cross-entropy converges to the positional marginal distribution, making it provably unable to produce antigen-specific sequence predictions. We propose a novel encoder-decoder architecture called AgForce, that uses a graph neural network (GNN) as the encoder and specialized decoders for sequence-structure co-design. Specifically, we apply framework dropout, gated bottlenecks, and hyperbolic cross attention that prevent the antibody shortcut path. In the decoder, a Mixture Density Network (MDN) sequence head with Potts-like pairwise coupling and annealed Multiple Choice Learning (aMCL) replaces the cross-entropy objective with a multi-component distribution whose optimal solution differs from the positional marginal. An antigen cycle consistency head routes gradients through the sequence decoder, forcing predicted distributions to encode antigen identity. AgForce achieves the best binding quality and sequence recovery simultaneously on the CHIMERA-Bench dataset, improving amino acid recovery by 8% over the strongest sequence baseline while surpassing the baselines across all interface metrics, and nearly doubling the effective vocabulary of GNN methods. The source code is available at: this https URL

---


### 23. [UniVL: Unified Vision-Language Embedding for Spatially Grounded Contextual Image Generation](https://arxiv.org/abs/2605.21611)

**<font color=#1a73e8>作者：</font>** Jiayun Wang, Yu Wang, Weijie Gan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce spatially grounded contextual image generation, a controllable image generation task that reframes the conditioning paradigm. Instead of supplying a reference image and a global text prompt through two separate encoders, one for vision and one for language, UniVL is trained to bind semantics to spatial locations directly from a single unified visual input, where the textual instruction is rendered onto the spatial mask. This removes the need for a standalone text encoder at inference time. The resulting model supports contextual image generation by following user-specified instructions about what should appear where, while substantially reducing computation.
To address this task, we propose a framework in which the UniVL encoder, adapted from an optical-character-recognition-pretrained backbone, reads the unified condition optically and produces a UniVL embedding, fVIL, that fuses visual and semantic intent with spatial locations in a single token sequence. A two-stage pipeline first aligns UniVL with the VAE embedding space and then conditions a pretrained diffusion backbone entirely on UniVL embeddings, eliminating the standalone text encoder, such as T5. Although this reframing uses a deliberately minimal text interface, it yields strong empirical gains. On UniVL-ImgGen, a benchmark of 477K mask-annotated images that we construct for training and evaluation, UniVL improves image quality over text-prompted baselines, reducing FID from 14 to 11 and increasing PSNR from 16 to 20. It also eliminates the text encoder entirely, reducing inference TFLOPs by up to 52% and runtime by up to 44%. Additional ablation studies validate the contributions of the proposed components, paving the way for efficient, spatially grounded image generation with a unified conditioning paradigm.

---


### 24. [Simulating Learners' Task-Selection Strategies and System Constraints in Mastery Learning](https://arxiv.org/abs/2605.21613)

**<font color=#1a73e8>作者：</font>** Haley Noh, Aarna Chowdhary, Jeroen Ooge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Intelligent Tutoring Systems often grant learners shared control over skill and problem selection. Prior work suggests learners exhibit diverse task-selection strategies, such as avoiding challenge, which may interact with mastery learning systems that optimize task selection based on estimated knowledge. Algorithmic constraints on problem selection may help mitigate these effects, but testing such constraints in classrooms is costly. We propose a simulation-based framework to examine how learner task-selection strategies and system constraints shape mastery learning efficiency. Using interaction data from 261 students across two mathematical domains (equation solving and graph interpretation), we simulate strategies such as Weakness Targeting and Interleaving. We evaluate how these strategies affect overpractice as a measure of efficiency. Results show substantial variability across strategies, with risk-averse strategies producing higher levels of overpractice, especially for complex multi-step problems. Targeted system constraints significantly reduce inefficiencies for maladaptive strategies while minimally affecting already efficient strategies. These findings show how simulation grounded in student data can guide the redesign of shared-control tutoring systems before classroom deployment.

---


### 25. [$\textit{BlockFormer}$ : Transformer-based inference from interaction maps](https://arxiv.org/abs/2605.21617)

**<font color=#1a73e8>作者：</font>** Eloïse Touron, Pedro L. C. Rodrigues, Julyan Arbel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference from interaction maps, such as centromere identification from genome-wide chromosome conformation capture techniques -- notably Hi-C -- can be formulated as a generic inverse problem: infer a set of parameters given a map summarizing pairwise interactions between entities through blocks of variable numbers and sizes. In this work, we introduce a data-driven approach that leverages shared structure between these maps, such as global alignment between localized patterns, while handling the variability in number and size of entities arising in real-world data. Our approach relies on a transformer architecture capable of handling such variability and a custom simulator to generate abundant, yet computationally cheap synthetic data for training. Applied to the problem of centromere localization, the method accurately recovers their genomic positions across a wide range of species of various genome sizes.

---


### 26. [TO-Agents: A Multi-Agent AI Pipeline for Preference-Guided Topology Optimization](https://arxiv.org/abs/2605.21622)

**<font color=#1a73e8>作者：</font>** Isabella A. Stewart, Hongrui Chen, Faez Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Topology optimization can generate efficient structures, but designers often must manually translate qualitative intent, such as desired visual style, product experience, or manufacturability into solver settings that are not directly tied to those preferences. We present TO-Agents, a multi-agent AI framework that connects natural-language design intent with iterative topology optimization. The framework converts a human-provided problem description into validated solver inputs, runs a topology optimization solver, renders the resulting 3D topology, and uses multi-view vision-language reasoning with an independent judge agent to critique each result and revise solver parameters. We evaluate the framework on two long-horizon design tasks: a cantilever beam benchmark and a phone-stand product design. In both tasks, the designer specifies an aesthetic preference for hierarchically branched structures inspired by natural tree morphologies, and the system performs four revision cycles across ten independent replicates. TO-Agents produces at least one preference-aligned design in 60% of trials for each case study, corresponding to up to 6x more successful trials than an ablated pipeline without visual or historical feedback. Judge scores and human evaluations show that the pipeline can identify effective parameter levers, recover from poor revisions, and expand design exploration. A manufacturing agent further post-processes top-ranked designs for additive manufacturing, enabling end-to-end intent-to-prototype design. We also identify failure modes, including overshooting, selective memory, misplaced tools, and incorrect parameter reasoning. These results suggest that agentic topology optimization can shift designers from low-level parameter tuning toward higher-level specification of form and function, while highlighting safeguards needed for reliable autonomous engineering design.

---


### 27. [MindLoom: Composing Thought Modes for Frontier-Level Reasoning Data Synthesis](https://arxiv.org/abs/2605.21630)

**<font color=#1a73e8>作者：</font>** Haiyang Shen, Taian Guo, Xuanzhong Chen 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although LLMs have made substantial progress in reasoning, systematically producing frontier-level reasoning data remains difficult. Existing synthesis methods often have limited visibility into the structural factors that govern problem difficulty, which can result in narrow diversity and unstable difficulty control. In this work, we view the difficulty of a reasoning problem as arising from the accumulation of atomic knowledge-reasoning transformations, which we term thought modes. Building on this perspective, we propose MindLoom, a framework for synthesizing frontier-level reasoning data through compositional thought mode engineering. Given a collection of hard problems with verified solutions, MindLoom first decomposes those solutions into thought mode chains that reveal each problem's construction logic. It then trains a retrieval model that matches problem states to compatible thought modes, providing guidance on which reasoning challenges to introduce during synthesis. New problems are composed by iteratively applying retrieved thought modes to seed questions, with distribution-aligned sampling to encourage diverse reasoning coverage. Finally, a rollout-based judging stage labels generated questions by difficulty and supplies judged-correct responses for supervised fine-tuning. We evaluate MindLoom on nine benchmarks covering five STEM disciplines and four mathematical reasoning tasks across multiple model families and sizes. Models fine-tuned on MindLoom-generated data achieves favorable performances over base models, distillation, and external-data baselines across the reported benchmarks. Ablation studies indicate the contribution of each component, and further analysis suggests that MindLoom covers a broad range of reasoning patterns while maintaining useful difficulty control. We have open-sourced our implementation at this https URL.

---


### 28. [Addressing the Synergy Gap: The Six Elements of the Design Space](https://arxiv.org/abs/2605.21635)

**<font color=#1a73e8>作者：</font>** Tommaso Turchi, Ben Wilson, Matt Roach 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI is now embedded in healthcare, finance, policy, and many other domains, yet genuine human-AI synergy - combined performance that exceeds what either party achieves alone - is uncommon. Meta-analyses show that AI assistance tends to improve human performance compared to working alone, but studies finding true synergy are scarce. We call this persistent shortfall the synergy gap. Most current work treats human-AI combination as an engineering problem and concentrates on interpretability, trust calibration, or interface design. These matter, but they cover only part of what determines whether combination works. Closing the synergy gap, we argue, requires explicit engagement with a wider design space. We map that space through six interconnected elements: sociotechnical context, decision-making frameworks, human decision participants, AI capabilities, interaction, and holistic evaluation. For each element, we describe what it covers, how it shapes the others in practice, and what it implies for design. The result is a shared vocabulary for practitioners building hybrid systems, an analytical lens for researchers studying combination patterns, and a starting point for evaluators interested in the full quality of human-AI decision-making rather than accuracy alone.

---


### 29. [Alike Parts: A Feature-Informed Approach to Local and Global Prototype Explanations](https://arxiv.org/abs/2605.21646)

**<font color=#1a73e8>作者：</font>** Jacek Karolczak, Jerzy Stefanowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prototype-based explanations offer an intuitive, example-based approach to support the interpretability of machine learning black box classifiers but often lack feature-level granularity. We introduce a framework that integrates feature importance at two levels to address this gap. First, for local explanations, we propose \textit{alike parts}: a method that uses feature importance scores to highlight the most relevant, shared feature subsets between a classified instance and its nearest prototype, guiding user attention. Second, we augment the global prototype selection objective function with a feature importance term to actively promote diversity in the feature attributions of the selected prototypes. Experiments on six benchmark datasets show that this augmented selection process maintains or, in some cases, increases the prediction fidelity of the surrogate model, suggesting that feature diversity does not compromise model fidelity.

---


### 30. [Dropout Universality: Scaling Laws and Optimal Scheduling at the Edge-of-Chaos](https://arxiv.org/abs/2605.21648)

**<font color=#1a73e8>作者：</font>** Lucas Fernandez Sarmiento  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a mean-field theory of dropout as a perturbation of critical signal propagation at the edge of chaos. Dropout shifts the perfect-alignment fixed point, making the depth scale for information propagation finite even at critical initialization. We derive critical and crossover scaling laws for correlation decay and establish that smooth activations and kinked, ReLU-like activations constitute distinct universality classes, with different critical exponents and a universal two-parameter scaling collapse in detuning and dropout strength. The distinction traces to the analytic structure of the correlation map: smooth activations admit a Taylor expansion near perfect alignment, while kinked activations develop a branch point with universal non-analyticity. As a corollary, the framework yields saturated dropout profiles under fixed budget; a rank-flow tie-breaker then selects front-loaded schedules, substantially reducing held-out test loss at no extra computational cost, with accuracy gains as a consistent secondary effect. We test the predictions in MLPs and Vision Transformers and discuss CNN/ResNet extensions.

---


### 31. [EntmaxKV: Support-Aware Decoding for Entmax Attention](https://arxiv.org/abs/2605.21649)

**<font color=#1a73e8>作者：</font>** Gonçalo Duarte, Miguel Couceiro, Marcos V. Treviso  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context decoding is increasingly limited by KV-cache memory traffic since each generated token attends over a cache whose size grows linearly with context length. Existing sparse decoding methods reduce this cost by selecting subsets of tokens or pages, but are designed for softmax attention, whose dense tails make any truncation discard nonzero probability mass. In contrast, $\alpha$-entmax produces exact zeros, turning sparse decoding from dense-tail approximation into support recovery: if the selected candidates contain the entmax support, sparse decoding remains exact. While recent entmax kernels enable efficient training, they do not address the autoregressive decoding bottleneck, where dense inference still streams the full KV cache before sparsity is known. In this work, we introduce EntmaxKV, an entmax-native sparse decoding framework that exploits sparsity before KV pages are loaded. EntmaxKV combines query-aware page scoring, support-aware candidate selection, and sparse entmax attention. We analyze truncation error through the dropped probability mass $\delta$, showing that output error is controlled by $\delta$ and vanishes when the entmax support is recovered. We further introduce a Gaussian-aware entmax selector that estimates the entmax threshold from lightweight page statistics, adapting the selected budget to the score distribution. Empirically, EntmaxKV drops less probability mass, retains more support tokens, and achieves lower output error than softmax-based sparse decoding at matched KV budgets. On long-context and language modeling benchmarks, it closely matches full-cache entmax while using a small fraction of the KV cache, achieving up to $3.36\times$ (softmax) and $5.43\times$ (entmax) speedup over full attention baselines at 1M context length. Code available at: this https URL.

---


### 32. [Look-Closer-Then-Diagnose: Confidence-Aware Ultrasound VQA via Active Zooming](https://arxiv.org/abs/2605.21652)

**<font color=#1a73e8>作者：</font>** Yue Zhou, Erxuan Wu, Yikang Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have significantly advanced medical visual question answering, yet their performance in ultrasound remains suboptimal. In clinical practice, sonographers explicitly focus on lesion regions to formulate reports, though diagnostic interpretations sometimes vary due to inherent subjectivity. However, existing VLMs are not explicitly structured to interactively zoom into lesions prior to diagnosis; moreover, they typically treat annotations as unbiased ground truths, failing to account for their inherent subjectivity and ambiguity. In this paper, we propose a framework specifically designed to consider the sonographer's cognitive workflow. We first introduce a structured Zoom-then-Diagnose paradigm, which replicates the interactive search process to enable lesion-focused reasoning. Furthermore, within the Group Relative Policy Optimization (GRPO) framework, we introduce an uncertainty-aware reward derived from stochastic group-wise rollouts to estimate prediction consistency as a proxy for model confidence. Together, these two components encourage the model to reinforce accurate predictions on clear cases while remaining cautious under ambiguity. Experiments across liver, breast, and thyroid datasets show that our framework improves lesion localization by 39.3\%, demonstrating that our model has learned the ability to actively look closer and diagnose.

---


### 33. [Amplifying, Not Learning: Fine-Tuned AI Text Detectors Amplify a Pretrained Direction](https://arxiv.org/abs/2605.21653)

**<font color=#1a73e8>作者：</font>** Alexander Smirnov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI text detectors amplify a pretrained typicality axis; they do not construct an AI-vs-human boundary. On raw encoders before any task supervision, projecting onto centroid(AI)-centroid(HC3) achieves NYT-vs-HC3 AUROC 0.806/0.944/0.834 across three architectures (86-106% of the fine-tuned discrimination ceiling: on RoBERTa-base, raw projection exceeds fine-tuning); on RoBERTa-base, full fine-tuning reduces discrimination below raw on both fluent-formal populations tested. The same axis inverts on non-native ESL writing (AUROC 0.06-0.20) -- a falsifiable prediction unique to the typicality reading. A 24-example frozen probe matches full fine-tuning (0.900 vs 0.895). A closed-form Jacobian predictor parameterises axis-manipulating interventions with R^2 = 1.000 universal, lifts ELECTRA-CE deployment TPR from 0.000 to 0.904 at FPR = 1%, and transfers to three independently-trained third-party RoBERTa detectors at 16/16 oracle-equivalence (57% NYT-FPR reduction on the OpenAI detector). Scope: encoder family; mechanism magnitude HC3-anchored; population-level shared axis with per-text mechanisms varying across architectures. Three operationally distinct probes -- text-surface caps_rate residualisation, geometric signed-epsilon ablation, closed-form text-pair predictor -- agree at cos 0.74/0.81/1.00 across three architectures, confirming observer-invariance. Under matched-TPR-0.90 evaluation, the published intervention zoo (CC, dealign-f2c) is calibration-equivalent across 27 cells (|Delta AUROC| <= 0.0081), and >= 97% of the LoRA->full-FT bias gap on ELECTRA is calibration shift, not learned representation -- the central claim's prediction confirmed.

---


### 34. [Hierarchical Variational Policies for Reward-Guided Diffusion](https://arxiv.org/abs/2605.21661)

**<font color=#1a73e8>作者：</font>** Kushagra Pandey, Farrin Marouf Sofian, Jan Niklas Groeneveld 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting pretrained diffusion models to downstream objectives such as inverse problems often requires expensive test-time guidance or optimization. We propose a principled framework for generating high-quality reward-aligned samples at substantially reduced inference cost. Our approach formulates test-time adaptation as a hierarchical variational model, where control is amortized into a lightweight yet expressive stochastic policy. This formulation naturally supports few-step diffusion sampling: large step sizes enable fast inference, while the learned policy maintains sample quality by providing structured per-step control. The resulting fully amortized sampler achieves a strong quality--speed tradeoff, matching or exceeding recent test-time scaling baselines while requiring significantly less compute. For example, on 4x super-resolution, our method achieves better perceptual quality with more than 5x faster inference compared to the best-performing baseline. We further extend our approach to a semi-amortized regime that combines cheap amortized proposals with limited test-time optimization, achieving state-of-the-art perceptual quality across several challenging inverse problems.

---


### 35. [Planning, Scheduling, and Behavior in EV Charging Systems: A Critical Survey and Trilemma Framework](https://arxiv.org/abs/2605.21665)

**<font color=#1a73e8>作者：</font>** Peiyan Xiao, Yuheng Li, Ayan Mukhopadhyay 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The rapid growth of electric vehicles is shifting the main constraint on transport electrification from vehicle adoption to the deployment and operation of charging infrastructure. Charging-network design requires decisions across three interdependent layers: Planning, which determines where and how much infrastructure to build; Scheduling, which governs charging dispatch, pricing, and grid interaction; and Behavior, which captures how users choose stations, charging times, and charging durations. Existing studies have advanced each layer substantially, but the literature remains fragmented, and cross-layer interactions are often treated through simplifying assumptions. This survey develops a three-layer Planning-Scheduling-Behavior (PSB) framework to organize EV charging research according to decision horizon, actor objective, and coupling structure. We further identify a fidelity-tractability tradeoff, termed the PSB trilemma: each layer is computationally difficult in isolation, and realistic integration across layers generally requires reducing the fidelity of at least one layer. Reviewing the three pairwise-coupling literatures - Planning-Scheduling, Scheduling-Behavior, and Planning-Behavior - we show that the omitted third layer is typically fixed exogenously or represented by a static aggregate surrogate. These simplifications enable tractability but impose distinct costs: they can obscure long-term investment feedback, temporal grid and emissions dynamics, or heterogeneous user response and equity outcomes. Building on this diagnosis, we identify open challenges in emerging charging technologies, behavioral incentives, equity metrics, and city-scale learning-based methods that balance fidelity, interpretability, and policy relevance.

---


### 36. [MRecover: A Conditional Generative Model for Recovering Motion-Corrupted MR images Using AI Generated Contrast](https://arxiv.org/abs/2605.21669)

**<font color=#1a73e8>作者：</font>** Jinghang Li, Tales Santini, Courtney Clark 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hippocampal subfield segmentation requires high-resolution T2w turbo spin echo (TSE) MRI, yet this sequence is susceptible to motion artifacts, leading to substantial data loss. We developed a conditional generative model (MRecover) that synthesizes routinely acquired T1w images to create TSE images with autoregressive slice conditioning for volumetric consistency. Trained on 7T MRI data (n=577), the model achieved high in-domain fidelity (n=148, SSIM=0.84, FSIM=0.94) and generalized well to out-of-domain 3T data: subfield volumes from synthesized and the as-acquired images closely matched: (n=416, r=0.87-0.97) and yielded 31.8% more analyzable subjects in the motion-affected ADNI3 dataset after quality control (593 vs 450). The synthesized images also achieved larger effect sizes due to increasing the sample size for diagnostic group differences in hippocampal subfield atrophy (whole hippocampus $\epsilon^2$= 0.121-0.100 vs. 0.086-0.062, left-right hemispheres). Project page: this https URL

---


### 37. [Representation Gap: Explaining the Unreasonable Effectiveness of Neural Networks from a Geometric Perspective](https://arxiv.org/abs/2605.21692)

**<font color=#1a73e8>作者：</font>** David Perera, Victor Moura, Lais Isabelle Alves dos Santos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Characterizing precisely the asymptotic generalization error of neural networks using parameters that can be estimated efficiently is a crucial problem in machine learning, which relies heavily on heuristics and practitioners' intuition to make key design choices. In order to mitigate this issue, we introduce the Representation Gap, a metric closely related to the generalization error, but admitting better-behaved asymptotic dynamics. Focusing on equivariant diffusion models and leveraging results from optimal quantization and point-process theory, we derive a precise asymptotic equivalent of the Representation Gap and show that it is governed by a single parameter, the \textit{intrinsic dimension} of the task, which is easy to interpret, efficient to estimate, and can be linked to the equivariances of common neural network architectures. We show that this asymptotic dynamic also extends to a broader range of tasks and training algorithms. Finally, we demonstrate empirically that our asymptotic law and intrinsic dimension estimation are accurate on a wide range of synthetic datasets, where these quantities are known, as well as on more realistic datasets, where we obtain results consistent with the related literature.

---


### 38. [PocketAgents: A Manifest-Driven Library of Autonomous Defense Agents](https://arxiv.org/abs/2605.21694)

**<font color=#1a73e8>作者：</font>** Sidnei Barbieri, Ágney Lopes Roth Ferraz, Lourenço Alves Pereira Júnior  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Connecting large language models (LLMs) to defensive enforcement requires more than asking a model whether an attack is happening. A defender must decide which model outputs may change the system state, which outputs must be rejected, and how failures should be recorded. We present PocketAgents, a manifest-driven library of autonomous defense agents. Each agent is installed as three data files: a manifest, a prompt, and a runtime context. The shared runtime gives the agent bounded telemetry access and accepts only typed reports whose requested action appears in the manifest. We implemented PocketAgents on top of a cyber arena (Perry), a cyber-deception testbed, and evaluated two agents, Command and Control and Exfiltration, in 18 closed-loop trials of a DarkSide-inspired attack on a small enterprise topology. Thirteen trials produced validated network-block actions and contained the attack; four failed schema validation; one produced a valid no-action decision. The experiments show that a typed boundary makes LLM-driven defense measurable, extensible, and attributable.

---


### 39. [The Impact of AI Usage and Informativeness on Skill Development in Logical Reasoning](https://arxiv.org/abs/2605.21695)

**<font color=#1a73e8>作者：</font>** Shang Wu, Hongyu Yao, Catarina Belem 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) is being increasingly integrated into human problem-solving, yet its effects on individual skill development remain unclear. We examine how both AI usage and informativeness can shape learning in the context of a controlled logical reasoning task with on-demand access to AI assistance. We find that greater AI usage is associated with weaker skill development: heavy AI users underperform relative to comparable peers, whereas light AI users perform similarly to matched users who do not use AI. We also find in our study that these patterns are mediated by AI informativeness. Low-information AI neither improves immediate performance nor preserves performance after AI assistance is removed, and is linked to weaker learning overall. On the other hand, high-information AI was found to improve short-run performance without reducing post-AI outcomes on average in our experiments, but with heterogeneous effects. Our findings in general suggest that AI can, depending on context, either complement human skill development by amplifying independent reasoning or can act as a substitute that undermines such reasoning, with the implication that regulating AI access and usage will be important for promoting skill development in the presence of AI assistance.

---


### 40. [Broadening Access to Transportation Safety Data with Generative AI: A Schema-Grounded Framework for Spatial Natural Language Queries](https://arxiv.org/abs/2605.21712)

**<font color=#1a73e8>作者：</font>** Mahdi Azhdari, Eric J. Gonzales  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transportation safety analysis requires integrating crash records, roadway attributes, and geospatial data through GIS-based workflows, but access remains uneven across agencies and community stakeholders. Technical prerequisites create a gap between analytical tools central to safety planning and the practitioners able to use them. Local agencies, school committees, and residents may have safety concerns but limited capacity to retrieve, filter, map, and analyze relevant data. Generative AI offers a way to narrow this divide, but its public-sector use raises questions about reliability, reproducibility, and governance. This paper presents a schema-grounded natural language interface for transportation safety analysis, using a large language model (LLM) to interpret user intent while preserving deterministic, reviewable execution against an authoritative database. User queries are translated into structured semantic frames, validated by a rule-based layer, compiled into a typed directed acyclic graph of spatial operations, and executed against a PostGIS database. This bounded design separates language interpretation from deterministic execution, keeping results reproducible and schema-grounded while removing access barriers. The framework is evaluated using a statewide Massachusetts transportation safety database integrating crash records, roadway attributes, and geospatial layers including schools, bus stops, crosswalks, and municipal boundaries. All queries executed successfully; the validation layer corrects errors in 29% of evaluation queries, reflecting the gap between flexible natural language and strict schema-grounded requirements. The results suggest that combining natural language accessibility with deterministic execution is a practical direction for broadening access to transportation safety data, with implications for trustworthy AI in public-sector planning.

---


### 41. [Sem-Detect: Semantic Level Detection of AI Generated Peer-Reviews](https://arxiv.org/abs/2605.21713)

**<font color=#1a73e8>作者：</font>** André V. Duarte, Brian Tufts, Aditya Oke 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How can we distinguish whether a peer review was written by a human or generated by an AI model? We argue that, in this setting, authorship should not be attributed solely from the textual features of a review, but also from the ideas, judgments, and claims it expresses. To this end, we propose Sem-Detect, an authorship detection method for peer reviews that operationalizes this principle by combining textual features with claim-level semantic analysis. Sem-Detect compares a target review against multiple AI-generated reviews of the same paper, leveraging the observation that different AI models tend to converge on similar points, while human reviewers introduce more unique and diverse ones. As a result, Sem-Detect is able to distinguish fully AI reviews from authentic human-written ones, including those that have been refined using an LLM but still reflect human judgment. Across a dataset of over 20,000 peer reviews from ICLR and NeurIPS conferences, Sem-Detect improves over the strongest baseline by 25.5% in TPR@0.1% FPR in the binary setting. Moreover, in the three-class scenario, we empirically show that LLM refinement preserves the semantic signals of human reviews, which remain distinct from the patterns exhibited by fully AI-generated text; as a result, fewer than 3.5% of LLM-refined human reviews are misclassified as AI-generated.

---


### 42. [AVI-HT: Adaptive Vision-IMU Fusion for 3D Hand Tracking](https://arxiv.org/abs/2605.21714)

**<font color=#1a73e8>作者：</font>** Ziyi Kou, Ankit Kumar, Mia Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present AVI-HT, an adaptive visual-IMU fusion approach for tracking 3D hand poses by jointly modeling the egocentric image with on-glove 6-DoF IMU signals. AVI-HT achieves significantly improved accuracy and availability, particularly in hand-object interaction (HOI) scenarios involving heavy visual occlusion. Two complementary ingredients underpin its success: (1) synchronized multi-modal training data pairing on-body vision-IMU sensor streams with ground-truth 3D hand poses from a motion-capture system, and (2) a cross-sensor deep attention mechanism that adaptively modulates the trust assigned to the vision and individual IMU sensors. To evaluate AVI-HT in real-world settings, we conduct extensive experiments on our DexGloveHOI dataset that consists of 100K+ pairwise vision-IMU samples with synchronized 3D annotated poses, in which users manipulate a variety of objects during daily tasks. We compare against multiple single- and multi-modal tracking approaches under two hand models (UmeTrack, MANO). The results show that AVI-HT reduces mean keypoint error by 16.1% and its wrist-aligned variant by 24.2% over the baselines. Ablation studies further reveal the per-finger contribution of IMU sensors across activity types, and the model's sensitivity to IMU noise and temporal misalignment in vision-IMU fusion.

---


### 43. [TBP-mHC: full expressivity for manifold-constrained hyper connections through transportation polytopes](https://arxiv.org/abs/2605.21724)

**<font color=#1a73e8>作者：</font>** Anton Lyubinin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyper-Connections (HC) improve residual networks by introducing learnable mixing across multiple residual streams, but unconstrained mixing leads to training instability. Manifold-Constrained Hyper-Connections (mHC) address this by enforcing approximate double stochasticity via Sinkhorn normalization, while mHC-lite ensures exact constraints through convex combinations of permutation matrices at the cost of factorial complexity. KromHC reduces this cost using Kronecker-product parameterizations, but restricts the mixing matrices to a structured submanifold of the Birkhoff polytope .
We propose Transportation Birkhoff Polytope (TBP) parameterizations and their Recursive variants (RTBP), which construct exactly doubly stochastic mixing matrices with $(n-1)^2$ degrees of freedom. Our approach avoids iterative normalization and combinatorial explosion while preserving full expressivity of the Birkhoff polytope. Empirical results on language model pre-training' demonstrate competitive performance with improved stability and scalability.

---


### 44. [I-SAFE: Wasserstein Coherence Metrics for Structural Auditing of Scientific AI Models](https://arxiv.org/abs/2605.21731)

**<font color=#1a73e8>作者：</font>** Barbara Tarantino, Gennaro Auricchio, Paolo Giudici  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models are increasingly used in scientific prediction tasks where strong benchmark performance is often interpreted as evidence of scientifically meaningful behavior. This interpretation is fragile, as models may exploit shortcut features, dataset-specific regularities, or distributional biases that are predictive on held-out data but not aligned with domain-relevant structure. To address this limitation, we introduce the \textsc{I-SAFE} (Interventional Secure, Accurate, Fair and Explainable) framework, a post-hoc distributional auditing framework for scientific AI models centered on the Wasserstein Coherence Metric (WCM). Given a trained black-box predictor and an external structural prior encoding domain knowledge about task-relevant input structure, \textsc{I-SAFE} evaluates raw model outputs under structurally guided perturbations of the input. The proposed audit measures output-distribution coherence through three complementary metrics: a Quantile-Based Metric (QBM) for location-level coherence, the WCM for ordinal coherence, and a translation-invariant WCM variant for shape coherence. We instantiate \textsc{I-SAFE} on drug--target interaction (DTI) prediction using the Davis kinase benchmark, KLIFS (Kinase--Ligand Interaction Fingerprints and Structures) binding-pocket annotations, and three sequence-based DTI models: DeepConvDTI, DeepDTA, and TAPB. Although the models operate in a comparable predictive regime, \textsc{I-SAFE} reveals substantially different distributional response profiles, a distinction invisible to accuracy-based evaluation. The framework is model-agnostic and applicable to any domain where inputs admit a structured decomposition and an external prior is available.

---


### 45. [Correcting Class Imbalance in Prior-Data Fitted Networks for Tabular Classification](https://arxiv.org/abs/2605.21742)

**<font color=#1a73e8>作者：</font>** Samuel McDowell, Nathan Stromberg, Lalitha Sankar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior-data fitted networks (PFNs) have achieved exceptional performance on tabular classification tasks. However, like other classifiers, their performance can suffer under the effect of class imbalance, resulting in poor performance for rare classes. Several techniques exist which attempt to mitigate the deleterious effect of class imbalance on classification performance, but the in-context learning (ICL) dynamic of PFNs means that loss-based strategies are impossible, and other techniques are unproven. We have adapted several classical techniques addressing class imbalance and analyzed their performance on PFN classification. We observe that thresholding performs exceptionally well because of the calibration characteristics of PFNs, and downsampling performs comparably because of PFNs exceptional limited-data performance, with the additional benefit of reduced computation cost for inference.

---


### 46. [Who Uses AI? Platforms, Workforce, and AI Exposure](https://arxiv.org/abs/2605.21743)

**<font color=#1a73e8>作者：</font>** Michelle Yin, Burhan Ogut  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A growing literature uses artificial intelligence platform conversation logs to measure occupation exposure. We show that these scores partly measure platform user base rather than the workforce. Holding outcome, sample, controls, and estimator fixed while varying only the platform input changes the post-ChatGPT employment coefficient by a factor of 1.9, and within-vendor consumer-versus-enterprise channels produce estimates that disagree in sign. Reweighting to Bureau of Labor Statistics workforce shares attenuates estimates by 42 to 93 percent. We formalize the non-classical measurement error, derive probability limits and partial-identification bounds for employment elasticities. The bias understates substitution more than augmentation.

---


### 47. [Quantitative coronary calcification analysis for prediction of myocardial ischemia using non-contrast CT calcium scoring](https://arxiv.org/abs/2605.21745)

**<font color=#1a73e8>作者：</font>** Juhwan Lee, Sadeer Al-Kindi, Ammar Hoori 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-contrast computed tomography calcium scoring (CTCS) is widely recognized as an effective tool for cardiovascular risk stratification. This study aimed to develop a novel machine learning framework for predicting myocardial ischemia from routine non-contrast CTCS scans using quantitative coronary calcium assessment. This study analyzed 1,375 patients who underwent both non-contrast CTCS and regadenoson stress cardiac positron emission tomography myocardial perfusion imaging within one year at University Hospitals Cleveland Medical Center. A total of 74 variables, including clinical variables, Agatston score, and calcium-omics features, were evaluated. Relevant features were identified using XGBoost with Shapley Additive exPlanations (SHAP). Predictive models were trained and evaluated using 5-fold cross-validation. Among 987 patients, 89 (9%) were positive for myocardial ischemia. The final model incorporated the Agatston score, eight calcium-omics features, and age. The proposed model achieved a precision of 98.9+/-3.0%, sensitivity of 79.2+/-8.4, and F1 score of 87.7+/-5.3%. The addition of calcium-omics features significantly improved predictive performance compared with models using clinical variables alone or clinical variables with the Agatston score (p<0.05). Interestingly, the number of calcified arteries, despite being the lowest-ranked feature based on SHAP analysis, showed the strongest association with myocardial ischemia in logistic regression analysis (odds ratio: 3.63, 95% confidence interval: 2.80-4.77, p<0.00001). We developed a machine learning approach for predicting myocardial ischemia using routinely acquired non-contrast CTCS scans. Calcium-omics features provided incremental predictive value beyond conventional risk factors and Agatston scoring and may support more accessible cardiovascular risk stratification.

---


### 48. [Models Can Model, But Can't Bind: Structured Grounding in Text-to-Optimization](https://arxiv.org/abs/2605.21751)

**<font color=#1a73e8>作者：</font>** Zhiqi Gao, Albert Ge, Alexander Berenbeim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-to-optimization requires two separable capabilities: modeling -- choosing the right optimization structure -- and binding -- grounding every coefficient, index, and parameter in the concrete problem data. We study this via Text2Opt-Bench, a scalable benchmark of solver-verified optimization problems spanning 12 categories, from textbook linear programs to stochastic and multi-objective formulations with up to thousands of variables. Across 10+ models, we find that accuracy collapses as instance data grows, even when the formulation itself is simple. We call this the effective binding limit. We address this via a simple inference-time approach, BIND, which externalizes numeric data to structured files so the model binds data programmatically rather than transcribing from the prompt. BIND improves GPT-5-Nano from 59.1% to 82.4% accuracy, matching pass@5 (82.0%) at lower token cost than pass@1, and GPT-5 from 86.2% to 95.8%. Furthermore, we validate our hypothesis by finetuning a model exclusively on binding and show that it outperforms end-to-end SFT and RL across three structurally distinct optimization categories, with a 1.5B binding specialist alone matching a 7B end-to-end baseline.

---


### 49. [PEARL: Unbiased Percentile Estimation via Contrastive Learning for Industrial-Scale Livestream Recommendation](https://arxiv.org/abs/2605.21752)

**<font color=#1a73e8>作者：</font>** Blake Gella, Wei Wu, Yuhao Yin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recommender systems trained on user interaction data are susceptible to behavioral intensity imbalance--a systematic distortion arising from heterogeneous engagement patterns across users. This imbalance skews feedback signals such that observed interactions no longer faithfully reflect true preferences, causing models to disproportionately amplify signals from highly active users while underrepresenting others, which ultimately degrades recommendation quality and robustness at scale. To address this issue, we propose a nonparametric contrastive percentile approximation framework, PEARL, that models relative preference signals instead of absolute engagement magnitudes. Building upon relative advantage debiasing, PEARL leverages real contrastive interaction samples to approximate percentile relationships directly, without relying on auxiliary distribution estimation models. We provide theoretical justification demonstrating that such pairwise comparisons yield unbiased estimates of percentile-based preference signals. For broader applicability, we introduce a prediction-based bootstrapping mechanism for percentile smoothing to handle sparse and discrete feedback, alongside a generalized value-weighted formulation and a co-training strategy to enhance both modeling flexibility and representation learning. Extensive offline experiments demonstrate that PEARL effectively mitigates behavioral bias and consistently improves recommendation performance across multiple ranking targets. Deployed in a production livestream platform with a combined user base of billions, online A/B testing confirms substantial real-world gains: +2.10% Watch Duration, +0.80% Consumption Amount, +1.49% Interaction Rate, and -6.91% Report Rate.

---


### 50. [A Causal Argumentation Method for Explainability of Machine Learning Models](https://arxiv.org/abs/2605.21758)

**<font color=#1a73e8>作者：</font>** Henry Salgado, Meagan R. Kendall, Martine Ceberio  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) methods identify which features are relevant to a model's predictions but often fail to clarify why certain decisions are made. In this work, we present a novel method that integrates causality with argument-based reasoning to explain why models may be making predictions. Our approach first identifies causal relationships among variables using causal discovery methods and then translates these into a Bipolar Argumentation Framework (BAF) to represent supportive and opposing interactions among features. By using semi-stable semantics, we find extensions of features that explain why certain outcomes may have been chosen. We demonstrate our method on two benchmark datasets and compare its results against standard post-hoc explainability approaches.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-347](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
