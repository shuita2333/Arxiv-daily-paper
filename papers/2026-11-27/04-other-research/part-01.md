# 📦 其他研究 | 2026年11月27日

> 本类共 **314** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-314](./part-07.md)

---

### 1. [Context Scaling: A New Frontier of AI Scaling](https://arxiv.org/abs/2611.33160)

**<font color=#1a73e8>作者：</font>** Xipeng Qiu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many failures of deployed AI arise not from weak inference but from a mismatch between the state a task depends on and the context available when the system acts. Relevant user state, repository revisions, tool traces, sensor readings, or environment changes may be unavailable, distorted, or poorly selected. We call the effort to reduce this bottleneck context scaling. We frame a model as $P_\theta(d\mid c)$ within a system governed by three budgets: training $B_\theta$, decision-time $B_d$, and context-infrastructure $B_c$. Pretraining scaling invests in $\theta$; decision-time scaling searches, refines, or verifies decisions under supplied context; context scaling improves the system's capacity to acquire, represent, deliver, evaluate, and persist deployment state for model use. The three programs interact, but only $B_c$ targets what the system can make available before a decision. This view makes the model-infrastructure pair the unit of analysis. We define effective-context value as a task- and intervention-dependent attribution, separate deployment state from model-visible context, and identify availability, fidelity, selection, and utilization failures. We then organize current mechanisms through a five-operation context lifecycle and propose controlled budget interventions and utility-cost curves for evaluation. The resulting agenda centers on grounded reporting, interaction-data and full-cost infrastructure, and safety and governance for persistent, adaptive systems.

---


### 2. [Quantum Machine Learning for Signature Forgery Detection](https://arxiv.org/abs/2611.33163)

**<font color=#1a73e8>作者：</font>** Nabila, Md Farhan Shahriyar, Nowshin Tabassum Puspa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline handwritten signatures remain a primary behavioural biometric in legal and financial documents. Detecting skilled forgeries from a static raster image is hard because pen pressure, timing and stroke order are missing. This work studies a family of quantum machine learning pipelines for offline signature forgery detection on a public Kaggle corpus of images split into two classes. We pair a ZZ feature map quantum kernel with three classical learners: K-Nearest Neighbours, Support Vector Machine and Random Forest. We then propose a deeper hybrid that uses EfficientNetB0 as a frozen feature extractor, reduces the resulting 1280 dimensional representation to a qubit register sized subspace through a quantum compatible principal component projection and decides class membership with a nearest neighbour rule. On a single held out test fold the proposed hybrid reaches 92.62 percent accuracy. On stratified five fold cross validation the same pipeline yields a mean accuracy of 91.26 percent with a standard deviation of 1.13 percent. The pipeline keeps a quantum embedding step that is portable to NISQ hardware. We report a controlled ablation across six quantum variants, confusion matrices, a t SNE projection and per class precision, recall and F1 score.

---


### 3. [AutoformBench: A Lean Formalization Benchmark for Advanced Mathematics](https://arxiv.org/abs/2611.33165)

**<font color=#1a73e8>作者：</font>** Charles Arnal, Ahmad Rammal, Niket Patel 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are increasingly capable of producing machine-checked Lean proofs of advanced mathematical results. Real mathematical formalization, however, is not isolated theorem proving: it requires building the definitions and intermediate lemmas that connect a result to a formal library. Existing evaluations often provide isolated theorem statements in settings where much of this supporting theory is already available in Mathlib. We introduce AutoformBench, a benchmark of 341 Lean 4 formalization tasks drawn from 24 advanced mathematical sources. Lean-experienced mathematicians formalized and audited each target statement, leaving the corresponding Lean proof to the evaluated agent. Each problem is embedded in a broader mathematical development: agents receive the informal proof but must translate it into Lean while constructing the missing definitions, intermediate lemmas, and supporting infrastructure. We compare the performance of frontier models on these problems. We find a largely shared difficulty frontier: success depends less on mathematical domain than on models' ability to construct missing formal infrastructure. Data and code at this https URL

---


### 4. [Temporal Exposure to Byzantine Vulnerability Under Intermittent Participation in Federated Learning](https://arxiv.org/abs/2611.33168)

**<font color=#1a73e8>作者：</font>** Sasa Maric Robert Abbas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study the effect of participation variability on per-round Byzantine vulnerability. We formalise Dynamic Participation Exposure (DPE), a phenomenon in which the global Byzantine fraction remains below an aggregation rule's tolerance threshold, while a participating client set violates, or approaches violation of, the assumptions required for robust aggregation. Under stochastic participation, we derive the probability of per round exposure and analyse how active-set size affects the variability of the observed Byzantine fraction. We further examine the accumulation of exposure over multiple rounds and consider adversaries that selectively participate during favourable rounds. Our analysis shows that intermittent participation does not automatically imply aggregation failure. Rather, it transforms Byzantine robustness from a static population-level property into a stochastic and temporal property. To mitigate this risk, we outline actionable design recommendations based on minimum active-set constraints, temporal monitoring, participation history, and adaptive aggregation.

---


### 5. [On the Tragedy of the Commons in Heterogeneous Distributed Resource Allocation](https://arxiv.org/abs/2611.33172)

**<font color=#1a73e8>作者：</font>** Avadh Kishor, Rajdeep Niyogi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We consider the Tragedy of the Commons (ToC) problem, which commonly arises in heterogeneous distributed resource allocation, in which selfish users are independently interested in optimizing their own utility. Such self-interested decision-making in decentralized settings often results in inefficient resource utilization because users prefer high-capacity resources, leading to their overutilization. We cast the problem into a non-cooperative game and derive closed-form characterizations of both the distributed Nash equilibrium (NE) and the socially optimal allocation. In view of these closed-form expressions, we establish the structural conditions under which the ToC arises, and derive an exact expression for the Price of Anarchy (PoA). We further prove that the PoA can become arbitrarily large (unbounded) under suitable traffic conditions. Motivated by these observations, we propose a penalty-based incentive mechanism that discourages the use of overloaded servers while preserving decentralized decision-making. We analyze the resulting equilibrium load redistribution and establish conditions under which the proposed mechanism reduces the overall system cost and improves equilibrium efficiency.

---


### 6. [The Bundesrat corpus: A dataset of political discourse in the German Federal Council](https://arxiv.org/abs/2611.33173)

**<font color=#1a73e8>作者：</font>** Adama Njie, Leandro Laperne, Laksh Agarwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Bundesrat is Germany's second legislative chamber and a constitutional veto player within its political system. The members of the Bundesrat are delegates of state governments. Tracing the political discourse in the Bundesrat is challenging as it has a limited machine-readable corpus available. To address this issue, we present a speaker-attributed corpus of 1,067 Bundesrat plenary sessions from the chamber's first session on 7 September 1949 to 10 July 2026. In this period, a total of 53,362 speeches by 2,473 individuals were delivered in the chamber, including written statements. Each speech includes a speech ID, the full German text, the speaker's name, the date and location of the session, the federal state that the speaker represents, the speaker's role (if applicable), the type of contribution, and the speaker's gender. The dataset provides interdisciplinary research opportunities across computational political science, legislative studies, and parliamentary discourse analysis, coupled with discourse from the Bundestag.

---


### 7. [Feature-Based Explainability of Transformer Scoring Models: A Fidelity-First Framework for Automated Writing Assessment](https://arxiv.org/abs/2611.33175)

**<font color=#1a73e8>作者：</font>** Michael Hemenway, Edward W. Wolfe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based automated writing scoring models can achieve strong agreement with human scores while providing limited transparency into the response characteristics associated with their predictions. This study evaluated a feature-based post-hoc explanation approach in which explanatory fidelity was established before feature importance was interpreted. English Language Arts responses from three writing prompts in Grades 6 and 8 were analyzed, with about 12,700 responses per prompt and separate DeBERTa-v3-base research models for Expression and Conventions. Each response was represented by 61 interpretable linguistic and writing-quality features. Four approaches - theory-driven composites, hierarchical feature groupings, exploratory factor analysis, and Random Forest surrogates - were compared in their ability to reproduce DeBERTa predictions. Random Forest surrogates produced the largest observed R2 values across all six prompt-by-trait conditions, with held-out R2 values from .81 to .95. SHAP analyses showed substantial overlap in high-importance features across traits, with 75% to 90% of the top 20 features shared. Trait differentiation occurred mainly through relative feature weighting: Expression showed greater importance for lexical and conceptual indicators, whereas Conventions showed greater importance for sentence-level and syntactic-control indicators. Under researcher-defined mappings, rubric correspondence was 90%-95% for Expression and 12%-18% for Conventions. These percentages are descriptive and conditional on the mappings and available linguistic features. The findings support a fidelity-first framework for examining apparent scoring priorities while distinguishing post-hoc evidence about model behavior from direct explanation of transformer internals.

