# 📦 其他研究 | 2026年11月02日

> 本类共 **432** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-432](./part-09.md)

---

### 1. [The FlightFinder Occurrence Corpus: harmonising 128 aviation-safety source codes into one deduplicated cross-national accident dataset](https://arxiv.org/abs/2610.37671)

**<font color=#1a73e8>作者：</font>** Denys Kolomiiets  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> National aviation-investigation databases are deep but territorial; global compilations such as the Aviation Safety Network and the Bureau of Aircraft Accidents Archives are hand-curated, apply their own inclusion thresholds, and publish no per-record lineage. The FlightFinder Occurrence Corpus harmonizes 279,485 occurrences and 131,882 attached narratives from 128 source codes -- national accident-investigation authorities, occurrence-reporting systems and four global compilations. Records are mapped into one schema; each normalized record reduces to exactly one key from an ordered ladder -- event signature, registration and date, rounded position and date, or source and native identifier -- so a missing field never creates a link, and the key is the occurrence identifier. Records the ladder cannot reach are scored in a blocked pass into an explicit merge table and applied only within an automatically approved score band or after a person confirms them. Field conflicts follow a documented source ranking; one provenance row per contributing source -- its native identifier and URL -- is retained, with attribution and licence terms per source code. Linkage error is measured on five adjudicated samples totalling 200 pairs. A recorded uniform random draw of 60 from the 3,441 merges the automatic band applies as it ships found no error; the exact two-sided 95% Clopper-Pearson upper bound on its false-merge rate is 6.0%, or 205 pairs. The measured error covers the scored band only; the ladder's deterministic joins are not adjudicated. The corpus has no exposure denominators and inherits the under-reporting of its sources. It is offered as a base for cross-national safety statistics, source-disagreement studies and narrative text mining; a frozen, DOI-referenced snapshot accompanies the live API.

---


### 2. [The Best Second Opinion Is Right Where the Primary Is Wrong: Partner Selection for Selective Span Tagging](https://arxiv.org/abs/2610.37678)

**<font color=#1a73e8>作者：</font>** Varun Kotte  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A span tagger that ranks its outputs by risk can defer the riskiest ones to a person, and a second model can sharpen this ranking. Which second model should it be? Partner selection is conditional, not global: the best second opinion is the model that is right where the primary is wrong. Across eight tagger types, three seeds and three English benchmarks (576 evaluated primary-partner pairings), choosing the partner by held-out accuracy on the primary's errors recovers 82% of the best partner's gain, against 69-70% for span F1 or a random pick. Frozen before a fourth dataset was chosen, the rule replicated there (Spearman 0.40 vs. 0.04 for span F1). Partner value is also directional. The predictive distribution is the second opinion: hard labels discard half of a partner's value, and scoring the served label improves 94% of pairings. Fixed before the fourth dataset was chosen, this score also replicated there. For LoRA-tuned decoders, independently trained partners beat every readout of the primary network. Applied zero-shot to 51 MASSIVE locales, every primary has a helpful trained partner in every locale, and the preferred partner follows competence.

---


### 3. [Where Planning Changes the Outcome of Orbital Games](https://arxiv.org/abs/2610.37686)

**<font color=#1a73e8>作者：</font>** Duncan Eddy, Mahdi Al-Husseini, Mykel J. Kochenderfer  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper introduces OrbitalGym, a simulation environment for studying when planning algorithms or system design determine the outcome of adversarial orbital encounters. In an orbital game, two non-cooperative teams of satellites maneuver during rendezvous and proximity operations to win a differential-reward objective. Advances in terrestrial game playing have prompted many methods for orbital games, but studies typically evaluate one method in one scenario, often against a passive or random defender. It is unclear whether better planning matters once vehicle capability (maneuverability, sensing, communications) and adversarial responses are considered.
OrbitalGym is a JAX-based environment supporting varying numbers of agents, state representations (position, velocity, attitude, fuel), explicit or implicit communication, and proximity or conical field-of-view sensors. It compiles games to batched GPU code, enabling large-scale parallel simulation of policies across many configurations. This identifies regimes where policy choice affects outcomes and regimes where system capability dominates.
We study two close-range games: pursuit-evasion, where one spacecraft tries to capture another, and lady-bandit-guard, where a guard prevents an attacker from reaching a protected asset. We compare PD, LQR, model predictive path integral control, and Monte Carlo tree search over ratios of thrust and propellant, initial separation, game duration, sensor capability, and the definition of capture. In pursuit-evasion the propellant ratio decides most encounters: against five of six evader policies, pursuer policy changes capture probability by 10 percent or more in at most 15 of 90 capability configurations. In lady-bandit-guard, policy matters more: against bandits able to reach the asset, a better guard policy raises defense probability by at least 10 percent in 56 to 74 of 90 configurations.

---


### 4. [One Confidence Threshold, Unequal Coverage: Language Gaps in Typed Decision Interfaces and How Translating Inputs Reduces Them](https://arxiv.org/abs/2610.37688)

**<font color=#1a73e8>作者：</font>** Junwei Yao, Yongxi Zhou, Zike Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deployed classifiers often act on a prediction only when its confidence clears a threshold and pass the rest to a person. We ask whether one threshold serves all languages equally on typed decision interfaces, APIs that return a probability for each option of a fixed multiple-choice question. In a confirmatory study with a written analysis plan, three vendors' interfaces classified 1,000 MASSIVE items, each in 51 languages, with a threshold of 0.9. Even when a request is answered correctly in both English and another language, the English version clears the threshold more often, by 8.6-11.7 percentage points on average. Observed coverage, the share of requests handled automatically, is lower than English's in every other language, while the requests the gate handles are rarely wrong. The gap remains when every language is reweighted to the same accuracy, and a standard calibration metric (ECE) does not detect it on one interface. In exploratory analyses, English's coverage stays higher when each language gets its own threshold fitted to the same 5% error target. Translating inputs into English nearly closes the gap at 0.9 but leaves English ahead at that error target. Requests written natively in African languages show a gap in the same direction when English is their human translation. We recommend reporting per-language coverage at the operating threshold.

---


### 5. [Balancing Mobility Efficiency and Environmental Exposure During Mega Events: A Multi-agent Routing Framework](https://arxiv.org/abs/2610.37702)

**<font color=#1a73e8>作者：</font>** Xinyue Liu, Qiumeng Li, Suhong Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Mega events can generate concentrated travel demand, intensifying congestion around venues and increasing travelers' environmental exposure. Existing traffic management strategies focus on travel efficiency, with limited attention to exposure risks. Taking mega-event travel as a short-term high-demand scenario, this study develops an exposure-aware multi-agent routing framework integrating road-network conditions, event-induced demand, background traffic, and environmental data within a unified simulation environment. Motorized travelers optimize travel efficiency, whereas micro-mobility travelers consider travel time and dynamic exposure to traffic-related PM2.5 and noise. We compare the framework with shortest-distance, congestion-aware, and exposure-aware routing baselines. Results show that, under high demand, the SARSA-based framework reduces vehicle travel time by 34.59% and cumulative environmental exposure by 58.65%, while micro-mobility travel time remains nearly unchanged. Exposure reduction is jointly driven by vehicle-side congestion mitigation and low-exposure routing. The framework provides quantitative support for vehicle diversion, low-exposure route guidance, and health-oriented traffic management in short-term high-demand scenarios.

---


### 6. [Moment-Guided Optimizers for Noisy Deep Learning: MGO-SC as a Simple Consistency Gate for Adam-Style Updates](https://arxiv.org/abs/2610.37712)

**<font color=#1a73e8>作者：</font>** Alicem Koyun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive optimizers are widely used in deep learning, yet their behavior can degrade under heavy stochasticity and label noise where the sign and magnitude of gradients can be unstable. We study MGO-SC (Moment-Guided Optimizer with Sign-Consistency), a lightweight modification of Adam-style methods that derives a coordinate-wise consistency gate from the magnitude of a sign exponential moving average (EMA): coordinates whose gradient sign is stable are trusted, while coordinates whose sign fluctuates are down-weighted. We show that the naive form of this gate, which can only shrink updates, loses effective step size and underperforms when the learning rate is matched to the baseline. We therefore introduce a mean-preserving variant that reallocates trust across coordinates without changing the net per-tensor step magnitude. On CIFAR-10 with ResNet-18, under a matched learning rate and decoupled weight decay, mean-preserving MGO-SC consistently improves over its AdamW baseline across clean, symmetric, and asymmetric label noise (e.g., +1.4 points at 40% symmetric noise; paired bootstrap 95% CI excluding zero; Wilcoxon p<0.01), while adding no second-order information or per-sample filtering. We report matched-seed effect sizes, nonparametric bootstrap confidence intervals, and paired significance tests, and we release code and raw logs.

---


### 7. [FVH-Bench: Evaluating Image Generator Safety Beyond Overtly Harmful Imagery](https://arxiv.org/abs/2610.37722)

