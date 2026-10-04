# 📦 其他研究 | 2026年10月05日

> 本类共 **385** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-385](./part-08.md)

---

### 201. [IQS-BO: In-Context Query Selection for Bayesian Optimisation](https://arxiv.org/abs/2610.01269)

**<font color=#1a73e8>作者：</font>** Luca Geminiani, Nadja Klein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian Optimisation (BO) is a powerful framework for the optimisation of expensive black-box functions, but typically requires refitting a surrogate and maximising an acquisition function at every evaluation step. In-context approaches based on Prior-data Fitted Networks (PFNs) amortise part of this cost by pre-training transformers on functions drawn from synthetic priors. PFNs4BO amortises the surrogate but still relies on a numerically maximised acquisition function, while FIBO performs BO fully in-context by sampling optimiser locations from a learned density, which fixes the decision rule and admits no surrogate. Learned acquisition functions score a finite candidate set with a trained network, but, lacking a label for the query, learn the score by reinforcement learning on previously solved tasks. We propose IQS-BO, a PFN that learns the query decision by supervised learning on synthetic priors. In a single forward pass, IQS-BO predicts the probability that each candidate maximises the objective over the set, and we show that the minimiser of its objective is the posterior probability of this event. The model can be pre-trained without a surrogate for fully in-context BO, or take the predictions of a fixed probabilistic surrogate as additional input, amortising only the decision step. Our method proposes queries at a fraction of the cost of acquisition-based methods, while either matching or outperforming standard BO with Gaussian processes (GPs) and available in-context methods on synthetic and real-world benchmarks. Finally, we propose a mixture prior for pre-training PFNs which combines samples from GPs with functions exhibiting warped inputs, isolated narrow optima, or plateaus that are poorly modeled by stationary kernels common in GP surrogates. We show that pre-training on this prior can lead to improved optimisation performance.

---


### 202. [Not All Is Lost: Repairing Lossy User Preference States of Personalization Encoders](https://arxiv.org/abs/2610.01270)

**<font color=#1a73e8>作者：</font>** Parthiv Chatterjee, Dhiraj Golhar, Ummesalma Diwan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalization encoders compress evolving interaction histories into preference states used to rank items or condition text generation. A task head operating only on this state can miss useful evidence that remains in the frozen encoder's cached representations for individual timesteps. We study this recoverability gap and propose REPAIR, which compares cached representations with the current preference state in a compact learned coordinate space. It resolves corrective evidence over extended history, recent interactions, and localized bursts. It then selects which patterns at which timesteps contribute and adds their aggregate correction to the state before the task head. Encoder-host repair reuses representations from the existing forward computation without re-encoding the history. Across MovieLens, PENS, MIND, and Amazon Reviews 2023, training only REPAIR improves MRR and nDCG@10 for all twelve representative recommendation hosts while both encoder and task head remain frozen. Head-only finetuning of the same hosts yields smaller gains. For example, Mamba4Rec on MovieLens gains 3.96 MRR points, compared with 0.19 from head-only finetuning. Rank and temporal diagnostics support a compact, host-dependent corrective structure. In personalized generation, IMPerSumm improves the two reported weighted PerSEval variants, which assess responsiveness to user preference, by up to 25.23%. These results support post-compression state correction and distinguish the availability of preference evidence from its downstream use.

---


### 203. [PickMoment: Continuous-Time Single-Image-to-Video via Learning Deblurring and Blur-to-Video](https://arxiv.org/abs/2610.01279)

**<font color=#1a73e8>作者：</font>** Junseong Shin, Hyeonsu Jo, Daehyun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion blur arises from the temporal integration of a continuous sharp signal over a finite exposure window, yet existing learning-based methods sidestep this physical model and predict only the sharp signal itself: most single-image deblurring methods recover a single frame at the exposure center, while blur-to-video methods predict a fixed set of frames. We introduce PickMoment, a continuous-time reformulation that directly learns the interval-mean blur over arbitrary sub-intervals of the exposure with a single deterministic model. Drawing an analogy to MeanFlow's average-velocity formulation, we train the model with three supervisions derived from the blur integral: an empirical reconstruction loss from available subframes, an additivity loss that enforces self-consistency across overlapping sub-intervals, and a sharp-frame loss anchored at the zero-interval limit. A single trained model unifies single-image deblurring, blur-to-video generation, and continuous-time pick-a-moment recovery as different queries to the same network, with no separate training for each task. Our PickMoment achieves state-of-the-art performance among generative-based deblurring methods on GoPro and HIDE while competitive against restoration-based methods on RealBlur, and the highest per-frame fidelity on GoPro-7 blur-to-video, all in a single forward pass without iterative sampling.

---


### 204. [Trustworthy Data- and ML-Ops for Intelligent Transportation Systems and Logistics](https://arxiv.org/abs/2610.01282)

**<font color=#1a73e8>作者：</font>** Antonio Emanuele Cinà, Giovanni Scodeller, Cecilia Caterina Pasquale 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of Intelligent Transportation Systems and Logistics (ITS\&L) has become a cornerstone of the modern social economy, relying heavily on the integration of Data, Artificial Intelligence (AI), and, more specifically, Machine Learning (ML). This paper provides a comprehensive review of Trustworthy Data and Machine Learning Operations (DataOps and MLOps) in the ITS\&L domain, underscoring their importance in improving efficiency, reliability, and decision-making precision within transportation and logistics services. We begin by identifying gaps in current literature, offering clear context for our contribution. Subsequently, we explore the complexities of DataOps and MLOps, discussing their necessity, key components, available tools, practical insights, and case studies relevant to ITS\&L. Additionally, we address the critical issue of Trustworthiness in AI applications, examining methods and tools designed to strengthen confidence in AI systems - especially in real-world ITS\&L scenarios. The paper concludes with a discussion of persisting challenges and future prospects in this rapidly advancing field, aiming to serve as a vital resource for researchers, industry practitioners, and policy makers. Overall, this work not only establishes a foundational understanding of DataOps and MLOps in ITS\&L but also charts a path for further research and innovation in developing more efficient, sustainable, and trustworthy intelligent transportation and logistics systems.

---


### 205. [ShelfChange3D: Object-Level 3D Change Detection for Retail Shelf Monitoring](https://arxiv.org/abs/2610.01283)

**<font color=#1a73e8>作者：</font>** Lingyi Zhou, Yunke Wang, Mengyu Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable shelf monitoring is an important capability for retail automation, yet existing out-of-stock detection methods mainly operate in image space and lack metric 3D localization for downstream robotic systems. We formulate shelf monitoring as object-level 3D change detection: given two RGB-D observations captured at different times, the goal is to identify changed products and localize each change with a 3D bounding box. To support this task, we introduce ShelfChange3D, comprising 145K synthetic and 5K real-world paired RGB-D observations with object-level 3D change annotations. We further propose ChangeBox, an end-to-end framework that jointly reasons over paired observations and predicts object-level 3D change boxes. To improve localization accuracy, we introduce a geometry-based refinement stage that exploits depth and gravity prior to estimate relative pose and refine predicted boxes. Experiments show that ChangeBox outperforms existing change detection baselines, with further gains from refinement and effective transfer from synthetic to real-world observations.

---


### 206. [Model validation in machine learning: A scenario-based guide from hold-out splits to nested group cross-validation in biomedical and applied research](https://arxiv.org/abs/2610.01284)

**<font color=#1a73e8>作者：</font>** Mehmet Baygin, Sengul Dogan, Turker Tuncer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model validation estimates the performance of a complete learning procedure on new data. However, an invalid split can produce an optimistic and stable result. This tutorial reviews hold-out validation, train/validation/test designs, repeated random subsampling, k-fold and repeated stratified cross-validation, leave-one-out and leave-p-out schemes, group-aware validation, and nested group cross-validation. General machine-learning principles are linked to EEG epochs, paired-eye OCT images, repeated clinical measurements, and multicenter data. Eight controlled scenarios compare flawed and leakage-safe designs: seven use locked confusion matrices with auditable metrics, and one uses a reproducible repeated-study simulation. The scenarios cover global feature selection, normalization leakage, dependent records, center mixing, repeated test-set use, and estimator instability. Bias, variance, metric aggregation, uncertainty, and computational cost are also examined. A data-size matrix, a decision tree, and reporting checklists are provided. Reproducible MATLAB templates and scikit-learn counterparts are included. The results show that no validation method is universally best. The independent unit must match the intended deployment target. Every data-dependent operation must also exclude the observations used for performance estimation.

---


### 207. [ODDR: One-Step Deshadow Diffusion via Reward Guidance](https://arxiv.org/abs/2610.01291)

