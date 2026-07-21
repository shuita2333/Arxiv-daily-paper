# 📦 其他研究 | 2026年07月22日

> 本类共 **386** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-386](./part-08.md)

---

### 151. [Certified-Gap Dual-Price Policies for Real-Time Truckload Bid Acceptance with Relocating, Clock-Constrained Resources](https://arxiv.org/abs/2607.16891)

**<font color=#1a73e8>作者：</font>** Aswin Chandrasekaran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A truckload carrier must accept or reject each load tender within seconds. The decision depends on fleet state, hours-of-service (HOS) clocks, and appointment windows. We model this as a weakly coupled dynamic program in which the resources relocate and carry clocks: serving a request moves the truck to a new market and depletes its clocks, and whether a truck can serve a request depends on its state. Occupancy-based reusable-resource models do not cover this setting. We build a real-time dual-price policy from the same Lagrangian relaxation that gives the problem's upper bound. Policy and bound come from one object, so every run reports a certified optimality gap. We prove three things. First, the certificate is valid for any duals, any discretization, and any surrogate quality. Second, the policy's same-time spatial-gradient rule is exactly fluid complementary slackness, and the policy is asymptotically optimal in the subcritical fluid regime; the fitted prices are also portable across sample paths, by linear-programming basis stability. Third, certificates have limits: per-resource Lagrangian slack can stay bounded away from zero at every fleet size. We exhibit a three-truck kernel with an exact rational certificate and a replication lemma. On a public closed-loop benchmark with thirty paired seeds, the policy -- which needs no rollout labels, only one offline dual solve -- beats a rollout-trained surrogate on two of three scenarios (tight: +2.0 pp, 95% CI [+0.5, +3.6], Wilcoxon p = 0.023; mild: +3.5 pp, CI [+2.4, +4.5]) and ties the third. It decides in 0.04-0.09 ms, three orders of magnitude faster than the Monte Carlo rollout teacher. Its certificates are stable across ten bounded instances per scenario, at 57-64% of optimal, within 3-6 points of what the 1000x-slower teacher certifies.

---


### 152. [TVGL-CFM:Generating and Forecasting Time-Varying Trajectories of Dynamic Networks with Conditional Flow Matching](https://arxiv.org/abs/2607.16894)

**<font color=#1a73e8>作者：</font>** Om Roy, Yashar Moshfeghi, Keith Malcolm Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many complex systems such as brain networks, financial markets, and gene-regulatory circuits are described not by a fixed graph but by one that changes over time. A standard way to summarise such structure at each instant is the sparse precision (inverse-covariance) matrix, and the time-varying graphical lasso (TVGL) turns a multivariate signal into a smooth chain of these matrices. We introduce TVGL-CFM, a single model that learns the distribution of such chains and can both generate new, realistic time-varying network trajectories for a given class and forecast how an observed trajectory will continue. Each precision matrix lives on a curved space of positive-definite matrices, but a log-Euclidean chart flattens an entire trajectory into an ordinary vector space, so a simple conditional flow-matching model can be trained and sampled there while every decoded matrix is guaranteed to be a valid precision matrix. For forecasting we start the flow not from noise but from a rough extrapolation of the recent history, so the model only has to learn a small correction. Across EEG motor-imagery, chaotic systems, and gene-expression data, TVGL-CFM generates trajectories that keep the class-discriminative structure of real data, and it forecasts future connectivity more accurately than raw-signal baselines. Generating the structured precision trajectory directly is therefore more faithful than generating raw signals and estimating connectivity afterwards.

---


### 153. [When Can Safe Controllers Adapt? Information before Commitment](https://arxiv.org/abs/2607.16895)

**<font color=#1a73e8>作者：</font>** Venkatesh Saligrama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe adaptive control is online adaptation under a safety guarantee on the learning trajectory itself. The controller may use any causal, history-dependent rule and act differently across environments as data arrive. Only its safety guarantee is uniform: the same rule must satisfy it under every initially plausible model. Performance is measured against a safe oracle that knows the realized model. Many finite-time analyses assume persistent excitation of the uniformly safe closed loop, so the data distinguish every pair of models requiring different control decisions. Under that assumption, feasibility is already settled; only the rate remains. We ask instead: Do the safety constraints permit such an informative experiment at all?
While an alternative remains plausible, the controller must preserve a safe continuation under it. We call the first action that forecloses such a continuation commitment. Chance safety allows commitment only on an event rare under the alternative, and the evidence must arrive beforehand: the observation generated by the committing action is too late. We define precommitment information as the KL divergence between learner-visible laws stopped before commitment.
Our main result is a causal reduction. The commitment rule determines (1) the probability that safety permits commitment under the alternative, (2) the target-side cost of remaining noncommittal, (3) and the information available when the decision is made. Bounded precommitment information therefore leaves a fixed fraction of the oracle gap unavoidable. If the gap is {\Omega}(T), every uniformly safe policy has linear regret. We establish the obstruction in a constrained linear system with quadratic regulation cost. We also prove recovery in special cases and derive semidefinite upper certificates for deterministic linear-Gaussian systems.

---


### 154. [Enhancing Personalized Bladder Cancer Treatment Through Reinforcement Learning: A Recurrent Patient State Transition Decision Support Framework](https://arxiv.org/abs/2607.16916)

**<font color=#1a73e8>作者：</font>** Divyansh Chawla, Anshu Garg, Isshaan Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bladder cancer treatment requires personalized and adaptive decision-making, particularly for recurrent disease, where treatment effectiveness changes across successive clinical episodes. Conventional clinical decision support systems typically rely on static treatment guidelines or single-step predictive models, limiting their ability to capture disease progression over time. This paper presents a recurrent patient state-transition simulation framework for bladder cancer treatment planning that integrates predictive state-transition modeling with a Markov Decision Process (MDP) and a Deep Q-Network (DQN) reinforcement learning environment. The predictive module estimates changes in tumor characteristics following treatment, while the reinforcement learning agent sequentially optimizes treatment decisions by interacting with simulated patient trajectories. This framework enables dynamic, patient-specific treatment planning by continuously adapting recommendations to evolving clinical states. It also generates interpretable treatment trajectories and detailed simulation logs to improve transparency and support clinical decision-making. The proposed framework was evaluated against existing reinforcement learning-based treatment planning approaches. It achieved a cumulative reward of 63,918.87, an average training loss per episode of 0.0056, and a policy improvement score of 6.62%, demonstrating effective sequential learning and robust treatment optimization in a simulated recurrent treatment environment. These findings highlight the potential of recurrent patient state-transition simulation with reinforcement learning as a flexible decision-support framework for personalized bladder cancer treatment planning and AI-assisted precision oncology.

---


### 155. [Pedestrian Archetypes Extension -- More Pedestrian Models for Autonomous Vehicle Safety Testing](https://arxiv.org/abs/2607.16922)

**<font color=#1a73e8>作者：</font>** Taorui Huang, Namita Gaidhani, Ritvik Bansal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In our prior work, Pedestrian Archetypes, we defined pedestrian archetypes as collections of behaviors that uniquely identify a specific type of pedestrian. The first paper proposed 12 pedestrian archetypes, including the Wanderer, Drunk, Distracted, Flash, Indecisive, Blind, Flock, Jaywalker, Elderly, Kid, Eventful, and Parked Pedestrian. These archetypes were introduced to move beyond single behavior labels and provide a more natural way to describe how dangerous pedestrians actually behave progressively in real-world traffic scenarios. However, upon further annotation of YouTube dash-cam videos, we identified 7 additional pedestrian archetypes with observable and significant behavioral differences from the previously proposed ones. These new archetypes capture pedestrian behavior patterns that could not be fully explained by the original taxonomy. In this pre-print, we introduce each new archetype, define its essential and optional behaviors, explain how it differs from previously proposed archetypes, and provide video-frame evidence showing the archetype in action.

---


### 156. [Splat-based 3D Scene Reconstruction with Extreme Motion-blur](https://arxiv.org/abs/2607.16926)

**<font color=#1a73e8>作者：</font>** Hyeonjoong Jang, Dongyoung Choi, Donggun Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a splat-based 3D scene reconstruction method from RGB-D input that effectively handles extreme motion blur, a frequent challenge in low-light environments. Under dim illumination, RGB frames often suffer from severe motion blur due to extended exposure times, causing traditional camera pose estimation methods, such as COLMAP, to fail. This results in inaccurate camera pose and blurry color input, compromising the quality of 3D reconstructions. Although recent 3D reconstruction techniques like Neural Radiance Fields and Gaussian Splatting have demonstrated impressive results, they rely on accurate camera trajectory estimation, which becomes challenging under fast motion or poor lighting conditions. Furthermore, rapid camera movement and the limited field of view of depth sensors reduce point cloud overlap, limiting the effectiveness of pose estimation with the ICP algorithm. To address these issues, we introduce a method that combines camera pose estimation and image deblurring using a Gaussian Splatting framework, leveraging both 3D Gaussian splats and depth inputs for enhanced scene representation. Our method first aligns consecutive RGB-D frames through optical flow and ICP, then refines camera poses and 3D geometry by adjusting Gaussian positions for optimal depth alignment. To handle motion blur, we model camera movement during exposure and deblur images by comparing the input with a series of sharp, rendered frames. Experiments on a new RGB-D dataset with extreme motion blur show that our method outperforms existing approaches, enabling high-quality reconstructions even in challenging conditions. This approach has broad implications for 3D mapping applications in robotics, autonomous navigation, and augmented reality. Both code and dataset are publicly available on this https URL.

