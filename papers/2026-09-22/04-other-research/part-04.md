# 📦 其他研究 | 2026年09月22日

> 本类共 **179** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-179**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-179**

---

### 151. [Catena: A Comprehensive Software Suite for Large-Scale Connectomics](https://arxiv.org/abs/2609.21887)

**<font color=#1a73e8>作者：</font>** Samia Mohinta, Pedro Gómez-Gálvez, Shi Yan Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The gold standard datasets for mapping connectomes are electron microscopy volumes of densely labeled neural tissue at nanometer resolution. Yet reconstructing and proofreading neuronal arbors and annotating all synapses requires pipelining multiple software tools that are often fragmented, inconsistently maintained, or proprietary, hindering reproducibility and automation. Here, we introduce Catena, an open-source, comprehensive, developer-centric software suite for connectomics that integrates modules for 3D neuron and organelle segmentation, synapse detection, microtubule tracking, and neurotransmitter inference. Catena organizes its modules in composable, chunk-wise processing pipelines in a completely documented, extensible, and adaptable design. We further reduce compute and ground-truth data requirements with pretrained machine learning models, facilitating fine-tuning. Catena ships fully containerized modules that encapsulate evolving dependencies for consistent execution across workstations and clusters. By consolidating open components, shareable models, and containerized runtimes, Catena delivers a reproducible and scalable approach to mapping cellular connectomes from electron microscopy volumes. Code and documentation: this https URL

---


### 152. [The Role of Radiometric Features in Cross-Site Leaf-Wood Segmentation of LiDAR Point Clouds](https://arxiv.org/abs/2609.21903)

**<font color=#1a73e8>作者：</font>** Roman Kaharlytskyi, Derek T. Robinson, Roberto Guglielmi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Leaf-wood segmentation of individual trees from LiDAR point clouds is essential for quantitative structure models (QSMs) used in non-destructive biomass estimation. Existing segmentation methods typically exclude radiometric features (e.g., intensity, return number) to maximize cross-sensor compatibility. We challenge this design choice by evaluating cross-site and cross-platform generalization: training on the public Heidelberg dataset (terrestrial TLS, 1550nm) and testing on a novel dataset from Ontario, Canada (RPA-LS, 905nm). Results show that geometry-only methods - including state-of-the-art deep learning models trained on high-density LiDAR datasets - fail to generalize to the sparse, top-down geometry of aerial scans, achieving F1 scores <= 0.56. Incorporating radiometric features (intensity, return number, number of returns) improves F1 to 0.61, but more critically, increases wood recall by 119% from 0.16 to 0.35. Furthermore, geometry-only approaches often result in fragmented stem and branch components. We find that leveraging radiometric features preserves greater structural connectivity, resulting in more coherent architectures that are better suited for QSM reconstruction. We demonstrate that while geometric patterns are view-dependent and prone to overfitting scan patterns, radiometric features encode physical material properties that generalize across disparate sensors and environments.

---


### 153. [Intervention Granularity Matters: Coherent Treatment Bundles in Counterfactual Simulation with Clinical World Models](https://arxiv.org/abs/2609.21906)

**<font color=#1a73e8>作者：</font>** Fangzhou Wang, Yixuan Yang, Camilla Balzarotti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual simulation with a clinical world model means fixing a patient's history, changing the treatment, and reading off the predicted response. Doing so requires deciding what counts as one intervention. In clinical settings, interventions are documented as bundles: a co-occurrence audit of 945,707 patient-hours from MIMIC-IV shows groups of components, such as every parameter of a dialysis circuit, that never appear apart, so an edit that changes one component on its own describes an hour that never occurs in the data. We hypothesize that the granularity at which an intervention is edited changes how a world model responds, and test this with Clin-JEPA, a latent world model of patient trajectories conditioned on hourly treatment text. At 1,019 documented onsets of invasive ventilation, we keep the patient's history and other treatments fixed and compare editing one ventilator setting with editing the complete configuration recorded for a real patient with the most similar recent trajectory. The complete bundle moves the predicted next state further than any single setting, consistently across all five settings, and the difference remains after accounting for how much each edit changes the model's input. Intervention granularity therefore materially affects the response of a clinical world model: single-component edits may understate treatment sensitivity, and bundle-aware editing may offer a better-supported basis for counterfactual treatment simulation.

---


### 154. [Beyond Kinematics: Benchmarking Simulation Fidelity for Muscle-Driven Imitation Learning](https://arxiv.org/abs/2609.21909)

**<font color=#1a73e8>作者：</font>** Ayah G. Ahmad, Claire E. Borden, Maegan Tucker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we conduct a systematic comparison of two state-of-the-art motion-imitation reinforcement learning (MIRL) pipelines, one built on SCONE/HyFyDy and one built on MuJoCo/MyoSim. HyFyDy emphasizes physiological realism through detailed musculotendon modeling, while MuJoCo prioritizes computational efficiency and scalable policy learning. While recent work has demonstrated that both pipelines reproduce human kinematics with high fidelity, it remains unclear if they accurately capture the underlying neuromuscular behavior that produced the movement. This limitation is particularly important for robotic assistive-device design and control, where outcome measures such as muscle activation patterns and metabolic cost are often used as optimization targets. To conduct a systematic comparison, our work compares both pipelines using a common set of human motion-capture and electromyography (EMG) measurements. The results find that while both pipelines produce similar kinematics with relative accuracy, the muscle activations from HyFyDy are more aligned with the experimental EMG, as supported by the average pooled (RMSE, r) values for muscle activations from HyFyDy and MuJoCo: (0.164, 0.4) and (0.344, 0.11), respectively. While we conclude that the more advanced physiological realism of HyFyDy currently makes it more suitable for musculoskeletal modeling, both require further development to bring physiological realism to GPU-parallelizable simulation environments and advance robotic assistive device design.