**<font color=#1a73e8>作者：</font>** Junseong Shin, Kijun Kim, Minseong Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in deep learning for shadow removal have significantly enhanced image quality and realism. However, most approaches rely on real-world paired datasets, which are costly to collect and often limited in scene diversity, leading to limited generalization. To address these limitations, we propose One-step Deshadow Diffusion via Reward guidance (ODDR), a new framework that achieves efficient and high-fidelity shadow removal without relying on real-world paired supervision. Our method begins with One-step Deshadow Diffusion (ODD), a baseline model trained on synthetic shadow data for efficient one-step shadow-free reconstruction. We further adapt ODD into ODDR using ShadowReward. In contrast to traditional, annotation-heavy approaches, ShadowReward is the first reward model for shadow removal trained entirely without human annotation. It learns to mimic human perceptual judgments by ranking synthetically generated images with controlled degradations, such as texture distortion and boundary artifacts. This reward-guided fine-tuning enables ODDR to close the synthetic-to-real domain gap. Extensive experiments show that ODD achieves strong performance without relying on real-world paired supervision, and ODDR further improves the results, narrowing the gap to fully supervised methods trained on real-world paired data while maintaining higher computational efficiency as a single-step model.

---


### 208. [GNSS Spoofing in Mobile Devices: A Survey on Impact and Countermeasures](https://arxiv.org/abs/2610.01294)

**<font color=#1a73e8>作者：</font>** Robert Argo, Andrea Nardin, Alex Minetto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smartphones rely on Global Navigation Satellite System (GNSS)-based positioning for many of the functions they execute everyday. The GNSS receivers embedded in smartphones are susceptible to anthropogenic radio frequency interference attacks in the forms of jamming and spoofing due to the low-power and open-architecture signals they receive from the satellite constellations. While jamming is a practice that denies a GNSS receiver the ability to form a position, velocity, and time (PVT) solution, spoofing represents a more insidious threat by using forged satellite signals that aim at causing the victim receiver to compute a false PVT solution. The ubiquity of smartphones and the sensitive geolocation data they hold make them a primary target for malicious spoofing. However, their hardware constraints and the lack of deep visibility into the GNSS receiver processing chain create significant hurdles for effective countermeasures. Existing surveys comprehensively explore general spoofing countermeasures but fail to address these mobile-specific limitations. This article fills that gap with a novel survey focused on techniques viable within the unique constraints of smartphone architectures. Specifically, we establish a taxonomy for defining GNSS spoofing attack effects and countermeasures, provide a historical review of smartphone vulnerability characterization, and provide an overview of techniques proposed to detect and counteract smartphone spoofing threats, offering a comparative framework to weigh their respective pros and cons on mobile platforms.

---


### 209. [Questionnaire-Guided Disaggregation of Energy Appliance Use for Domestic Smart Meter Data](https://arxiv.org/abs/2610.01297)

**<font color=#1a73e8>作者：</font>** Achal Nanjundamurthy, Rupam Misra, Suzanne Little 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ireland's smart metering programme records electricity use at 30-minute resolution, with smart meters installed in over 80\% of households as of late 2025. While this is useful for billing of smart, time-of-use tariffs, it is too coarse to capture use of domestic appliances. We present a label-free disaggregation system that breaks usage data into 9 appliance categories by combining event detection for high-power loads with questionnaire-guided estimation. Our evaluation draws on four datasets: a calibration household with a commercial comparator, two public benchmarks (UK-DALE and REFIT) with per-appliance sub-metering, and a smart meter dataset of more than 4,800 years of use from 2,968 Irish consumers. Compared against two independently developed disaggregation systems our hybrid method combining analysis of usage data with questionnaire results, achieves the lowest whole-decomposition error on all buildings across the datasets, with better month-level performance over 54 paired months ($p<0.001$, Holm-corrected). Our method provides useful advice on a household's energy consumption patterns and advice on how to reduce or shift usage on some appliances in order to reduce costs.

---


### 210. [A Systematization of Knowledge on DeFi Vaults: Architectures, Curation Mechanisms, and Strategy Design](https://arxiv.org/abs/2610.01300)

**<font color=#1a73e8>作者：</font>** Davide Mancino, Luca Pennella  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decentralized finance (DeFi) vaults are smart-contract-based asset management systems that pool deposits, execute programmable strategies, and mint tokenized shares representing claims on underlying assets and strategy performance. As vault designs have evolved from early yield aggregators to modular, actively managed systems, a new control layer, curation, has emerged to select strategies, configure risk parameters, and coordinate operational execution, introducing principal-agent dynamics and new failure modes.
This paper systematizes DeFi vault architectures and curator-mediated control planes through (i) a unified system model and formal definitions for share accounting, roles, and operational dependencies, and (ii) three complementary taxonomies covering vault exposures and objectives, curator governance and accountability mechanisms, and strategy execution patterns together with their failure modes. We further map a representative set of production protocols to the proposed dimensions. The frameworks in this work aim to support rigorous analysis and safer design of blockchain-based financial applications.

---


### 211. [STAGE: Subspace-Targeted Affine Generative Erasure for Text-to-3D Models](https://arxiv.org/abs/2610.01302)

**<font color=#1a73e8>作者：</font>** Karol Dziekan, Przemysław Spurek, Dawid Malarz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept erasure suppresses a target concept while preserving behavior on unrelated inputs. Existing closed-form methods were designed for 2D image diffusion and assume a single generative pathway, so one edit must cover geometry and texture at once. Native 3D generators, which synthesize structured 3D representations directly rather than by lifting 2D samples, violate this assumption. We show that shape and object concepts must be erased in the structural stage of the pipeline and material concepts in the appearance stage. We therefore formulate erasure in native text-to-3D as a stage-aware editing problem and introduce STAGE, a training-free, closed-form framework. STAGE confines each edit to the low-dimensional subspace spanned by the differences between erase and anchor embeddings, and relaxes the norm-preserving (orthogonal) constraint of prior editors into a least-squares affine correction that maps target activations onto safe anchors subject to a penalty on the displacement of retained prompts. The correction applies to the structural stage, the appearance stage, or both. We find that the stage an edit must reach is determined by concept type. On TRELLIS, the standard open native 3D generator, across 15 shape, material, and object concepts, STAGE reaches 66.7 on a composite score that balances forgetting the target concept against preserving everything else, aggregating CLIP-based semantic and physical metrics, versus 53.2 for the strongest adapted baseline.
Code: this https URL
Project Page this https URL

---


### 212. [ARROW: Arbitrary Reconstruction and Tracking of 4D Observations in the Wild](https://arxiv.org/abs/2610.01314)

**<font color=#1a73e8>作者：</font>** Ilya Fradlin, Christian Schmidt, Jens Piekenbrinck 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic scenes may be captured by a moving camera, multiple video streams, or images taken at different times. These observations reveal complementary aspects of scene geometry and motion, yet bringing them together requires establishing correspondence across viewpoints, capture times, and visibility changes. We introduce ARROW, a feed-forward model that unifies 3D reconstruction and 3D point tracking from arbitrary image sets. At its core is a novel order-invariant querying approach, which allows the association of queries with observations across arbitrary inputs. We show that exposing the model to more diverse sets of inputs during training results in improved task performance. Moreover, the resulting model is capable of generalization to a wider range of tasks including multi-view tracking. Trained with this strategy, ARROW establishes a new state of the art in 3D tracking on WorldTrack and TAPVid-3D and outperforms dedicated multi-view trackers on an adapted RGB-only MVTracker benchmark, while remaining competitive across 3D reconstruction tasks. Code and weights are publicly available.

---


### 213. [EP-Flow: Disordered Crystal Structure Prediction without Site-Level Annotations](https://arxiv.org/abs/2610.01315)

**<font color=#1a73e8>作者：</font>** Qiuliang Liu, Liming Wu, Qi Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models have made rapid progress in ordered crystal structure prediction, yet many functional materials are intrinsically disordered, with substitutional mixing, vacancies, or interstitial species controlling their properties. Existing crystal generators either assume deterministic site occupations or require site-level disorder annotations, which are often unavailable when the chemical formula is the primary input. We formulate disordered crystal structure prediction through an Occupancy Distribution Matrix (ODM), a continuous site-by-species representation that unifies ordered crystals, solid solutions, vacancy disorder, and interstitial occupancy. A valid ODM must satisfy coupled site-wise occupancy, mass-conservation, and non-negativity constraints, placing each sample on a formula-dependent transportation polytope. We propose Entropic Polytope Flow (EP-Flow), a marginal-constrained flow matching framework that canonicalizes heterogeneous polytopes into a shared double-centered space, learns a marginal-preserving flow, and recovers feasible occupancies through a Sinkhorn inverse map. By jointly generating occupancies, fractional coordinates, and lattice parameters, EP-Flow achieves state-of-the-art performance on formula-conditioned disordered CSP benchmarks derived from COD and MPDS, substantially outperforming adapted ordered-crystal generators. Analyses further show that EP-Flow recovers sparse and chemically meaningful local disorder patterns rather than merely matching global composition statistics.