---


### 8. [Geophysics-informed invertible operator network for Bayesian geophysical inversion](https://arxiv.org/abs/2611.33178)

**<font color=#1a73e8>作者：</font>** Yangwen Zhang, Xintong Wang, Xiaofei Guan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geophysical inverse problems are inherently ill-posed because of sparse observations and measurement noise. Classical sampling-based Bayesian inference methods, such as Markov chain Monte Carlo (MCMC), are computationally prohibitive because they require many forward simulations. Data-driven machine-learning methods often struggle to produce physically consistent solutions when training data are limited. To address these issues, we propose a geophysics-informed invertible operator network (GI-ION) that integrates an invertible neural network (INN) within a deep operator-learning framework for efficient Bayesian geophysical inversion. The INN serves as the branch network and transforms the model parameters into branch coefficients that represent the forward solution and a latent variable that captures uncertainty in the inverse problem. By learning the forward operator and enforcing statistical independence between the branch coefficients and the latent variable, GI-ION enables efficient sampling from a learned conditional approximation, even with sparse boundary observations. We validated GI-ION on three representative cases: 1D surface-wave dispersion and travel-time tomography for a 2D synthetic random-field model and a seismic-slice model. Numerical experiments demonstrate robust performance across diverse problem settings and efficient conditional sampling.

---


### 9. [Deep Learning-Based Mesoscopic Emission Modeling](https://arxiv.org/abs/2611.33179)

**<font color=#1a73e8>作者：</font>** Abdelkader Dib, Milos Balac, Antonio Sciarretta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic-related emissions are a major contributor to urban air pollution. However, existing emission models face a fundamental trade-off: macroscopic models are computationally efficient but rely on average speeds, leading to systematic errors, while microscopic models achieve high accuracy but are computationally prohibitive for large scale simulations. To bridge this gap, this study introduces Direct Emission Prediction (DEP), a Gated Recurrent Unit (GRU)-based deep learning model. DEP was trained on over one million synthetic trips generated by coupling real-world GNSS speed profiles with the microscopic emission model MOBSim. By processing sequential link-level inputs, including vehicle characteristics, road attributes, and ambient temperature, DEP predicts CO$_2$ and NOx emissions. We integrated DEP into a MATSim-based workflow and applied it to the Ile-de-France region. DEP matches the accuracy of SPG-M, a hybrid mesoscopic-microscopic reference model, within 0.35% for CO$_2$ and 1.87% for NOx across both hot and cold-start scenarios, while reducing computational runtime to just 2.2%. Furthermore, validation against empirical remote sensing data confirms that DEP accurately reproduces real-world NOx emission levels across Euro 2-6 diesel vehicles, whereas traditional macroscopic tools like COPERT and HBEFA systematically underestimate them. Finally, DEP effectively captures the spatial distribution of cold-start emissions, identifying key hotspots in dense urban areas. This work demonstrates that deep learning-based mesoscopic frameworks can achieve microscopic accuracy at a fraction of the computational cost, enabling scalable, high-resolution urban emission modeling without relying on pre-computed emission factor databases.

---


### 10. [REI: Learning Ideation from Repository Evolution](https://arxiv.org/abs/2611.33183)

**<font color=#1a73e8>作者：</font>** Muyu Zou, Xiang Feng, Yufei Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As AI systems become increasingly capable of executing and evaluating experiments, ideation is emerging as a bottleneck in automated scientific and engineering iteration. In many real-world domains, useful ideas are sparse and their validation is costly, making direct online exploration inefficient. We observe that repository evolution provides a scalable source of reusable technical experience: code changes record concrete technical hypotheses, while subsequent revisions, adoption, and reuse provide signals about their utility. Based on this observation, we propose REI, a Repository Evolution-driven Ideation framework that learns reusable ideation policies from repository evolution, injecting domain-specific technical experience into model parameters and reducing reliance on costly trial-and-error. We further identify a hidden failure mode in quality-driven ideation optimization: semantic diversity collapse. Although generated ideas can remain lexically diverse, they increasingly concentrate in a small number of dominant method families, limiting cross-task generalization and long-tail exploration. To address this problem, we introduce Semantic Prior Optimization and Debiasing (SPOD), a diversity-preserving alignment mechanism that makes method identity explicit, corrects category-level reward bias, and limits redundant accumulation within the same method family while retaining strong representatives. Experiments on public benchmarks and a real-world industrial setting demonstrate improvements in ideation quality, method diversity, cross-task generalization, and long-tail exploration.

---


### 11. [PhoneWatchUI: A Dataset of Smartphone and Smartwatch Images from App Stores](https://arxiv.org/abs/2611.33196)

**<font color=#1a73e8>作者：</font>** Jialiang Wei, Walid Maalej  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Smartwatch apps are unique as they must condense functionality into a tiny screen of a few square centimeters. Yet, public GUI datasets are almost exclusively phone- or web-centric. We present PhoneWatchUI: 966.2k publisher-curated gallery image records from 72k store-specific app IDs on the US Apple App Store and Google Play, collected during October 2026. The Apple App Store part covers 37.6k apps with explicit Apple Watch platform metadata: 143.8k watch and 212.2k phone images labeled by their source galleries. The Google Play part covers 34.3k keyword-selected apps and 610.2k gallery images, provisionally labeled as watch, phone, or others by aspect ratio. Image records link to app metadata (title, description, category, ratings, developer, price) and retain source URLs, device-label provenance, and dimensions where available. We describe the dataset composition, image properties, and limitations. PhoneWatchUI enables research on cross-device GUI adaptation, wearable GUI retrieval and generation, as well as app-store analysis that links textual claims to visual evidence. Dataset is available at: this https URL

---


### 12. [Soft Decentralized Expected SARSA: Equilibrium Selection via Gradual Adaptation](https://arxiv.org/abs/2611.33228)

**<font color=#1a73e8>作者：</font>** Giuseppe Martucci, Janusz M. Meylahn, Gurdal Arslan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We introduce Soft Decentralized Expected SARSA (SDES), a modification of Decentralized Q-learning in which agents maintain persistent exploration and update their acting Q-values gradually rather than switching directly to newly learned best responses when updating. We prove convergence to $\epsilon$-greedy Nash equilibria in weakly acyclic stochastic games for sufficiently large batch sizes. We then show, in the repeated Prisoner's Dilemma with memory, that soft updating can reshape basins of attraction without changing the equilibrium set. In the deterministic limit, we derive analytical basin bounds governed by the Q-value differences between actions in the target policies and show that reducing the policy learning rate can favor either cooperative or competitive equilibria. These results suggest that soft updating is not merely a stabilization device but also a mechanism of equilibrium selection in decentralized learning.

---


### 13. [A comprehensive survey of deep face verification systems adversarial attacks and defense strategies](https://arxiv.org/abs/2611.33231)

**<font color=#1a73e8>作者：</font>** Sohair Kilany, Ahmed Mahfouz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face Verification (FV) systems have exhibited remarkable performance in verification tasks and have consequently garnered extensive adoption across various applications, from identity duplication to authentication in mobile payments. However, the surge in popularity of face verification has raised concerns about potential vulnerabilities in the face of adversarial attacks. These concerns originate from the fact that advanced FV systems, which rely on deep neural networks, have recently demonstrated susceptibility to crafted input samples known as adversarial examples. Although imperceptible to human observers, adversarial examples can deceive deep neural networks during the testing and deployment phases. These vulnerabilities raised significant concerns about the deployment of deep neural networks in safety-critical contexts, prompting extensive investigations into adversarial attacks and corresponding defense strategies. This comprehensive survey provides a comprehensive overview of recent advances in deep face verification, encompassing a broad spectrum of topics such as algorithmic designs, database utilization, protocols, and application scenarios. Furthermore, we conduct an in-depth examination of state-of-the-art algorithms to generate adversarial examples and the defense mechanisms devised to mitigate such adversarial threats.

---


### 14. [KiRA: Kronecker Input-Gated Rank Adaptation for Parameter-Efficient Fine-Tuning of Pretrained Models](https://arxiv.org/abs/2611.33236)