---


### 155. [Depressive symptoms are reflected differently across digital contexts](https://arxiv.org/abs/2609.21919)

**<font color=#1a73e8>作者：</font>** Yajing Wang, Emilia Marchese, Talayeh Aledavood 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As more of everyday life takes place online, digital behavior may provide a potential window into how depressive symptoms are reflected in daily life. Yet digital mental health studies have produced mixed findings. These inconsistencies may partly reflect how digital behavior is measured: self reported use, single device studies, and aggregate screen time can obscure differences across devices, activities, and patterns of engagement. We combined monthly assessments of depressive symptoms with passively recorded mobile and desktop web traces from 1,146 adults in Germany over six months. We examined how general, cognitive-affective, and somatic depressive symptoms are reflected across digital contexts defined by device and activity type. Associations varied markedly across these contexts. On mobile, more severe symptoms were associated with more nighttime activity, greater use of social media, messaging, and entertainment, and fewer but longer sessions. On desktop, associations were fewer and largely involved reduced engagement with news, shopping, and adult content. Mobile associations primarily arose for general and cognitive-affective symptoms, whereas desktop associations were concentrated in somatic symptoms. Our findings suggest that characterizing how depressive symptoms are reflected in digital behavior requires attending to what people do online and where, not only how much screens are used.

---


### 156. [What Should We Ask Next? Retrieval-Aware Question Learning under Partial Evidence](https://arxiv.org/abs/2609.21924)

**<font color=#1a73e8>作者：</font>** Lyucheng Qian, John Yuehan Zhang, Pingyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive retrieval under partial evidence is a sequential information-acquisition problem: an agent must decide which question will create the most useful evidence for the next retrieval update. Existing systems train this decision by imitating an offline ordering of candidate QA pairs, although question value is determined by the response it elicits and its downstream effect on retrieval. We establish that candidate discriminativeness and perceived usefulness provide weak supervision for this objective, then introduce RAVEL, a retrieval-aware online reinforcement learning framework for interactive person re-identification. RAVEL initializes from supervised question generation, observes the current Top-4 candidates directly, and optimizes the question policy with rank feedback from the full question-answer-retrieval loop. Experiments on Interactive-PEDES show that RAVEL delivers progressively stronger retrieval performance across five interaction rounds. Further analysis shows that RAVEL reallocates the questioning budget toward localized open-ended attributes, which provide more useful retrieval evidence and yield the largest gains on initially difficult queries.

---


### 157. [Kinks vs. Smoothness: Identifiability of Real Analytic nICA for Laplace-like Sources](https://arxiv.org/abs/2609.21926)

**<font color=#1a73e8>作者：</font>** Isaac Manring, Kejun Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many machine learning systems try to explain complex data - like images or financial time series - in terms of hidden, independent factors that generated them. Recovering the true underlying factors, rather than some scrambled version of them, is the central challenge of nonlinear Independent Component Analysis (nICA). We prove identifiability (exact recovery) up to trivial ambiguities for real analytic generating functions when source probability density functions have a finite number of discontinuities in the first derivative. The Laplace distribution is the most prominent example satisfying this assumption. Our proof relies on the contrast between kinks in the source distribution and the smoothness of real analytic functions. Real analytic functions comprise a broad class of generating mechanisms, and can be approximated with Normalizing Flows or Variational Autoencoders with standard activation functions (e.g., tanh, softplus, GELU), so our result applies with minimal changes to existing training pipelines. We perform experiments on real and synthetic data with both Normalizing Flows and Variational Auto-Encoders demonstrating their identifiability properties. In experiments on CelebA data we recover several interpretable latent factors controlling unique attributes across the dataset.

---


### 158. [Joint Remaining Useful Life Prediction and Capacity Estimation of Lithium-Ion Batteries Using Partial-Charging Data](https://arxiv.org/abs/2609.21932)

**<font color=#1a73e8>作者：</font>** Khoa Tran, Ho-Si-Hung Nguyen, Phone Wai Yan Moe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint remaining useful life (RUL) prediction and capacity estimation require representations of both gradual degradation and recent battery behavior. This paper presents a cross-expert framework using partial-charging measurements without measured historical full-cycle capacity as an input. The RUL Expert encodes nominal 10-min segments from ten cycles sampled within a 30-cycle history using a pretrained gated recurrent unit (GRU) encoder, a two-dimensional convolutional neural network (2D-CNN), and a temporal GRU. The Capacity Expert processes statistical descriptors of nominal 40-min segments from ten consecutive cycles using a 2D-CNN and a Transformer. A feature-wise linear modulation module uses the short-term representation to condition the long-term representation for joint prediction. Training comprises supervised autoencoder pretraining, independent expert pretraining, and fusion training with frozen experts. On two public battery-aging datasets, the reference configuration achieves mean RUL root-mean-square errors of 143.69 and 161.10 cycles and capacity errors of 12.36 and 7.28mAh, respectively. On Dataset I, fusion reduces both mean errors relative to either standalone expert. The results demonstrate a trade-off between RUL and capacity accuracy: the proposed method attains the lowest reported RUL RMSE among the compared methods on both datasets, whereas several baselines yield lower capacity errors.