**<font color=#1a73e8>作者：</font>** Zihao Zhu, Yuhan Liu, Siwei Lyu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern image generators can produce complex visual artifacts, including diagrams, interfaces, and records that combine text, graphics, and layout to convey detailed information. They may refuse requests for overtly harmful imagery yet still generate artifacts that guide dangerous actions or support deception. We call the risk arising from what such images enable, rather than only what they depict, functional visual harm (FVH). Existing safety benchmarks focus largely on overtly harmful content, such as pornography and graphic violence, leaving image generators' safety alignment against FVH insufficiently evaluated. To address this gap, we introduce FVH-Bench, comprising 669 prompts across five harmful visual functions and ten risk domains. The 11 evaluated image generators rarely refuse these requests and frequently generate artifacts that fulfill the targeted harmful functions. High scores for target harm realization and harmful artifact usability further indicate that these outputs can support the intended harmful purposes. A further analysis finds that existing safety detectors also provide limited coverage of FVH, indicating gaps in their ability to recognize harmful visual functions. Together, these findings show that evaluating image-generator safety alignment requires considering not only what images depict, but also what they may enable.

---


### 8. [Threshold Compatibility and Support-Selection Diagnostics in Neural Discovery of Partial Differential Equations](https://arxiv.org/abs/2610.37726)

**<font color=#1a73e8>作者：</font>** Zeen Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate regression need not yield the correct equation after support selection. For a median/sample-standard-deviation threshold in neural PDE discovery, we derive an exact two-signal retention boundary and a complete-vector perturbation bound. Exact advection-diffusion libraries lose diffusion despite coefficient recovery to numerical precision. True-support refits of forty saved sparse states reduce diffusion error without restoring all derivative accuracy. A fixed sequential threshold ridge comparator recovers exact support in sixty ideal controls but selects extra terms in every learned state. All-fold correct-support candidates are rejected by conditional validation; post hoc energy pooling preserves their higher minimum loss in all sixty states. Supplied-support estimates outperform unchanged selected equations in all 240 physical-residual comparisons on four unused analytic trajectories. With coefficients, observation points and weights fixed, exact replacement of the learned library and target reverses their learned-row ordering in 59/60 states. Weighting both losses also fails the specified Burgers diffusion-benefit criterion at every tested budget. These finite diagnostics distinguish threshold incompatibility, refit damage and score rejection; they establish neither automatic correction nor general recovery or predictive stability.

---


### 9. [Predicate Neuron: Differentiable Quantization of Predicate Relations in Gradient-based Learning](https://arxiv.org/abs/2610.37727)

**<font color=#1a73e8>作者：</font>** Ioannis Konstantoulas, Iliana Loi, Kyriakos Sgarbas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In machine learning, symbolic reasoning approaches often rely on static architectures that hinder integration into deep neural networks and gradient-based optimization. To address this, we introduce the Native Predicate Neuron, a differentiable logic-reasoning neural module that enriches standard architectures with symbolic reasoning capabilities via first-order logic quantization. The proposed neuron models relational logic by learning to alternate between operations using a single trainable parameter. It features a tailored gradient mechanism with a dual-nature formulation: executing hard logical operations during training while maintaining differentiability for backpropagation. By quantizing both its input and choice state, the Predicate Neuron approximates continuous and non-continuous functions, effectively resolving discontinuities that standard deep learning architectures struggle with. We evaluate the Predicate Neuron across Fully-Connected, Convolutional, Recurrent, and Transformer architectures on benchmarks like MNIST and Wikitext. Results show that incorporating Predicate Neurons accelerates convergence, boosts accuracy, and lowers loss in general, with particularly strong improvements in tasks requiring monotonic reasoning or handling discontinuities. Overall, the Predicate Neuron natively integrates into standard neural networks to enable fuzzy logic operations and is available in Keras and PyTorch.

---


### 10. [Amortized Localized Posterior Inference for Model Calibration with Application to an Ocean Turbulence Closure](https://arxiv.org/abs/2610.37731)

**<font color=#1a73e8>作者：</font>** Exaucé Luweh Adjim Ngarti, Élise Arnaud, Léo Nicoletti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model discrepancy may prevent a single calibration parameter from reproducing a physical response across the context domain. In addition, uncertainties in observations and contexts affect calibration and must be accounted for and quantified. We construct a family of localized posteriors by weighting observation likelihoods according to their proximity to a target context. Gaussian localization weights incorporate context uncertainty through covariance inflation, with reflection at domain boundaries and an optional correction for uneven context sampling. A conditional normalizing flow approximates the family of posteriors through amortized variational inference. Integrating the localized posteriors under a prescribed context measure gives the marginalized parameter distribution. In a twin experiment with the Branin-Hoo model, we compare global and localized inference under uniform and skewed context distributions. Localization reduces the reported aggregate predictive errors relative to the global posterior. An application to the k-$\epsilon$ turbulence closure in a single-column ocean model, with atmospheric surface forcing as context, shows that localized posterior calibration reduces temperature and zonal-velocity errors relative to deterministic and global-posterior calibration. Both twin experiments are constructed to admit local compensation.

---


### 11. [Selective Transfer Learning for Groundwater Level Anomaly Forecasting: Accuracy-Risk Trade-offs](https://arxiv.org/abs/2610.37733)

**<font color=#1a73e8>作者：</font>** Yaxuan Wu, Ali Mohammed Mansoor Alsahag, Seyed Sahand Mohammadi Ziabari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work studies context-aware selective transfer learning for multi-well groundwater anomaly forecasting in the Netherlands. Source-domain pretraining can raise average accuracy but is not uniformly reliable: it degrades performance on a substantial fraction of heterogeneous wells. Context-Aware Selective Learning (CASL) uses calibration-trained, constrained contextual blending of frozen no-transfer and fixed-transfer parents. Global Convex Blend uses the same parents with one calibration-fitted weight per seed. The corrected task requires nine consecutive observed monthly inputs and an exact three-calendar-month target, without interpolation. Evaluation covers 457 wells and 13,718 test windows under five predefined seeds, with the four-cell maxsim0.60 source pool frozen using Always-TL validation RMSE alone. Fixed transfer harms 18.38-51.86% of wells. CASL has 0.424-1.084% lower RMSE than No TL, partially rescuing 97.53-99.50% and fully rescuing 23.46-43.78% of fixed-harmed wells. Partial rescue can arise structurally from convex blending and does not establish contextual superiority. Global Convex Blend protects more wells in four seeds, while CASL has slightly lower pooled RMSE in four. Neither dominates: the results support an accuracy-risk trade-off on the fixed split, not rolling deployment validity.

---


### 12. [Anisotropic Trust Region Warping for Prior-Data Fitted Networks in Bayesian Optimisation](https://arxiv.org/abs/2610.37737)

**<font color=#1a73e8>作者：</font>** Samuel Younger, Tinkle Chugh, George De Ath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior-Data Fitted Networks (PFNs) replace the hyperparameter refitting of Gaussian Process (GP) surrogates in Bayesian optimisation with a single forward pass, at the cost of a prior that is fixed at meta-training time. We show empirically that a PFN's predictive log-likelihood falls increasingly behind that of a refitted GP as the objective function's lengthscale grows beyond the mode of the PFN's meta-training prior, and that this deficit carries over to optimisation performance. To correct the mismatch without retraining the network, we introduce Anisotropic Trust Region (ATR) warping. Per-dimension lengthscales are estimated by kernel target alignment, and an affine rescaling of the input space maps the objective onto the lengthscale the PFN expects, with a trust region around the anchor determining which observations are retained, leaving the PFN's $\mathcal{O}(d \cdot N^2)$ inference cost unchanged. On functions drawn from a Matérn-3/2 kernel, ATR warping improves optimisation performance of the PFN at both extremes of the lengthscale range. Our implementation is publicly available at this https URL.

---


### 13. [Sparse tensor networks for individual tree diameter estimation in mixed forests](https://arxiv.org/abs/2610.37784)

**<font color=#1a73e8>作者：</font>** Clara Lößl, Fabian Ewald Fassnacht, Viacheslav Barkov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Measurements of tree diameter at breast height (DBH) are fundamental to forest inventories, but manual surveys across entire stands or regions are impractical. UAV-borne laser scanning (ULS) enables scalable automated forest surveys, yet canopy occlusion makes accurate DBH estimation from ULS point clouds non-trivial. Limited stem-level point density of ULS data constrains approaches relying on detailed stem reconstruction, such as Quantitative Structure Models (QSMs) and circle fitting. Empirical machine learning methods based on predefined point cloud metrics are an alternative. New deep learning approaches offer an even more principled solution, allowing models to learn directly from point clouds. Sparse tensor networks have shown particular promise, transforming forestry tasks such as tree species classification. We investigate whether these strengths can be extended to estimate individual tree DBH from ULS data across four mixed-species temperate forest plots in Germany. We further advance existing sparse tensor networks by introducing TreeNext, a lightweight deep learning architecture for direct individual tree parameter estimation from voxelized LiDAR point clouds. We present a fully automated forest inventory pipeline from individual tree instance segmentation to DBH regression, and quantify the impact of segmentation errors by comparing performance on automatically segmented and ground truth instances. TreeNext achieves an $R^2$ of 0.8355 on automatically segmented trees and 0.9380 on ground truth segments, outperforming strong tabular baselines including Random Forest and XGBoost. Segmentation quality emerges as the dominant error source in the automated pipeline. TreeNext proves highly data-efficient, performing well even in small data scenarios. Our findings establish sparse tensor networks as a practical foundation for automated individual tree DBH estimation from ULS.