---


### 214. [Prediction-powered Neural Architecture Search](https://arxiv.org/abs/2610.01317)

**<font color=#1a73e8>作者：</font>** Pascal Janetzky, Yuxin Wang, Michael Klar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating candidate architectures in neural architecture search (NAS) faces an inherent trade-off: on the one hand, reliable performance labels are limited because training and evaluating architectures is costly; on the other hand, zero-cost proxies (ZCPs) are cheap to compute at large scale but can be noisy. Yet, how to effectively combine these two sources of supervision remains unclear. In this paper, we propose PPNAS, a novel prediction-powered inference (PPI) approach for NAS. PPNAS fuses (1) a small set of architectures with observed performance labels and (2) a large set of architectures with ZCP information. To combine these two sources of supervision, PPNAS exploits the ordinal information provided by ZCPs to construct additional pairwise ranking supervision, while PPI debiases systematic discrepancies between ZCP-based and true performance rankings. We evaluate PPNAS in end-to-end predictor-based NAS, where it achieves state-of-the-art under limited evaluation budgets. To the best of our knowledge, PPNAS is the first prediction-powered approach for label-efficient NAS.

---


### 215. [Feature Selective Model Collapse in Diffusion Models: Total Replacement versus Fixed-Budget Training](https://arxiv.org/abs/2610.01318)

**<font color=#1a73e8>作者：</font>** Hanna Malet, Gabriel Turinici  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model collapse arises when generative models are trained on synthetic data produced by earlier models. The phenomenon has attracted considerable attention because of its societal and technical implications. However, previous studies have reached seemingly contradictory conclusions: replacing real data with synthetic data causes collapse (Shumailov et al.), yet accumulating real data alongside synthetic data can prevent it. For diffusion models, we study an intermediate regime typical of finite-budget pipelines: all past datasets and the real data are kept, but each new model is trained on a fixed-size sample from this growing pool, so the real fraction vanishes without any data being removed. Experiments on a 2D spiral dataset as well as the image benchmarks (MNIST, Fashion-MNIST, and CIFAR-10) show that replacement protocol degrades dataset rapidly as in the literature, whereas the fixed budget degrades only partially, sparing some features. A linear-response model of the multi-generational parameter dynamics, analyzed by stochastic recursion, confirms that the two protocols differ: some features will be fragile and lost within a few generations for both protocols, while some will be robust and preserved over practically unbounded horizons under the fixed budget protocol.

---


### 216. [ProtoFlow: Prototype-Guided Flow Matching for Multivariate Time Series Forecasting](https://arxiv.org/abs/2610.01320)

**<font color=#1a73e8>作者：</font>** Shibo Feng, Wanjin Feng, Yang Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative modeling has shown strong promise for multivariate time mseries (MTS) forecasting, especially scale to high-dimensional settings. Diffusion-based methods achieve competitive performance but typically require many sampling steps at inference. VAE-based non-iterative forecasting frameworks have therefore emerged as an efficient alternative. Within this line of work, vector quantization (VQ) enables controllable latent space modeling by mapping multivariate series into compact discrete representations. Existing VQ-based forecasting methods, however, typically rely on autoregressive (AR) token generation, which suffers from exposure bias and training-inference mismatch. Flow matching provides an efficient non-autoregressive alternative for latent forecasting, but existing formulations usually initialize transport from a generic Gaussian prior. We instead observe that the trained VQ codebook already captures representative latent prototypes and can thus serve as a more informative prior for flow matching. Based on this insight, we propose ProtoFlow, a forecasting framework that combines vector-quantized autoencoding with Prototype-prior Flow matching. Our method first maps multivariate sequences into a discrete latent space, then constructs a structured prior from the learned codebook, and finally learns a DiT-based rectified flow to transport samples from this prior to future latent representations conditioned on historical observations. By replacing generic noise initialization with a learned prototype prior, ProtoFlow avoids the rollout mismatch of AR token prediction and promotes faster training convergence. Extensive experiments on benchmark datasets show that it consistently achieves superior forecasting performance with efficient inference.

---


### 217. [Clifford Sheaf Neural Networks](https://arxiv.org/abs/2610.01322)

**<font color=#1a73e8>作者：</font>** Kotaro Kamiya, Joel Nicholls  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Clifford Sheaf Neural Network (CSNN), an equivariant sheaf neural network for geometric graphs that places a Clifford algebra on each stalk of a cellular sheaf and transports multivector features along edges. The canonical choice of restriction map for sheaves with algebra-valued stalks is algebra homomorphism. Adding the constraint of equivariance, the naive choice becomes versor conjugation. However, versor conjugation is expressively weak, so we drop algebra homomorphism and arrive at the K-term sandwich. The resulting sheaf Laplacian is positive semidefinite by construction, needs no versor constraint, and still mixes grades. Our main contribution characterizes the resulting family of restriction maps along three axes: which grades a map couples, how much of the endomorphism space it reaches, and how well it is conditioned. The K-term sandwich spans half of the endomorphism space, and in Cl(3, 0, 0) it corresponds to the maps that commute with the central pseudoscalar. The number of terms controls expressivity. CSNN is the reversion member, a first-order model by construction and the grade-mixing corner of this family, developed as a sheaf construction for graph-level equivariant regression.

---


### 218. [PPO-HRAP: Proximal Policy Optimization with a Hybrid Regime-Aware Policy for Risk-Controlled Trading](https://arxiv.org/abs/2610.01325)

**<font color=#1a73e8>作者：</font>** Duong Hien Chi Kien, Thanh Trung Huynh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for trading often struggles to balance upside participation with drawdown control. Profit-only policies can collapse toward passive long exposure on upward-drifting assets, while aggressively risk-penalized rewards can become too defensive during volatile periods. This paper proposes PPO-HRAP, a hybrid regime-aware policy that combines Proximal Policy Optimization with an interpretable regime prior. The agent observes both market features and portfolio-state variables, receives a reward combining portfolio log return, VIX-conditioned drawdown-increase penalty, target-exposure deviation, and turnover cost, and executes a blended action between the PPO actor output and a regime-derived target exposure. On the held-out 2020-2022 SPY test window, PPO-HRAP achieves 27.62% total return, 8.48% annualized return, 0.6447 Sharpe ratio, 0.8588 Sortino ratio, and 0.4592 Calmar ratio, while reducing maximum drawdown from 34.10% for Buy and Hold to 18.47%. Across five SPY seeds, PPO-HRAP remains stable with mean total return $0.2725 \pm 0.0109$ and mean Sharpe ratio $0.6219 \pm 0.0565$. Single-run cross-asset tests on QQQ and DIA further show that the proposed method ranks first on total return and Sharpe ratio for all three reported assets. These results suggest that blending learned actions with a volatility-aware regime prior is a practical way to improve risk-adjusted trading behavior, although the current policy still incurs high turnover and cross-asset robustness beyond SPY remains limited to single-run evidence.

---


### 219. [An ontology for cross-sectoral crisis management: core and public health modules](https://arxiv.org/abs/2610.01326)

**<font color=#1a73e8>作者：</font>** Aldo Gangemi, Rita T. Sousa, Luigi Asprino 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents the European Crisis Management Ontology (ECMO), a modular OWL-based ontology intended as a cross-sectoral reference for disaster risk reduction and response. ECMO is designed to be organised as a network of ontological modules. Among the modules, ECMO-CORE captures fundamental crisis management concepts such as hazard, event, exposure, impact, and response measure and uses ontology design patterns and the OWL2 punning technique to resolve ambiguities between hazard types and event manifestations. In addition, domain-specific modules are defined as in the case of the public health module aligned with SNOMED CT and ICD-11. To demonstrate the resource's utility, we used ECMO to represent the data of the Epidemic Intelligence from Open Sources system of the Joint Research Centre to generate an end-to-end pipeline that populates an ECMO-compliant knowledge graph from unstructured epidemiological news. Initial results demonstrate that ECMO provides the formal guardrails necessary for consistent and unified knowledge representation and integration. The ontology is publicly available at this https URL and is released under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

