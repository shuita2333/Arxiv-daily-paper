# 📦 其他研究 | 2026年11月11日

> 本类共 **520** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

---

### 201. [Robust and Efficient Continual Model Merging via Global Singular Subspace Separation and Restoration](https://arxiv.org/abs/2611.10881)

**<font color=#1a73e8>作者：</font>** Juncheol Shin, Byeongho Yu, Semin Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual model merging incrementally integrates task-specific models without revisiting past models or data. However, repeated merging entangles past task components and distorts their singular geometry, making balanced task-wise allocation increasingly difficult. We propose Global Singular Subspace Separation and Restoration (GS3R), which augments the merged update with a compact restoration state. At each merge, GS3R restores the retained singular geometry, separates task-wise subspaces, and globally reallocates the available rank across tasks fairly. To reduce merging-time memory overhead, we further introduce Pre-merge Restoration and Flushing (PRF). Experiments on vision, NLP, and multimodal benchmarks show that GS3R provides a strong accuracy-efficiency trade-off.

---


### 202. [Complementarity without ground truth?](https://arxiv.org/abs/2611.10893)

**<font color=#1a73e8>作者：</font>** Andrea Ferrario, Alessandro Facchini, Federico Cabitza  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human-AI complementarity captures the idea that a human assisted by an AI system can outperform both the human and the AI acting alone. In prediction tasks, this improvement is assessed against ground truth labels produced through a reference construction procedure and intended to represent the state of affairs to be predicted. Many human-AI interactions, including those where medical AI provides treatment recommendations, however, concern tasks other than predicting what obtains. Their relevant output concerns adequacy relative to a practical goal and depends on several evaluative dimensions. In this work, we examine the ground truth dependence of complementarity and extend it to human-AI interactions where ground truth is not the appropriate reference. We show that tasks beyond prediction can still admit a reference construction procedure that generates adequacy labels. We develop a route for extending complementarity to such settings. It replaces ground truth labels with context-dependent adequacy labels generated through a two-step scoring methodology inspired by multi-criteria decision analysis frameworks in healthcare and it makes the normative choices underlying reference construction explicit. Because the construction of adequacy labels embeds evaluative choices, we draw methodological inspiration from computational reliabilism to identify technical, scientific, and social factors relevant to supporting their construction. Our approach expands the empirical study of human-AI complementarity beyond prediction tasks, enabling its quantitative evaluation in decision-support settings where ground truth is not the appropriate evaluative reference.

---


### 203. [Robust Satisficing Ensemble: Scalable Model Aggregation Under Distribution Shifts](https://arxiv.org/abs/2611.10895)

**<font color=#1a73e8>作者：</font>** Ahmet Faruk Cetinkaya, Enes Agirman, Cem Tekin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard ensemble methods can improve robustness by mitigating individual model stochasticity, but they frequently fail to generalize beyond the training distribution, leaving systems vulnerable to out-of-distribution (OOD) data. We introduce the Robust Satisficing Ensemble (RSE), a scalable probabilistic aggregation framework designed to secure model combinations by minimizing their fragility against distributional changes. By bridging a robust satisficing objective with a quadratic risk surrogate, RSE derives an analytical inner adversary. This fundamental reformulation enables highly efficient weight updates without the computational bottleneck of standard minimax optimization, crucially decoupling optimization complexity from sample size to scale effectively to large datasets. In particular, we prove a geometrically decaying truncation error for the fragility approximation via Lagrange-Burmann expansion and establish stationarity guarantees for RSE. We evaluate RSE across a comprehensive spectrum of distribution shifts, including adversarial label shift (SST-5, TREC), natural subpopulation and temporal shifts (CivilComments, HuffPost). Our results demonstrate that RSE consistently outperforms strong robust baselines, including GroupDRO, IRM, and SRM. These findings establish RSE as a practical, theoretically grounded safeguard for reliable model aggregation in dynamic environments.

---


### 204. [Optimal Byzantine-resilient Federated Learning with User-level Differential Privacy](https://arxiv.org/abs/2611.10898)

**<font color=#1a73e8>作者：</font>** Ming Xiang, Stratis Ioannidis, Edmund Yeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world deployment of federated learning (FL) requires resilience against adversarial clients and data privacy. Byzantine fault captures the worst-case behavior of adversarial clients, while differential privacy (DP) provides statistical guarantees against privacy loss. In particular, user-level DP guards a client's entire contribution and provides more realistic protection against information leakage. Despite intensive efforts, the minimax-optimal convergence bound of Byzantine-resilient FL with user-level DP remains open. We establish an information-theoretic lower bound for any Byzantine-resilient empirical risk minimization problem under user-level DP and heterogeneous clients. We propose ByzULDP, a central DP algorithm featuring a two-level momentum across the client and server. Client-side momentum mitigates stochastic gradient variance during robust aggregation. Unlike the fault-free case, naively combining non-linear Byzantine-resilient aggregation with central DP noise can be insufficient to guarantee convergence to a bounded neighborhood of a stationary point. Our key contribution is a server-side momentum that leverages a property specific to user-level DP, where privacy sensitivity depends on how client updates are constructed, to empower convergence. ByzULDP achieves the order-optimal convergence bound for strongly-convex objectives, with vanishing error terms decaying at the optimal $O(1/T)$ and $O(1/\sqrt{T})$ rates for strongly-convex and non-convex objectives, respectively. We corroborate our analysis with numerical experiments on real-world datasets across diverse privacy budgets.

---


### 205. [How Short Is Too Short? Length-Conditional Calibration and Abstention for Detecting AI-Generated Text](https://arxiv.org/abs/2611.10901)

**<font color=#1a73e8>作者：</font>** Ritesh Janga, Justin Zhan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Detectors of AI-generated text are usually tuned and tested on passages of several hundred tokens, yet many real cases are short. We study score-based detection as a function of passage length. We give a closed form for how the false-positive rate of a threshold set on long text changes as length falls, and a formula for the number of tokens a detector needs to reach a target true-positive rate. We calibrate thresholds within length bins with conformal p-values, and we add a bin-level rule that abstains when the detector cannot be informative at that length. On synthetic scores the formulas agree with simulation, and binned calibration holds the false-positive rate at its nominal value at every length. On three zero-shot detectors (log-likelihood, log-rank, Binoculars), three corpora and two open-weight generators, binned calibration gives a mean false-positive rate of 5.0% in every detector-length cell from 10 to 200 tokens, averaged over 300 random document-level resplits. A single threshold set at 200 tokens gives 29% for Binoculars at 10 tokens and about 1% for log-likelihood, as the closed form predicts. No detector reaches an 80% true-positive rate, and the best, Binoculars at 200 tokens, reaches 59%, so the rule abstains in every cell at that floor and releases only the 200-token bins at floors of 0.3 and 0.5.

---


### 206. [Prescriptive Learning of Linear Policies with Feasibility Guarantees for Binary Decision-Making](https://arxiv.org/abs/2611.10923)

**<font color=#1a73e8>作者：</font>** Farzaneh Pourahmadi, Trine Krogh Boomsma, Pierre Pinson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Binary decision-making under uncertainty arises across a wide range of applications, including energy systems scheduling, transportation, and workforce planning. While machine learning has been increasingly applied to accelerate or replace mixed-integer solvers in such settings, existing approaches rely on predictive learning, training models to reproduce optimal decisions from labeled data, which lacks knowledge of counterfactual outcomes and provides no guarantees that the resulting decisions will be feasible. This limitation is further compounded under distributional shift, where policies trained on historical data may produce systematically infeasible decisions. We propose a prescriptive learning framework for binary decision-making that addresses both limitations. Rather than predicting optimal labels, the framework jointly optimizes over linear decision policies and feasible assignments across all training scenarios, allowing feasible alternatives and their operational performance to be considered directly during training. We further extend the framework to a distributionally robust chance-constrained formulation using a Wasserstein ambiguity set, which enforces feasibility with a prescribed probability under the worst-case distribution in the ambiguity set and enables a tunable trade-off between robustness and solution quality. We demonstrate the framework on two case studies, namely a unit commitment problem and a staff allocation problem. Out-of-sample experiments under test distributions that either match or differ from the training distribution show that the robust model is more conservative when the two distributions coincide, while under distributional shift it substantially reduces unmet demand and lowers total cost by up to 76.5% relative to classical predictive learning.

---


### 207. [Gendered Misclassification from Surname-Based Race Imputation](https://arxiv.org/abs/2611.10931)