---


### 157. [Pediatric Bone Age Prediction Using Deep Learning](https://arxiv.org/abs/2607.16936)

**<font color=#1a73e8>作者：</font>** Al Zadid Sultan Bin Habib, Md. Ekramul Islam, Md Asif Bin Syed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pediatric bone age prediction is a crucial task in clinical practice that can help diagnose endocrine disorders and provide insight into a child's growth and development. However, conventional bone age prediction methods are often labor-intensive and require specialized radiological expertise. This paper presents a Deep Learning (DL)-based approach to pediatric bone age prediction using EfficientNet with Additive Attention, a state-of-the-art neural network architecture for image classification and regression tasks. The method utilizes over 12,000 X-ray images from the RSNA bone age dataset. It involves image preprocessing, transforming them into three-channel images, and training a Convolutional Neural Network (CNN) to automatically learn the features of hand bone images. This approach provides a more effective and accurate solution for predicting bone age, which is critical in diagnosing pediatric endocrine diseases. This work uses two variations of the EfficientNet model (B0 and B4), where EfficientNetB4 is also finetuned with the Additive Attention mechanism. These three models predict the age for the original age, and their comparison is shown in curves. The predicted ages depict that in most cases, EfficientNetB4 and EfficientNetB4 with Additive Attention (EN-AA) successfully predicted the bone ages more accurately regarding the original age, and their performance was better than the EfficientNetB0. Specific performance metrics are provided to underscore this improvement. Learning curves for training and validation loss confirm effective learning without overfitting or underfitting, further validating our approach's efficacy in pediatric endocrine disease diagnosis.

---


### 158. [What Do They See? Interpreting Complex Road Scenarios Through the Eyes of Vision-Language-Action Models for Safe and Trustworthy Autonomous Vehicle Learning](https://arxiv.org/abs/2607.16938)

**<font color=#1a73e8>作者：</font>** Kalpana Panda, Wesley Maia, Vinti Agarwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end autonomous driving models are now able to navigate complex road scenarios, mapping raw sensor observations directly to observed paths for open-loop evaluation and often effective driving in closed-loop evaluation. Yet the internal logic of these safety-critical systems remains largely opaque, due to the complexity of traffic scenes. We propose a counterfactual ablation framework called Counterfactual Vision Action Analysis (CVAA) that systematically removes individual detected objects from front-camera images using photorealistic generative inpainting to prepare counterfactual sets to evaluate the difference in the model's response. This isolates the causal effect of each object's presence on the model's planning behaviour. Applied to the Alpamayo 1 trajectory predictor across 210 nuScenes driving scenes, we create a dataset Counter -nuScenes, using which we see that vehicles and pedestrians within the model's 'path' dominate causal influence as expected, while traffic lights, as expected, exert disproportionate effect relative to their image footprint. However, we also find cases where the model responds strongly to objects a human driver would consider irrelevant. This brings forth a deeper question: does the model itself view the scene as a sum of individual objects influencing the outcome, or does it encode an entirely different set of internal features that do not correspond to human-legible scene elements? To further understand this, we compare intermediate representations of original and inpainted image pairs using mechanistic interpretability techniques and examine the effect of the removal through the various model layers. Together, these two stages offer a path from behavioral auditing to representational understanding, creating explainable driving systems and solidifying human-AI trust.

---


### 159. [Investigation of Polycystic Ovary Syndrome (PCOS) Diagnosis Using Machine Learning Approaches](https://arxiv.org/abs/2607.16941)

**<font color=#1a73e8>作者：</font>** Al Zadid Sultan Bin Habib, Md Asif Bin Syed, Md. Ekramul Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Polycystic Ovarian Syndrome (PCOS) is a widespread hormone problem for women of childbearing age. Women with PCOS may not ovulate; they might have high levels of androgens and have many small cysts on the ovaries. It can cause missed or irregular menstrual periods, excess hair growth, acne, infertility, and weight gain. Machine Learning (ML) can effectively diagnose this disease at an earlier stage as tons of medical data are available now. Traditional approaches to detect PCOS encompass a combination of clinical evaluation, medical history assessment, physical examination, and laboratory tests. These approaches aim to identify the characteristic symptoms and hormonal imbalances associated with PCOS. Physical examination requires good resources and costs time and money. In recent times, data-driven techniques have substantially advanced disease prediction within the medical field. We aim to utilize ML approaches, incorporating unique feature selection algorithms, to predict PCOS. This paper introduces a data-driven approach to PCOS diagnosis, combining Feature Engineering and ML. Several feature selection approaches have been considered to select sets of features for training the ML model, including CatBoost, Extreme Gradient Boosting (XGBoost), Light Gradient Boosting Machine (LGBM), AdaBoost, Random Forest (RF). Results demonstrate that AdaBoost, with ten features selected by RF Feature Importance and Highest Correlation (HC), provides the highest test accuracy.

---


### 160. [When Physical Preferences Meet Semantic Constraints: Physical and Semantic Direct Preference Optimization for Text-to-Video Generation](https://arxiv.org/abs/2607.16947)

**<font color=#1a73e8>作者：</font>** Siwei Meng, Yawei Luo, Shu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) generation models have achieved strong visual realism, but improving physical plausibility can come at the cost of semantic consistency with the input text. This tension arises because physical preference is typically determined by comparing dynamics between two videos, without accounting for whether either video faithfully depicts the scene specified by the prompt, making physical-semantic conflict a systematic tendency under this supervision paradigm. We formulate this challenge as a constrained preference optimization problem and propose Physical and Semantic Direct Preference Optimization (PSDPO), which modulates each preference pair's contribution based on the agreement between its physical and semantic signals. A gradient-level analysis shows that PSDPO bounds the semantic drift from conflicting pairs to a controllable residual, and further motivates a staged optimization protocol that provably reduces cumulative drift. The resulting method operates entirely within the standard DPO framework, requiring no auxiliary models or additional loss terms. Experiments show that PSDPO improves physical plausibility by up to $2\times$ over the baseline on VideoPhy-2, while maintaining strong semantic consistency on VBench, achieving a more reliable balance than existing preference-based methods.

---


### 161. [Rollback-Free Cross-Chain Atomicity Through Forward-Only Correction](https://arxiv.org/abs/2607.16959)

**<font color=#1a73e8>作者：</font>** Tahrim Hossain, Faisal Haque Bappy, Tarannum Shaila Zaman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchain platforms have grown into an ecosystem of independent networks, and a growing class of applications now requires smart contracts on separate chains to act as one. Such operations must be atomic, yet immutability makes this fundamentally harder: a confirmed transaction cannot be reversed, so the rollback on which classical atomic commitment protocols depend is unavailable. Two challenges follow. Contract state must be held across an operation whose outcome is not yet known, and each chain's execution outcome must be established even though no chain can observe another. In response, we introduce a framework that achieves atomicity through forward-only correction, resolving incomplete operations with new on-chain transactions rather than reversal. The framework bounds how long contract state is held and confines contention to the state an operation touches, and it establishes outcomes from an on-chain record of what each chain executed, without relying on any single coordinating party. This work lays the foundation for atomic coordination of general smart contract operations across heterogeneous blockchains.

---


### 162. [Adaptive Incident Prioritization for Security Operations at Scale](https://arxiv.org/abs/2607.16963)

**<font color=#1a73e8>作者：</font>** Scott Freitas, Amir Gharib, Maayan Magenheim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large security operations centers (SOCs) often face hundreds of active incidents per day, creating substantial cognitive and operational demands for analysts. Analysts must quickly decide which incidents deserve attention within long, constantly changing queues, yet incidents are commonly ordered by arrival time, coarse severity, or product-specific heuristics that leave their relative priority unclear. We introduce Adaptive Incident Prioritization (AIP), the ranking algorithm behind Microsoft Defender Queue Assistant, which continuously prioritizes security incidents for analyst investigation. AIP adapts BM25-style ranking to a query-less, multi-tenant queue setting by representing each incident as a collection of normalized security components extracted from alerts and metadata. The model combines saturated local component frequency, global component rarity estimated across tenants, bounded domain-prior multipliers, and component-level explanations. Deployed across tens of thousands of customers, AIP performs near-real-time inference and refreshes incident scores with a median latency of five seconds. In an expert-reviewed evaluation across 1,000 customer organizations, AIP achieves 92.8% Precision@10. In post-launch telemetry across 473,000 organization-day queues, AIP increases alert-detail interaction by 5.8% and alert-detail view events by 17.5% relative to severity ordering, providing behavioral evidence that model-ranked queues concentrate analyst engagement. We also extend the Microsoft GUIDE dataset with, to our knowledge, the first public label source for SOC queue prioritization over real-world incidents. The extension covers 499 organization queues and 9,980 incidents with expert-derived priority labels, enabling the research community to develop, compare, and advance methods for incident prioritization.

