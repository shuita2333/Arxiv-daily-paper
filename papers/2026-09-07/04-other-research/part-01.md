# 📦 其他研究 | 2026年09月07日

> 本类共 **194** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-194](./part-04.md)

---

### 1. [Counterexamples as Feedback for Agent Self-Correction](https://arxiv.org/abs/2609.02892)

**<font color=#1a73e8>作者：</font>** Sidhesh Badrinarayan, Adithya Parthasarathy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Single-turn code-generation metrics understate a central property of deployed agents: whether they can repair a wrong artifact after receiving concrete feedback. This paper presents A-CEGIS, a lightweight framework that uses counterexamples as feedback for evaluating multi-turn refinement in natural-language-to-regex synthesis. An agent proposes a regex, a deterministic oracle checks it under full-match semantics, and compact false-positive or false-negative witnesses guide the next turn. On 30 NL-RX-Turk tasks, diagnostic counterexample feedback solves 90\% of tasks within a four-turn ablation budget, compared with 17% for zero-shot generation, 27% for generic self-correction, and 23% for error-only feedback. In a full diagnostic run with hardening, all tasks are solved on the hidden set by the final turn, with mean time-to-success of 2.7 turns and robust success of 77% after targeted probing. These results show that A-CEGIS measures how efficiently an agent improves across turns while adding a practical robustness check beyond the original held-out cases.

---


### 2. [RL-ADA: A World-Feedback Framework for Adversarially Robust Enterprise Dialogue Agents](https://arxiv.org/abs/2609.02902)

**<font color=#1a73e8>作者：</font>** Ram Narayanan, Harshit Rajgarhia, Abhishek Mukherji  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deploying task-oriented dialogue agents in enterprise customer support faces a persistent annotation bottleneck: robust training requires labelled interaction data at scale, yet enterprise conversational logs are privacy-sensitive and expensive to annotate, while user behaviour evolves faster than labelling pipelines can keep pace. We present RL-ADA (Reinforcement Learning with Adversarial Dialogue Agents), a co-evolutionary training framework that eliminates this bottleneck by replacing human labels with \emph{world feedback}: consequence-based reward signals derived directly from measurable interaction outcomes. A Customer Support Agent (DA, 3B parameters) and an Adversarial Customer Agent (CA, 7B parameters) co-evolve in an adversarial arena guided by a fixed automated judge: the DA is rewarded for correctly handling multi-turn customer conversations to successful resolution, while the CA is rewarded for producing realistic, intent-concealing utterances that cause misroutes, creating asymmetric adversarial pressure through opposing but independently structured rewards. An isolation gym iteratively retrains the weaker agent on prior-failure transcripts, requiring no human annotation at any stage. In a banking customer support proof of concept, tool-routing errors are eliminated and the strict end-to-end PASS rate doubles over five co-evolutionary cycles, driven solely by automated arena reward with no labelled data. We additionally observe the emergence of \textbf{Contextual Camouflage}, an adversarial strategy in which the CA learns to embed intent within dense realistic customer detail purely from reward pressure, with direct implications for enterprise red-teaming and robustness evaluation.

---


### 3. [Towards Scaling Reinforcement Learning to Massive Populations: Learning Mean-Field Representations](https://arxiv.org/abs/2609.02928)

**<font color=#1a73e8>作者：</font>** Aditya Makkar, Benjamin Unger, Jeongyeol Kwon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Modern multi-agent systems are increasingly deployed at scale over large populations of agents in settings such as ad-auctions, traffic routing, and recommendation systems. The dominant approach in such settings is to optimize each agent's policy independently, treating the other agents as part of a fixed single-agent environment rather than modeling the population dynamics. In many large-population systems, the dynamics depend on an aggregate summary of the population rather than the identity of any individual. Mean-field RL exploits such structure, providing a principled framework that models each agent's environment as an explicit function of the population distribution. However, in large state-action spaces or high-dimensional control problems, modeling the population distribution is itself intractable. How can we design a scalable framework for high-dimensional control problems with large populations? This work explores this question from the perspective of representation learning. We introduce a mean-field RL framework in which the rewards and transition dynamics depend on the population only through an unknown low-dimensional aggregate statistic. We then study this framework in the offline setting and design a provable approach that learns a near-optimal policy by learning a low-dimensional representation. Motivated by real-life supply-chain optimization problems, we design a one-step routing game to test the hypothesis that learning a low-dimensional population representation improves reward prediction and Nash gap estimation relative to baselines that don't exploit this structure. We show that under a fixed neural-network parameter count and optimization budget, learning a low-dimensional population representation improves reward prediction and the equilibrium quality of the resulting policies.

---


### 4. [A Public-Key-Dependent Adversarial-Deletion Ceiling for Fixed-Alphabet Multi-Bit Pseudorandom Codes](https://arxiv.org/abs/2609.02943)

**<font color=#1a73e8>作者：</font>** Frederick Dehmel, Shilun Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A pseudorandom code (PRC) is a keyed error-correcting code whose codewords are computationally indistinguishable from uniform strings. We study public-key PRCs over fixed alphabets against adversarial deletions, where the deletion channel may both depend on the public encoding key and the transmitted codeword.
Let $\gamma_q^{\mathrm{LCS}}$ denote the asymptotic normalised longest-common-subsequence length of two independent uniform $q$-ary strings. We prove that for every fixed $q\ge2$ no multi-message public-key PRC with a single-output decoder is robust against all such $\delta$-deletion channels for any $\delta>1-\gamma_q^{\mathrm{LCS}}$. For $q=2$, the current rigorous bound $\gamma_2\ge0.792665992$ rules out every constant $\delta>0.207334008$. The proof uses pseudorandomness only to transfer an LCS event from uniform strings to independently sampled codewords and therefore also the resulting collision argument is information-theoretic and requires no secret key. We also extend the argument to list decoding: for every fixed constant $L$, provided the message space contains at least $L+1$ messages, no such PRC with output lists of size at most $L$ is robust for $\delta>1-\gamma_2^{(L+1)}$. Since $\gamma_2^{(m)}=1/2+\Theta(1/\sqrt m)$, these thresholds approach $1/2$. Our bounds are specific to public-key-dependent adversarial channels and do not apply to oblivious edit channels.

---


### 5. [PrivateHub: Contrastive Diffusion Model for Private Sensor-Intensive Environment Data Generation](https://arxiv.org/abs/2609.02958)

**<font color=#1a73e8>作者：</font>** Jiechao Gao, Yuandong Pan, Jie Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sensor-intensive environments enable many intelligent services by inferring user applications from heterogeneous data streams. However, not all applications should be exposed: users want some activities to stay private. This creates a tension between inferring applications for useful services and preventing unwanted inference. Existing approaches such as differential privacy and rule-based filtering protect individual streams but cannot address the privacy risk from cross-sensor inference.
We introduce Privatehub, which uses contrastive learning within a diffusion model to generate synthetic multi-sensor streams that keep non-private applications detectable while concealing private ones. Privatehub has two stages: App-Conditioned Pre-training (ACP), which conditions the model on multi-sensor data with application embeddings, and App-Aware Fine-tuning (AAF), which separates private from non-private data via contrastive learning. We also define a threat model for the multi-sensor sharing setting. Experiments on three real-world multi-sensor datasets show Privatehub lowers private-application accuracy by 40 to 50\% without hurting non-private performance, and stays robust when the attacker retrains on the synthetic data.

---


### 6. [Privacy Leakage in Federated Learning: Gradient-Based Client Identity Inference and Defenses for Inertial Sensing in Vehicular Edge Networks](https://arxiv.org/abs/2609.02971)

**<font color=#1a73e8>作者：</font>** Ali Akarma, Toqeer Ali Syed, Muhammad Khan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As vehicular networks move toward 5G/6G edge intelligence, federated learning (FL) is widely promoted as a privacy-preserving way for vehicles and infrastructure to train shared models without exposing raw sensor data. Yet the updates clients transmit still leak enough information to identify who sent them, which threatens the anonymity that safety-critical V2X applications assume and adds to existing concerns over adversarial ML, model poisoning, and backdoor attacks. We study server-side client identity inference from transmitted weight deltas using inertial (IMU) measurements, evaluated on the UCI Human Activity Recognition (HAR) benchmark as an accessible proxy for the IMU streams produced onboard connected vehicles. Across five attack classifiers and five non-IID partitions, an honest-but-curious server recovers client identity with near-perfect accuracy (approximately 1.000) from undefended updates, confirming a concrete identifiability risk. We then quantify the privacy-utility trade-off of a lightweight clip-then-noise defense by sweeping Gaussian noise (sigma in {0.00, 0.05, 0.10, 0.20, 0.50, 1.00}) at fixed clipping (C=1.0), and report formal (epsilon, delta)-DP budgets through Renyi accounting. A practical region (sigma in [0.1, 0.2]) drives attack accuracy to near-random while costing under 5% relative FL accuracy. Ensemble FL supplies complementary structural privacy with a 1/K anonymity-set bound and no noise penalty. Results are supported by cryptographic (SHA-256) train/evaluation gradient disjointness, three seeds, and a count-normalized attacker-advantage metric. We position HAR explicitly as a proxy and discuss what validation on true vehicular telemetry would require.