**<font color=#1a73e8>作者：</font>** Akil Ahmad Taki, Shaikh Anowarul Fattah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full fine-tuning of large pretrained models is expensive, and parameter-efficient fine-tuning (PEFT) is the standard alternative. Most PEFT methods use low-rank updates, whose rank lies far below that of full fine-tuning and is the same for every input. Input-adaptive variants vary the capacity per input but remain within the low-rank bottleneck, and whether a task benefits from input conditioning is not known before training. This paper introduces Kronecker input-gated rank adaptation (KiRA). Instead of the conventional low-rank product, the update $\Delta W$ is the Kronecker product of a frozen random $p\times p$ matrix $A$ and a trainable factor $M(x)$, which overcomes the rank ceiling: because rank is multiplicative under this product, $A$ multiplies the rank of $M(x)$ by $p$ without adding trainable parameters. The factor $M(x)$ is further decomposed as $B_1\,\mathrm{diag}(g(x))\,B_2$, where the input gate $g(x)$, computed once per sample by a network shared across all adapted layers, adjusts the rank of the update to each input in steps of $p$. Where input conditioning is unnecessary, the gate is folded into $B_1$ at deployment. Because the gate changes the rank only in discrete steps, the benefit of input conditioning can be predicted before training from a few hundred labeled inputs. Across six medical imaging and language benchmarks, KiRA attains the highest mean score against five published baselines with 8.7--9.7 times fewer trainable parameters than low-rank adaptation, and the pre-training criterion agrees with the measured benefit of input conditioning on all six tasks.

---


### 15. [Resource-Efficient Multimodal Fusion for Early Rice Blast Forecasting in Sustainable Agriculture](https://arxiv.org/abs/2611.33237)

**<font color=#1a73e8>作者：</font>** Shubhajyoti Das, Pritam Bikram, Arindam Biswas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Resource-efficient artificial intelligence has become increasingly important for sustainable agriculture, where timely disease forecasting must be achieved under computational and energy constraints. Early estimation of rice blast can enhance food security by optimizing crop management practices while reducing excessive pesticide use. However, existing frameworks often suffer from high computational overhead and limited capability to model the complex spectral-temporal dependencies present in heterogeneous meteorological and remote sensing data. To address these challenges, this paper proposes a lightweight multimodal fusion framework comprising an attentive positional encoding-based Transformer and a convolutional neural network (CNN)-embedded gated recurrent unit (GRU) for efficient spectral-temporal representation learning. The attention-enhanced positional encoding assigns adaptive importance to sequential meteorological tokens, enabling effective modelling of temporal characteristics. In parallel, the lightweight CNN extracts discriminative spectral features, while the GRU captures temporal dynamics from remote sensing imagery acquired over two time-instances. A multimodal fusion layer integrates these heterogeneous representations to forecast rice blast risk 5-10 days before symptom manifestation across diverse agro-climatic zones. Extensive experiments demonstrate that the proposed framework outperforms state-of-the-art methods, achieving a validation accuracy of 96.93% and an F1-score of 95.79%. In addition to its predictive performance, the lightweight multimodal architecture substantially reduces computational complexity, inference latency, and carbon emissions, making it an energy-efficient solution for large-scale disease forecasting. The proposed framework provides a practical foundation for resource-efficient artificial intelligence in sustainable agriculture.

---


### 16. [Sequential Testing on Complex and High Dimensional Data Streams Leveraging Unsupervised Model Errors](https://arxiv.org/abs/2611.33238)

**<font color=#1a73e8>作者：</font>** George Stamatelis, Iordanis Koutsopoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose two general, distribution-free test statistics for binary Sequential Hypothesis Testing (SHT) and Sequential Change Point Detection (SCPD) respectively, in streaming environments where the data (e.g., network traffic metadata) are too complicated for the exact probabilistic modeling required by conventional likelihood ratio-driven tests. Our framework also addresses the challenge of information asymmetry, where data is available only from the null/pre-change regime and not from the alternative/post-change one such as zero-day attacks or emerging disease related regimes. The proposed statistics monitor the errors of a predictive or reconstructive machine learning model trained solely on null/pre-change data, relying on imperfect generalization (the model's performance will degrade when deployed on data from the alternative/post-change class). Under mild assumptions on the model's errors, we establish rigorous analytical guarantees: strict non-asymptotic error control for SHT, and explicit bounds on the Average Run Length (ARL) and the Expected Detection Delay (EDD) for SCPD. Extensive evaluations in target tracking, chaotic dynamical systems, and real-world network security datasets, demonstrate that our framework consistently satisfies prescribed constraints where existing algorithms succumb to inflated missed detections and/or false alarms. Finally, because our methods operate on scalar errors without requiring online retraining or kernel evaluations, they are highly scalable.

---


### 17. [Beyond the Efficiency-Efficacy Dilemma: A Critical Analysis of Transferability in Adversarial Malware Detection](https://arxiv.org/abs/2611.33243)

**<font color=#1a73e8>作者：</font>** Veysel Alevcan, Mohammad Furqan Ali, Teresa Sousa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine Learning (ML) models are already being deployed at scale for malware detection. Therefore there is a pressing need to rigorously study adversarial robustness. To that end, we introduce the Adversarial AI Engine (AAIE): a platform for automated security stress-testing. We performed transfer attacks, via EMBER2018, against a Random Forest target. Counterintuitively, we found single-step FGSM to have the highest attack success rate (ASR) of 52.9% compared to iterative PGD with 45.2% (p < 0.002). Compared to iterative attacks which tend to overfit surrogate networks creating brittle perturbations, FGSM created more transferable examples. We benchmarked our attacks using ASR, transferability score, evasion rate, and resilience index. Through these metrics, proposed in concordance with emerging standards in AI governance, we expose shortcomings as our transferability scores peak at ~0.8 with constrained perturbations. We highlight the practical security implications of these findings and demonstrate AAIE for automated adversarial auditing.

---


### 18. [FERRETS: A Scalable Symbolic Transform for Time Series Classification](https://arxiv.org/abs/2611.33249)

**<font color=#1a73e8>作者：</font>** Antoine Guillaume  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dictionary methods for time series build bags of symbolic words from subsequences, but the accurate ones scale poorly. Against other families of methods, their accuracy no longer pays for their cost. We present FERRETS, a label-free dictionary transform built on WEASEL~2. It keys windows of random length and dilation into exact eight-bit words, adds a level word of each window's mean and spread, and on multivariate data adds cross-channel words. We compare it with leading classifiers, deep networks and foundation models included, on the UCR, Multiverse and MONSTER archives. FERRETS is the fastest of the eleven methods timed on UCR under a ten-thread budget. Of the ten others, only MultiRocket-Hydra is significantly more accurate, taking 24.7 times as long. FERRETS is not significantly different from WEASEL~2, the most accurate earlier dictionary method, which takes 125 times as long, and is significantly ahead of the other dictionary methods. On the Multiverse core, it is not significantly different in accuracy from HIVE-COTE~2 and MultiRocket-Hydra, though behind both on UCR. It is also significantly more accurate than five frozen foundation models on UCR's published split. On the MONSTER problems both complete, MiniRocket takes 3.7 times as long to fit as the streaming FERRETS classifier, which is significantly more accurate.

---


### 19. [MonoQPM: Splitting Features into Concepts for Inherent Interpretability and Predictive Performance](https://arxiv.org/abs/2611.33252)

**<font color=#1a73e8>作者：</font>** Thomas Norrenbrock, Robert Zimmermann, Timo Kaiser 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Alongside superposition, polysemanticity is one of the primary obstacles to achieving interpretable deep neural networks. While these phenomena are typically intrinsically linked, the Quadratic Programming Enhanced Model (QPM) naturally decouples them. By representing classes with a sparse binary assignment of very few features, QPM prevents superposition by design on its final features but still exhibits polysemanticity. However, measuring polysemanticity is an open problem. This work proposes a utility-focused approach to measuring polysemanticity by quantifying the decrease in interference-induced activation errors, which yields the practical utility of tighter prediction sets using Conformal Prediction (CP). We explicitly disentangle the polysemantic features of QPM into monosemantic concepts to create the Monosemantic QPM (MonoQPM). Because its features are disentangled, MonoQPM acts as a significantly more efficient Conformal Predictor. Additionally, we introduce CUBCars, a dataset providing ground truth information about shared concepts. Using this and other datasets, we demonstrate that polysemanticity emerges in QPM across all tested architectures, but is effectively alleviated by MonoQPM. For instance, MonoQPM guarantees 88% coverage using Adaptive Prediction Sets on ImageNet with just 66% of the frozen QPM's set size.

---