---


### 163. [SurvCF(t): Counterfactual Explanations for Survival Analysis in Predictive Maintenance Multivariate Time Series Data](https://arxiv.org/abs/2607.16969)

**<font color=#1a73e8>作者：</font>** Zara Karazian, Panagiotis Papapetrou, Sindri Magnússon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive maintenance relies on accurate Remaining Useful Life estimation, often formulated using survival analysis over multivariate time-series data. While modern deep survival models achieve strong predictive performance, their black-box nature limits their use in safety-critical settings where actionable insight is required. In this work, we introduce \textit{SurvCF(t)}, the first framework for generating counterfactual explanations for survival models operating on time-series data. \textit{SurvCF(t)} identifies minimal, plausible, and temporally consistent changes to an asset's operational history that increase its predicted life time, framing explanation as a constrained optimization problem combining validity, proximity, sparsity, and plausibility. We evaluate the method on multiple benchmarks, including C-MAPSS, N-CMAPSS, and a real-world case study of the Scania Component\_X dataset, demonstrating its ability to produce actionable and interpretable interventions. Our results show that \textit{SurvCF(t)} bridges the gap between survival prediction and prescriptive maintenance, enabling explainable and decision-oriented AI for maintenance strategies.

---


### 164. [Training Continuous Chain of Thought Models: A Tale of Two Regimes](https://arxiv.org/abs/2607.16972)

**<font color=#1a73e8>作者：</font>** Varun Yerram, He He, Eunsol Choi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continuous Chain-of-Thought methods replace verbose reasoning traces with a short sequence of dense latent representations. Earlier continuous CoT methods indirectly supervise the latent representations such that its final state match that of verbose reasoning traces, requiring autoregressive, slow generation during training. We introduce C-MTP, a simpler, faster direct supervision approach that models each latent as an average of the embeddings in the CoT traces to be compressed. Our approach outperforms a prior direct supervision method that approximates the distribution of compressed tokens, and performs competitively to slower indirect supervision approaches in existing evaluation setup with simplified CoT traces (less than 100 tokens). Lastly, we extend the evaluation of Continuous CoT methods to complex tasks with longer reasoning traces ($\ge$ few hundreds reasoning tokens). We find both direct and indirect supervision training methods perform poorly (roughly 65\% performance drop) in this setting, revealing the limitations of current continuous CoT methods. The code and checkpoints are released at this https URL

---


### 165. [Expected Free Energy as Belief-Dependent Utility for rho-POMDPs](https://arxiv.org/abs/2607.16981)

**<font color=#1a73e8>作者：</font>** Patrick Cooper, Alvaro Velasquez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent acting under partial observability must decide when to gather information and which observations are worth their cost. Standard POMDPs value information only through its eventual effect on reward. The $\rho$-POMDP framework instead rewards uncertainty reduction directly, through a belief-dependent utility $\rho$, but in practice both the choice of $\rho$ and the weight placed on it are tuned by hand for every task. We show that active inference removes this tuning entirely. Minimizing Expected Free Energy (EFE) is exactly equivalent to solving a $\rho$-POMDP whose utility is expected information gain, and the exploration weight is fixed at $w=1$ because the variational bound expresses pragmatic and epistemic value in the same units (nats). We prove this equivalence for observe-then-commit POMDPs and extend it to factored observation POMDPs, a broader class that covers interleaved observe-act problems such as non-destructive testing and mobile sensing, where gathering information leaves the hidden state unchanged. Experiments support the theory. Across environments ranging from the classic Tiger problem to RockSample and a new Structural Inspection benchmark with over 65,000 states, the untuned weight matches or outperforms reward-only planning at the same horizon, avoids the over-exploration of bonuses tuned per task, and sits near the reward-maximizing knee of the success-reward Pareto frontier. The practical payoff is an exploration objective that works out of the box. In applications such as fault detection and medical screening, where every test has a price and every missed fault has a cost, EFE supplies a belief-dependent utility that is derived rather than tuned.

---


### 166. [Periodic Bootstrap Thompson Sampling For Periodically Non-Stationary Bandit Problems](https://arxiv.org/abs/2607.16986)

**<font color=#1a73e8>作者：</font>** Boning Shao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces Periodic Bootstrap Thompson Sampling (PBTS), an innovative extension of the classic Thompson Sampling (TS) algorithm tailored for bandit problems with periodic non-stationarity. Conventional TS accumulates all past observations, leading to biased posteriors when reward distributions cycle over time. PBTS overcomes this by synchronizing belief resets with known or inferred period intervals and embedding structured bootstrap exploration phases, effectively purging obsolete data while preserving uncertainty estimates. PBTS is tested in artificially constructed environments, which include skewed and balanced reward distributions, along with different bootstrap proportions and misaligned periodic intervals. Results indicate that PBTS generally achieves statistically significant reductions in cumulative regret against traditional TS in periodic non-stationary environments. Subsequent discussion further articulates the potential of PBTS's real-world deployment. The study mentions limitations like extreme periodic misalignment and proposes future research such as self-adjusting cycle-recognition. With memory reset and bootstrap phase, PBTS introduces a novel approach to optimizing bandit algorithms in periodic reward contexts.

---


### 167. [Real-World Evaluation of an AI Agent Drafting Translational Impact Summaries](https://arxiv.org/abs/2607.16989)

**<font color=#1a73e8>作者：</font>** Mohammad Arvan, Amber E. Osterholt, Bailee Rue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Introduction. Clinical and Translational Science Award (CTSA) programs must document their scholars' research impact, but assembling each scholar's record by hand takes staff an estimated 15 hours and does not scale to a full cohort. An artificial intelligence (AI) agent could serve as a tool to gather scholar data across platforms and disciplines.
Methods. We built a human-in-the-loop AI agent that assembles a dossier of sourced evidence for each scholar and drafts one-sentence Translational Science Benefits Model (TSBM) impact summaries for staff review. We evaluated it in the impact-reporting workflow of one CTSA hub across 10 career-development (KL2/K12) scholars. Two evaluation staff independently coded all 507 findings as accept, edit, or reject; the primary measure was the unanimous usable rate, defined as the share both accepted or edited.
Results. Both reviewers accepted or edited 81.7% of the agent's findings. Reviewers each spent a median of 14 minutes per scholar, replacing an estimated 15 hours of manual assembly. Inter-rater agreement was moderate (Cohen's kappa 0.43 on the usable-versus-reject decision). A profile discovery study found the agent's recall close to human search. The agent's impact evidence spanned all four TSBM domains, and about a third of the reviewed findings fell in non-scholarly categories that routine processes tend to miss. Reviewers rated synthesis accuracy 4.5 and usefulness 4.8 on a 5-point scale.
Conclusions. A human-in-the-loop AI agent can serve as the first-pass author of a scholar's impact record, shifting staff from collecting and writing to reviewing, and making cohort-scale impact reporting feasible.

---


### 168. [Automated Cardiac Adipose Tissue Segmentation in Computed Tomography: A Literature Review](https://arxiv.org/abs/2607.16992)

**<font color=#1a73e8>作者：</font>** Andreas W. Aspe, Jonas Jalili Pedersen, Andreas Ohrt Johansen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This review provides an overview of recent advancements in automated segmentation methods on Computed Tomography (CT) for two types of cardiac fat: Epicardial adipose Tissue (EAT) and Pericardial Adipose Tissue (PAT). These fat deposits, separated by the pericardium, have been linked to various cardiovascular diseases, with EAT receiving the most research attention. Their complex anatomical context makes manual quantification highly time-consuming and prone to considerable inter-observer variability. Automated methods effectively address these complications, offering a more efficient and consistent solution. This study encompasses a broad range of methods, spanning AI as well as non-AI approaches. Additionally, it presents the remaining challenges, including the need for larger annotated public datasets and optimized attenuation thresholds for contrast-enhanced CT. It is demonstrated that automated methods are able to achieve segmentation results comparable to the quality of human annotation, proving their potential as a clinical tool for discovering new biomarkers and enhancing patient outcomes.

---


### 169. [PriorProof: A Point-in-Time Measure of Technique Novelty for Formal Proofs](https://arxiv.org/abs/2607.16997)