---


### 220. [CLASP: Continual Low-rank Adapters for Spatially Placed Concepts from One Hypernetwork](https://arxiv.org/abs/2610.01331)

**<font color=#1a73e8>作者：</font>** Wojciech Gromski, Patryk Krukowski, Jan Miksa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual personalization of text-to-image diffusion models requires sequentially acquiring new concepts while retaining previously learned ones. However, existing methods either suffer from catastrophic forgetting or rely on storing additional concept-specific parameters and spatial components, causing their parameter footprint to grow with the concept stream. This limits their ability to scale to long sequences of personalization tasks. We propose a rehearsal-free approach that uses a single fixed-size hypernetwork to continually personalize a frozen diffusion model. Instead of expanding the model as new concepts are acquired, the hypernetwork dynamically produces the concept-specific adaptations required for personalization while preserving previously learned concepts. Our framework further integrates spatial control into the personalization process, allowing users to specify where a personalized concept should appear without introducing additional per-concept components. This formulation enables continual personalization with a parameter footprint that remains independent of the number of learned concepts, aside from compact concept representations. Experiments demonstrate strong retention of previously learned concepts and reliable spatial grounding, matching or improving upon existing methods while scaling effectively to long streams of personalization tasks.

---


### 221. [Robust Non-Clairvoyant Scheduling with Classification Models](https://arxiv.org/abs/2610.01343)

**<font color=#1a73e8>作者：</font>** Anthony Dugois, Vincent Fagnon, Giorgio Lucarelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the classical single-machine scheduling problem of minimizing the sum of completion times of jobs in a non-clairvoyant setting, where the processing time of each job remains unknown until its completion. This is a hard problem for which no constant competitive algorithm is possible. Inspired by robust optimization and learning-augmented algorithms, we introduce a novel robustness framework that leverages structural information provided by a classification model to overcome this limitation. Specifically, we assume that jobs are partitioned into classes and we have access to the confusion matrix of the classifier, whose entry $(k,\ell)$ indicates the number of jobs predicted to belong to class~$k$ but that actually belong to class~$\ell$. In this manner, we are able to characterize uncertainty as a set of permutations within each predicted class, rather than as a collection of discrete numerical scenarios, avoiding the computational difficulty of classical robust metrics, such as Min-Max and Min-Max Regret. In addition to these worst-case metrics, we also consider the expected objective over all scenarios. We first propose an optimal non-adaptive strategy that is oblivious with respect to all three robust criteria. We then investigate adaptive and randomized algorithms, showing that they can outperform the optimal non-adaptive strategy when the matrix exhibits particular structural properties.

---


### 222. [Verify Claims, Not Scores: Evidence-Based Verification of Modular Agents](https://arxiv.org/abs/2610.01348)

**<font color=#1a73e8>作者：</font>** Ali Atiah Alzahrani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When developers change one component of an agent, such as its controller, a learned model or its verifier, they usually judge the change by an aggregate task score. That score cannot tell whether improvement was attainable, which component lost value, or what the agent's own checks certify. We introduce a claim-specific verification audit for modular agents that plan, act, check and refine. Instead of scoring the agent, the audit scores the evidence: each conclusion is recorded with the evidence behind it, one of four verdicts (supported, unsupported, unresolved or not evaluated) and the boundary within which it holds. Three tools supply that evidence. Oracle policies measure attainable improvement under an explicitly stated action set, so that a low value can be traced to the evaluation rather than to the environment. Replacing one component at a time with a perfect counterpart locates lost value, with null results read as unresolved whenever a downstream component could mask them. A separate test asks whether the verifier's score identifies the quantity it is read as bounding. Applied to a constrained portfolio-allocation agent in a synthetic market with known hidden regimes, the audit shows that the value of perfect regime information depends on the action set used to measure it, that the scenario generator discards most of the regime signal while better local fidelity does not improve decisions, and that the runtime verifier can be bypassed with no visible change in outcomes. The contribution is the protocol and the evidential distinctions it enforces; the empirical findings are specific to the agent and environment studied.

---


### 223. [Discrete Wasserstein Flows for One-Step Generative Modeling](https://arxiv.org/abs/2610.01355)

**<font color=#1a73e8>作者：</font>** Alessandro Micheli, Andrea Zerio, Samir Bhatt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a new framework for one-step generative modelling on finite state spaces. To extend drifting beyond continuous domains, we use discrete Wasserstein geometry to define a target-relative KL gradient flow over the transitions of a reversible Markov kernel. We realize this probability flow at the particle level through Markov jumps and amortize the resulting transport updates into a latent-conditioned generator, so that the iterative dynamics are required only during training while inference remains one-step. In a controlled setting where the underlying distributions and transport dynamics can be computed exactly, we verify KL dissipation, consistency between the particle dynamics and the probability flow, and the predicted numerical scaling. We further show that a finite-capacity neural generator can track these exact transport targets while retaining one-step generation. These results validate the basic construction and provide a foundation for scaling Discrete Drifting to structured discrete data.

---


### 224. [Port-Hamiltonian Neural Networks for Systems with Multiple Asymptotically Stable Equilibria](https://arxiv.org/abs/2610.01356)

**<font color=#1a73e8>作者：</font>** Simon Heilig, Jens Püttschneider, Mohammad Itani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stable port-Hamiltonian neural networks certify asymptotic stability by construction. Yet, their Hamiltonian is a global Lyapunov function with a single global minimum, so they can represent only dynamic systems with {one} attractor. We demonstrate that this excludes even simple systems with energy landscapes forming a double well, and we overcome the restriction by parametrising the Hamiltonian as a {product} of Bregman divergences generated by one input-convex network. We prove that the resulting model is locally Lyapunov stable, that the coexistence of stable equilibria forces additional non-asymptotically-stable equilibria to exist, that all equilibria lie in a bounded region, and under a hyperbolicity assumption that almost-everywhere stability holds. On three systems our approach is able to recover the energy surface characteristics and improve the convergence speed by 1.8$\times$-8.5$\times$.

---


### 225. [From Redundancy to Minimality: Fixed-Point-Guided Hierarchical Reduction of Learned Piecewise-Linear Dynamics](https://arxiv.org/abs/2610.01369)

**<font color=#1a73e8>作者：</font>** Hiroto Tamura, Gouhei Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding a nonlinear dynamical system from time series requires not only reproducing its trajectories, but also identifying a simple representation that preserves its essential dynamical structure. Almost-linear recurrent neural networks (AL-RNNs) are piecewise-linear RNNs in which only a subset of units use ReLU nonlinearities, so that nonlinear capacity is explicitly controlled by the number of ReLU units. Their activation patterns define linear regions, represented as symbols, whose observed transitions form a symbolic transition graph. However, directly training AL-RNNs with few ReLU units to realize minimal dynamical representations can be unreliable. We ask whether an AL-RNN with more ReLU units can instead be trained first and systematically reduced to a minimal dynamical representation. We introduce a fixed-point-guided hierarchical reduction procedure that progressively linearizes selected ReLU units, merging neighboring linear regions and graph nodes while preserving distinct symbols containing fixed points (FPs). The resulting reduction tree defines a hierarchy of progressively simpler candidates. Each reduced candidate is initialized from the parent parameters and retrained under guidance from the parent dynamics. We also prove that reproducing $Q$ distinct fixed points requires at least $Q$ FP-containing symbols, providing a certificate of symbol-level minimality when this bound is attained. On the 3-scroll Chua system, direct training with the theoretical minimum of three ReLU units achieves high-fidelity minimal realizations in only 20% of seeds, whereas our learn-reduce-retrain strategy increases the seed-macro success rate to approximately 71% at the same final nonlinear capacity. These results show that redundant nonlinear capacity can serve as a scaffold for discovering and realizing minimal dynamical representations.

---


### 226. [Learning Commute-Time-Preserving World Models for Planning](https://arxiv.org/abs/2610.01373)

**<font color=#1a73e8>作者：</font>** Michael Hauri, Peter Buttaroni, Fabian A. Mikulasch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models allow agents to plan in latent space by choosing a sequence of actions that most reduces the distance to a given goal state. Thus, planning can benefit from latent representations whose distances mirror commute-times in the environment. The spectral embedding space of the graph Laplacian provides such a representation, if it obeys a specific eigenvalue-dependent scaling. Unfortunately, instantiating the graph Laplacian is intractable in large, continuous environments. Self-supervised learning offers a natural route to such commute-time-preserving embeddings at scale. However, here we show that existing methods, which commonly encourage isotropic representations to prevent representational collapse, tend to degrade the "correct" eigenvalue-dependent scaling, leading to an inaccurate representation of commute times. To address this problem, we introduce Commute-Time-Preserving World Models (CTWMs), combining a latent displacement predictor and a log-determinant regularizer that prevents collapse, which provably recover the correctly scaled Laplacian representation under reversible deterministic dynamics and at the predictor's fixed point. In numerical simulations, CTWM matches or outperforms LeWM, a task-agnostic baseline, on several complex, continuous goal-reaching benchmarks, while using half the parameters.

