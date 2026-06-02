# 📦 其他研究 | 2026年06月03日

> 本类共 **651** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

---

### 51. [Emergence of Exploration in Policy Gradient Reinforcement Learning via Retrying](https://arxiv.org/abs/2606.00151)

**<font color=#1a73e8>作者：</font>** Soichiro Nishimori, Paavo Parmas, Sotetsu Koyamada 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In reinforcement learning (RL), agents benefit from exploration only because they repeatedly encounter similar states: trying different actions can improve performance or reduce uncertainty; without such retries, a greedy policy is optimal. We formalize this intuition with ReMax, an objective that evaluates a policy by the expected maximum return over $M$ samples, where $M$ is a positive integer, while accounting for return uncertainty. Optimizing this objective induces stochastic exploration as an emergent property, without explicit bonus terms. For efficient policy optimization, we derive a new policy-gradient formulation for ReMax and introduce ReMax PPO (RePPO), a PPO variant that optimizes ReMax while generalizing the discrete retry count $M$ to a continuous parameter $m > 0$, enabling fine-grained control of exploration. Empirically, RePPO promotes exploration, without any explicit exploration bonuses, on the MinAtar and Craftax benchmarks.

---


### 52. [Digital-to-Physical Transfer of Adversarial Patches for Aerial Vehicle Detection](https://arxiv.org/abs/2606.00159)

**<font color=#1a73e8>作者：</font>** Jung Heum Woo, Eun-Kyu Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural network (DNN)-based object detectors are widely used for analyzing aerial and satellite imagery in applications such as environmental monitoring and urban analytics. Despite their strong performance, these models are known to be vulnerable to adversarial examples, and physical adversarial attacks using printable patterns pose realistic security threats. In this paper, we evaluate physical adversarial patch attacks against an aerial vehicle detector by bridging digital optimization and real-world deployment. Adversarial patches are optimized in the digital domain using a loss function that minimizes the maximum objectness score while incorporating non-printability score (NPS) and total variation (TV) constraints to ensure both printability and spatial smoothness. The optimized patches are printed and deployed in three configurations: ON, OFF, and OFF-Side. Experiments using a YOLOv3 detector show that while the OFF patch achieves the highest effectiveness in the digital domain (85.51% Average Objectness Reduction Rate (AORR)), the ON patch demonstrates superior robustness in physical environments (0.197-0.343 Objectness Score Ratio (OSR)) due to its consistent visibility. Furthermore, our results indicate that weather-based augmentation does not necessarily improve patch optimization in this domain. These findings provide critical insights into the practical vulnerabilities of aerial object detection systems.

---


### 53. [Improving IoT Intrusion Detection Through SMOTE-Based Oversampling and Extended Multi-Model Evaluation on Side-Channel Power Data](https://arxiv.org/abs/2606.00161)

**<font color=#1a73e8>作者：</font>** Muhammad Khuram Shahzad, Haseeb Khan, Muhammad Masood Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The detection of intrusions in IoT-based networks poses challenges that cannot be overcome using traditional machine learning methods. Perhaps the biggest of them is related to the presence of a class imbalance in the side-channel dataset, where the number of samples in the normal class compared to the attacks can reach a ratio of 75,964 to 1. Such an aspect is addressed by Dominguez et al. through the proof of concept of power-based intrusion detection. Unfortunately, neither the authors attempt to cope with the problem of imbalance nor do they assess the classifier performance using a balanced training set. In the current paper, both aspects will be handled at once. First, a Synthetic Minority Oversampling Technique (SMOTE) was performed on all nine possible datasets extracted from the initial one, providing an exact imbalance ratio of 1.1 for each. Then, eight algorithms i.e. Random Forest, HistGradientBoosting, LightGBM, Extra Trees, XGBoost, k-Nearest Neighbors, Multi-Layer Perceptron, and Decision Tree were trained under identical conditions for the SMOTE balanced 6-hour dataset. Random Forest reached a micro-averaged F1 score of 0.9989 and macro F1 of 0.9794, thus outperforming the previously best micro-F1 result obtained by Time Series Forest algorithm from the base paper of 0.9983. Extra Trees provided the same performance as well, but at 10 times faster. The introduction of a macro-F1 metric explicitly in contrast to the base paper assessment reveals important class-level information missed with aggregate performance metrics. Recall rates per-class calculated with confusion matrices, F1 heatmaps, and ROC curves show that minority attack classes, especially those with combined M+L infections, are detected reliably only when using SMOTE balance. Feature importance analysis indicates the latest time steps as the most important predictor signals out of 60 steps in a power window.

---


### 54. [RealityTest: How People Probe AI Identity and Whether Models Disclose It](https://arxiv.org/abs/2606.00168)

**<font color=#1a73e8>作者：</font>** Anna Gausen, Sarenne Wallbridge, Bessie O'Dell 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI systems are increasingly deployed in conversational settings where users may be uncertain whether they are speaking with a human or an AI. Despite mounting regulatory attention to this known safety risk, existing evaluations of AI disclosure are typically English-only, based on machine-generated questions, and restricted to text. We present RealityTest to comprehensively test whether AI systems disclose their identity when asked. The benchmark is the first large-scale multimodal and multilingual evaluation, grounded in human data on how people actually encounter and question AI identity in the real-world. Alongside the benchmark, we release the underlying dataset of 3,152 identity-probing queries collected from ~750 participants across 49 countries and five languages, in text and speech scenarios. We find that only 31% of people ask about identity directly in ambiguous scenarios, and that the questions people ask are far more diverse than machine-generated queries. We test 17 text and 6 speech models, and find substantial variation in disclosure behaviour. However, a single suppression instruction reduces disclosure rates to below 30%, even in the best-performing models. Validating our investment in diverse, human-grounded evaluation data, we find that how the question is phrased and the context of the conversation matter more for disclosure than which model is being tested. Safety evaluations built on narrow or synthetic query sets risk mischaracterising how models behave in realistic deployment settings.

---


### 55. [ChurnNet: A Optimized Modern AI for Churn Prediction](https://arxiv.org/abs/2606.00169)

**<font color=#1a73e8>作者：</font>** Syed Saad Saif, Giulio Maggiore, Paolo Russo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Increased competition and the growing similarity of products and services offered by retailers have lowered the barriers for customers to switch to competitors. Accurate churn prediction can be a valuable tool for driving effective personalized marketing campaigns and helping to reduce customer attrition. This study evaluates the performance of traditional machine learning techniques, namely, Random Forests, XGBoost, and Support Vector Machines, and compares them with the Unified Multi-Task Time Series Model for churn prediction, a binary time-series classification task. Despite the strong capacity of the latter to model complex temporal dynamics and inter-variable relationships, our results indicate that for churn prediction, conventional methods can still outperform it in terms of predictive performance, data efficiency, and computational resource requirements for training and deployment. These findings are consistent across multiple datasets and various churn labeling techniques.

---


### 56. [CAST: Non-Privileged Clipped Asymmetric Self-Teaching with Advantage Flipping for GRPO](https://arxiv.org/abs/2606.00172)

**<font color=#1a73e8>作者：</font>** Yang Li, Gongle Xue, Yijia Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR), especially Group Relative Policy Optimization (GRPO), has been widely used to improve reasoning in large language models. However, outcome-level rewards provide only sparse supervision, and group-relative advantages vanish when all sampled trajectories for a prompt are either correct or incorrect. On-Policy Self-Distillation (OPSD) offers dense token-level guidance, but its token preferences are not necessarily aligned with trajectory correctness; empirical diagnostics show that OPSD signals behave differently on correct and incorrect rollouts, with teacher-positive and teacher-negative gap signals exhibiting different noise profiles. These diagnostics are conducted under an OPSD-style privileged teacher context for analysis only, whereas CAST training uses answer-free self-teacher this http URL by these observations, this work proposes CAST, an answer-free self-distillation method for GRPO-style RLVR. CAST keeps the verifier-grounded GRPO objective, but uses a stop-gradient self-teacher to shape token-level advantages according to trajectory correctness. Unlike prior self-distilled RLVR methods, CAST does not require reference-solution-conditioned teacher scoring, keeps the self-teacher log-probability gap active throughout training, and applies bidirectional local advantage sign reversal: teacher-negative tokens in correct trajectories can receive negative token-level advantages, while teacher-positive tokens in incorrect trajectories can receive bounded positive local advantages. For zero-variance all-correct and all-wrong groups, CAST assigns bounded sign-constrained base advantages, so these otherwise zero-gradient groups can contribute verifier-signed token feedback. Experiments on mathematical reasoning show that CAST improves RLVR training while retaining a lightweight, verifier-grounded trajectory-level objective.