### 20. [CriticalScenes: Scalable Photorealistic Critical-Scenario Generation for Closed-Loop Driving Adaptation](https://arxiv.org/abs/2611.33255)

**<font color=#1a73e8>作者：</font>** Alexandros Theocharous, Holger Caesar, Ziqi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Safety-critical interactions are rare in recorded driving data, leaving end-to-end driving planners with limited exposure to evasive behaviour during training. This lack of critical supervision can lead to unsafe behaviour and, in rare instances, collisions. To address this gap, we introduce CriticalScenes, a reconstruction-based framework that transforms ordinary recorded driving scenes into photorealistic safety-critical interactions with corresponding collision-avoidance supervision. Across 53 reconstructed source scenes, 979 of 1,060 attempted interactions yield feasible threat trajectories (92.4\%), while the inserted threat actors remain detectable in more than 95\% of non-occluded observations within 5--35\,m. Experiments with two structurally different end-to-end planners show that the generated supervision improves critical-scenario planning, while closed-loop transfer varies across planner architectures. SparseDrive achieves a 46.5\% relative reduction in collision rate on an independent photorealistic closed-loop benchmark, whereas UniAD shows only a modest closed-loop improvement despite substantial open-loop gains. The results further highlight the importance of closed-loop evaluation, as improvements in open-loop trajectory prediction do not necessarily translate into equivalent safety gains.

---


### 21. [Fast and Scalable Abstract Interpretation for Deep Neural Networks](https://arxiv.org/abs/2611.33259)

**<font color=#1a73e8>作者：</font>** Avaljot Singh, Dushyant Bharadwaj, Yasmin Chandini Sarita 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Abstract interpretation can certify properties of Deep Neural Networks (DNNs), but precise analyses remain expensive. General implementations repeat work when analyzing the same architecture under different inputs and properties. Interleaving this work with numerical operations limits GPU utilization and restricts how much of the analysis a tensor compiler can process together.
We present Scepter, a framework for specializing DNN abstract interpreters through structural semantics. The semantics determine the structure of intermediate abstract values while deferring their numerical evaluation. Structural computations from successive operations can therefore be performed together before certification, generating an executable tensor program. With the abstract interpreter and DNN architecture fixed, the program can be reused with different weights and input regions. We prove that it computes the same bounds as the general interpreter in exact arithmetic. The generated program also exposes operations and their dependencies for tensor compilation and memory planning. We implement Scepter for the tensor programs that Neuton generates from ConstraintFlow specifications.
We evaluate Scepter on eight abstract interpreters and 44 DNNs against six baseline systems on GPUs and CPUs. Scepter handles networks with up to 153x as many neurons as the largest completed by the corresponding baselines. It completes DeepPoly on ResNet50 and VGG-16, whereas none of the evaluated DeepPoly baselines completes either network. On configurations completed by both systems, GPU geometric-mean speedups over Neuton range from 11.9x to 44.4x across eight analyses, with a 2.60x geometric-mean reduction in peak memory. In an input-splitting case study, Scepter proves 68 properties for which the baselines time out.
Code: this https URL

---


### 22. [Onnx2TEE: Automated Graph-Aware Model Partitioning for TEE-based Edge AI Protection](https://arxiv.org/abs/2611.33262)

**<font color=#1a73e8>作者：</font>** Daniela M. Vela Hernandez, Samuel Hildebrand, Sean Oesch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI models are increasingly being deployed at the edge. Since these models often require significant research and development to produce, are often deployed in potentially hostile environments, and downstream systems often rely on accurate data; protecting them from theft or manipulation is worthy of serious consideration. Trusted Execution Environments (TEEs), which provide hardware-enforced separation of software execution, can protect model weights but impose strict resource constraints, making full-model execution impractical for large neural networks. We present Onnx2TEE, an automated, model-independent pipeline that partitions ONNX models across rich, trusted execution environments for non-sequential feed-forward networks using graph-aware segmentation to preserve computational dependencies while minimizing boundary communication and reducing TEE-induced inference latency. Evaluation on an NVIDIA Jetson AGX Orin using an Arm TrustZone TEE demonstrates that model parameters can be highly concentrated in individual segments, supporting selective protection of parameter-dense model components. The evaluation further shows that the generated trusted app's memory requirements depend on both computation and intermediate tensor sizes.

---


### 23. [FrIdéo: French News Outlet Ideology Scoring via Multi-Source Evidence Fusion and Distancing-Aware Lexical Scoring](https://arxiv.org/abs/2611.33266)

**<font color=#1a73e8>作者：</font>** Amr Sobhy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Outlet ideology is a standard explanatory variable in media framing, media effects, and political communication research, but continuous, ecosystem-wide coverage lets it enter as graded exposure rather than a coarse bin. For France, existing references are either broad but non-analytic or analytic but sparse and source-specific, and none we are aware of offers ecosystem-wide coverage on a unified continuous scale. We contribute FrIdéo: to our knowledge the first ecosystem-wide continuous ideology scores for the French press, a transparent composite score for 30 French news outlets, fusing nine independent families of evidence with empirical-Bayes-style shrinkage toward a structural prior. For the text-based family we introduce symmetric plain/qualified scoring, which separates the plain use of ideologically loaded vocabulary from its qualified (distanced) use on both sides, a distinction bag-of-words methods miss. The resulting scale runs from L'Humanité on the far left to Valeurs actuelles on the far right; the far-right pole is near-indistinguishable and CNews ties Le Figaro. Because the text family reads current articles, it also captures editorial change that static sources miss, such as the Journal du Dimanche's sharp rightward shift after its 2023 ownership change. The ordering is robust to perturbation and to dropping any single family, and agrees with held-out Media Bias Fact Check labels. We release the scores, confidence intervals, and replication code.

---


### 24. [JetDiffusion: Pushing the Speed Limits of Video Generation with NVFP4 Sparse Attention](https://arxiv.org/abs/2611.33268)

**<font color=#1a73e8>作者：</font>** Yulun Wu, Zihan Min, Minshen Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attention over long sequences is a major computational bottleneck in video generation, which can be alleviated through sparsity and low-bit quantization. We propose JetDiffusion, a video generation system built on trainable Video Sparse Quantized Attention (VSQA), with custom inference kernels that combine native NVFP4 computation and kernel fusion. At 90% sparsity, VSQA accelerates attention by 8-29x compared with FlashAttention on different hardwares. To further accelerate video generation, we combine VSQA with NVFP4 linear quantization and step distillation. Although each technique can individually preserve generation quality, jointly adapting to all three remains challenging, particularly under aggressive NVFP4 quantization. Through empirical studies, we develop an effective staged training recipe that enables stable adaptation to quantization, sparsity, and few-step denoising. On Wan2.1-14B, the resulting model achieves 273x end-to-end video generation speedup on the RTX 5090 while maintaining comparable video quality.

---


### 25. [CoSMo: A Compact Spectral Space of Body Motion in Video](https://arxiv.org/abs/2611.33296)

**<font color=#1a73e8>作者：</font>** Maham Tanveer, Hao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce CoSMo, a compact spectral space of body motion in video, in which each motion is a single code that can be compared and edited without training, transferred to a new subject, interpolated, composed, scaled in intensity and detail, or sampled anew. Our encoder expresses how a clip's DINOv2 features change over time in a fixed temporal basis, the discrete cosine transform (DCT), and compresses this change into 384 numbers. Because each frequency band is the same cosine pattern in every code, codes are aligned in time, ordered from coarse to fine, and can be blended or added without matching frames. What stays constant over a clip cancels, and keeping fewer frequencies leaves less of the performer and scene. The encoder is trained on real videos and on synthetic motions of several characters, and lightweight adapters let a frozen image-to-video model render any code with any subject. On unseen videos, our code ranks the same motion on other bodies higher than DisMo, a per-frame representation, while its nearest neighbors show the same performer about 40% less often with a seven times more compact code. In generation, without per-motion training, CoSMo transfers motion more faithfully than FlexiAct and a text-prompt baseline, at least as faithfully as DisMo on automatic metrics and clearly better between humanoid bodies, and its blends keep much more of both source motions than DisMo's. Users rank CoSMo first nearly twice as often as DisMo for motion transfer (59% vs. 30%), place it top-two 94% of the time, and prefer it in 76% of the interpolation comparisons.

---


### 26. [Change Partners at Every Layer: Balanced Random Regrouping for Model Merging](https://arxiv.org/abs/2611.33308)