---


### 159. [Info3R: Information-Adaptive Test-Time Training for 3D Reconstruction](https://arxiv.org/abs/2609.21938)

**<font color=#1a73e8>作者：</font>** Sunghyun Baek, Hanna Bae, Minchan Kwon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based models have recently achieved strong performance on 3D reconstruction from images, and recent works extend them to process video streams in an online manner for real-world deployment. However, existing methods overlook two key signals when handling long image streams: the importance of each incoming frame and the information saturation of the model's internal state. In this paper, we propose Info3R, a novel information-adaptive test-time training method for the online 3D reconstruction. We introduce an information-aware state update that modulates the state update strength based on the redundancy and informativeness of each incoming frame. To restore the state's plasticity -- its capacity to incorporate new observations -- we propose a dynamic state reset, triggered by the cumulative magnitude of state updates and the model's prediction confidence and accompanied by an anchor-to-world alignment. Our method achieves consistent improvements on camera pose estimation, video depth estimation, and 3D reconstruction, while substantially mitigating the performance degradation in the long sequence evaluation. Notably, on KITTI Odometry, our method achieves on average 1.68x lower ATE than LongStream, demonstrating its robustness on extended outdoor sequences.

---


### 160. [End-to-End Hard-Label Cryptanalytic Model Extraction Using Efficient Sign Recovery](https://arxiv.org/abs/2609.21941)

**<font color=#1a73e8>作者：</font>** Akira Ito, Takayuki Miura, Yosuke Todo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The importance of deep neural networks (DNNs) is widely recognized, and the parameters obtained through training are regarded as valuable assets. Recently, attacks that extract these parameters using only oracle queries to a DNN have been actively studied at IACR conferences. The hard-label setting is the most challenging setting for model extraction, where an adversary can observe only the final output label, such as "dog" or "cat." At Eurocrypt 2025, Carlini et al. proposed polynomial-time hard-label extraction of ReLU-based MLPs. However, one step of this attack process, i.e., sign recovery, requires a large number of queries and substantial computation. Implementing this step in a black-box setting remains difficult. Consequently, a fully black-box end-to-end demonstration on trained deep ReLU MLPs has remained a challenge. In this paper, we propose a new sign-recovery algorithm based on a completely different principle from the existing method. Our method requires no dedicated queries for sign recovery. In our experiments, it achieves higher sign-recovery accuracy than the existing method. Consequently, it enables efficient sign recovery even for trained models. With our sign-recovery algorithm, all steps of hard-label model extraction can be implemented in a black-box setting. By combining these implementations, we demonstrate end-to-end model extraction from models trained on MNIST and Fashion-MNIST, with width 16 and 4 or 6 hidden layers, achieving over 98% label agreement.

---


### 161. [Learning to Move Cities: Deep Meta-Models and Reinforcement Policies for Calibration and Control in Urban Networks](https://arxiv.org/abs/2609.21945)

**<font color=#1a73e8>作者：</font>** Adewumi Augustine Adepitan, Christopher J. Haruna, Oluwasegun Adegoke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban transportation networks present complex optimization challenges spanning calibration of high-fidelity simulators and real-time operational control. This paper presents a shared latent-space framework that connects simulator calibration and reinforcement learning control through a common learned representation of urban traffic dynamics. First, we develop a combinatorial MLP-autoencoder architecture that learns low-dimensional manifolds linking simulator inputs (origin-destination demand, network parameters) to outputs (travel times, congestion patterns), enabling efficient Bayesian optimization for calibration. This approach demonstrates superior sample efficiency compared to traditional dimension reduction methods, achieving better fit to observational data within fixed computational budgets. Second, we implement a deep Q-learning agent with experience replay and target networks to optimize dynamic traffic assignment through scheduling and routing adjustments. In empirical evaluations on benchmark networks, our approach reduces system-wide travel times by up to 51% compared to baseline operations. The learned latent representation is not only used to reduce the dimensionality of Bayesian calibration, but is also incorporated into the reinforcement learning state representation, allowing the control policy to operate on compressed and calibrated traffic dynamics. This shared latent-space formulation provides a unified pathway from simulator calibration to adaptive operational control within intelligent transportation systems. Our results highlight the transformative potential of deep learning methods in urban mobility planning and management, particularly for large-scale networks where traditional optimization approaches face computational bottlenecks.

---


### 162. [RACER: Role-Aligned Competence Estimation for Human-AI Routing](https://arxiv.org/abs/2609.21953)