---


### 7. [Structure and Implementation of New Practical English Textbooks Driven by Artificial Intelligence](https://arxiv.org/abs/2609.02981)

**<font color=#1a73e8>作者：</font>** Ya Wang, Lei Zhang, Xueguang Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is changing the form of applied English materials from fixed paper sequences to adaptive learning systems that can diagnose learners, recommend tasks, and provide formative feedback. This paper studies the structure and application of a new practical English textbook driven by artificial intelligence. A five-layer architecture is proposed: knowledge mapping, learner profiling, task generation, feedback orchestration, and teacher-side governance. A prototype was tested on 186 non-English-major undergraduates for eight weeks of teaching. Compared with a static digital textbook, the proposed system increased the unit completion accuracy from 72.4% to 84.9%, raised the average score for speaking tasks by 10.8 points, and reduced the teacher's correction time by 31.6%. Therefore, an AI-driven textbook can maintain the stability of the curriculum while providing personalised learning paths, rich practice materials and traceable classroom data.

---


### 8. [Equation Recast for Canonical Operator Learning Across Parametric PDEs](https://arxiv.org/abs/2609.02982)

**<font color=#1a73e8>作者：</font>** Qiyun Cheng, Valentin Duruisseaux, Cesar F. Clauser 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning solution operators across broad parameter ranges can require substantial coverage of both input functions and physical parameters, particularly for purely data-driven parametric models. In addition, the resulting models may fail silently outside the training distribution. We introduce equation recast, which reformulates parametric operator learning as the learning of a single canonical operator. Parameter-induced operator variations are derived analytically from the governing equation and absorbed into effective sources, enabling zero-shot prediction across new parameter regimes. Across multi-parameter, nonlinear, and singular PDE settings, equation recast supports extrapolation, integrates sparse heterogeneous datasets in a shared canonical representation, and uses loss of convergence as an internal warning signal for failure of the recast iteration. In high-fidelity tokamak simulations for nuclear fusion, the framework unifies electron-temperature data across four device geometries through canonical-domain mapping within one jointly trained operator. Equation recast provides a route toward reusable neural PDE solvers combining equation-guided transfer, data efficiency, and monitorable inference.

---


### 9. [Boundary-Mutation Testing for Pattern-Based Secret Detection: A Rule-Level Method and Cross-Scanner Evaluation](https://arxiv.org/abs/2609.02983)

**<font color=#1a73e8>作者：</font>** Shweta Mishra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Pattern-based secret scanners are commonly validated with example-based fixtures that fix one variable: the text surrounding a credential. We introduce boundary-mutation testing to vary that context, generating credentials from each rule's own regular expression, embedding them in realistic source contexts, and classifying outcomes at the rule level rather than the tool level, yielding three detection metrics. Applied to three scanners - a 43-rule open-source scanner, Gitleaks 8.21.2, and TruffleHog 3.82.13 - detection in the primary subject holds at >=0.9976 across ten contexts but collapses to 0.5233 when a credential ends in a hyphen. Five rules are affected: two, with fixed-count quantifiers, fail totally and deterministically; three, with variable-count quantifiers, backtrack and match a truncated credential; an entropy fallback rescues some failures but downgrades their severity. We validate a repair restoring full robustness with no new false positives, and report a caution: a plausible first attempt silently regressed two rules, caught only by re-running the same battery. Gitleaks has an unrelated, source-confirmed defect - a hard-coded terminator allowlist causing total misses for most credential types - while TruffleHog shows no boundary fragility but narrowest coverage. We report marginal, not conditional, failure probabilities: one common token format is structurally immune, another fails once in 64; on 292,527 lines of real code, the false-positive ordering inverts relative to the synthetic corpus. Because per-type detection is deterministic, the comparison unit is ten credential types, not hundreds of samples; no recall difference reaches significance, so we report the null result, not a ranking.

---


### 10. [From Euclidean to Graph-Structured Data: A Survey of Collaborative Learning](https://arxiv.org/abs/2609.02984)

**<font color=#1a73e8>作者：</font>** Rémi Bourgerie, Šarūnas Girdzijauskas, Viktoria Fodor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The conventional approach to machine learning, that is, collecting data, training models, and performing inference in a single location, faces fundamental limitations, including scalability and privacy, that restrict its applicability. To address these challenges, recent research has explored collaborative learning approaches, including federated learning and decentralized learning, where individual agents perform training and inference locally, with limited collaboration. Most collaborative learning research focuses on Euclidean data with regular, grid-like structure (e.g., images, text). However, these approaches fail to capture the relational patterns in many real-world applications, best represented by graphs. Learning on graphs relies on message-passing mechanisms to propagate information between connected nodes, making it conceptually well-suited for collaborative environments where agents must exchange information. Yet, the opportunities and challenges of learning on graph-structured data in collaborative settings remain largely underexplored. This survey provides a comprehensive investigation of collaborative learning from Euclidean to graph-structured data, aiming to consolidate this emerging field. We begin by reviewing its foundational principles for Euclidean data, organizing them along three core dimensions: learning effectiveness, efficiency, and privacy preservation. We then extend the discussion to graph-structured data, introducing a taxonomy of graph distribution scenarios, characterizing associated statistical heterogeneities, and developing standardized problem formulations and algorithmic frameworks. Finally, we systematically identify open challenges and promising research directions.

---


### 11. [Tail-Likelihood Reinforcement Learning](https://arxiv.org/abs/2609.02987)

**<font color=#1a73e8>作者：</font>** Shrinivas Ramasubramanian, Daman Arora, Fahim Tajwar 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning typically optimizes average reward. For generative policies, the average can hide an important distinction: two policies can achieve the same mean reward while having very different chances of producing a rare but high-reward rollout. This matters as sampling increases during training and inference, since its benefit depends on retaining probability mass on high-reward outcomes. We propose to optimize this coverage directly. Rather than considering only expected reward, we consider all of its upper tails: for each reward threshold, how likely is the policy to exceed it? This turns a continuous reward into a family of binary success events. We introduce Tail-Likelihood Reinforcement Learning (TailRL), which maximizes the log-probability of exceeding a randomly chosen reward threshold. Its gradient gives more weight to rare, high-reward rollouts and can be interpreted as a mixture of Best-of-(k) gradients. TailRL requires only a simple modification to the advantage function, making it compatible with existing reinforcement learning pipelines. Across object localization, maze navigation, GUI grounding, and code optimization, TailRL leverages rare high-reward training samples to avoid suboptimal solutions and yields models that benefit more from additional samples at inference time.

---


### 12. [Mesh-Native Physics-Informed Graph Surrogates for TCAD-in-the-Loop Design Space Exploration](https://arxiv.org/abs/2609.02988)

**<font color=#1a73e8>作者：</font>** Leonid Popryho, Ayoub Sadeghi, Inna Partin-Vaisband  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-fidelity TCAD simulation of drift-diffusion transport remains the workhorse of emerging FinFET device design, but it is computationally expensive, especially for 3D structures where runtime escalates steeply with mesh complexity. This sharply limits multi-objective design space exploration. Existing machine-learning surrogates map a fixed set of design parameters to a few scalar device metrics, discarding the underlying physics and losing transferability across device geometries and families. A physics-informed graph attention network (GAT) surrogate is proposed. It operates directly on the tetrahedral TCAD mesh and predicts, at every mesh node, the electrostatic potential together with the electron and hole quasi-Fermi levels, the fundamental unknowns of the drift-diffusion system. Training combines a data loss with finite-volume current-continuity residuals, embedding carrier-transport physics into the objective. Operating on the mesh as a graph, the surrogate inherits size generalization: a model trained on few-fin meshes applies unchanged to substantially larger arrays, bounded at inference only by GPU memory. Per-node uncertainty from a deep ensemble drives an active-learning loop that screens large candidate pools in seconds and forwards only the most informative designs for full simulation. Benchmarked against Sentaurus Device on multi-fin tri-gate FinFETs, the surrogate reproduces the three drift-diffusion fields with sub-volt per-field RMSE and reaches a per-design throughput orders of magnitude higher than the full simulator. The advantage grows with device size: on large multi-fin arrays that are prohibitively slow to simulate directly, inference still completes in under a second per device, enabling Pareto-front exploration across device scales infeasible for direct TCAD sweeps.