**<font color=#1a73e8>作者：</font>** Kaiyang Li, Shaobo Han, Shihao Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging combines fine-tuned experts into one model that serves many tasks without retraining, but merging many experts this way substantially reduces accuracy. Grouping offers a middle ground: at every layer or weight matrix, the $N$ experts are divided into $K<N$ groups, the experts in a group are merged into one shared module, and a task uses the module merged from its expert's group. Natural choices are to keep the same partners across layers or to group similar experts. Surprisingly, we find that randomly changing partners at every layer outperforms both. We call this Balanced Random Regrouping (BRR): it independently partitions the experts into $K$ equal-sized random groups at each layer (BRR-layer) or weight matrix (BRR-matrix) and merges each group with an existing method. With validation-selected merge scales, both BRR variants outperform reusing one grouping across layers in all 24 CLIP settings, by 1.0-6.8 points, and BRR-matrix also outperforms the similarity-based FlexMerge in every setting. A first-order analysis explains this gain. At each layer, merging a task's expert with its partners shifts the task's output features; when the partners are the same at every layer, these shifts tend to point in similar directions and add up, whereas with new partners at every layer they vary independently and add up less on average. A series of experiments supports this analysis, which further guides a grouping search that can outperform BRR.

---


### 27. [Large-scale Model Merging via Recovery-aware Task Weighting](https://arxiv.org/abs/2611.33315)

**<font color=#1a73e8>作者：</font>** Kaiyang Li, Shaobo Han, Boming Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model merging combines multiple task-specific expert models into a single model. However, merging preserves expert capabilities unevenly across tasks. This imbalance is particularly pronounced in large-scale settings, where some tasks can suffer severe capability losses even when average accuracy remains high. To address this imbalance, we introduce Recovery-aware Task Weighting (RaTW), a model merging framework that assigns larger weights to tasks whose expert capabilities are poorly retained by an initial merged model. We quantify these recovery opportunities as the fraction of a task's labeled validation samples that its expert predicts correctly but the initial merged model gets wrong, and use the resulting task weights to re-merge the experts. To evaluate merging at large scale, we construct CLIPMerge-100, a 100-task benchmark with task-specific experts on CLIP ViT-L/14 and ViT-B/32. Across eleven merging methods with 20, 50, and 100 tasks on two CLIP backbones, RaTW improves both mean accuracy and tail20 (the mean expert-normalized accuracy of the 20% worst-retained tasks) in all 33 ViT-L/14 settings and 32 of 33 ViT-B/32 settings. We further introduce ReForge++, which combines RaTW with iterative model refinement and outperforms all evaluated baselines, including a matched-budget control, in both mean accuracy and tail20 across all settings.

---


### 28. [StyleID++: Position-Decoupled and Structure-Coherent Style Retrieval across Diffusion Architectures](https://arxiv.org/abs/2611.33323)

**<font color=#1a73e8>作者：</font>** Chun Xie, Itaru Kitahara  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attention injection offers a remarkably simple route to training-free style transfer: content queries retrieve style keys and values inside a pretrained diffusion model. We show that this operation also creates an overlooked failure mode. Position signals that are useful within one image become a spurious shared coordinate system across two spatially unrelated images, causing content tokens to favor style tokens at similar coordinates. This cross-image positional leakage appears in both convolutional U-Nets and diffusion transformers (DiTs), despite their different position mechanisms. Removing the positional shortcut exposes a second problem: unconstrained global retrieval lets related content tokens select incompatible style regions, producing fragmented appearance. We present StyleID++, a training-free framework that addresses the two problems jointly. Position-Decoupled Retrieval reduces coordinate-dependent matching through circular padding in U-Nets and injection-only RoPE removal in DiTs, while preserving native position modeling elsewhere. Affinity-Coherent Refinement then regularizes style assignments with the content self-attention graph, encouraging structurally related tokens to retrieve compatible style evidence. We quantify the leakage with a coordinate--centroid correlation and a permutation test on the style reference. The permutation error can be driven to zero in both backbones, which identifies the position mechanism as the carrier of the leakage, and StyleID++ obtains the best ArtFID of all methods we compare.

---


### 29. [Do Not Let the Prior Heal the Anomaly: Selective Anchoring for Detection from Incomplete Measurements](https://arxiv.org/abs/2611.33331)

**<font color=#1a73e8>作者：</font>** Nicolas Tricard, Stefan Brandstätter, Jason Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative priors can recover anatomical detail from incomplete medical measurements, but may erase the very lesions that imaging aims to detect, even when the measurements contain evidence of them. We introduce selective anchoring that protects reliably measured image components from prior-driven changes, while allowing expressive generative models to reconstruct unresolved structure. Acquisition uncertainty in the protected components is either added deterministically to the downstream test or carried by the ensemble through stochastic perturbations of the readings. We implement this principle as a wrapper for pretrained diffusion and flow samplers and as AnchoredFM, a fast constrained flow model. Under a linear-Gaussian measurement model, the protected coefficients are unbiased in expectation and achieve nominal interval coverage across repeated acquisitions, independently of the learned prior. Across sparse-view CT, accelerated brain MRI, and photoacoustic tomography, selective anchoring improves lesion contrast preservation and uncertainty reliability, and can reduce reconstruction error within lesions. For tumor detection in accelerated MRI, with a healthy reference estimated from the measurements alone, deterministic anchoring raises mean AUROC across eight samplers from 78.4% to 84.6% and lesion sensitivity at 0.25 false-positive marks per slice from 38.8% to 47.5%, with gains in all four predefined tumor-size groups. At thresholds frozen on healthy validation data, mean sensitivity rises from 20.2% to 44.1% (37.6% with stochastic anchoring). These findings show how expressive generative priors can reconstruct unresolved anatomy without healing away the abnormalities that the measurements support.

---


### 30. [Online Prediction System for Proactive Autoscaling](https://arxiv.org/abs/2611.33332)

**<font color=#1a73e8>作者：</font>** Jun Gao, Areg Poghosyan, Pavel Paulau 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an online learning system for short-term time series forecasting that enables proactive autoscaling in large-scale distributed systems. Unlike traditional forecasting methods that focus on modeling seasonality and long-term trends, the system targets high-accuracy, low-latency predictions for immediate future intervals for dynamic resource management in internet-scale infrastructures. The system employs a two-stage architecture: a seasonality decomposition stage followed by a residual correction stage using lightweight linear models with engineered features. By retraining models on-the-fly for every prediction cycle, the online prediction system continuously adapts to changing demand patterns without requiring persistent model storage or feature drift monitoring. Deployed across many heterogeneous services, the system processes over 900K predictions per hour; in an offline evaluation on production traffic, its STL-based configuration reduces prediction error (MAPE) by 18.6\% relative to the previous production model. In production, the system has saved an estimated 118K servers daily.

---


### 31. [A Hierarchy of Risk Certificates for Representation-Based Prediction](https://arxiv.org/abs/2611.33333)

**<font color=#1a73e8>作者：</font>** Mohit Kumar, Somayeh Kargaran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation-based prediction underlies many machine-learning systems. Yet a fitted predictor's failure to meet an accuracy requirement does not establish that its representation-decoder class cannot meet it. We study optimal population mean squared error (MSE) over Lipschitz decoders acting on a fixed representation. For blocks of $b\geq2$ independent and identically distributed (iid) observations, we minimize total squared error (normalized by $b-1$) under pairwise Lipschitz constraints. We prove that expected block scores form nondecreasing lower bounds on optimal class risk and converge to that risk on compact metric feature spaces, although no fixed block size provides a uniform relative guarantee. Verified dual lower bounds and iid calibration observations independent of model development, with bounded targets and predictions, yield simultaneous lower confidence bounds on optimal class risk and upper confidence bounds on fitted-predictor risk. These bounds can establish that every admissible decoder exceeds a prescribed MSE threshold or that an admissible fitted predictor meets it. Controlled experiments illustrate population-risk certification; fixed PTB-XL and Bike Sharing experiments provide deterministic empirical-risk conclusions. The results support principled assessment and selection of representation-decoder configurations. Efficient certification at scale and extensions to dependent observations remain open problems.

---


### 32. [FlowersBench: A FluidFlower-Inspired Dataset for Benchmarking Carbon Storage Surrogates Across Geological Structures](https://arxiv.org/abs/2611.33335)