**<font color=#1a73e8>作者：</font>** Noah Dasanaike  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Researchers increasingly estimate political behavior based on race and gender from voter files, where race is imputed from surnames and geography. This only works where surnames suggest group membership, an assumption violated where surnames follow norms around marriage. Imputation is therefore biased against women who adopt their husband's surname, especially those who racially inter-marry, an outcome itself endogenous to partisanship. Using six US states recording self-reported race, I show that imputation is less accurate for Asian and Hispanic women, particularly those sharing the surname of a partner of another race, who differ politically from other women of their race. This violates assumptions behind downstream inference approaches, which nearly double the gender gap in partisanship among Asian voters. I derive an expression showing the bias is largest where a group is small. Using maiden rather than marriage-adopted surnames in North Carolina raises accuracy up to fourfold for women married across racial lines. Recovering maiden surnames, or omitting the married surname, removes much of the bias. In a national replication of a study of gender gaps in turnout, the correction more than triples the gap among Asian voters. In Lebanon, where wives register in their husband's locality, the error enters through geography.

---


### 208. [Can small transformers learn the language of Coxeter groups?](https://arxiv.org/abs/2611.10936)

**<font color=#1a73e8>作者：</font>** J. Elisenda Grigsby, Yiyao Huang, Arushi Katyal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The field of mechanistic interpretability is well-suited to collaborative projects between mathematicians and AI researchers. This work describes one such project. We trained a small transformer to learn the language of the Coxeter group affine A2, best known as the symmetries of the tiling of the Euclidean plane by equilateral triangles. We then formulated and proved a word-theoretic conjecture about affine A2 after observing the attention patterns of the trained model.

---


### 209. [CoupledFlow: One-Step Neural Operators for Coupled Multi-Physics PDEs](https://arxiv.org/abs/2611.10945)

**<font color=#1a73e8>作者：</font>** Trong Khiem Tran, Minh Long Bui, Phi Le Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces COUPLED FLOW, a new neural operator learning framework for multi-physics PDE systems that captures the co-evolution of multiple physical processes by modeling their cross-process interactions. Unlike existing neural operator methods that primarily target single-physics settings, COUPLED FLOW employs a novel structure-constrained flow matching algorithm to learn process- specific mean velocity fields conditioned on the full multi-physics state. This enables fast and accurate one-step prediction of coupled PDE systems that would otherwise require expensive numerical simulations. A key challenge in training COUPLED FLOW however lies in sampling structure-constrained conditional flow interpolants that capture cross-process correlations and serve as training examples for flow matching. To address this challenge, we derive a multi-physics mean-flow consistency identity that characterizes cross-process interactions and defines the structure-constrained mean-flow matching loss. To provide informative training samples for flow matching with this loss, we develop a principled method for sampling correlated conditional interpolants based on posterior multi-output Gaus- sian processes, which capture richer cross-process correlations than the commonly used endpoint-conditioned linear interpolants. We also establish a theoretical re- sult showing that the Wasserstein-2 distance between the predicted and oracle PDE solution distributions is upper-bounded in terms of the structure-constrained flow matching loss and the smoothness of the learned flow. Experiments across diverse coupled PDE benchmarks demonstrate that COUPLED FLOW consistently outperforms existing state-of-the-art neural operators and generative PDE solvers.

---


### 210. [Validating AI-Discovered Cloud Threats on Live Infrastructure: A Multi-Model, Multi-Cloud Study](https://arxiv.org/abs/2611.10947)

**<font color=#1a73e8>作者：</font>** Nicholas Pecka, Lotfi Ben Othmane, Renee Bryce  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud infrastructure threat modeling lacks empirical validation of AI-discovered threats. We present a three-phase methodology of multi-agent threat discovery, automated exploit synthesis, and non-destructive live validation, and apply it to three commercial foundation models on two cloud architectures, validating each threat natively on the cloud (AWS, GCP, or Azure) it was discovered against. Of 233 AI-discovered threats, 103 were confirmed and 34 refuted (75.2\% precision, 95\% CI [67.3, 81.7]); 44 were conditional (the named mechanism refuted but an equivalent impact shown through another path) and 52 indeterminate. Multi-model discovery helped through breadth, not agreement: the three models together found 2.2$\times$ the confirmed threats of the best single model at comparable precision, while threats reported by several models were confirmed no more often than single-model ones. False positives were not architecture-specific: they asserted access or system state the deployment did not have. Threats coded in advance as observable configuration resolved cleanly more often than multi-step behavioral threats (72.5\% vs.\ 51.6\%), which were more often conditional, suggesting that models more often misidentify the exploitation mechanism than the underlying weakness. AI-assisted discovery is a practical input to security workflows when paired with empirical validation.

---


### 211. [Interpretable Cyber-Physical Attack Detection in Smart Grids: A Leakage-Controlled Multi-Testbed Evaluation of Fusion, Robustness, and Observability Limits](https://arxiv.org/abs/2611.10950)

**<font color=#1a73e8>作者：</font>** Muhammad Ridwanul Hoque, Sarah Sharif, Reza Saeed Kandezy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cyber-physical smart-grid detectors are typically treated as black boxes and validated exclusively on clean, temporally shuffled datasets, which risk overly optimistic performance claims. This work presents a multi-testbed evaluation study built around an interpretable, time-windowed fusion Random Forest, adopting the pessimistic result whenever evaluation protocols disagree. (i) On a public paired cyber-physical dataset, shuffled cross-validation is optimistic: macro-F1 falls from 0.96 to 0.88 +/- 0.06 under rolling-origin temporal evaluation. A topology-free graph convolutional network (GCN) serving as a control confirms that this lightweight model is competitive on these splits. (ii) The adaptive and adaptive-joint feature-space attacks, which are infeasible as realistic grid manipulations, degrade macro-F1 to 0.67 and 0.34, respectively. Adversarial training and randomized smoothing partially restore performance, and a physics-constrained evolution-strategy evasion on the IEEE 14-Bus testbed shows the same vulnerability pattern. (iii) On real IEC-104 traffic, the cyber view reliably catches structural attacks (recall of 0.87 to 0.98) but largely fails on semantic value manipulation (recall of 0.11 to 0.35). An observability taxonomy on the IEEE 14-Bus system reveals that stealthy false data injection defeats all three observation views. (iv) On a full AC weighted least-squares state-estimation testbed, a forecasting-aided temporal test is evaded by slow ramps precisely where a rate-invariant physics-manifold test sustains detection at a common 5% false-alarm target. A full end-to-end evaluation on IEEE 118-Bus confirms the ordering but bounds its strength: the manifold test detects every trial down to 0.05 degree/step and 0.48 at 0.02 degree/step, against 0.14 for the temporal test. All code and benchmarks are released.

---


### 212. [Improving Analytic Constants via Interpretable AI-Guided Lean Proof Refinement](https://arxiv.org/abs/2611.10961)

**<font color=#1a73e8>作者：</font>** Rahul Saha, Alan Li, Anton Xue 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly capable of discovering new mathematical results, yet their reasoning and generated proofs can be difficult to understand and verify. We introduce an interpretable framework for AI-guided mathematical discovery, focused on improving quantitative bounds on analytic constants. Our key insight is that existing proofs often contain slack in intermediate lemmas, which can be tightened without reconstructing the entire argument. To exploit this structure, we represent proofs as partially-formalized Lean blueprints: human-interpretable dependency graphs of definitions, lemmas, and theorems. An AI agent then iteratively refines the Lean code while preserving the blueprint's dependency structure, allowing local improvements to automatically propagate to a verified final bound. This interpretable structure allows humans to inspect the agent's refinements and understand how local improvements propagate to the final theorem. For Grothendieck's constant ($\mathcal{K}_G$), we obtain $$
\mathcal{K}_G \leq
\frac{\pi}{2\log(1+\sqrt{2})} - 10^{-17}, $$ an explicit numerical improvement over Krivine's 1977 bound. For Korenblum's constant ($\mathcal{K}_K$), we obtain $$
\mathcal{K}_K \geq 0.356565, $$ improving Wang's 2025 bound of $0.3554$. Our experiments demonstrate the potential of both partial formalization and iterative agentic refinement for interpretable mathematical discovery.

---


### 213. [PQC-Corpus: A Dataset of Linked Development Histories for Post-Quantum Cryptography](https://arxiv.org/abs/2611.10966)

**<font color=#1a73e8>作者：</font>** Souhardya Saha Dip, Moshood A. Fakorede, Umar Farooq  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As post-quantum cryptography (PQC) standards evolve, developers must adapt implementations, tests, and protocols. Studying this work requires connecting code changes to problem reports and developer reviews. We present PQC-Corpus, a dataset of linked development histories from 179 public GitHub repositories, spanning cryptographic libraries and general-purpose projects. It connects issues and closing pull requests to commits and full patches, with comments and reviews. We combine Git histories with GitHub threads, reconstruct 23 pull-request commit lists truncated at 250 entries, and check file integrity, schemas, and links. Two annotators independently assessed sampled commits and issues ($\kappa=0.86$ and $0.93$), labeling about seven in ten commits and two in three issues PQC-related within these samples. We provide full and filtered views with removal ledgers, and quantify how filtering reduces links from issues to commits. A patch-free view supports inspection before downloading patches, while traversal scripts follow issues to code changes. We make the dataset and collector publicly available for studies of specification changes, hybrid interoperability, cryptographic review, and migration assistance.