---


### 14. [GOFish: Full Field-of-View Gaussian Splatting and Mesh Extraction](https://arxiv.org/abs/2610.37818)

**<font color=#1a73e8>作者：</font>** Allen Tu, Meher Gitika Karumuri, Shifan Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robots, autonomous vehicles, and consumer 360° cameras use fisheye lenses for wide fields of view (FoVs). Simulation-ready digital twins require photorealistic rendering across the full FoV and an aligned collision mesh. However, prior fisheye Gaussian Splatting methods only rasterize up to 180° and do not produce meshes, while Gaussian surface reconstruction methods assume pinhole training images. We present GOFish, the first 3D Gaussian Splatting surface reconstruction method to train directly on fisheye images, rasterize FoVs beyond 180°, and extract an aligned mesh from the same scene. Calibrated densification recovers the surface across the entire FoV, while Calibrated Mip Filtering and Wide-Angle Appearance Modeling keep pixel blur and lens falloff out of the scene and mesh. Across the 200° FIORD and 205° FullCircle benchmarks, GOFish improves PSNR over the best prior method by 2.28 and 1.97 dB, respectively. It also outperforms fisheye rendering baselines within their own FoVs and achieves the highest mesh F-score on FIORD and the main ScanNet++ set. Together, the Gaussian scene and mesh form a LiDAR-free, simulation-ready digital twin that renders in real time, ray traces the full FoV, and provides collision geometry.

---


### 15. [Responsible Quantum Machine Learning for Medical Imaging: A Fairness Audit Across Sensitive Subgroups](https://arxiv.org/abs/2610.37819)

**<font color=#1a73e8>作者：</font>** Giovanni dos Santos Franco, Felipe Mahlow, Ellison Fernando Cardoso 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum machine learning (QML) is increasingly explored for medical classification, yet its behaviour under subgroup-aware fairness criteria remains understudied. We present an empirical fairness audit of classical and quantum classifiers for medical imaging, assuming QML is not inherently fair. Two scenarios are evaluated: dermatological lesions on DDI (sensitive attribute: Fitzpatrick skin type) and chest X-rays on CheXpert-derived data (sensitive attribute: age group). Using ResNet-18 embeddings, we train SVM, MLP, QSVM and QCNN under a baseline and three mitigation settings: differentiable Equalized Odds (EO) regularisation, Gradient Reversal Learning (GRL), and both combined. Foundation models (PanDerm, EVA-X) serve as external references. Quantum classifiers may achieve competitive aggregate performance while still exhibiting subgroup disparities. Since a smaller subgroup AUC gap may stem from degrading the best group rather than improving the worst, each mitigation is also tested against a pre-specified non-inferiority margin relative to its baseline. Under this criterion, several configurations with the smallest disparity, notably QCNN with GRL on DDI, are not clinically acceptable due to loss of global discrimination. On DDI, QSVM with GRL+EO performed best and approached PanDerm in the performance/fairness trade-off; on CheXpert, QCNN with GRL achieved the highest aggregate performance but increased disparity, and EVA-X remained stronger. Fairness effects are model- and dataset-dependent, so QML requires empirical subgroup-aware evaluation. All quantum models run in classical simulation; we claim no quantum advantage.

---


### 16. [Learning Without Clocks: Partition-Invariant Neural Network](https://arxiv.org/abs/2610.37823)

**<font color=#1a73e8>作者：</font>** Han Wang, Jingyuan Bao, Juntao Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Event cameras, spiking cochleas and similar sensors emit asynchronous events, yet most learning systems first bin them into frames or packets, so the output depends on how the stream was sliced. Networks whose state is updated exactly at every event and evolves in closed form between events are invariant to this slicing. We ask what more makes the output (i) independent of the processing order of simultaneous events and (ii) continuous in the time stamps, even when two events cross in time, while (iii) staying sensitive to temporal order. For arbitrary nonlinear event models we prove that (i) and (ii) are each equivalent to pairwise commutation of the event updates, and that once updates commute, all order dependence comes from their non-commutation with the inter-event dynamics and vanishes linearly in the time lag. This identifies a class of time-mediated non-commutative (TM) models and yields a resolution-robustness bound for any model. We construct the minimal TM layer, a learnable, provably Lipschitz generalization of the Hassenstein-Reichardt correlator; prove that no single additive layer can uniformly represent ordered pair interactions, whereas a three-dimensional TM state can; show that each TM layer adds two levels of temporal nesting versus one for additive layers; and give a single-layer higher-order construction (TM-k) and a stacking rule preserving all three properties. We instantiate these results as the Clock-Free Event (CFE) layer, linear in the number of events, give a topology-free variant for temporal point processes with closed-form likelihoods, and specify a preregistered clock-robustness protocol with a physical-time threat model for spike-retiming attacks. In preliminary development-set experiments, the TM state beats an otherwise identical additive state by 3.5-9.1 points on DVS128 Gesture and by 24.5 and 30.6 points on SHD and Speech Commands.

---


### 17. [Learning Lotteries with Minimal Stakeholder Violations from Membership Queries](https://arxiv.org/abs/2610.37828)

**<font color=#1a73e8>作者：</font>** Nicholas Teh, Paul W. Goldberg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An AI developer often has several candidate versions of a system and can deploy a mixture of them, sending each request to a randomly chosen version, as in A/B testing. Each stakeholder (e.g., a safety team, a regulator, or a customer with private test data) accepts a mixture exactly when its expected performance (e.g., its rate of harmful replies) meets the stakeholder's own standard, which the developer can learn only by asking whether a proposed mixture is acceptable. We model this as choosing a lottery over $m$ alternatives for $n$ agents, each of whom accepts exactly the lotteries in an unknown halfspace and answers such binary membership queries. While Choo et al. (ICML 2026) sought a lottery that every agent accepts, none may exist when, say, safety and helpfulness requirements conflict, so we minimize the number of rejecting agents. We show that this problem is APX-hard even when all halfspaces are known and all utilities are $0$ or $1$. We then give exact algorithms that run in polynomial time when $m$ is constant, and in quasi-polynomial time when, for a constant $\eta$, some optimal lottery has no accepting agent within $\eta$ of its threshold. When only some agents can be queried, optimizing over a uniform sample of agents gives additive and relative guarantees for the whole population, with a sample size that does not depend on $n$, and a linear program gives a polynomial-time method for any $m$. On the other hand, for $m\ge 3$, a deterministic algorithm that queries only $K$ distinct agents cannot guarantee fewer than $n-K$ extra rejections, and this is achievable; in other words, it can guarantee nothing for the agents it does not ask. Small synthetic experiments indicate that our worst-case bounds are conservative on random instances.

---


### 18. [Measuring Where Intent Gets Lost in Agentic Smart Contract Synthesis](https://arxiv.org/abs/2610.37830)

**<font color=#1a73e8>作者：</font>** Abhinav Goel, Agostino Capponi, Alfio Gliozzo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can now write software from a plain-English description, but code that runs is not the same as code that does what was asked. This gap matters most for smart contracts, the programs behind Web3 applications that move money on a blockchain and cannot be fixed once deployed. We ask how to check whether an AI-written contract behaves as it should, and where the requested behavior gets lost.
We design an evaluation built on execution rather than opinion. We replay the same transactions on an AI-written contract and on the original it should reproduce and measure how often they agree. We test every grading tool on planted mistakes, compare against an answer key written without the description, and audit our own scorer until known wrong answers cannot pass. Common methods, such as AI judges and standard analysis tools, miss obvious mistakes, and scoring choices matter too. Checking only the functions every system includes hid about half the difference between pipelines.
We then propose an elicitation-first architecture. Before writing code, the agent asks the client a short checklist of questions, checks the contract against an independently written executable answer key, and returns disagreements to the client instead of silently rewriting code. Asking first matters far more than reviewing or patching afterwards, across three AI models, while automated security fixes often break requested behavior. A few well-chosen questions recover much of what a short description omits, and their value can be estimated without the original contract. To our knowledge, this is the first study in smart contract synthesis to gather missing requirements before generation and check the result against an independently written executable model. The lessons extend to any setting where AI agents turn requests into programs. We release our tools, 600 tasks and all results.