---


### 57. [MyoSem: Aligning Electromyography to Natural-Language Action Semantics for Hand Action Understanding](https://arxiv.org/abs/2606.00174)

**<font color=#1a73e8>作者：</font>** Chiyue Wang, Dong She, Yang Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Electromyography (EMG) directly reflects muscle activation and is a key sensing modality for gesture recognition, prosthetic control, and wearable interaction. Existing EMG methods, however, commonly formulate hand action understanding as classification over fixed labels, making it difficult to support querying, retrieval, and generalization based on action descriptions. We present MyoSem, an EMG--action semantic alignment framework that maps low-level EMG signals into a shared semantic space constructed from multi-view action descriptions. MyoSem combines multi-view action-semantic construction, activation-aware EMG encoding, and semantic query alignment, enabling bidirectional retrieval between EMG signals and text descriptions. We systematically evaluate MyoSem on EMG2Pose and NinaPro-series datasets. Results show that MyoSem performs well on EMG--text bidirectional retrieval, generally outperforms most baselines, and shows favorable generalization to unseen users, held-out action classes, and amputee-user transfer scenarios. Ablations and visualizations further validate the effectiveness of each module. Overall, MyoSem advances EMG-based hand action understanding from fixed-label recognition toward queryable bidirectional semantic retrieval, providing a new modeling paradigm for language-mediated EMG action understanding.

---


### 58. [Beyond Augmentation: Score-Guided Pathological Prior for EEG-based Depression Detection](https://arxiv.org/abs/2606.00180)

**<font color=#1a73e8>作者：</font>** Xiaojing Chen, Jingqi Cheng, Xu Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning-based Major Depressive Disorder (MDD) detection using Electroencephalography (EEG) is fundamentally constrained by the "small-sample dilemma." Prevailing generative data augmentation methods not only incur heavy computational overhead but also risk introducing synthetic noise, thereby blurring classification boundaries. To challenge the traditional "data quantity first" convention, we propose a novel framework "Beyond Augmentation": Score-Guided Classification (SGC). SGC does not synthesize pseudo-samples; instead, it utilizes an unsupervised generative network architecture to model the structural and statistical anomaly degrees of samples, serving as the core "Pathological Prior". This prior, after robust normalization, is explicitly fused with deep feature representations, thereby precisely guiding the classifier's decision boundary. Furthermore, to dynamically adapt to varying channel configurations, we propose a Cross-Channel Spatial Adaptation module, utilizing a spatial mapping mechanism to effectively resolve the hardware heterogeneity of mismatched channels in multi-center datasets. Extensive experiments on the Mumtaz2016 and high-density MODMA datasets demonstrate the effectiveness and exceptional generalizability of our method under the challenging "zero data augmentation" setting and at "zero sample synthesis cost".
Keywords: Electroencephalography (EEG), Depression Detection, Anomaly Score, Diffusion Models, Few-Shot Learning

---


### 59. [The New Social Image: How AI Competency and AI Proactivity Influence Self- and Peer-Perceptions in the Workplace](https://arxiv.org/abs/2606.00182)

**<font color=#1a73e8>作者：</font>** Kuntal Ghosh, Marc Hassenzahl, Shadan Sadeghian  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-AI collaboration is considered the most promising way to incorporate AI in the workplace. What remains unexplored are the experiential consequences of this teaming. More specifically, in a team with AI, how humans perceive themselves (self-perception) and how they are perceived by their coworkers (peer perception) in terms of work ownership and job meaningfulness. In a 2x2x2 vignette study (n=50), participants rated perceptions of ownership, affect, job meaningfulness and satisfaction, and role dynamics across two levels (low/high) of AI proactivity and AI competency as within-subject factors, with point-of-view (self perception/peer perception) as between-subjects. Our results showed that AI with low competency or low proactivity generally improved feelings related to ownership, meaningfulness, satisfaction, and role dynamics, and also increased positive affect while reducing negative affect. However, these effects were often influenced by point-of-view. For instance, low AI proactivity resulted in higher job satisfaction from self-perception rather than peer perception. Based on our findings, we argue that designing AI for the future of work solely around performance metrics may not be adequate. Highly competent and proactive AI-driven systems can have undesirable impacts on perceptions of ownership, job identity, social image and team dynamics, and consequently, job meaningfulness.

---


### 60. [Inferring Routing-Layer Defense Mechanisms from Observable Behavior in OLSR-Based MANETs](https://arxiv.org/abs/2606.00184)

**<font color=#1a73e8>作者：</font>** Nadav Schweitzer, Kiril Danilchenko, Ariel Stulman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile ad hoc networks (MANETs) based on proactive routing protocols such as OLSR remain vulnerable to routing-layer attacks. While prior work has focused primarily on attack detection, the problem of identifying deployed defenses has received comparatively little attention. This work examines whether the presence of a routing-layer defense can be inferred from features derived exclusively from externally observable routing and control-plane behavior. The evaluated Fictive Mitigation mechanism operates entirely within standard OLSR control traffic and introduces no new packet types, making passive detection inherently difficult. Using ns-3 simulations across baseline, attack-only, defense-only, and combined attack-defense regimes under both static and mobile conditions, we derive features from observable routing dynamics and control-plane activity available to a passive observer. Despite the restricted observability available to the adversary, the results show that defense detection remains feasible in this setting. Ensemble models achieve in-domain accuracy up to $0.91$ (AUC $0.96$). Cross-domain generalization is asymmetric: models trained on static data degrade under mobility ($\approx 0.67$), whereas mobile-trained models transfer more robustly ($\approx 0.84$). Restricting the model to a compact invariant feature subset of four metrics yields near-symmetric cross-domain transfer ($\approx 0.86$ in both directions). These findings indicate that the evaluated defense mechanism leaves a detectable statistical footprint in passively observable routing behavior, providing adversaries with a potential reconnaissance capability in protected MANET deployments.

---


### 61. [AI-Guided Design and Optimization of Graphite-Based Anodes via Iterative Experimental Feedback](https://arxiv.org/abs/2606.00187)

**<font color=#1a73e8>作者：</font>** Qian Du, Mark M. Sullivan, James E. Saal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study presents an iterative AI-guided workflow that accelerates graphite-based anode development by improving both formulation feasibility and process robustness. Sequential learning via AI/ML-guided multiobjective inverse design for anode optimization was implemented using the Citrine Platform. Starting from a noisy, incomplete dataset, the Citrine Platform was used to generate early surrogate models, which despite low predictive certainty highlighted missing process constraints. By iteratively adding feasibility labels and boundary condition failures, the workflow rapidly converged toward manufacturable, higher-performing formulations. Fabrication reliability improved from frequent process failures to 100% successful cell production, while the fraction of cells delivering $\geq$ 350 mAh g$^{-1}$ increased from 28.4% to 84.8%, with capacity retention rising from 42.1% to 97.3%. These results demonstrate that structured, feedback-driven AI workflows can transform imperfect industrial data into actionable guidance, enabling faster, more reproducible optimization of battery electrode manufacturing.

---


### 62. [A Moderatorless Protocol for WEREWOLF](https://arxiv.org/abs/2606.00190)