---


### 214. [JUBILEE: A Benchmark Environment for Off-Policy Evaluation in Debt Collections](https://arxiv.org/abs/2611.10972)

**<font color=#1a73e8>作者：</font>** Diego Silva Prado, Tiago Amaral Penteado de Jesus, Bruno Caldas de Souza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-policy evaluation (OPE) estimates the value a candidate decision policy would achieve, using only data logged by the policy already in production. In debt collections, unrecorded factors can influence both actions and outcomes. This paper presents JUBILEE, a benchmark environment built around a debt-collections simulator that generates million-loan panels with competing risks, rare recovery events, and hidden factors driving both outcomes and assignment. The evaluation includes an 80-run comparison of tabular and gradient-boosted estimators under two synthetic outcome mechanisms and a 190-run parameter grid. Independent policy simulations provide reference values with estimated Monte Carlo uncertainty for a synthetic reward score and for simulated cash. With hidden factors influencing action assignment, several tabular methods agree closely while underestimating the field-visit policy's score, an error that also appears with boosted models. Intervals from tabular doubly robust estimation usually contain the reference without hidden assignment dependence but mostly miss it when that dependence is present. Estimates from randomized decisions do not show the same large error, although their limited precision leaves policy choice uncertain. The decision consequences depend on how policy value is defined. The field-visit policy ranks last under the score and first under simulated cash, which excludes channel costs. Under cash, log-based estimators miss this best candidate in nearly every run with hidden assignment dependence in the paired study. JUBILEE supports reproducible study of these failure modes under specified collections mechanisms.

---


### 215. [An Analysis of Reinforcement Learning with Function Approximation](https://arxiv.org/abs/2611.10981)

**<font color=#1a73e8>作者：</font>** Francisco S. Melo, Sean P. Meyn, M. Isabel Ribeiro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the problem of computing the optimal Q-function in Markov decision problems with infinite state-space. We analyze the convergence properties of several variations of Q-learning when combined with function approximation, extending the analysis of TD-learning in Tsitsiklis and Van Roy (1996) to stochastic control settings. We identify conditions under which such approximate methods converge with probability 1. We conclude with a brief discussion on the general applicability of our results and compare them with several related works.

---


### 216. [Horizon-Scalable Q-Learning](https://arxiv.org/abs/2611.10987)

**<font color=#1a73e8>作者：</font>** Haoran Xu, Pragya Srivastava, Xinjie Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning accurate off-policy state-action value functions (Q-functions) from offline datasets becomes harder as the task horizon grows. One-step temporal-difference (TD) learning bootstraps after every transition, so small per-step errors accumulate along the horizon, and early states can be badly misvalued even when the TD loss is small. Multi-step TD shortens this chain by following the dataset trajectory for several steps; however, since the behavior policy is often suboptimal, every followed action adds a bias, and no fixed number of steps suits a whole trajectory. In this paper, we propose Horizon-Scalable Q-Learning (HQL), a simple method that enables accurate long-horizon value learning by automatically balancing between one-step and multi-step returns. HQL extends a target through a dataset action only when the critic values it at least as highly as the best-of-N actions sampled from the BC policy, and otherwise falls back to a one-step target. We show that this rule is a principled off-policy correction that needs no action densities, which makes HQL compatible with expressive flow and diffusion policies. Experiments show that HQL avoids the failures of both one-step and multi-step TD on a combination-lock task across horizons, and outperforms prior horizon-reduction methods on long-horizon OGBench and OCBench tasks.

---


### 217. [Sensitivity-Gated Accumulator Caching for On-Device Learning of Low-Bit Hand Networks](https://arxiv.org/abs/2611.10991)

**<font color=#1a73e8>作者：</font>** Soroor Ghandali, Kanika Mamgain, Manjot Kaur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small hand-tracking networks are deployed as 4- and 8-bit codes, and they should keep adapting to a user's camera after deployment, on the device and within roughly the memory of the model itself. Quantization-aware training cannot do this cheaply, because it keeps a 32-bit master copy of every weight together with its optimizer state, about 96 bits per weight. Training the codes directly with stochastic rounding needs no copy but injects rounding noise at every step, and the methods that remove this noise keep a residual buffer for every weight. We introduce sensitivity-gated accumulator caching (SGAC), which keeps residual state for only a small and changing set of weight groups. A set-associative cache of 8-bit accumulators collects the sub-step updates of the groups with the largest Fisher-weighted squared code step and writes them into the codes as whole steps; an evicted line is flushed by stochastic rounding, and a group without a line does not move until it is admitted. We prove that the write-back is unbiased and show, under a local quadratic model, that rounding a sub-step update costs loss of the same order as the update's own gain, so that rounding pays only where the expected gradient is large relative to the curvature. On a 383k-parameter hand-keypoint network, SGAC trains with 8.1 bits of state per weight. Scored on the 4/8-bit network that the device runs after adaptation, it has the highest mean accuracy of nine deployed low-bit networks on two simulated cameras. On twelve ImageNet-C corruptions it has the highest average of corrupted and clean accuracy of seven deployed methods, ahead of the PEQA-style, ECO-style and direct low-bit baselines with confidence intervals that exclude zero, and it matches an 8-bit accumulator kept for every weight with 56% of that state.

---


### 218. [DPDP: Diffusion Policy-Steered Diffusion Planner for Offline Reinforcement Learning](https://arxiv.org/abs/2611.10993)

**<font color=#1a73e8>作者：</font>** Ruyi An, Mingyuan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In offline reinforcement learning, diffusion models fill two roles with complementary strengths. Typically guided by a critic, a diffusion policy is value-aware and favors high-return, behavior-supported actions, but it is short-sighted: it never lays out the states it intends to visit. A diffusion planner is far-sighted, synthesizing such a long-horizon trajectory, but it is only behavior-driven at execution, realizing each planned transition using only offline this http URL is strong exactly where the other is weak. We introduce DPDP to bring them together at the planner's execution step, where a planned transition becomes an action. Reading the planner's inverse-dynamics executor as a posterior over actions: the environment's transition likelihood relates an action to the planned next state, while the behavioral prior determines its weight under the offline data. Replacing this prior with a value-optimized diffusion policy preserves the planned transition likelihood and favors valuable actions that can serve the plan. We target the resulting clean-action distribution in two ways. A training-free sampler composes policy and inverse-dynamics scores at matched action noise levels and applies Langevin correction; this route uses a shared action noise schedule and an approximately common terminal prior. A preference objective instead amortizes the transfer into a single diffusion executor. Across D4RL, DPDP improves the planner it builds on, staying competitive with reactive diffusion policies on locomotion and leading on long-horizon navigation.

---


### 219. [Toward a theory of Evaluability](https://arxiv.org/abs/2611.10996)

**<font color=#1a73e8>作者：</font>** Kunal Talwar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models, particularly large foundation models, are increasingly evaluated along multiple axes that are relevant for their usage. In addition to accuracy measures appropriate for the specific task of interest, measures capturing safety, calibration and fairness properties are often of interest. The classical approach to these problems assumes that the test set has been held out from the training process, an assumption that is increasingly harder to justify for large foundation models. In this work, we formalize a notion of evaluability without this assumption, and ask if it is feasible to evaluate black-box models in settings where our test samples may have been used during training.
We study this problem under different settings, capturing different levels of access to the model. We first study the natural setting, where the evaluator only looks at the output of the model on the test set. We fully characterize the class of distributions where accurate evaluation is possible, and show tight upper and lower bounds on the sample complexity of evaluation. Our results show that black-box evaluation in this setup is feasible if and only if the distribution is close to being small support. We then consider evaluation algorithms that can query the model on additional inputs and demonstrate connections to self-correctors studied in program testing. Using these, we show that a small amount of query access can increase the power of the evaluator for natural distributions and concept classes.

---


### 220. [Open Problems in Chatbots and Mental Health](https://arxiv.org/abs/2611.10997)