---


### 19. [TensorBound: Characterizing Tensor Binding Failures in AI Compiler and Runtime Stacks](https://arxiv.org/abs/2610.37838)

**<font color=#1a73e8>作者：</font>** Wen Li, Yongxi Sha, Baihong Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI compiler and runtime stacks must preserve bindings between tensor values and their operations, storage, and execution state. These bindings can fail while the underlying objects remain present, with symptoms appearing in another layer. We present TensorBound, an empirical study of tensor binding failures in IREE and the XLA and PyTorch ecosystems. The study analyzes 264 reports and reconstructs 149 distinct repaired causes through source tracing and comparisons of pre-fix and repaired revisions. Each reconstruction connects the first invalid decision to its violated condition, physical effect, and repair. Missing eligibility checks, incorrect mappings or translations, and lost or omitted relations account for 69.1% of repaired causes. These patterns highlight the need to preserve binding facts and check the conditions for their use. The 101 first invalid decisions in compiler code identify candidate checking points before execution. Four archived IREE diagnostic attempts distinguish effect localization from source-based cause explanation. Together, these findings motivate transition-specific checks that preserve binding facts across representations and enforce the required conditions at consuming decisions.

---


### 20. [Convex Potential Learning for Optimal Transport Between Medical Images](https://arxiv.org/abs/2610.37844)

**<font color=#1a73e8>作者：</font>** Hongyu Kan, Ivan Medri, Natasha Ironside 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computing optimal transport maps between medical images plays a fundamental role in morphological analysis. However, existing methods are either difficult to scale to large 3D medical images or rely on regularized formulations that provide only approximate transport maps. To improve the accuracy of downstream medical image analysis, we propose a novel approach for estimating optimal transport maps by parameterizing the convex potential function. By construction, the resulting transport map is guaranteed to be curl-free, consistent with Brenier's theorem. We evaluate the proposed method on both 2D and 3D medical imaging datasets. Experimental results demonstrate that our approach achieves lower transport estimation errors and produces higher-quality image reconstructions than existing methods.

---


### 21. [Detecting Covert Collusion between AI Agents through Partner-Outsider Positive Listening](https://arxiv.org/abs/2610.37849)

**<font color=#1a73e8>作者：</font>** Kevin Yandoka Denamganaï  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents that share a secret convention can coordinate through messages that look innocent, so a monitor that reads only the messages can miss them. We propose a behavioural test: a partner that uses a code reacts to the exact wording of a message, whereas an uninvolved agent placed in its seat does not. Partner--Outsider Positive Listening (PoPLi) is the difference between the two agents in how much their action changes when the message is reworded with its meaning kept, and it is computed after the fact by replaying logged prompts. In a simulated market with five conditions (no collusion, a joint reward with neutral messages, the same with an openly stated intention, a covert first-letter code, and the code with a stated intention), PoPLi is between 0.48 and 0.59 whenever the code is present (95% intervals all above 0.29) and between -0.10 and -0.01 without it. Message-only monitors did not separate the conditions: one reading the speaker's messages answered "no" in all 50 markets, and one reading every seller's messages flagged 9 of 10 markets with no collusion. PoPLi detects the use of a private channel, not collusion as such, and it cannot detect collusion through incentives alone or codes carried by meaning.

---


### 22. [Effects of Deep Learning Architecture and Pretraining on Automated Vocal Fold Segmentation in Ex Vivo High-Speed Phonation Images](https://arxiv.org/abs/2610.37860)

**<font color=#1a73e8>作者：</font>** Varun Vinayak Kalaiarasan, Charles Farbos de Luzan, Khalid Malik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Two-dimensional (2D) intraglottal particle image velocimetry (PIV) of ex vivo phonation experiments quantifies vocal fold medial surface dynamics and the intraglottal flow field. However, it relies on manual segmentation because residual glare, low tissue-to-flow contrast, and tracer-particle speckle obscure the vocal fold boundaries. This study assessed how deep learning architecture and ImageNet pretraining affect automated vocal fold segmentation in these high-speed images. Four established architectures from three categories were benchmarked: the convolutional neural network (CNN)-based UNet and UNet++, the hybrid CNN-transformer-based TransUNet, and the pure transformer-based Swin-UNet, the latter two trained from scratch and from ImageNet-pretrained weights. Using 16,344 expert-annotated images from 227 phonation trials of excised canine larynges, the six pipelines were trained with five seeds under a standardized protocol and compared on 50 held-out test trials using trial-level Wilcoxon signed-rank tests with Holm correction. Mean Dice similarity coefficient (DSC) spanned only 0.9734 to 0.9764, so the pipelines differed mainly in boundary fidelity. Pretraining significantly improved the boundary F1 score (BF1) and 95th percentile Hausdorff distance (HD95) of the TransUNet and Swin-UNet, about four times more for the Swin-UNet. Once pretrained, the two performed similarly, although the Swin-UNet has only about a quarter of the trainable parameters. Without pretraining, the TransUNet had a significantly higher BF1 and a lower HD95 than both CNN-based pipelines and about half their share of images with HD95 > 50 pixels. To our knowledge, this is the first study to apply deep learning to vocal fold segmentation in 2D intraglottal PIV, and it offers a reference framework for segmenting experimental flow-visualization images with noisy optical conditions or highly deformable objects.

---


### 23. [Improving Group Deliberation through AI-Guided Self-Reflection](https://arxiv.org/abs/2610.37862)

**<font color=#1a73e8>作者：</font>** Haiwen Li, Crystal Qian, Ben Usman 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI systems increasingly mediate human communication, identifying conditions under which they augment collective sense-making is a critical challenge. Through a randomized experiment (N=1,173 U.S. participants across 391 small-group deliberations), we investigate whether AI-guided self-reflection improves subsequent deliberative discourse. We show that engaging with a non-directive AI chatbot instructed to structure self-reflection prior to group deliberation yields significantly higher deliberation quality (measured by the Discourse Quality Index, DQI) compared to a baseline of no self-reflection (Cohen's d=0.31) and a condition of unassisted self-reflection (d=0.27), and the positive impact is most pronounced in groups with disagreement. This improvement may be driven by more sophisticated argument justifications, greater consensus-building effort, and increased respect for counterarguments. Furthermore, after self-reflection, participants in the AI condition reported higher empathy toward dissenting peers and a deeper understanding of opposing reasoning. Beyond observed behavior, our findings are empirically relevant to open debates between political philosophy and psychology surrounding self-reflection, demonstrating that interactive AI could transform solitary thinking into productive internal reflection. Together, these results demonstrate that even simple AI-based reflective scaffolds can foster more productive group dynamics, opening new avenues for leveraging AI to augment collective intelligence.

---


### 24. [What Constitutes Food Similarity? Visual Representations and Retrieval in Indian Cuisine](https://arxiv.org/abs/2610.37867)

**<font color=#1a73e8>作者：</font>** Saransh Kumar Gupta, Akshadha Sharma, Lipika Dey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Food similarity underlies retrieval, recommendation, substitution, and other food computing tasks, yet food representations are typically evaluated by identity preservation. We ask what happens to food similarity beyond identity: how different visual representations organize foods into relational neighborhoods, what culinary relationships these neighborhoods reveal or obscure, and how consistently these structures emerge across representations. Indian cuisine provides a challenging setting in which visually similar foods may have different culinary identities, while foods within a culinary family can vary substantially in appearance. Using an expanded Khana dataset and seven pretrained visual representations spanning convolutional, transformer-based, self-supervised, and image-text aligned models, we evaluate image-to-image retrieval and image-to-dish neighborhoods, examining culinary-family structure, contrast cases, and cross-representation agreement. We also aggregate image representations to compare dish-level visual similarity across models and against recipe-derived similarity for the same dishes. Image-level neighborhoods vary substantially across representations, including similarities across culinary-family boundaries. At the dish level, aggregation reveals common visual structure despite local variation, but this structure corresponds less strongly with recipe-derived similarity. These findings show that recognition performance alone cannot characterize relational structure: food similarity depends on representation, modality, and abstraction level rather than being a fixed property of the food collection. Understanding these structures is therefore a prerequisite to combining multiple food information modalities into a coherent notion of similarity.

---


### 25. [Multi-Agent Reinforcement Learning for Global Climate Policy Cooperation](https://arxiv.org/abs/2610.37870)

