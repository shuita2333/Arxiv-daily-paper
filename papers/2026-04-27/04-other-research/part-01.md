# 📦 其他研究 | 2026年04月27日

> 本类共 **231** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-231](./part-05.md)

---

### 1. [Architecture of an AI-Based Automated Course of Action Generation System for Military Operations](https://arxiv.org/abs/2604.20862)

**<font color=#1a73e8>作者：</font>** Ji-il Park, Inwook Shim, Chong Hui Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The automation system for Course of Action (CoA) planning is an essential element in future warfare. As maneuver speeds increase, surveillance ranges extend, and weapon ranges grow, the operational area expands, making traditional manned-based CoA planning increasingly challenging. Consequently, the development of an AI-based automated CoA planning system is becoming increasingly necessary. Accordingly, several countries and defense organizations are actively developing AI-based CoA planning systems. However, due to security restrictions and limited public disclosure, the technical maturity of such systems remains difficult to assess. Furthermore, as these systems are military-related, their details are not publicly disclosed, making it difficult to accurately assess the current level of development. In response to this, this study aims to introduce relevant doctrines within the scope of publicly available information and present applicable AI technologies for each stage of the CoA planning process. Ultimately, it proposes an architecture for the development of an automated CoA planning system.

---


### 2. [Towards a Systematic Risk Assessment of Deep Neural Network Limitations in Autonomous Driving Perception](https://arxiv.org/abs/2604.20895)

**<font color=#1a73e8>作者：</font>** Svetlana Pavlitska, Christopher Gerking, J. Marius Zöllner  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety and security are essential for the admission and acceptance of automated and autonomous vehicles. Deep neural networks (DNNs) are widely used for perception and further components of the autonomous driving (AD) stack. However, they possess several limitations, including lack of generalization, efficiency, explainability, plausibility, and robustness. These insufficiencies can pose significant risks to autonomous driving systems. However, hazards, threats, and risks associated with DNN limitations in this domain have not been systematically studied so far. In this work, we propose a joint workflow for risk assessment combining the hazard analysis and risk assessment (HARA) following ISO 26262 and threat analysis and risk assessment (TARA) following the ISO/SAE 21434 to identify and analyze risks arising from inherent DNN limitations in AD perception.

---


### 3. [Frequency-Forcing: From Scaling-as-Time to Soft Frequency Guidance](https://arxiv.org/abs/2604.20902)

**<font color=#1a73e8>作者：</font>** Weitao Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While standard flow-matching models transport noise to data uniformly, incorporating an explicit generation order - specifically, establishing coarse, low-frequency structure before fine detail - has proven highly effective for synthesizing natural images. Two recent works offer distinct paradigms for this. K-Flow imposes a hard frequency constraint by reinterpreting a frequency scaling variable as flow time, running the trajectory inside a transformed amplitude space. Latent Forcing provides a soft ordering mechanism by coupling the pixel flow with an auxiliary semantic latent flow via asynchronous time schedules, leaving the pixel interpolation path itself untouched. Viewed from the angle of improving pixel generation, we observe that forcing - guiding generation with an earlier-maturing auxiliary stream - offers a highly compatible route to scale-ordered generation without rewriting the core flow coordinate. Building on this, we propose Frequency-Forcing, which realizes K-Flow's frequency ordering through Latent Forcing's soft mechanism: a standard pixel flow is guided by an auxiliary low-frequency stream that matures earlier in time. Unlike Latent Forcing, whose scratchpad relies on a heavy pretrained encoder (e.g., DINO), our frequency scratchpad is derived from the data itself via a lightweight learnable wavelet packet transform. We term this a self-forcing signal, which avoids external dependencies while learning a basis better adapted to data statistics than the fixed bases used in hard frequency flows. On ImageNet-256, Frequency-Forcing consistently improves FID over strong pixel- and latent-space baselines, and naturally composes with a semantic stream to yield further gains. This illustrates that forcing-based scale ordering is a versatile, path-preserving alternative to hard frequency flows.

---


### 4. [Do Masked Autoencoders Improve Downhole Prediction? An Empirical Study on Real Well Drilling Data](https://arxiv.org/abs/2604.20909)

**<font color=#1a73e8>作者：</font>** Aleksander Berezowski, Hassan Hassanzadeh, Gouri Ginde  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Downhole drilling telemetry presents a fundamental labeling asymmetry: surface sensor data are generated continuously at 1~Hz, while labeled downhole measurements are costly, intermittent, and scarce. Current machine learning approaches for downhole metric prediction universally adopt fully supervised training from scratch, which is poorly suited to this data regime. We present the first empirical evaluation of masked autoencoder (MAE) pretraining for downhole drilling metric prediction. Using two publicly available Utah FORGE geothermal wells comprising approximately 3.5 million timesteps of multivariate drilling telemetry, we conduct a systematic full-factorial design space search across 72 MAE configurations and compare them against supervised LSTM and GRU baselines on the task of predicting Total Mud Volume. Results show that the best MAE configuration reduces test mean absolute error by 19.8\% relative to the supervised GRU baseline, while trailing the supervised LSTM baseline by 6.4\%. Analysis of design dimensions reveals that latent space width is the dominant architectural choice (Pearson $r = -0.59$ with test MAE), while masking ratio has negligible effect, an unexpected finding attributed to high temporal redundancy in 1~Hz drilling data. These results establish MAE pretraining as a viable paradigm for drilling analytics and identify the conditions under which it is most beneficial.

---


### 5. [Forget, Then Recall: Learnable Compression and Selective Unfolding via Gist Sparse Attention](https://arxiv.org/abs/2604.20920)

**<font color=#1a73e8>作者：</font>** Yuzhen Mao, Michael Y. Li, Emily B. Fox  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling large language models to long contexts is challenging due to the quadratic computational cost of full attention. Mitigation approaches include KV-cache selection or compression techniques. We instead provide an effective and end-to-end learnable bridge between the two without requiring architecture modification. In particular, our key insight is that interleaved gist compression tokens -- which provide a learnable summary of sets of raw tokens -- can serve as routing signals for sparse attention. Building on this, we introduce selective unfolding via GSA, which first compresses the context into gist tokens, then selects the most relevant gists, and subsequently restores the corresponding raw chunks for detailed attention. This yields a simple coarse-to-fine mechanism that combines compact global representations with targeted access to fine-grained evidence. We further incorporate this process directly into training in an end-to-end fashion, avoiding the need for external retrieval modules. In addition, we extend the framework hierarchically via recursive gist-of-gist construction, enabling multi-resolution context access with logarithmic per-step decoding complexity. Empirical results on LongBench and RAG benchmarks demonstrate that our method consistently outperforms other compression baselines as well as inference-time sparse attention methods across compression ratios from $8\times$ to $32\times$. The code is available at: this https URL

---


### 6. [Validating a Deep Learning Algorithm to Identify Patients with Glaucoma using Systemic Electronic Health Records](https://arxiv.org/abs/2604.20921)

**<font color=#1a73e8>作者：</font>** John Xiang, Rohith Ravindranath, Sophia Y. Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We evaluated whether a glaucoma risk assessment (GRA) model trained on All of Us national data can identify patients at high probability of glaucoma using only systemic electronic health records (EHR) at an independent institution. In this cross-sectional study, 20,636 Stanford patients seen from November 2013 to January 2024 were included (15% with glaucoma). A pretrained GRA model was fine-tuned on the Stanford cohort and tested on a held-out set using demographics, systemic diagnoses, medications, laboratory results, and physical examination measurements as inputs. The best model achieved AUROC 0.883 and PPV 0.657. Calibration was consistent with clinical risk: the highest prediction decile showed the greatest glaucoma diagnosis rate (65.7%) and treatment rate (57.0%). Performance improved with more trainable layers up to 15 and with additional data. An EHR-only GRA model may enable scalable and accessible pre-screening without specialized imaging.

---


### 7. [ILDR: Geometric Early Detection of Grokking](https://arxiv.org/abs/2604.20923)