**<font color=#1a73e8>作者：</font>** Neel Somani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematicians distinguish proofs that explain, simplify, or introduce a nonstandard route, but these judgments are difficult to operationalize. We study a deliberately narrower construct: time-relative proof-route nonstandardness in formal mathematics. For a Lean theorem, PriorProof extracts the dependency footprint of its elaborated proof term and scores the weighted surprisal of that footprint under a retrieval-conditioned, hierarchically smoothed prior built only from an earlier quarterly snapshot of Mathlib. The method requires no hand-built technique ontology and no human labels: statement retrieval is learned from proof-derived contrastive pairs, while the scored object is read mechanically from proof terms. In a blinded topology study, 100 presentations collapse to 76 distinct underlying pairs: 12 canonical contrasts shown three times for consistency screening and 64 distinct stratified pairs. Against the majority of three retained domain raters, PriorProof agrees on 53/76 pairs (69.7%, Wilson 95% CI 58.7-78.9%), including 11/12 canonical pairs (91.7%, 64.6-98.5%) and 42/64 stratified pairs (65.6%, 53.4-76.1%). Score-gap quartiles are nonmonotone after repeat collapse; the endpoints are 12/19 (63.2%, 41.0-80.9%) in the smallest-gap bin and 16/19 (84.2%, 62.4-94.5%) in the largest, supporting an endpoint-calibration tendency rather than a resolved staircase. The best language-model condition agrees on 60/76 pairs (78.9%, 68.5-86.6%); on paired outcomes, PriorProof alone is correct on 8 pairs and the model alone on 15 (exact two-sided McNemar p = 0.210), so the difference is not established at this sample size. We therefore present PriorProof not as a replacement for expert or model judgment, but as a decomposable, time-anchored signal whose score gap provides an interpretable reliability indicator.

---


### 170. [Counterfactual Shapley Credit Assignment](https://arxiv.org/abs/2607.16999)

**<font color=#1a73e8>作者：</font>** Mingxuan Li, Kaizhan-Lee, Elias Bareinboim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Credit Assignment Problem (CAP) is fundamental to developing efficient and explainable Reinforcement Learning (RL) agents. Existing frameworks, whether relying on temporal contiguity or hindsight-conditioned reward reweighting, frequently fail to attribute properly between an agent's policy (skill) and environmental stochasticity (luck). A principled approach to CAP must isolate the true causal drivers of observed outcomes from spurious correlations and environmental randomness. We introduce Counterfactual Shapley Credit Assignment, a novel framework grounded in causal theory that attributes credit and blame via the Counterfactual Shapley Value ($\phi$-value). By redistributing environmental rewards, $\phi$-values enhance temporal credit assignment across three critical dimensions: sparse causality, high stochasticity, and delayed rewards, all while preserving the optimal policy. We derive a consistent estimator that computes $\phi$-values efficiently, enabling a new class of policy gradient methods, $\phi$-PPO, combined with Prioritized Trajectory Replay (PTR). Empirical results demonstrate that $\phi$-values align precisely to the ground truth causes of task rewards with superior sample efficiency in challenging environments where prior state-of-the-art methods fail to converge.

---


### 171. [Scalable Causal Imitation Learning](https://arxiv.org/abs/2607.17003)

**<font color=#1a73e8>作者：</font>** Eylam Tagor, Mingxuan Li, Elias Bareinboim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imitation learning enables learning a policy in an unknown environment with a latent reward signal using expert demonstrations, but it struggles when the imitator's and expert's observations are mismatched and unobserved confounders are present in expert demonstrations. By identifying appropriate adjustment sets via the sequential $\pi$-backdoor criterion, causal imitation learning (CIL) provides a framework for approximating the expert's policy from confounded data. However, existing CIL methods, Causal Behavioral Cloning (Causal BC) and Causal Generative Adversarial Imitation Learning (Causal GAIL), are designed for short-horizon, low-dimensional settings. When applied to continuous control tasks with long horizons and high-dimensional state-action spaces, these methods exhibit poor performance: Causal BC suffers from compounding errors, Causal GAIL is unstable and sample-inefficient, and sequential $\pi$-backdoor adjustment becomes impractical. We introduce Causal Soft Q Imitation Learning (SQIL) and Causal Inverse soft-Q Learning (IQ-Learn), two off-policy causal imitation learning algorithms that combine the causal adjustment framework with state-of-the-art inverse reinforcement learning objectives. Both algorithms operate on causally-adjusted state representations produced by an efficient approximation of the sequential $\pi$-backdoor criterion, exploiting the causal structure of continuous control environments to reduce the full-horizon adjustment to a fixed-size sliding window. We evaluate all methods in a suite of confounded environments and find that Causal SQIL and Causal IQ-Learn substantially outperform prior CIL algorithms on long-horizon tasks, sometimes surpassing the expert, whereas all causally unaware imitation methods fail to learn meaningful behavior.

---


### 172. [Regularize or Localize: When Training-Time KV-Cache Geometry Pays Under Quantization](https://arxiv.org/abs/2607.17019)

**<font color=#1a73e8>作者：</font>** Libo Sun, Po-Wei Harn, Zewei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study whether \sigreg -- LeJEPA's anti-collapse objective -- can reshape representations during standard autoregressive language-model pretraining, and when the resulting geometry helps \kv-cache quantization. We train 110M-parameter models on 10B FineWeb tokens and report three findings. \textbf{(1)} At $\lambda{=}0.01$, \sigreg reduces hidden-state pairwise-cosine anisotropy by $38\%$ across three paired seeds. Perplexity increases by less than $0.35\%$ in every pair, with no consistent zero-shot loss. \textbf{(2)} This change does not propagate from hidden states to the \kv cache. Applying \sigreg directly to K and V during continued training, however, reduces mean cache anisotropy by $94\%$ across four checkpoints. A matched continuation without the \kv term leaves cache geometry nearly unchanged, and the frozen-trunk retrofits we tested do not reproduce the effect. \textbf{(3)} Under untransformed symmetric group-free quantization, direct \kv regularization is the only training condition that prefers per-channel scaling in all three seeds, and under that same 3-bit per-channel scheme the baseline incurs $4.3$--$7.9\times$ the directly regularized model's \dnll. Under the full simulated KIVI-style configuration (mixed arrangement, zero-points, grouped scales), however, all models reach near-parity, including when storage overhead is approximately matched. In this 110M regime, the training intervention helps when quantizer scales are coarse; the advantage vanishes under the tested combination of token-local grouping, mixed \kv scaling, and zero-points. To our knowledge this is the first training-time \emph{distributional} regularization of standard \kv-cache geometry evaluated against post-hoc cache quantization.

---


### 173. [Interpretable Machine Learning for Air Pollution and Respiratory Health Prediction: A Socioeconomic Subgroup Analysis](https://arxiv.org/abs/2607.17024)

**<font color=#1a73e8>作者：</font>** Maede Azani Hassan Abadi, Shouyi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Air pollution and climate-related stressors are increasingly important concerns for respiratory health, especially in settings with unequal environmental exposure and healthcare capacity. This study evaluates an interpretable machine learning framework for predicting respiratory disease rates and air-quality status using structured country-level weekly data. Two supervised learning tasks were considered: regression of respiratory disease rate per 100,000 population and binary classification of air-quality status. Nine regression models and nine classification models were compared using nested cross-validation. Model interpretation was conducted using SHAP values, and subgroup analysis was performed across income levels and geographic regions. The results showed that PM2.5 concentration was the dominant predictor of respiratory disease rate, with linear and regularized linear models achieving the strongest regression performance. For air-quality classification, models achieved high balanced accuracy when PM2.5 was included, but performance decreased substantially when PM2.5 was removed, indicating strong dependence on pollutant-related information. SHAP analysis showed that, without PM2.5, socioeconomic and meteorological variables such as GDP per capita, precipitation, and healthcare access became more influential. Subgroup analysis showed similar aggregate regression error across income groups, but PM2.5 contributed more strongly to predictions in lower-middle-income countries. These results show that model accuracy alone is not sufficient for climate-health prediction. Interpretable models can help identify dominant pollution-related signals, test whether results depend on key pollutant variables, and show whether prediction patterns differ across socioeconomic groups.

---


### 174. [Federated Lightweight Intrusion Detection in Drone Swarms with Knowledge Distillation](https://arxiv.org/abs/2607.17025)

**<font color=#1a73e8>作者：</font>** Fawaz J. Alruwaili, Cihan Tunc  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Drone swarms are increasingly deployed in critical applications such as surveillance, disaster response, and infrastructure monitoring. However, their reliance on open communication channels and their limited computational resources make them vulnerable to a wide range of cyber-threats. There is a growing interest in intrusion detection systems (IDS) specifically designed for drone environments and operations. However, the conventional solutions including Machine Learning (ML)-based approaches require collecting all data from heterogeneous drones in the swarm and processing on a central server may not be always feasible. Federated Learning (FL) has emerged as a promising distributed solution with an additional privacy-preserving feature. Even though potential studies exist, conventional FL-based IDS frameworks still face communication and computational overhead challenges, while achieving a balance between efficiency and effective detection under practical resource constraints remains a challenge. Therefore, we propose a lightweight FL-based IDS tailored for drone swarm networks using deep neural networks (DNN) enhanced with knowledge distillation (KD) to reduce model complexity and communication costs without sacrificing detection performance. We evaluate our framework using Raspberry Pi 4 devices and a real-world drone network dataset. Our approach demonstrates a detection accuracy of approximately 98.6% while reducing overall communication cost by around 70% and computational overhead by 29%. These results show that FL combined with KD is a practical and suitable solution for secure and efficient deployment in resource-constrained drone networks.