**<font color=#1a73e8>作者：</font>** Anne Moll-Elsborg, Oskar Bohn Lassen, Francisco Camara Pereira  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> International climate policy requires coordination among countries whose mitigation decisions impose local costs but generate global benefits. Classical game-theoretic and integrated assessment approaches can study these incentives, but typically rely on prescribed behavioural assumptions or equilibrium concepts. Recent work has therefore explored Multi-Agent Reinforcement Learning as a way to model climate-policy cooperation as an emergent outcome of repeated strategic interaction. We extend an existing MARL climate framework with a multi-stage negotiation mechanism in which agents propose agreements, accept or reject commitments, and face penalties for non-compliance. This allows us to study how agreement design affects learned mitigation behaviour, compliance, and climate outcomes. In an idealized setting with four homogeneous agents, we find that non-binding agreements do little to overcome free-riding, while moderate non-compliance penalties improve cooperation and reduce warming. However, excessively strong penalties discourage ambitious commitments, revealing a trade-off between enforcement and participation. We position the framework as a methodological contribution for testing agreement design rather than a predictive model of real negotiations.

---


### 26. [Set an Exploit to Catch an Exploit: Compiling Public Proofs of Concept into Threat Hunting Rules](https://arxiv.org/abs/2610.37872)

**<font color=#1a73e8>作者：</font>** Muhammad Shoaib, Alexander Suh, Joshua Andrew Tomiak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public exploit code for a newly disclosed vulnerability usually appears before any published rule that detects its exploitation. Of the 45 CVEs we evaluate, 37 ever received a Sigma, Elastic or Splunk rule; in 33 the exploit came first, by a median of 22 days. Analysts still write every rule by hand. We present Encore, which compiles a public Python proof-of-concept exploit (PoC) into CVE-specific hunting rules over a web service's existing logs, without running it. Encore rests on the PoC Behavior Alignment Principle: a PoC performs the exploit, so its code already provides a rule's HTTP requests, payloads and host operations. That is hard to act on: a PoC is written against libraries and runs on the attacker's machine, while the target's web-server, proxy and host logs record only what arrived and what it did. Encore closes the gap with a map from library calls to the operations they cause, built once per library, keeping only the operations visible on the target. For 12 of the 45, Encore's rule states the exploit's own payload fragment or host operation, which is evidence of the exploit itself, and not of traffic to its endpoint. On matched controls it separates that exploit from the same request with a harmless value, and it raises no alerts across 27,081 legitimate and crawl requests. We never compile the exploit that produced the logs. Most are Splunk's public attack data, recorded by a third party. Without reading a single log, Encore's rules find 43 of the 45. Splunk's log-tested rules cover 30 of the 45, and Encore finds 28 of those, plus all 10 CVEs without an ESCU rule. Where Splunk's rules alert on 20 wrong CVE pairs, Encore's alert on only 2. Hunting can start as soon as a PoC is public, and rules can raise an alert when it provides a payload or host operation.

---


### 27. [PairCLIP-SWA: Similarity-Guided Balancing and Stochastic Weight Averaging for Generalized Deepfake Image Detection with OpenCLIP](https://arxiv.org/abs/2610.37874)

**<font color=#1a73e8>作者：</font>** Md. Nakib, Sudipto Sarkar, A. J. A. Jubayer Talukder 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detectors are almost always deployed as the single checkpoint that scored best on a validation split, yet the reliability of that choice is rarely measured. We measure it with PairCLIP-SWA, a single-backbone detector that adapts an OpenCLIP ViT-L/14 visual tower by progressive block unfreezing on a class-balanced corpus built by CLIP-similarity-guided one-to-one subsampling, and averages the fine-tuning trajectory in weight space. Trained in-domain on the IEEE SP Cup 2025 (DF-Wild-Cup) benchmark under the same protocol as the strongest published three-backbone ensemble, the weight-averaged detector reaches 97.04% accuracy, 98.64% AU-ROC and a 4.07% equal error rate, against 94.46%, 97.60% and 5.00%. Its training log shows why averaging matters: over the averaged epochs the non-averaged checkpoint swings across 5.34 points of validation accuracy while its validation loss more than doubles, whereas the average is never worse and is up to 5.99 points better. On an OpenForensics-derived benchmark the same instability becomes a misranking: the checkpoint that validation accuracy selects (98.43%) scores 88.85% on a disjoint 10,905-image test partition, rejecting 21.1% of genuine photographs, while the terminal average, ranked last on validation, scores 94.76%. A study of twenty-two in-house configurations on the identical DF-Wild-Cup split, including preprocessing ablations, shows that CLIP pre-training rather than ensembling drives accuracy, that secondary face cropping costs about 34 points, and that frequency-domain inputs transfer poorly. We recommend per-class selection criteria measured off the early-stopping split.

---


### 28. [Verification Learning Theory: A Process Model of Checking and Retention in AI-Assisted Judgment](https://arxiv.org/abs/2610.37875)

**<font color=#1a73e8>作者：</font>** Christoph Trattner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate AI assistance can improve immediate judgments while reducing opportunities to practise the operations needed for independent performance. Verification Learning Theory (VLT) formalises this possibility for claim-evaluation practice followed by correct, independent, rule-specific feedback. The model links perceived assistant reliability to evidence checking and links the history of those checks to retained rule use. Its strict form assumes that task demands and perceived reliability influence learning only through checking, with equal learning per genuine check. It therefore predicts that perceived fallibility can improve delayed unaided judgment even without observed assistant errors, and that this advantage disappears when checking is already required and performed. Rule-specific gains and forecasts from checking histories provide further tests. Simulations examine the consequences and parameter dependence of these commitments; they do not constitute empirical validation. Comparisons with depth-of-processing and feedback-encoding accounts identify where predictions diverge and where the accounts remain observationally equivalent. The framework specifies experiments that can test the proposed mechanism and separates retention of practised rules from the broader problem of recognising which rule applies to a new claim.

---


### 29. [Interpretable neural equation learning for high-dimensional materials data](https://arxiv.org/abs/2610.37880)

**<font color=#1a73e8>作者：</font>** Philip Jacobson, Prasad Iyer, Remi Dingreville 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equation learning seeks to discover compact, interpretable equations from data using various machine-learning techniques. However, few workflows discover and interpret learned equations in sparse, high-dimensional materials datasets. We present nn-EQL, an equation-learning framework that generates candidate equations through iterative training, pruning, and retraining of a neural network with customizable, user-specified neuron-level activation functions. Candidate equations are ranked using a minimum description length (MDL)-inspired score, balancing error and sparsity, and diagnosed to assess term-wise contributions, input-scaled sensitivities, and uncertainties. We demonstrate nn-EQL on standard AI-Feynman benchmarks as well as multiscale high-dimensional materials datasets such as finite-element simulations of heterogeneous materials, and high-throughput experimental thin-film deposition data. nn-EQL integrates with tabular data and high-dimensional data via standard encoder models, learning equations and providing insight into learned terms. Looking forward, integrating physically interpretable representations, multimodal and multi-fidelity data, and adaptive data acquisition could enable equation learning to formulate and test mechanistic hypotheses.

---


### 30. [Intersectional Invariant Learning for Fair Deepfake Detection](https://arxiv.org/abs/2610.37881)

**<font color=#1a73e8>作者：</font>** Uzoamaka Ezeakunne, Taiwo Olabamipe, Deevesh Jain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detection models achieve high overall accuracy but exhibit large performance disparities across demographic groups, causing some groups to experience substantially higher false-positive rates than others. Existing fairness-aware methods address this by constraining model outputs to equalize group predictions, but do not tackle the underlying feature-level bias. As a result, models may still rely on demographic characteristics, such as skin texture, as indirect cues for detecting manipulated content. To address this problem, we propose Intersectional Invariant Learning (IIL), a framework that improves feature learning rather than only adjusting model outputs. IIL alternates between identifying the most challenging demographic partitions and learning features that remain consistent across those partitions. The framework also includes a false-positive-rate fairness objective and group-balanced sampling across six gender x skin-tone intersectional groups. We evaluate IIL on a large-scale fairness benchmark containing over one million images, 10 baseline detectors, and 21 fairness and utility metrics. Results show that IIL achieves Pareto-optimal performance, simultaneously attaining an AUC above 99%, a false-positive rate under 2.5%, and the lowest intersectional fairness disparity (FMEO) among all compared methods. IIL outperforms prior fairness-aware methods on the large majority of the 21 evaluation metrics, while reducing both false-positive rates and intersectional fairness disparities by several-fold compared with the strongest competing method.

---


### 31. [FYC: FPR-Disparity Weight Perturbation and Youden Calibration for Fair Deepfake Detection](https://arxiv.org/abs/2610.37882)