**<font color=#1a73e8>作者：</font>** Jared Moore, Jacy Reese Anthis, William Agnew 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General-purpose chatbots are increasingly used for emotional and mental health support. They can be useful, but issues such as sycophancy, reinforcement of delusional beliefs, and poor crisis response create risks that are difficult for researchers to study and evaluate. In this paper, we review the most critical open problems for researchers and policymakers in the use of general-purpose chatbots and their effects on mental health. First, there are tractable problems in the controlled evaluation of chatbots: establishing the construct and ecological validity of evaluations, evaluating multi-turn interactions, and connecting evaluations to improvements in chatbot behavior. For example, conventional benchmarks that primarily rely on static datasets cannot establish chatbot safety, and novel simulation methods need validation. Second, researchers must connect their studies of chatbots and mental health to real-world evidence. This includes analyzing the chatbot products that AI companies and mental health practitioners have deployed, including their user interfaces and human review and escalation practices for user welfare concerns. However, clinical analysis opportunities afforded by real chat log data sharing are complicated by significant privacy concerns. Finally, we argue that researchers should take an active role in the construction and refinement of evidence-based policy through corporate and governmental decisions such as user protections, standards of care, protected access to user chat logs, data sharing between institutions, incident reporting, and post-deployment monitoring. Such behavioral evaluations, studies of real-world outcomes, and data governance depend on each other and must be addressed in tandem. We believe a coordinated research effort would have substantial real-world impact.

---


### 221. [Differentiable Agent-Based Modeling for Multi-Echelon Supply Chains: Gradient-Based Optimization of Heterogeneous Policies at Scale](https://arxiv.org/abs/2611.10999)

**<font color=#1a73e8>作者：</font>** Bulent Soykan, Murtadha Alsayegh, Sean Mondesire 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global supply chains rely on the interactions of thousands of heterogeneous agents, posing significant challenges for optimization. While traditional optimization often assumes homogeneity to ensure tractability, Reinforcement Learning struggles with sample inefficiency when scaling to high-dimensional state spaces. We propose a Differentiable Agent-Based Model for multi-echelon inventory management. By implementing stochastic dynamics via differentiable tensor operations, we enable direct gradient propagation through the simulation. We validate the framework by recovering theoretical Newsvendor optima without supervision. Crucially, we demonstrate ``Mass Personalization'' by optimizing 10,000 distinct agent policies simultaneously in seconds, achieving a 53% cost reduction compared to scalar baselines. Furthermore, we utilize gradient sensitivity analysis to generate causal heatmaps, accurately recovering inherent lead-time delays from the computation graph. This approach bridges the gap between simulation and optimization, enabling the efficient training of self-correcting Digital Twins.

---


### 222. [Elastic Representations via Hyperbolic Geometry](https://arxiv.org/abs/2611.11001)

**<font color=#1a73e8>作者：</font>** Arjun Ramesh Kaushik, Rudrasis Chakraborty, Nalini Ratha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned representations (or embeddings) are the foundation of modern machine learning systems, yet they are typically trained as fixed-size embeddings, without accounting for varying downstream resource or task constraints. Matryoshka Representation Learning (MRL) addresses this limitation by learning nested representations, but requires costly end-to-end retraining and does not support post hoc expansion, while Contrastive Sparse Representations (CSR) reduce training overhead via lightweight adaptors but operate at a 4x larger dimensionality. Additionally, all prior works restrict their framework towards compression only. In this work, we introduce Hyperbolic Elastic Representation Learning (HERL), a framework for learning dimension-adaptive embeddings (compression and expansion) through a lightweight adaptor without retraining the base encoder. Our key idea is to exploit the exponential capacity of hyperbolic geometry by learning a non-linear mapping from the encoder space to hyperbolic space. We train a simple MLP to downsample the representations before projecting them onto a Lorentzian and learn adaptive representations that respect the Lorentzian geometry. Our approach is model-agnostic and effective in both supervised and unsupervised settings. Through extensive experiments across image and text modalities, we show that HERL preserves downstream performance across a wide range of embedding sizes, exhibits smooth interpolation between dimensions, and achieves these benefits at a fraction of the computational cost. Code: this https URL.

---


### 223. [Efficient 3D plant segmentation through multiscale graph learning and optimized geometric processing](https://arxiv.org/abs/2611.11007)

**<font color=#1a73e8>作者：</font>** Jesus Ivan Ruiz-Martinez, Andres Mendez-Vazquez, Eduardo Rodriguez-Tello  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Plant organ segmentation on compact computing platforms requires accurate predictions and affordable geometric preparation. We develop and evaluate a multiscale edge based graph attention model that combines local shape descriptors, two neighborhood scales and a residual stem and leaf correction in approximately 78 thousand parameters. The engineering application is plant point cloud segmentation for precision agriculture, assessed through grouped accuracy experiments and physical Raspberry Pi 5 inference. Broad comparisons with hierarchical, graph and transformer baselines establish PointNeXt as the strongest external accuracy reference among the tested local recipes. A nested four variant ablation on a local maize collection separates geometric information from the combined multiscale configuration across seven outer groups and three seeds. The complete model achieves the highest mean intersection over union, 86.36%, although uncertainty and boundary errors qualify the contribution of each component. We then optimize full cloud principal component analysis, sampling and neighbor queries without changing learned weights or descriptor definitions. All 1,180 paired desktop comparisons on PlantNet and TomatoWUR preserve exact logits and predictions. Multiscale pipeline latency falls from 330.33 to 96.82 milliseconds on PlantNet and from 1,054.52 to 463.10 milliseconds on TomatoWUR. PointNeXt also benefits from optimized sampling and remains faster over the complete pipeline. These results support compact graph learning with reduced geometric overhead, while physical board measurements establish inference feasibility rather than energy efficiency or readiness for autonomous flight.

---


### 224. [Learning Actionable Information Landscapes for Multimodal Active Sensing in Hawkmoths](https://arxiv.org/abs/2611.11011)

**<font color=#1a73e8>作者：</font>** Abdelrahman Sharafeldin, Yaqing Wang, Simon Sponberg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Animals integrate information across sensory modalities to guide exploration, suggesting that they maintain internal estimates of where actions are expected to reduce uncertainty. However, how such action-conditioned information maps are learned from multimodal sensory experience remains unclear, as previous studies have been largely confined to unimodal sensing frameworks. We introduce a multimodal predictive-coding framework for learning uncertainty-reduction maps from visual and mechanosensory observations in hawkmoth flower interaction tasks. A variational generative model trained on simulated environments recovers modality-specific information landscapes over the action space, capturing how visual patterns, surface geometry, and mechanosensory cues shape the value of exploratory actions. These learned maps are consistent with several features of hawkmoth behavior, including nonzero tracking offsets, probing along visual patterns, and geometry-dependent exploration. Applying the model to behavioral data from flower tracking and nectary search, we find that natural trajectories tend to occupy regions of high uncertainty reduction in these learned maps. Building on these observations, we develop an uncertainty-gated lexicographic algorithm that switches between information gathering and reward exploitation based on perceptual uncertainty. In nectary search, uncertainty gating improves learning relative to exploit-only, $\epsilon$-greedy, fixed-time, and uncertainty-calibrated non-lexicographic controls, with better generalization and robustness to sensory and curvature shifts. These results link information landscapes learned through generative modeling to biological sensing and embodied exploration.

---


### 225. [ProtLink: Sequence and Multispecies Graph Context for Protein Interaction Prediction](https://arxiv.org/abs/2611.11017)

**<font color=#1a73e8>作者：</font>** Xingyuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting protein-protein interactions (PPIs) from sequence alone is difficult, while known interaction networks may provide informative biological context. We introduce ProtLink, a sequence-conditioned graph-learning framework that combines frozen ESM-2 representations with protein interaction topology and orthogroup-mediated connections between species. We compare sequence-only models, GraphSAGE, a homogeneous graph transformer, and a heterogeneous graph transformer (HGT) for human PPI prediction. In an initial edge-level comparison, three-layer multispecies HGT with ESM-2 650M features achieves an average precision (AP) of 0.980 under random negative sampling, compared with 0.951 for the homogeneous transformer; its AP decreases to 0.878 with two-hop-preferred negatives. In controlled three-seed experiments, three-layer full-graph HGT obtains an AP of $0.9701\pm0.0022$, exceeding an orthogroup-only model ($0.9435\pm0.0094$). The corresponding two-layer comparison shows little additional benefit from non-human PPI edges, consistent with the greater message-passing depth needed to transmit their information. For human proteins excluded from training interactions, multispecies HGT achieves $0.8335\pm0.0094$ AP versus $0.6482\pm0.0052$ for a sequence-only pair model. These results identify the value, depth dependence, and limits of evolutionary graph context while distinguishing prediction of held-out edges from generalization to held-out proteins.

---


### 226. [Unified Factored Representations Resist Catastrophic Forgetting](https://arxiv.org/abs/2611.11020)