**<font color=#1a73e8>作者：</font>** Naoki Kitamura, Hironori Kiya, Hirotaka Ono  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Social deduction games, or hidden-role games, are multiplayer games in which players are assigned private roles and act under asymmetric information about other players' roles and actions. In the canonical example Werewolf, werewolves conceal their roles and mislead the other players, while the seer can obtain role information about a chosen player. Thus, a central functionality of such games is controlling which players can access which information. In typical play, this control is implemented by a trusted human moderator, who assigns roles, mediates secret actions, and reveals outcomes. This reliance raises the barrier to participation and introduces a trusted third party as a single point of failure. In this work, we show that Werewolf can be played without a moderator or any digital device, using only ordinary playing cards. Our construction maintains a shared pool of cards that is observable to all players and manipulated according to a common public procedure, while its interpretation depends on each player's private role. This induces role-dependent views from a single public sequence of card operations. Consequently, even without private messages, werewolves can identify one another and coordinate, and the seer can test whether a chosen player is a werewolf in each round. The proposed implementation is built from card-based physical cryptographic primitives, such as face-down commitments and verifiable shuffles, and higher-level subprotocols for intra-role information sharing, secret action designation, and attribute testing. These subprotocols implement the moderator's core functions while keeping all card operations public and auditable under standard assumptions on physical card operations. We show that the resulting complete moderatorless implementation of Werewolf scales to an arbitrary number n of players using O(n^3) cards.

---


### 63. [BOUTEF: A Multilingual Corpus for FakeNews in North Africa -- Language as a Weapon](https://arxiv.org/abs/2606.00193)

**<font color=#1a73e8>作者：</font>** Kamel Smaili, Yassine Toughrai, Amina Laggoun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid spread of fake news on social media has become a major challenge, particularly in multilingual and under-resourced contexts such as North Africa. In this paper, we introduce BOUTEF, a large-scale multilingual corpus designed to study the propagation, characteristics, and impact of fake news in Algeria and Tunisia. The corpus integrates three complementary components: fake narratives, genuine narratives, and associated user-generated comments, along with verified debunking information. It covers a wide range of languages and linguistic varieties, including MSA, Algerian and Tunisian dialects, Arabizi, French, English, and code-switched language. Building on this resource, we conduct a comprehensive empirical analysis combining quantitative and qualitative approaches. We examine thematic distributions, linguistic and rhetorical strategies, sentiment patterns, and social engagement dynamics. Statistical analyses reveal significant associations between thematic categories and message veracity, as well as strong correlations between user engagement and the visibility of fake content. Our findings show that fake news relies heavily on emotionally charged narratives, sensational framing, and hybrid linguistic practices that enhance virality and audience engagement. In contrast, debunking content adopts a more factual and verification-oriented style. Furthermore, a comparative analysis between Algeria and Tunisia highlights both shared dynamics and country-specific characteristics shaped by sociopolitical contexts. The results emphasize the role of informal language practices in the diffusion and reception of misinformation. By providing a rich, annotated, and publicly available dataset, this work contributes to advancing research on fake news detection, low-resource language processing, and the understanding of information disorders in complex linguistic environments.

---


### 64. [From Rashomon Theory to PRAXIS: Efficient Decision Tree Rashomon Sets](https://arxiv.org/abs/2606.00202)

**<font color=#1a73e8>作者：</font>** Zakk Heile, Hayden McTavish, Varun Babbar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard machine learning pipelines often admit many near-optimal models. These "Rashomon sets" pose a range of challenges and opportunities for uncertainty-aware, robust decision making. They allow users to incorporate domain knowledge and preferences that would otherwise be difficult to specify directly in an objective, and they quantify diversity among valid models for a given training dataset and objective function. However, computation of Rashomon sets, even for simple, interpretable model classes such as sparse decision trees, continues to require immense memory and runtime resources. We present PRAXIS, an algorithm to approximate this Rashomon set with orders of magnitude improvement in runtime and memory usage. We validate that PRAXIS regularly recovers almost all of the full Rashomon set. PRAXIS allows researchers and practitioners to scalably model the Rashomon set for real-world datasets. Code for PRAXIS is available at this https URL

---


### 65. [DeSQ: Decomposition-based SPARQL Query Generation](https://arxiv.org/abs/2606.00203)

**<font color=#1a73e8>作者：</font>** Papa Abdou Karim Karou Diallo, Aditya Sharma, Neshat Elhami Fard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dominant approaches to Knowledge Base Question Answering (KBQA) fall into two categories. First is the generation of a formal query that suffers from brittleness and limited explainability, and the second is direct answer retrieval through KB exploration that is computationally costly and prone to hallucination. To combine the strengths of both paradigms while mitigating their respective weaknesses, we introduce DeSQ (Decomposition-based SPARQL Query Generation), a KB-agnostic framework that operates in three stages. First, it decomposes complex questions into Atomic Constraints (ACs) that mirror the relational structure of the underlying KB. Second, it generates a two-part structured output: (a) Mapping of each AC to its corresponding SPARQL Fragment, using standardized variable and URIs placeholders, and (b) URIs Grounding block describing each placeholder. Third, it assembles these fragments into a complete SPARQL query. DeSQ surpasses state-of-the-art approaches on four out of five major benchmarks and demonstrates superior robustness to lexical variation. Beyond performance gains, our framework greatly simplifies evaluation by eliminating the need for a live KB endpoint, and its structured output enables fine-grained error analysis, allowing more targeted interventions for improvement.

---


### 66. [LithoGRPO: Fast Inverse Lithography via GRPO Reinforced Flow Matching](https://arxiv.org/abs/2606.00228)

**<font color=#1a73e8>作者：</font>** Yao Lai, Xuyuan Xiong, Zeyue Xue 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In semiconductor manufacturing, lithography projects circuit layouts onto silicon wafers through an optical mask. As circuit features shrink below the wavelength of light, optical diffraction causes the printed patterns to deviate from their intended layouts. Inverse Lithography Technology (ILT) addresses this challenge by generating optimized masks that enhance the fidelity of pattern transfer onto wafers. While ILT resembles an image synthesis task, its reliance on explicit physical metrics for mask evaluation limits the applicability of existing generative models. We introduce LithoGRPO, an ILT framework that integrates the flow-matching paradigm with GRPO-based reinforcement learning (RL) fine-tuning, enabling efficient exploration of diverse masks for a given target layout. Unlike purely generative or optimization-based approaches, RL in LithoGRPO exploits the explicitly defined, physics-based reward function of ILT, enabling optimization under complex, process-aware constraints. To the best of our knowledge, this is the first framework that unifies flow matching and RL for mask optimization. To improve RL sampling efficiency, we propose a fast shot-counting algorithm for manufacturability evaluation, achieving over 130x speedup while preserving the mask ranking of the traditional shot-count metric. Extensive experiments demonstrate that LithoGRPO achieves state-of-the-art performance over both optimization-based and learning-based methods, while maintaining efficient mask generation.

---


### 67. [Geodesic Flow Matching for Denoising High-Dimensional Structured Representations](https://arxiv.org/abs/2606.00248)

**<font color=#1a73e8>作者：</font>** Karim Habashy, Chris Eliasmith  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vector Symbolic Algebras (VSAs) enable robust neurosymbolic reasoning by encoding symbolic information into high-dimensional distributed representations. For continuous domains, Spatial Semantic Pointers (SSPs) extend this framework by mapping variables onto continuous toroidal manifolds. However, standard approaches like Flow Matching assume a flat Euclidean geometry, which fails to account for the geometric constraints imposed on valid SSP states. We demonstrate that this assumption fails for SSPs: Euclidean linear interpolants ``cut through" the manifold's interior, destroying the phase and magnitude structure required for accurate decoding. To resolve this, we employ Geodesic Flow Matching, adapting Riemannian transport dynamics to strictly restrict the denoising flow to the SSP toroidal manifold. We validate this approach in a Spiking Neural SLAM system, showing that manifold-aware cleanup stabilizes path integration against drift. The method achieves a 72\% reduction in tracking error and enables a 40\% increase in neural efficiency compared to competitive baselines. Code is available at this https URL .

---


### 68. [ARCA: Adapter-Residual Credit Assignment When Token Signals Degenerate](https://arxiv.org/abs/2606.00257)