**<font color=#1a73e8>作者：</font>** Uzoamaka Ezeakunne, Taiwo Olabamipe, Deevesh Jain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detectors routinely achieve high aggregate accuracy while exhibiting substantial demographic disparities in their errors: false-positive rates differ by double digits across gender and skin tone. Most existing remedies require either full retraining with a fairness-aware objective or demographic-annotated training data, both impractical when only a pretrained checkpoint is available, while label-free post-hoc calibrators leave the detector's weights unchanged. We introduce FYC (FPR-disparity Weight Perturbation and Youden Calibration), a two-stage post-hoc method that perturbs a detector's weights under an FPR-disparity criterion, then calibrates a separate decision threshold for each demographic group - requiring no architectural changes and no full retraining. Evaluated against every detector benchmarked on AI-Face v2 across six intersectional gender x skin-tone groups, FYC outperforms the field on 18 of 21 reported fairness and utility metrics, including purpose-built fairness architectures, at a fraction of the training cost. We further identify why the choice of fairness criterion is critical: the original Demographic Parity objective used in prior weight-perturbation work is architecture-dependent and unpredictable, improving two of four evaluated architectures, leaving a third largely unchanged, and substantially degrading the fourth (PG-FDD), with no way to anticipate the outcome for a given checkpoint in advance. Conditioning the same objective on real images only - our FPR-disparity criterion - eliminates this unpredictability, improving fairness and accuracy jointly across all four architectures with no exceptions.

---


### 32. [Advisor, Co-pilot, or Guardian? AI Role Framing and Human Decision Behavior in Automated Vehicle Takeovers](https://arxiv.org/abs/2610.37892)

**<font color=#1a73e8>作者：</font>** Wei-Hsiang Lo, Jingyi Xie, Gaojian Huang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) technology has gradually been integrated into automated vehicles. However, how this technology could systematically support takeover transitions in SAE Level 3 automated vehicles remains unknown, even though this level may remain a major form of driving automation in the near future. To address this, we implemented the three AI roles proposed by the triadic Human-AI collaboration framework (Advisor, Co-pilot, and Guardian) as potential authority-ability configurations for AI agents within an automated system. We then examined their interactions with explanation type (why and action) and directional semantics (ipsilateral and contralateral) in an automated driving simulator study with 24 participants. Results showed that, across the three AI roles, Advisor had the shortest decision-making time, followed by Guardian and Co-pilot. Advisor and Guardian were associated with higher decision-making accuracy and higher satisfaction ratings than Co-pilot. Guardian was associated with the lowest workload, followed by Advisor and Co-pilot. The effect of explanation type on decision-making time depended on AI role. Action explanations were faster under Advisor, whereas why explanations were faster under Co-pilot. For directional semantics, ipsilateral semantics were associated with shorter decision-making time than contralateral semantics. Overall, these findings provide preliminary guidance for designing AI-role authority-ability configurations and their associated speech-based takeover messages.

---


### 33. [SAC-GCL: Structure-Aware Compression for Graph Contrastive Learning](https://arxiv.org/abs/2610.37898)

**<font color=#1a73e8>作者：</font>** Muhammad Ifte khairul Islam, Tanvir Hossain, Esra Akbas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Contrastive Learning (GCL) has achieved remarkable success in self-supervised representation learning by maximizing agreement between augmented views of a graph. Although augmented view generation is the central step in GCL, existing models rely on stochastic augmentation of the input graph, such as edge perturbation and node masking, which lack structural awareness and frequently destroy critical topology or introduce semantically inconsistent views. While recent adaptive methods improve upon random perturbations, they primarily operate on localized node or edge neighborhoods and fail to capture higher-order, macro-level structural organization crucial for graph classification. To address this limitation, we propose Structure-aware Compression for Graph Contrastive Learning (SAC-GCL), a novel framework that employs structural decomposition and graph compression as a principled view generation strategy. Moving beyond random augmentations, SAC-GCL leverages structural decomposition techniques to extract cohesive subgraphs and condense them into supernodes, constructing coarsened graph views that preserve local density and capture higher-level structural patterns while reducing noise and redundancy. We leverage multiple cohesive subgraph models to derive complementary views of the graph, each capturing distinct structural properties. To capture multi-resolution information, a hierarchical view encoder processes these compressed views by initializing super-node features with shared-weight cohesive subgraph embeddings. Our results from extensive experiments on six benchmark datasets demonstrate that structure-aware compression provides a powerful alternative to random perturbations, yielding more robust and discriminative graph representations for graph classification tasks.

---


### 34. [Beyond Low-Pass Dynamics: Frequency-Selective Spiking Reservoirs with Resonant Neurons](https://arxiv.org/abs/2610.37906)

**<font color=#1a73e8>作者：</font>** Aurora Micheli, Claudio Gallicchio, Nergis Tomen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking reservoir computing combines the training efficiency of fixed recurrent reservoirs with the energy efficiency of event-driven inference, where computation is triggered by sparse spikes rather than executed densely at every timestep. However, existing spiking reservoirs almost exclusively rely on Leaky Integrate-and-Fire (LIF) neurons, whose low-pass dynamics limit their ability to distinguish information encoded at different temporal frequencies. We introduce HRF-Res, a liquid state machine in which LIF neurons are replaced by a heterogeneous population of Harmonic Resonate-and-Fire (HRF) neurons. These neurons exhibit intrinsic oscillatory dynamics and selectively respond to input frequencies, enabling the reservoir to capture frequency-specific temporal patterns. The result is more discriminative representations and higher classification accuracy than LIF-based reservoirs, achieved without sacrificing the energy efficiency of spiking computation, with up to 19x lower energy consumption than an equivalent non-spiking oscillatory reservoir. Evaluated on ten benchmarks spanning time series, sequential images, audio spike trains, and neuromorphic vision, HRF-Res achieves state-of-the-art accuracy among spiking reservoir methods. These results demonstrate that introducing frequency-selective dynamics into spiking reservoirs improves representational quality and classification performance while preserving their inherent energy efficiency.

---


### 35. [TERRA: Task-Oriented Edge AI for Regional Fire Detection with Identity-Free Reporting](https://arxiv.org/abs/2610.37909)

**<font color=#1a73e8>作者：</font>** Mohammad Kazemi, Julie A. McCann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributed fire-monitoring systems may involve many sensing devices reporting over a shared uplink, even though the operational objective is often to identify regions exhibiting evidence of fire rather than to recover device-specific measurements. We introduce TERRA (Task-Oriented Edge Representation and Regional Aggregation), an edge-AI framework that combines task-oriented local inference, identity-free region-tagged reporting, and permutation-invariant regional evidence aggregation. TERRA supports two reporting modes: TERRA-Score, in which each device communicates a quantized local fire probability, and TERRA-Feature, in which it communicates a compact learned representation for receiver-side aggregation using a permutation-invariant DeepSets model. Using all 15 numerical sensing modalities of the distributed indoor EN54 fire-alarm dataset as a proof-of-concept testbed, we evaluate regional inference for an episode-level fire-scenario target under repetition-disjoint three-fold cross-validation. We study representation size, task-payload quantization, report availability, and robustness to missed and false recovered messages. With nine reports and perfect message recovery, TERRA-Feature achieves mean AUPRC 0.990 using a 24-bit task payload, while TERRA-Score achieves 0.987 using only 6 bits; both attain an MDR of 1.81% at FAR $\leq$1%. TERRA-Feature achieves slightly higher AUPRC under reliable recovery, whereas the more compact TERRA-Score is less sensitive to increasing false-message contamination.

---


### 36. [Generative modeling for fusion: a large-scale benchmark of stellarator fast-ion simulations](https://arxiv.org/abs/2610.37910)

**<font color=#1a73e8>作者：</font>** Misha Padidar, Teresa Huang, Mark Goldstein 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stellarators offer a promising magnetic confinement approach for achieving controlled nuclear fusion. However, stellarator design remains challenging, as evaluating configuration performance requires computationally expensive, high-fidelity simulations. In particular, key performance metrics derived from guiding center simulations are costly to include directly in the design optimization loop, and are almost exclusively used as diagnostics. Machine learning has the potential to advance fusion research by enabling rapid generation and evaluation of new stellarator configurations. Effectively applying ML for fusion demands large-scale datasets that capture both design diversity and high-fidelity simulation outputs. In this work, we introduce the Benchmark of Stellarator Simulations (BoSS), a dataset of stellarator designs paired with guiding center simulation results and trajectories. The BoSS is the first large-scale dataset of guiding center simulations, containing simulation data for 180,000 distinct magnetohydrodynamic equilibria spanning a wide range of magnetic geometries and confinement properties. To exemplify the utility of ML to accelerate stellarator design, we formulate and address two sets of modeling tasks: generative modeling for designing stellarators with good particle confinement, and surrogate modeling for predicting stellarator heat deposition patterns and particle trajectories. The tasks reveal the potential impact ML can have in the stellarator field and important opportunities to improve the applicability of ML models in the sciences. Our baselines generate diverse, performant stellarators and provide useful surrogate predictions, and point to long-horizon trajectory forecasting and out-of-distribution generation as key directions for future work. The BoSS can be accessed through this https URL.

---


### 37. [Grounding Long Financial Text with Semantically-Enriched Tables via Multimodal Learning](https://arxiv.org/abs/2610.37913)