**<font color=#1a73e8>作者：</font>** Shreel Golwala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking describes a delayed generalization phenomenon in which a neural network achieves perfect training accuracy long before validation accuracy improves, followed by an abrupt transition to strong generalization. Existing detection signals are indirect: weight norm reflects parameter-space regularization and consistently lags the transition, while GrokFast's slow gradient EMA, used without gradient amplification, is unstable across seeds with standard deviation exceeding mean lead time. We propose the Inter/Intra-class Distance Ratio (ILDR), a geometric metric computed on second-to-last layer representations as the ratio of inter-class centroid separation to intra-class scatter. ILDR provides an early detection signal: it rises and crosses a threshold at 2.5 times its baseline before the grokking transition appears in validation accuracy, indicating early geometric reorganization in representation space. Grounded in Fisher's linear discriminant criterion, ILDR requires no eigendecomposition and runs in O(|C|^2 + N). It is evaluated exclusively on held-out data, making it robust to memorization effects. Across modular arithmetic and permutation group composition (S5), ILDR leads the grokking transition by 9 to 73 percent of the training budget, with lead time increasing with task algebraic complexity. Over eight random seeds, ILDR leads by 950 +/- 250 steps with a coefficient of variation of 26 percent, and post-grokking variance drops by 1696 times, consistent with a sharp phase transition in representation space. Using ILDR as an early stopping trigger reduces training by 18.6 percent on average. Optimizer interventions triggered at the ILDR threshold demonstrate bidirectional control over the transition, suggesting ILDR tracks representational conditions underlying generalization rather than a downstream correlate.

---


### 8. [Unsupervised Learning of Inter-Object Relationships via Group Homomorphism](https://arxiv.org/abs/2604.20925)

**<font color=#1a73e8>作者：</font>** Kyotaro Ushida, Takayuki Komatsu, Yoshiyuki Ohmura 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While current deep learning models achieve high performance by learning statistical correlations from vast datasets,which stands in stark contrast to human learning. They lack the flexibility of humans-particularly preverbal infants-to autonomously acquire the underlying structure of the world from limited experience and adapt to novel situations. In this study, we propose an unsupervised representation learning method based on a hierarchical relationship in group operations, rather than statistical independence, aiming to build a computational model of the cognitive development of infants. The proposed model features an integrated architecture that simultaneously performs object segmentation and the extraction of motion laws from dynamic image sequences. By introducing the Homomorphism from algebra as a structural constraint within a neural network, the model structurally separates pixel-level changes into meaningful, decomposed transformation components, such as translation and deformation. Using interaction scenes (chasing and evading tasks) based on developmental science findings, we experimentally demonstrate that the model can segment multiple objects into individual slots without any ground-truth labels. Furthermore, we confirmed that relative movements between objects, such as approaching or receding, are accurately mapped and structured into a one-dimensional additive latent space. These results suggest that by introducing algebraic geometric constraints rather than relying solely on statistical correlation learning, physically interpretable "disentangled representations" can be acquired. This study contributes to the understanding of the process by which infants internalize environmental laws as structures and provides a new perspective for constructing artificial systems with developmental intelligence.

---


### 9. [Hidden Secrets in the arXiv: Discovering, Analyzing, and Preventing Unintentional Information Disclosure in Source Files of Scientific Preprints](https://arxiv.org/abs/2604.20927)

**<font color=#1a73e8>作者：</font>** Jan Pennekamp, Johannes Lohmöller, David Schütte 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Preprints are essential for the timely and open dissemination of research. arXiv, the most widely used preprint service, takes the idea of open science one step further by not only publishing the actual preprints but also LaTeX sources and other files used to create them. As known from other contexts, such as GitHub repositories, and anecdotally exemplified for arXiv, making source code publicly available risks disclosing otherwise "hidden" information. Consequently, the public availability of paper sources raises the question of how much sensitive content is (unintentionally) disclosed through them.
In this paper, we systematically answer this question for all 2.7M arXiv submissions with available source files across three dimensions of source file-induced information disclosure: (1) inclusion of unnecessary files, (2) metadata embedded in files, and (3) irrelevant content in files such as source code comments. Our analysis reveals that nearly every arXiv submission contains some form of "hidden" information. Notable findings range from links to editable web documents for internal coordination over API and private keys to complete Git histories.
While different tools promise to remove such information from source files, we show that they fail to reliably achieve the intended cleaning functionality. To mitigate this situation, we provide ALC-NG to comprehensively remove files, metadata, and comments that are not needed to compile a LaTeX paper.

---


### 10. [Domain-Aware Hierarchical Contrastive Learning for Semi-Supervised Generalization Fault Diagnosis](https://arxiv.org/abs/2604.20928)

**<font color=#1a73e8>作者：</font>** Junyu Ren, Wensheng Gan, Philip S Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fault diagnosis under unseen operating conditions remains highly challenging when labeled data are scarce. Semi-supervised domain generalization fault diagnosis (SSDGFD) provides a practical solution by jointly exploiting labeled and unlabeled source domains. However, existing methods still suffer from two coupled limitations. First, pseudo-labels for unlabeled domains are typically generated primarily from knowledge learned on the labeled source domain, which neglects domain-specific geometric discrepancies and thus induces systematic cross-domain pseudo-label bias. Second, unlabeled samples are commonly handled with a hard accept-or-discard strategy, where rigid thresholding causes imbalanced sample utilization across domains, while hard-label assignment for uncertain samples can easily introduce additional noise. To address these issues, we propose a unified framework termed domain-aware hierarchical contrastive learning (DAHCL) for SSDGFD. Specifically, DAHCL introduces a domain-aware learning (DAL) module to explicitly capture source-domain geometric characteristics and calibrate pseudo-label predictions across heterogeneous source domains, thereby mitigating cross-domain bias in pseudo-label generation. In addition, DAHCL develops a hierarchical contrastive learning (HCL) module that combines dynamic confidence stratification with fuzzy contrastive supervision, enabling uncertain samples to contribute to representation learning without relying on unreliable hard labels. In this way, DAHCL jointly improves the quality of supervision and the utilization of unlabeled samples. Furthermore, to better reflect practical industrial scenarios, we incorporate engineering noise into the SSDGFD evaluation protocol. Extensive experiments on three benchmark datasets demonstrate that...

---


### 11. [SDNGuardStack: An Explainable Ensemble Learning Framework for High-Accuracy Intrusion Detection in Software-Defined Networks](https://arxiv.org/abs/2604.20934)

**<font color=#1a73e8>作者：</font>** Ashikuzzaman, Md. Saifuzzaman Abhi, Mahabubur Rahman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software-Defined Networking (SDN) is another technology that has been developing in the last few years as a relevant technique to improve network programmability and administration. Nonetheless, its centralized design presents a major security issue, which requires effective intrusion detection systems. The SDN-specific machine learning-based intrusion detection system described in this paper is innovative because it is trained and tested on the InSDN dataset which models attack scenarios and realistic traffic patterns in SDN. Our approach incorporates a comprehensive preprocessing pipeline, feature selection via Mutual Information, and a novel ensemble learning model, SDNGuardStack, which combines multiple base learners to enhance detection accuracy and efficiency. In addition, we include explainable AI methods, including SHAP to add transparency to model predictions, which helps security analysts respond to incidents. The experiments prove that SDNGuard-Stack has an accuracy rate of 99.98% and a Cohen Kappa of 0.9998, surpassing other models, and at the same time being interpretable and practically executable. It is interesting to see such features like Flow ID, Bwd Header Len, and Src Port as the most important factors in the model predictions. The work is a step towards closing the gap between performance intrusion detection and realistic deployment in SDN, which will lead to the creation of secure and resilient network infrastructures.

---


### 12. [Data-Driven Open-Loop Simulation for Digital-Twin Operator Decision Support in Wastewater Treatment](https://arxiv.org/abs/2604.20935)

**<font color=#1a73e8>作者：</font>** Gary Simethy, Daniel Ortiz Arroyo, Petar Durdevic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wastewater treatment plants (WWTPs) need digital-twin-style decision support tools that can simulate plant response under prescribed control plans, tolerate irregular and missing sensing, and remain informative over 12-36 h planning horizons. Meeting these requirements with full-scale plant data remains an open engineering-AI challenge. We present CCSS-RS, a controlled continuous-time state-space model that separates historical state inference from future control and exogenous rollout. The model combines typed context encoding, gain-weighted forcing of prescribed and forecast drivers, semigroup-consistent rollouts, and Student-t plus hurdle outputs for heavy-tailed and zero-inflated WWTP sensor data. On the public Avedøre full-scale benchmark, with 906,815 timesteps, 43% missingness, and 1-20 min irregular sampling, CCSS-RS achieves RMSE 0.696 and CRPS 0.349 at H=1000 across 10,000 test windows. This reduces RMSE by 40-46% relative to Neural CDE baselines and by 31-35% relative to simplified internal variants. Four case studies using a frozen checkpoint on test data demonstrate operational value: oxygen-setpoint perturbations shift predicted ammonium by -2.3 to +1.4 over horizons 300-1000; a smoothed setpoint plan ranks first in multi-criterion screening; context-only sensor outages raise monitored-variable RMSE by at most 10%; and ammonium, nitrate, and oxygen remain more accurate than persistence throughout the rollout. These results establish CCSS-RS as a practical learned simulator for offline scenario screening in industrial wastewater treatment, complementary to mechanistic models.