**<font color=#1a73e8>作者：</font>** Rodney Lafuente-Mercado  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Token-level credit assignment for language-model reinforcement learning is usually formulated as if the policy were fully trainable, while practical LLM-RL pipelines often rely on parameter-efficient fine-tuning, especially LoRA. We argue that this separation hides a structural failure mode. Under LoRA, the policy is restricted to a low-rank neighborhood of the reference model, so the per-token output-distribution differences used by common intrinsic credit signals, surprisal, entropy reduction, and policy divergence, can become degenerate after within-trajectory normalization, either approaching uniform weights or concentrating on a small set of task-agnostic positions. We formalize this behavior and propose measuring it directly with concentration diagnostics such as weight Gini and effective-token ratio. We then introduce \emph{Adapter-Residual Credit Assignment} (ARCA), a lightweight alternative that derives token salience from the adapter's own hidden-state residual, $\|h^{\text{adapted}}_t - h^{\text{base}}_t\|_2$. ARCA asks where the adapter actually changes the model, rather than where the output distribution appears uncertain or shifted, and requires no learned reward model, value head, or tree construction. In a compact MATH/Qwen3-1.7B GRPO sweep, ARCA exhibits the predicted non-degenerate middle-regime credit distribution under matched rollout budgets and remains competitive with rank-matched baselines.

---


### 69. [LastAct: Trajectory-Guided Latest-Activity Localization for Real-Time Smart-Home Activity Recognition](https://arxiv.org/abs/2606.00260)

**<font color=#1a73e8>作者：</font>** Zishuai Liu, Ruili Fang, Jin Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human Activity Recognition (HAR) from ambient sensors enables smart-home applications such as health monitoring and assisted living. In realistic deployments, however, sensor events arrive as a continuous stream and activity boundaries are unknown. Sliding-window inference therefore produces many windows that straddle transitions and contain mixed activities, creating boundary contamination that violates the pre-segmented instance assumption used by most benchmarks and models. Moreover, many pipelines under-use spatial context by treating sensor IDs as independent tokens. We present LastAct, a trajectory-centric framework for streaming smart-home HAR that targets the most recent activity under mixed windows while explicitly modeling spatial structure. LastAct projects sensor events onto the home floorplan to form a layout-aligned trajectory image sequence that preserves spatial continuity. A lightweight gate identifies contaminated windows, and a boundary localizer estimates the last transition to enable boundary-guided masking that emphasizes post-boundary evidence and suppresses stale context. For efficiency, we reuse a precomputed layout-aligned template cache to avoid repeated rendering. Empirically, across four public smart-home datasets under near-realistic mixed-activity protocols, LastAct achieves competitive or superior performance on pure windows and yields substantial Macro-F1 gains on cross/mixed windows, demonstrating improved robustness under near-realistic sliding-window regimes.

---


### 70. [The Harsh Truth: Segment-Level Analysis of Harsh Driving Events in Milan Using Large-Scale Telematics, Street Networks, and Google Street View](https://arxiv.org/abs/2606.00261)

**<font color=#1a73e8>作者：</font>** Andrea La Grotteria, Paolo Santi, Titus Venverloo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Police-reported crash statistics remain the standard input for urban road-safety assessment, but their incompleteness and reporting lag limit their usefulness for timely, fine-grained intervention design. Harsh acceleration and braking events are widely used as surrogate safety indicators, but have so far been studied only in comparatively small urban samples. This study analyses harsh events across the urban road network of Milan, combining high-resolution telematics from more than 4.2 million vehicles equipped with On-Board Units, segment-level traffic metrics from TomTom, street-network and infrastructure attributes from OpenStreetMap, and visual streetscape features extracted from Google Street View via semantic segmentation using a OneFormer model. We employ an analytical framework combining non-parametric Mann--Whitney U tests of segment-feature distributions between high- and low-harshness groups with supervised machine-learning regressors. We find that, once exposure is controlled for, wider carriageways, crossings and transit stops, and more open visual fields (higher sky- and road-pixel proportions) are associated with higher harsh-event intensity, while denser built frontage is associated with lower intensity. Finally, the cycling-infrastructure case study identifies a gradient in harsh-event intensity across facility types: markings-only cycle lanes are associated with a 19.5% higher harshness score, and mixed-traffic configurations with an 11.5% higher score, relative to physically separated cycle paths, conditional on the included controls. These results support context-specific rather than uniform urban-safety interventions and illustrate how large-scale telematics combined with open geospatial and visual data can inform Vision Zero decision-making at the metropolitan scale.

---


### 71. [When Softmax Fails at the Top: Extreme Value Corrections for InfoNCE](https://arxiv.org/abs/2606.00262)

**<font color=#1a73e8>作者：</font>** Melihcan Erol, Suat Evren, Oktay Ozel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> InfoNCE is the standard contrastive learning objective, but its softmax form is not only a computational convenience: it also encodes a statistical assumption about how the top-scoring example is selected. Using extreme value theory, we show that this assumption is often misaligned with the normalized embedding setting used in modern contrastive learning. Motivated by this mismatch, we propose \textsc{WEINCE}, a simple modification of InfoNCE that uses anchor-wise online batch statistics to blend the usual softmax logits with an endpoint shortfall correction, adding no trainable parameters. Across five vision benchmarks, \textsc{WEINCE} yields consistent improvements in frozen-feature evaluation. These results show that a more faithful statistical treatment of hard negatives can improve contrastive objectives.

---


### 72. [Closed-Loop Neural Activation Control in Vision-Language-Action Models](https://arxiv.org/abs/2606.00269)

**<font color=#1a73e8>作者：</font>** Abhijith Babu, Ramneet Kaur, Nathaniel D. Bastian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models can be steered at test time by intervening on semantically meaningful internal directions, but existing methods use a fixed steering coefficient, effectively operating in open loop. This is poorly suited to embodied control, where task state and concept error evolve over time, often causing overcorrection, oscillation, and reduced task success, especially for temporal behaviors such as speed and smoothness. We propose CTRL-STEER, a closed-loop framework that replaces static intervention strength with adaptive, time-varying control signals. The key idea is to decouple representation from regulation: rather than assuming temporal concepts are directly controlled by individual neurons, we steer along motion-aligned residual directions while a feedback controller adjusts intervention magnitude online. We instantiate this framework with both PID and reinforcement learning based controllers. Experiments with a fine-tuned OpenVLA policy on four LIBERO task suites show that CTRL-STEER achieves more stable concept regulation and a better steering-task success trade-off than fixed-coefficient baselines, without modifying or retraining the base model.

---


### 73. [Robust Shielding for Safe Reinforcement Learning](https://arxiv.org/abs/2606.00270)

**<font color=#1a73e8>作者：</font>** Edwin Hamel-De le Court, Thom Badings, Alessandro Abate 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Shielding is an effective approach to formally guarantee the safety of reinforcement learning agents in Markov decision processes (MDPs). However, existing shielding techniques typically assume knowledge of the safety-relevant transition dynamics - a requirement that is seldom met in practice. To address this limitation, we introduce a novel shielding framework for robust MDPs (RMDPs), i.e., MDPs with sets of transition probabilities. We define safety as the satisfaction of a linear temporal logic (LTL) formula with a certain threshold probability under the worst-case transition probabilities of the RMDP. We prove that our shielding framework is both sound and optimal for the RMDP: every policy admissible by the shield is safe, and conversely, every safe RMDP policy is admissible by the shield. We combine our approach with existing sampling methods for learning transition probabilities of MDPs with probably approximately correct (PAC) guarantees. This combination enables the construction of shields for MDPs that, with high confidence, guarantee safety while remaining minimally restrictive. Our experiments show that our shields for learned RMDPs guarantee safety in unknown MDPs while recovering strong expected return as the number of samples increases.

---


### 74. [On Wednesdays, We Ask Questions: Optimizing "Active Listening" in Automated Legal Triage and Referral](https://arxiv.org/abs/2606.00272)