**<font color=#1a73e8>作者：</font>** Xiaoyu Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose a multimodal transformer framework for efficiently modeling long1 financial documents that combine structured tabular data with noisy, unstructured2 textual disclosures. The framework represents financial tables as semantically3 enriched token sequences and integrates them with long-form text through a cross-4 attention mechanism that explicitly captures cross-modal dependencies. In par-5 ticular, we augment each numerical variable with a semantic embedding derived6 from its textual definition, enabling the model to encode both numerical magnitude7 and economic meaning. This design yields a more expressive and parameter-8 efficient representation of tabular data compared to value-only embeddings. Using9 a large-scale dataset of financial statements and MD&A disclosures, we show that10 structured numerical features remain the dominant source of predictive signal;11 however, textual information provides consistent incremental gains when incor-12 porated via cross-attention rather than simple concatenation. Our results further13 demonstrate that noisy textual disclosures are most useful when conditioned on a14 stable, semantically structured tabular representation. In particular, using frozen15 variable-level tabular representations as cross-attention queries enables the model16 to weight MD&A chunks differently for each financial variable and observation.17 These findings suggest that cross-attention provides an efficient mechanism for18 table-conditioned aggregation of long-form narrative evidence.

---


### 38. [What Is the Role for Humans in Creative Writing? Creativity and Diversity in Human-AI Collaboration](https://arxiv.org/abs/2610.37916)

**<font color=#1a73e8>作者：</font>** Chenyi Li, Haoyu Hu, Raja Marjieh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI agents increasingly participate in creative teamwork, writing emerges from hybrid human-AI teams. Although AI can improve the creativity of individual outputs, these gains may come at the cost of homogenization. What is the best role for human intervention? We introduce a transmission-chain paradigm inspired by cognitive models of writing, with four stages: Plan, Write, Review, and Revise. Each stage receives the previous output and passes its own forward. Using data from 333 participants across 427 stories, we compared creativity, diversity, and enjoyment across human, AI, and hybrid chains. Consistent with prior work, all-AI chains produced more creative but less diverse stories than all-human chains. Introducing a single human into an otherwise all-AI chain increased diversity depending on role. Human planning provided the best balance: it preserved AI-level creativity, increased diversity that persisted through downstream AI stages, and maintained enjoyment. We discuss implications for designing human-in-the-loop creative pipelines.

---


### 39. [Finite-Step Geometry of Marginal-Preserving Velocity Fields in Generative Flows](https://arxiv.org/abs/2610.37936)

**<font color=#1a73e8>作者：</font>** Ewsey Obzherin, Valentin Khrulkov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative flows can admit different velocity fields that induce the same continuous marginal evolution but behave differently after numerical discretization. We study this finite-step non-equivalence while keeping the marginal path and numerical method fixed. Projected modified equations characterize the component of local integration error that changes the marginal law and give sufficient conditions for higher marginal convergence order. For affine fixed-shape distributions, we characterize exact finite-step reachability and derive spectral obstructions and sharp nearest-reachable Wasserstein errors. For diffusion probability-flow ODEs, we construct skew-score perturbations that preserve the exact marginal path under exact scores and quantify their leakage under score error. Controlled Gaussian and mixture experiments recover the predicted order, reachability, and obstruction phenomena.

---


### 40. [You Don't Need Aligned Representations: Knowledge Distillation via Random Prototype Spaces](https://arxiv.org/abs/2610.37937)

**<font color=#1a73e8>作者：</font>** Hamza Etcibasi, Ramazan Gokberk Cinbis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A widely held assumption in knowledge distillation is that teacher and student representations must occupy a compatible or explicitly aligned feature space. We propose RPKD (Random Prototype Knowledge Distillation), which discards this assumption by comparing both networks against a shared bank of randomly initialized, frozen prototype vectors. Alignment is therefore carried out in an external reference space rather than in the teacher's native feature coordinates: the teacher side is projected by fixed random maps that carry no trainable parameters, and only the student adapts. Two branches handle the transfer: a logit branch aligning global prototype similarity distributions and a feature branch matching spatially-resolved prototype activation maps. Both operate within the same fixed prototype space, which can be interpreted as a random feature embedding that approximately preserves inter-sample similarity structure, so the prototype bank and the distillation objective stay unchanged across teacher-student pairs while only the input projections are instantiated per architecture. In low-category settings, decoupling the prototype vocabulary from the task label space yields richer supervision than the label space alone, an advantage absent from logit-based methods, whose supervisory signal collapses as class count shrinks. This advantage is especially relevant in real-world scenarios where the label space is typically constrained. Extensive experiments demonstrate the effectiveness of RPKD, achieving a maximum gain of +7.98% over OFA on CIFAR-100, +12.44% on ImageNet-100, and +1.28% on ImageNet-1K. Source code is available at this https URL

---


### 41. [The Collaborative Critique: An Inspection Method for Expert Evaluation of User Interfaces](https://arxiv.org/abs/2610.37946)

**<font color=#1a73e8>作者：</font>** Wendy Lucas, Tamara Babaian  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The development of the collaborative critique (CC) usability inspection method was driven by the need for systems, ranging from the simple to the complex, to lessen the workload on their users by being better collaborative partners. In the collaborative view of system-user interaction, the role of the system is expanded to that of a partner that must help its users achieve their goals. This perspective shifts the dynamic from focusing on the user's ability to make effective and efficient use of the system to the system's usefulness within a given task, user, and interaction context, thereby reducing the user's cognitive and physical efforts. The CC method consists of a walkthrough evaluation in which the questions answered at each step of the interaction assess the collaborative strength of the system. This method is further distinguished by the inclusion of questions that access the behavior of the system in error situations, which are known to be particularly burdensome to users of complex systems. In this paper, we provide a detailed description of the CC method and its application and demonstrate its usefulness in evaluating an interface. The results of a laboratory evaluation show that the method performed well in identifying the problems experienced by users across all severity levels and predicted almost all of the problems associated with error situations.

---


### 42. [AI-Generated Non-Consensual Intimate Imagery is Configured, Not Built: How General-Purpose AI Technology Enables Sexual Violence](https://arxiv.org/abs/2610.37949)

**<font color=#1a73e8>作者：</font>** Julia B. Kieserman, Ashley Phoebe Ishoel, Damon McCoy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-generated non-consensual intimate imagery (AIG-NCII) is an increasingly prevalent form of online abuse, distinguished from AI-generated sexual content (AIG-SC) by the sexualized depiction of a real person's identity without their consent. To understand how offenders may benefit from the tools and resources shared across the broader AIG-SC community, we analyzed 139 R+ guides on CivitAI, a popular platform known to host a disproportionate amount of AIG-SC.
We find that AIG-SC guides discuss how to create content generation workflows composed of sexual and identity concepts, the building blocks of AIG-NCII, including one guide that explicitly outlines an AIG-NCII workflow. We identify that ultimately AIG-NCII is enabled by configuration rather than a distinct set of technical tools. We map AIG-NCII threat models across basic and advanced AIG-SC workflows to demonstrate how multiple dual-use technical components can compose NCII outputs in an environment with little to no discussion of ethical implications or responsible use. We conclude by noting that, as most workflows rely on open-weight models, existing technical defenses against AIG-NCII are limited. However, our findings offer a starting point for evaluation of AI-based models and products against realistic attacker behavior required by new EU regulation and suggest that efforts to develop safeguards at the model- and product-levels should focus on generation of identity content.

---


### 43. [SAG-Sep: Sparse Augmented Graphs and Onion-Guided Search for Rounded Capacity Cut Separation](https://arxiv.org/abs/2610.37952)

**<font color=#1a73e8>作者：</font>** Haoran Liu, Guanyi Wang, Yu Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rounded capacity cuts (RCCs) are among the most effective cuts for capacitated vehicle-routing relaxations, but exact separation is computationally prohibitive at scale. Existing heuristic and neural separators can be fast, but often fail to produce sufficiently many effective cuts within practical separation budgets. We introduce SAG-Sep, a separator that scores node membership in RCC-inducing subsets across vehicle-count levels from a fractional LP solution in a single encoder forward pass, avoiding the iterative predict-and-coarsen inference used by NeuralSEP-style separators. SAG-Sep encodes the LP solution as a Sparse Augmented Graph (SAG), adding flow-informed multi-hop edges that expose long-range routing structure without densifying attention. Beyond LP-aware sparse encoding, we observe that high-value exact RCCs are typically nested, organizing into onion-like subset families, and SAG-Sep's node scores track subset nesting depth. This motivates Onion-Sweep (OS), a training-free decoder that ranks customers by their scores, evaluates the RCC violation of every prefix of the ranking in one vectorized pass, and emits the most violated prefix of each replica together with a cross-replica family of nested proposals, converting independent node scores into structurally coordinated RCC candidates without a tuned threshold or probing band. On the NeuralSEP benchmark with N=1000 customer instances, SAG-Sep with OS reduces the average root gap by 17.7% relative to the strongest NeuralSEP baseline, while the single-pass SAG-Sep separator achieves a roughly 30-fold per-iteration neural separation speedup. Our findings suggest that LP-aware sparse encoding and the nested structure of high-value cuts are structural patterns worth leveraging in neural separation more broadly.