**<font color=#1a73e8>作者：</font>** Joel Lehman, Kenneth O. Stanley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper explores an unexpected connection between the quality of a neural network's (NN's) internal representation and its vulnerability to catastrophic forgetting. The representational forgetting hypothesis is that networks with unified, factored representation (UFR) can resist catastrophic forgetting without any modification to the underlying fine-tuning algorithm or network architecture. The key insight is that catastrophic forgetting may largely result from fractured entangled representation (FER): fine-tuning on only part of the input domain results in disruptive changes for other input patterns, because of how individual features are globally entangled. In contrast, if a gradient update is compatible with how a UFR network factors its representation, such an update may result in coordinated change across the input domain, alleviating catastrophic forgetting. Experiments in two domains provide evidence for this hypothesis: (1) an illustrative 1D regression task, in which UFR networks constructed by hand are compared against networks trained from scratch with SGD, and (2) an image-regression task with NNs previously shown to exhibit UFR. In both settings, UFR networks forget substantially less than their FER counterparts when repeatedly fine-tuned on UFR-compatible variations. Further experiments show that a training loss that distills UFR representations into fresh NNs reduces forgetting; along with several additional controls, these results help isolate representation as the critical factor. Together these results suggest that representational quality is an underappreciated contributor to catastrophic forgetting, and that the encouragement and maintenance of such quality may require attending to what patterns a particular NN is ready to learn.

---


### 227. [Hybrid Product Search Without the Copy: Lexical, Semantic and Filtered Retrieval Served Directly from a Data Lake](https://arxiv.org/abs/2611.11031)

**<font color=#1a73e8>作者：</font>** Raghvendra Yadav, Xiang Fu, Chinmay Soman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> E-commerce catalogs increasingly live in lakehouse tables: Apache Iceberg metadata over Parquet files in object storage. Product search, however, still runs on copies of that catalog, in a lexical engine and a vector database, each with its own ingestion pipeline, schema, staleness window and bill. We show that search applications can be hosted directly on the data lake, with the lakehouse table as the single system of record. We extend Apache Pinot, a real-time OLAP engine that already serves Iceberg tables in place, with BM25 relevance scoring over its Lucene text index, corpus-wide term statistics so that scores are comparable across files, and reciprocal rank fusion in plain SQL; a real-time table fed by a stream can sit behind the same table, merged by the broker. On the Amazon ESCI benchmark (1.2M US products, 22,458 test queries), hybrid search served from the lake matches exact retrieval (nDCG@10 .361). The lake table is queryable 149 s after its files are registered, and a lake commit is searchable in 3.8 s, close to indexing directly into a search engine. On a brand-sorted lake of 277M products (0.8 TB), one 16-vCPU node answers brand-scoped vector, BM25 and client-fused hybrid searches in 6.5-9 ms (p50), sustains 1,100 vector and 635 BM25 searches per second at under 180 ms p99, and makes a commit searchable in 4.3 s. Search adds only its indexes: no copy of the catalog, no sync pipeline and no second schema, which cuts storage, rebuild time and the operational work of keeping copies consistent.

---


### 228. [Finite-Sample and Communication-Efficient Networked Information Aggregation](https://arxiv.org/abs/2611.11032)

**<font color=#1a73e8>作者：</font>** Mohammadhossein Bateni, Zahra Hadizadeh, MohammadTaghi Hajiaghayi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building on SODA 2026 work Kearns et al. (2026), we study learning in directed acyclic graphs in which each agent observes only a subset of the input coordinates and may use the predictions of its parents as additional features. In the finite-sample protocol, the message sent along each edge is the agent's prediction vector on a shared sample, so the communication cost is linear in the sample size $m$. In this paper we study this model under communication constraints.
First, we revisit the finite-sample analysis of the full-message protocol. We identify a gap in the finite-sample proof of Kearns et al. (2026) and develop a different argument that establishes a finite-sample population-risk guarantee along paths satisfying deterministic $M$-coverage.
Second, we introduce a shared-sketch protocol in which each agent sends a $k$-dimensional linear sketch of its prediction vector instead of the full $m$-dimensional message, where $k\ll m$. We analyze this protocol through a reduction to least squares on the compressed sample together with an oblivious subspace embedding argument. The resulting bound separates statistics from communication: the statistical term is still governed by the original sample size $m$, while the additional error due to compression is controlled by the sketch dimension $k$. For Gaussian sketches, we obtain an explicit high-probability population-risk bound, showing that row subsampling is not the only possible communication-statistics tradeoff for networked information aggregation.

---


### 229. [Virtual Task Prompting for Multi-Task Scene Understanding](https://arxiv.org/abs/2611.11041)

**<font color=#1a73e8>作者：</font>** Zedong Wang, Yucheng Wang, Dan Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-task scene understanding models typically rely on modified vision encoders or complex decoders for cross-task interaction, which limits their flexibility and compatibility with off-the-shelf vision foundation models (VFMs). We introduce Virtual Task Prompting (VTP), which frames multi-task prompting as retrieving task-adaptive compositions from a shared virtual state, where both the state and routing process are optimized in an end-to-end manner. Concretely, VTP maintains an expanded set of virtual tasks alongside the backbone. At each layer, learnable routing matrices read task-specific compositions as input to interact with image tokens and write the processed results back, forming explicit pathways that capture the intricacies among tasks outside the encoder. Since VTP keeps the backbone clean, it integrates seamlessly with pretrained VFMs, advancing the state of the art on Pascal-Context and NYUD-v2. Stress test on Taskonomy with 13 heterogeneous tasks further shows VTP's robustness in extreme settings. Ablations and analysis indicate that VTP's gains stem from adaptive routing rather than increased capacity. The project page is available at this https URL.

---


### 230. [But It Was True When I Checked: Compiling SHOP-Style Method Preconditions into Partially-Ordered HTN Planning](https://arxiv.org/abs/2611.11055)

**<font color=#1a73e8>作者：</font>** Harrison Oates  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Method preconditions specify when a method may be applied in hierarchical task network (HTN) planning, but their meaning differs under two established semantics. The SHOP planners, like the classical HTN formalism of Erol, Hendler and Nau, require the precondition to hold immediately before the method's first action. HDDL, the input language of the International Planning Competition's HTN track, instead introduces an auxiliary action to check it; under partial order, unrelated actions may invalidate the precondition before the method starts. HDDL's designers adopted this weaker semantics because the first-action reading could not easily be compiled. Subsequent work has repeatedly identified its compilation under partial order as an open question, with existing transformations limited to total order. We give a compilation of the first-action semantics into standard partially ordered HTN planning without method preconditions using only two additional facts, thereby resolving a longstanding question in the HTN planning community.

---


### 231. [Differentiable Virtual-Slot Partitioning for Adaptive Tokenization in Vision Transformers](https://arxiv.org/abs/2611.11058)

**<font color=#1a73e8>作者：</font>** Gaoxiang He, Bin Zhu, Bo Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adaptive tokenization aims to reduce the compute spent on uninformative image regions while preserving accuracy. Existing work relies on (i) fixed or frozen scoring rules, which cannot be trained toward the task loss, or (ii) discrete masks trained with straight-through estimators, which yield noisy gradients, while fully differentiable alternatives instead leave the pre-trained regular grid. We revisit adaptive tokenization from a regular-grid perspective and ask: can a two-scale quadtree be learned end-to-end without deleting a single token during training? We show that one coarse token and its four fine children can be made the two endpoints of a single continuous interpolation. We introduce Differentiable Virtual-Slot Partitioning (\dvsp{}), which keeps four \emph{virtual slots} per $2{\times}2$ region and blends their token features and attention mass with a single weight $\alpha$, exactly reproducing the discrete grid at $\alpha \in \{0,1\}$. On COCO detection with EVA-02-B, \dvsp{} retains $97.9\%$ of dense Box AP while removing $64.2\%$ of visual tokens, giving a $1.61\times$ end-to-end speedup, and it outperforms entropy-based APT, DART, and uniform lower-resolution dense adaptation at matched budgets; these gains depend on the conserved attention mass, whose removal costs $1.59$ Box AP. On a frozen Segmenter it also improves Cityscapes mIoU, and on frozen DeiT backbones it exceeds entropy selection at identical per-image token counts.

---


### 232. [What Does Multiple Choice Actually Measure? Disentangling Video Understanding from Option Exploitation](https://arxiv.org/abs/2611.11062)

**<font color=#1a73e8>作者：</font>** Elliott Piercy, Justin Chan, Sepand Dyanatkar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding evaluations are intended to measure a model's proficiency in video perception and task solving. However, current VideoQA benchmarks struggle to isolate these capabilities due to their reliance on multiple-choice (MC) answer guidance, language priors, and fragile scoring pipelines. Disentangling these confounding factors reveals how much of a model's score is supplied by the evaluation context rather than earned through faithful perception. Across six VideoQA benchmarks of varying length, we find that accuracy is significantly above chance without any visual input. This is caused by shortcutting and option-prior reliance. We express these effects in the language of faithfulness: option-exploitation and answer-conditioned reasoning traces are unfaithful even when they are correct. Together, our results show that a VideoQA score is jointly determined by language priors, option timing, and how outputs and labels are converted into correctness. We produce a novel Option-Delayed Replay (ODR) mechanism that discloses options at controlled stages of an open-ended (OE) trajectory, to obtain objective MC scores from faithful option-free inference. Our work demonstrates that agentic methods with ODR and faithful inference can match option-exploiting performance. Finally, we formalize our diagnostic collection and ODR as a reproducible evaluation protocol, and we release a human-relabelled edition of LVBench (correcting $20.5\%$ of keys) to remove annotation noise as a confounding variable.