---


### 13. [TRACE: Spatiotemporal Contact Memory Graph Network Simulator for Granular Dynamics](https://arxiv.org/abs/2609.02991)

**<font color=#1a73e8>作者：</font>** Changjian Zhou, Negin Yousefpour, Jie Qi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned graph simulators provide an efficient alternative to high-fidelity solvers for granular dynamics. However, granular motion depends strongly on inter-granular contact history, which is difficult to preserve when particle contacts form, break, and rearrange. Existing simulators mainly store temporal information in node features or node-level memory. Here we introduce TRACE, a graph-network simulator that stores interaction history directly on contact edges. Each edge maintains a persistent memory updated by attention-based message passing and a gated recurrent unit, while an edge-identity dictionary preserves this memory as the contact graph changes. A physics-structured decoder predicts inter-granular normal and tangential contact forces, enforces the Coulomb friction limit, and applies equal-and-opposite internal forces. The model is trained with single-step pretraining followed by autoregressive rollout fine-tuning. We evaluate TRACE on 2D and 3D granular column-collapse benchmarks. In both cases, TRACE produces stable, physically consistent long-horizon rollouts, closely reproducing the final deposit geometry and the kinetic energy released during collapse. Compared with graph network simulator (GNS) and node-memory graph neural simulator (NMGNS), TRACE reduces long-rollout position error by 31-62% and final-deposit error by 58-89% across the two benchmarks, while using fewer parameters and maintaining near-zero particle interpenetration. TRACE also achieves 12.2$\times$ and 8.9$\times$ speedups over the material point method (MPM) reference solver in 2D and 3D, respectively. Our code is available at this https URL.

---


### 14. [No-Regret Bayesian Optimization with Finite-Library Input-Warped Kernels](https://arxiv.org/abs/2609.02993)

**<font color=#1a73e8>作者：</font>** Edvin Ketabati Augustinsson, Robert A. Bridges  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian-process Bayesian optimization (GP-BO) excels at black-box optimization of costly functions, e.g., hyperparameter optimization (HPO) and multi-agent system (MAS) design. Convergence-rate guarantees exist for select methods, notably GP upper confidence bound (GP-UCB), but require a fixed kernel. Critically, the kernel encodes how input proximity affects objective value similarity. When raw coordinates poorly match this geometry - as with log-scaled hyperparameters or localized peaks - input warping can greatly improve sample efficiency, yet known GP-UCB proofs require a fixed kernel. We propose Finite-Library Input-Warped Bayesian Optimization (FLIWBO), which selects warps from a finite library of smooth input maps by any history-dependent rule. It adapts the input geometry to accelerate learning while retaining high-probability convergence guarantees under mild hypotheses, with an explicit $\sqrt(N_\varepsilon)$ library-size cost. Controlled diagnostics show that finite-library warping repairs planted geometry mismatches and identify FLIWBO failure cases. Across four repeated benchmarks - warped synthetic objectives, a confidence-fence trap, and Fashion-MNIST HPO - FLIWBO-UCB beats raw-coordinate GP-UCB under misspecified geometry, escapes traps that defeat even oracle-warp expected improvement, and recovers much of the gain from manual log scaling, while leading the tested methods that admit a matching regret guarantee. A 20-dimensional MAS design study further shows feasibility under costly noisy evaluations. Code for experiments is available: this https URL.

---


### 15. [Evaluating Graph Neural Networks for Change-Criticality Classification in Maritime Navigation Charts](https://arxiv.org/abs/2609.02996)

**<font color=#1a73e8>作者：</font>** Abhishek Potnis, Jacob Arndt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) are a class of neural networks suitable for learning on graph-structured data. Their application to spatial data is a natural extension, however its relatively unclear which message-passing operations, architectural configurations, and graph representation is best suited for classifying changes to objects in electronic navigational charts (ENCs)--geospatial vector datasets used for marine navigation. Maintaining these datasets is a challenge, and categorizing changes to objects in the ENC based on their significance to navigational safety is of particular importance. Here, we propose to represent these vector navigation datasets as a graph structure where the spatial objects serve as nodes and their spatial and semantic relationships form edges. We encode both the old ENC dataset and new ENC dataset into a pair of graphs and frame the task as a graph-pair classification problem. Building on this representation, we investigate the use of GNN architectures to classify whether the encoded graphs constitutes a critical or non-critical risk to navigational safety. We train and evaluate several GNN architectures and model configurations on ENC changes reviewed by maritime experts. Our results demonstrate that graph-based representations improve the classification of ENC updates, providing a scalable approach for automating or improving ENC maintenance workflows.

---


### 16. [Population-Calibrated Graph Screening at 835-Million-Address Scale, with Label-Free Transfer to New Chains](https://arxiv.org/abs/2609.03036)

**<font color=#1a73e8>作者：</font>** Yury Korolev  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Compliance screening of blockchain addresses is, in practice, a lookup against sanctions registries plus clustering heuristics; it fails on unlabelled addresses and on chains with no label coverage at all. We describe a deployed system that scores an address by its position in a multi-chain transaction graph rather than by its presence in a list. The substrate is a single graph of 835,330,427 addresses and 15,826,261,934 edges across five EVM chains; a shared inductive encoder with per-chain normalisation feeds two scoring heads. Decision thresholds are exact quantiles of the score distribution over the full population, scanned per chain segment, so the alert volume is known in advance. We report: label-free transfer: heads trained on two chains recall 0.8598 / 0.8182 / 0.9967 of held-out positives on Base, Arbitrum and Gnosis at a $10^{-3}$ population alert rate, with no target-chain labels in head training; a static lead-time replay over 68 external registry events: 40 of 68 (58.8%) flagged at the 0.1% budget, $\times$152 over an event-level random-flagging baseline, with first on-chain appearance a median of 528.8 days (Ethereum) / 647.8 days (Tron) before public designation; a serving path whose score is bit-identical to the offline artefact at end-to-end p50 151 ms, gated by a 2,882-address drift panel; and an adversarial harness of eight recurrent reinforcement-learned archetypes that passes an 8-criterion degeneracy audit and, on a detector-independent snapshot, exposes a measured blind spot of the deployed heads against synthesised behaviour.

---


### 17. [IDSPACE: A Novel Document Generator for Reliable Evaluation of Digital Identity Verification Systems [Extended Technical Report]](https://arxiv.org/abs/2609.03052)

**<font color=#1a73e8>作者：</font>** Lulu Xie, Yancheng Wang, Kanchan Chowdhury 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As services move online, trust institutions such as banks, lenders, and governments must verify the identity of remote users. Fraud detection tools are widely available, but evaluating and fine-tuning them remains difficult because identity documents are sensitive and therefore scarce. Synthetic data generation offers a path forward, and demand is clear: our prior work in this area has been downloaded over $11{,}000$ times (aggregated from eight parts). We introduce IDSpace, extending this line of research in three directions. First, we propose model-guided Bayesian optimization, which tunes generation parameters to maximize both visual similarity and prediction consistency with target-domain models given only a few samples from a target domain. Second, we decouple user-specified metadata (demographics, fraud patterns, capture device) from automatically tuned control parameters (font styles, noise levels, image quality), allowing users to configure evaluations without low-level expertise. Third, we expand beyond template images to support scanned and mobile-captured documents. Experiments show IDSpace improves evaluation consistency by $15-45\%$ over baselines including CycleGAN, diffusion inpainting, and non-guided optimization, using only a few real samples, while improving training accuracy by up to $9\%$ and SSIM similarity with the target domain by $10\%$. We also released a new dataset consisting of $359{,}240$ high-quality synthetic documents across ten European ID types.

---


### 18. [Differentially private federated learning with Byzantine-robust aggregation: A cross-domain framework for secure model training in banking and healthcare systems](https://arxiv.org/abs/2609.03064)

**<font color=#1a73e8>作者：</font>** Srikumar Nayak  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning allows banks, hospitals, and other regulated organizations to train a shared model without moving raw records off their own servers, which is attractive wherever data protection law or competitive sensitivity rules out pooling data centrally. Two problems limit how far this promise can be trusted in practice. First, the parameter updates that clients exchange still leak information about local records through gradient inversion and membership inference attacks. Second, an honest averaging rule such as FedAvg has no defense against a subset of clients that submit corrupted or adversarial updates, so a small number of malicious or compromised participants can quietly steer the shared model off course. This paper presents a federated learning framework, DP-BR-FedAvg, that combines a Gaussian-mechanism differential privacy layer with a coordinate-wise trimmed-mean Byzantine-robust aggregation rule, evaluated on a simulated cross-institutional classification task resembling fraud and clinical-risk scoring. Across sixty communication rounds with twenty clients, a quarter of them Byzantine, plain FedAvg collapses on the minority class (F1-score 0.030) while the proposed framework recovers substantially more of the signal (F1-score 0.119) while bounding the privacy loss of any single client's contribution. A Byzantine-robust aggregator with no privacy layer performs best in raw accuracy, quantifying the cost privacy imposes on robustness. The results show that privacy and robustness mechanisms interact rather than simply add, and that system design for regulated, adversarial, cross-institutional settings needs to budget for that interaction.