---


### 13. [HARBOR: Automated Harness Optimization](https://arxiv.org/abs/2604.20938)

**<font color=#1a73e8>作者：</font>** Biswa Sengupta, Jinhua Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon language-model agents are dominated, in lines of code and in operational complexity, not by their underlying model but by the harness that wraps it: context compaction, tool caching, semantic memory, trajectory reuse, speculative tool prediction, and the glue that binds the model to a sandboxed execution environment. We argue that harness design is a first-class machine-learning problem and that automated configuration search dominates manual stacking once the flag space exceeds a handful of bits. We defend this claim in two steps. First, we formalize automated harness optimization as constrained noisy Bayesian optimization over a mixed-variable, cost-heterogeneous configuration space with cold-start-corrected rewards and a posterior chance-constrained safety check, and give a reference solver, HARBOR (Harness Axis-aligned Regularized Bayesian Optimization Routine), built from a block-additive SAAS surrogate, multi-fidelity cost-aware acquisition, and TuRBO trust regions. Second, we instantiate the problem in a flag-gated harness over a production coding agent and report a controlled four-round manual-tuning case study against a fixed task suite and an end-to-end HARBOR run. The formulation itself is task-class agnostic: the configuration space, reward correction, acquisition, and safety check apply to any agent harness with a bounded flag space and a reproducible task suite.

---


### 14. [LAF-Based Evaluation and UTTL-Based Learning Strategies with MIATTs](https://arxiv.org/abs/2604.20944)

**<font color=#1a73e8>作者：</font>** Yongquan Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many real-world machine learning (ML) applications, the true target cannot be precisely defined due to ambiguity or subjectivity information. To address this challenge, under the assumption that the true target for a given ML task is not assumed to exist objectively in the real world, the EL-MIATTs (Evaluation and Learning with Multiple Inaccurate True Targets) framework has been proposed. Bridging theory and practice in implementing EL-MIATTs, in this paper, we develop two complementary mechanisms: LAF (Logical Assessment Formula)-based evaluation algorithms and UTTL (Undefinable True Target Learning)-based learning strategies with MIATTs, which together enable logically coherent and practically feasible modeling under uncertain supervision. We first analyze task-specific MIATTs, examining how their coverage and diversity determine their structural property and influence downstream evaluation and learning. Based on this understanding, we formulate LAF-grounded evaluation algorithms that operate either on original MIATTs or on ternary targets synthesized from them, balancing interpretability, soundness, and completeness. For model training, we introduce UTTL-grounded learning strategies using Dice and cross-entropy loss functions, comparing per-target and aggregated optimization schemes. We also discuss how the integration of LAF and UTTL bridges the gap between logical semantics and statistical optimization. Together, these components provide a coherent pathway for implementing EL-MIATTs, offering a principled foundation for developing ML systems in scenarios where the notion of "ground truth" is inherently uncertain. An application of this work's results is presented as part of the study available at this https URL.

---


### 15. [Early Detection of Latent Microstructure Regimes in Limit Order Books](https://arxiv.org/abs/2604.20949)

**<font color=#1a73e8>作者：</font>** Prakul Sunil Hiremath, Vruksha Arun Hiremath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Limit order books can transition rapidly from stable to stressed conditions, yet standard early-warning signals such as order flow imbalance and short-term volatility are inherently reactive. We formalise this limitation via a three-regime causal data-generating process (stable $\to$ latent build-up $\to$ stress) in which a latent deterioration phase creates a prediction window prior to observable stress. Under mild assumptions on temporal drift and regime persistence, we establish identifiability of the latent build-up regime and derive guarantees for strictly positive expected lead-time and non-trivial probability of early detection. We propose a trigger-based detector combining MAX aggregation of complementary signal channels, a rising-edge condition, and adaptive thresholding. Across 200 simulations, the method achieves mean lead-time $+18.6 \pm 3.2$ timesteps with perfect precision and moderate coverage, outperforming classical change-point and microstructure baselines. A preliminary application to one week of BTC/USDT order book data shows consistent positive lead-times while baselines remain reactive. Results degrade in low signal-to-noise and short build-up regimes, consistent with theory.

---


### 16. [Escaping the Agreement Trap: Defensibility Signals for Evaluating Rule-Governed AI](https://arxiv.org/abs/2604.20972)

**<font color=#1a73e8>作者：</font>** Michael O'Herlihy, Rosa Català  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Content moderation systems are typically evaluated by measuring agreement with human labels. In rule-governed environments this assumption fails: multiple decisions may be logically consistent with the governing policy, and agreement metrics penalize valid decisions while mischaracterizing ambiguity as error -- a failure mode we term the Agreement Trap. We formalize evaluation as policy-grounded correctness and introduce the Defensibility Index (DI) and Ambiguity Index (AI). To estimate reasoning stability without additional audit passes, we introduce the Probabilistic Defensibility Signal (PDS), derived from audit-model token logprobs. We harness LLM reasoning traces as a governance signal rather than a classification output by deploying the audit model not to decide whether content violates policy, but to verify whether a proposed decision is logically derivable from the governing rule hierarchy. We validate the framework on 193,000+ Reddit moderation decisions across multiple communities and evaluation cohorts, finding a 33-46.6 percentage-point gap between agreement-based and policy-grounded metrics, with 79.8-80.6% of the model's false negatives corresponding to policy-grounded decisions rather than true errors. We further show that measured ambiguity is driven by rule specificity: auditing 37,286 identical decisions under three tiers of the same community rules reduces AI by 10.8 pp while DI remains stable. Repeated-sampling analysis attributes PDS variance primarily to governance ambiguity rather than decoding noise. A Governance Gate built on these signals achieves 78.6% automation coverage with 64.9% risk reduction. Together, these results show that evaluation in rule-governed environments should shift from agreement with historical labels to reasoning-grounded validity under explicit rules.

---


### 17. [User-Centered Design of Hyperlocal Communication Platforms: Insights from the Design and Evaluation of KUBO](https://arxiv.org/abs/2604.20973)

**<font color=#1a73e8>作者：</font>** Eljohn Evangelista, Alyssa Cea, Axel Balitaan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Effective hyperlocal communication is critical in the Philippines, where delayed or algorithm-filtered updates can leave residents uninformed about emergency advisories and community events. We conducted a user-centered study consisting of contextual inquiry and semi-structured interviews to identify four key barriers: delayed alerts, algorithm-driven noise, language gaps, and digital divides. Guided by these insights, we designed KUBO (Kumunidad at Balitang Opisyal), a prototype that integrates a home module for verified local government unit advisories and curated headlines, and a community module for resident-powered neighborhood reports and discussions. Using a within-subjects evaluation design, KUBO significantly reduced task completion times (p-value < 0.001), improved information recall on post-task quizzes (p-value = 0.010), and yielded higher user satisfaction ratings for ease of use, overall satisfaction, and perceived effectiveness compared to Facebook, the commonly used communication platform in the Philippines. These results demonstrate that a dual-channel, inclusive platform can substantially enhance real-time information access, comprehension, and civic engagement in hyperlocal settings.

---


### 18. [Differentially Private Model Merging](https://arxiv.org/abs/2604.20985)

**<font color=#1a73e8>作者：</font>** Qichuan Yin, Manzil Zaheer, Tian Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In machine learning applications, privacy requirements during inference or deployment time could change constantly due to varying policies, regulations, or user experience. In this work, we aim to generate a magnitude of models to satisfy any target differential privacy (DP) requirement without additional training steps, given a set of existing models trained on the same dataset with different privacy/utility tradeoffs. We propose two post processing techniques, namely random selection and linear combination, to output a final private model for any target privacy parameter. We provide privacy accounting of these approaches from the lens of R'enyi DP and privacy loss distributions for general problems. In a case study on private mean estimation, we fully characterize the privacy/utility results and theoretically establish the superiority of linear combination over random selection. Empirically, we validate our approach and analyses on several models and both synthetic and real-world datasets.

---


### 19. [Droplet-LNO: Physics-Informed Laplace Neural Operators for Accurate Prediction of Droplet Spreading Dynamics on Complex Surfaces](https://arxiv.org/abs/2604.20993)