---


### 175. [Apeliotes: A Diffusion-Based Modeling Framework for km-scale Multi-Level Atmospheric Fields](https://arxiv.org/abs/2607.17037)

**<font color=#1a73e8>作者：</font>** Evangelia Rafaela Frastali, Achyut Paudel, Maryam Golbazi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-resolution atmospheric data are required to resolve mesoscale and localized meteorological structures, however such datasets remain limited in many regions of the world. Existing high-resolution weather products are typically produced through dynamical downscaling, which is computationally expensive and difficult to scale across locations, variables, and forecast scenarios. These limitations motivate machine-learning-based downscaling systems that can generate multiple weather variables stochastically while producing new high-resolution fields directly. In this paper we present Apeliotes, a framework for high-resolution weather forecasting. Built on the global re-analysis atmospheric data, a pre-trained global weather foundation model, and a regionally trained generative diffusion model, Apeliotes not only provides accurate kilometer-scale weather variables, but also multi-level atmospheric fields which are not directly available in the existing global atmospheric data. Our comprehensive evaluation demonstrates that Apeliotes achieves highly competitive performance. The model predicts vertical wind profile with less than 3\% error between truth and predicted fields, achieving correlations of 0.91 for 10-m wind speed and 0.99 for 2-m temperature, with NRMSE values of 0.42 and 0.17, respectively.

---


### 176. [EvoGUI: An Evolution-Aware Benchmark for GUI State-Transition Understanding](https://arxiv.org/abs/2607.17050)

**<font color=#1a73e8>作者：</font>** Yaohan Yang, Minglei Shi, Borui Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI agents must reason about how actions transform interface states, but end-to-end success rates entangle this ability with perception, grounding, planning, and recovery. We introduce EvoGUI, a diagnostic framework that converts normalized GUI trajectories into three complementary visual question answering probes: temporal ordering, inverse action/value prediction, and contrastive one-step successor discrimination. Their labels are derived from trajectory order and logged actions, requiring no additional task-label annotation after trajectory normalization. We instantiate EvoGUI-Bench from Mind2Web and WebLINX, yielding 3,000 instances across 120 domains, and evaluate 28 vision-language model configurations zero-shot. The strongest model reaches only 60.4 EvoGain, while model scale and GUI specialization do not reliably predict performance. These results establish EvoGUI-Bench as a scalable diagnostic complement to end-to-end GUI-agent evaluation while exposing substantial headroom in state-transition understanding. The source code is publicly available at this https URL.

---


### 177. [High-Capacity Robust Watermarking Technology for High-Resolution Images](https://arxiv.org/abs/2607.17056)

**<font color=#1a73e8>作者：</font>** Shaowu Wu, Wei Lu, Qing Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most existing watermarking techniques are primarily designed for low-resolution images, with few methods tailored for high-resolution images. Moreover, the embedding capacity is often limited to fixed lengths (e.g., 30, 100, 256 bits, etc.), which struggles to meet practical demands. To address these issues, this paper proposes a high-capacity robust watermarking method for high-resolution images, capable of embedding a watermark of 4 KB (32,768 bits) into images with a resolution of 1024*1024, achieving an embedding rate of 0.0313 bpp. Specifically, this paper adopts a block-wise strategy to effectively embed the watermark into local regions, enabling the network to train and learn normally even under low-resource conditions. The encoder and decoder structures respectively employ a reversible symmetric architecture with three convolutional and three deconvolutional layers, ensuring consistency in the coupling and decoupling of the watermark and image features. Additionally, the loss function combines global and local losses with weighted contributions. By incorporating constraints on the visual quality and robustness of local block regions, the overall imperceptibility and robustness of the image are further enhanced. Extensive experimental results verify that the proposed method is effective and feasible in high-resolution image scenarios with high-capacity watermarking, while demonstrating strong robustness against various noise attacks.

---


### 178. [What does a Bayes-filtered transformer believe? A predictive Monte Carlo approach](https://arxiv.org/abs/2607.17060)

**<font color=#1a73e8>作者：</font>** Afiq Abdillah Effiezal Aswadi, Haotong Ma, Susan Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A Bayes-filtered transformer (BFT) is a transformer trained on sequences that are generated in two steps: first a latent task is drawn from a prior, then observations are drawn conditional on that task. Trained under autoregressive log loss, the BFT's next-token prediction, in the idealized limit, is the Bayesian posterior predictive distribution (PPD) induced by that prior and that conditional law. In practice the trained BFT is only an approximation of this ideal PPD, raising an interpretive question: what prior and posterior over the latent task has the trained BFT actually internalized? Existing work answers this question by comparing the trained BFT's predictions against the predictions of various "reference" posteriors, each standing in for a different candidate algorithm or computation the BFT might be implementing. This prediction-space comparison is fragile: different posteriors can share the same posterior-mean predictions. We use predictive Monte Carlo (PMC) as a general interpretability tool for any BFT: using only next-token generation, PMC returns an approximation to the implicit prior and posterior over the latent task, answering the interpretive question directly in latent space. We apply PMC to three stylized task families spanning 0-Markov and 1-Markov exchangeability. The phenomena previously reported in these settings remain visible in latent space. Code is available at this https URL

---


### 179. [AdvSerial: Physical Adversarial Attacks on Infrastructure-mounted Pedestrian Detectors via Semantic Feature Suppression](https://arxiv.org/abs/2607.17069)

**<font color=#1a73e8>作者：</font>** Yuanhao Huang, Yilong Ren, Jinlei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-based visual perception systems are increasingly deployed in infrastructure surveillance, including roadside monitoring units, highway cameras, and smart-city pedestrian management systems. The security vulnerability of these systems to physical adversarial attacks poses a direct threat to the reliable operation of transportation infrastructure. We propose AdvSerial, a dynamic 2D--3D joint optimization framework for generating continuous high-angle physical adversarial patches against pedestrian detectors in infrastructure-based scenarios. We UV-map a boundary-aware quilted texture onto 3D garments, combine 2D digital attacks with 3D sparse- and continuous-frame rendering, and explicitly suppress person-specific semantic features while enforcing temporal continuity. A Feature Smooth Quilting strategy reduces visible patch boundaries and bounds cross-seam feature discontinuities. A serial-frame loss encourages long uninterrupted sequences of detection failures. In physical world experiments, AdvSerial achieves a 74.8% attack success rate on YOLO-v5 and degrades mean detection confidence from 84.30% to 39.38%. Experiments spanning eight detectors with different architectures demonstrate strong transferability. Notably, it achieves an $89.71%$ attack success rate on YOLO-v2 and resists both patch-detection defenses (NapGuard) and 3D-temporal perception (Sparse4D-v3). The results reveal persistent, temporally consistent failure modes under high-angle surveillance, and motivate the design of motion-aware and 3D-aware defenses for security-critical infrastructure deployments.

---


### 180. [Bridging the Information Gap: Semantic Densification and Hindsight Distillation for Cold-Start Prediction](https://arxiv.org/abs/2607.17070)

**<font color=#1a73e8>作者：</font>** Hao Duong Le, Yifei Gao, Huan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> New-user cold-start is a critical bottleneck for e-commerce platforms: predicting user lifetime value (LTV) and conversion rate (CVR) for users with sparse interaction history. Two prior directions -- LLM-based semantic augmentation and learning using privileged information (LUPI) -- each face a key limitation. First, LLM augmentation produces unstructured rationales that are noisy and hard to operationalize in production. Second, naive student-teacher distillation can be brittle due to an information gap between the privileged teacher and the sparse student; moreover, this gap is heterogeneous across users. We propose SemRaD, a Semantic Reasoning-aware Distillation framework addressing both limitations. First, a Structured Semantic Reasoning Pipeline replaces free-form rationales with a structured schema built via a discover-curate-audit workflow, producing per user a Densified Semantic Profile (consumed by the deployed student via a Semantic-Gated Encoder that focuses on the most informative dimensions) and a Hindsight Distillation Target reconciled from pre- and post-conversion reasoning (used only at training). Second, to bridge this gap and handle its heterogeneity, a Hindsight-Aware Distillation Network transfers privileged knowledge via the hindsight target, with Distillation Experts improving transfer under per-user variability. On a large-scale industrial dataset, SemRaD lifts +1.9% LTV (Gini) and +1.0% CVR (AUROC) over a production-grade base; a four-week online A/B at Keeta confirms +1.0% LTV / +0.43% CVR. SemRaD also matches the production system's LTV using only 9% of the training data while improving CVR by 0.8%.

---


### 181. [SATLOCK: Handover-Coupled Scheduling for Weather-Resilient Quantum Key Distribution over LEO Constellations](https://arxiv.org/abs/2607.17076)