---


### 233. [Target Recoverability under Selective Labels: A Failure Mode in ECG-Based Acute Coronary Syndrome Prediction](https://arxiv.org/abs/2611.11063)

**<font color=#1a73e8>作者：</font>** Alexander Schubert, Anton Håkansson, Ziad Obermeyer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical machine learning models often learn from diagnoses observed only in patients clinicians chose to test. The biases of such selective labels are well known, but less understood is what happens when a diagnosis includes cases the model's inputs cannot detect. Because testing decisions draw on information the model does not see, these cases can appear predictable among tested patients, producing relationships that fail, and can even reverse, among the untested. We formalize this mechanism and show in simulations that it worsens as testing becomes more selective or undetectable cases more common, while models trained only on detectable cases remain informative. We empirically study electrocardiogram (ECG)-based prediction of acute coronary syndrome (ACS), which is confirmed only by invasive testing and whose subtypes differ in how clearly they appear on the ECG. Three ECG foundation models fine-tuned on revascularization, our ACS proxy, performed well among catheterized patients (AUROC 0.740-0.770) but worse than chance for 30-day major adverse cardiovascular events among untested patients (AUROC 0.381-0.478). Models trained on ECG-visible subtypes retained discrimination (AUROC 0.680-0.709), whereas a model trained on unstable angina, which can occur without ECG changes, was inversely related to risk (AUROC 0.310). Under selective labels, effective learning therefore requires prediction targets that can be inferred from the model's inputs and evaluation in the intended deployment population, which often extends beyond the patients who were tested.

---


### 234. [Discrete Diffusion Playground: A 2D Benchmark for Discrete Generative Models](https://arxiv.org/abs/2611.11068)

**<font color=#1a73e8>作者：</font>** Justin Shao, Sihyun Park, David Ryan Koes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion is a promising framework for categorical generative modeling, but current evaluation protocols often fail to reveal whether models have actually learned the target distribution. We introduce the Discrete Diffusion Playground, a diagnostic benchmark that converts known 2D continuous distributions into binary token sequences through an exact discretized bijection. This creates a rare setting in which models are trained on discrete sequences, but generated samples can be decoded back into 2D and compared directly against a known ground-truth distribution. The benchmark spans smooth Gaussian mixtures and tilted checkerboards with sharp boundaries, disconnected support, and coordinate-dependent structure, allowing it to expose failures that are invisible in standard proxy metrics. It supports exact grid divergences, Wasserstein distances, density visualizations, and nonparametric two-sample tests, providing both quantitative evaluation and interpretable failure diagnosis. Using this testbed, we show that masked diffusion models can learn meaningful adaptive reveal orders but remain less stable than autoregressive baselines on smooth targets and largely fail on tilted checkerboards, where autoregressive models preserve the target geometry. Control experiments with reversed and interleaved token orderings show that autoregressive performance is not explained by favorable bit order alone. The Playground provides a simple but stringent benchmark for stress-testing discrete generative models and for developing evaluation metrics that detect real distributional mismatch rather than proxy performance. Our code is available at this https URL .

---


### 235. [NanoNet: Ultra-Lightweight Network for MRI Brain Tumor Classification toward Edge AI](https://arxiv.org/abs/2611.11071)

**<font color=#1a73e8>作者：</font>** Tran Nguyen-Le, Huu-Thuan Huynh, Minh-Triet Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated brain tumor classification from magnetic resonance imaging (MRI) can support accessible medical image analysis, but conventional deep learning models often exceed the resource budgets of highly constrained edge-AI platforms. We present NanoNet, an ultra-lightweight convolutional neural network designed for resourceconstrained MRI classification and motivated by future edge-AI applications. Inspired by MobileNetV2, NanoNet substantially reduces network depth, channel capacity, expansion ratios, and final feature dimensionality, resulting in only five inverted residual blocks and 8,132 parameters. We further investigate dependency-aware structured pruning, knowledge distillation, and INT8 quantization-aware training for additional compression. Experiments on the BRISC 2025 benchmark show that NanoNet achieves 92.80% accuracy and 92.97% macro F1 with 8,132 parameters and 10.498 MFLOPs. Across three compression seeds, it exceeds the mean accuracy of 70%-pruned MobileNetV2 by 5.20 percentage points while using 60.2% fewer parameters and 9.8% less computation. Converted INT8 NanoNet achieves 89.70% accuracy and 90.22% macro F1 across three QAT seeds. Earlier TensorFlow Lite measurements indicate 27.7 KB of baseline model storage, motivating future edge-AI deployment.

---


### 236. [ADC-RANet: Improving Resolution Adaptive Neural Networks with Attention, Distillation and Calibration](https://arxiv.org/abs/2611.11076)

**<font color=#1a73e8>作者：</font>** Jeferson Severino de Araujo, Lilian Hollard, Eric Granger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic neural networks are a class of adaptive models in which the computation assigned to each input sample is determined dynamically, potentially reducing computational cost while maintaining similar performance. For image classification, the Resolution Adaptive Network (RANet) is a strong approach that progressively allocates computational resources across input scales based on sample difficulty. In this work, we introduce RANet with Attention, Distillation and Calibration (ADC-RANet), an enhanced version of RANet that improves performance across all computational budgets. Our approach combines three tightly connected components: bottom-up channel attention, top-down cascaded knowledge distillation, and overconfidence correction using MixUp, in a synergistic design that coordinates both pathways. Experiments on CIFAR-100 and ImageNet datasets show consistent gains while preserving the efficiency of RANet. Our code is available: this https URL

---


### 237. [A Hierarchical Tokenization Framework for Voxel-Level fMRI Representation Learning](https://arxiv.org/abs/2611.11081)

**<font color=#1a73e8>作者：</font>** Karanpartap Singh, Yue Zhao, Mohammad H. Abbasi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce HBAR (Hierarchical Brain Activity Representation), a hierarchical tokenization framework for learning compact, multi-scale representations of neuroimaging data. HBAR organizes voxel-level resting-state fMRI into a hierarchy spanning sub-parcel voxel groups, parcels, and large-scale functional networks, enabling up to 415x compression while preserving fine-grained spatial information beyond conventional parcellation. The framework supports fixed atlas-based, fully learned, and softly prior-guided hierarchies, allowing us to systematically study the role of structured priors in brain representation learning. On HCP-YA, at approximately 415x compression, HBAR achieves higher parcel and network correlations than rate-matched flat tokenizers, while at a lower 52x compression rate, shuffling the anatomical grouping reduces parcel correlation from 0.920 to 0.886. Demographic readouts with autoregressive training also reveal potential gains from the hierarchical structure. By combining sub-parcel inputs, compact discrete tokens, and multiscale brain structure, HBAR offers a practical framework for representation learning in high-dimensional neuroimaging data.

---


### 238. [Uncertainty-Guided Reward Labeling for Reinforcement Learning under Limited Feedback](https://arxiv.org/abs/2611.11091)

**<font color=#1a73e8>作者：</font>** Renhao Zhang, Shreyas Chaudhari, Bruno Castro da Silva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In reinforcement learning from limited feedback (RLLF), only a small fraction of an offline dataset can be labeled with rewards, and the central question is which samples should be labeled to learn a high-performing policy from the resulting partially labeled dataset. Prior work formalized this as a reward-selection problem by focusing on the selection stage while treating downstream policy learning as a black box, in a regime where queried rewards are not retained for reward-model training. We instead study the retained-label setting, where queried rewards can be stored and used to fit a reward model before policy learning. We bound the suboptimality of the learned policy in terms of two sources of error: one arising from offline RL on a fixed, offline dataset, and the other from uncertainty in the reward model. Since reward selection cannot change the offline dataset, the limited labeling budget must be used to strategically reduce reward uncertainty. Motivated by RLLF's observation that useful rewards tend to keep the agent on high-return trajectories, we introduce Successor-Guided Uncertainty REduction (SURE), a novel method that uses successor features to select rewards that are both uncertain and associated with states from which high-valued states are reachable. We formally derive SURE from a bound-induced design objective and characterize its exact one-step marginal gain. Empirically, SURE reaches near full-feedback performance with few reward labels across a variety of domains and offline-RL backbones, yielding an effective method for feedback-efficient reinforcement learning.