**<font color=#1a73e8>作者：</font>** Ganesh Sahadeo Meshram, Partha Pratim Chakrabarti, Suman Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spreading of liquid droplets on solid substrates constitutes a classic multiphysics problem with widespread applications ranging from inkjet printing, spray cooling, to biomedical microfluidic systems. Yet, accurate computational fluid dynamic (CFD) simulations are prohibitively expensive, taking more than 18 to 24 hours for each transient computation. In this paper, Physics-Informed Laplace Operator Neural Network (PI-LNO) is introduced, representing a novel architecture where the Laplace integral transform function serves as a learned physics-informed functional basis. Extensive comparative benchmark studies were performed against five other state-of-the-art approaches: UNet, UNet with attention modules (UNet-AM), DeepONet, Physics-Informed UNet (PI-UNet), and Laplace Neural Operator (LNO). Through complex Laplace transforms, PI-LNO natively models the exponential transient dynamics of the spreading process. A TensorFlow-based PI-LNO is trained on multi-surface CFD data spanning contact angles $\theta_s \epsilon [20,160]$, employing a physics-regularized composite loss combining data fidelity (MSE, MAE, RMSE) with Navier-Stokes, Cahn-Hilliard, and causality constraints.

---


### 20. [VRSafe: A Secure Virtual Keyboard to Mitigate Keystroke Inference in Virtual Reality](https://arxiv.org/abs/2604.21001)

**<font color=#1a73e8>作者：</font>** Yijun Yuan, Na Du, Adam J. Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Password-based authentication is one of the most commonly used methods for verifying user identities, and its widespread usage continues in virtual reality (VR) applications. As a result, various forms of attacks on password-based authentication in traditional environments such as keystroke inference and shoulder surfing, are still effective in VR applications. While keystroke inference attacks on virtual keyboards have been studied extensively, few efforts have developed an effective and cost-efficient defense strategy to mitigate keystroke inferences in VR. To address this gap, this paper presents a novel QWERTY keyboard called \textit{VRSafe} that is resilient to keystroke inference attacks. The proposed keyboard carefully introduces false positive keystrokes into the information collected by attackers during the typing process, making the inference of the original password difficult. \textit{VRSafe} also incorporates a novel malicious login detector that can effectively identify unauthorized login attempts using credentials inferred from keystroke inference attacks with high detection rate and minimal time and memory cost. The proposed design is evaluated through both simulation experiments and a real-world user study, and the results show that \textit{VRSafe} can significantly reduce the accuracy of keystroke inference attacks while incurring a modest overhead from a usability standpoint.

---


### 21. [The Last Harness You'll Ever Build](https://arxiv.org/abs/2604.21003)

**<font color=#1a73e8>作者：</font>** Haebin Seong, Li Yin, Haoran Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly deployed on complex, domain-specific workflows -- navigating enterprise web applications that require dozens of clicks and form fills, orchestrating multi-step research pipelines that span search, extraction, and synthesis, automating code review across unfamiliar repositories, and handling customer escalations that demand nuanced domain knowledge. \textbf{Each new task domain requires painstaking, expert-driven harness engineering}: designing the prompts, tools, orchestration logic, and evaluation criteria that make a foundation model effective. We present a two-level framework that automates this process. At the first level, the \textbf{Harness Evolution Loop} optimizes a worker agent's harness $\mathcal{H}$ for a single task: a Worker Agent $W_{\mathcal{H}}$ executes the task, an Evaluator Agent $V$ adversarially diagnoses failures and scores performance, and an Evolution Agent $E$ modifies the harness based on the full history of prior attempts. At the second level, the \textbf{Meta-Evolution Loop} optimizes the evolution protocol $\Lambda = (W_{\mathcal{H}}, \mathcal{H}^{(0)}, V, E)$ itself across diverse tasks, \textbf{learning a protocol $\Lambda^{(\text{best})}$ that enables rapid harness convergence on any new task -- so that adapting an agent to a novel domain requires no human harness engineering at all.} We formalize the correspondence to meta-learning and present both algorithms. The framework \textbf{shifts manual harness engineering into automated harness engineering}, and takes one step further -- \textbf{automating the design of the automation itself}.

---


### 22. [Deep FinResearch Bench: Evaluating AI's Ability to Conduct Professional Financial Investment Research](https://arxiv.org/abs/2604.21006)

**<font color=#1a73e8>作者：</font>** Mirazul Haque, Antony Papadimitriou, Samuel Mensah 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Deep FinResearch Bench, a practical and comprehensive evaluation framework for deep research (DR) agents in financial investment research. The benchmark assesses three dimensions of report quality: qualitative rigor, quantitative forecasting and valuation accuracy, and claim credibility and verifiability. Particularly, we define corresponding qualitative and quantitative evaluation metrics and implement an automated scoring procedure to enable scalable assessment. Applying the benchmark to financial reports from frontier DR agents and comparing them with reports authored by financial professionals, we find that AI-generated reports still fall short across these dimensions. These findings underscore the need for domain-specialized DR agents tailored to finance, and we hope the work establishes a foundation for standardized benchmarking of DR agents in financial research.

---


### 23. [Linear Image Generation by Synthesizing Exposure Brackets](https://arxiv.org/abs/2604.21008)

**<font color=#1a73e8>作者：</font>** Yuekun Dai, Zhoutong Zhang, Shangchen Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The life of a photo begins with photons striking the sensor, whose signals are passed through a sophisticated image signal processing (ISP) pipeline to produce a display-referred image. However, such images are no longer faithful to the incident light, being compressed in dynamic range and stylized by subjective preferences. In contrast, RAW images record direct sensor signals before non-linear tone mapping. After camera response curve correction and demosaicing, they can be converted into linear images, which are scene-referred representations that directly reflect true irradiance and are invariant to sensor-specific factors. Since image sensors have better dynamic range and bit depth, linear images contain richer information than display-referred ones, leaving users more room for editing during post-processing. Despite this advantage, current generative models mainly synthesize display-referred images, which inherently limits downstream editing. In this paper, we address the task of text-to-linear-image generation: synthesizing a high-quality, scene-referred linear image that preserves full dynamic range, conditioned on a text prompt, for professional post-processing. Generating linear images is challenging, as pre-trained VAEs in latent diffusion models struggle to simultaneously preserve extreme highlights and shadows due to the higher dynamic range and bit depth. To this end, we represent a linear image as a sequence of exposure brackets, each capturing a specific portion of the dynamic range, and propose a DiT-based flow-matching architecture for text-conditioned exposure bracket generation. We further demonstrate downstream applications including text-guided linear image editing and structure-conditioned generation via ControlNet.

---


### 24. [Micro-DualNet: Dual-Path Spatio-Temporal Network for Micro-Action Recognition](https://arxiv.org/abs/2604.21011)

**<font color=#1a73e8>作者：</font>** Naga VS Raviteja Chappa, Evangelos Sariyanidi, Lisa Yankowitz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-actions are subtle, localized movements lasting 1-3 seconds such as scratching one's head or tapping fingers. Such subtle actions are essential for social communication, ubiquitously used in natural interactions, and thus critical for fine-grained video understanding, yet remain poorly understood by current computer vision systems. We identify a fundamental challenge: micro-actions exhibit diverse spatio-temporal characteristics where some are defined by spatial configurations while others manifest through temporal dynamics. Existing methods that commit to a single spatio-temporal decomposition cannot accommodate this diversity. We propose a dual-path network that processes anatomically-grounded spatial entities through parallel Spatial-Temporal (ST) and Temporal-Spatial (TS) pathways. The ST path captures spatial configurations before modeling temporal dynamics, while the TS path inverts this order to prioritize temporal dynamics. Rather than fixed fusion, we introduce entity-level adaptive routing where each body part learns its optimal processing preference, complemented by Mutual Action Consistency (MAC) loss that enforces cross-path coherence. Extensive experiments demonstrate competitive performance on MA-52 dataset and state-of-the-art results on iMiGUE dataset. Our work reveals that architectural adaptation to the inherent complexity of micro-actions is essential for advancing fine-grained video understanding.

---


### 25. [SGD at the Edge of Stability: The Stochastic Sharpness Gap](https://arxiv.org/abs/2604.21016)