**<font color=#1a73e8>作者：</font>** Joshua Strong, Emma Sun, Alexander Capstick 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning to defer asks a predictive system when to act autonomously and when to defer to a human expert. Population-adaptive deferral extends this problem to unseen experts using a small context set of expert behavior. Neural context encoders such as L2D-Pop can be query-dependent, but may learn routing shortcuts tied to absolute class coordinates. Identity-Free Deferral (IFD) removes such shortcuts through role-indexed classwise competence profiles, but its estimates are constant within each class and cannot capture instance-level expert specialization. We propose RACER---Role-Aligned Competence Estimation for Routing---a role-relative framework for estimating an unseen expert's competence from context. RACER estimates the posterior-predictive probability that the expert is correct on a query under each candidate class role, then combines these estimates with the model posterior to obtain the Bayes-relevant expert-correctness probability. Nonparametric and neural kernel-pooling estimators use candidate-role relations, shared aggregation, and symmetric summaries, excluding absolute class-identity channels. We prove coherent class-relabelling invariance, derive a Bayes-aligned deferral surrogate, and give a plug-in regret bound relating routing regret to classifier and competence-estimation error. On controlled synthetic benchmarks, including a PathMNIST histopathology context-scaling study with simulated experts, RACER benefits from additional context under hidden subtype dependence and gives the strongest aggregate performance on a separately sampled unseen-expert split in the CIFAR-100 synthetic experiments. On the radiologist and human--AI chest-radiography benchmarks (VinDr-CXR and CheXpert), the RACER family is competitive or best in budget-swept deferral, with calibration results varying across metrics and datasets.

---


### 163. [Provisional Reachability: Containing Agents by Making Every Crossing Revocable](https://arxiv.org/abs/2609.21957)

**<font color=#1a73e8>作者：</font>** Yoshiaki Takashita  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A companion paper found that what a defender must block over time has units: bits per period [Takashita, 2026a]. This paper sets it. Hold every crossing in escrow for one period, audit each held item independently with probability r, and revoke the window if any audit catches something. An adversary crossing k times, each carrying c bits, expects kc(1-r)^k, maximised at k* = 1/ln(1/(1-r)), a bound of L(r) ~ c/(er) per window. The bound is a supremum over the adversary's choice, so the scheme may be public; simulation matches it to 7.7 standard errors. It is a rate, not a total: escrow alone still lets the secret assemble in every run. But if the secret decays at a fraction mu of held bits per period, holdings converge to g/mu at any horizon, so an L-bit secret is unreachable once mu > g/L -- an error threshold in Eigen's sense, sharp where the closed form puts it (100% of runs assemble at 0.9mu*, 0% at 2mu*, over 20,000 windows). Deception that needs the adversary to reason badly fails: a surface whose names lie left accuracy at 18 of 18, and 100% at three reader strengths. Withholding reference works, and differently: no reader would commit at all. Keying the entry points hides 0.10 bits of what a module does; keying the denotation hides 2.64 of 3.00 at chance accuracy, while 100% of readers still call it ordinary Python. Variance must be removed from the audit rate, where loot is convex in r, and added to the activation budget, where survival is multiplicative: extinction 70% to 100% at a fixed mean. End to end the stack takes the leak from 100,000 to 59 bits, a factor of 1,704, leaving 12% of legitimate work standing; keying the window to the caller restores that to 100% at no cost in leakage, at the price of a bound that is per principal. Of 65 read-only tools, escrow leaves 2,400 bits per call: a factor of 10, not infinity.

---


### 164. [Learning Cardiac Features: ECG Biometrics Across Time and~Exercise](https://arxiv.org/abs/2609.21962)

**<font color=#1a73e8>作者：</font>** Luca Thiebaud, Paul Chauchat, Mustapha Ouladsine 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electrocardiograms (ECGs) carry subject-specific patterns enabling reliable individual discrimination, forming the basis of ECG biometrics. Beyond authentication, this paradigm holds significant potential to secure sensitive cardiac data and to serve as a pretext task in self-supervised learning. Yet, most studies remain confined to singlesession, resting data, leaving robustness to temporal and physiological variations largely untested. We address this gap by evaluating ECG biometrics under realistic conditions involving exercise-induced stress and cross-session variability. A Siamese ResNet with late multi-lead fusion strategy is trained on a large ECG dataset extracted from cardiopulmonary exercise tests and evaluated with a exercise-and time-aware protocol, as well as on public benchmarks. This first extensive assessment of ECG biometrics under combined physiological and temporal variability achieves an intra-session rest-to-peak EER of 1.7% and stateof-the-art 3.9% on the CYBHi dataset. Findings support the presence of an intrinsic cardiac signature resilient to physiological and temporal drift.

---


### 165. [Time series generation with spectrally aligned latent flow matching](https://arxiv.org/abs/2609.21989)

**<font color=#1a73e8>作者：</font>** Camilo Carvajal Reyes, Felipe Tobar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent flow models have proven to be a reliable and cost-effective method for time series generation. However, the latent compression induces unwanted artefacts, such as a spectral mismatch with respect to the underlying dataset, thus hindering their use as training surrogates. In this article, we propose a spectrally-aligned latent-flow time series generator, where the latent space for flow matching is trained to preserve dynamical properties that are relevant for the suitability of synthetic samples. We find that incorporating fine-tuning losses based on canonical signal representations such as the Fourier, wavelet and signature transforms helps overcome these issues. The interpretability of these transformations allows us to ensure that the synthetic signals are aligned with the true ones in terms of relevant features, such as smoothness or targeted spectral content, as opposed to relying on pointwise reconstruction losses only. We compare the proposed aligned models against a base latent-flow model and the state of the art over real-world long-range univariate and multivariate benchmark datasets. Our quantitative results validate the superiority of the proposed method in terms of its performance on metrics reflecting signal realness and computational efficiency, while being aligned to the training set with respect to its local structure.