---


### 239. [Does Pose Encoding Matter? Analyzing Geometric Representations for Discrete Motion Vocabulary Learning](https://arxiv.org/abs/2611.11093)

**<font color=#1a73e8>作者：</font>** Amir Kimiyaie, Nahal Mafi, Hamed Tabkhi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compressing continuous human motion into a finite vocabulary of discrete tokens is now the first stage of many motion understanding and generation pipelines. Vector quantization partitions a latent space into Voronoi cells around a finite codebook, but the geometry of that latent space is inherited from the input pose encoding, and it is unclear which encoding admits an efficient discretization. We study four encodings that place skeletal motion in different geometric spaces: Gaussian joint heatmaps on the pixel lattice, which we show to be a morphological dilation of the joint point set by a quadratic structuring function; root-relative joint positions in Euclidean space; local joint rotations on $\SO$ through a continuous 6D embedding; and a redundant full kinematic encoding. For each, we train VQ-VAE tokenizers whose codebooks lie on the unit hypersphere, varying codebook size, temporal stride, and code dimension. Beyond reconstruction, we measure codebook utilization and the effective vocabulary size, i.e., the number of equiprobable spherical Voronoi cells with the same entropy as the observed token distribution. Rotation and position encodings keep converting additional codewords into effective vocabulary, whereas the full kinematic encoding saturates at a few hundred effective cells and heatmaps at fewer than sixty. The smallest code dimension gives the highest utilization for three of the four encodings, and the effect of temporal stride depends on the encoding. Encodings of the same pose family can thus yield effective vocabularies differing by an order of magnitude, a difference that reconstruction loss alone does not reveal, which points to input geometry as a first-order design choice in motion tokenization.

---


### 240. [Jointly Optimizing Memory, Computing and Offloading for Energy-Efficient DNN Inference](https://arxiv.org/abs/2611.11106)

**<font color=#1a73e8>作者：</font>** Yunchu Han, Zhaojun Nan, Sheng Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In edge intelligence systems, computation offloading and dynamic voltage and frequency scaling (DVFS) are widely used to improve energy efficiency. However, as applications like deep neural network (DNN) inference evolve in complexity, their demands for memory resources have progressively increased, establishing memory as a critical bottleneck that impacts both latency and energy consumption. In this paper, we propose a joint optimization scheme integrating memory, computing and offloading for energy-efficient DNN inference. We formulate the energy minimization problem under deadline constraints as a mixed-integer nonlinear programming (MINLP) problem, where the main challenge arises from the coupling between offloading and resource optimization. To address this issue, we decompose the original problem into two subproblems under a fixed offloading policy. The local subproblem is transformed into an equivalent geometric programming (GP) problem to derive the optimal memory frequency and computing frequency, while the edge subproblem is solved via convex optimization. An efficient coordinate descent (CD) algorithm is further developed to jointly optimize all variables. Simulation results demonstrate that our proposed algorithm achieves near-optimal performance with the gap from the optimal policy being at most 9.3%, and reduces the energy consumption of devices by up to 16.1% compared with benchmarks without memory frequency optimization.

---


### 241. [MySign: A High-Fidelity Motion-Capture Dataset for 3D Sign Generation in Bahasa Isyarat Malaysia](https://arxiv.org/abs/2611.11115)

**<font color=#1a73e8>作者：</font>** Jiayu Shen, Kalin Stefanov, Lay-Ki Soon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Progress in 3D sign generation is constrained by the scarcity of high-fidelity 3D sign language datasets, a limitation that is particularly severe for under-resourced languages. We introduce MySign, the first motion-capture dataset for isolated signs in Bahasa Isyarat Malaysia (BIM). Its 5,000 samples cover 1,000 lexical items (glosses) and were produced by five Deaf native signers. Prior datasets that rely on SMPL-X parameters regressed from video provide pseudo-labels, which are often affected by depth ambiguity, inaccurate finger poses, and temporal jitter. MySign instead provides ground-truth SMPL-X sequences retargeted from recordings made with a motion-capture setup tailored for sign language; these sequences offer higher-fidelity motion, particularly in fine-grained hand and finger articulation. A controlled comparison on the same glosses and signers indicates that training on these sequences improves generation over training on such pseudo-labels. We establish MySign as a challenging benchmark for gloss-conditioned 3D sign generation: state-of-the-art models produce visually plausible outputs but fall short of the ground truth, most notably in fine-grained articulation, revealing persistent gaps in modeling articulated sign motion. In contrast, recognition baselines consistently achieve high lexical accuracy, indicating that the dataset reliably supports supervised learning. The dataset is available at this https URL

---


### 242. [When gene summaries reveal the answers: Gene Ontology circularity in gene embedding benchmarks](https://arxiv.org/abs/2611.11118)

**<font color=#1a73e8>作者：</font>** Jiawei Wu, Huishu Wang, Junlin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A gene summary can contain the very annotations used to evaluate an embedding of its text. The Alliance of Genome Resources converts Gene Ontology (GO) annotations into sentences, which NCBI Gene displays and GenePT includes in its input. These summaries covered 6,172 of 19,256 human protein-coding genes (32.1%), including 58% of genes with one to ten linked publications. We embedded the same corpus with and without the generated summaries and refitted a function-prediction probe on each version. Among genes with one to ten publications, removal reduced the reported per-gene area under the receiver operating characteristic curve (AUROC) by 0.078 with a linear probe (95% bootstrap interval 0.072-0.084) and by 0.033 with a multilayer perceptron. These estimates use a historical GO scorer that mishandled ties. The original predictions are unavailable for rescoring. A simple TF-IDF encoder also benefited from the summaries, as did models evaluated only on experimental annotations. Replacing generated summaries with UniProt function descriptions recovered much of the lost performance despite little verbatim overlap. UniProt also curates many of the evaluation labels. In mouse and yeast, we found a similar dependence on the source of the description. We introduce GeneProv to compare encoders on matched text and to examine how representation rankings change across GO recovery, non-GO endpoints and co-essentiality.

---


### 243. [What You Show Is Not What You Get: Rethinking Demonstration Following in Visual In-Context Segmentation](https://arxiv.org/abs/2611.11122)

**<font color=#1a73e8>作者：</font>** Xiao Hu, Ilia Sucholutsky  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual in-context segmentation uses visual demonstrations to guide predictions for a new image. In SegGPT, we identify background color mapping deviation, where non-target regions sharing a background label receive different output colors, and part-to-parent expansion, where predictions extend beyond the requested part into its parent object. These deviations can occur even when the relevant regions remain distinguishable in internal features. Controlled changes to demonstration colors and requested targets support an account in which demonstrations guide role and color assignments over familiar semantic regions, influenced by learned semantic and color preferences. Building on these findings, we introduce Semantic Contrast Prompt Selection (SCPS). Its semantic contrast encoding assigns separate colors to the requested part and the rest of its object while keeping the remaining scene black. SCPS combines existing retrieval scores with quality estimates from labeled development images to select demonstrations and their binary or semantic contrast encodings. Averaged across seven retrieval methods on three benchmarks, SCPS improves target IoU by 0.054 and reduces leakage into the rest of the object by 22.7% relative to the original binary selectors. Our findings offer a new perspective on understanding and improving demonstration following in visual in-context segmentation.

---


### 244. [CrossLiDAR: Controllable Multi-Sensor LiDAR Sequence Generation](https://arxiv.org/abs/2611.11131)

**<font color=#1a73e8>作者：</font>** Khanh Nguyen, Thomas Walker, Hichem Telli 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity LiDAR simulation remains a bottleneck for scalable development and validation of autonomous systems. Existing generators can synthesize realistic scans, but they are typically constrained to a single sensor configuration, offer limited control over structure and geometry, and drift in long-horizon 4D generation. We present CrossLiDAR, a unified transformer-based framework capable of generating controllable and spatio-temporally consistent multi-sensor LiDAR sequences. Our approach leverages a rectified flow objective with a Multi-Modal Diffusion Transformer (MM-DiT) backbone, within a compact latent space of range images. To support multiple LiDAR sensors, an Inter-sensor Module enables interaction across sensors, while a ControlNet-style branch provides structural conditioning (e.g., BEV priors or 3D bounding boxes). For modeling the temporal consistency, CrossLiDAR generates short $N$-frame sequences and extends them autoregressively to improve long-horizon coherence. Our model significantly outperforms state-of-the-art baselines, achieving an average improvement of 29.56\% in JSD and 15.36\% in MMD evaluated on nuScenes and the Waymo Dataset. CrossLiDAR bridges the gap to modern autonomous-driving simulation by enabling calibration-consistent multi-sensor LiDAR rollouts over long horizons for controllable, scenario-based testing.

---