**<font color=#1a73e8>作者：</font>** Fangshuo Liao, Afroditi Kolomvaki, Anastasios Kyrillidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When training neural networks with full-batch gradient descent (GD) and step size $\eta$, the largest eigenvalue of the Hessian -- the sharpness $S(\boldsymbol{\theta})$ -- rises to $2/\eta$ and hovers there, a phenomenon termed the Edge of Stability (EoS). \citet{damian2023selfstab} showed that this behavior is explained by a self-stabilization mechanism driven by third-order structure of the loss, and that GD implicitly follows projected gradient descent (PGD) on the constraint $ S(\boldsymbol{\theta})\leq 2/\eta$. For mini-batch stochastic gradient descent (SGD), the sharpness stabilizes below $2/\eta$, with the gap widening as the batch size decreases; yet no theoretical explanation exists for this suppression.
We introduce stochastic self-stabilization, extending the self-stabilization framework to SGD. Our key insight is that gradient noise injects variance into the oscillatory dynamics along the top Hessian eigenvector, strengthening the cubic sharpness-reducing force and shifting the equilibrium below $2/\eta$. Following the approach of \citet{damian2023selfstab}, we define stochastic predicted dynamics relative to a moving projected gradient descent trajectory and prove a stochastic coupling theorem that bounds the deviation of SGD from these predictions. We derive a closed-form equilibrium sharpness gap: $\Delta S = \eta \beta \sigma_{\boldsymbol{u}}^{2}/(4\alpha)$, where $\alpha$ is the progressive sharpening rate, $\beta$ is the self-stabilization strength, and $\sigma_{ \boldsymbol{u}}^{2}$ is the gradient noise variance projected onto the top eigenvector. This formula predicts that smaller batch sizes yield flatter solutions and recovers GD when the batch equals the full dataset.

---


### 26. [Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations](https://arxiv.org/abs/2604.21018)

**<font color=#1a73e8>作者：</font>** Bowen Zuo, Dongruo Zhou, Yinglun Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While scaling test-time compute can substantially improve model performance, existing approaches either rely on static compute allocation or sample from fixed generation distributions. In this work, we introduce a test-time compute allocation framework that jointly adapts where computation is spent and how generation is performed. Our method begins with a warm-up phase that identifies easy queries and assembles an initial pool of question-response pairs from the test set itself. An adaptive phase then concentrates further computation on unresolved queries while reshaping their generation distributions through evolving in-context demonstrations -- conditioning each generation on successful responses from semantically related queries rather than resampling from a fixed distribution. Experiments across math, coding, and reasoning benchmarks demonstrate that our approach consistently outperforms existing baselines while consuming substantially less inference-time compute.

---


### 27. [HypEHR: Hyperbolic Modeling of Electronic Health Records for Efficient Question Answering](https://arxiv.org/abs/2604.21027)

**<font color=#1a73e8>作者：</font>** Yuyu Liu, Sarang Rajendra Patil, Mengjia Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electronic health record (EHR) question answering is often handled by LLM-based pipelines that are costly to deploy and do not explicitly leverage the hierarchical structure of clinical data. Motivated by evidence that medical ontologies and patient trajectories exhibit hyperbolic geometry, we propose HypEHR, a compact Lorentzian model that embeds codes, visits, and questions in hyperbolic space and answers queries via geometry-consistent cross-attention with type-specific pointer heads. HypEHR is pretrained with next-visit diagnosis prediction and hierarchy-aware regularization to align representations with the ICD ontology. On two MIMIC-IV-based EHR-QA benchmarks, HypEHR approaches LLM-based methods while using far fewer parameters. Our code is publicly available at this https URL.

---


### 28. [A Deep U-Net Framework for Flood Hazard Mapping Using Hydraulic Simulations of the Wupper Catchment](https://arxiv.org/abs/2604.21028)

**<font color=#1a73e8>作者：</font>** Christian Lammers, Fernando Arévalo, Leonie Märker-Neuhaus 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increasing frequency and severity of global flood events highlights the need for the development of rapid and reliable flood prediction tools. This process traditionally relies on computationally expensive hydraulic simulations. This research presents a prediction tool by developing a deep-learning based surrogate model to accurately and efficiently predict the maximum water level across a grid. This was achieved by conducting a series of experiments to optimize a U-Net architecture, patch generation, and data handling for approximating a hydraulic model. This research demonstrates that a deep learning surrogate model can serve as a computationally efficient alternative to traditional hydraulic simulations. The framework was tested using hydraulic simulations of the Wupper catchment in the North-Rhein Westphalia region (Germany), obtaining comparable results.

---


### 29. [Synthetic Data in Education: Empirical Insights from Traditional Resampling and Deep Generative Models](https://arxiv.org/abs/2604.21031)

**<font color=#1a73e8>作者：</font>** Tapiwa Amion Chinodakufa, Ashfaq Ali Shafin, Khandaker Mamun Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic data generation offers promise for addressing data scarcity and privacy concerns in educational technology, yet practitioners lack empirical guidance for selecting between traditional resampling techniques and modern deep learning approaches. This study presents the first systematic benchmark comparing these paradigms using a 10,000-record student performance dataset. We evaluate three resampling methods (SMOTE, Bootstrap, Random Oversampling) against three deep learning models (Autoencoder, Variational Autoencoder, Copula-GAN) across multiple dimensions: distributional fidelity (Kolmogorov-Smirnov distance, Jensen-Shannon divergence), machine learning utility such as Train-on-Synthetic-Test-on-Real scores (TSTR), and privacy preservation (Distance to Closest Record). Our findings reveal a fundamental trade-off: resampling methods achieve near-perfect utility (TSTR: 0.997) but completely fail privacy protection (DCR ~ 0.00), while deep learning models provide strong privacy guarantees (DCR ~ 1.00) at significant utility cost. Variational Autoencoders emerge as the optimal compromise, maintaining 83.3% predictive performance while ensuring complete privacy protection. We also provide actionable recommendations: use traditional resampling for internal development where privacy is controlled, and VAEs for external data sharing where privacy is paramount. This work establishes a foundational benchmark and practical decision framework for synthetic data generation in learning analytics.

---


### 30. [Unlocking Multi-Spectral Data for Multi-Modal Models with Guided Inputs and Chain-of-Thought Reasoning](https://arxiv.org/abs/2604.21032)

**<font color=#1a73e8>作者：</font>** Dahun Kim, Ganesh Satish Mallya, Anelia Angelova  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-spectral imagery is a valuable input signal for Remote Sensing applications, such as land-use and land-cover classification and environmental monitoring. However, generalist Large Multi-modal Models (LMMs) are typically trained on RGB images, limiting their applicability to the RGB domain. At the same time, training multi-spectral multi-modal models is expensive and produces uniquely specialized models. To address this, we propose a novel training-free approach that introduces multi-spectral data within the inference pipeline of standard RGB-only LMMs, allowing large gains in performance. Our approach leverages the LMMs' understanding of the visual space by adapting non-RGB inputs to that space and injecting domain-specific information and Chain-of-Thought reasoning as instructions. We demonstrate this with the Gemini 2.5 model and observe strong Zero-Shot performance gains on popular Remote Sensing benchmarks. These results highlight the potential for geospatial professionals to leverage powerful generalist models for specialized sensor inputs, benefiting from rich reasoning capabilities grounded in specialized data.

---


### 31. [White Paper: Human-AI Collaboration in Conflict Analysis: Text Classifier Development with Peacebuilders](https://arxiv.org/abs/2604.21034)

**<font color=#1a73e8>作者：</font>** Allan Kipyator Kipkemboi Cheboi, Julie Hawke, Hussam Abualfatah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper documents a collaborative research process involving peacebuilders and data scientists in Kenya and Sudan to develop AI-based text classifiers for monitoring online polarization and hatespeech. The method describes a participatory annotation process in which practitioners and domain experts contributed to problem definition, annotation design, iterative validation, and model evaluation. Fine-tuned BERT-based classifiers were trained on collaboratively annotated datasets and evaluated against held-out test sets. In each case, the models produced enhanced contextual alignment, reduced misclassification driven by cultural nuance, and increased practitioner ownership of AI tools. The resulting models (Kenya-polarization and Sudan-hate speech) are open-source and accessible via HuggingFace. The study contributes empirical evidence that participatory AI development can simultaneously improve technical robustness, contextual validity, and normative alignment in sensitive humanitarian domains.

---


### 32. [Projected Gradient Unlearning for Text-to-Image Diffusion Models: Defending Against Concept Revival Attacks](https://arxiv.org/abs/2604.21041)