**<font color=#1a73e8>作者：</font>** Mohammad Arif Hossain, Md Jafrin Hossain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Routing quantum keys over low-earth-orbit (LEO) satellite constellations is harder than classical routing: satellite handovers couple consecutive scheduling decisions, stochastic cloud cover can silently zero a ground link, and finite-key effects eliminate short, low-elevation passes entirely. We present SATLOCK, a handover-aware Quantum Key Distribution (QKD) routing framework that combines (i) a composite channel model incorporating atmospheric loss, pointing jitter, Markov cloud cover, decoy-state estimation, and finite-key correction; (ii) an integer linear program (ILP) giving a provable handover-aware throughput upper bound; and (iii) a decentralized deep Q-network (DQN) baseline for weather-adaptive online routing. We evaluate two contention regimes on a Walker constellation serving intercontinental demands. In low contention (16 satellites, 6 demands), the ILP delivers 1,311 Mbit while the strongest heuristics reach 95--96\% of ILP. In high contention (8 satellites, 12 demands), where handovers become binding, heuristics drop to 89.5\% of ILP. The DQN agent reaches 91.8\% and 84.6\% of ILP in the two regimes; it learns effective per-demand weather policies but is limited in aggregate by the lack of cross-demand coordination.

---


### 182. [ALLUDE: A Unified Evaluation System for Configurable Attacks in Differentiable Environments](https://arxiv.org/abs/2607.17077)

**<font color=#1a73e8>作者：</font>** Mansi Phute, Alexander Greenhalgh, Matthew Hull 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks against vision models like object detectors are often evaluated under limited conditions, leaving their performance under-characterized. Bridging simulation and differentiable rendering enables more robust, end-to-end evaluation of these adversarial attacks, yet there is no easy-to-use, unified system that offers a rich set of customizable configurations for adversarial attacks across multiple scenes, objects, environmental and lighting conditions, and camera trajectories. We present ALLUDE, which addresses these gaps, offering first-of-its-kind evaluation capabilities across Linux and Windows. We comprehensively demonstrate ALLUDE's evaluation breadth through a two-pronged strategy: (1) using Latin Hypercube Sampling, we draw a representative subset from 5,400 configurations spanning 10 scene-object pairs, 9 weather conditions, 4 optimizers, 5 camera trajectories, and 3 detection models; (2) we stress-test existing attacks (CAMOU, RAUCA, FCA) under diverse weather conditions and continuous camera trajectories, revealing degradation of attack success across every attack, exposing evaluation gaps in prior work. Through ALLUDE's end-to-end differentiable rendering, adversarial attacks can be optimized against shifting real-world deployment conditions. Our cross-platform code is open source.

---


### 183. [Otap:Structure-Aware Optimal Transport for Evaluating Planning and Execution in Agent Trajectories](https://arxiv.org/abs/2607.17082)

**<font color=#1a73e8>作者：</font>** Babak Barazandeh, Subhabrata Majumdar, George Michailidis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents solve tasks by generating trajectories that interleave planning, tool calls, and intermediate results. Current evaluation metrics reduce such a trajectory to a binary success flag or compare it against a reference by exact matching. A success flag cannot distinguish a sound solution from one that succeeds by luck, and says nothing about why a failed run went wrong. Exact matching penalizes plans that are valid but reordered or decomposed differently from the reference. We reframe trajectory evaluation as a distance between the agent's execution graph and a set of valid solution graphs, and instantiate it via an unbalanced fused Gromov-Wasserstein transport problem over attributed dependency graphs. The resulting score, termed \otap{} (Optimal Transport for Agentic Planning), is a pseudo-metric that is provably invariant to dependency-preserving reorderings and has bounded sensitivity to redundant steps. Its unbalanced marginals handle missing or hallucinated steps without forcing a match, and its soft coupling accommodates variation in plan granularity. On controlled perturbations and three public benchmarks, \otap{} separates valid from invalid trajectories in a regime where semantics-only metrics score below chance. Its accuracy is highest when the dependency graph is recovered exactly, and drops only when the graph is inferred heuristically from free-text traces.

---


### 184. [Autoregressive B-Rep Shape Generation with Parametric Surfaces](https://arxiv.org/abs/2607.17093)

**<font color=#1a73e8>作者：</font>** Dafei Qin, Rui Xu, Zeyu Shen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative CAD modeling has broad design and application potential. Despite significant advances in Boundary Representation (B-Rep) generation, the dominant representation in CAD, existing methods largely depend on uniformly sampled point- or grid-based geometry representations, sacrificing native surface types and parameters and thereby limiting geometric fidelity and downstream usability. We present ParaCAD, an autoregressive framework for point-cloud-conditioned B-Rep generation that directly operates on native parametric surfaces. ParaCAD introduces a surface-centric tokenization that explicitly encodes each face by its exact surface type and continuous parameters, preserving the intrinsic semantics of CAD geometry. Our model first generates parametric surfaces with constrained UV domains, and then constructs a valid B-Rep by globally intersecting these surfaces to recover edges and vertices. ParaCAD places point-cloud-conditioned generation at the core of B-Rep synthesis, making it practical for user-guided reconstruction and seamless integration into existing 3D generation pipelines. Extensive experiments demonstrate that ParaCAD produces accurate B-Reps with faithful point-cloud alignment, outperforming point-based baselines in geometric precision, robustness, watertightness and downstream usability.

---


### 185. [Fourier Geometric Wind Power Forecasting with Numerical Weather Prediction](https://arxiv.org/abs/2607.17095)

**<font color=#1a73e8>作者：</font>** Shiyuan Piao, Fan Zehui, Yang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate short-term wind power forecasting is essential for grid stability and operational planning, yet remains challenging due to the complex interactions between atmospheric conditions and turbine dynamics. However, existing methods fail to effectively incorporate weather forecasting with wind turbine data (i.e., SCADA), leading to suboptimal solutions. To address this, we introduce a multimodal framework that integrates historical point-based SCADA data with grid-based Numerical Weather Prediction (NWP) forecasts, which is challenging due to heterogeneous input and the complex physical wind-turbine interactions. Our approach first explicitly decomposes inputs into scalar and vector features to better capture both site-specific and geometric dependencies and then incorporates a geometric encoder to extract rotation-invariant features from wind vectors. We further leverages a Fourier Neural Operator (FNO) architecture, which performs global convolutions in the frequency domain to efficiently model long-range spatiotemporal relationships. Extensive experiments on three real-world wind farms, with weather forecasting data, demonstrate that our model consistently outperforms state-of-the-art baselines, highlighting the effectiveness of its physically-informed design. The core implementation of our method is publicly available at: this https URL.

---


### 186. [HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object Interaction Synthesis](https://arxiv.org/abs/2607.17097)

**<font color=#1a73e8>作者：</font>** Lingwei Dang, Juntong Li, Zonghan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hand-Object Interaction (HOI) synthesis is a cornerstone for animation production and embodied AI. Despite the strong priors of video foundation models, multi-view consistent HOI synthesis remains challenging due to complex hand motions and occlusions. We present HarmoHOI, a unified diffusion framework that jointly and harmoniously generates synchronized multi-view HOI videos and globally aligned 3D point tracks. Our core insight is that robust multi-view consistency fundamentally requires globally aligned 3D geometry and motion. To this end, we propose a Mixture of Multi-view Diffusion Transformer that co-models RGB videos and 3D point tracks. By representing point tracks as pseudo-videos, we align 3D geometric signals with the 2D latent space of foundation models, thereby minimizing the domain gap and easing adaptation of priors. To further ensure geometry consistency, we introduce Global Motion Aligning Diffusion, which refines coarse point tracks into metric-scale, globally aligned 3D trajectories. HarmoHOI enables on-the-fly co-evolution of 2D appearance and 3D motion during denoising. To overcome the scarcity of multi-view HOI data, we employ a hybrid data curriculum learning strategy that successfully transfers generic priors from single-view data to synchronized multi-view generation. Experimental results show that HarmoHOI achieves state-of-the-art performance in visual quality, motion plausibility, and multi-view geometric consistency. Project page available at this https URL.

---


### 187. [DepthART: Scaling Foundation Monocular Depth to Tiny Models](https://arxiv.org/abs/2607.17099)

**<font color=#1a73e8>作者：</font>** Feng Xue, Wu Chen, Mingshuai Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent geometric foundation models (e.g., Metric3D, Depth Anything and UniDepth) have substantially improved monocular depth estimation (MDE) in both cross-scene generalization and metric-scale prediction, yet these gains have not translated to tiny models. We bridge this gap with DepthART (Depth Anything Rethought for Tiny Models), which is a compact MDE model for on-device deployment across diverse scenes. We first identify two capacity-driven bottlenecks in tiny models: (i) overfitting to dataset-specific distribution bias and (ii) unstable metric adaptation under camera shift, where full fine-tuning easily damages transferable geometry. Accordingly, DepthART combines two simple but effective strategies: a bias-resistant data sampling scheme to reduce distribution bias under the same training budget, and a camera-conditioned fine-tuning protocol that freezes the distilled encoder and adjusts metric scale conditioned on intrinsics while better preserving cross-dataset generalization. Across datasets, DepthART consistently surpasses previous tiny baselines in both zero-shot generalization and metric accuracy (e.g., zero-shot $\delta_1$=0.964 for DepthART-S on NYUD v2), and in some cases approaches heavy models. We further provide a scalable model family, with DepthART-S reaching 347/245 FPS (strict FP32) on an RTX A6000 at $224^2/448^2$, 102 FPS (TF32) on a Orin NX 8GB, and over 15 FPS (FP32) on a Jetson Nano 4GB.