**<font color=#1a73e8>作者：</font>** Farah Rabie, Hannah Menke, Florian Doster 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning surrogates are emerging as a computationally efficient tool for uncertainty quantification in geological carbon storage (GCS). Geological structure constitutes a major source of uncertainty; however, existing benchmark simulation datasets predominantly vary petrophysical and operational parameters within a fixed geological setting. Generalisation to unseen geological structures therefore remains largely unexplored. We introduce FlowersBench, a benchmark dataset of 5,000 two-dimensional, reservoir-scale CO$_2$ storage simulations across 244 structural geometries. The geometries are sampled from an in-house structural generator inspired by the FluidFlower experiments and Case B of the 11th Society of Petroleum Engineers Comparative Solution Project (SPE11B). Each simulation is run with Open Porous Media (OPM) Flow over a 50-year injection period and a 500-year post-injection monitoring period. Test geometries are withheld from training to assess generalisation to unseen structural geometries. Two additional subsets support evaluation under structural shift. The first extends the parameter ranges of the structural generator beyond those used for training, and the second introduces an unseen topology of multiple parallel faults. A baseline U-Net surrogate is trained to predict CO$_2$ gas saturation. In representative test cases, the surrogate recovers the main migration pathways, including lateral spreading beneath low-permeability layers and upward flow along fault damage zones, with errors concentrated near the plume boundary. Under both structural shifts, prediction error exceeds that on the held-out geometries, and the increase in relative error is greater for the unseen fault topology. FlowersBench is publicly available and provides a common basis for evaluating GCS surrogates across geological structures.

---


### 33. [LGCount: Layout-Guided Diffusion for Zero-Shot Object Counting](https://arxiv.org/abs/2611.33344)

**<font color=#1a73e8>作者：</font>** Adriano D'Alessandro, Ali Mahdavi-Amiri, Ghassan Hamarneh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class-agnostic counting requires the user to specify what to count, usually with a class name or a few annotated boxes. We propose a richer text-based specification: a structured layout that names the target, the region that holds it, the distractors to ignore. A prompt upsampler writes this layout from the image and the requested category alone, and an image-editing diffusion model, adapted into a single-step counter, turns it into a density map. Because counting datasets pair each image with a single valid density map, a counter trained on it learns to ignore the layout. We therefore train on synthetic counterfactuals in which one image admits several valid density maps, so that the layout cannot be ignored. On FSC-147 we improve on the previous zero-shot state of the art and we set the best reported result on LOOKALIKES while being told the least about each image. A single photograph can be counted by category, by region, or by granularity without retraining.

---


### 34. [The Marauder's Map: Bézier Manifolds Reveal Hidden Surfaces for Model Merging and Ensembling](https://arxiv.org/abs/2611.33353)

**<font color=#1a73e8>作者：</font>** Abhiram Iyer, Mark T. Harnett, Sarthak Chandra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural circuits are famously more robust than deep networks. This is often explained through degeneracy, where structurally distinct configurations support the same function. However, real biological systems exhibit a more flexible form of degeneracy in which specialized circuits continually adapt towards new competencies through localized changes while preserving existing function. Deep learning studies degeneracy through mode connectivity, which connects same-task networks by low-loss curves, sheets, or volumes. However, the field lacks a counterpart to flexible degeneracy, which demands more than ordinary mode connectivity. Defining such an analogue requires asking whether many independently initialized models trained on distinct tasks can be connected by a high-dimensional region of multi-task solutions. We introduce $\textit{Nimbus}$, which learns a high-dimensional Bézier manifold connecting $N$ specialists, going beyond the one-dimensional paths and two-dimensional sheets of mode connectivity work. A naive parameterization would scale combinatorially with $N$, but $\textit{Nimbus}$ requires learning corrections of only 3 interaction orders, showing that the connecting manifold has surprisingly low complexity yet supports multi-task competencies. The resulting manifold forms a navigable "Marauder's Map" that connects specialist models through a shared geometry of competent solutions. Trained across vision and language domains, $\textit{Nimbus}$ produces manifolds that are functionally and locally weight-flat: ensembles sampled from them degrade more gracefully than baselines under input and weight perturbations, with the largest gains in NLL loss and calibration error. $\textit{Nimbus}$ supplies a deep learning interpretation of flexible degeneracy, recasting model connectivity from a low-dimensional path between distant solutions into a high-dimensional volume of nearby ones.

---


### 35. [DDxBasis: Explaining Frozen Foundation Encoder-based Medical Classification by Exact Differential Diagnosis](https://arxiv.org/abs/2611.33358)

**<font color=#1a73e8>作者：</font>** Luojie Huang, Gregory N. McKay, Nicholas J. Durr  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In differential diagnosis (DDx), a clinician explains a diagnosis by the few findings that separate it from the alternatives. Medical image classifiers cannot yet explain themselves this way. Existing explanations are either faithful but spread over hundreds of concepts, or compact but leave part of each decision unexplained. We present DDxBasis, which explains a classifier on a frozen foundation encoder as a differential diagnosis in three steps. First, a concept bottleneck reads all patch tokens at every encoder layer using gated, second-order slot attention. A concept basis then regroups the concepts into two-pole axes, each a differential between groups of diagnoses. Finally, we read a differential diagnosis from each axis through the typical presentation of its poles, the pertinent findings of the case, and counterfactual edits of borderline cases. Across five medical datasets, DDxBasis is the most accurate frozen-encoder model and close to the best published domain-specific results. Because every concept adds its own evidence, its reproducible concept basis splits each decision exactly, at no cost in accuracy. Without ordered stage or concept labels, the axes recover cell lineages and rare subtypes, agree with dermatologists' structure annotations, and expose planted and real shortcuts.

---


### 36. [Discovering Explicit Magnetic Core-Loss Equations via Symbolic Sparse Identification](https://arxiv.org/abs/2611.33364)

**<font color=#1a73e8>作者：</font>** Haoyu Wang, Jialin Zheng, Ziyang Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compact core loss equations are essential tools in magnetic component design, but existing approaches trade accuracy against interpretability. Empirical models such as the Steinmetz Equation (SE) yield compact expressions of limited accuracy, while machine learning methods achieve high accuracy as black-box predictors. This paper bridges the gap with a Symbolic Sparse Identification (SSI) framework, which casts core loss modeling as a data-driven symbolic regression problem and recovers unknown equations directly from measured data, without presuming a functional form. First, a comprehensively expanded library of symbolic candidate terms far richer than the SE is constructed. Second, the governing terms are isolated from this library by sparse regression. Third, the coefficients of the retained terms are refined with an AdamW optimizer to maximize accuracy and form an analytical equation. Experiments on Fair-Rite 78, 79, and 95 yield test mean absolute percentage errors of 1.89%, 1.01%, and 1.56%, respectively, with only 10, 10, and 7 active terms. Comparisons with empirical, numerical, and symbolic models quantify the resulting balance of accuracy and compactness. SSI thus provides an explicit and physically guided approach for high-frequency magnetic characterization and design.

---


### 37. [Benchmarking Segmentation Models for Scalable Mangrove Mapping with Sentinel-1/2 Imagery](https://arxiv.org/abs/2611.33369)

**<font color=#1a73e8>作者：</font>** Damba Koné, Sara Mobsite, Joris Guérin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mangroves are dynamic coastal ecosystems that contribute to carbon storage, coastal protection and biodiversity conservation, but are vulnerable to climate change. Very-high-resolution imagery such as Pléiades enables detailed mangrove mapping but it is costly and have a low revisit rate. Large-scale monitoring requires free and regularly available data such as Sentinel-1 and Sentinel-2 but their spatial resolution poses challenges for detailed mangrove mapping. In this work, we benchmark deep learning approaches for mangrove mapping from Sentinel-1 radar and Sentinel-2 optical imagery using reference maps derived from very-high-resolution Pléiades imagery. We compare four segmentation configurations based on CROMA and BigEarthNet-pretrained ResNet50 representations with different segmentation decoders. We construct a mangrove mapping dataset covering French Guiana, Suriname, and Amapá. CROMA + UPerNet achieves the best performance, with an F1-score of 0.9218 and an IoU of 0.8549. These results highlight the potential of pretrained multimodal Earth observation representations and open Sentinel data to support mangrove resilience through scalable monitoring.

---


### 38. [MotifFlow: Training-Free, Self-Contained Style Transfer from Color to Motif in Rectified Flow Transformers](https://arxiv.org/abs/2611.33371)