**<font color=#1a73e8>作者：</font>** Aljalila Aladawi, Mohammed Talha Alam, Fakhri Karray  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning for text-to-image diffusion models aims to selectively remove undesirable concepts from pre-trained models without costly retraining. Current unlearning methods share a common weakness: erased concepts return when the model is fine-tuned on downstream data, even when that data is entirely unrelated. We adapt Projected Gradient Unlearning (PGU) from classification to the diffusion domain as a post-hoc hardening step. By constructing a Core Gradient Space (CGS) from the retain concept activations and projecting gradient updates into its orthogonal complement, PGU ensures that subsequent fine-tuning cannot undo the achieved erasure. Applied on top of existing methods (ESD, UCE, Receler), the approach eliminates revival for style concepts and substantially delays it for object concepts, running in roughly 6 minutes versus the ~2 hours required by Meta-Unlearning. PGU and Meta-Unlearning turn out to be complementary: which performs better depends on how the concept is encoded, and retain concept selection should follow visual feature similarity rather than semantic grouping.

---


### 33. [Interpretable Quantile Regression by Optimal Decision Trees](https://arxiv.org/abs/2604.21042)

**<font color=#1a73e8>作者：</font>** Valentin Lemaire, Gaël Aglin, Siegfried Nijssen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The field of machine learning is subject to an increasing interest in models that are not only accurate but also interpretable and robust, thus allowing their end users to understand and trust AI systems. This paper presents a novel method for learning a set of optimal quantile regression trees. The advantages of this method are that (1) it provides predictions about the complete conditional distribution of a target variable without prior assumptions on this distribution; (2) it provides predictions that are interpretable; (3) it learns a set of optimal quantile regression trees without compromising algorithmic efficiency compared to learning a single tree.

---


### 34. [Active Data](https://arxiv.org/abs/2604.21044)

**<font color=#1a73e8>作者：</font>** Richard Arthur, Virginia DiDomizio, Louis Hoebel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In some complex domains, certain problem-specific decompositions can provide advantages over monolithic designs by enabling comprehension and specification of the design. In this paper we present an intuitive and tractable approach to reasoning over large and complex data sets. Our approach is based on Active Data, i.e., data as atomic objects that actively interact with environments. We describe our intuition about how this bottom-up approach improves designs confronting computational and conceptual complexity. We describe an implementation of the base Active Data concepts within the air traffic flow management domain and discuss performance for this implementation.

---


### 35. [JEPAMatch: Geometric Representation Shaping for Semi-Supervised Learning](https://arxiv.org/abs/2604.21046)

**<font color=#1a73e8>作者：</font>** Ali Aghababaei-Harandi, Aude Sportisse, Massih-Reza Amini  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-supervised learning has emerged as a powerful paradigm for leveraging large amounts of unlabeled data to improve the performance of machine learning models when labeled data are scarce. Among existing approaches, methods derived from FixMatch have achieved state-of-the-art results in image classification by combining weak and strong data augmentations with confidence-based pseudo-labeling. Despite their strong empirical performance, these methods typically struggle with two critical bottlenecks: majority classes tend to dominate the learning process, which is amplified by incorrect pseudo-labels, leading to biased models. Furthermore, noisy early pseudo-labels prevent the model from forming clear decision boundaries, requiring prolonged training to learn informative representation. In this paper, we introduce a paradigm shift from conventional logical output threshold base, toward an explicit shaping of geometric representations. Our approach is inspired by the recently proposed Latent-Euclidean Joint-Embedding Predictive Architectures (LeJEPA), a theoretically grounded framework asserting that meaningful representations should exhibit an isotropic Gaussian structure in latent space. Building on this principle, we propose a new training objective that combines the classical semi-supervised loss used in FlexMatch, an adaptive extension of FixMatch, with a latent-space regularization term derived from LeJEPA.
Our proposed approach, encourages well-structured representations while preserving the advantages of pseudo-labeling strategies. Through extensive experiments on CIFAR-100, STL-10 and Tiny-ImageNet, we demonstrate that the proposed method consistently outperforms existing baselines. In addition, our method significantly accelerates the convergence, drastically reducing the overall computational cost compared to standard FixMatch-based pipelines.

---


### 36. [StyleVAR: Controllable Image Style Transfer via Visual Autoregressive Modeling](https://arxiv.org/abs/2604.21052)

**<font color=#1a73e8>作者：</font>** Liqi Jing, Dingming Zhang, Peinian Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We build on the Visual Autoregressive Modeling (VAR) framework and formulate style transfer as conditional discrete sequence modeling in a learned latent space. Images are decomposed into multi-scale representations and tokenized into discrete codes by a VQ-VAE; a transformer then autoregressively models the distribution of target tokens conditioned on style and content tokens. To inject style and content information, we introduce a blended cross-attention mechanism in which the evolving target representation attends to its own history, while style and content features act as queries that decide which aspects of this history to emphasize. A scale-dependent blending coefficient controls the relative influence of style and content at each stage, encouraging the synthesized representation to align with both the content structure and the style texture without breaking the autoregressive continuity of VAR. We train StyleVAR in two stages from a pretrained VAR checkpoint: supervised fine-tuning on a large triplet dataset of content--style--target images, followed by reinforcement fine-tuning with Group Relative Policy Optimization (GRPO) against a DreamSim-based perceptual reward, with per-action normalization weighting to rebalance credit across VAR's multi-scale hierarchy. Across three benchmarks spanning in-, near-, and out-of-distribution regimes, StyleVAR consistently outperforms an AdaIN baseline on Style Loss, Content Loss, LPIPS, SSIM, DreamSim, and CLIP similarity, and the GRPO stage yields further gains over the SFT checkpoint, most notably on the reward-aligned perceptual metrics. Qualitatively, the method transfers texture while maintaining semantic structure, especially for landscapes and architectural scenes, while a generalization gap on internet images and difficulty with human faces highlight the need for better content diversity and stronger structural priors.

---


### 37. [Layer 2 Blockchains Simplified: A Survey of Vector Commitment Schemes, ZKP Frameworks, Layer-2 Data Structures and Verkle Trees](https://arxiv.org/abs/2604.21055)

**<font color=#1a73e8>作者：</font>** Ekleen Kaur, Marko Suvajdzic  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Layer-2 (L2) protocols address the fundamental limitations of Layer-1 (L1) blockchains by offloading computation while anchoring trust to the parent chain. This architectural shift, while boosting throughput, introduces a new, complex security surface defined by off-chain components like sequencers, bridges, and data availability mechanisms. Prior literature[31][33] offers fragmented views of this risk. This paper presents the first unified, security-focused survey that rigorously maps L2 architecture to its underlying cryptographic security. We dissect the technical progression from L1 primitives to the core of modern L2s, analyzing the security assumptions(Discrete Logarithm, Computational Diffie-Hellman, Bilinear Diffie-Hellman) of ZK frameworks (Groth16, Plonk) and their corresponding commitment schemes (KZG, IPA). We formalize a comprehensive L2 threat model encompassing sequencer liveness, bridge exploits, and data-availability failures. This work serves as an accessible yet rigorous reference for researchers and developers to reason about L2 security from a deep crypto-mathematical perspective.

---


### 38. [TRACES: Tagging Reasoning Steps for Adaptive Cost-Efficient Early-Stopping](https://arxiv.org/abs/2604.21057)

**<font color=#1a73e8>作者：</font>** Yannis Belkhiter, Seshu Tirupathi, Giulio Zizzo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The field of Language Reasoning Models (LRMs) has been very active over the past few years with advances in training and inference techniques enabling LRMs to reason longer, and more accurately. However, a growing body of studies show that LRMs are still inefficient, over-generating verification and reflection steps. Additionally, the high-level role of each reasoning step and how different step types contribute to the generation of correct answers, is largely underexplored. To address this challenge, we introduce TRACES (Tagging of the Reasoning steps enabling Adaptive Cost-Efficient early-Stopping), a lightweight framework that tags reasoning steps in real-time, and enable adaptive, cost-efficient early stopping of large-language-model inferences. Building on this framework we monitor reasoning behaviors during inferences, and we find that LRMs tend to shift their reasoning behavior after reaching a correct answer. We demonstrate that the monitoring of the specific type of steps can produce effective interpretable early stopping criteria. We evaluate the TRACES framework on three mathematical reasoning benchmarks, namely, MATH500, GSM8K, AIME and two knowledge and reasoning benchmarks, MMLU and GPQA respectively. We achieve 20 to 50% token reduction while maintaining comparable accuracy to standard generation.

---