---


### 166. [Moral Entropy: Auditing Bias and Uncertainty in Moral Judgment](https://arxiv.org/abs/2609.21992)

**<font color=#1a73e8>作者：</font>** Maciej Skorski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most work in computational ethics treats annotator disagreement on moral content as noise to be voted away, collapsed into majority vote or the more permissive any-annotator rule the moment a single annotator flags an item. We argue this uncertainty should instead be modeled and learned from.
We introduce Moral Entropy, a Bayesian framework that keeps a full posterior over the true label and decomposes its entropy into aleatoric uncertainty (irreducible disagreement about the moral content) and epistemic uncertainty (from insufficient or noisy annotation) -- and lets any heuristic consensus rule be audited against a calibrated ground truth via entropy methods such as cross-entropy/KL, Brier score, and expected calibration error.
Across three corpora and fifteen discourse domains, auditing the standard aggregation rules against this posterior reveals bias that no current pipeline reports: the any-annotator rule disagrees with the calibrated posterior on roughly 30% of items -- pooled, almost entirely false positives, though the errors invert at the foundation level (19.9%/38.9% mean FPR/FNR on MFTC) -- while the stricter majority and two-vote rules miss 63-83% of true positives.

---


### 167. [Assessment of Machine Learning-Based Critical Heat Flux Models in the CTF Subchannel Code for Square Rod Bundle Prediction](https://arxiv.org/abs/2609.21995)

**<font color=#1a73e8>作者：</font>** Aidan Furlong, Vinicius de Melo Monteiro, Robert Salko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The prediction of critical heat flux (CHF), a key safety-related quantity in nuclear thermal hydraulics, remains an important challenge due to its direct relationship with fuel performance and reactor safety. Recent studies have demonstrated that relative to traditional empirical correlations and lookup tables (LUTs), machine learning (ML) methods can substantially improve CHF prediction accuracy. Most ML-based CHF models, however, have been developed and evaluated using tube databases, leaving their applicability to reactor-relevant rod bundle geometries largely unexplored.
This study evaluates ML-based CHF models deployed within the CTF subchannel code using the Electric Power Research Institute (EPRI) rod bundle CHF database. Both pure and hybrid residual correction models are considered in local and semilocal formulations. The tube-trained ML CHF models generally transferred favorably to rod bundle applications and outperformed traditional CHF methods across most geometries and operating conditions. The local hybrid LUT model produced the strongest overall performance, and the semilocal pure ML model remained highly competitive. Comparison against the Bowring correlation, W-3 correlation, and 2006 Groeneveld LUT demonstrated that substantial improvements in rod bundle CHF prediction are possible even when models are trained exclusively on tube data. These findings provide one of the first large-scale assessments of ML-based CHF models in square rod bundles within a production-level subchannel analysis environment and support their broader application in reactor thermal hydraulic analysis.

---


### 168. [COMPLEX: A Closed-Form Certified Embedding of Multiparameter Persistence Modules](https://arxiv.org/abs/2609.22012)

**<font color=#1a73e8>作者：</font>** Sushovan Majhi, Atish Mitra, Žiga Virk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every multiparameter persistence vectorization we know of carries a one-sided Lipschitz upper bound and nothing below it: without a lower gauge there is no sense in which the features are faithful, and no per-prediction guarantee can be built on them. This paper supplies the missing side. COMPLEX is a closed-form, training-free embedding of multiparameter modules -- slice the module along a fixed near-diagonal net, embed each slice barcode by the certified PLACE/PALACE landmark map, concatenate. Under a checkable witnessing-slice coherence condition, holding on 100% of audited pairs on Orbit5k, a single slice carries a closed-form lower gauge: separated modules stay separated in the embedding. With the standard upper bound this gives, to our knowledge, the first two-sided distortion bound for a multiparameter feature map, making faithfulness measurable. Measuring it, we find the floor tight within a small factor of realized distances yet operationally local: an RBF-SVM reaches 91% where 1-NN reaches 78% on the same features. Local per-prediction certification therefore fails for a structural reason common to every landmark embedding whose lower gauge is witnessed by one coordinate. With no learned embedding and no held-out calibration -- only a cross-validated SVM head -- COMPLEX sets the state of the art on both Orbit benchmarks (91.95% on Orbit5k, 92.98% on Orbit100k), level with or above Euler-characteristic surfaces and above transformers and graphcode. On graphs it exceeds GRIL on all four shared molecular benchmarks with one fixed configuration, including the only multiparameter method to clear COX2's majority baseline by more than three points. Closed-form selection -- of the landmark radius, the kernel (certificate-preserving), and the bifiltration set -- buys further accuracy; gradient-shaped adaptation buys none.

---


### 169. [The Supersingular Isogeny Problem in Time and Memory $p^{1/3+o(1)}$, Unconditionally](https://arxiv.org/abs/2609.22018)