**<font color=#1a73e8>作者：</font>** Chun Xie, Itaru Kitahara  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Expressive style transfer must reproduce a painting's palette, brushwork, and characteristic motifs while retaining the content image's structure. Attention injection is effective in U-Net-based diffusion models, but adapting it to FLUX often transfers color without capturing the style's distinctive brushwork. Our analysis across backbones links this gap to how injected features are integrated across neighboring spatial locations. We introduce MotifFlow, a training-free, self-contained framework that combines style injection with style-alignment guidance in FLUX. Injection supplies style features during generation but does not explicitly encourage the model's native attention output to align with them. We therefore use the discrepancy between native and injected attention outputs to guide latent-space updates, encouraging the evolving image to develop the style's distinctive brushwork and motifs. Style encoding, guidance, and synthesis all use the same frozen backbone, without auxiliary image encoders or trained adapters. A single strength parameter controls the transition from color transfer to pronounced brushwork and motifs, with additional support for regional stylization and style mixing. Experiments on 1,000 content-style pairs show that MotifFlow better matches the local textures of the style image than baseline methods and produces more consistent stylization than injection alone. The same design extends to FLUX.2.

---


### 39. [From Conversations to Commitments: A Design Study of Shared Records for Agent-to-Business Coordination](https://arxiv.org/abs/2611.33373)

**<font color=#1a73e8>作者：</font>** Carlos Eberhardt, Mansura Habiba  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Business commitments require accepted terms to be linked to delegated authority, reserved resources and durable evidence. We examine how a shared, attributable interaction record can support these links across independently operated organisations. Talea combines signed AT Protocol records with A2A task execution. We use its coordination sandbox and a proposed commercial extension in a design study of an airline booking disrupted passengers into three competing hotels. Four observations follow. First, AT Protocol provides mechanisms supporting five of six coordination requirements, while record-level access and release controls require additional enforcement. Second, the case's confidentiality constraints restrict each hotel's authorised view to its bilateral exchange; only the airline can correlate all three deals. Third, this leaves a possible benefit for late-joining participants inside the airline's trust boundary, but does not establish an advantage over an equally instrumented point-to-point design. Fourth, a deterministic release interface constrains fixed, approved payloads but cannot bound disclosure when negotiated values depend on private state. Finite-model explorations and deterministic interface checks reproduce the specified behaviours and counterexamples when selected controls are removed. They do not measure comparative benefit or validate a deployed commercial system. The remaining hypothesis is that, within one trust boundary, shared records improve decision reconstruction and recovery under changing participation relative to point-to-point exchange with equivalent authority, reservation, retention and correlation evidence. We specify an experiment to test it.

---


### 40. [VersionGS: Compact and Motion-Robust Dynamic Gaussian Splatting via Versioned Gaussians](https://arxiv.org/abs/2611.33374)

**<font color=#1a73e8>作者：</font>** Shihang Wei, Yichi Zhang, Fengqing Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent dynamic Gaussian splatting methods encode temporal change, either as smooth functions of time or as constrained updates between frames. We observe that their reconstruction quality degrades significantly under fast motion. In challenging dance sequences, their PSNR drops by 1.1-4.0 dB on high-motion frames compared to low-motion frames. To overcome this limitation, we propose VersionGS, a method that directly encodes per-frame Gaussian states and uses motion estimation only to guide reconstruction. Within each group of frames, unchanged Gaussians keep their current versions in a shared dictionary, while modified Gaussians are appended as new versions. To maximize version reuse, we introduce selective sequential construction, which refines the Gaussians selected by optical flow, photograph differences or rendering errors and leaves the others unchanged. The dictionary is then pruned, fine-tuned with simulated quantization and encoded as images. Adjusting the pruning ratio trades off storage and quality without rebuilding the dictionary. On the fast dance sequences of DanceNet3D, VersionGS improves foreground PSNR by 2.7 dB over the best baseline, and its PSNR decreases by less than 0.3 dB on the highest-motion frames. On N3DV and Technicolor, it requires 6.0x and 5.7x less storage than TAD-GS, the strongest baseline overall, while achieving even higher PSNR. Finally, playback is fast and requires no motion model or neural network, only a 3DGS rasterizer.

---


### 41. [DreamTour: Layout Steering for Training-Free World Exploration](https://arxiv.org/abs/2611.33378)

**<font color=#1a73e8>作者：</font>** Srikumar Sastry, Meher Gitika Karumuri, Chenqi Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion and world models generate plausible videos but do not reliably match the requested camera direction and travel distance. We present DreamTour, a training-free framework that generates camera tours from a single image with more accurate control over camera motion. DreamTour first uses a frozen image inpainting prior to extend the photograph beyond its original field of view while preserving the input pixels. Depth-based rendering of this extended scene along the requested camera path produces approximate target views that serve as spatial guidance. We introduce Layout Steering, which aligns early video latents with these views through decaying low-frequency corrections, leaving later denoising to refine appearance and dynamics. For longer tours, we autoregressively generate the video segments, repeating guidance construction from each segment's final frame to maintain camera control across the full trajectory. DreamTour improves directional accuracy and travel calibration on VBench while maintaining competitive video quality. On WorldScore, it strengthens camera control and scene consistency across chained movements. Together, these results demonstrate that training-free spatial guidance enables more accurate and consistent camera control in pretrained video diffusion and world models.

---


### 42. [ArtTet: Watertight Part Meshes of Articulated Objects from Rigid-Body Rules and Partitioned Marching Tetrahedra](https://arxiv.org/abs/2611.33382)

**<font color=#1a73e8>作者：</font>** Sylvia Yuan, Dan Wang, Ravi Ramamoorthi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present ArtTet, a method that reconstructs an articulated object from multi-view observations of two articulation states and outputs one watertight mesh per rigid part together with the joints that move them. Mesh splatting gives explicit triangles, but it treats the object as one scene. It extracts a single global surface and cannot keep the triangles of different parts apart; the mesh it exports is layered, self-intersecting, and full of holes. ArtTet follows a divide-and-conquer strategy instead. We first divide the object into rigid parts with dynamic- and geometric-constrained articulation and ownership inference. A multibody registration of the two states recovers the parts and their screw joints. Rigid-body rules on attachment, contact, and swept motion then correct joint types and part labels without any part annotation. We then divide space into part cells with an articulated tetrahedral partition, and conquer each cell with its own differentiable signed distance field on a shared tetrahedral grid. In these partitioned marching tetrahedra the fields are mutually exclusive by construction, so the extracted part meshes are closed and never overlap. All part meshes are optimized jointly from the images of both states through the recovered joints. On Articulate-100, ArtTet gives the most accurate axis directions, part motions, and part geometry over all objects among methods that use no part masks, and its part meshes have virtually no open boundary edges. We also show reconstructions of real captures from the SplArt dataset.

---


### 43. [BreathSplat: Grounding One Smooth Motion in the Breathing Phase for 4D Cone-Beam CT](https://arxiv.org/abs/2611.33392)

**<font color=#1a73e8>作者：</font>** Sujong Shin, Sang-Il Choi, Kwang Moo Yi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Four-dimensional cone-beam computed tomography (4D-CBCT) images the anatomy of a breathing patient, but sees each breathing phase from only a few angles. Breathing, however, is a smooth motion that repeats; it has a phase. Existing methods exploit this either by reconstructing the anatomy as a function of the breathing phase, often through bins, or by estimating smooth dynamic motions in time. Yet none of these grounds one smooth motion in the phase. We thus propose to share projections across breathing phases with splines. Specifically, we represent the 4D volume with dynamic Gaussians whose motion uses B-splines in space and time. We ground the motion state in the respiratory phase, which we read from well-studied conventional surrogates. Projections at the same phase in different breathing cycles then constrain the same anatomy and motion. On simulated lung scans, our method, BreathSplat, outperforms recent dynamic methods in reconstruction and motion accuracy, including those given the ground-truth phase. We further show qualitatively, on two real patient scans, that our method provides clearer reconstructions than the state of the art.

---


### 44. [Federated Learning with Uncertainty Quantification on Pseudo Label Exchange](https://arxiv.org/abs/2611.33395)

**<font color=#1a73e8>作者：</font>** Jingqiao Tang, Phuoc-Toan Huynh, Richard Archibald 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we investigate federated stochastic operator learning for stochastic partial differential equations (SPDEs), with an emphasis on heterogeneous client data distributions and uncertainty quantification. Federated learning enables clients to collaboratively train models without exchanging their original solution data, but conventional federated averaging can suffer significant performance degradation when client distributions differ, particularly when their input function supports are disjoint. To address these challenges, we propose the Federated Stochastic Operator Network (FedSON), a two-phase framework that combines auxiliary data construction with stochastic operator learning. In the first phase, locally trained deterministic neural operators and their corresponding input functions are exchanged to generate pseudolabeled auxiliary data, enabling the federated model to learn across heterogeneous input distributions without sharing original solution trajectories. In the second phase, a stochastic operator network is trained on top of the frozen deterministic operator to characterize stochastic fluctuations and quantify uncertainty in the predicted solutions. Numerical experiments involving the heat equation, viscous Burgers' equation, and two-dimensional advection-diffusion equation demonstrate the FedSON substantially improves deterministic prediction accuracy under heterogeneous client distributions while producing uncertainty estimates comparable to those obtained through centralized training.