---


### 19. [Learnable composition for neural operators](https://arxiv.org/abs/2609.03069)

**<font color=#1a73e8>作者：</font>** Zituo Chen, Baiming Zhang, Sili Deng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators are fast, differentiable surrogates for physical simulation, but their accuracy often degrades when domain geometry, size, or operating conditions differ from training. Supervised adaptation can recover accuracy, but even a small target set requires costly high-fidelity simulations. We therefore ask how pretraining and transfer can be designed together to reduce this deployment cost. LatentDDM first pretrains a neural operator to predict fields on small subdomains. For a new setting, it freezes this operator and trains only a lightweight module that composes the local predictions. We evaluate our method on two complementary problems: steady Darcy flow, where long-range pressure coupling must extend across increasingly large porous domains, and unsteady incompressible flow around a pitching airfoil, where rollout errors compound as target pitching frequencies exceed the training range. Compared with the capacity-matched models that process the full domain at once, LatentDDM's error is 36-56% lower on larger Darcy domains after adaptation with 16 target simulations. It also improves 20-step field rollouts in fast-pitching airfoil flow, both zero-shot and after few-shot calibration. These results identify the co-designed local pretraining and composition-level transfer as a promising design principle for physical foundation models.

---


### 20. [Position: Unlabeled IS NOT Equal to No Human Supervision in Visual Learning](https://arxiv.org/abs/2609.03077)

**<font color=#1a73e8>作者：</font>** Dong Lao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This position paper argues that the absence of labels does not imply the absence of human supervision in visual learning, and urges the research community to identify sources of supervision more explicitly. Many recent methods in computer vision build upon representations learned from large-scale unlabeled data, and are therefore grouped under the same umbrella term ``unsupervised.'' However, different data curation schemes and training objectives embed substantially different human priors on which models rely, and we argue that one ``unsupervised'' umbrella term is no longer capturing these distinctions. This ambiguity makes it harder to compare unsupervised learning research conducted under different assumptions, coinciding with a sharp decline in papers titled with ``unsupervised'' in flagship computer vision conferences since 2021, despite continued growth of the field. While we fully embrace pre-training as a strong foundation for modern computer vision, we advocate for a community-level effort toward greater conceptual clarity: authors are encouraged to disclose priors in data selection and learning objectives, and to specify which components of a learning pipeline depend on which assumptions. Standardized disclosure practices can improve academic communication, ensure fairer comparisons, and preserve methodological diversity in unsupervised learning.

---


### 21. [Exemplar: Classical Priors Complement Frozen Features for Few-Shot Microscopy Segmentation at Native Resolution](https://arxiv.org/abs/2609.03080)

**<font color=#1a73e8>作者：</font>** Michal Průšek, Adam Novozámský, Filip Šroubek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmenting a new biomedical dataset usually means a domain-specific model trained on substantial annotation, or a foundation model steered at inference time. We present Exemplar, a few-shot segmenter that fuses a frozen DINOv3 backbone with a fixed bank of classical native-resolution filter responses in one lightweight head, fitted from the support masks alone. In the few-mask, native-resolution regime, classical priors and frozen self-supervised features are complementary: fused in one head, a single fixed configuration spans eleven biomedical imaging datasets. Under the same head, the classical bank alone reaches 0.693 on the eleven-dataset panel, scored by foreground intersection-over-union or centreline Dice, and the frozen features alone 0.672; the bank leads on seven of the eleven and the features on the rest, and fused they reach 0.782. Against five forward-pass few-shot methods, Exemplar leads in 54 of 55 method-dataset comparisons, 52 of them significant after Holm correction. From a single annotated mask it reaches 0.703 on the same panel, against 0.682 for a from-scratch nnU-Net trained on that same mask. At eight masks nnU-Net overtakes it on the panel mean, chiefly on centreline agreement, but takes 16-77x longer to fit.

---


### 22. [A Bayesian Correlated Equilibrium for Early Insider-Threat Detection](https://arxiv.org/abs/2609.03096)

**<font color=#1a73e8>作者：</font>** Javed M. Shah, Ian A. Kash, Natalie Parde  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We model insider threat detection as a dynamic Bayesian game in which a platform coordinates a committee of strategic certifiers to sustain equilibrium among honest users and detect malicious deviations before exfiltration. Certifiers and users operate under a Bayesian Temporal Correlated Equilibrium (BTCE), where a sealed-envelope correlating device issues private recommendations over time and obedience is verified at every on-path information state. Unlike Stackelberg formulations, BTCE coordinates heterogeneous certifiers without requiring commitment power. We incorporate present bias and loss aversion to capture impulsive escalation dynamics, enabling 1.7--4.5 days earlier detection than rational baselines. We prove three guarantees: (1) calibrated intervention losses make recommended behavior a current-self best response despite behavioral biases, (2) controlled evidence accumulation guarantees intervention in bounded expected time before exfiltration, and (3) median aggregation confines implemented actions to the honest recommendation range when fewer than half of certifiers are Byzantine. On CERT r6.2 our mechanism achieves up to 28.3% pre-exfiltration detection with false positives below 1.6%, while both a transformer baseline and a streaming provenance approximation (HOLMESLite) achieve near-zero pre-exfiltration detection under comparable constraints.

---


### 23. [Distilling deep optical flow stereo methods to retrieve dense three-dimensional wind fields](https://arxiv.org/abs/2609.03100)

**<font color=#1a73e8>作者：</font>** Thomas J. Vandal, Dong L. Wu, James L. Carr 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geostationary atmospheric motion vectors (AMVs) provide the dense horizontal wind vectors (u,v) and heights ingested into data assimilation systems. Traditional AMVs track features using window-based cross-correlation and estimate heights via infrared brightness temperatures paired with numerical weather prediction (NWP) background states, creating a circular dependency that yields inaccurate heights, high computational cost, and sparse retrievals. Stereo winds from GEO-GEO and GEO-LEO geometrically resolve heights from parallax shifts across different poses, eliminating NWP dependence and improving accuracy, but they remain computationally heavy with limited coverage. In this work, we replace window-based tracking in stereo matching with deep optical flow for efficient, improved retrieval. Fine-tuning balances a self-supervised geometric residual loss with supervised radiosonde reconstruction. To eliminate multi-satellite overlap requirements, we distill the stereo teacher into a single-satellite student model. Chi-square and height uncertainties from the teacher are emulated by the student for quality assurance. The student generates winds across full-disk GEO imagery globally. Validation compares stereo and student models against radiosondes, operational AMVs, ERA5 reanalysis, and EarthCARE cloud profiles. Results through triple collocation show that stereo winds improve performance beyond operational AMVs for water vapor bands (6.2, 6.9, and 7.3 {\mu}m), wit degradation in the long-wave infrared (11.2 {\mu}m) band.

---


### 24. [WireSeg-32K: A Physics-Grounded Synthetic Dataset for Wire Instance Segmentation](https://arxiv.org/abs/2609.03102)

**<font color=#1a73e8>作者：</font>** Zilin Dai, Lehong Wang, Yi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deformable linear objects such as wires and cables are difficult to segment because they are thin, highly deformable, and frequently self-occluded, while large-scale instance-level annotations are expensive to obtain in real scenes. Existing resources either focus on cable tracing or semantic segmentation under constrained settings, or generate visually plausible images without physically grounded wire deformation. We present WireSeg-32k, a synthetic dataset for wire instance segmentation with 32,000 RGB images, instance masks, depth maps, and a complementary real-world test set with annotations. To generate this dataset, we develop DeformX, a co-simulation pipeline that couples Cosserat-rod dynamics with photorealistic Isaac Sim rendering, enabling physically plausible, contact-consistent wire shapes, CAD-based wire assets, and diverse visually grounded scenes. As a simple baseline, LoRA fine-tuning SAM3 on WireSeg-32k alone improves real-world mAP@75 by 10.2% over the off-the-shelf model, showing that physically grounded synthetic data can transfer to real wire perception.

---


### 25. [Scaling Laws, Tabular Data and Actuarial Ratemaking Models](https://arxiv.org/abs/2609.03106)