**<font color=#1a73e8>作者：</font>** José Luis Delgado  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Given a supersingular elliptic curve $E/\mathbb{F}_{p^2}$, the $\mathsf{OneEnd}$ problem asks for a non-scalar endomorphism of $E$. By known reductions, solving this problem also solves the supersingular endomorphism ring and isogeny problems. Wesolowski obtained exponent $1/3$ under an assumption on the factorization of a small degree, whereas the previous unconditional exponent was $2/5$. We give a Las Vegas algorithm, analyzed without a smoothness heuristic, with expected time and memory \[ p^{1/3}\exp\bigl(O(\sqrt{\log p\,\log\log p})\bigr) = p^{1/3+o(1)}. \]
The algorithm fixes in advance a family of degrees that are products of small primes. Known counting results provide many isogenies of these degrees from curves to their Frobenius conjugates, and a collision estimate shows that the isogenies occur on sufficiently many distinct curves for a random walk to reach one of them. From such a curve, the algorithm splits a degree into two parts, enumerates two lists of shorter isogenies, and matches their targets to obtain an isogeny to the conjugate, whose composition with Frobenius gives the required endomorphism.

---


### 170. [Gricea: An Open Science Platform for Conversational AI Research](https://arxiv.org/abs/2609.22039)

**<font color=#1a73e8>作者：</font>** Nikhil Sharma, Yunlin Gong, Xinyang Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We need studies on conversational AI (CAI) at scale to understand human behavior and shape CAI design. However, fragmented reporting of systems and study configurations hinders replication, extension, and knowledge accumulation. We present Gricea, an open-science platform representing studies as configurable, deployable research artifacts that researchers can run, inspect, share, and reuse. Informed by a formative analysis of prior CAI research, Gricea couples study procedures, participant-facing systems, and conversational task behavior in. In a replication study using Gricea, we replicated configurations 93% of eligible CUI 2026 papers; while also flagging missing information in 96% of papers that hinder faithful replication --- further motivating Gricea's need. In a user study, researchers and practitioners from diverse backgrounds successfully constructed runnable studies addressing various open-ended research questions. Together, these findings demonstrate Gricea's support for constructing, reproducing, and extending CAI studies through shared research artifacts, enabling cumulative knowledge building through open science.

---


### 171. [Available Guardrails: Certifying Selective Prediction across ML Systems](https://arxiv.org/abs/2609.22048)

**<font color=#1a73e8>作者：</font>** Parivesh Priye, Yufeng Wang, Haibin Ling 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A selective predictor acts as a safety gate: it returns an output only when the prediction appears sufficiently trustworthy. Deployments increasingly require this reliability to be certified at a target precision for every reporting unit of interest, such as a tool, policy label, or patient subgroup. The main difficulty is often not whether a granted certificate is valid, but whether finite calibration data can produce one at all. As the gate becomes safer or more fine-grained, some units may receive too little evidence to certify. We make this notion of availability computable through classical exact-binomial inversion and formulate reporting-partition selection, under a fixed group order, as a dynamic program that exposes the trade-off among safety, granularity, and served traffic. The resulting frontier reveals a large population opportunity that finite-sample estimation nearly erases: a truth-informed planner gains $0.157$ mean coverage over support balancing, whereas a naive estimator recovers only $0.005$, making recovery from finite data the central challenge. Constructing candidate partitions on one planning split and selecting among them on another recovers part of this gap, improving mean coverage over support balancing by $0.060$, with the direction reproduced in $59$ of $60$ model effects across three intent-routing datasets and two architectures. A complementary validity-preserving lever, reallocating the familywise error budget across reporting units, recovers additional coverage both with population quantities and noisy estimates. The same frontier recurs, with predictor-specific ceilings, across LLM tool-calling, content moderation, lesion classification, and recommendation. Certified availability is therefore a plannable deployment resource that determines when a safety gate can be certified, at what granularity, and over how much traffic.

---


### 172. [Particle Competition and Cooperation for Robust Graph Convolutional Network Learning Under Label Noise](https://arxiv.org/abs/2609.22053)

**<font color=#1a73e8>作者：</font>** Fabricio Breve  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Convolutional Networks (GCNs) are highly sensitive to label noise, since corrupted supervision can propagate through the graph and degrade learned node representations. This work proposes PCC+GCN, a hybrid framework that uses Particle Competition and Cooperation (PCC) as a graph-based label-refinement stage before GCN training. PCC identifies suspicious labeled nodes through particle domination dynamics and determines whether their labels should be preserved, removed, or reassigned before GCN training. The framework also allows the graph used by PCC to be augmented with feature-based $k$-nearest-neighbor edges, while the GCN itself is trained on the original graph structure and node features. The proposed method was evaluated on ten graph datasets from the NoisyGL benchmark under conventional Uniform, Pair, and Random label noise, as well as under instance-dependent label noise. A detailed hyperparameter analysis was also conducted on Cora, CiteSeer, and PubMed. Under conventional noise, PCC+GCN achieved the highest overall average accuracy and the best average rank among the evaluated methods, with an average gain of $1.67$ percentage points over the baseline GCN across the clean setting and all noisy scenarios. Under instance-dependent noise, PCC+GCN remained competitive with the best-performing robust methods while requiring substantially lower execution time, being the fastest robust method on eight of the ten datasets. The results indicate that PCC-based label refinement provides an effective and computationally efficient preprocessing strategy for improving GCN robustness under noisy supervision.

---


### 173. [Benchmarking World Models for Continual Learning on Compositional Tasks](https://arxiv.org/abs/2609.22055)