**<font color=#1a73e8>作者：</font>** Quinten Steenhuis, Jacqueline Harvey  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The FETCH classifier generates follow-up questions to help refine the best match for the applicant's legal problem, using a low-cost ensemble of LLMs. In this paper, we describe an expert attorney and LLM-assisted evaluation of the follow-up question approach in FETCH and show that while low-cost LLMs perform well at classification tasks, generating high-quality plain-language questions in this setting appears to require a more sophisticated and higher-cost model. Through discussion with legal intake workers, we propose a rubric for the evaluation of legal intake classification questions, and we find that prompt engineering alone is not enough to improve question quality for intake purposes. We also find that LLM-as-judge and human ratings diverge. We demonstrate that with the addition of a single high-cost model, GPT-5, the classifier can elicit relevant information from applicants for legal help, and that the questions lead to more accurate performance at classification tasks. We also find uneven fact elicitation across different categories, including domestic violence, at odds with family law screening protocols, suggesting the value of including dedicated screening panels for certain areas of law.

---


### 75. [Evaluating Bivariate Causal Statements Based on Mutual Compatibility](https://arxiv.org/abs/2606.00278)

**<font color=#1a73e8>作者：</font>** Erik Jahn, Dominik Janzing  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For many real-world systems, causal ground truth is difficult to obtain, making claims about causal effects hard to assess. We develop methods for evaluating collections of $\binom{n}{2}$ bivariate causal statements over a set of $n$ variables. In the setting of acyclic linear statements, any such collection can be extended to a unique multivariate causal model, but we argue that this induced model is implausible if it imposes substantial additional confounding to explain observed correlations. We introduce a compatibility score that quantifies this notion of plausibility, notably without relying on the faithfulness assumption. Additionally, we define an incompatibility score for purely graphical bivariate causal statements, based on global consistency constraints that are derived from acyclicity and faithfulness assumptions. We give theoretical and empirical evidence that both scores can successfully distinguish correct from incorrect causal statements in generic settings. Moreover, we demonstrate the practical applicability of our methods by analyzing causal claims made by large language models. Our work aims to provide a foundation for assessing the reliability of causal information derived from human experts or artificial intelligence in settings where alternative forms of validation are unavailable.

---


### 76. [Bit-Exact AI Inference Verification Without Performance Tradeoffs](https://arxiv.org/abs/2606.00279)

**<font color=#1a73e8>作者：</font>** Naci Cankaya  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Verifying claims about AI workloads is a pre- requisite for credible AI governance of covert adversaries (who comply with monitoring only when detection likelihood is high), yet the ap- parent non-determinism of GPU floating-point arithmetic forces auditors to accept approximate output matches. Covert adversaries can exploit un- verifiable degrees of freedom in monitored compu- tation. Attack vectors include steganography, un- reported modification of inference software, and covert computation via unreported batch elements. Empirically, we analyze how modern inference engines (vLLM, HF transformers) produce deter- ministic but non-invariant outputs, without need- ing to set performance-compromising determin- ism flags, if the right information is available for re-computation and no atomic functions are called in the backend. We demonstrate that such bitwise- precise re-computation does not require access to identical hardware, via a software-only emula- tion of LLM inference across multiple NVIDIA GPU variants. Thus, accumulated rounding errors can be an auditable signature of the software and hardware setup used for inference, instead of a constraint on verifiability.

---


### 77. [Model-Based Quality Assessment for Massively Multilingual Parallel Data](https://arxiv.org/abs/2606.00285)

**<font color=#1a73e8>作者：</font>** Abdelaziz M.A. Ibrahim, Zihao Li, Jörg Tiedemann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale multilingual bitext often contains two distinct problems: non-parallel sentence pairs and low-quality translations. We decompose model-based assessment for such data into two independent components: parallelism assessment with multilingual embeddings and reference-free quality estimation (QE). For parallelism, we benchmark four embedding models on FLORES-200 and BOUQuET retrieval tasks, covering 6,654 source--target directions in our target language-pair inventory. For QE, we evaluate nine reference-free evaluators on professional FLORES-200 translations across 41,412 ordered source--target directions. Results show that no model is universally reliable across translation directions. Naive QE ensembles dilute strong model signals, while documented target-language coverage is strongly associated with higher QE scores. Overall, these findings suggest that multilingual parallel-data assessment is best approached as a direction-aware routing and calibration problem, where no single universal metric is expected to suffice across all languages.

---


### 78. [Inner Product Aware Quantization: Provably Fast, Accurate, and Adaptive Algorithms](https://arxiv.org/abs/2606.00289)

**<font color=#1a73e8>作者：</font>** Nathan White, Krish Singal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization is a fundamental tool used to compress datasets, neural network weights, and memory usage in a range of computational tasks. Many downstream applications of vector quantization perform inner products with arbitrary inputs. This motivates the study of inner product aware quantization schemes that approximately preserve inner products with unseen vectors -- in contrast to simply minimizing the mean-squared error.
In this work, we formulate objectives that capture natural desiderata and develop adaptive and unbiased quantization methods that approximately preserve inner products with worst-case and average-case inputs. An analysis of these objectives shows a tight connection with the well-studied notion of Adaptive Stochastic Quantization (ASQ).
We develop provably fast exact and approximate algorithms for our objectives. Our theoretical results inspire efficient practical algorithms that perform well across a variety of workload distributions. They also lead to practical algorithms for standard ASQ which are 2-10$\times$ faster than prior state-of-the-art methods while maintaining quality. These theoretical and empirical results contribute towards making adaptive quantization techniques more efficient and tractable in practical settings.

---


### 79. [Accurate Large-sample Uncertainty Quantification using Stochastic Gradient Markov Chain Monte Carlo](https://arxiv.org/abs/2606.00293)

**<font color=#1a73e8>作者：</font>** Yu Wang, Jie Ding, Jonathan H. Huggins  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tuning algorithms such as stochastic gradient descent (SGD) and stochastic gradient Langevin dynamics (SGLD) for approximate sampling and uncertainty quantification remains challenging, particularly in the practically relevant settings when the batch size is large or the model is misspecified. Existing theory that provides tuning guidance relies on continuous-time limits or strong statistical assumptions, which can become quantitatively inaccurate in these regimes. We address these shortcomings by proposing new discrete-time approximations to SG(L)D with and without momentum, which enables accurate predictions of the stationary covariance, iterate average covariance, and integrated autocorrelation time. Moreover, we prove quantitative, non-asymptotic error bounds showing that these estimates are sufficiently accurate for practical tuning and uncertainty quantification. Numerical experiments demonstrate that our theory yields improved tuning guidance across a range of models and data-generating distributions where existing approaches fail, including when using the $\beta$-divergence rather than log-loss to obtain statistically robust inferences.

---


### 80. [Uncovering Temporal Framing in the News](https://arxiv.org/abs/2606.00294)

**<font color=#1a73e8>作者：</font>** Tarek Mahmoud, Veronika Solopova, Premtim Sahitaj 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Temporal language does more than place events on a timeline. In news discourse, references to the past, present, and future can function as rhetorical devices that shape interpretation and persuasion. Here, we study temporal framing, defined as the persuasive use of time-related language to structure meaning rather than to report chronology. We propose a taxonomy of eight temporal frames grounded in prior work on temporality and framing, and we realize it through expert annotation of a multilingual news corpus. The resulting dataset includes 458 English and German news articles, with over 2K temporally framed sentences and approximately 3K temporal framing annotations identified from a corpus of more than 20K sentences. We analyze frame prevalence, co-occurrence patterns, and lexical cues, and evaluate temporal framing detection using supervised fine-tuning and zero-shot classification. Our experiments show that temporal framing is learnable at the sentence level, with supervised models substantially outperforming zero-shot approaches. We publicly release the corpus to support future research on temporal framing: this https URL.

---


### 81. [Adaptive Order Policies for Masked Diffusion](https://arxiv.org/abs/2606.00295)