---


### 227. [Action-On-Item Preference Flow: A Shared Event Schema for Predictive and Generative Personalization](https://arxiv.org/abs/2610.01375)

**<font color=#1a73e8>作者：</font>** Parthiv Chatterjee, Kashish Kanjaria, Vashisth Purani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A user's movie, news, and dialogue histories differ in their native actions and outputs, yet each interaction supplies evidence that can update user memory. We study whether these histories can train one reusable update mechanism. An action-on-item schema pairs a mapped interaction role with a content embedding, allowing shared update parameters to operate on separate user states. We establish invariance to native relabeling, bounded state changes under item-embedding perturbations, and a pooled-training bound under explicit compatibility conditions. The Multi-Timescale State Hypothesis (MTSH) specifies how this evidence enters, persists, and is consumed; PerTIDE implements it with action gating, three state-space traces, fusion, and command-conditioned readout. On PENS, the same history encoder supports both next-news prediction and personalized headline generation. In a controlled PENS-to-MovieLens experiment, a frozen source-trained core exceeds an identically structured random core by 15.23 MRR points after fitting the same target consumer. On MIND, PerTIDE retains a 4.12-point MRR advantage over a same-input three-branch state-space control. Action, readout, and trace interventions identify complementary contributions to these gains. Together, the theory and experiments support learning history updates across compatible sources and reusing them through predictive and generative consumers.

---


### 228. [Minimax Optimal Regret for Causal Logistic Bandits with Counterfactual Fairness](https://arxiv.org/abs/2610.01377)

**<font color=#1a73e8>作者：</font>** Junhyuk Huh, Seoungbin Bae, Dabeen Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study causal logistic bandits with counterfactual fairness constraints. The causal structure is given through known factual and counterfactual feature maps that share an unknown logistic reward parameter, but the learner observes only factual rewards. Consequently, the directions determining counterfactual feasibility need not be identifiable from the available feedback. The closest prior analyses either omit a coverage condition or impose a comparatively strong one, and do not establish matching lower bounds. We first show that some coverage condition is necessary: without a coverage-type restriction, factually indistinguishable environments with different optimal fair actions force $\Omega(T)$ expected joint loss. Under a weaker full-rank condition on the factual covariance pooled across actions, we identify a target-specific information scale $V_\star$ that measures the difficulty of estimating rewards and counterfactual effects from factual feedback. We construct worst-case families satisfying this condition on which every policy incurs expected joint loss $\Omega\left(\left[V_\star\min\{\log K,d\}\right]^{1/3}T^{2/3}\right)$. We also give an explore--then--exploit procedure tuned using $V_\star$ and an adaptive algorithm that does not require its value. Both algorithms achieve $\max\{R_T,V_T\}=\widetilde{O}\left(\left[V_\star\min\{\log K,d\}\right]^{1/3}T^{2/3}+\kappa d/\sigma_0^2\right)$, where $R_T$ is regret relative to the best fair action and $V_T$ denotes the cumulative stage-wise positive violations. Thus the upper and lower bounds match in their leading dependence on $T$, $V_\star$, and $\min\{\log K,d\}$, up to logarithmic factors.

---


### 229. [Generation Provenance Before Behavior Attribution: Auditing Synthetic Speech Research Objects](https://arxiv.org/abs/2610.01378)

**<font color=#1a73e8>作者：</font>** Sidi Chang, Peiying Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Attributing model behavior to synthetic training data requires knowing what produced each training item before estimating what that item caused. A waveform-label pair does not preserve this knowledge. We propose a generation-provenance substrate in which a synthetic research object binds source specification, generated content, waveform, target, fact requirements, quality signals, review lineage, and immutable manifest identity. Producer and selection mechanism determine evidentiary meaning; storage location and variable name do not. We audit this substrate in a private Japanese care-handoff pipeline. A 113-asset review population contains 1.552 hours of synthetic speech across six scenario families; all items have linked audio, transcripts, candidate notes, and fact checklists, but human evidence is selective and source-specific. Two faithful-only manifests are scenario-seed-disjoint and immutably versioned, while exact upstream attribution remains blocked by floating generator aliases, missing per-clip TTS and code stamps, and an unversioned checking prompt. We argue that generation provenance is necessary but not sufficient for behavior attribution: it defines the candidate causal graph and audit units, whereas contributive attribution still requires frozen training runs and intervention or influence evidence. The paper contributes a compact provenance contract, an audit protocol, and a bounded case study for synthetic-data attribution; controlled research access may be offered, but we do not claim causal training-data attribution, clinical validity, or unrestricted public release.

---


### 230. [Robust Evidential Learning Through Latent Consistency](https://arxiv.org/abs/2610.01384)

**<font color=#1a73e8>作者：</font>** Charmaine Barker, Daniel Bethell, Simos Gerasimou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty quantification is essential for deploying deep learning models in high-stakes settings, where out-of-distribution and adversarial inputs can induce confident but unreliable predictions. Evidential Deep Learning provides efficient uncertainty estimates in a single forward pass, but can still assign high evidential strength to inputs that are poorly supported by the learned representation, such as adversarial inputs. We introduce CLEAR, a lightweight, task-agnostic post-hoc method that improves evidential robustness without retraining or altering the base prediction. Using held-out calibration data, CLEAR characterises the group-conditioned geometry of the model's latent space. At inference, it efficiently generates perturbation views directly in the latent space and measures their conflict relative to the calibrated geometry of the predicted group. High latent conflict indicates unsupported evidence, which CLEAR uses to selectively reduce evidential strength while retaining evidence for latent-consistent inputs. On ImageNet$\rightarrow$CUB, CLEAR improves OOD and adversarial AUROC by $+8.29$ and $+5.01$ while running 17.4$\times$ faster than competing post-hoc methods while preserving predictive performance across classification, regression, and object detection benchmarks.

---


### 231. [Is it Possible to Generate Irreversible PolyProtected Templates from Face Embeddings using System-Specific Keys?](https://arxiv.org/abs/2610.01385)

**<font color=#1a73e8>作者：</font>** Vedrana Krivokuća Hahn, Jérémy Maceiras, Sébastien Marcel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This work aims to answer the question of whether it is possible to generate irreversible protected templates when the PolyProtect biometric template protection method is applied to face embeddings using system-specific keys (i.e., the same C and E parameters, which define the transform, are applied to all subjects' face embeddings), instead of the traditional subject-specific keys (i.e., each subject has their own C and E parameters). This is important for determining whether we can perform de-duplication of face identities in the PolyProtected domain, which is not possible in the subject-specific key scenario due to the clash with PolyProtect's unlinkability property (i.e., one could generate multiple protected templates belonging to the same identity, using different C and E parameters, such that those templates cannot be linked to each other). We present experiments (reproducible using our open-source code) to prove that there exist at least three ways of systematically selecting system-specific keys that produce irreversible PolyProtected templates: (i) from pre-selected subject-specific keys, (ii) by applying a previously proposed key selection algorithm to random vectors, and (iii) by approximating a "good" C/E pair distribution from which system-specific keys can be constructed. Our findings thus point to the conclusion that it is, indeed, possible to safely operate PolyProtect in the system-specific key scenario without degrading the template protection potential. This opens up the possibility for identity de-duplication in the PolyProtected domain.

---


### 232. [Evidence Coverage for Intent-Bound Execution: Scope, Obligations, and Cutoff Reasoning](https://arxiv.org/abs/2610.01386)

**<font color=#1a73e8>作者：</font>** Mengting Wu, Lin Wang, Yong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A verifier may authenticate every available record and still lack grounds to call an execution account complete. Such a claim requires a justified account of which records were due for the execution being assessed. We present an analytical model for retrospective coverage of declared execution-evidence obligations. Its scope binds a structured Intent, an exact Candidate, a selected analytical attempt, an execution and evidence boundary, a stage horizon, a fixed record-obligation profile, a named verifier, and an assessment cutoff. Branch and trigger premises determine obligation instances; source competence, content, integrity, and object and stage bindings determine admissibility. We distinguish closure of the obligation inventory from closure of the relevant verifier view, and define three reporting results: COMPLETE_WITHIN_SCOPE, INCOMPLETE, and UNKNOWN. These results concern current coverage of obligations due at the cutoff. Execution progress, external outcome knowledge, and historical delivery timeliness are reported separately. Constructed service-principal-disablement cases demonstrate complete dispatch and refusal branches, a due but missing final-result record, subsequent coverage after late delivery, and the limits of extending one selected attempt's coverage to all attempts. The contribution is an execution-specific composition of scope, branch, horizon, obligations, admissibility, view, and cutoff. Completeness remains conditional on the declared profile and assessment premises.