---


### 45. [Sequentially Acquiring Concept Knowledge to Guide Continual Learning](https://arxiv.org/abs/2611.33399)

**<font color=#1a73e8>作者：</font>** Shivanand Kundargi, Kowshik Thopalli, Tejas Gokhale  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The goal of continual learning (CL) is to adapt to new data (plasticity) while retaining the knowledge acquired from old data (stability). Existing methods are explicitly designed to focus on balancing stability and plasticity to mitigate the challenge of catastrophic forgetting while promoting learning. However, the impact of order and nature of samples from the new data that the network is trained on remains an under explored factor. We argue that a CL algorithm should have the ability to rank incoming samples in terms of their relationship with prior data and their effect on the learning process. In this work, we investigate if scoring and prioritizing incoming data based on their semantic relationships with the model's current knowledge can benefit CL. We propose SACK, short for Sequentially Acquiring Concept Knowledge, a plug and play technique for continual learning methods. SACK dissects categorical knowledge of the model into fine-grained concepts, computes the relationships between previously learned concepts and new concepts in each experience, and uses this relationship knowledge for prioritizing new samples. Experiments across several types of CL methods (regularization, replay, and prompt based) in class incremental and task incremental settings demonstrate that integration of SACK not only improves accuracy and reduces forgetting but also handles long tail distribution, helps focus on semantically interpretable regions, and yields better calibrated and robust models compared to prior approaches.

---


### 46. [ArtKit: Motion-Driven Re-Segmentation and Link Re-Generation for Articulated Objects from RGB-D Video](https://arxiv.org/abs/2611.33403)

**<font color=#1a73e8>作者：</font>** Sylvia Yuan, Dan Wang, Vivian Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An RGB-D camera that films an object being moved, often from one viewpoint, sees one side of it and how its parts move. We present ArtKit, which takes such a video as input to create an articulated model with complete parts, a kinematic tree, and typed joints. Our central idea is generating the hidden geometry and verifying it against what the camera sees. A generative part prior proposes complete, part-decomposed geometry based on the first frame. Point tracks, grouped into rigid trajectories, split and merge the generated parts into links. We then fit revolute and prismatic joints, with a visibility-aware energy ensuring that the articulated model explains the depth observed across the video. A rule checks against the video to choose between synchronous group fits and per-frame chain fits, so that one pipeline serves a diverse range of articulated objects, such as household items and robotic hands. Finally, we regenerate each link of the chosen fit as one part and keep it wherever it agrees better with the observations. We evaluate on Articulate-100 and on HArt, a new benchmark of 60 PartNet-Mobility objects and 8 robotic hands and grippers rendered as RGB-D videos with ground-truth parts and joints. ArtKit reduces the axis and part motion errors of the strongest baseline by more than half on the objects, as well as the axis error on the hands. ArtKit also runs on real recordings and generated videos.

---


### 47. [Temporal Selective Exploration for Reinforcement Learning-Guided Continuous-Discrete Flow Matching in 3D Molecular Design](https://arxiv.org/abs/2611.33417)

**<font color=#1a73e8>作者：</font>** Lianghong Chen, Yan Yi Li, Gen Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching has shown strong potential in generative tasks, while its optimization via Reinforcement Learning (RL) remains underexplored, especially in continuous-discrete mixed settings. Moreover, flow matching is formulated as an Ordinary Differential Equation (ODE), whose deterministic trajectories do not naturally support RL optimization. Introducing stochasticity by converting the entire trajectory into a Stochastic Differential Equation (SDE) is a common practice. Nevertheless, not all timesteps contribute to the final outcomes, and redundant exploration introduces additional noise. Furthermore, in multi-objective settings, some objectives may dominate the optimization while others receive insufficient updates. In this study, we propose an RL-guided continuous-discrete flow matching framework with temporal selective exploration for 3D de novo molecular design. Specifically, our method jointly optimizes continuous and discrete flow matching for atomic coordinates and molecular identities, respectively, while restricting exploration to timesteps that primarily contribute to target properties, reducing ineffective exploration. We also introduce a reward-based advantage calibration mechanism to mitigate objective dominance in multi-objective optimization. The framework is applied to design inhibitors for both the well-studied target protein EGFR and the challenging Pin1 protein. We identify some novel candidate inhibitors, supported by in silico validation.

---


### 48. [Yet Another Concept Drift Benchmark? A Principled Framework for Evaluating Drift Detectors](https://arxiv.org/abs/2611.33424)

**<font color=#1a73e8>作者：</font>** Lorenzo Iovine, Giacomo Ziffer, Emanuele Della Valle  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept drift detection is a fundamental component of data stream learning, yet its empirical evaluation remains based on loosely defined protocols, ambiguous alarm semantics, and inconsistent metrics. We propose a principled benchmark grounded in an explicit formulation of drift observability and alarm semantics. Our framework introduces finite detection windows and repeated alarms, enabling a clear separation between detection accuracy, timeliness, and stability, and employs a reproducible observer to provide a controlled and interpretable performance signal. Building on this formulation, we define normalized evaluation metrics and a composite score addressing limitations of existing measures. We validate the framework through a large-scale stress-testing evaluation of 10 detectors across 9 learner configurations and 16 datasets.

---


### 49. [Anatomy-Aware Pseudo-Labels and Homotopy-Annealed Hausdorff Supervision for Semi-Supervised Pancreas Segmentation](https://arxiv.org/abs/2611.33425)

**<font color=#1a73e8>作者：</font>** Alireza Kheyrkhah, Amir Hossein Saleknia, Reza Azad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Confidence-gated co-training assumes that pseudo-label errors are uncertain and concentrated at organ boundaries. We argue that for pancreas CT, where the target organ is a single connected structure and detached fragments are anatomically implausible, the dominant failures arise at three levels: where the organ is, what its boundary should look like, and how a correct boundary is penalized. Anatomical Rectification relabels implausible fragments of a teacher prediction as confident background, without adding any loss or parameter; an audit confirms that its rejections are overwhelmingly detached hallucinations and that thin, tail-like slices are not eroded. Boundary Grafting transplants labelled surface regions with their annotation into unlabeled volumes, replacing unreliable boundary pseudo-labels with ground truth. The residual error is coherent surface displacement, weakly penalized by permutation-invariant Dice and cross-entropy losses. Homotopy-Annealed Hausdorff (HAH) supervision anneals a distance-weighted penalty from an annotation-anchored objective that is convex in the prediction to a Hausdorff surrogate, admitting the prediction-dependent distance term only after the predicted surface becomes reliable. On NIH pancreas CT, under the standard semi-supervised split, the full method reaches 84.60% Dice and 4.97 voxels 95HD, improving all four metrics over compared methods; on MSD Task07, 78.90% Dice and 4.19 voxels 95HD. We further contribute PanTS-SSL, a semi-supervised evaluation protocol derived from the public 9,901-case PanTS corpus, with a curated 1,015-volume main pool, labelled tiers of 50, 100 and 250 volumes, an 80-case tumor track, shift probes for acquisition and anatomy change, and a fixed 901-volume test set. On it, the method exceeds the co-training baseline at 100 labels, scales to 85.29% Dice at 250 labels, and reaches 85.50% Dice at 100 labels with HAH.

---


### 50. [Open-Source FUTO Keyboard Layouts and Predictive Text for a Few Endangered Languages](https://arxiv.org/abs/2611.33432)

**<font color=#1a73e8>作者：</font>** Mika Hämäläinen, Jack Rueter, Khalid Alnajjar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present open-source FUTO Keyboard layouts and predictive text dictionaries for five endangered Uralic languages: Erzya, Moksha, Komi-Zyrian, Livonian, and Skolt Sami. Existing Divvun Android keyboard layouts are converted automatically into the YAML format used by FUTO Keyboard. For predictive text, we construct weighted AOSP dictionaries using translated Finnish lemma frequencies together with morphological frequencies extracted from small target-language corpora using finite-state transducers. This combination provides a practical way to rank inflected word forms when large monolingual corpora are unavailable. The resulting resources offer reusable mobile keyboard support for endangered Uralic languages.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-314](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