### 245. [Graphene: A Lightweight Transformer with Ising Mean-Field Refinement for Image Super-Resolution](https://arxiv.org/abs/2611.11139)

**<font color=#1a73e8>作者：</font>** Seungki Hong, Taekwang Jang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes Graphene, a lightweight image super-resolution architecture with two complementary feature refinement mechanisms: Ising-model-inspired local feature refinement using an Ising Refinement Block (IRB) and stage-history-based feature refinement using a History Attention (HistAttn) module. The IRB reuses attention output features and pre-softmax attention logits to construct signed pairwise token couplings within each local window, applies unrolled mean-field updates, and refines features through a gated residual correction. These signed couplings allow alignment and opposition between latent spins to modulate local feature refinement. HistAttn attends over the current stage output and earlier representations at the same token position and adaptively blends the current stage output with a history-weighted feature aggregate without adding spatial pairwise attention. On Urban100 at $\times4$, Graphene and Graphene-light improve over IET and IET-light by 0.24 dB and 0.38 dB, respectively, with 34.3%/13.7% fewer parameters, 44.8%/44.4% fewer FLOPs, 78.4%/71.5% lower latency, and 76.0%/85.5% lower peak memory. Real-world SR comparisons further show that Graphene recovers fine details and preserves textures across diverse degradations. Code and reference checkpoints are available at this https URL

---


### 246. [SurgWorld: Learning Surgical Representations Beyond Observation via Latent Prediction](https://arxiv.org/abs/2611.11140)

**<font color=#1a73e8>作者：</font>** Jingkun Yue, Pengxiang Wang, Siqi Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical procedures are inherently partially observable, requiring surgeons to continuously infer evolving anatomical dynamics and future surgical states beyond the current observation. However, existing self-supervised learning methods primarily learn from observed surgical videos through masked reconstruction or predicting representations within the camera's current field of view, lacking the capability to explicitly model the out-of-sight surgical dynamics. Inspired by latent predictive world models, we introduce SurgWorld, a video-native, self-supervised framework for surgical representation learning, which treats a specified spatial or temporal shift as a pseudo-action and learns to predict the target latent representation from a partial observation. Specifically, we propose Out-of-Sight Dynamics Modeling (OSDM) as the pretraining objective for predicting representations conditioned on relative spatio-temporal shifts. We further regularize the learned latent dynamics from OSDM with a Geometric Visual Similarity (GVS) objective by aligning patch-level relational structures between predicted and target representations, preserving spatial geometry and local visual coherence for dense perception. These two objectives are integrated through an agglomerative training framework that consolidates complementary supervisory signals from multiple teachers to learn a unified latent representation of surgical dynamics and visual geometry. Extensive transfer learning experiments on 17 surgical benchmarks show that SurgWorld consistently outperforms existing vision foundation models across surgical workflow recognition, fine-grained action understanding, and dense visual perception. We further conduct tailored qualitative and quantitative analyses, demonstrating that SurgWorld effectively captures surgical dynamics beyond the directly observed context through latent prediction.

---


### 247. [Full Fine-Tuning is not the Problem: Why Adam Fails and SGD Succeeds in Few-Shot CLIP Adaptation](https://arxiv.org/abs/2611.11152)

**<font color=#1a73e8>作者：</font>** Nairouz Mrabah, Ismail Ben Ayed, Eric Granger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Few-shot CLIP adaptation is often treated as a parameterization problem. Full fine-tuning is assumed to overfit, so parameter-efficient fine-tuning (PEFT) methods are preferred. In this paper, we show that this conclusion conflates parameterization with optimization. Across 11 datasets, 3 CLIP backbones, and 5 shot levels, dense full fine-tuning with plain SGD outperforms representative PEFT methods under the reported evaluation protocol, whereas Adam/AdamW collapses. We trace this collapse to unreliable support-set preconditioning. The few-shot second moment systematically underestimates the corresponding full-data statistic, already at initialization. Adam's inverse-square-root normalization converts this error into an oversized adaptive update. Matching Adam's first-step update budget to SGD resolves most of the collapse, whereas numerator-side alignment does not explain the failure. Shampoo and SOAP also fail, so richer preconditioning alone does not resolve the problem. Theory formalizes how few-shot estimation error is amplified into unsafe updates. SGD succeeds because it avoids unreliable preconditioners and stays close to pretrained CLIP. Interpolation probes show low-loss connections along tested directions, and curvature probes show favorable directional curvature. These results identify optimizer-induced preconditioning, not dense full fine-tuning itself, as the main source of failure in few-shot CLIP adaptation.

---


### 248. [Map2SLAM: From Streaming Map Prediction to Real-Time SLAM](https://arxiv.org/abs/2611.11169)

**<font color=#1a73e8>作者：</font>** Jian Gao, Lin-Zhuo Chen, Yihang Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 3D foundation models (3DFMs) estimate camera poses and dense geometry online, but they fall short of SLAM: their predictions are fixed once emitted, so loop closures cannot correct accumulated drift. With such models already providing strong geometric capability, a central question for SLAM becomes how to schedule their inference and how to keep its results as revisable state. We present Map2SLAM, which keeps LingBot-Map frozen, trains only a lightweight retrieval head, and builds SLAM on the model's inference interface, turning its predictions into observations of an external persistent SLAM state. The front-end tracks every incoming frame with the model's causal streaming inference and decides which frames are written to the persistent state as keyframes. The back-end asynchronously decides when and which past frames to re-observe, re-running the model's joint inference over them with fresh context; verified loop observations correct the trajectory online, and segment observations refine dense geometry after the sequence. All invocations share a single frame encoder pass per image, whose cached features also drive loop retrieval, so frequent re-invocation incurs no additional encoding cost. Map2SLAM achieves state-of-the-art performance on KITTI, VBR, and Oxford Spires, reducing mean ATE by over 40% compared with the best uncalibrated baselines, while maintaining real-time tracking at over 28 FPS at a resolution of $518\times154$ on an NVIDIA RTX 5090D GPU. Please visit our project page at this https URL.

---


### 249. [ClusLoad: Cluster-Guided Model Sharing for Scalable Distribution Transformer Load Forecasting](https://arxiv.org/abs/2611.11170)

**<font color=#1a73e8>作者：</font>** Fangzhou Lin, Guoshun He, Yi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale device-level load forecasting for distribution transformers is challenged by substantial cross-device heterogeneity and the deployment burden of maintaining device-specific forecasting models. Existing approaches typically rely either on device-specific models, which are difficult to scale to large transformer populations, or on global models, which reduce deployment complexity but may overlook heterogeneous load patterns across devices. To address this trade-off, this study develops a trend-clustered forecasting framework that enables model sharing among transformers with similar temporal behaviors. Representation Learning for Time Series using Time-Embeddings (T-Rep) is employed to learn compact temporal representations of transformer load series, which are subsequently grouped using a Gaussian mixture model (GMM). Representative transformers are sampled within each cluster to train cluster-specific Patch Time Series Transformer (PatchTST) models while retaining device-level predictions. The framework is evaluated using real-world 15-min operational data from nearly one thousand distribution transformers. The proposed framework reduces mean absolute error (MAE) by approximately 20% relative to the direct PatchTST baseline, achieves a high-load warning accuracy of 95.66%, while requiring only seven cluster-specific forecasting models. These results demonstrate that behavior-based device organization provides an effective balance between forecasting accuracy, deployment scalability, and risk-oriented operational support for distribution transformer management.

---


### 250. [When Are Nearby Experts Composable? Cross-Task Model Merging in Neural Thickets](https://arxiv.org/abs/2611.11177)

**<font color=#1a73e8>作者：</font>** Suxin Ji, Hungtao Wan, Mingjun Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Random perturbations around a shared checkpoint can produce experts for distinct tasks, but shared origin does not ensure that their gains survive composition. We formulate expert-pair selection for joint base-relative retention, measured by strict joint success and worst-task gain with unconditional abstention accounting. An exact finite-difference decomposition and an arbitrarily small orthogonal counterexample show why proximity and orthogonality alone are insufficient. We instantiate this formulation with quality-constrained spectral selection, a fixed-budget framework combining cross-task screening, layerwise pair geometry, separate validation, and Base fallback. Across six checkpoints, 21 task pairs, and five independent perturbation pools, the procedure improves strict joint success over Top-1 averaging throughout and leads the four-method model-scale comparison on four of six checkpoints. For the five models with at least 1.5B parameters, matched quality-only, global-cosine, and spectral ranking attain 49.1%, 50.5%, and 53.1% joint success. Under this matched protocol, the spectral selector also yields the highest worst-task gain and Weak Pareto rate and the lowest regression rate. Mean worst-task gain reaches +0.61 percentage points, while 17.1% regression and 13.0% abstention show that composability remains conditional. Project page: this https URL.

---


> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