---


### 233. [Supervising Sound Localization by In-the-wild Egomotion](https://arxiv.org/abs/2610.01388)

**<font color=#1a73e8>作者：</font>** Anna Min, Ziyang Chen, Hang Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a method for learning binaural sound localization using egomotion as a supervisory signal. Over the course of a video, the cameras direction to a sound source will change as the camera moves. We train an audio model to predict sound directions that are consistent with visual estimates of camera motion, which we obtain using traditional methods from multi-view geometry. This provides a weak but plentiful form of supervision that we combine with traditional binaural cues. To evaluate this method, we propose a dataset of real-world audio-visual videos with egomotion. We show that our model can successfully learn from real-world data and that it performs well on sound localization tasks

---


### 234. [Reusing Past Samples in Proximal Policy Optimization: When and How Does It Help?](https://arxiv.org/abs/2610.01399)

**<font color=#1a73e8>作者：</font>** Alessandro Montenegro, Riccardo Venturelli, Marco Mussi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Among on-policy deep reinforcement learning methods, Proximal Policy Optimization (PPO) has become the de facto standard, due to its consistently strong empirical performance across diverse application domains. However, on-policy methods are inherently sample inefficient: fresh data collected under the current policy is used for just a few updates before being discarded. Off-policy methods avoid this inefficiency via experience replay, achieving notable sample efficiency gains, but at the cost of training instabilities or extensive tuning. This motivated the rise of hybrid strategies that augment PPO with off-policy data reuse. Existing sample-reuse variants of PPO demonstrated improved sample efficiency over vanilla PPO, yet a systematic study of when reuse helps, in which scenarios, and to what extent remains missing. In this work, we study the effectiveness of sample reuse in PPO by instantiating two variants within a multiple importance weighting framework. Both retain the core PPO mechanics, reusing only samples from a window of recent iterations, thereby isolating the effect of data reuse from other factors. The variants, termed wPPO-U and wPPO-BH, employ vanilla importance weights or balance-heuristic-corrected ones, respectively. For both, we derive policy improvement lower bounds providing theoretical grounding for their respective losses. We use them to empirically study when and how data reuse improves sample efficiency or final performance of PPO across continuous control tasks.

---


### 235. [Contrastive Attention Mitigates Spectral Bias in Spiking Transformers](https://arxiv.org/abs/2610.01403)

**<font color=#1a73e8>作者：</font>** Xiaoli Liu, Malu Zhang, Yang Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking Transformers merge the energy-efficiency of spiking neural networks (SNNs) with the representational power of self-attention, creating a promising architecture for high-performance, energy-efficient computation. However, a performance gap persists versus its counterparts in artificial neural networks (ANNs). Unlike prior works attributing this to binary activations, we reveal that both spiking neurons and spiking self-attention (SSA) act as low-pass filters through multiscale spectral analysis. This characteristic leads to the dissipation of high-frequency components. To address this issue, we propose the Spiking Contrastive Attention (SCA) paradigm, which draw inspiration from the edge-detection and differential sensing properties of biological visual system. By extracting contrast prototypes via global contrastive aggregation and applying local differential refinement, SCA effectively enhances high-frequency information. Extensive experiments show that SCA is a general module that consistently boosts Spiking Transformers across image classification, semantic segmentation, and event-based tracking. Furthermore, it achieves lower complexity, offering superior efficiency over original SSA. These results establish its potential as a fundamental building block for energy-efficient Spiking Transformers.

---


### 236. [Smoother Flow Matching via Contrastive Trajectory Repulsion](https://arxiv.org/abs/2610.01408)

**<font color=#1a73e8>作者：</font>** Ziqi Jiang, Zhenqi He, Long Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Trajectory crossing remains a critical bottleneck in Flow Matching (FM), and previous works typically view these crossings from a theoretical optimization perspective causing velocity averaging. They attempt to address it indirectly by post-hoc distillation or endpoint coupling, without explicitly regulating the intermediate trajectories. In this paper, we introduce a new network learning perspective: crossing points inherently induce large local Lipschitz constants in the target velocity field, leading to two drawbacks. First, high Lipschitz constants correspond to high-frequency signals in the velocity field that neural networks struggle to fit due to spectral bias. Second, they also imply drastic velocity variations, leading to severe numerical integration errors in few-step inference. To alleviate this, we propose CoFlow, a framework that introduces the contrastive learning paradigm into FM to explicitly repel trajectories during training, thereby lowering the local Lipschitz constants of the velocity field. Specifically, we formulate CoFlow from a Stochastic Differential Equation (SDE) perspective by injecting a repulsive drift term. This drift actively guides the forward process of positive samples away from negative trajectories, effectively reducing the local Lipschitz constant. Furthermore, we derive an equivalent stochastic interpolant formulation from this SDE, providing a simple and tractable design space to control the influence of negative samples. Extensive experiments on ImageNet 256x256 demonstrate that CoFlow significantly reduces FID compared to standard FM in few-step inference (e.g., 20 steps), with no added training overhead. The code can be accessed at: this https URL

---


### 237. [Localisation-Aware Uncertainty for Pretrained Object Detection](https://arxiv.org/abs/2610.01409)

**<font color=#1a73e8>作者：</font>** Charmaine Barker, Daniel Bethell, Simos Gerasimou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty estimation is essential for deploying object detectors when distribution/covariate shift and adversarial attacks may occur. Existing approaches often require detector retraining, architectural modification, or repeated inference, which may be infeasible or incur significant overheads. We introduce a lightweight post-hoc evidential meta-model that learns when object localisations should be considered uncertain while keeping the base detector frozen. Our approach automatically identifies localisation-relevant features and uses saliency-guided modification to construct an increasingly challenging curriculum. Detection-level targets combine localisation error, modification level, and prediction instability to guide an evidential meta-model to estimate uncertainty for each predicted bounding box. Our approach requires no changes to the detector and preserves its original localisation outputs. Across adversarial attacks and evaluated strengths, GRACE improves TP-FP AUROC by 22% relative to the strongest comparator in some cases while maintaining in-distribution detection performance.

---


### 238. [Least-time Gradient Flow](https://arxiv.org/abs/2610.01426)

**<font color=#1a73e8>作者：</font>** Alessandro Betti, Marco Gori, Stefano Melacci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prescribing the speed of gradient flow on the risk itself, by the dynamics $\dot w=-u(E(w))\nabla E(w)/\abs{\nabla E(w)}^{2}$, makes the risk $e(t)=E(w(t))$ obey $\dot e=-u(e)$ exactly, whatever the landscape~$E$; the time needed to reach zero risk from $e_0$ is $\int_0^{e_0}\dd e/u(e)$. Minimizing this time alone is ill posed, and we study the regularized problem $\inf\{\int_0^{e_0}(\tfrac\lambda2\abs{u'}^{2}+1/u)\,\dd e:\ u\in H^{1}(0,e_0),\ u\ge0,\ u(0)=0\}$, $\lambda>0$. We prove that the minimizer exists, is unique, and is a linearly scaled cycloid, and we show that the optimal rate behaves like $u^{*}(e)\sim(9/(2\lambda))^{1/3}e^{2/3}$ near zero risk: the exponent $2/3$ is the one found in \cite{betti2026holder} by a power-law ansatz, and it lies in the Hölder window $(\tfrac12,1)$ where the arrival is in finite time with vanishing weight speed. The proof follows the classical route: existence by the direct method, uniqueness by strict convexity, positivity of the minimizer away from the origin, and the explicit integration of the Euler-Lagrange equation.

---


### 239. [SHAMS: An Audio-Grounded Pronunciation Benchmark for Levantine Arabic](https://arxiv.org/abs/2610.01427)