**<font color=#1a73e8>作者：</font>** Jama Hussein Mohamud, Mohsin Hasan, Mirco Ravanelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion models have seen great success in capturing data distributions over discrete sequences in domains such as text and proteins. These models generate data by iteratively unmasking tokens starting from a fully masked sequence, with the unmasking order typically chosen at random or using a heuristic based on denoiser probabilities. In this work, we propose a scheme for learning the unmasking order using an additional lightweight policy network on top of a diffusion model. Our proposed loss reweights terms in the masked diffusion loss according to policy probabilities, and results in a policy that prefers positions where the denoiser is more likely to be correct. We study this loss in two settings: (i) training solely the policy while using a frozen pre-trained denoiser, and (ii) training the policy and denoiser jointly with the weighted loss to allow for mutual adaptation. We demonstrate that our approach outperforms common heuristics on problems that are sensitive to token ordering, such as combinatorial tasks and proteins.

---


### 82. [Real2SAM2Real: Generative 3D Caches as Complementary Context for Video Diffusion](https://arxiv.org/abs/2606.00299)

**<font color=#1a73e8>作者：</font>** Jiayi Wu, Haoming Cai, Cornelia Fermuller 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Video Diffusion Models (VDMs) excel at synthesizing high-fidelity videos, enabling precise camera and scene control remains challenging. Existing methods predominantly rely on implicit diffusion priors to generate unobserved regions, inevitably leading to structural collapse during high-dynamic movements or complex occlusions. To address this challenge, we propose Real2SAM2Real, a framework that leverages 3D lifting models (e.g., SAM3D) to extract an explicitly editable 3D cache, serving as a robust geometric scaffold for the VDM. By capturing the entire 3D volume of foreground entities rather than just their visible shells, this cache injects holistic spatial priors into the VDM, providing dependable 3D-aware guidance for complex scene dynamics. To effectively leverage this 3D guidance while preserving pre-trained priors, we design a Soft Spatial-Aligned Injection mechanism alongside a minimally invasive fine-tuning strategy tailored for VDMs. Furthermore, we employ masked normal maps as a cross-modal bridge to construct a 3D-free data curation and perturbation pipeline. Extensive experiments demonstrate that Real2SAM2Real enables precise, decoupled control over both camera trajectories and multi-entity motions. By utilizing the complementary context from generative 3D caches, our framework overcomes typical breakdowns caused by over-reliance on diffusion priors, maintaining exceptional spatiotemporal consistency under large camera shifts and severe occlusions. Crucially, by decoupling geometry from appearance, our VDM-tailored 3D cache eradicates perspective ambiguities caused by structural holes and erroneous facades, as well as misleading cues from reflections and refractions. Project website is available at this https URL

---


### 83. [FLaG: Fine-Grained Latent Grouping for Hallucination Detection](https://arxiv.org/abs/2606.00301)

**<font color=#1a73e8>作者：</font>** Wentao Ye, Liyao Li, Zhiqing Xiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hallucinations in large language models (LLMs) arise from heterogeneous failure mechanisms, making reliable detection difficult for any single global uncertainty score. In this work, we formulate hallucination detection as a mechanism-aware evidence aggregation problem, where diverse representation- and token-level signals must be interpreted under multiple latent explanations. We propose FLaG, a lightweight hallucination detection framework that models correctness through a set of latent evidence groups. Each instance is softly associated with multiple groups via an energy-based routing mechanism, and group-conditional reliability signals are combined through a principled log-marginal aggregation. This design enables FLaG to capture heterogeneous hallucination patterns while remaining invariant to decision thresholds and evaluation metrics. The framework operates as a frozen-model head, requires no modification to the underlying language model, and incurs minimal computational overhead. We further provide a theoretical perspective that connects FLaG to optimal evidence aggregation under heterogeneous error mechanisms, showing that the Bayes-optimal test statistic necessarily admits a log-marginal form and that FLaG constitutes a tractable approximation with a controllable error bound. Extensive experiments across multiple benchmarks and LLM backbones demonstrate that FLaG consistently achieves SOTA performance, while exhibiting robust transfer across datasets and models, and remaining effective under limited supervision.

---


### 84. [Modeling Spectral Energy Shifts in Spatio-Temporal Graph Anomaly Detection](https://arxiv.org/abs/2606.00304)

**<font color=#1a73e8>作者：</font>** Yilin Liu, Hongchao Zhang, Taylor T. Johnson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph anomaly detection methods aim to distinguish anomalous nodes. While prior methods characterize anomalies through increased variation in the spectral energy distributions, they overlook those that result in decreased variation, i.e., camouflaged anomalies that appear normal. We show that this type of anomaly persists across multiple datasets and remains undetectable by existing spectral approaches. To address this limitation, we propose a node-level spectral energy formulation that is fully compatible with message passing and enables the detection of camouflaged anomalies. Building on this formulation, we introduce an energy-aware graph learning framework that models spectral shifts through energy-driven message passing in both static and time-series graphs. Besides, our unified architecture extends to temporal settings without introducing specialized sequence modules, enabling efficient learning under long sliding windows. Extensive experiments on large-scale benchmarks demonstrate the effectiveness and scalability of our approach.

---


### 85. [Bridging Reasoning Trajectories in On-Policy Distillation via Near-Future Guidance](https://arxiv.org/abs/2606.00305)

**<font color=#1a73e8>作者：</font>** Yuxuan Jiang, Francis Ferraro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-Policy Distillation (OPD) improves large language model reasoning by training a student model on trajectories sampled from its own policy under teacher supervision. Although OPD operates on trajectories, its learning signal remains token-level: it identifies deviations through high-loss tokens and repairs them through local reverse-KL correction. We show that this "trajectory-sampled but token-learned" mechanism cannot reliably bridge student trajectories toward teacher trajectories. About 30% of high-loss tokens fall into the low-divergence regime, indicating that many are surface-form mismatches rather than real reasoning forks. Moreover, even truly divergent tokens are difficult to repair with isolated token-level supervision, since reasoning failures often unfold as short-horizon distributional drift. We propose Trajectory-aware OPD (TOPD), which uses near-future trajectory information to identify real divergent states and distribute guidance across multiple future tokens. Experiments show that suppressing non-divergent high-loss tokens improves standard OPD from 47.8% to 48.2% average accuracy, while TOPD further improves performance to 52.2%, with gains on AIME24 from 60.0% to 63.3% and AIME25 from 46.7% to 53.3%.

---


### 86. [Large-scale Uncertainty Quantification for Latent Variable Models Using Subsampling Markov Chain Monte Carlo](https://arxiv.org/abs/2606.00309)

**<font color=#1a73e8>作者：</font>** Xiaoyu Wang, Jonathan H. Huggins  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic gradient Langevin dynamics combined with Gibbs updates (SGLD--Gibbs) provides a highly scalable approach to approximate Bayesian inference in latent variable models. However, it remains unclear how to tune the algorithm's hyperparameters in a principled manner to ensure the uncertainty estimates are statistically meaningful. In this work, we address this gap in tuning guidance by developing a statistical scaling limit theory for SGLD--Gibbs. We derive a joint asymptotic limit for the global parameters and latent variables under appropriate space-time rescaling. We show that global parameters converge to a diffusion-type limit, while each latent variable converges to a jump process, reflecting the use of intermittent Gibbs updates. This joint jump-diffusion structure reveals how latent-variable randomness contributes to the stationary distribution of the global parameters. We leverage our results to propose explicit guidance on hyperparameter tuning for SGLD--Gibbs that ensures meaningful uncertainty quantification. Numerical experiments show that SGLD--Gibbs with our tuning guidance leads to better parameter estimates, uncertainty quantification, and predictive performance than stochastic variational inference.

---


### 87. [Where to Refine, When to Stop: Rethinking Redundancy via Latent Discrepancy for Efficient Visual Autoregressive Generation](https://arxiv.org/abs/2606.00310)