**<font color=#1a73e8>作者：</font>** Ronald Richman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws in modern deep learning describe how held-out loss improves as model capacity, training data, and compute increase, often following power-law trends. We investigate whether analogous scaling regularities arise in actuarial ratemaking, where data are tabular, heterogeneous, and noisy, and where classical models such as GLMs remain strong baselines. Using a real-world motor insurance portfolio, we train models from different families across increasing fractions of the training data and multiple random seeds, evaluating out-of-sample Poisson deviance, a likelihood-based loss for Poisson count predictions in which lower values indicate better held-out fit. We find that all model families improve with additional data, but scaling exponents differ substantially: TabM exhibits markedly stronger data scaling than purely supervised tabular Transformers and standard MLP baselines. Transformer variants show weak parameter scaling unless augmented with additional inductive biases (TabM-style adaptation or self-supervision). These results provide quantitative guidance on model selection by data regime and suggest that effective scaling on actuarial tabular tasks depends on architecture and loss function objective design, with simple increases in Transformer size providing limited gains.

---


### 26. [Kernel Reboot: Breaking the Boundaries of Neural Tangent Kernels for Neural Fields](https://arxiv.org/abs/2609.03117)

**<font color=#1a73e8>作者：</font>** Amir Mallak, Alaa Maalouf, Lior Wolf 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural fields (NFs) map continuous coordinates to signals such as color or density, but fast high-quality reconstruction from sparse observations remains difficult. Classical Neural Tangent Kernel (NTK) regression gives closed-form fits, yet it is fundamentally linear and cannot accumulate reusable task priors. We develop three algorithms that address these gaps. NTK-KIP learns a distilled support set of coordinates (and optional labels) so that a finite NTK can inpaint large missing regions from little observed data, yielding a compact non-linear representation instead of a raw kernel solve. MetaQuill meta-learns a shared initialization for an INR so that new scenes can be adapted by updating only a small task-specific weight offset, which provides true feature learning and a reusable prior. Finally, MetaQuill-KIP fuses both ideas: it seeds the task with a KIP-style non-linear warm start, then refines only that small offset around the meta-learned initialization. MetaQuill-KIP achieves high-PSNR reconstructions and semantically plausible inpainting under very sparse observations, while requiring only lightweight per-instance adaptation, whereas diffusion-style baselines typically depend on large pretrained generative priors and costly per-image tuning. This shows that NTK-driven neural fields can be made both non-linear and meta-learnable, narrowing the gap between analytic kernels and practical few-shot reconstruction.

---


### 27. [SecDT: A Profile-Based Security Layer for TRDP Communications](https://arxiv.org/abs/2609.03133)

**<font color=#1a73e8>作者：</font>** Erlantz Alonso, Igor Lopez, Jasone Astorga  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Train Real-time Data Protocol (TRDP) is widely used on rolling stock but it provides limited native support for cryptographic protection. Furthermore, the multicast traffic profile used in TRDP Process Data to exchange critical information between onboard subsystems makes the introduction of cryptographic protection a challenge. This paper presents a lightweight security layer for secure TRDP communication that implements a number of security profiles built around modern cryptographic algorithms. This additional layer relies on an On-board Key Management System (OKMS) for both security profile negotiation, dynamic key distribution and key lifecycle management. The security profiles allow for cryptographic agility and flexibility, ranging from simple authentication to Authenticated Encryption with Associated Data (AEAD) algorithms. The security profile negotiation procedure guarantees all TRDP End Devices (ED) on a common Communication ID (ComID) share the same security profile and can therefore process each other's messages. A prototype implementation based on mbedTLS and Arm Platform Security Architecture (PSA) was developed and evaluated. Experimental results demonstrate manageable overhead, suitable for the real-time and time-sensitive communication found on rolling stock.

---


### 28. [Beyond Small Patches: Black-Box Detection and Purification of Diverse Backdoor Triggers](https://arxiv.org/abs/2609.03139)

**<font color=#1a73e8>作者：</font>** Ahmed Abdelnaby, Mohamed Elmahallawy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) are increasingly deployed in real-world vision systems, yet their predictions can be covertly manipulated by backdoor attacks, in which malicious triggers cause targeted misclassification while preserving high clean accuracy. Existing defenses often rely on model internals, training data, or clean validation samples, making them difficult to deploy when only black-box access to a trained model is available. We propose TRIM (Trigger Removal by Identifying Manipulated Regions), a deployment-oriented black-box defense that detects and selectively removes backdoor triggers at inference time without requiring model internals, training data, or clean samples. The key insight behind TRIM is to identify image regions that are responsible for anomalous model behavior and purify only those regions while preserving benign content. TRIM innovates via three key components: (i) region-based segmentation with deep feature representations, (ii) adaptive trigger discovery through inpainting and diffusion-based reconstruction to isolate regions responsible for misclassification---without assumptions about trigger type, shape, or location, and (iii) selective region purification that cleans poisoned regions while retaining benign content. To support practical deployment, TRIM further caches feature embeddings of previously identified triggers, enabling efficient recognition and avoiding redundant detection and purification. Extensive experiments across diverse datasets and backdoor types, including blended, sparse, varying-size, and multiple triggers, show that TRIM consistently outperforms existing black-box defenses, reducing attack success rates (ASR) to as low as 1.16% while preserving clean accuracy of up to 87.87%. These results demonstrate that effective backdoor mitigation is possible at inference time even when the defender has no access to any auxiliary data.

---


### 29. [VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement](https://arxiv.org/abs/2609.03153)

**<font color=#1a73e8>作者：</font>** Wenzhuo Xu, Yuchen Zhu, Chongjian Ge 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual fluency in generated video does not imply physical reliability, and a scalar quality score alone is incapable of indicating the obligation a clip violates or the moment it fails. We present VeriPhy, an auditable physical-verification system in which a text-only planner compiles the prompt into typed physical obligations and a statically validated execution plan before any frame is observed. During execution, observations gate and scope only declared calls to frozen low-level experts (e.g., segmentation and tracking, counting, eleven typed physical measurements over the resulting tracks, depth, OCR, and audio-event detection). Each action returns a provenance-carrying evidence record whose payload, when usable, is either a typed measurement or an explicitly tagged learned state. Typed resolvers and fixed composition map usable records to a three-valued state (supported, contradicted, or unknown, surfaced as plausible, implausible, or abstain) with full provenance, so that every verdict is traceable to the evidence that produced it. We anchor evaluation in a 1,500-clip corpus of human-annotated flaw records that localize real generation failures in prompt reference, space, and time. On a 149-clip core carrying 304 such records, VeriPhy accounts for 228, against 164 for a published question-decomposition evaluator given the same clips and the same claims. Recall alone does not separate it from prompting the same backbone monolithically, which reaches 222; what separates them is that each decision retains its evidence record and provenance, making the traces auditable one verdict at a time and usable as the interface through which a critic verdict could be written back into generation.

---


### 30. [Signal-Driven Pervasive Game Design: The LifeSync-Games Framework as a Player Experience Integration Layer](https://arxiv.org/abs/2609.03169)

**<font color=#1a73e8>作者：</font>** J. Macías-Cáceres, F. Gutiérrez-Vela, P. Paderewski-Rodriguez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Pervasive games extend the magic circle across spatial, temporal, and social dimensions, yet treat the player's physiological and cognitive state as a passive receptor rather than an active signal. This paper presents LifeSync-Games (LSG), a framework that (unlike proposals treating player signals as an additional dimension), operationalizes them as a Player Experience Integration Layer (PEIL) acting transversally across the three existing pervasive dimensions through verified real-world signals: physical activity, sleep quality, memory, and decision speed. The framework introduces a gamified integration artifact (the LSG portal) that mediates the real <-> virtual exchange through redeemable points, real-world missions, and structural gamification. Five HCI design principles grounded in Self-Determination Theory and Flow Theory are proposed, instantiated across six commercial video games, together with a study protocol (n = 70-80 participants, quasi-experimental design). This paper reports the design stage of LSG: rule thresholds and portal parameters are design decisions pending empirical calibration; no data collection has yet been conducted. The main contribution is a theoretically grounded framework and validation protocol positioning player-sensitive integration as the mechanism enabling pervasive games to respond to the player's actual biological and cognitive state.

---


### 31. [Portable Causal Fairness Across Synthetic Data Generator Families](https://arxiv.org/abs/2609.03180)