**<font color=#1a73e8>作者：</font>** Ben Sapirstein, Roy Mattar, Guy Mor-Lan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Levantine Arabic (LA) is spoken by tens of millions of people, creating a pressing need for shared benchmarks to evaluate LA speech-language technologies. Evaluating such technology is particularly challenging given LA's internal diversity and its opaque and non-standardized orthography. We present SHAMS (SHami Annotated Multi-dialect Speech), a benchmark comprising 1,300 utterances drawn from open audio corpora, balanced across five LA varieties (Urban and Rural Palestinian, and Urban Jordanian, Lebanese, and Syrian). Each utterance is represented across four aligned tiers: audio, unvocalized orthography, diacritized text, and phonetic transcription. This structure supports evaluation of various downstream tasks such as diacritization, grapheme-to-phoneme conversion, automatic speech recognition, and audio-to-phoneme, grounded in audio and stratified by variety. We benchmark open and proprietary models across these tasks to demonstrate the utility of this benchmark for measuring progress across LA. We release SHAMS at this https URL .

---


### 240. [A Deterministic and Auditable AI Security Risk Assessment Framework with ATLAS Aligned Executable Rules and Formal Verification](https://arxiv.org/abs/2610.01436)

**<font color=#1a73e8>作者：</font>** Yixuan Huang, Basel Halak, Boojoong Kang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence systems are increasingly deployed in high impact and safety critical settings, yet security assessment remains difficult to reproduce and defend under audit. Existing approaches often rely on narrative checklists or assessor driven scoring, and they lack an explicit, machine evaluable mapping from observable engineering artefacts to stable technique level outcomes. We present an evidence driven AI security assessment framework that operationalises assessment as a deterministic decision function. The framework normalises heterogeneous artefacts into a project independent Control ID taxonomy scored on a bounded four level ordinal scale, compiles technique level predicates from a pinned MITRE ATLAS snapshot via an explicit mitigation to control mapping, and outputs technique indexed feasibility and impact levels with traceable links back to the triggering evidence. We package all normative choices as a versioned assessment policy object to support repeatable reassessment across snapshots. To ensure semantic correctness, we formally verify boundedness, totality, ordered semantic consistency, and monotonicity of the compiled evaluator over the full declared score domain. We evaluate the framework on five public open source AI projects pinned to explicit repository snapshots, quantify before and after changes under a unified hardening intervention, and validate responsiveness to real engineering changes through fork based implementations of Software Bill of Materials (SBOM) generation and Continuous integration (CI) security scanning gates. Results show consistent downward shifts in feasibility profiles under strengthened observable controls, while worst case residual feasibility persists when technique specific core controls remain absent from the evidence scope.

---


### 241. [The Impact of Processing Parameters on High-Accuracy Measurements in UAV Photogrammetry](https://arxiv.org/abs/2610.01438)

**<font color=#1a73e8>作者：</font>** Paweł Ćwiąkała, Edyta Puniach, Elżbieta Pastucha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV) photogrammetry is increasingly used in applications requiring high accuracy, such as determining ground surface changes caused by landslides, mining, or microrelief transformation. While acquisition strategies have been widely studied, the influence of the processing workflow-particularly Bundle Block Adjustment parameter settings-remains insufficiently explored. This study addresses this gap through a systematic, full-factorial evaluation of 768 processing variants applied to ten UAV datasets collected over 1.5 years in a 220 ha study area. Eight key parameters were analysed. The results show substantial variability in final 3D accuracy: the best performing variant achieved a root mean square error (RMSE) of 16 mm, whereas the weakest reached 303 mm. The most influential factors were the number of ground control points, the application of additional camera calibration corrections, and the use of the Post-Processing Kinematic GNSS method for determining camera projection center coordinates. The study also evaluates how workflow optimization affects the accuracy of displacement, tilt changes, and horizontal strain determination. While random displacement errors remained stable (RMSE of ~6-7 mm), systematic errors were significantly reduced by over half in all axes, with vertical median absolute error decreasing from 14 mm to 7 mm in the optimized configuration compared to the baseline previously used by the authors. This study provides the first large-scale, practice-oriented assessment of how processing parameter selection shapes the accuracy of both photogrammetric products and deformation indices determination. The results offer actionable guidance for developing more robust and repeatable UAV photogrammetry workflows tailored to high-precision monitoring.

---


### 242. [ibUMAP: Coherent and Scalable Field Evaluation for UMAP Optimization](https://arxiv.org/abs/2610.01445)

**<font color=#1a73e8>作者：</font>** Bin Chen, Yumeng Xue, Patrick Paetzold 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> UMAP achieves scalable layout optimization through stochastic negative sampling. However, this stochasticity can lead to unstable embeddings across reruns and downstream reuse, as the estimated repulsive forces depend on the ordering of sampling events. We present ibUMAP, a coherent field-based alternative that evaluates attraction and repulsion from a shared embedding snapshot and applies them synchronously. Its degree-weighted repulsive field is motivated by the conditional expectation of negative sampling for a fixed embedding and represented by three scalar moments, which are evaluated efficiently on CPUs and GPUs using an interpolation-based FFT scheme. This formulation avoids explicit all-pairs computations while inducing optimization dynamics that differ from those of standard online UMAP. Controlled experiments show that synchrony and kernel capping alter the local-global fidelity trade-off, whereas FFT evaluation produces small average changes in final quality. End-to-end benchmarks show median speedups of 3.29x unseeded and 5.79x seeded over umap-learn on CPU, and 1.44x over cuML on million-scale datasets under unseeded GPU execution. These gains accompany greater run-to-run stability and measurable fidelity trade-offs.

---


### 243. [Uncertainty-Guided Handshake: Efficient Human-in-the-Loop Refinement for Surgical-Grade Glioma Segmentation](https://arxiv.org/abs/2610.01452)

**<font color=#1a73e8>作者：</font>** Samuel Hart, Ahmad Yahya, Ahmed Karam Eldaly  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While state-of-the-art automated models for medical image segmentation achieve high mean performance, they frequently suffer from localized, catastrophic failures that preclude safe clinical deployment, particularly in neuro-oncology. Interactive segmentation frameworks mitigate this by incorporating human oversight, but traditionally impose prohibitive cognitive and temporal workloads by requiring clinicians to manually search for errors. In this project, we present an efficient, Hybrid Structural-Aleatoric Human-in-the-Loop framework for glioma segmentation that bridges the gap between automated baseline performance and surgical-grade precision, achieving sub-2.0 mm HD95 on curated benchmarks while providing safety-net routing for structural failures across real-world clinical data. By extracting voxel-wise Test-Time Augmentation (TTA) uncertainty and applying hierarchical topological filtering, our method proactively isolates high-risk structural anomalies. We comprehensively evaluated our approach on a challenging out-of-distribution clinical stress-test cohort (N = 362). Operating under a simulated Human Oracle, the framework improved the Whole Tumor (WT) Dice score from 0.891 to 0.914 and reduced the 95th percentile Hausdorff Distance (HD95) from 5.82 mm to 4.76 mm. Critically for surgical safety, the system rescued severe boundary failures in the Tumor Core, reducing mean HD95 from 17.96 mm to 14.83 mm (improving absolute TC Dice to 0.356). These spatial rescues were achieved while demanding a median interactive workload of just 11.3% of the target volume. Acknowledging this as a simulated upper bound lacking real-world cognitive friction, the framework nevertheless demonstrates a highly Pareto-efficient pathway for safely deploying clinical AI.

---


### 244. [Repurposing Obsolete Representations for Post-Deployment Adaptation](https://arxiv.org/abs/2610.01453)

**<font color=#1a73e8>作者：</font>** Daniel Bethell, Charmaine Barker, Simos Gerasimou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks are increasingly deployed in long-lived systems, where task requirements may change after training. In such settings, part of the original output space may become obsolete: a class, prediction region, or learned behaviour may no longer be valid. Existing approaches either leave the obsolete behaviour intact or require fine-tuning, which can be expensive. We propose Deep Repurposing (DR), a post-hoc framework for adapting models under task obsolescence. DR estimates the latent geometry of obsolete and retained regions, removes obsolete-supporting components, and reallocates retained-compatible evidence through an analytic repair map without gradient updates. This yields repaired predictions and representations in which obsolete regions no longer act as valid outputs, while useful obsolete structure can support the retained task. Across multiple task settings, DR removes obsolete behaviour while preserving retained utility. More importantly, across classification benchmarks, DR matches or exceeds competing unlearning and editing baselines in retained accuracy, eliminates obsolete predictions, and adapts up to $60\times$ faster than competing unlearning methods.

---


### 245. [Streaming algorithms for robust max-min diversification](https://arxiv.org/abs/2610.01456)