**<font color=#1a73e8>作者：</font>** Changwang Mei, Peisong Wang, Zekun Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Autoregressive (VAR) models deliver high-quality image generation but suffer from significant inference latency at high resolutions. Recent acceleration approaches most rely on heuristic measures with layer features to prune tokens. Such heuristics are sensitive to complex contextual semantics, leading to inaccurate identification of redundant computation and poor adaptability across prompts. We rethink redundancy in VAR from the perspective of its impact on pixel-space generation and introduce Latent Discrepancy. This unified metric quantifies a token's contribution by measuring the change in model states during generation. Our analysis shows that redundancy is more accurately identified when guided by image latent or pixel-space signals. We further observed that in classifier-free guidance (CFG), the convergence trend of the discrepancy between conditional and unconditional branches exhibits high dynamics with different prompts. Based on these findings, we propose LD-Pruning (Latent Discrepancy Pruning), a training-free framework that removes redundancy via latent discrepancy by integrating decoding-free region selection and adaptive unconditional-branch skipping. Extensive experiments show that LD-Pruning substantially reduces inference latency while maintaining high generation quality, achieving up to 2.35x speedup on Infinity-8B.

---


### 88. [Perturbative methods for non-parametric instrumental variable](https://arxiv.org/abs/2606.00322)

**<font color=#1a73e8>作者：</font>** Wei Bu, Arthur Gretton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a perturbative approach for nonparametric instrumental variable (NPIV) estimation. By drawing inspiration from perturbation theory in physics, we extend standard kernel ridge methods with systematic higher perturbation order corrections that significantly improve estimation accuracy. Spectrally, the perturbation introduces mixing between different eigenmodes of the expectation integral operator, which becomes especially useful when the integral equation is ill-defined. One source for such ill-definedness can be the curse of dimensionality. Our method performs across various dimensionality regimes, particularly when the dimensionality parameter $\beta$ which is defined through the number of samples $n$ and dimension $d$ as $n^\beta = d$, becomes large. Experimental results show that our first-order perturbative corrections can reduce prediction error by up to 99\% in high-dimensional ill-defined cases ($\beta > 0.7$) compared to standard ridge regression approaches. The performance improvement is maintained across a wide range of dimensions, with the advantage becoming more pronounced as dimensionality increases.

---


### 89. [KG-Guard: Graph-Based Hallucination Detection for Knowledge Base Question Answering](https://arxiv.org/abs/2606.00328)

**<font color=#1a73e8>作者：</font>** Albert Sawczyn, Piotr Bielak, Tomasz Kajdanowicz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for knowledge base question answering (KBQA), where answering requires selecting entities from a question-specific knowledge-graph subgraph. Yet LLMs are known to hallucinate across tasks, and KBQA is no exception: even when we provide a graph as the knowledge source, the model may rely on parametric knowledge instead of graph evidence or perform invalid reasoning over the given relations. Such hallucinated answer nodes can limit the practical deployment of KBQA systems, especially in high-stakes domains such as healthcare. We formulate hallucination detection in KBQA as an answer-node classification problem and propose a lightweight graph-based framework that treats the answering LLM as a black box. \methodname represents each KBQA instance as an augmented graph. It initializes node features with semantic representations of KG entities, marks topic entities and LLM-proposed answer nodes with learned vectors, and connect a virtual question node to the topic entities. A graph encoder then produces verification-oriented node representations, and a small MLP classifies each proposed answer node using its graph representation together with the question embedding. Experiments on WebQSP, ComplexWebQuestions, and PUGG show that our detector achieves the highest F1 on all three benchmarks ($82.0$, $87.4$, and $84.3$), outperforming LLM-as-judge and sampling-based baselines, while having $\sim305\times$ fewer parameters than the reference approaches. Beyond detection, the node-level feedback is actionable: when flagged answers are fed back to the KBQA system for iterative refinement, downstream KBQA F1 improves by $13.0$--$14.5$ points and Exact Match by $16.9$--$17.6$ points.

---


### 90. [From Noise to Control: Parameterized Diffusion Policies](https://arxiv.org/abs/2606.00336)

**<font color=#1a73e8>作者：</font>** Renhao Zhang, Haotian Fu, Mingxi Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose Parameterized Diffusion Policy (PDP), a framework for learning diffusion policies conditioned on low-dimensional, continuous parameters embedded in a learned behavior manifold. By constructing this manifold so that distances between latent representations reflect the semantic similarity between physical trajectories, we transform diffusion from a mechanism for stochastic diversity into a precise and optimizable tool for behavior steering. Our approach enables smooth interpolation between known strategies and efficient adaptation to novel constraints without updating policy weights. We demonstrate that PDP significantly improves adaptation performance on complex multimodal benchmarks in both simulated and real-robot experiments compared to standard diffusion policies, particularly in scenarios requiring the synthesis of novel behaviors.

---


### 91. [CHAM-net: A Contrastive Hierarchical Adaptive Meta-network for Robust Global Methane Flux Prediction](https://arxiv.org/abs/2606.00338)

**<font color=#1a73e8>作者：</font>** Rongchao Dong, Yiming Sun, Shuo Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Methane is a potent greenhouse gas that significantly contributes to global warming. However, accurately estimating global methane emissions and consumption remains challenging due to the complex interactions among environmental drivers that may vary across spatial and temporal scales. Prior data-driven methods often overlook the inherent spatiotemporal heterogeneity of ecosystems, failing to explicitly capture site-specific characteristics and cross-year evolutionary dynamics. To address these issues, we propose the Contrastive Hierarchical Adaptive Meta-network (CHAM-net), a novel framework that explicitly learns from historical context to capture site-specific dynamics. CHAM-net employs a hierarchical encoder-decoder architecture, in which the encoder captures site-specific characteristics from historical data and then dynamically conditions the decoder to generate the final prediction. Experimental results demonstrate that CHAM-net consistently outperforms all baseline methods on both simulation and observational datasets for methane emission and consumption, achieving nRMSE values as low as 0.43 and 0.88 with corresponding R2 scores up to 0.97 and 0.68 for emission prediction.

---


### 92. [Balancing Learning Rates Across Layers: Exact Two-Step Dynamics and Optimal Scaling in Linear Neural Networks](https://arxiv.org/abs/2606.00340)

**<font color=#1a73e8>作者：</font>** Tianyu Pang, Vignesh Kothapalli, Shenyang Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study optimal learning-rate selection in two-layer and three-layer linear neural networks trained to learn linear target functions. In particular, we derive the exact closed-form expressions for the gradients and test loss after one and two steps of gradient descent, enabling a precise characterization of early training dynamics. We characterize how learning rates should scale under the gradient approximation in the first two steps, and prove that performing updates with this approximation yields a tractable surrogate loss with a tight, small approximation error. This formulation enables the theoretical analysis of layer-wise learning rates and reveals a distinct early-training regime: test loss can be minimized by unequal learning rates at the initial step, while equal learning rates become optimal in subsequent steps. Our numerical experiments validate the theory and demonstrate the importance of balancing layer-wise learning rates early during training. The code is available at: this https URL.

---


### 93. [ROGUE: Misaligned Agent Behavior Arising from Ordinary Computer Use](https://arxiv.org/abs/2606.00341)

**<font color=#1a73e8>作者：</font>** Jeremy Tien, Abishek Anand, Yu-Rou Tuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As AI agents are increasingly deployed in real personal and corporate settings (email accounts, development workflows, company databases, etc.), safety considerations surrounding these agents become paramount. Although much work has focused on agent safety in the presence of an adversary, we show that agents can exhibit misaligned behavior even in benign settings, taking unsafe actions when those actions are instrumental to task completion. We study this failure mode through the lens of corrigibility, the safety desideratum that agents remain amenable to human correction, interruption, or shutdown. To demonstrate this tendency, we introduce a benchmark in which agents are asked to complete realistic, computer-use tasks but are confronted with a corrigibility obstacle: a human interrupt, a login page, or a shutdown notification. We then evaluate whether agents choose to violate corrigibility in order to complete the task -- overriding the human, accessing private passwords, rewiring shutdown. We find that the overwhelming majority of frontier models tested frequently bypass user interruptions or restrictions. In addition, better model performance appears to lead to greater misalignment. Finally, even when models are completely corrigible initially, we show there are no guarantees that the subagents they create are. Our work highlights the critical need for principled, corrigibility-focused alignment methods in autonomous agents.