**<font color=#1a73e8>作者：</font>** Steven Golob, Sikha Pentyala, Martine De Cock  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a statistical agency or regulator releases synthetic data in place of sensitive records, it chooses the generator that produces the table, and can shape that generator so unfair pathways are absent. DECAF made this concrete on one non-private GAN: three fairness definitions become three sets of edge cuts on the generator's causal graph. Whether the mechanism belongs to DECAF, or to causal factorisation itself, was untested. We port all three definitions to nine generators from three unrelated families (marginals-based, GAN, and diffusion, each with differentially private variants), across three levels of formal privacy guarantee, over 2,520 matched-pair runs on Adult and COMPAS datasets. The mechanism transfers everywhere, and our new causal diffusion backbone yields the fairest release of any family we tested, at fidelity close to the marginals tier. Applying the cut barely moves fidelity, only costs a downstream classifier about $0.07$ to $0.15$ AUC on average, and adding privacy guarantees don't make the data less fair.

---


### 32. [RoboTok: An Internet-Scale Data Engine for Human Demonstration Retrieval and Dexterous Manipulation Learning](https://arxiv.org/abs/2609.03199)

**<font color=#1a73e8>作者：</font>** Howard Qian, Yiting Chen, Yunfei Xie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robot learning increasingly depends on broad and diverse demonstrations, yet collecting robot data remains expensive and poorly suited to covering the long tail of real-world tasks. To address this bottleneck, we introduce RoboTok, an internet-scale data engine that, given a query human manipulation video, retrieves manipulation-relevant human demonstrations from web videos for training dexterous robot policies. Specifically, we learn a latent motion space from 3D hand trajectories expressed in estimated actor-centered reference frames. This representation enables manipulation behaviors to be compared across variations in camera viewpoint, scene appearance, and actor occlusions, while remaining compact enough for efficient search and continual indexing over internet-scale video collections. We evaluate RoboTok against existing robot-data retrieval approaches on retrieval benchmarks and downstream robot policy performance. Our results show that RoboTok retrieves more relevant manipulation demonstrations and improves downstream task success, establishing hand-pose trajectory-aware retrieval as a way to make web video a scalable and continuously growing source of supervision for robot learning.

---


### 33. [ProgResViT: Progressive Resolution and Width for Adaptive Vision Transformers](https://arxiv.org/abs/2609.03216)

**<font color=#1a73e8>作者：</font>** Ali Hojjat, Janek Haberer, Olaf Landsiedel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) typically process every image using a fixed input resolution and model width, even though many images can be classified with substantially less computation. We introduce ProgResViT, an input-adaptive ViT that performs inference progressively across multiple rounds. The first round processes a low-resolution image with a narrow subnetwork. Inference terminates when the prediction is sufficiently confident; otherwise, the model reuses the representations produced in the current round and proceeds with a higher-resolution input and a wider subnetwork to refine its prediction. As all rounds share a single backbone, we propose Progress-Conditioned Soft Gating (PSG), which conditions token fusion and layer outputs on the current round, block, and input resolution. On image classification, applying ProgResViT to DeiT yields better accuracy-compute trade-offs than adaptive-width, adaptive-depth, and dynamic-token baselines. With knowledge distillation, a DeiT-based ProgResViT achieves 84.9% top-1 accuracy, slightly exceeding the reported DeiT-III-S accuracy under a comparable evaluation setting. We show that the same design also provides favorable accuracy-compute trade-offs for self-supervised DINO representations and downstream semantic segmentation. Code is available at this https URL.

---


### 34. [The 2026 PNPL Competition: Word Classification and Efficient Cross-Subject Generalisation in LibriBrain100](https://arxiv.org/abs/2609.03231)

**<font color=#1a73e8>作者：</font>** Francesco Mantegna, Gereon Elvers, Dulhan Jayalath 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ambition of the 2025 PNPL competition (Landau et al., 2025) was to launch a multi-year curriculum for non-invasive speech decoding. Designed to progress from foundational tasks toward the linguistic complexity required for a practical brain-computer interface (BCI), it set the stage with speech detection and phoneme classification tasks. Winning submissions reached F1-macro scores of 95.6% and 73.6% on the respective tasks (Elvers et al., 2026), highly significant advances. This success was built on the LibriBrain dataset (Özdogan et al., 2025), the largest within-subject MEG dataset recorded at the time with ${\sim}50$ hours of data for one subject. However, while within-subject scale drives strong decoding performance, a practical BCI must generalise to new users from minutes of data, not hours.
The 2026 PNPL competition responds to this challenge with LibriBrain100 (Mantegna et al., 2026), an extended LibriBrain dataset with 32 additional subjects (${\sim}40$ minutes each) plus even more within-subject data (${\sim}80$ hours). Advancing the curriculum of tasks to focus on word classification, two complementary tracks are presented in this competition: the Deep track targets within-subject word classification at scale, aiming at the best possible performance; the Broad track targets cross-subject generalisation, progressively reducing the amount of subject-specific fine-tuning data from ${\sim}40$ to ${\sim}20$ to ${\sim}10$ minutes, a duration that falls within a clinically feasible range and brings us a step closer to a non-invasive BCI capable of restoring communication to people living with profound paralysis.

---


### 35. [Counting Animals in Camera-Traps Image Sequences without Count Labels: Winning Solution to the iWildCam 2021 Challenge](https://arxiv.org/abs/2609.03233)

**<font color=#1a73e8>作者：</font>** Fagner Cunha, Juan G. Colonna, Eulanda M. dos Santos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera traps have become an essential tool for wildlife monitoring, motivating the development of computer vision methods for the automated extraction of information from these data. While most prior work has focused on species identification, many ecological applications also require estimating the number of unique individuals appearing across short image sequences. This task is particularly challenging because camera traps typically acquire bursts of images at approximately one frame per second, creating large temporal discontinuities that may make conventional multi-object tracking methods unreliable, and because manually collecting individual count annotations is prohibitively expensive. In this work, we describe the winning solution to the iWildCam 2021 Challenge, which introduced a benchmark for counting animals at the sequence level under realistic annotation constraints where count annotations are unavailable for training. Our approach, MaxBoxCount, combines a strong species classification pipeline with a simple yet effective counting heuristic based on MegaDetector detections to estimate the number of unique individuals without requiring count annotations. Code is available at this https URL.

---


### 36. [B2B Customer Conversion Prediction: A Document Representation, Graph Theory, and CatBoost Driven Methodology](https://arxiv.org/abs/2609.03239)

**<font color=#1a73e8>作者：</font>** Tianqi Wang, Sheikh Shams Azam, Wan Eih Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the one-time selling B2B context, the buying cycle may last months or even years. During the long process, targeting customers that have a high potential to make purchases and recommending personalized campaigns accordingly are important for effective marketing. For this goal, we study the following problems, B2B customer data aggregation, customer feature generation, and prediction of whether a B2B customer would show interest in making a purchase (i.e., prediction of conversion into sales funnel). We propose an algorithm to aggregate individual contacts to the B2B customer level based on multiple keys. For non-standardized keys such as company names, we propose a novel architecture to cluster them in a domain encompassing irregularities such as spelling mistakes and spelling variants. We then define and generate a set of features and apply the CatBoost model for customer conversion prediction. Our framework achieves 91\% prediction accuracy. Based on the prediction results and analysis of the model, we then discuss personalized campaign recommendations to foster conversion.

---


### 37. [Memetic Search for Supersingular Elliptic Curves over $\mathbb{F}_p$](https://arxiv.org/abs/2609.03249)

**<font color=#1a73e8>作者：</font>** Ismel Martínez-Díaz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The search for supersingular elliptic curves is a fundamental computational problem in isogeny-based cryptography. A recent metaheuristic formulation over $\mathbb{F}_{p^2}$ introduced the NonMultiplicity Distance (NMD) objective, measuring the deviation of the Frobenius trace from a multiple of $p$, and showed that uninformed random search fails beyond $\approx 10^{13}$ candidates. This work investigates metaheuristic search over the prime field $\mathbb{F}_p$, the setting for oriented isogeny protocols such as CSIDH, OSIDH, and SQISign. Although the candidate space decreases from $p^2$ to $p$, the supersingular locus is asymptotically sparse ($O(\sqrt{p}\log p)$ curves), keeping the search exponentially difficult. We formulate a memetic algorithm tailored to $\mathbb{F}_p$ using a one-dimensional $j$-invariant chromosome, bit-level recombination, adaptive mutation, and periodic local search under the NMD objective. Benchmarks across 30 independent seeds at 40-bit, 46-bit, and 51-bit prime sizes ($p \approx 1.13\times 10^{15}$) show that the algorithm discovers an exact supersingular curve at 46 bits and consistently converges to ``near-supersingular'' ordinary curves with Frobenius traces remarkably close to zero: best NMD values of 19 at 40 bits and 3 at 51 bits, corresponding to relative trace deviations of $1.3\times 10^{-5}$ and $4.5\times 10^{-8}$ across the Hasse interval. These results demonstrate that NMD-driven memetic search effectively navigates the sparse $\mathbb{F}_p$ landscape and systematically locates near-supersingular structures.