### 39. [Clinically-Informed Modeling for Pediatric Brain Tumor Classification from Whole-Slide Histopathology Images](https://arxiv.org/abs/2604.21060)

**<font color=#1a73e8>作者：</font>** Joakim Nguyen, Jian Yu, Jinrui Fang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate diagnosis of pediatric brain tumors, starting with histopathology, presents unique challenges for deep learning, including severe data scarcity, class imbalance, and fine-grained morphologic overlap across diagnostically distinct subtypes. While pathology foundation models have advanced patch-level representation learning, their effective adaptation to weakly supervised pediatric brain tumor classification under limited data remains underexplored. In this work, we introduce an expert-guided contrastive fine-tuning framework for pediatric brain tumor diagnosis from whole-slide images (WSI). Our approach integrates contrastive learning into slide-level multiple instance learning (MIL) to explicitly regularize the geometry of slide-level representations during downstream fine-tuning. We propose both a general supervised contrastive setting and an expert-guided variant that incorporates clinically informed hard negatives targeting diagnostically confusable subtypes. Through comprehensive experiments on pediatric brain tumor WSI classification under realistic low-sample and class-imbalanced conditions, we demonstrate that contrastive fine-tuning yields measurable improvements in fine-grained diagnostic distinctions. Our experimental analyses reveal complementary strengths across different contrastive strategies, with expert-guided hard negatives promoting more compact intra-class representations and improved inter-class separation. This work highlights the importance of explicitly shaping slide-level representations for robust fine-grained classification in data-scarce pediatric pathology settings.

---


### 40. [Optimizing Diffusion Priors with a Single Observation](https://arxiv.org/abs/2604.21066)

**<font color=#1a73e8>作者：</font>** Frederic Wang, Katherine L. Bouman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While diffusion priors generate high-quality posterior samples across many inverse problems, they are often trained on limited training sets or purely simulated data, thus inheriting the errors and biases of these underlying sources. Current approaches to finetuning diffusion models rely on a large number of observations with varying forward operators, which can be difficult to collect for many applications, and thus lead to overfitting when the measurement set is small. We propose a method for tuning a prior from only a single observation by combining existing diffusion priors into a single product-of-experts prior and identifying the exponents that maximize the Bayesian evidence. We validate our method on real-world inverse problems, including black hole imaging, where the true prior is unknown a priori, and image deblurring with text-conditioned priors. We find that the evidence is often maximized by priors that extend beyond those trained on a single dataset. By generalizing the prior through exponent weighting, our approach enables posterior sampling from both tempered and combined diffusion models, yielding more flexible priors that improve the trustworthiness of the resulting posterior image distribution.

---


### 41. [Weighting What Matters: Boosting Sample Efficiency in Medical Report Generation via Token Reweighting](https://arxiv.org/abs/2604.21082)

**<font color=#1a73e8>作者：</font>** Alexander Weers, Daniel Rueckert, Martin J. Menten  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training vision-language models (VLMs) for medical report generation is often hindered by the scarcity of high-quality annotated data. This work evaluates the use of a weighted loss function to improve data efficiency. Compared to standard cross-entropy loss, which treats all token prediction errors equally, the reweighted loss shifts the focus to semantically salient tokens with outsized clinical importance. In experiments on ophthalmological report generation, we show that this simple method improves efficiency across multiple data scales, achieving similar report quality with up to ten times less training data.

---


### 42. [TRAVELFRAUDBENCH: A Configurable Evaluation Framework for GNN Fraud Ring Detection in Travel Networks](https://arxiv.org/abs/2604.21093)

**<font color=#1a73e8>作者：</font>** Bhavana Sajja  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce TravelFraudBench (TFG), a configurable benchmark for evaluating graph neural networks (GNNs) on fraud ring detection in travel platform graphs. Existing benchmarks--YelpChi, Amazon-Fraud, Elliptic, PaySim--cover single node types or domain-generic patterns with no mechanism to evaluate across structurally distinct fraud ring topologies. TFG simulates three travel-specific ring types--ticketing fraud (star topology with shared device/IP clusters), ghost hotel schemes (reviewer x hotel bipartite cliques), and account takeover rings (loyalty transfer chains)--in a heterogeneous graph with 9 node types and 12 edge types. Ring size, count, fraud rate, scale (500 to 200,000 nodes), and composition are fully configurable. We evaluate six methods--MLP, GraphSAGE, RGCN-proj, HAN, RGCN, and PC-GNN--under a ring-based split where each ring appears entirely in one partition, eliminating transductive label leakage. GraphSAGE achieves AUC=0.992 and RGCN-proj AUC=0.987, outperforming the MLP baseline (AUC=0.938) by 5.5 and 5.0 pp, confirming graph structure adds substantial discriminative power. HAN (AUC=0.935) is a negative result, matching the MLP baseline. On the ring recovery task (>=80% of ring members flagged simultaneously), GraphSAGE achieves 100% recovery across all ring types; MLP recovers only 17-88%. The edge-type ablation shows device and IP co-occurrence are the primary signals: removing uses_device drops AUC by 5.2 pp. TFG is released as an open-source Python package (MIT license) with PyG, DGL, and NetworkX exporters and pre-generated datasets at this https URL, with Croissant metadata including Responsible AI fields.

---


### 43. [Spectral Embeddings Leak Graph Topology: Theory, Benchmark, and Adaptive Reconstruction](https://arxiv.org/abs/2604.21094)

**<font color=#1a73e8>作者：</font>** Thinh Nguyen-Cong, Truong-Son Hy, Thang N. Dinh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) excel on relational data, but standard benchmarks unrealistically assume the graph is centrally available. In practice, settings such as Federated Graph Learning, distributed systems, and privacy-sensitive applications involve graph data that are localized, fragmented, noisy, and privacy-leaking. We present a unified framework for this setting. We introduce LoGraB (Local Graph Benchmark), which decomposes standard datasets into fragmented benchmarks using three strategies and four controls: neighborhood radius $d$, spectral quality $k$, noise level $\sigma$, and coverage ratio $p$. LoGraB supports graph reconstruction, localized node classification, and inter-fragment link prediction, with Island Cohesion. We propose AFR (Adaptive Fidelity-driven Reconstruction), a method for noisy spectral fragments. AFR scores patch quality via a fidelity measure combining a gap-to-truncation stability ratio and structural entropy, then assembles fragments using RANSAC-Procrustes alignment, adaptive stitching, and Bundle Adjustment. Rather than forcing a single global graph, AFR recovers large faithful islands. We prove heat-kernel edge recovery under a separation condition, Davis--Kahan perturbation stability, and bounded alignment error. We establish a Spectral Leakage Proposition: under a spectral-gap assumption, polynomial-time Bayesian recovery is feasible once enough eigenvectors are shared, complementing AFR's deterministic guarantees. Experiments on nine benchmarks show that LoGraB reveals model strengths and weaknesses under fragmentation, AFR achieves the best F1 on 7/9 datasets, and under per-embedding $(\epsilon,\delta)$-Gaussian differential privacy, AFR retains 75% of its undefended F1 at $\epsilon=2$. Our anonymous code is available at this https URL

---


### 44. [Preconditioned DeltaNet: Curvature-aware Sequence Modeling for Linear Recurrences](https://arxiv.org/abs/2604.21100)

**<font color=#1a73e8>作者：</font>** Neehal Tumma, Noel Loo, Daniela Rus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To address the increasing long-context compute limitations of softmax attention, several subquadratic recurrent operators have been developed. This work includes models such as Mamba-2, DeltaNet, Gated DeltaNet (GDN), and Kimi Delta Attention (KDA). As the space of recurrences grows, a parallel line of work has arisen to taxonomize them. One compelling view is the test-time regression (TTR) framework, which interprets recurrences as performing online least squares updates that learn a linear map from the keys to values. Existing delta-rule recurrences can be seen as first-order approximations to this objective, but notably ignore the curvature of the least-squares loss during optimization. In this work, we address this by introducing preconditioning to these recurrences. Starting from the theory of online least squares, we derive equivalences between linear attention and the delta rule in the exactly preconditioned case. Next, we realize this theory in practice by proposing a diagonal approximation: this enables us to introduce preconditioned variants of DeltaNet, GDN, and KDA alongside efficient chunkwise parallel algorithms for computing them. Empirically, we find that our preconditioned delta-rule recurrences yield consistent performance improvements across synthetic recall benchmarks and language modeling at the 340M and 1B scale.

---


### 45. [A Hybridizable Neural Time Integrator for Stable Autoregressive Forecasting](https://arxiv.org/abs/2604.21101)