---


### 188. [Auto Research for Materials: Auditable AI-Scientist Workflows with Held-Out Transfer](https://arxiv.org/abs/2607.17100)

**<font color=#1a73e8>作者：</font>** Jingjie Ning, Xiaochuan Li, Shanshan Zhong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> An AI research agent can improve the score it sees without finding a modelling change that works on new materials. We ask a stricter question. After repeated experiments, does the selected change survive on data that never entered the loop, and can its code be reused? We separate the search into changes to features, models, representations, and training data. Seven searches produce 701 evaluated changes across ten Matbench endpoints. Agents receive only the mean over five inner folds, reducing reliance on any single development split. We then freeze the selected code and evaluate it once on an untouched holdout. Nine of ten choices remain the best tested single intervention. The surviving changes reveal two materials modelling regimes. With composition alone, feature, model, and representation changes provide comparable routes to improvement. They include held-out MAE reductions of 17.4\% for band gap and 18.6\% for steel strength, as well as gains on both classification endpoints, while screened external data adds little. For structure tasks, richer geometry descriptors and model or calibration changes lower mean held-out MAE by 14.6\% and 7.1\% and lead on different property families, whereas composition embeddings do not transfer. Combining separately found feature and model changes yields a 26.3\% mean held-out improvement. These results show in materials prediction that closed-loop agents can produce decisions that survive unseen evidence and code changes that can be reused across tasks and combined. More broadly, they provide an evaluation design for testing executable discoveries beyond the feedback loop.

---


### 189. [A Multi-Model Hybrid Defense Approach Against White-box Adversarial Attacks in Computer Network Traffic](https://arxiv.org/abs/2607.17105)

**<font color=#1a73e8>作者：</font>** Khushnaseeb Roshan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> It is crucial to safeguard computer networks from evolving network security threats and unknown cyberattacks. An essential tool for protecting computer networks against unknown cyber threats is Network Intrusion Detection System (NIDS). However, NIDS faces a major security concern due to its susceptibility to adversarial attacks. Adversarial attacks aim to deceive NIDS by crafting and injecting adversarial examples into the system. These adversarial inputs can deceive the NIDS into misclassifying benign network traffic as malicious. We developed a resilient hybrid defense mechanism aimed to mitigate the impact of two potent adversarial attacks: Fast Gradient Sign Method (FGSM) and Carlini & Wagner (C&W) attack. Our hybrid defense approach leverages the combined strength of two heuristic defense methods: Adversarial Training (AT) and Gaussian Data Augmentation (GDA). GDA provides multi-directional defense, while AT enhances NIDS robustness against specific adversarial vectors. Under pre-attack scenarios, NIDS demonstrated good accuracy and f1-score. However, in the post-attack scenario, its accuracy significantly dropped under FGSM and C&W attacks (0.2649 and 0.4961, respectively). Our proposed hybrid defense method effectively mitigated these adversarial threats, with post-defense accuracy of 96.57% and 89.20% for FGSM and C&W attacks. We evaluated the defense strategy across a range of epsilon and confidence noise factor values (ranging from 0.0001 to 0.0009). This research provides a good direction for future researchers in the emerging area of adversarial machine learning from a security perspective.

---


### 190. [DSA Nonce Vulnerabilities: An Interactive Analysis](https://arxiv.org/abs/2607.17107)

**<font color=#1a73e8>作者：</font>** Rundong Wei, Xiaomei Tian, Xiaoqi Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital signatures are fundamental to identity authentication and data integrity in cybersecurity, and the NIST-standardized Digital Signature Algorithm (DSA) frequently appears in the cryptography track of CTF competitions. However, DSA relies on number theory, modular arithmetic, and large-integer computation, making both the algorithm and its associated attacks difficult for beginners to follow. Conventional tools often expose only inputs and outputs, leaving the intermediate computations of signing, verification, and key-recovery attacks opaque. This paper presents a DSA signature analysis and visualisation platform tailored to CTF competitions. The platform provides three main capabilities: basic signature generation and verification, reproduction of common CTF attack methods, and dynamic visualisation of attack workflows. It covers three representative nonce vulnerabilities: nonce reuse, linear nonce leakage, and HNP-based lattice attacks. Stepwise displays and highlighted intermediate values make the underlying computations directly inspectable. Experiments show that the platform correctly reproduces the standard DSA workflow and all three attack scenarios.

---


### 191. [Evidence Interfaces Shape How Retrieval-Augmented Readers Use Support](https://arxiv.org/abs/2607.17108)

**<font color=#1a73e8>作者：</font>** Junchi Liao, Jiawen Deng, Fuji Ren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In multi-hop RAG evaluation, a top-k answer score can hide two different failures: the retrieval window may drop part of the support chain, or it may contain support in a form the adapted reader does not use well. We call this reader-facing form of retrieved evidence an evidence interface. Using three support-annotated multi-hop QA benchmarks, we compare matched adapted readers trained with raw context, retrieval windows, and gold-support diagnostic renderings. These comparisons distinguish support-availability failures from remaining reader-interface effects. Top-k windows become interpretable only after checking whether the complete annotated support chain survives: when it does, short ranked windows can match or improve over raw context; when it does not, missing support explains much of the loss. Gold support-first improves matched readers; on 2Wiki and MuSiQue, a support-supervised ranker raises coverage and recovers raw-context quality at lower prompt cost, while retaining gold headroom. Support-removal checks further show that the gains rely on exposed evidence, not only answer priors. On support-annotated evaluations, top-k answer scores should therefore be reported together with complete-support coverage.

---


### 192. [BLAD: A Historically Contextualized, Multilingual Dataset of Bangladeshi Legal Acts (1799 to 2025)](https://arxiv.org/abs/2607.17111)

**<font color=#1a73e8>作者：</font>** Adib Sakhawat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the Bangladesh Legal Acts Dataset (BLAD), a curated collection of 1{,}484 legislative acts enacted between 1799 and 2025. Each act is represented with its full text, structured sections and footnotes, repeal status, and metadata linking it to the governing regime, head of state, and prevailing legal framework at the time of enactment. The corpus spans English, Bengali, and mixed-language documents, supporting temporal and multilingual analysis of statutory law. BLAD addresses a persistent gap in legal natural language processing (NLP) resources for low-resource, civil-law jurisdictions in South Asia. We describe the acquisition and enrichment pipeline, report descriptive statistics over more than two centuries of legislation, and outline the research directions the corpus enables. The dataset is publicly available under the CC~BY-SA~4.0 license at this https URL.

---


### 193. [The generator is the tracker: Multi-object tracking by painting persistent identity colours](https://arxiv.org/abs/2607.17120)

**<font color=#1a73e8>作者：</font>** Haiyu Yang, Miel Hostens  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking (MOT) is conventionally decomposed into detection followed by association, with object identity maintained as external state: track buffers, motion models, and appearance embeddings. We ask whether a video generator can maintain that state in pixels. We fine-tune a 22B text-to-video diffusion model (LTX-2.3) with a lightweight in-context LoRA to translate an RGB clip into an ID-map clip, a video in which every person is painted a flat, distinct color that persists over time: same color, same identity. Long videos are generated as chained windows, where each window is conditioned on the cleaned tail of the previous one. A brief continuation fine-tune teaches the model to extend a given coloring, after which identity flows through the chain with no tracker, no motion model, and no re-identification module. On the DanceTrack test server, our system, to our knowledge the first generative tracker evaluated there and the only entry with no detector and no tracking stack, reaches 40.3 HOTA. This is well below today's specialist state of the art (>=70 HOTA), but with a unique, inverted error profile: its association score (AssA 44.1) exceeds every tracker of the original benchmark suite while detection remains the sole deficit. Controlled comparisons show the mechanism matters: the same generated windows linked by classical post-hoc association score 2x worse (18.2 HOTA), and frame-to-frame IoU association fragments tracks that the generator's colors keep whole. On 383 mined occlusion events, the generator re-acquires identities after gaps at a 42% conditional rate where appearance-embedding baselines score zero, including gaps longer than its temporal context, evidence that the generator's color assignment functions as an emergent re-identification signal. We release code, checkpoints, and the full pre-registered experimental log.

---


### 194. [Learning Emotion from Motion: Kinetic Multi-Stream Skeleton Modeling with Metadata-Conditioned Weak Label Distributions](https://arxiv.org/abs/2607.17121)