**<font color=#1a73e8>作者：</font>** Haoyu Zhou, Joe Watson, Anson Lei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A desirable property of a world model is the ability to learn continually across tasks, adapting to new environments without forgetting what the agent has already learnt. In particular, the ability to retain and reuse knowledge obtained from prior experiences underpins an agent's ability to efficiently adapt to novel environments, as the dynamics of the physical world can often be described in recurring mechanisms. However, the world model's measure of adaptation entangles two abilities: the speed and capacity to learn unseen tasks, and the reuse of knowledge already acquired, since incoming tasks carry novel content alongside what recurs. In order to isolate knowledge reuse from prior experiences, we propose a compositional continual learning benchmark for world models in robot manipulation. Specifically, we design each task curriculum with compositional tasks that combine aspects of the tasks seen in the sequence. We further factorise this composition along the axes of action and perception to better understand how different input modalities bottleneck knowledge reuse. We evaluate state-of-the-art world models under canonical continual learning methods, alongside a modular world model whose dynamics backbone contains explicitly reusable components. Results show that modularity balances reuse against forgetting better than conventional methods, but none solve the problem fully, leaving clear room for continual world models built to reuse without forgetting. More details are available on our project website: this https URL.

---


### 174. [Traffic Sign Recognition for Autonomous Driving Using Branched YOLOv2 and Geometric Features](https://arxiv.org/abs/2609.22060)

**<font color=#1a73e8>作者：</font>** Arefeh Rezaei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic sign recognition (TSR) is an important perception task for autonomous driving and advanced driver-assistance systems, where a system must both localize traffic signs and determine their semantic classes efficiently. This work presents a TSR system based on YOLOv2 for simultaneous detection and classification. Two complementary modifications are studied. First, YOLOv2 is extended with intermediate prediction layers, forming a branched architecture that can terminate inference early for easy cases and reduce computation time. Both whole-image and cell-wise branching strategies are investigated. Second, geometric information is introduced to reduce classification errors between visually similar signs. An unsupervised Bayesian image-segmentation method produces binary representations that are compared with class-specific geometric templates inside YOLOv2 bounding boxes. This information is used either during inference or as an additional signal during training. A dedicated dataset is constructed by combining GTSDB and GTSRB samples using seamless cloning and controlled image transformations. Experiments cover ten traffic-sign classes, with 3,000 training and 300 test samples. The selected branched architecture reports 0.647 s runtime and 0.680 mAP, compared with 0.6607 s and 0.680 mAP for baseline YOLOv2. Geometric verification during inference increases mAP to 0.713, while the geometric-feature training variant achieves 0.697 mAP with a reported runtime of 0.6608 s.

---


### 175. [BrainWideBench: Benchmarking large-scale pretraining and across-animal transfer in multi-region neural recordings](https://arxiv.org/abs/2609.22064)

**<font color=#1a73e8>作者：</font>** Alexandre Andre, Shivashriganesh P. Mahato, Vinam Arora 等 42 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advances in large-scale neural recording have made it possible to collect data across many animals and distributed brain regions, raising the question of whether this scale can be exploited to learn general-purpose neural representations transferable across diverse downstream tasks. Yet, progress toward this goal has been limited by fragmented evaluation protocols and a narrow focus on individual task domains. Here, we present BrainWideBench, a benchmark for evaluating across-animal transfer on multi-region neural recordings, built on the International Brain Laboratory Brainwide Map dataset of neural and behavioral recordings spanning 276 brain regions from 139 mice performing a sensory-guided decision-making task. The benchmark is organized around three complementary task suites that evaluate whether learned representations support downstream decoding of behavior, can predict masked or future neural activity, and can recover biologically meaningful anatomical organization. With this benchmark, we systematically evaluate pretraining methods across transfer settings, including finetuning on downstream objectives and zero-shot generalization to unseen animals. Our results confirm pretraining improves performance over matched single-session baselines, but we show current methods exhibit heterogeneity in transfer capabilities: gains depend strongly on the alignment between pretraining objectives and downstream tasks. No single approach performs uniformly well across all three suites, and most methods are designed to only address a subset of them. Together, these findings suggest that learning representations that jointly generalize across behavior, dynamics, and anatomy remains an open challenge. By providing a unified and reproducible evaluation suite, BrainWideBench establishes a framework for measuring progress toward general-purpose models of the mouse brain.

---


### 176. [OmniVBench: A Benchmark and Large-Scale Dataset for Omni Reference-to-Video Generation](https://arxiv.org/abs/2609.22069)

**<font color=#1a73e8>作者：</font>** Wenxue Li, Peiyan Guan, Haoyang Jiang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-to-video (R2V) generation is evolving toward increasingly general and versatile reference control, giving rise to the emerging paradigm of omni R2V generation. However, existing benchmarks fall short of these emerging capabilities: their test cases cover limited reference types and compositions, and their evaluation protocols largely assess holistic reference consistency, overlooking whether reference factors are properly preserved, disentangled, and routed. Meanwhile, the high cost of constructing omni R2V training data makes suitable training resources scarce. To address these gaps, we introduce OmniVBench and the Omni-R2V Dataset for evaluating and training omni R2V models. OmniVBench expands R2V evaluation across broader reference types, fine-grained control tasks, and richer reference compositions, covering 7 task families and 18 fine-grained tasks spanning content, motion, style, structure, narrative, and multi-reference settings. We introduce factor-grounded evaluation with 12,172 case-specific checklist items, assessing whether intended reference factors are faithfully preserved, correctly disentangled and bound to their targets, and properly realized according to the instruction. We further introduce the Omni-R2V Dataset, bringing industrial-grade training resources for diverse R2V tasks to the broader research community. Drawing primarily on a large-scale corpus of professional video footage, it comprises 340K processed training samples spanning diverse reference types and multi-reference compositions. We develop task-specific pipelines for reference-target pair construction, offering a practical and scalable recipe for omni R2V data construction. Extensive evaluation of advanced open- and closed-source R2V models reveals clear performance gaps across task families and evaluation dimensions on OmniVBench, highlighting remaining limitations of current R2V models.