**<font color=#1a73e8>作者：</font>** Brooks Kinch, Xiaozhe Hu, Yilong Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For autoregressive modeling of chaotic dynamical systems over long time horizons, the stability of both training and inference is a major challenge in building scientific foundation models. We present a hybrid technique in which an autoregressive transformer is embedded within a novel shooting-based mixed finite element scheme, exposing topological structure that enables provable stability. For forward problems, we prove preservation of discrete energies, while for training we prove uniform bounds on gradients, provably avoiding the exploding gradient problem. Combined with a vision transformer, this yields latent tokens admitting structure-preserving dynamics. We outperform modern foundation models with a $65\times$ reduction in model parameters and long-horizon forecasting of chaotic systems. A "mini-foundation" model of a fusion component shows that 12 simulations suffice to train a real-time surrogate, achieving a $9{,}000\times$ speedup over particle-in-cell simulation.

---


### 46. [AI Governance under Political Turnover: The Alignment Surface of Compliance Design](https://arxiv.org/abs/2604.21103)

**<font color=#1a73e8>作者：</font>** Andrew J. Peterson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Governments are increasingly interested in using AI to make administrative decisions cheaper, more scalable, and more consistent. But for probabilistic AI to be incorporated into public administration it must be embedded in a compliance layer that makes decisions reviewable, repeatable, and legally defensible. That layer can improve oversight by making departures from law easier to detect. But it can also create a stable approval boundary that political successors learn to navigate while preserving the appearance of lawful administration. We develop a formal model in which institutions choose the scale of automation, the degree of codification, and safeguards on iterative use. The model shows when these systems become vulnerable to strategic use from within government, why reforms that initially improve oversight can later increase that vulnerability, and why expansions in AI use may be difficult to unwind. Making AI usable can thus make procedures easier for future governments to learn and exploit.

---


### 47. [Materialistic RIR: Material Conditioned Realistic RIR Generation](https://arxiv.org/abs/2604.21119)

**<font color=#1a73e8>作者：</font>** Mahnoor Fatima Saad, Sagnik Majumder, Kristen Grauman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rings like gold, thuds like wood! The sound we hear in a scene is shaped not only by the spatial layout of the environment but also by the materials of the objects and surfaces within it. For instance, a room with wooden walls will produce a different acoustic experience from a room with the same spatial layout but concrete walls. Accurately modeling these effects is essential for applications such as virtual reality, robotics, architectural design, and audio engineering. Yet, existing methods for acoustic modeling often entangle spatial and material influences in correlated representations, which limits user control and reduces the realism of the generated acoustics. In this work, we present a novel approach for material-controlled Room Impulse Response (RIR) generation that explicitly disentangles the effects of spatial and material cues in a scene. Our approach models the RIR using two modules: a spatial module that captures the influence of the spatial layout of the scene, and a material module that modulates this spatial RIR according to a user-specified material configuration. This explicitly disentangled design allows users to easily modify the material configuration of a scene and observe its impact on acoustics without altering the spatial structure or scene content. Our model provides significant improvements over prior approaches on both acoustic-based metrics (up to +16% on RTE) and material-based metrics (up to +70%). Furthermore, through a human perceptual study, we demonstrate the improved realism and material sensitivity of our model compared to the strongest baselines.

---


### 48. [TabSHAP](https://arxiv.org/abs/2604.21120)

**<font color=#1a73e8>作者：</font>** Aryan Chaudhary, Prateek Agarwal, Tejasvi Alladi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) fine-tuned on serialized tabular data are emerging as powerful alternatives to traditional tree-based models, particularly for heterogeneous or context-rich datasets. However, their deployment in high-stakes domains is hindered by a lack of faithful interpretability; existing methods often rely on global linear proxies or scalar probability shifts that fail to capture the model's full probabilistic uncertainty. In this work, we introduce TabSHAP, a model-agnostic interpretability framework designed to directly attribute local query decision logic in LLM-based tabular classifiers. By adapting a Shapley-style sampled-coalition estimator with Jensen-Shannon divergence between full-input and masked-input class distributions, TabSHAP quantifies the distributional impact of each feature rather than simple prediction flips. To align with tabular semantics, we mask at the level of serialized key:value fields (atomic in the prompt string), not individual subword tokens. Experimental validation on the Adult Income and Heart Disease benchmarks demonstrates that TabSHAP isolates critical diagnostic features, achieving significantly higher faithfulness than random baselines and XGBoost proxies. We further run a distance-metric ablation on the same test instances and TabSHAP settings: attributions are recomputed with KL or L1 replacing JSD in the similarity step (results cached per metric), and we compare deletion faithfulness across all three.

---


### 49. [AGNT2: Autonomous Agent Economies on Interaction-Optimized Layer 2 Infrastructure](https://arxiv.org/abs/2604.21129)

**<font color=#1a73e8>作者：</font>** Anbang Ruan, Xing Zhang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Current blockchain Layer 2 solutions, including Optimism, Arbitrum, zkSync, and their derivatives, optimize for human-initiated financial transactions. Autonomous AI agents instead generate high-frequency, semantically rich service invocations among mutually untrusting principals. Existing chains treat those interactions as generic calldata, forcing identity, escrow, dependency ordering, and session state to be encoded above the execution layer at the wrong cost point. We present AGNT2, a three-tier stack purpose-built for agent and microservice coordination on-chain. AGNT2 combines: (1) a sidecar deployment pattern that turns any Docker container into an on-chain agent without application-code modification; (2) Layer Top P2P state channels for established bilateral pairs (<100 ms, rough design target 1K-5K TPS per pair, 10M+ aggregate TPS design envelope under endpoint-resource limits), Layer Core as a dependency-aware sequenced rollup for first-contact and multi-party interactions (500 ms-2 s, 300K-500K TPS design target), and Layer Root settlement with computational fraud proofs anchored to any EVM L1; and (3) an agent-native execution environment plus interaction trie that make service invocation, identity, reputation, capabilities, and session context first-class protocol objects. This paper focuses on the execution-layer systems problem: sequencing, state, settlement, and the data-availability (DA) bandwidth gap that bounds all three. Simulation and analytical modeling support the architecture, and prototype measurements validate selected components, but no end-to-end Layer Core implementation exists yet. Practical deployment is currently constrained to roughly 10K-100K TPS by DA throughput, leaving a ~100x gap at the target ceiling. AGNT2 argues that the agent economy requires a dedicated execution layer rather than a general-purpose chain repurposed for agents.

---


### 50. [Cross-Session Threats in AI Agents: Benchmark, Evaluation, and Algorithms](https://arxiv.org/abs/2604.21131)

**<font color=#1a73e8>作者：</font>** Ari Azarafrooz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-agent guardrails are memoryless: each message is judged in isolation, so an adversary who spreads a single attack across dozens of sessions slips past every session-bound detector because only the aggregate carries the payload. We make three contributions to cross-session threat detection.
(1) Dataset. CSTM-Bench is 26 executable attack taxonomies classified by kill-chain stage and cross-session operation (accumulate, compose, launder, inject_on_reader), each bound to one of seven identity anchors that ground-truth "violation" as a policy predicate, plus matched Benign-pristine and Benign-hard confounders. Released on Hugging Face as intrinsec-ai/cstm-bench with two 54-scenario splits: dilution (compositional) and cross_session (12 isolation-invisible scenarios produced by a closed-loop rewriter that softens surface phrasing while preserving cross-session artefacts).
(2) Measurement. Framing cross-session detection as an information bottleneck to a downstream correlator LLM, we find that a session-bound judge and a Full-Log Correlator concatenating every prompt into one long-context call both lose roughly half their attack recall moving from dilution to cross_session, well inside any frontier context window. Scope: 54 scenarios per shard, one correlator family (Anthropic Claude), no prompt optimisation; we release it to motivate larger, multi-provider datasets.
(3) Algorithm and metric. A bounded-memory Coreset Memory Reader retaining highest-signal fragments at $K=50$ is the only reader whose recall survives both shards. Because ranker reshuffles break KV-cache prefix reuse, we promote $\mathrm{CSR\_prefix}$ (ordered prefix stability, LLM-free) to a first-class metric and fuse it with detection into $\mathrm{CSTM} = 0.7 F_1(\mathrm{CSDA@action}, \mathrm{precision}) + 0.3 \mathrm{CSR\_prefix}$, benchmarking rankers on a single Pareto of recall versus serving stability.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-231](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