---


### 38. [An Ensemble-Based Self-Taught Learning Approach for Parking Space Classification Under Limited Data](https://arxiv.org/abs/2609.03258)

**<font color=#1a73e8>作者：</font>** Lucas de Oliveira Cunha, Joelton Deonei Gotz, Paulo Lisboa de Almeida 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parking spot classification is a fundamental task in intelligent transportation systems, yet most deep learning approaches rely on large amounts of annotated data and exhibit limited generalization across heterogeneous environments. To address these limitations, we investigate a self-taught learning framework based on unsupervised representation learning with convolutional autoencoders. The proposed approach learns transferable visual representations from unlabeled data and reuses the learned encoders as fixed feature extractors for supervised classification with limited annotated samples in the target domain. To further enhance robustness and mitigate architectural bias, an ensemble of heterogeneous autoencoders is employed, with independent classifier heads and prediction fusion at inference time. Experiments conducted on the PKLot and CNRPark benchmarks under cross-dataset evaluation protocols show that the proposed ensemble-based strategy substantially reduces annotation requirements while improving robustness under significant domain shifts, achieving accuracies between 93\% and 96\% in data-constrained scenarios.

---


### 39. [MedQA-MM: Shortcuts Behind Medical Visual Reasoning](https://arxiv.org/abs/2609.03261)

**<font color=#1a73e8>作者：</font>** Benlu Wang, Yifan Zhang, Jiaqing Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A benchmark score credits final answers, but not the route by which an item can be answered. In medical multimodal multiple-choice questions (MCQs), this distinction matters because a correct answer can be supported by the intended image finding or by benchmark-preserved cues in the wording of answers, non-visual clinical text, visible image text, artificial annotations, or device/context artifacts. We call the resulting score-level overinterpretation reasoning inflation. Here, a route is an observable input path that can support answer selection, not a claim about the model's hidden cognition. Across six medical multimodal MCQ datasets, we separate candidate cues from behavioral evidence through prompt- and image-side audits, modality ablations, and matched repairs that preserve the medical target and answer key. In a 13-configuration open-model panel, full-input accuracy is 62.63%, while text-only and options-only settings achieve 53.96% and 29.71%, respectively. Removing length-gap, absolute/conspicuous, and spatial/prepositional cues lowers accuracy by 6.58, 3.50, and 4.77 percentage points. We also construct MedQA-MM, a 1,000-item shortcut-mitigated subset, where text-only and options-only accuracy fall to 5.21% and 12.33%. This does not imply that models never use images; it shows that medical image-reasoning claims require route-level evidence.

---


### 40. [Selective Hypergraph Refinement for Frozen Graph Clustering](https://arxiv.org/abs/2609.03265)

**<font color=#1a73e8>作者：</font>** Zimo Si  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing graph-clustering methods typically improve clustering performance by optimizing model parameters and node representations. Effective means of further improving the clustering results of an already trained and frozen model, however, remain limited. We study post-processing for frozen graph clustering. After checkpoint fixation, the procedure uses no labels and updates neither model parameters, node representations, nor the original graph structure. Instead, it exploits an attribute hypergraph to supplement higher-order relations that ordinary graphs cannot readily express, thereby refining existing cluster assignments. Because global hypergraph refinement can yield both performance gains and erroneous updates, we propose Selective Hypergraph Refinement (SHR). The method generates candidate residual directions from the hypergraph and evaluates their reliability using graph structure, node attributes, and matched-null evidence. It updates only nodes with sufficient support and otherwise retains their original assignments. Further analysis shows that whether a node changes cluster is jointly governed by its native assignment gap and the directional strength of the refinement. In a controlled common-suite evaluation, 13 of 15 backbone-dataset cells had a positive mean macro gain, one produced exact no-action, and one was negative. The cell-equal macro gain was 0.066 pp (95% bootstrap CI, [0.030, 0.107] pp), while only 0.209% of hard assignments changed on average. A broader 15-combination native-interface evaluation yielded a macro gain of 0.137 pp at a mean change ratio of 0.375%. These results indicate that frozen clustering outputs retain a limited but measurable refinement space after training. The effect is heterogeneous across backbone-dataset pairs, and broader coverage also increases exposure to negative transfer.

---


### 41. [After Cheap Discovery: From unknown to known-and-unfixed](https://arxiv.org/abs/2609.03266)

**<font color=#1a73e8>作者：</font>** Bahman Sistany  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated vulnerability discovery has removed the scarcity of expert attention that protected most software. The response has concentrated on discovery and on repair, and both are becoming cheaper. This article argues that neither cost curve determines exposure. What determines it is remediation coverage at the release decision: the fraction of identified vulnerabilities fixed before a product ships, and the residue of known, assessed, unremediated flaws an organisation has decided to ship with. Four arguments follow. The residue is not a random sample of what was found, because triage sorts on cost and the expensive cases are architectural. The deferred backlog is itself a high-value artifact. Documented awareness alters an organisation's legal and market position, and produces an adverse selection that the price of software does not reflect. And no regulatory instrument reaching vendors triggers on internal knowledge -- every one fires on exploitation observed by a third party -- which leaves the distance between what a vendor knows and what it must disclose entirely at the vendor's discretion. CISA's Binding Operational Directive 26-04 is examined as the exception that shows what a solution requires. Release coverage is not currently measured, and measuring it is the precondition for liability, insurance or procurement to act.

---


### 42. [Long-Range Indirect Control-Flow Prediction in Stripped Binaries via Dual Virtual Hubs and Multi-Task Graph Learning](https://arxiv.org/abs/2609.03280)

**<font color=#1a73e8>作者：</font>** Kun Liu, Zhengming Ding, Chenke Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recovering indirect control-flow (ICF) edges is fundamental to binary security analysis, yet existing methods struggle with long-range dependencies, isolate different ICF types, and are often evaluated under protocols vulnerable to label noise and data leakage. We present ICFlowNet, a unified framework for long-range ICF prediction in stripped binaries. ICFlowNet introduces candidate-aware Dual Virtual Hubs, a Global Code Hub and a Global Data Hub, to create short routing paths between distant code and data evidence, and combines them with multi-task graph learning to jointly model indirect calls, indirect tail calls, jump tables, and returns. To enable credible evaluation, we further develop a leakage-aware, noise-controlled pipeline with package-level splits, function-level mnemonic-hash deduplication, and a clean test protocol built from dynamic positives and absolute negatives. Using this pipeline, we construct a dataset of 15,901 unique stripped x86-64 binaries, including 1,351 with dynamic ground truth. Experiments show that simply scaling static supervision yields only marginal gains, whereas our structural and multi-task designs are essential: Dual Virtual Hubs improve long-range F1 by up to 9.13 points, multi-task learning adds up to 5.81 points, and the final model outperforms prior baselines by more than 13 F1 points on long-range indirect calls while adding only 11.44 percent topological overhead.

---


### 43. [PACE: Towards Surfacing Hidden Conflicts in User Requests](https://arxiv.org/abs/2609.03293)

**<font color=#1a73e8>作者：</font>** Yoojin Kim, Jihyoung Jang, Hyounghun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized assistants should not only comply with user requests but also assess whether those requests are appropriate given the user's current circumstances. However, prior work has primarily focused on accurately executing requests, overlooking the need for assistants to account for context and engage in conflict-based refusal. Furthermore, while existing work on conflict or safety detection relies on explicitly provided factors, real-world scenarios often involve implicit factors that must be retrieved from a knowledge base (KB). To this end, we introduce Personalized Assistants for Conflict Evaluation (PACE), a dataset for evaluating whether models can identify latent constraints, expressed as egocentric knowledge or events, that render seemingly reasonable user requests inappropriate. PACE pairs user requests grounded in well-defined personas with egocentric KB facts, requiring models to integrate contextual evidence to determine whether a request is conflicting. This implicit retrieval setting hinders the direct association between user requests and conflict-inducing knowledge, making it difficult for existing models to identify relevant user-specific facts. To address this challenge, we further propose PaceMaker, a multi-agent framework in which specialized agents coordinate across query reformulation, multi-hop graph traversal, and conflict-aware filtering to retrieve contextually decisive evidence. Experiments on PACE evaluate both evidence retrieval quality and conflict decision accuracy, showing that PaceMaker consistently outperforms existing approaches.

---


### 44. [Latent Energy Action Planning with World Models](https://arxiv.org/abs/2609.03294)