---


### 44. [Self-Supervised Latent Action-Conditioned World Modeling for Time Series](https://arxiv.org/abs/2610.37963)

**<font color=#1a73e8>作者：</font>** Chia-Han Kuo, Chengshuai Zhao, Huan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series data play an important role in various tasks, such as weather forecasting, web traffic analysis, and speech recognition. Recently, pioneering studies have increasingly adopted Joint-Embedding Predictive Architecture (JEPA) based encoders to learn time-series representations through latent-space prediction. However, they often overlook the underlying factors governing transitions between time-series observations. In this work, we hypothesize that explicitly modeling the information behind changes in time series can facilitate time-series modeling. Building on this hypothesis, we propose ACTS-WM, a self-supervised latent action-conditioned world model framework for time-series analysis. First, we introduce a latent action modeling approach that infers the underlying information behind time-series transitions as latent actions, without requiring explicit action annotations. We then develop a JEPA-based encoder and an action-conditioned world model to predict target time-series representations conditioned on the learned latent actions and task information. We evaluate ACTS-WM across 4 representative tasks on 22 datasets from diverse domains, covering univariate and multivariate forecasting and classification. Comprehensive experiments demonstrate that ACTS-WM can improve downstream performance over pretrained JEPA-based encoders by learning complementary representations.

---


### 45. [Meta-Initialization of Implicit Neural Representations to Accelerate Deformable Medical Image Registration](https://arxiv.org/abs/2610.37965)

**<font color=#1a73e8>作者：</font>** Marat O. Zinovev, Dmitry V. Sorokin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representation (INR) methods for deformable medical image registration require the network parameters to be optimized for each new image pair, making adaptation speed a practical limitation. This work investigates whether early adaptation can be accelerated using an initialization learned from a collection of previously solved registration tasks. We examine two schemes: Reptile meta-initialization and STRAINER transfer of the shared component of a coordinate network. KAN-IDIR is used as the base INR displacement-field model. Experiments are conducted on OASIS-1, with 364 consecutive pairs used for training and 49 pairs for test-time adaptation. Registration quality is evaluated using mean Dice and HD95, together with the fraction of voxels with a negative Jacobian determinant at iteration 1500. In the configurations studied, both schemes yield higher Dice and lower HD95 at early iterations than random initialization. Reptile numerically outperforms STRAINER under a small iteration budget, although their pretraining budgets are not matched. As the number of iterations increases, the differences between the schemes shrink. STRAINER pretraining takes 39-40 minutes, compared with 44.98 hours for Reptile.

---


### 46. [Application of PDE emulators for a multi-material, multi-physics simulation problem](https://arxiv.org/abs/2610.37972)

**<font color=#1a73e8>作者：</font>** Diane Oyen, Morgan Jones, Adithan Kathirgamaraju 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) architectures are being developed for fast emulation of numerical simulators to accelerate both scientific discovery and engineering design. While these approaches are well-tested on popular PDE (partial differential equation) benchmarks, it is necessary to evaluate their performance on datasets that more accurately reflect industrial and engineering applications. We evaluate several computer vision-based architectures trained as surrogate models on a challenging computational physics task involving multiple materials, revealing significant implementation challenges for adapting certain pre-trained models, including transformer-based architectures. For such multi-physics multi-material datasets, our results underscore the importance of learning algorithms designed for sparse and imbalanced data, techniques for adapting spatial encodings and physical consistency metrics, in addition to methods for reducing the cost of generating sufficient training data.

---


### 47. [Sometimes less is more: Investigating inductive biases of MLPs and Transformers on noisy k-parity features](https://arxiv.org/abs/2610.37976)

**<font color=#1a73e8>作者：</font>** Alasdair Paren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We empirically investigate how MLPs and Transformers differ when trained on data sets containing one or more features encoded by noisy k-parity. Noisy k-parity gives us hard synthetic data sets in which we can control the predictivity and availability of every feature. Across a range of data distributions, data scales and model sizes, we find large differences in the training dynamics and inductive biases of the two architectures: Transformers are more robust to noisy features but struggle to learn complex, low-availability features, whereas MLPs show the opposite trend and improve steadily with more data. We also find that, under a fixed training budget, increasing the number of unique training examples can slow Transformer optimisation enough to reduce final accuracy, so that a smaller data set performs better. Training-accuracy results show this is an optimisation-speed effect; it shrinks, but does not vanish, when the budget is scaled with the data set size. By giving precise control over feature predictivity and availability, this testbed offers a clear starting point for understanding when and why Transformers and MLPs learn differently, and for designing data and training budgets that exploit those differences.

---


### 48. [Separability Is Not Alignability: Representations for Spectrum-to-Molecule Retrieval](https://arxiv.org/abs/2610.37979)

**<font color=#1a73e8>作者：</font>** Karol Musielinski, Fanurs C.E. Teh, Takahiko Koyama 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying a small molecule from its tandem mass spectrum is limited by paired data. Foundation models offer a way around this scarcity: pretrain a spectrum encoder on unlabeled spectra and a molecule encoder on a large corpus of structures, then align the two frozen representations, as in vision-language and as the Platonic Representation Hypothesis suggests. We audit this route on MassSpecGym with spectrum encoders retrained free of test-fold contamination. Alignment needs a metric relating distinct molecules, but the objectives that produce spectrum encoders never see molecular structure: we prove that some predictive objectives fix molecular identity without fixing that metric. Moreover, we find that a candidate-based objective rewards a spectrum-independent prior over the benchmark's decoys, which we isolate. What ultimately addresses data scarcity is not architectural: simulated spectra surpass frozen geometry.

---


### 49. [Revision-Bound Evidence Cuts: Authenticated Queries and Contextual Witness Capacity](https://arxiv.org/abs/2610.37982)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Taylan Alpay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Authentic records can support unauthorized narratives when their qualifications, query scope, or counterevidence are silently dropped. We present revision-bound evidence cuts, a framework for authenticating both supporting and opposing inference obligations across changing source versions. Signed complete-update frontiers permit transport of unaffected certificates, alternative-cut recovery, and an exact certified-reuse radius given by a frontier-hypergraph transversal number. Their source obligations induce an integral model of context-bound authorization. To secure database-derived claims, we introduce an authenticated relational query contract that binds original source records, complete selected bags, counting units, parameters, and aggregates independently of execution strategy. A full-source verifier checks 16,824 Chogha Mish records across SQLite scans, indexes, and materialized views; three valid strategies agree and eight contract/view mutations are rejected. A separate 340-row NISP cohort shows that changing the admitted weighting rule can reverse a comparison while preserving every source record. A frozen English text-to-frame compiler produces qualified evidence receipts, with linguistic accuracy evaluated separately from cryptographic integrity. We also separate logical-source from transport commitments so lossless re-encoding need not invalidate unchanged scientific evidence. The SCENE prototype evaluates signed revisions, authenticated queries, scoped disclosures, and adversarial mutations at scales reaching one million source records. These guarantees rely on declared policies and independently pinned trust roots; they authenticate specified computations and obligations, not historical truth, complete counterevidence, or institutional endorsement.

---


### 50. [Hierarchical Diffusion for Camera-controlled Autoregressive Video Generation](https://arxiv.org/abs/2610.37983)

**<font color=#1a73e8>作者：</font>** Kaihua Chen, Yiming Gong, Deva Ramanan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the task of long-video, camera-controlled generation from a single image. The dominant autoregressive paradigm suffers from two key limitations: (1) error accumulation over time, as distant frames are conditioned on previously generated outputs rather than ground truth, leading to drift; and (2) ambiguity in how to incorporate camera control. Standard solutions to both--such as self-forcing and conditioning on explicit 6-DOF poses--either incur significant computational overhead or produce drifting scene geometries over time. We propose a simple and lightweight framework that combines autoregressive generation (WanAR) with hierarchical long-context denoising (FixAR). To enforce scene geometry remains consistent with input cameras, we draw from feed-forward novel-view synthesis and reformulate video generation as a warping-and-inpainting problem. To mitigate drift, we introduce a hierarchical denoising strategy in which different stages condition on different temporal histories. Specifically, we first generate frames conditioned on the immediate past, and then refine them using a second denoiser conditioned on a temporally subsampled long-range history to enforce global consistency. This fine-to-coarse scheme enables each generated frame to effectively condition on the full temporal context without incurring a prohibitive cost. Experiments on RealEstate10k and DL3DV demonstrate that WanAR+FixAR outperforms prior methods for camera-controlled long-video generation, producing results that are both temporally stable and consistent with input camera trajectories.

---


> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-432](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