**<font color=#1a73e8>作者：</font>** Sosuke Suzuki, Yijin Wei, Koichiro Kamide 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based emotion recognition from body motion remains challenging because emotional expressions are often characterized by subtle dynamic and relational motion cues, and hard labels may not fully capture ambiguity among related emotion categories. For the DIEM-A task in the MMAC ACII 2026 Challenge, we propose a multi-branch skeleton-based emotion recognition framework that combines a 6D rotation-based branch, a part-aware kinetic multi-stream branch, and a metadata-conditioned weak label distribution learning (LDL) branch. The branches are trained independently and fused by a probability-level ensemble at inference time. In 10-fold leave-performer-out cross-validation, the proposed framework improves Accuracy from 0.271 to 0.366 and Macro-F1 from 0.252 to 0.353 over the rotation-based baseline. Explainability ablations show that velocity and bone streams, as well as arm and leg regions, provide important cues for recognizing emotional body motion.

---


### 195. [SAVEstate: A Method for Documenting Player Reflection in Digital Games](https://arxiv.org/abs/2607.17128)

**<font color=#1a73e8>作者：</font>** Nisha Devasia, Michele Newman, Safinah Ali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In recent years, interest in eudaimonic player experiences (PX) - concerning reflection, meaning-making, and personal growth - has increased. However, most games user research methods are not well-suited to study eudaimonic PX, as they have been developed to evaluate features of hedonic PX, such as flow, immersion, and playability. To more deeply explore eudaimonic PX, we require methods that can 1) investigate how moment-to-moment PX shapes player reflection and 2) explore how players reengage and reinterpret their experiences longitudinally. In this paper, we present SAVEstate, a method that uses documentation as a means of studying player reflection. SAVEstate consists of two phases: reflection-in-action and reflection-on-action, which allow researchers to probe players' in-situ reflections and how they reengage with their gameplay, respectively. Using SAVEstate, we were able to observe in-situ meaning-making and connect it to post-game reflection-on-action, and view synchronous sensemaking across multiple participants. We also developed an open-source desktop application for researchers to adapt in their own SAVEstate deployments. We discuss implications for how researchers might use SAVEstate to conduct future research in meaningful PX.

---


### 196. [Denoising Models Develop Human-Like Perceptual Illusion Representations Across Architectures](https://arxiv.org/abs/2607.17138)

**<font color=#1a73e8>作者：</font>** Gautam Ranka, Paras Chopra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks trained on natural images are shown to produce outputs consistent with human observers for brightness illusions. While this phenomenon has been documented across architectures, all evidence, to date, is measured at the output level: restored pixels, decoded trajectories, or classification decisions. Whether these models actually represent illusions internally, and if so where and how, remains unknown. We show that denoising models develop illusion-sensitive representations at specific internal layers, across varied architectures. Specifically, we identify the layers and channels that discriminate illusory from physically matched control regions. We show that the denoising objective is a more important driver of the effect than the architecture. On domain-appropriate stimuli, these activations track a validated psychophysical model of human brightness perception (FLODOG; Spearman $\rho \geq 0.70$) and scale monotonically with parametric illusion strength. Leveraging these findings, we provide causal evidence via channel ablation showing that illusion-sensitive channels specifically and substantially affect the internal signal. Yet injecting these representations into the generation pipeline produces no measurable pixel shift across all tested architectures; we term such representations perceptual phantoms: active in internal processing yet invisible to any output-based evaluation. While related internal-output dissociations have been characterized in language models, this is the first such characterization for perceptual representations in denoising vision models.

---


### 197. [Noise-Robust Box-Supervised Infrared Small Target Detection via Physics-Inspired Soft Label Optimization](https://arxiv.org/abs/2607.17148)

**<font color=#1a73e8>作者：</font>** Xizhe Zhang, Fan Shi, Mianzhao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection (IRSTD) commonly relies on pixel-level mask supervision. Such annotations, however, are costly and inherently uncertain because infrared targets have blurred boundaries and weak textures. We formulate box-supervised IRSTD as a problem distinct from generic box-to-mask segmentation and point-supervised IRSTD. Its central challenge is to construct stable pixel-level soft supervision from highly contaminated boxes. To this end, we propose Hotspot-Anchored Label Optimization (HALO). HALO localizes a radiometric anchor inside each box under local background-statistics constraints, then synthesizes a Physically Anchored Gaussian (PAG) soft label around the anchor. This turns noisy box supervision into continuous, pixel-level soft labels. The entire process is performed offline before training, remains decoupled from the detector backbone, and requires no online label updates. Experiments on public datasets show that HALO is competitive with representative box-supervised methods under standard tight boxes. Under looser or shifted box annotations that better approximate real scenarios, HALO is substantially more robust while remaining consistent across backbones. We further introduce a contamination-aware operating-regime analysis to characterize the effective boundary of this class of methods and reveal how intrinsic signal-to-clutter ratio relates to performance.

---


### 198. [A Diagnostic Framework for AI Agent Behavior](https://arxiv.org/abs/2607.17149)

**<font color=#1a73e8>作者：</font>** Xichen Zhang, Yingjie Zhang, Tianshu Sun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly act within the same clinical, political, scientific, and social systems that behavioral scientists study. Evaluating these systems requires source-level diagnosis: the same behavioral pattern may arise from an agent representational substrate or from the roles, objectives, interaction structures, and governance rules that shape its expression. This Perspective proposes a diagnostic framework for AI agent behavior: layer attribution. The foundational computational layer defines what behaviors are possible through architecture, memory, perception, attention, and representation. The behavioral modulation layer shapes how those capacities are expressed through identity, resources, objectives, social interaction, institutional constraints, and governance. The framework clarifies three consequences: surrogate validity is a model-task-layer relation, human-AI divergence provides diagnostic evidence, and governance requires source attribution before intervention. Treating AI agents as behavioral actors therefore requires evaluation methods that determine where behavior originates before deciding how to explain, validate, or govern it.

---


### 199. [Strategic Gaze: Attention Allocation and Transition Patterns Across Functional Areas of Interest by Gameplay Outcome](https://arxiv.org/abs/2607.17151)

**<font color=#1a73e8>作者：</font>** Yufei Cao, Penny Sweetser  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Video games present players with complex, spatially distributed information across interface elements, with attention shaped by visual features and task goals. Eye tracking provides a useful method for examining player attention through gaze behaviour during gameplay. Yet empirical game research has relied on accumulated fixation measures that capture where attention is directed and how long it is maintained within regions, leaving less known about how gaze moves between regions to coordinate distributed information. We address this gap by integrating distribution-, duration-, and transition-based gaze measures across functionally organised interface regions in relation to gameplay outcomes. We conducted a within-subject study with 32 participants using a deck-building game, defining six functional Areas of Interest (AOIs) within the turn-based combat interface, spanning enemy, player, action, and auxiliary elements. We computed AOI hit, dwell time, transition probabilities, and entropy to compare gaze behaviour across outcome groups. Players in the win group showed more selective attention allocation extending to peripheral auxiliary resources, with more frequent action-oriented gaze transitions, a wider range of AOI pairs, and a more even distribution across AOIs. Within a strategic game setting, our findings show that gameplay outcomes are reflected in how players distribute, sustain, and shift visual attention across functional interface elements, offering a more comprehensive account of attention organisation in gameplay.

---


### 200. [VLA-ReID: Video-Level Association for Re-Identification in Multi-Object Tracking with Highly Similar Objects](https://arxiv.org/abs/2607.17157)

**<font color=#1a73e8>作者：</font>** Yanrong Qin, Xiaoyan Cao, Yao Yao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking (MOT) aims to localize multiple objects in videos while preserving their identities over time. Long-term identity preservation remains difficult when objects are small, densely distributed, and highly similar in appearance, as in bee swarm scenes. Existing trackers rely on re-identification (re-ID) models trained through single-instance assignment (instance-level querying). At inference, however, MOT requires global assignment between multiple trajectories and detections, corresponding to video-level querying. This training-inference mismatch can cause identity switches among visually similar objects. Existing approaches also often require substantial additional annotations to enhance appearance discrimination. We propose Video-Level Association re-ID (VLA-ReID), which reformulates re-ID as video-level association modeling. It uses aggregated historical trajectory features as queries and all current-frame detections as candidates, enabling direct optimization of their global association at each frame. In addition, Frame-Common Appearance Estimation (FCAE) estimates a common appearance direction from current-frame detections, while Common-Appearance Suppression (CAS) removes the corresponding component along this direction from trajectory and detection features. This amplifies discriminative differences among highly similar objects without additional annotations. Experiments on BEE24 show that VLA-ReID improves HOTA by 1.1, MOTA by 0.3, AssR by 2.6, AssA by 0.7, and IDF1 by 0.8 over state-of-the-art trackers, while reducing identity switches by 28%. These results demonstrate the effectiveness of video-level re-ID modeling for appearance-based association in MOT.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-386](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