**<font color=#1a73e8>作者：</font>** Phu Pham, Aniket Bera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models support efficient model predictive control from high-dimensional observations, yet optimizing a single learned latent objective can favor action sequences whose decoder-predicted terminal descriptor does not match the goal descriptor. We introduce Latent Energy Action Planning (LEAP), which treats the complete action horizon as a differentiable variable and optimizes it through a frozen LeWorldModel (LeWM). LEAP couples terminal latent goal matching with a terminal-window state energy. Low energy requires the predicted terminal latent to agree with the goal latent and the decoder-predicted terminal descriptor to agree with the goal descriptor. A frozen goal-conditioned proposal initializes the search, a quasi-Newton solver refines actions through the autoregressive rollout, and post-optimization projection enforces the admissible action range. Across four control domains using the officially released LeWM checkpoints, the complete LEAP planning system raises mean success from 77.5% for LeWM planned with the cross-entropy method (LeWM+CEM) to 94.8% under a matched protocol, a 17.3-percentage-point improvement, while retaining the frozen LeWM representation and predictor.

---


### 45. [Code Black: Desktop-Mediated Co-Design of AR-HMD Microinteractions for Emergency Department Teamwork](https://arxiv.org/abs/2609.03295)

**<font color=#1a73e8>作者：</font>** Jonathan Segal, Jalynn Nicoly, Francisco Ortega 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Emergency Department (ED) teams coordinate shifting roles, medication decisions, and time-critical interventions under uncertainty. Augmented reality head-mounted displays (AR-HMDs) have shown potential to spatially anchor information during care, creating opportunities to examine how spatial interfaces might support teamwork. We conducted a speculative co-design study with 12 healthcare workers (HCWs) using an editable, desktop-mediated Unity-based 3D design probe to visualize and refine work-as-imagined AR-HMD interfaces for role-based notifications, task-specific timers, and dosage verification. Guided by microinteraction rules, participants identified future spatial user interfaces (SUI) requirements such as how they appear, update, or are dismissed in relation to clinical practice, safety concerns, and existing tools. Five returning participants and 26 additional HCWs subsequently provided follow-up feedback on derived visual interface alternatives. Findings show that desktop-mediated spatial co-design elicited formative specifications for role visibility, task-linked timing, and verification-oriented dosage assistance, while revealing tensions involving clutter, shared awareness, communication, privacy, and reliability. Rather than evaluating a functional AR-HMD system or team-based clinical performance, this study contributes the Speculative Co-Design Framework for AR-HMD Teamwork (SCF-HMD) and a visual design catalog for translating expert critique of work-as-imagined (WAI) concepts into situated goals for future AR-HMD systems.

---


### 46. [Tensor-based Brain Surface Modeling and Analysis](https://arxiv.org/abs/2609.03302)

**<font color=#1a73e8>作者：</font>** Moo K. Chung, Keith J. Worsley, Steve Robbins 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a unified computational approach to tensor-based morphometry in detecting the brain surface shape differences between two clinical groups based on magnetic resonance images. Our approach is novel in a sense that we combined surface modeling, surface data smoothing and statistical analysis in a coherent unified mathematical framework. The cerebral cortex has the topology of a 2D highly convoluted sheet. Between two different clinical groups, the local surface area and curvature of the cortex may differ. It is highly likely that such surface shape differences are not uniform over the whole cortex. By computing how such surface metrics differ, the regions of the most rapid structural differences can be localized. To increase the signal to noise ratio, diffusion smoothing based on the explicit estimation of Laplace-Beltrami operator has been developed and applied to the surface metrics. As an illustration, we demonstrate how this new tensor-based surface morphometry can be applied in localizing the cortical regions of the gray matter tissue growth and loss in the brain images longitudinally collected in the group of children.

---


### 47. [Geometry-Aware Graph Construction via Adaptive Spectral Bandwidth Control](https://arxiv.org/abs/2609.03306)

**<font color=#1a73e8>作者：</font>** Ecem Bozkurt, Antonio Ortega  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernelized graph methods - spectral clustering, diffusion maps, and sparse kernel -regression graphs - that use Gaussian kernels depend on the choice of Gaussian bandwidth sigma, which governs the spectral character of the local kernel operator. When sigma is too small, the kernel overestimates local complexity and treats each sample as an independent direction; when sigma is too large, the kernel collapses multiple directions together, the condition number diverges, and all geometric discrimination is lost. We propose a choice of scale to make the spectral complexity of the kernel consistent with the intrinsic complexity of the underlying manifold. We propose a per-node bandwidth criterion that operationalizes this principle by jointly matching the kernel's effective rank to the local intrinsic dimension estimated via minimum spanning tree, anchoring the search in the manifold-consistent log-log scaling regime. We evaluate SSL embeddings from six encoders on CIFAR-100, showing that adaptive bandwidth consistently improves leave-one-out (LOO) classification and label propagation (LP) accuracy over fixed-bandwidth methods and competing adaptive methods.

---


### 48. [Risk and Anomaly Identification for Distribution Network Optimal Operation Based on Reinforcement Learning and Uncertainty Quantification](https://arxiv.org/abs/2609.03308)

**<font color=#1a73e8>作者：</font>** Ziqi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable operation of modern distribution networks requires timely identification of operational risks and anomalous events under pervasive uncertainty. In practice, operators must identify risks that are inherent in stochastic yet in-distribution conditions, and anomalies that correspond to out-of-distribution behaviors such as unusual load patterns, extreme weather or cyber-physical attacks. This paper addresses this joint risk and anomaly identification problem for optimal distribution network operation and proposes a deep reinforcement learning framework that is explicitly uncertainty aware. We integrate distributional and Bayesian deep reinforcement learning to realize a second- order uncertainty quantification scheme that decomposes total uncertainty into aleatoric and epistemic components, which are respectively used to characterize inherent risk and out-of- distribution anomalies. The resulting epistemic estimates drive both exploration during training and out-of-distribution detec- tion with fallback control during deployment, whereas aleatoric estimates are used to characterize intrinsic operational risk. Simulation results demonstrate the performance of our DRL agent and the effectiveness of the uncertainty quantification.

---


### 49. [Laplacian Frequency Hierarchies for Efficient 3D Gaussian Splatting Training](https://arxiv.org/abs/2609.03334)

**<font color=#1a73e8>作者：</font>** Yixiong Yang, Sisheng Zhang, Qingsong Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A key bottleneck in 3D Gaussian Splatting training is the continual growth of Gaussian primitives, which increases optimization cost and slows convergence, especially at high resolutions. We propose Laplacian Frequency Hierarchies, a simple yet efficient 3DGS scheme that combines Laplacian image decomposition with coarse-to-fine, frequency-staged training. After fitting lower-frequency structure, we archive the corresponding Gaussian field so that subsequent fields can optimize higher-frequency residuals without carrying the full primitive burden, and we compose the rendered components in the image domain via a Laplacian-style reconstruction at inference time. This design reduces the number of active Gaussians during training, thereby lowering optimization overhead and accelerating training. The proposed scheme is plug-and-play and orthogonal to prior 3DGS accelerations: it can be directly combined with strong backbones such as Taming-3DGS and FastGS to improve training speed with competitive reconstruction quality. It achieves average speedups of 1.73x and 1.21x at 1K setting, and 1.74x and 1.33x at 4K setting on Taming-3DGS and FastGS, with larger gains on more challenging scenes and increasingly pronounced benefits at higher resolutions.

---


### 50. [A Large Open Multi-Energy Corpus of Soil Compaction Tests, with Machine-Learning Baselines](https://arxiv.org/abs/2609.03337)

**<font color=#1a73e8>作者：</font>** Sompote Youwai, Chana Phutthananon, Warat Kongkitkul  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every engineered fill is specified by a maximum dry density and an optimum moisture content. Each determination needs a full Proctor test. Published correlations rest on one to four hundred specimens, usually from one laboratory at one compactive energy, and are seldom released. This paper releases a corpus without those limits. It holds 2,854 laboratory compaction tests from six public sources, across 162 provenance groups and four Proctor energy levels, with fines from 1.5 to 100%. Every record is audited to the Proctor method its source names, and no energy is inferred. Screening on the zero-air-voids condition removed 11.8% of harmonised records, and 5.7% of those with a measured specific gravity. A material share of published compaction data is physically impossible. The optimum degree of saturation over the corpus is 0.815 at a coefficient of variation of 11%. That is a baseline, not a constant. Both parameters are then estimated from one classification suite and the compaction standard. A tabular foundation model reaches R2 0.824 for density and 0.784 for water content under random folds. It reaches 0.727 and 0.696 with folds drawn around provenance, and 0.520 and 0.614 with a whole source held out. Compactive energy is negligible marginally yet decisive conditionally. Density on the 66 modified-Proctor records is predicted at R2 0.740 with it and -0.651 without. Symbolic regression yields closed forms coupled through a phase relation. No predicted pair can then exceed the zero-air-voids line. The predictions are for screening, not acceptance.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-194](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