**<font color=#1a73e8>作者：</font>** Andrea Pietracaprina, Geppino Pucci, Stefano Zanon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given a set of $n$ points $X$ in a metric space and an integer $k$, max-min diversification aims to select $k$ points of $X$ maximizing their minimum pairwise distance. This objective function is however highly vulnerable to noisy points. In[Amagata, AAAI23], a robust formulation is proposed which addresses this vulnerability by excluding solutions containing any of $z$ outliers, defined as the $z$ points in $X$ with the largest nearest-neighbor distances. That paper also presents a coreset-based streaming algorithm for the new formulation, based on a suitable inlier-outlier separation assumption. However, we identify three shortcomings in the algorithm by [Amagata, AAAI23]: its coreset construction requires an offline computation over $X$, which needs memory linear in $n$, in stark contrast with the typical goals of stream processing; the one-pass procedure used to extract the solution from the coreset may return fewer than $k$ points (hence, an unfeasible solution) because it permanently discards points too far from the current solution; and its outlier-exclusion guarantee is only probabilistic and weakens as the coreset size shrinks. In contrast, we present a deterministic coreset-based algorithm that, under a natural inlier-outlier separation assumption (similar to the one used in [Amagata, AAAI23]), returns exactly $k$ inliers which are a $(2+\varepsilon)$-approximate solution, for any $\varepsilon>0$, thus only $\varepsilon$ above the best polynomial-time sequential approximation, even without outliers. Its one-pass streaming implementation adapts obliviously to the dataset's doubling dimension $D$ and, for wide ranges of $k$, $z$, $\varepsilon$, and $D$, it uses memory independent of $n$. For sufficiently long streams, its amortized update time is proportional to the coreset size, thus also independent of $n$.

---


### 246. [Tight Transition Time Bounds for Separable Logistic Regression at the Edge of Stability](https://arxiv.org/abs/2610.01459)

**<font color=#1a73e8>作者：</font>** Haodong Wen, Kaiyue Wen, Jiaye Teng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study logistic regression on linearly separable data under gradient descent with a large constant stepsize $\eta$. Such dynamics may exhibit a characteristic Edge of Stability phenomenon, in which the loss initially oscillates before transitioning to a stable phase of monotone decrease. Existing work provides a tight $\Theta(1)$ bound in dimension $d=2$ as $\eta \to \infty$ and conjectures a bound independent of $\eta$ in arbitrary dimensions $d\geq 2$. In this paper, we disprove this conjecture by showing that, for every fixed sample size $n\geq 2$ and sufficiently small margin $\gamma$, the worst-case transition time is $$\Theta\!\left((\log\eta)^{\min\{n-2,d-2\}}\right)$$ uniformly over $d\geq2$. The key challenge in establishing a tight bound is that the sample contributing most strongly to the gradient can change repeatedly across iterations. To address this issue, we control such changes by induction on dimension and sample size, and construct matching hard instances.

---


### 247. [NextMe-800: Anticipating Personal Behavior from Months of Egocentric Video](https://arxiv.org/abs/2610.01461)

**<font color=#1a73e8>作者：</font>** Zhaoxu Meng, Yiming Sun, Mingyuan Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We often plan ambitiously yet act habitually and wonder, in retrospect, whether we would have planned differently had we known what we would actually do. Hindsight offers a valuable perspective on past decisions, although we often wish we could have simulated hindsight at the moment of choosing. If a system could generate plausible trajectories from one's personal history, such previews might help people formulate more realistic plans and make better informed decisions. We introduce NextMe-800, an approximately 800-hour first-person dataset from one volunteer over 126 days with 1 Hz images, gaze, and audio, captioned at five hierarchical abstraction levels from atomic actions to major activities. We formulate personalized action anticipation as open-vocabulary K-step sequence prediction and construct NextAct, a 1,500-point benchmark combining NextMe-800 with the multi-person EgoLife dataset. Using an embedding-based soft edit distance as the metric, we evaluate how well different models can anticipate personal behavior across abstraction levels and prediction horizons. NextMe-800 and NextAct provide a months-long resource and evaluation framework for studying how far ahead personal behavior can be anticipated from egocentric observation.

---


### 248. [FiVOS: A Fish Segmentation Algorithm Based on Interactive Video Object Segmentation and Filter Enhancement](https://arxiv.org/abs/2610.01480)

**<font color=#1a73e8>作者：</font>** Yuqing Duan, Song Zhang, Shili Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the continuous expansion of aquaculture, precise and efficient monitoring of fish behavior has become increasingly critical for improving farming efficiency and reducing economic losses. In particular, with the ongoing enhancement of computational capabilities in deep learning models, vision-based fish segmentation methods are garnering growing attention. By analyzing video segmentation results, fish behavior can be effectively tracked, thereby providing reliable data support for the precise regulation of aquaculture environments. However, existing deep learning-based video segmentation methods for aquaculture scenarios often overlook the dynamic correlations between video frames. In contrast, Interactive Video Object Segmentation (IVOS) employs an interaction-propagation scheme to achieve high-precision segmentation while minimizing user effort, thereby enhancing monitoring efficiency. Yet, IVOS applications in aquaculture remain limited due to data scarcity, and are susceptible to error accumulation and mask loss over long sequence propagation due to high intra-class similarity. In response, this paper proposes an improved interactive video object segmentation method (FiVOS) and constructs two fish-specific datasets. FiVOS utilizes a mask block filter to enable early detection and correction of erroneous propagated mask blocks, enhancing filtering accuracy through a rule-based thresholding approach. Additionally, it serializes noise filters to further eliminate erroneous mask noise, thereby improving model robustness. Experimental results demonstrate that FiVOS achieves state-of-the-art (SOTA) performance in fish video segmentation tasks, providing robust technical support for fish behavior research.

---


### 249. [Key-Reuse Vulnerability of Phase-Keyed Fourier-Curve Modulation: Relation Leakage and Key-Refresh Cost on Coded Links](https://arxiv.org/abs/2610.01484)

**<font color=#1a73e8>作者：</font>** Bin Han, Muxia Sun, H. Vincent Poor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The security of keyed modulation is often argued from the key-space size and the error rate of a key-less receiver. This evidence fails when the key is reused and the waveform is harmonically coupled. For a phase-keyed Fourier-curve constellation, whose $k$ tones share one data parameter, integer relations among the harmonic indices yield data-cancelling mixed moments of the received tones that expose key characters. A modular relation lattice characterizes the exposed characters; for consecutive harmonics, third-order moments recover the relative phases and a fourth-order moment completes the key up to cyclic relabeling whenever its coefficient is nonzero, as in all evaluated settings. A non-data-aided relation-moment estimator turns this leakage into an attack that never enumerates the key space. On a regular $(3,6)$ LDPC-coded link, one key per 168-symbol codeword leaves the eavesdropper a block error rate below $0.04$ at the middle noise level, and the attack meets a predeclared $0.1$ compromise criterion in eleven of twelve operating points. Tangent artificial noise and a harmonic set without relations below order four raise her measured error rate at intermediate reuse lengths but do not remove the one-codeword vulnerability. For a grid of $2^{128}$ protocol keys at the middle noise level, equal-length refresh schedules that keep a $95\%$ lower confidence bound of her block error rate above $0.9$ consume at least $1.52$ fresh key bits per information bit, $1.52$ times the entropy rate of a one-time pad on the data.

---


### 250. [Let the Heads Talk: Beyond Diagonal Graph Attention](https://arxiv.org/abs/2610.01494)

**<font color=#1a73e8>作者：</font>** Riccardo Ali, Alessio Borgi, Mario Severino 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sheaf Neural Networks generalize scalar-weighted message passing by replacing scalar edge weights with linear transport maps between local feature spaces. Yet the role of this matrix-valued transport is entangled with the broader sheaf-diffusion construction. We isolate the transport primitive through quiver representations and establish a direct connection with multi-head attention. Treating attention heads as coordinates of a local transport space reveals that standard multi-head attention implements diagonal edge maps: along each directed interaction, a source head can contribute only to the corresponding receiver head. Allowing off-diagonal entries instead enables edge-conditioned communication across heads before neighborhood aggregation. We show that this operation cannot, in general, be absorbed into a single shared linear map applied after aggregation. Building on this characterization, we introduce Topological Attention (Top-A), a multi-head attention that learns edge-dependent off-diagonal routes while preserving the original same-head paths and exactly recovering vanilla attention when the additional routing vanishes. We evaluate Top-A on relational reasoning, heterogeneous graph learning, and algorithmic reasoning, including out-of-distribution generalization, with heterophilic node classification as a contrast setting. The results show that cross-head transport is most useful when the task benefits from interaction-dependent transformations, while heterophily alone provides no systematic advantage. These findings identify edge-conditioned cross-head communication as a distinct computational primitive of matrix-valued transport.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-385](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