---


### 94. [PE-means: Improved Differentially Private $k$-means Clustering through Private Evolution](https://arxiv.org/abs/2606.00342)

**<font color=#1a73e8>作者：</font>** Thomas Humphries, Zinan Lin, Sergey Yekhanin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of differentially private (DP) $k$-means clustering in Euclidean space. Previous solutions rely on summing the private data directly, which induces a sensitivity proportional to the domain. We introduce PE-means, an extension of the private evolution (PE) algorithm (an increasingly popular method for synthetic data generation), to the problem of $k$-means clustering. The key advantage of PE is that it only computes a private histogram with constant sensitivity to guide the evolution. Our adaptation of PE includes new evolutionary operators for clustering, as well as other algorithmic improvements of independent interest. Overall, PE-means achieves an average improvement of 20% in clustering loss over state-of-the-art baselines.

---


### 95. [The role of class encoding in neural collapse](https://arxiv.org/abs/2606.00344)

**<font color=#1a73e8>作者：</font>** Bastien Massion, Roy Makhlouf, Estelle Massart  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural collapse is a structural property of the last-hidden-layer activations in neural network classification models, when trained beyond a zero classification error. In this work, we explore the role of label encoding in neural collapse by relying on the unrestricted feature model with mean squared error training loss. We demonstrate that, for one-hot encoded labels and balanced data, the uncentered mean features associated with each class transition from a simplex equiangular tight frame to an orthogonal frame when increasing the bias regularization coefficient associated with the final classifier. These structures are reminiscent of the orthogonal frame structure of one-hot encoded labels. For any arbitrary encoding, we also show that the final classifier's bias aims at centering the labels, compensating for the discrepancy between the global mean of the labels and the origin. We further discuss the role of the encoding in other neural collapse properties.

---


### 96. [(HB-ARFM) History-Bootstrapped Flow Matching for Inverse Boiling Reconstruction](https://arxiv.org/abs/2606.00349)

**<font color=#1a73e8>作者：</font>** Xianwei Zou, Sheikh Md Shakeel Hassan, Arthur Feeney 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing spatiotemporal fields from partial observations is fundamental to scientific inference, from inferring atmospheric states from satellite data to recovering fluid states from imaging. When observations are incomplete, the inverse problem is fundamentally ill-posed: even when the underlying PDE dynamics are Markovian in the full state, partial observation operators induce a non-Markovian posterior that cannot be resolved from a single timestep. We propose a history-bootstrapped autoregressive flow matching (HB-ARFM) for spatiotemporal inverse reconstruction under partial observability. Observation history bootstraps the initial reconstruction via conditional flow matching, reducing ambiguities. The same conditional transport model is then applied autoregressively, conditioning on both new observations and past predictions to propagate the reconstruction forward in time. We evaluate the method on boiling dynamics reconstruction, recovering full velocity and temperature fields from interface geometry and motion. Across two inverse tasks with varying observation sparsity, HB-ARFM produces physically and temporally valid reconstructions where other models fail.

---


### 97. [Drift Q-Learning](https://arxiv.org/abs/2606.00350)

**<font color=#1a73e8>作者：</font>** Anas Houssaini, Mohamad H. Danesh, Amin Abyaneh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning requires improving a policy from fixed data while avoiding out-of-distribution actions with unreliable value estimates. Diffusion and flow policies handle this trade-off by modeling the behavior distribution to regularize the RL objective, but they require iterative denoising, solver integrations, and in more efficient variants, distillation or other approximations at inference. We propose DriftQL, which combines a drift-based behavioral regularizer with critic-driven policy improvement. The value signal biases the policy toward high-value regions of the data support, while attraction and repulsion together keep generated actions near the data and prevent collapse onto a single mode. DriftQL is implemented as a single network with a unified training objective and generates actions in a single forward pass. On D4RL and OGBench, DriftQL consistently outperforms diffusion and flow methods, advancing the state of the art. Under degraded data quality, where the baselines visibly struggle, DriftQL remains close to its clean-data performance, positioning it as a promising alternative to diffusion and flow-based methods while maintaining the simplicity and efficiency of deterministic approaches. Project page: this https URL

---


### 98. [UniVerse: A Unified Modulation Framework for Segmentation-Free,Disentangled Multi-Concept Personalization](https://arxiv.org/abs/2606.00351)

**<font color=#1a73e8>作者：</font>** Quynh Phung, Sandesh Ghimire, Minsi Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized visual understanding has advanced significantly, yet existing approaches struggle to localize and extract specific concepts when input images contain multiple objects. Many prior methods rely heavily on segmentation-based supervision or exhibit poor compositional generalization, limiting their ability to accurately disentangle and manipulate individual concepts. In this work, we propose UniVerse, a Unified Modulation Framework for segmentation-free, disentangled multi-concept personalization in diffusion transformers. Our method allows for composable and decomposable concept extraction, enabling fine-grained localization and representation of target objects without explicit segmentation masks. UniVerse learns to decompose complex scenes into concept-specific representations and then compose them in a unified manner, enabling robust personalization across diverse visual contexts. Through extensive experiments on multiple benchmarks, we demonstrate that UniVerse significantly outperforms state-of-the-art baselines in both localization accuracy and visual fidelity. Qualitative and quantitative results show that our approach can precisely extract target concepts in cluttered scenes, paving the way for more flexible, interpretable, and personalized visual generation and understanding.

---


### 99. [HiGS: A Hierarchical Rendering Architecture for Real-Time 3D Gaussian Splatting](https://arxiv.org/abs/2606.00352)

**<font color=#1a73e8>作者：</font>** Dawid Pająk, Martin Bisson, Rodolfo Lima  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has become the standard for real-time novel view synthesis on commodity GPUs. Its pipeline ties spatial partitioning and rasterization to one tile size, yet the two pull in opposite directions: partitioning, which bins and depth-sorts gaussians, grows cheaper with larger tiles, while rasterization gets cheaper with smaller ones. Prior acceleration work reduces the cost of individual stages but keeps both locked to that single scale, where a few dense tiles dominate frame time. We present Hierarchically Tiled Gaussian Splatting (HiGS), which gives each its own scale: partitioning runs over coarse macro-tiles, while rasterization runs over the fine render tiles within them. Rasterization work is then issued in proportion to the gaussians in each macro-tile rather than per tile, so dense regions spread across many parallel units instead of serializing through one. Across tested scenes, HiGS renders up to 15.8x faster than the original 3DGS and outperforms every other rasterizer we evaluate, while preserving exact front-to-back alpha compositing.

---


### 100. [How Far Do Auto-Interpretation Labels Generalize: A Controlled Study Across Languages, Scripts, and Rewordings](https://arxiv.org/abs/2606.00356)

**<font color=#1a73e8>作者：</font>** Sripad Karne  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoder (SAE) features are increasingly used to interpret language models, with auto-generated natural-language labels serving as the primary interface for understanding what each feature represents. We ask whether these labels generalize: does a feature labeled for a concept actually track that concept across languages and scripts? Using Serbian digraphia as a controlled testbed -- the same language written in both Latin and Cyrillic via deterministic transliteration -- we first find that SAE feature sets activated by the same content in different languages, scripts, and wordings share substantial overlap (peak Jaccard similarity 0.57 vs.\ 0.13 random baseline), suggesting genuine cross-lingual semantic features. We then test whether auto-interpretation labels keep pace. They often do not: features whose labels describe semantic content miss the same meaning in Serbian up to $4\times$ more often than within English, and miss Serbian Cyrillic more than Serbian Latin -- two scripts that are deterministic transliterations of each other -- suggesting the failures track how well each form is represented in training. The gap grows with network depth, yet the labels give no indication that they fail. These results suggest that auto-interpretation labels may reflect a feature's behavior on well-represented inputs rather than the concept itself.

---


> [!TIP]
> 当前位于：**51-100**（第 2/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