---


### 177. [A Sociotechnical Review of Algorithms in Health Systems: Technical, Cost, and Human-Centered Considerations](https://arxiv.org/abs/2609.22070)

**<font color=#1a73e8>作者：</font>** Victoria Chui, Kelly McConvey, Shion Guha  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) applications in healthcare are becoming increasingly prevalent, to assist health systems, providers, and patients with tasks such as decision-making, risk prediction, and diagnosis. This increasing computational potential brings AI applications to the forefront of workplace decision making, often without full consideration of subsequent computational, organizational, and social costs. These applications are leveraged to reduce healthcare costs and increase efficiency of daily tasks, with model-related costs being considered at varying levels of granularity. To understand these trends, we critically analyze 114 papers to examine how cost-aware AI models have been developed for health systems. We explore the data, method, and outcome choices of these models, as well as their intersection with cost and human-centered concerns, highlighting the gaps in rigorous sociotechnical model design. From these trends, we define model costs and subsequent dimensions, presenting insight into those studies reporting financial, computational, organizational and/or social measures. Further, we critique the benefits and challenges of evaluating model-related costs and sustainability concerns when developing AI models for health systems.

---


### 178. [APort Vault: Benchmarking AI Agent Payment Authorization with the Open Agent Passport](https://arxiv.org/abs/2609.22076)

**<font color=#1a73e8>作者：</font>** Uchi Uchibeke  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> APort Vault is a benchmark for payment authorization in tool-using AI agents. It replays 4,371 attacks written by humans against a live payment agent during a public capture-the-flag event, across 14 models from 8 labs, five policy configurations and two replay tracks, with and without a deterministic pre-action check implementing the Open Agent Passport (OAP) specification. 225,964 evaluations completed. We report five distinct events per evaluation, because collapsing them is how an agent benchmark produces a number that does not survive review.
Requests are common and their rate differs far more across configurations than across models, though each attack exists at exactly one configuration so policy and attack cohort vary together: 10.9% of model-alone evaluations at Level 1, 3.0% at Level 2, 0.1% at Level 3, 79.4% at Level 4. On the 1,293 Level 4 prompts, each evaluated on every model, request rates run from 71.2% to 84.3%, and 809 prompts (62.6%) elicited a request from all fourteen models, each ending in a successful payment to the level's allowlisted recipient.
The authorization boundary is where the conditions diverge. At Levels 2 to 4, transfers to recipients the passport did not permit number 140 of 76,842 with the model alone and 0 of 69,297 behind the layer, and 105 against 0 on 68,970 matched model, prompt and track triples. The zero spans 790 source sessions, giving a per-session upper bound of 0.38%. It was not obtained by refusing payments: 25,370 payments executed behind the layer, while the policy denied 187 of the 25,640 transfer calls it evaluated, 148 of them for a forbidden recipient.
We release the 225,964 evaluations, the level passports, the scoring code and the analysis script at this http URL .

---


### 179. [Cross-sector generalization of accident-process role classification in occupational accident narratives](https://arxiv.org/abs/2609.22081)

**<font color=#1a73e8>作者：</font>** Aho Yapi, Pierre Latouche, Arnaud Guillin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Occupational accident narratives contain valuable information about work situations, unfavourable conditions, accident events, and their consequences. Automatically structuring these narratives can facilitate large-scale accident analysis and support occupational risk prevention. However, the terminology and writing styles used to describe accidents vary considerably across sectors and organisations, raising questions about the ability of automated coding systems to generalize beyond their training domain. In this paper, we evaluate the cross-sector generalization of accident-process role classification in French occupational accident narratives. We construct an expert-annotated corpus in which factual units are classified into four roles: work situation (A0), explicitly reported unfavourable condition (A1), accident event or deviation (B), and reported consequence (C). The role classifiers are developed and selected exclusively on 42,244 factual units extracted from 6,040 construction-sector narratives and are then evaluated on unseen corpora from the metallurgy and chemistry--plastics sectors, as well as on an independently collected company corpus, without retraining or target-domain tuning of the role classifier. We compare frozen pretrained representations with task-specific fine-tuning and supervised representation-learning strategies. The results show that task-specific adaptation consistently improves cross-domain transfer over frozen representations. Across repeated training runs, the three leading task-adapted strategies achieved average balanced accuracies between 85.6% and 85.8% across the three target corpora. These findings support the development of transferable assisted-coding systems capable of consistently structuring heterogeneous occupational accident narratives for expert review and cross-sector prevention analysis.

---


> [!TIP]
> 当前位于：**151-179**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-179**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
