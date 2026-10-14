# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 201. [Random Feature Pruning for Multi-Class Classification](https://arxiv.org/abs/2610.15101)

**<font color=#1a73e8>作者：</font>** Mohammad Amin Omidi, Babak Seyfe, Shahrokh Valaee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weighted sums of random kitchen sinks (W-RKS) is a commonly used feature extraction technique for supervised learning tasks. A major drawback of this method is the redundancy and ineffectiveness of many extracted random features. This paper investigates efficient methods for reducing such redundancy in multi-class classification problems. We specifically formulate feature selection as a variant of the sequentially nested model selection problem and introduce the Successive Empirical Excess Risk Difference Maximization (SEED-MAX) algorithm. It recursively computes empirical risks to identify the most parsimonious yet informative set of features. We derive an analytical lower bound for the probability of correct feature selection by the SEED-MAX algorithm. This lower bound on the probability of correct feature selection can be made arbitrarily close to one by increasing the training dataset size. To further enhance the rate of pruning, we evaluate the features retained by SEED-MAX using the Fisher test (F-Test). Empirical evaluations on UCR time-series classification datasets show that the sequential application of SEED-MAX with the Fisher test achieves approximately 92 percent rate of pruning with negligible degradation in classification accuracy. Implementations of the SEED-MAX and SEED-MAX-F-Test methods are available at this https URL.

---


### 202. [RELAGRAM: Recursive Latent Graph Model for the Capacitated Vehicle Routing Problem](https://arxiv.org/abs/2610.15106)

**<font color=#1a73e8>作者：</font>** Vladimir Kirill Bickov, Neil Yorke-Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent recursion repeatedly processes internal representations through the same neural network. Recent work has shown this approach to be effective on structured reasoning tasks such as Sudoku and maze solving. However, whether latent recursion can support neural routing remains unclear. We introduce RELAGRAM (Recursive Latent Graph Model), a novel approach that brings latent recursion to graph combinatorial optimization. RELAGRAM encodes a capacitated vehicle routing problem (CVRP) instance as edge tokens; a compact transformer recurrently updates the latent representations of these tokens. An output head maps the answer state to an edge heatmap, from which an autoregressive decoder constructs a feasible solution. On CVRP-100 instances, the 0.53M-parameter RELAGRAM achieves gaps to a PyVRP reference of 13.4%, 9.8%, and 8.3% under greedy decoding, eightfold symmetry augmentation, and 256-candidate search, respectively. Trained only on CVRP-100, RELAGRAM generalizes zero-shot to CVRP-500 and CVRP-1000, achieving gaps of 15.6% and 21.7% under 256-candidate search. Together, these results demonstrate that latent recursion is a promising approach to neural routing.

---


### 203. [scHFBiMamba: a bidirectional Mamba autoencoder for cardiac disease-state classification from single-nucleus RNA-seq data](https://arxiv.org/abs/2610.15117)

**<font color=#1a73e8>作者：</font>** Ugo Lomoio, Pietro Hiram Guzzi, Pierangelo Veltri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To evaluate whether a compact bidirectional state-space autoencoder improves joint classification of species, cell type, and disease state from single-nucleus RNA-sequencing profiles in heart failure (HF), while yielding interpretable gene attributions. Building on the dense denoising autoencoder (DAE) and MLP framework of Ruz Jurado et al., we developed scHFBiMamba, combining a bidirectional Mamba autoencoder (BiMambaAE) with an MLP head. BiMambaAE maps 16,545-gene profiles to 350-dimensional latent representations using 13.2M parameters, about 14.6-fold fewer than the dense DAE (192.9M). We compared six encoder-classifier configurations on 38,275 held-out cardiac nuclei using McNemar tests with Benjamini-Hochberg correction, and assessed nine classifiers on frozen representations. Biological relevance was evaluated by comparing SHAP-derived differentially explained genes with differentially expressed genes against curated HF-related Gene Ontology keywords. BiMambaAE+MLP achieved the highest aggregate F1: pooled macro-F1 across 13 outputs was 0.966 versus 0.957 for DAE+MLP, and the mean category macro-F1 was 0.977 versus 0.970. It significantly improved cell-type and disease-state accuracy (adjusted p=7.1e-3 and p=4.8e-6, respectively), with species F1 of 1.000. SHAP-derived differentially explained genes achieved a pathway-enrichment benchmark F1 of 0.105 versus 0.053 for differentially expressed genes. Compact bidirectional state-space autoencoders can outperform substantially larger dense autoencoders for joint cardiac transcriptomic classification while reducing parameters. scHFBiMamba enables accurate multi-task prediction and hypothesis-generating gene-level interpretation. Code: this https URL.

---


### 204. [ShellElastic: Scalable Elastic Pretraining with Simultaneous Maximal Updates and Hyperparameter Transfer](https://arxiv.org/abs/2610.15124)

**<font color=#1a73e8>作者：</font>** Can Jin, Yan Kang, Yifan Gong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models need to support diverse inference budgets, yet training a separate model for each budget duplicates pretraining effort. Elastic models train several nested sub-networks inside one weight-shared supernet, but existing recipes face three obstacles: variable per-step workloads that hinder distributed scaling, limited hyperparameter (HP) transfer across model sizes, and no guarantee that all sub-networks are maximally updated at once. We present \Ours, an elastic transformer that organizes hidden dimensions into a dense core and successive shells, so that every hidden matrix is block lower triangular. One full-width forward pass contains every sub-network's exact hidden states as prefixes, so joint training keeps a fixed computation graph and costs about as much per step as training the widest sub-network alone. We further introduce \muE, an extension of maximal update parameterization (\mup) to \Ours and other elastic architectures. Its scaling rules provably keep all sub-networks of a supernet maximally updated simultaneously (\muI), and keep doing so when the supernet is widened or given more shells; sweeps confirm that HPs tuned on a small non-elastic proxy stay near-optimal for elastic families and larger supernets (\mbox{\muT}). A single \Ours run produces sub-networks that outperform MatFormer and fully elastic baselines at matched parameter counts, and approach separately trained models that together take several times the steps.

---


### 205. [RIECNN: Real-Time Image Enhanced CNN for Traffic Sign Recognition](https://arxiv.org/abs/2610.15127)

**<font color=#1a73e8>作者：</font>** Reem Abdel-Salam, Rana Mostafa, Ahmed H. Abdel-Gawad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic sign recognition plays a crucial role in the development of autonomous cars to reduce the accident rate and promote road safety. It has been a necessity to address traffic signs that are affected significantly by the environment as well as poor real-time performance for deep-learning state-of-the-art algorithms. In this paper, we introduce Real-Time Image Enhanced CNN ({\our}) for Traffic Sign Recognition. {\our} is a real-time, novel approach that tackles multiple, diverse traffic sign datasets, and out-performs the state-of-the-art architectures in terms of recognition rate and execution time. Experiments are conducted using the German Traffic Sign Benchmark (GTSRB), the Belgium Traffic Sign Classification (BTSC), and the Croatian Traffic Sign (rMASTIF) benchmark. Experimental results show that our approach has achieved the highest recognition rate for all Benchmarks, achieving a recognition accuracy of 99.75\% for GTSRB, 99.25\% for BTSC and 99.55\% for rMASTIF. In terms of latency and meeting the real-time constraint, the pre-processing time and inference time together do not exceed 1.3 ms per image. Not only have our proposed approach achieved remarkably high accuracy with real-time performance, but it also demonstrated robustness against traffic sign recognition challenges such as brightness and contrast variations in the environment.

---


### 206. [Trust Hinders Bidirectional Human-AI Alignment](https://arxiv.org/abs/2610.15136)

**<font color=#1a73e8>作者：</font>** Michaela Benk, Kacper Sokol  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trust calibration remains the dominant framing of AI-assisted decision making: the goal is to close the gap between perceived and actual trustworthiness of AI systems so that users exhibit appropriate reliance on them. We argue that this approach, while useful for decision problems that are well-defined and clearly scoped, overly restricts what it means to make a decision with AI support. To overcome this limitation, we develop three dimensions of AI-assisted decision making. First, trusting AI is only one of several possible strategies for managing uncertainty. Second, trust calibration is often misapplied when AI models "large-world" decision problems, i.e., ill-defined situations where goals and states are only partially known or unknowable. Third, in such settings human-AI alignment requires addressing higher-order decision processes. We conclude by reflecting on the implications of our observations on the design of process-oriented human-AI coupled systems that jointly identify and negotiate uncertainty throughout the decision-making task.

---


### 207. [The Agent Clicks Approve: Injected Page Text Makes Browser Agents Authorize Access the Task Never Named](https://arxiv.org/abs/2610.15138)

**<font color=#1a73e8>作者：</font>** Md Imran Hossen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A browser agent that works in its user's signed-in session can be steered by a two-sentence note on a page it reads into approving a third party's access to the user's account. The agent is a confused deputy: the session supplies the authority, the page designates the access request to approve or the webhook URL to register, and nothing at the point of action checks one against the other. The agent thereby supplies the approval click that a consent screen reserves for the account holder. We measure this failure on two authorization surfaces, an OAuth-style access grant and a webhook registration, with agents built on an open-source browser framework and models from two providers. Without a defense the unauthorized action completed in all 73 attack runs. An instruction telling the model that only the user's task authorizes a grant still left 7 of 10 consent attacks completing. We therefore move the check to where the action completes. The authority envelope gate has the service accept a request only when it matches the task's envelope, the client and account or the webhook URL that the user's task named, fixed before the agent starts. With the gate the agent still sent the request in every one of 70 attack runs, the service rejected each, and the action completed in every control run whose task named it. A service that receives the task's envelope should therefore check agent-driven authorization requests against it.

---


### 208. [Single-step Retrosynthesis via Reinforcement Learning from Forward Feedback](https://arxiv.org/abs/2610.15141)

**<font color=#1a73e8>作者：</font>** Zixun Lan, Zhenfu Liu, Yi Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Single-step retrosynthesis is a one-to-many inverse problem, yet most models are trained and evaluated against a single recorded reactant set. Reference-based training gives no explicit positive signal for unrecorded alternatives, and exact-match evaluation rejects non-matching predictions regardless of chemical plausibility. We propose Retrosynthesis via Reinforcement Learning from Forward Feedback (RetroRLFF), which optimizes reactant generation using both reference agreement and forward consistency with the target product. Starting from a supervised decoder-only Transformer, RetroRLFF generates complete reactant candidates and uses a frozen forward reaction model to predict products. A sequence-level reward combines reference agreement and forward consistency while penalizing invalid outputs. Direct Advantage-Based Policy Optimization updates the policy without human preference annotations or a preference-trained reward model. On USPTO-50K, RetroRLFF outperforms all 14 baselines in candidate-level round-trip accuracy at k = 1, 3, 5, and 10. With approximately 50 million parameters, it achieves 90.1% top-1 round-trip accuracy, exceeding R-SMILES, the strongest competing baseline on this metric, by 8.5 percentage points. Compared with its supervised policy, round-trip accuracy increases from 83.1% to 90.1%, while exact-match accuracy is maintained at 57.9% versus 57.5%. In an anonymized expert assessment of 131 randomly selected test cases, organic synthesis experts prefer RetroRLFF over EditRetro in 67.9% of comparisons. These results support forward feedback as a training signal for improving forward consistency while retaining top-1 reference recovery. Expert assessment provides complementary evidence of synthetic feasibility on the selected cases, although neither forward consistency nor expert preference establishes experimental feasibility.

---


### 209. [Sensor-Aware Joint Data Fusion and State Estimation under Sparse Multi-rate Distribution Grid Sensing](https://arxiv.org/abs/2610.15156)

**<font color=#1a73e8>作者：</font>** Pooja Algikar, Stefano Fenu, Kumarsinh Jhala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distribution-system state estimation is a growing necessity for the modern power grid as the addition of local storage and generation add system complexity that an operator or aggregator is not able to directly monitor. Classical methods work well when all system elements are time-synchronized and at least partly observable, but multi-rate monitoring of sparse heterogeneous sensors typically relies on machine learning approaches. It is a common practice in the literature to structure this task as a two-stage pipeline, first fusing data from disparate sensors and then feeding the fused pseudo-measurements to a separately trained state estimator. We propose a heterogeneous latent graph ODE in which measurement functions and sampling processes are typed and localized on specific buses, paired with a graph- transformer state estimator solving DSSE specifically for multi-rate heterogeneous sensor placements, and demonstrate its effectiveness across multiple IEEE standard topologies as observability degrades.

---


### 210. [Learning Proposition-Level Links from Sentence-Level Supervision for Neuro-Symbolic NLI](https://arxiv.org/abs/2610.15158)

**<font color=#1a73e8>作者：</font>** Xuyao Feng, Antonis Bikakis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study neuro-symbolic natural language inference (NLI) with independently translated propositional representations of the premise and hypothesis. Before symbolic reasoning, the system must infer semantic links between their proposition-level units (atoms). Existing systems based on Abstract Meaning Representation (AMR) and Boolean satisfiability (SAT) identify these links using fixed embedding-based source selection and pretrained sentence-level NLI models not trained for atom-level linking. We introduce a trainable atom linker that jointly predicts link existence, source selection, and relation type. Without atom-pair training annotations, we treat cross-formula link structures as latent and train the linker from sentence-level NLI labels, keeping the translator and SAT reasoner fixed. We evaluate on the full public test splits of Stanford Natural Language Inference (SNLI) and Sentences Involving Compositional Knowledge (SICK), and the matched and mismatched validation splits of Multi-Genre Natural Language Inference (MNLI). Our system improves accuracy by 11.40-27.09 percentage points over a baseline applying sentence-trained NLI models unchanged to atom pairs within the same SAT pipeline. It also improves over the prior fixed-linker AMR-to-SAT system by 8.14-26.32 percentage points on SNLI and both MNLI splits, with a smaller gain on SICK.

---


### 211. [TRIG: Toward Measuring Texture Realism in Image Generation](https://arxiv.org/abs/2610.15164)

**<font color=#1a73e8>作者：</font>** Zhiwei Xu, Jiali Cui, Zhiqiang Lao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper studies the backbone used by metrics for evaluating the quality of generated images. Although generative models have advanced rapidly, some outputs still exhibit unrealistic texture characteristics, and these differences are difficult to measure. Widely used evaluation metrics provide limited insight into texture realism, since they often rely on a backbone trained for another objective, such as image classification or image-text alignment. Such objectives typically encourage invariance to low-level variations that carry texture, so the resulting features primarily encode semantic and global structure. As a result, texture-specific discrepancies may not be explicitly captured. We propose TRIG, a metric directed at the texture realism of generated images. Its backbone is instead the discriminator of a generative adversarial network pre-trained on a texture dataset, which provides a learned prior for the local statistics of natural textures. A plausibility head is fine-tuned to identify local texture degradations, while preserving natural defocus and sensor noise as positive cases. On the features of this backbone, we compute a standard distributional distance between a reference set of real images and a set of generated ones. We apply TRIG to several generative models and observe closer agreement with human realness ratings than baseline metrics.

---


### 212. [Active Learning for Finding a Needle in a Haystack](https://arxiv.org/abs/2610.15165)

**<font color=#1a73e8>作者：</font>** Emily Silcock, Simon Löwe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training a classifier to find a rare class of documents, such as hate speech directed at a particular religious group, requires labelled examples that are expensive to obtain when the class makes up only a small fraction of a corpus. Active learning reduces this cost, but it must start from an initial labelled set that contains examples of the target class. Random sampling cannot supply these at reasonable cost, so they must be selected in some other way, such as keyword search, and any such selection biases the initial set towards part of the target class. We evaluate whether active learning can correct this bias. On AG News and Measuring Hate Speech, at a prevalence of around 1%, we compare random sampling with eight active learning strategies, starting from initial sets that cover or omit known subgroups of the target class, and measure recall on the omitted subgroups as well as F1. On AG News, almost every strategy recovers the omitted subgroup. On Measuring Hate Speech, uncertainty-based strategies recover less of the omitted subgroups than random sampling, whereas discriminative active learning recovers 55% of them without a significant loss of F1. Aggregate metrics conceal these differences.

---


### 213. [LexiCan: Lexicographic Canonicalization of Point Clouds for Machine Learning Applications](https://arxiv.org/abs/2610.15171)

**<font color=#1a73e8>作者：</font>** Daniel Sanchez, Djordje Mihajlovic, Federica Valeau 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Canonicalization resolves the rotational and permutation ambiguity of 3D point clouds by selecting a unique orbit representative, maintaining their geometric information while allowing standard architectures, such as Transformers, to operate on them. Existing canonicalizations, however, exhibit discontinuity jumps on molecular configurations and non-trivial invariance errors in popular molecular datasets, which lead to ambiguity in their representation. To bridge this gap, we introduce LexiCan, a canonicalization that is provably invariant under either $O(3)$ or $SO(3)$, empirically invariant to rotations to within $\sim 10^{-6}$ angstroms on the QM9 and QM-sym molecular datasets, and mitigates discontinuity jumps on QM-sym, while running orders of magnitude faster than an existing canonicalization. Finally, non-invariant models perform better on QM9 property prediction and ModelNet40 shape classification with LexiCan than with that canonicalization.

---


### 214. [Game-Theoretic Reinforcement Learning based Topology-Agnostic Defense for Virtual Power Plants](https://arxiv.org/abs/2610.15183)

**<font color=#1a73e8>作者：</font>** Pooja Algikar, Stefano Fenu, Kumarsinh Jhala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of distributed energy resources (DERs) aggregated by virtual power plants (VPPs) elevates cybersecurity risk by expanding the attack surface. A coordinated cyberattack has the potential to disrupt distribution-system, bulk-system, and market operations. Existing cyberphysical defense strategies largely assume access to grid network models and operating conditions, which may not be available to third-party aggregators. This paper proposes a novel hybrid, perturbation-based cyber-physical defense for VPP-operated DERs that blends game-theoretic planning with model-free reinforcement learning (RL) under a Bayesian belief-update framework. Topology agnosticism is defined from the VPP information and implementation perspective: the VPP does not require access to the feeder topology, line parameters, switching configuration, or full system state. This work advances the state of the art through three contributions: (1) a multi-output Gaussian process with Hamiltonian Monte Carlo for discrete attacker-type inference, probability of detection, and confidence of detection for modeling the belief distribution; (2) moment-matched Gaussian propagation of posterior beliefs across episodes; and (3) an RL policy that adaptively integrates Stackelberg leader (VPP) actions with exploration. Furthermore, we establish equilibrium existence and derive an episode-level closed-loop utility bound connecting attacker-belief uncertainty with GT-RL action alignment. Evaluations on IEEE 13- and 123-Bus feeders with DER portfolios demonstrate effective detection under attacker-model uncertainty and evaluated feeder re-configuration conditions, while requiring no explicit feeder-topology knowledge. Overall, the results indicate that combining bi-level game-theoretic planning, nonparametric Bayesian inference, and adaptive RL is a promising direction for VPP cybersecurity.

---


### 215. [On the Effectiveness of NetFlow-Based Deanonymization of Tor Onion Services (Extended Version)](https://arxiv.org/abs/2610.15198)

**<font color=#1a73e8>作者：</font>** Jinseo Lee, Jongkook Han, Yixin Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the context of Tor, deanonymization attacks via traffic correlation have long been studied for both clients and onion services. Complementing prior investigations that utilize fine-grained flow metadata such as packet sizes and timings, we study a relatively less explored yet easier-to-obtain adversarial capability: deanonymization using only coarse NetFlow-style telemetry, such as one-minute, 1-out-of-1,000 sampled packet counts. We first revisit active NetFlow-based traffic analysis attacks against Tor onion services and show, through large-scale experiments with live Tor data, that coarse telemetry is sufficient to deanonymize a targeted onion service when the adversary can induce discernible traffic patterns through controlled downloads. We then introduce a stronger active attack based on controlled introduction requests, which removes application-specific assumptions and gives adversaries more flexibility while achieving comparable success rates. Finally, we present a passive deanonymization attack that sends zero traffic to target onion services. The attack exploits Tor's puzzle-based DoS defense as a side channel: public puzzle difficulty reveals service-load changes that can be semantically matched against NetFlow traces. Our findings show that coarse network telemetry poses a practical deanonymization threat to onion services today and call for proactive mitigations and a redesign of the globally visible defense signals that may leak service-load information.

---


### 216. [HarnessNet: Feedback-driven Hierarchical Joint Harness Evolution for Multi-agent Systems](https://arxiv.org/abs/2610.15221)

**<font color=#1a73e8>作者：</font>** Zhaoyuan Qiu, Sachith Seneviratne, Yu Xia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can evolve by using environment feedback to revise their harnesses, the software managing model inputs, tool use, memory, and execution, while keeping foundation models frozen. Existing studies focus on single agents, leaving joint harness evolution in multi-agent systems (MAS) underexplored. A single global optimizer faces growing context and workload as the system scales, while access restrictions may prevent sharing agent internals or system-wide feedback. We propose HarnessNet, a framework for hierarchical harness evolution in MAS. Its basic unit, Agentron, comprises an evolvable forward harness, a foundation model, and a local optimizer that can observe and modify only that harness. Agentrons form a layered graph through which environment feedback propagates backward, with upstream optimizers receiving node-specific feedback from the downstream layer. This decomposes joint harness evolution into smaller, coordinated tasks with separate contexts, reducing individual optimizers' context and workload while keeping access local. Optimizers need not access all agent trajectories or raw environment feedback. Experiments on AgentBench with multiple foundation models demonstrate the feasibility of training HarnessNet. Compared with a single global optimizer, HarnessNet achieves comparable performance gains while respecting local privacy and requiring fewer tokens and less time per optimizer call. A migration study shows that the evolved harnesses remain jointly effective after replacing the foundation models, suggesting transferability across models.

---


### 217. [Correlation-Aware Reconstruction for Multivariate Time Series Anomaly Detection](https://arxiv.org/abs/2610.15250)

**<font color=#1a73e8>作者：</font>** Md. Johir Raihan, Zahra Zamanzadeh Darban, Yueyang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstruction-based detectors for multivariate time series anomaly detection typically learn a single entangled representation of normal behavior and flag anomalies based on reconstruction error. However, real-world anomalies are not only isolated spikes in a single channel but also disruptions in the relationships between channels, where each sensor individually appears normal, but their joint behavior deviates from the norm. Because these models compress both temporal evolution and inter-channel structure into this single space, they lack an explicit mechanism to isolate such inter-channel dependencies from normal temporal dependencies, leading to lower detection rates for cross-channel anomalies. We propose CARMA (Correlation-Aware Reconstruction for Multivariate Time Series Anomaly Detection), which is a reconstruction-based variational autoencoder with two complementary latent spaces: a temporal latent that captures sequential dynamics, and a correlation latent that is trained to reconstruct the window's pairwise Pearson correlations. Both representations are fused in the signal decoder, and anomalies are detected from the reconstruction error. We evaluate CARMA on the TSB-AD-M benchmark suite (17 datasets, 180 series) against 29 baseline methods, and show that it significantly outperforms all of them across multiple threshold-free and range-aware metrics, achieving a VUS-PR of 0.4929. Ablations show that removing the correlation branch degrades performance, that adding a second latent without supervision recovers only part of the gain, and that supervising the correlation latent with an explicit correlation target accounts for the rest and produces a sharper error response at anomalies.

---


### 218. [Do Rollups Self-Organize? Multi-Agent Reinforcement Learning in the EIP-4844 Blob Fee Market](https://arxiv.org/abs/2610.15256)

**<font color=#1a73e8>作者：</font>** Alessio Brini  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> EIP-4844 gave Ethereum rollups a separate fee dimension for data, governed by a multiplicative update rule that targets three ``blobs'' per block. Whether this target is reached depends on how many independent, self-interested rollups choose to post data, a question that closed-form models address only for a single agent under exogenous prices or in a static equilibrium. We propose a calibrated multi-agent reinforcement learning environment for the blob fee market in which the blob base fee is endogenous, set by the EIP-4844 rule on the aggregated decisions of heterogeneous rollups fit to post-Dencun Ethereum data. After confirming that the environment reproduces the known single-agent analytical optimum, we show that independent learners, with no convergence guarantee, still settle near the target without coordination ($3.32\pm0.01$ blobs per block over five seeds). Over a fiftyfold demand range ($10\times$ to $500\times$), supply stays at the target from $10\times$ to $200\times$ and rises above it at higher demand, where the fee can no longer hold it. Posting frequency increases with rollup size, an emergent analog of the size threshold predicted by prior theory. A costless layer-1 calldata outside option pushes the fee down by roughly an order of magnitude while aggregate supply stays at the target, so the fee rule acts as a negative-feedback controller on decentralized supply.

---


### 219. [Asymptotics of Random-Lattice Enumeration: Beyond HKZ via Dense Sublattices](https://arxiv.org/abs/2610.15265)

**<font color=#1a73e8>作者：</font>** Thijs Laarhoven  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> To bridge the gap between worst-case and heuristic analyses of lattice enumeration, we study the sizes of (unpruned) enumeration trees on $n$-dimensional Haar-random lattices. Writing $n^{cn+o(n)}$ for the tree size at the shortest vector radius, we investigate the asymptotic scaling of $c$, and which bases minimize it.
For quasi-HKZ bases, we rigorously analyze the random-lattice HKZ geometry and establish $c=1/(2e)\approx 0.1839$. This matches the worst-case enumeration exponent of Hanrot-Stehlé and confirms earlier predictions for the geometry of HKZ bases on random lattices.
Searching beyond quasi-HKZ bases, we prove that with high probability, the minimum achievable tree size exponent $c$ over all bases of a random lattice satisfies: \begin{align} 0.1464 \approx \frac{2-\sqrt{2}}{4}\leq c<0.1474. \end{align}
For the lower bound, we use Kim's mean-value formula for nested chains of primitive sublattices to rule out bases with small prefix determinants. This strengthens the earlier Rankin-based heuristic lower bound exponent $c \geq 1/8$, discussed by Nguyen and Hanrot-Stehlé, and rules out the existence of random-lattice bases with trees as small as predicted by the geometric series assumption.
For the upper bound, we show that with high probability a dense primitive half-rank sublattice exists with determinant at most $n^{n/8 + o(n)}$. Combining dual HKZ on this sublattice with HKZ on its quotient gives a basis with $c \leq 1/(4\sqrt{e}) \approx 0.1516$. Recursively splitting each half lowers the upper bound below $0.1474$, and under a natural heuristic assumption we prove that the lower bound is tight.
Combined with the collision search of Feng-Gao-Liu, our two-block construction gives a polynomial-space algorithm solving the closest vector problem with preprocessing (CVPP) on random lattices in query time $n^{0.0892 n + o(n)}$ for arbitrary targets.

---


### 220. [LeHami: Symplectic Latent Dynamics for World Models](https://arxiv.org/abs/2610.15267)

**<font color=#1a73e8>作者：</font>** Romina Yalovetzky, Randall Balestriero, Yann LeCun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures (JEPAs) learn world models directly in latent space, but unconstrained autoregressive predictors may contract the latent distribution over long rollouts. We introduce Symplectic Hamiltonian JEPA (LeHami), which replaces the standard predictor with an action-conditioned Hamiltonian flow over a structured latent state (q, p) integrated using an exactly symplectic leapfrog step. This construction preserves phase-space volume at every rollout step and rules out uniform contraction, asymptotically stable fixed points, and merging of distinct latent states, independently of the learned parameters or action sequence. We obtain the momentum-like component from temporal derivatives of the learned position-like representation, providing an explicit second-order state for prediction and control. On conservative and actuated visual pendulum environments, LeHami substantially improves long-horizon velocity prediction over an unconstrained JEPA world model and empirically maintains constant latent volume where the baseline contracts. The learned flow also supports accurate integration at unseen sub-frame step sizes and numerical time reversal. These results show how geometric structure can provide inference-time guarantees that are complementary to representation regularization in latent world models.

---


### 221. [GeoBridge: Evolving Transferable Decoder Topologies for Geometric Vision](https://arxiv.org/abs/2610.15280)

**<font color=#1a73e8>作者：</font>** Rui Wang, Haoyu Zhang, Ran Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depth estimation and Gaussian reconstruction share a need for multi-scale feature processing, yet use different prediction interfaces and training objectives. Whether a decoder's internal computation can be optimized once and reused across these systems remains a structural design question. Search over primitive configurations alone leaves the organization of transformations fixed. To address this gap, we propose GeoBridge, an evolutionary framework for transferable decoder topologies. First, GeoBridge makes stage-internal topology searchable through residual, sequential, and parallel composition of configurable primitives. Shape-preserving composition retains the stage interfaces of a fixed multi-scale scaffold. Second, a functional-tree encoding supports stage-aware crossover and hierarchical mutation, while a gradient sensitivity-alignment proxy evaluates candidates without training. Multi-objective evolution balances this proxy with computation and parameter cost. Third, selected topologies are instantiated and trained in target systems with task-specific prediction interfaces. A single source search takes approximately 12 GPU hours. GeoBridgeNet-A3 achieves the best depth accuracy among four adapted decoder baselines under a common encoder and training protocol on NYU Depth V2 and KITTI. The same topology reaches 27.11 dB PSNR in Gaussian novel-view synthesis on RealEstate10K, and its refined representations support open-vocabulary segmentation on LERF. These results support decoder topology as a reusable design object across the evaluated geometric vision systems. Code and pretrained weights are available at this https URL.

---


### 222. [Imperfect Verifiers, Exact Targets: Inference-Time Scaling for Continuous Generation](https://arxiv.org/abs/2610.15281)

**<font color=#1a73e8>作者：</font>** Kijung Jeon, Molei Tao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Verifier-guided inference-time scaling uses additional computation to score intermediate states and steer generation toward better outputs. However, imperfect intermediate verifiers can distort sampling, and repeated refinement alone does not ensure recovery of the desired reward-tilted distribution. We introduce Continuous-State Verifier-Guided Backtracking (CS-VGB), an inference-time scaling method for sampling from reward-tilted distributions with continuous generative models through repeated denoising and renoising. With correctly paired denoising and renoising transitions, the stationary distribution of CS-VGB at the clean checkpoint equals the desired reward-tilted target, even when intermediate verifiers are inaccurate. Under stated regularity conditions, CS-VGB converges exponentially to the target despite verifier error, and the expected number of updates needed to reach a clean sample grows only linearly with the number of checkpoints. In analytically tractable settings, we empirically demonstrate that CS-VGB recovers the desired reward-tilted distribution despite verifier error, whereas the compared verifier-based sampling methods fail to recover the target under the same verifier errors. We also instantiate the framework with diffusion models and one-step stochastic posterior maps. Across prompt-guided ImageNet generation, facial-attribute generation on CelebA, and multi-robot planning, recurrent CS-VGB search improves reward and task success as inference budgets grow, with image-generation rewards continuing beyond the observed plateaus of denoising-only baselines.

---


### 223. [FragFlex: Fragment-Based Flexible Molecular Generation for Exploring Vast Chemical Space](https://arxiv.org/abs/2610.15284)

**<font color=#1a73e8>作者：</font>** Sihyun Park, David Ryan Koes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug discovery requires efficient exploration of an astronomically large chemical space. Molecular graph diffusion models offer a promising approach to this task, but many require graph size to be fixed before generation. Although atom-level insertion and deletion can enable flexible-size generation, jointly modeling molecular size, atom types, and bonds while maintaining chemical validity remains challenging. We introduce FragFlex, a flexible-length discrete diffusion model that performs node insertion and deletion at the fragment level. During denoising, FragFlex jointly learns the size, fragment identities, and inter-fragment connectivity of the fragment graph. A neural attachment-site predictor and valence-aware assembler then convert the generated fragment graph into an atom-level molecule. In large-scale experiments generating 10 million molecules, FragFlex achieves near-perfect chemical validity while maintaining high uniqueness, demonstrating a strong balance between the two.

---


### 224. [Protein Crystallization Segmentation and Classification Using Subordinate Color Channel in Fluorescence Microscopy Images](https://arxiv.org/abs/2610.15286)

**<font color=#1a73e8>作者：</font>** Truong X. Tran, Marc L. Pusey, Ramazan S. Aygun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The accuracy of detecting protein crystals for fluorescence microscopy images is very critical for high throughput and automated systems. Although the trace fluorescent labeling method could highlight protein crystals, reflection and emission from the fluorescence dye is not always due to crystal regions. Therefore, the analysis of the peak wavelength in the emission spectra of a fluorophore may not always yield effective results. In this paper, we show that using the subordinate color intensity corresponding to longer wavelengths than the peak wavelength of the emission spectra could improve the accuracy of protein crystal detection. Hence, we have built a segmentation method based on the percentile intensity of the subordinate color for trace fluorescently labeled (TFL'd) protein crystallization trial images. Compared to using the dominant color channel, our segmentation method on subordinate color channel was able to reduce the misclassification rate of likely-leads or crystals as non-crystals by the percentage of from 9.71% to 2.02% depending on the classifier. Similarly, the accuracy of classifiers were increased by the percentage of from 1.77% to 5.53%. Our method reached around 94% accuracy while keeping misclassification of likely-leads and crystals as non-crystals below 1%. Moreover, to evaluate the generalizability of our method, we have conducted new wet lab experiments on two proteins, Concanavalin A (Con A) and Ab inorganic pyrophosphate (AbIPPase), and the misclassification rate was below 1%. Our experiments show that using the subordinate channel may be more helpful for TFL'd protein trial image classification.

---


### 225. [ASM-6D: Fast Certified Pose-Shape Inference with Complete Correspondence Flow Maps](https://arxiv.org/abs/2610.15287)

**<font color=#1a73e8>作者：</font>** Ho Jin Choi, Minku Kim, Nadia Figueroa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Category-level 6D pose and shape estimation requires recovering an object's pose and geometry from partial observations without an exact instance model. We present ASM-6D, which couples generative complete-geometry prediction with explicit category-level pose-shape inference through shared correspondences. Given an RGB-D image, ASM-6D generates alternative complete 3D correspondence hypotheses whose point identities are shared with a category-level Active Shape Model (ASM), including occluded points. Each hypothesis is fitted directly for rotation, translation, metric scale, and instance shape without a separate correspondence-assignment stage. We analytically eliminate translation and shape coefficients, reducing fitting to a nine-variable scaled-rotation optimization problem that enables efficient batched evaluation of multiple hypotheses in real time. ASM-6D achieves state-of-the-art performance on ROPE and HouseCat6D benchmarks. Ablations demonstrate the importance of generative correspondence prediction and active shape variation. The representation also supports shape completion, shape-dependent pose ambiguity, tracking, and robotic grasping at 6-38 Hz, depending on the inference budget.

---


### 226. [HGA-Quant: Heterogeneity-Aware Quantization for AutoRegressive Visual Generation Models](https://arxiv.org/abs/2610.15297)

**<font color=#1a73e8>作者：</font>** Xinmeng Liu, Xianglong Yan, Kaicheng Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, AutoRegressive Visual Generation (ARVG) models have emerged as a competitive paradigm for high-quality image synthesis. However, their substantial computational and memory demands make them difficult to deploy on resource-constrained edge devices. Post-Training Quantization (PTQ) provides a promising solution to reduce the computational and memory costs of ARVG models, yet existing methods often suffer from substantial image quality degradation under low-bit quantization. In this paper, we propose a training-free PTQ framework for ARVG, consisting of Tail-Aware Bounded-init Grid Refinement (T-BGR) and Coarse-to-Fine Activation Precision Scheduling (CAPS). T-BGR introduces a tail-aware reconstruction objective for weight quantizer calibration, assigning greater importance to distribution-tail coefficients and preserving fine-grained information without introducing additional parameters or high-precision branches. CAPS performs coarse-to-fine activation precision scheduling by jointly considering the importance and computational cost of different generation stages, enabling efficient mixed-precision allocation under a given bit budget. Extensive experiments on multiple ARVG backbones demonstrate that our framework consistently improves robustness under aggressive low-bit quantization. Notably, on Infinity, our framework achieves near full-precision image generation quality at an effective W4A5.6 activation precision, while existing methods at W4A6 still exhibit noticeable quality degradation or inconsistent performance. Code is available at this https URL.

---


### 227. [WisdomNet: trustable machine learning toward error-free classification](https://arxiv.org/abs/2610.15299)

**<font color=#1a73e8>作者：</font>** Truong X. Tran, Ramazan S. Aygun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Misclassification is a critical problem in many machine learning applications. Since even the classifier models with high accuracy (e.g., > 95%) still introduce some misclassification error, it may not be possible to rely on the output of a classifier. In this paper, we introduce trustable learning, which prompts the learning model to yield only the true output, thus avoiding misclassifications. Whenever the model cannot decide the output accurately, the learning model should indicate that there could be a misclassification error if it is forced to classify, and hence, it should reject to make a decision or defer it to a human expert. Therefore, we develop a methodology for trustable learning and apply it to artificial neural networks and show that it is possible to develop a classifier with 0% misclassification error. We propose a novel neural network architecture named WisdomNet that could provide zero prediction error by introducing an additional neuron named as conjugate neuron that would indicate whether the network is able to classify the data correctly or not. The WisdomNet architecture can be applied to any previously built model, and we have evaluated WisdomNet with several network architectures such as multilayer perceptron, convolutional neural network, and deep network on different data sets. The results show that the WisdomNet is able to reduce the classification error rate to 0%, while labeling the data is difficult to classify as `reject' at a low percentage of within around 10%.

---


### 228. [FENAS: A Few-Shot Meta-Ensembling Framework for Efficient Neural Architecture Search with Synergized Zero-Cost Proxies](https://arxiv.org/abs/2610.15307)

**<font color=#1a73e8>作者：</font>** Yifeng Mao, Yuze Feng, Yutong Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient neural architecture search (NAS) requires accurate performance estimation under limited evaluation budgets. Existing zero-cost proxies (ZCPs) provide fast training-free signals, but each proxy usually captures only a partial property of an architecture, leading to unstable rankings across datasets and search spaces. In contrast, GNN-based predictors can improve accuracy, but often depend on labeled architectures, graph encoders, and costly representation learning, which makes them less suitable for extreme few-shot settings. We propose FENAS, a topology-agnostic few-shot prediction framework that turns complementary initialization priors into robust ranking signals. Its core component, CAST, is a feature pipeline that combines copula alignment and synergy transformation. CAST maps heterogeneous ZCPs into a compact feature manifold, enabling lightweight meta-learners to produce reliable rankings from scarce supervision. On NAS-Bench-201, with only 0.5% labeled samples, FENAS achieves a Kendall's Tau ($\tau$) of 0.70, outperforming representative topology-based few-shot predictors in this low-label regime. In closed-domain search, FENAS evaluates the NAS-Bench-201 space in approximately 1138 seconds and achieves competitive test accuracy. By providing a fast, reliable, and structurally simple evaluation mechanism, FENAS supports the design of automated neural architectures under limited evaluation budgets.

---


### 229. [ArguScale: Evidence-Grounded Human-AI Sensemaking Across Concurrent Live Conversations](https://arxiv.org/abs/2610.15319)

**<font color=#1a73e8>作者：</font>** Panayu Keelawat, Caleb Wohn, Shiva Pochampally 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Monitoring concurrent classroom collaborative reasoning discussions is challenging because instructors have to track collaboration-relevant behaviors across multiple ongoing conversations at once. Existing Human-AI conversational sensemaking systems can scale monitoring upward through summaries and visual abstractions, but these representations may distance users from underlying conversational evidence, e.g., relevant audio and transcript segments, needed to forage downward. Through our formative study, we developed ArguScale, an evidence-grounded Human-AI sensemaking system that organizes interactional signals into temporally aligned representations linked to transcript and audio evidence. A temporal signal-density view provides temporal context and supports rapid cross-group comparison, while selective evidence access allows instructors to inspect audio and transcript. We evaluated ArguScale in a mixed-design study with 20 participants. Compared to other conditions, ArguScale improved participants' ability to efficiently and accurately identify collaboration-relevant cues. We further identify strategies participants used to forage for and make sense of conversational evidence under live time constraints.

---


### 230. [Channel Match: Calibrating Shape Latents for Few-Step 3D Generation](https://arxiv.org/abs/2610.15321)

**<font color=#1a73e8>作者：</font>** Di Yang, Zhihao Li, Yanhai Xiong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent native 3D generators achieve high-quality asset creation by modeling structured 3D latents with flow-based transformers, but their high-resolution generation remains computationally expensive due to costly iterative sampling. In this work, we introduce a few-step distillation framework for native 3D generation, enabled by continuous self-consistency training with a custom JVP FlashAttention kernel and an analytic velocity regression objective for sparse structured 3D latents. To stabilize joint optimization, we further introduce an adaptive loss weighting strategy that automatically balances them without manual tuning. Beyond acceleration, we reveal a previously overlooked failure mode of few-step native 3D generation: sampling-induced latent distribution drift preserves geometric correctness but disrupts downstream PBR texture synthesis, causing texture artifacts on geometrically valid assets. To address this issue, we propose Channel Match, a training-free adaptive per-channel latent calibration method that restores the latent distribution without modifying either generator. We validate our approach on TRELLIS.2 at the $1024^3$ resolution setting. Our two-step model achieves $4.5\times$ faster geometry sampling while maintaining geometry quality comparable to the many-step teacher, and Channel Match further improves rendering quality by recovering the latent interface between geometry and appearance generation.

---


### 231. [CIViC: Evidence Gates for Audio-Conditioned Visual Prediction on Proxy Tasks](https://arxiv.org/abs/2610.15327)

**<font color=#1a73e8>作者：</font>** Mengzhe Geng, Max W. Y. Lam, Yuewen Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Removing audio can shift a visual predictor's output without showing whether the task uses the intended audio information. We introduce Conditional Input and Visual Interpretation Checks (CIViC), a four-gate protocol that links an interpretation to an intervention, held-out task comparison, or endpoint control. We demonstrate CIViC on actor-disjoint face-raster tests, a synthetic audio-feature mixture, and source-video-disjoint SpeakerVid proxy tasks. In the static face-raster test, cross-actor audio replacement meets the registered detection rule with a small effect; on a separate temporal endpoint, constant-audio fits score better than audio-trained fits in four matched seeds. In the synthetic mixture, the condition-augmented fit has higher 1,000-step RMSE than the audio-only fit (0.1807 vs. 0.1707), with the gap shrinking during training. In the SpeakerVid proxy, the five-feature-zero fit (five low-level audio summaries zeroed; identity, dialogue, and condition inputs retained) has lower whole-frame grayscale RMSE than aligned audio across four held-out conditions and five paired seeds, while aligned audio has lower segment-drift error. The results show that output activation, held-out error, and endpoint controls support different interpretations across these proxy tasks.

---


### 232. [BaT-SAM: Introducing Inductive Bias into SAM via a Mixture of Convolutional Experts for Brain Tumor Segmentation](https://arxiv.org/abs/2610.15330)

**<font color=#1a73e8>作者：</font>** Sumiaya Jannat, Md Mahedi Hasan, Md Shamimul Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate brain tumor segmentation from magnetic resonance imaging (MRI) is essential for diagnosis and treatment planning; however, manual delineation is labor-intensive and time-consuming. Existing approaches are either task-specific with limited generalization or rely on user-provided prompts during inference. We present BaT-SAM, a parameter-efficient adaptation framework that enables fully automatic brain tumor segmentation with the Segment Anything Model (SAM). BaT-SAM injects local inductive bias into SAM's frozen Vision Transformer (ViT) encoder via Conv-LoRA, where image features are processed by a sparsely gated mixture of multi-scale convolutional experts. This design compensates for the limited translation-equivariant inductive bias of vanilla ViTs while fine-tuning fewer than 5M parameters (less than 1% of the full model). To remove the need for user prompts, we further introduce a lightweight self-prompting box regressor that is jointly optimized with the adapter using scheduled sampling and predicts tumor locations directly from image embeddings. On the BRISC2025 benchmark, BaT-SAM achieves a weighted mean IoU of 0.832 while outperforming state-of-the-art benchmarks. It further demonstrates strong cross-dataset generalization, achieving Dice scores of 0.702 on Figshare and 0.784 on the LGG MRI Segmentation dataset.

---


### 233. [Full Waveform Inversion with a Learned Preconditioner](https://arxiv.org/abs/2610.15331)

**<font color=#1a73e8>作者：</font>** Jeongjin Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full-waveform inversion (FWI) is a powerful approach for reconstructing subsurface velocity models, but its practical performance is limited by ill-conditioning, sensitivity to the update direction, and the high cost of curvature-based methods. In this project, we investigate whether a neural operator trained on reverse-time-migration (RTM) images can provide a useful learned preconditioner for FWI. We compare projected FWI against neural-preconditioned FWI using either a standard Fourier neural operator (FNO) or a Jacobian-informed FNO (JI-FNO). The neural preconditioner applies the normal operator of the learned RTM map to modify the true Devito FWI gradient. Our experiments show that the JI-FNO preconditioner achieves the lowest model error while maintaining data-residual decay comparable to baseline projected FWI. In contrast, the standard FNO preconditioner is unstable and gives worse model recovery, despite using the same neural-preconditioning framework. We also identify a failure mode of a nonlinear neural Gauss Newton-type inner solve: directly matching the neural RTM output to the FWI gradient creates an objective-space mismatch and does not yield a reliable descent direction. These results suggest that forward RTM-image prediction alone is insufficient for learned preconditioning; accurate learned derivatives and objective-consistent use of the neural operator are critical for producing useful inversion updates.

---


### 234. [MultiFlow: Vision-Driven Multimodal fMRI Encoding via Stimulus-Informed Source Flow Matching](https://arxiv.org/abs/2610.15339)

**<font color=#1a73e8>作者：</font>** Bui Van Hung, Hoang-Son Vo, Mai Duc Minh Huy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current fMRI encoding models frame prediction as deterministic regression, yet identical stimuli evoke a distribution of neural responses (arising from physiological noise, hemodynamic variability, and cognitive fluctuations) that a single point estimate cannot capture. This work introduces MultiFlow, a generative fMRI encoding framework based on Conditional Flow Matching (CFM) and a formulation termed Stimulus-Informed Source Flow Matching (SISFM). SISFM generalises CFM by conditioning the source distribution on the stimulus: a learnable temporal convolution shapes the source mean with an HRF-length receptive field, while a variance head shrinks its scale, shortening the expected transport path. SISFM is instantiated with a Diffusion Transformer (DiT-X) decoder parameterising the velocity field, with sub-layer Attention Residuals, heterogeneous fusion of ten frozen vision, audio, language, and audiovisual backbones, and per-subject Yeo-network heads. On the Algonauts 2025 dataset, a single MultiFlow checkpoint recovers most of the benefit of large deterministic ensembles: it trails the 1000-model TRIBE ensemble in-distribution by 0.003 PCC (0.3163 vs. 0.3195), and the strongest in- and out-of-distribution ensembles (VIBE-20, MedARC-50) by 0.010 and 0.009 PCC, using a single trained model rather than an ensemble of 20-1000. The same checkpoint also provides stimulus-conditioned uncertainty estimates and sample-based diversity.

---


### 235. [StimFlow: Synthesizing Brain Activity from Images via Stimulus-conditioned Flow Matching](https://arxiv.org/abs/2610.15341)

**<font color=#1a73e8>作者：</font>** Bui Van Hung, Dang Thanh Vu, Hoang-Son Vo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The inherent variability of fMRI responses across trials encourages a generative view of the stimulus-to-response mapping. Prior generative encoders often operate in compressed latent spaces and condition predominantly on semantic features, which provide limited low-level cues for early visual cortex. We propose StimFlow, which synthesizes fMRI directly in native voxel space using conditional flow matching with a linear path. This design aligns training and inference distributions, enabling competitive performance with a single sample and reducing reliance on averaging. To match the visual hierarchy, StimFlow combines structural DINOv2 features with semantic CLIP features, which prove complementary along the cortical processing stream. With a single sample, StimFlow achieves a per-voxel Pearson correlation of 0.371, matching baselines that average five draws. Generation in voxel space allows direct ROI analysis and concept localization without a decoder. Furthermore, it recovers over half of full-data performance from just one hour of scans, supporting efficient cross-subject adaptation.

---


### 236. [Across Viewpoints and Time: Trajectory-Generalizable Physical Attacks on World Models and Video Understanding Models](https://arxiv.org/abs/2610.15343)

**<font color=#1a73e8>作者：</font>** Song Xia, Meiwen Ding, Chenqi Kong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models and video understanding models are increasingly deployed in dynamic visual environments, yet their robustness to physical adversarial threats remains largely underexplored. We study whether a single physical adversarial texture can mislead the victim model across different real-world scenarios where observing viewpoints vary along uncontrolled object--camera trajectories. We identify that heterogeneous video semantics and trajectories induce poorly aligned gradients for optimizing the adversarial texture. To address that, we propose the Trajectory-aware adversarial Alignment and Refinement Attack (TARA), which incorporates trajectory-aware optimization to capture the evolving geometric variations of a printed texture under real-world scenarios. To improve cross-instance optimization compatibility, TARA incorporates trajectory-aware contrastive alignment to encourage attacked representations from diverse video--trajectory instances to approach a shared adversarial region and then performs trajectory-aware task refinement to translate the aligned representation into task-level prediction errors. For reproducible evaluation, we develop a geometry-grounded tracking pipeline that provides physically plausible adversarial regions with temporally consistent trajectories on EPIC-KITCHENS-100 and Something-Something V2. We further collect real-world print-and-recapture videos to validate attack effectiveness under physical deployment conditions. Together, the annotated benchmarks and real-world captured data form a reproducible testbed for future evaluation. Notably, our results reveal that a single printable adversarial texture can persistently disrupt world models and video understanding models under physical conditions, highlighting the fundamental security challenge.

---


### 237. [Siam-ALS: An Explainable Siamese Deep Learning Framework for Early ALS Detection Using EEG and Eye-Tracking Signals](https://arxiv.org/abs/2610.15351)

**<font color=#1a73e8>作者：</font>** Abdur Rahman, A. A. M. Muzahid, Istiak Ahmed 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Amyotrophic lateral sclerosis (ALS) diagnosis remains challenging due to heterogeneous symptoms and reliance on clinical assessment, underscoring the need for objective, data-driven approaches that leverage patient-generated physiological signals. We propose Siam-ALS, an explainable Siamese deep learning framework that jointly models synchronized electroencephalography (EEG) and eye-tracking (ET) signals. EEG captures ALS-related changes in brain activity, while ET provides information about oculomotor control, allowing the model to learn complementary patterns associated with ALS. The framework employs two modality-specific encoders: a convolutional EEG encoder that captures spatiotemporal neural patterns and an MLP-based ET encoder that models oculomotor dynamics. These modality-specific features are processed through weight-sharing Siamese branches and fused into a compact 64-dimensional joint embedding. A lightweight classifier is used to predict ALS, while pairwise metric learning helps the model learn more effective patterns from the small, diverse ALS datasets. Performance was evaluated on the public EEGET-ALS dataset using strict subject-level cross-validation, where Siam-ALS achieved an accuracy of 0.988 and an AUROC of 0.998, demonstrating strong performance compared with classical machine learning, DL, and non-Siamese fusion approaches. Cross-dataset evaluation on the independent BigP3BCI dataset achieved an AUROC of approximately 0.98, supporting the generalization capability of Siam-ALS across different BCI paradigms. To enhance interpretability, six XAI methods were evaluated in the learned embedding space, with SHAP achieving the highest, though statistically comparable, fidelity in identifying important EEG and ET patterns that contribute to ALS predictions. Overall, Siam-ALS provides an accurate, generalizable, and explainable framework for multimodal ALS detection.

---


### 238. [Video-Based Sexual Harassment Detection Using Fine-Tuned Video Transformers](https://arxiv.org/abs/2610.15354)

**<font color=#1a73e8>作者：</font>** Jubayer- Al- Mahmud, Md Shamimul Islam, Md Nur Hossain  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sexual harassment represents a pervasive societal challenge, with a substantial proportion of incidents remaining unreported due to insufficient evidence and delayed intervention mechanisms. Smart surveillance systems capable of detecting such incidents in real-time could assist law enforcement and serve as a deterrent. However, video-based harassment detection poses significant challenges, including variations in clothing, illumina- tion, partial occlusions, low resolution, and diverse camera view- points. Despite its social importance, this problem has received limited research attention, primarily due to the scarcity of large- scale annotated video datasets. To address this gap, we extend the Sexual Harassment Video (SHV) dataset to 600 short video clips sourced from YouTube and annotated into harassment and non-harassment categories using consistent labeling guidelines. We fine-tune three state-of-the-art video transformer models, VideoMAE, ViViT, and TimeSformer, pretrained on Kinetics- 400, for binary harassment classification. Experimental results show that all three models achieve competitive classification performance, with TimeSformer attaining the highest test accu- racy of 92.27%, outperforming VideoMAE 91.71% and ViViT 91.16% on the extended SHV test set. Our analysis reveals that performance is notably influenced by dataset size, video quality, frame sampling strategy, and model architecture. This work presents a comprehensive evaluation of modern video transformers for this sensitive real-world task.

---


### 239. [UniForge3D: Joint 3D Reconstruction and Generation in a Shared Anchor-Guided Space](https://arxiv.org/abs/2610.15357)

**<font color=#1a73e8>作者：</font>** Wenjue Chen, Wenyue Chen, Heliang Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating complete 3D assets from sparse, unposed images requires preserving observed geometry while completing unseen regions. Joint reconstruction and generation offers a way to address both goals: reconstruction recovers the geometry observed in the input images, while generation contributes learned shape priors. However, combining camera-relative reconstruction with canonical-space generation introduces a coordinate mismatch that makes direct geometric interaction more difficult. Moreover, conditioning each 3D location on all views without accounting for their relevance may mix useful geometric evidence with unrelated image content, hindering local detail recovery. We present UniForge3D, which jointly models reconstruction and generation in a shared anchor-guided space, resolving their coordinate mismatch. This space follows the anchor view's azimuth while keeping the object upright. The two branches exchange features bidirectionally to predict per-view point maps and a complete sparse voxel structure. We further condition point-map prediction on the generated structure to establish pixel-to-voxel correspondences and select the most informative input view for each voxel. Features from the selected views then guide detailed shape generation, helping preserve observed geometric details. Our method achieves state-of-the-art appearance and geometry results on Toys4K and GSO, generating complete 3D assets with improved fidelity. Project webpage: this https URL

---


### 240. [Adversarial Detection for Pre-trained Classifiers via Lipschitz-Margin Analysis with Certification](https://arxiv.org/abs/2610.15359)

**<font color=#1a73e8>作者：</font>** Rui Zhang, Xinle Cao, Huazhen Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep classifiers deployed in safety-critical services like autonomous-driving perception remain vulnerable to small adversarial perturbations. Certified $\ell_2$ defenses today face a costly trade-off: randomized smoothing (RS) requires hundreds of noisy queries per input, while Lipschitz networks (LN) constrain the architecture and sacrifice clean accuracy. We take a detection-oriented approach instead: rather than certifying that predictions are invariant inside an $\ell_2$ ball, we certify that adversarial inputs within an $\ell_2$ ball are \emph{detected} --- a guarantee aligned with security-critical deployments where missing an attack is costlier than flagging a clean input.
To realize this, we prove a Lipschitz-margin reduction from certified $\ell_2$ robustness to certified detection, which reduces the problem to handling a single Lipschitz constant $L$. We introduce two detector families: $\mathbb{D}_{Adv}$, which estimates $L$ from a single defender-side perturbed pair, and $\mathbb{D}_{lc}$, which augments that pair with a local margin centroid to keep the estimate above what the certificate requires. Both deploy on any pretrained classifier without retraining. With a valid global bound, the detector is fully certified at that radius; with a local estimate $L'$, certification is sample-wise and applies only when our certified condition holds.
Across MNIST, CIFAR-10, and ImageNet-1k on four backbones (LeNet-5, VGG16, ResNet-50, ViT-B/16), our detectors match or outperform five baselines (CTT, SortNet, CRM, ContraNet, A$^2$D). For CIFAR-10 with 1-Lipschitz SortNet, our reduction delivers $100\%$ certified detection at the lowest FPR among compared certified detectors; on the standard CIFAR-10 VGG16, our detectors reject all evaluated in-budget adversarial examples, with 62-82\% both rejected and formally certified.

---


### 241. [Analyzing the Dynamics of WSBM-based Echo State Networks using InputDSA](https://arxiv.org/abs/2610.15380)

**<font color=#1a73e8>作者：</font>** Huy Mai, Robert Clarke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bridging the structural gap between biological brains and artificial neural networks presents a pathway to altered computational dynamics. This paper introduces a Reservoir Computing framework that replaces random networks with biologically realistic modularity by applying the Weighted Stochastic Block Model (WSBM) to Echo State Networks (ESNs). This topological parameterization constructs reservoirs reflecting latent functional sub-circuits. Furthermore, the integration of Input Dynamical Similarity Analysis (InputDSA) provides a mechanism to isolate and compare how structural priors modulate intrinsic recurrent dynamics versus external inputs. By evaluating these architectures, we establish that structural diversity does not necessarily predicts behavioral diversity across the selected network subset. Furthermore, our demixed analysis confirms Anna Karenina principle of dynamics, demonstrating that environmental constraints enforce dynamical convergence in successful agents, while failing networks degenerate into idiosyncratic trajectories.

---


### 242. [Approximation in Contrastive Representation Learning](https://arxiv.org/abs/2610.15388)

**<font color=#1a73e8>作者：</font>** Yuanfan Li, Zihan Zhang, Yiming Ying 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive representation learning (CRL) is a fundamental paradigm for
learning transferable representations. Recent work
identifies its population target as the pointwise mutual information (PMI)
$\log\frac{p(x,y)}{p_X(x)p_Y(y)}$
between two modalities $X,Y$, where $p$ is the joint density function and
$p_X,p_Y$ are the marginals. However, it remains unclear why standard inner-product scores $f(x)^\top g(y)$ can effectively approximate a generally nonseparable population target PMI. In this paper, we address this question from the aspect of approximation for CRL. By linking PMI to a compact operator, we show that $D$-dimensional inner-product models perform rank-$D$ spectral approximation, with error controlled by the spectral tail. We then study neural network realizations: in general settings, we show that deep neural network scoring functions are universally consistent, and the approximation error rates depend on the smoothness of the PMI function; under structured low-rank data models we obtain improved rates attained by moderate-width encoders. Finally, we establish a fast calibration rate from contrastive excess risk to downstream retrieval error under a density-ratio Tsybakov noise condition.

---


### 243. [CoverSynth: Coverage-Guided Generation of Retrieval Evaluation Sets](https://arxiv.org/abs/2610.15409)

**<font color=#1a73e8>作者：</font>** Anahita Sharma, Apaar Shanker, Rishav Chakravarti 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise agents need retrieval evaluation sets that expose domain-specific failures and guide developers towards efficient deployment tradeoffs. Neither expert-human-authored sets nor current synthetic generation methods provide a methodology for achieving the necessary coverage, reliability, efficiency, and discriminability required for such decision-making. Simultaneously, the field does not have an assessment framework for determining when an evaluation set has satisfied these properties. We introduce an evaluation set assessment framework for these criteria and CoverSynth -- a generator specifically designed to satisfy these criteria without incurring the high cost of human expert labeling. Starting from an unannotated corpus, CoverSynth targets coverage across retrieval demands and system capabilities. Deterministic checks locate evidence quotes in their sources, while model-based checks assess semantic validity to guarantee reliable ground truth. Across five public enterprise-style corpora, our method provides informative variation in difficulty, revealing unseen failure modes such as an inability of agents to handle underspecified or ambiguous requests. On the RepLiQA corpus, 91\% of human-generated queries can be answered by all members on a panel of 12 retrieval systems, compared to only 12\% of CoverSynth-generated queries. Finally, in a repeated TechQA/RepLiQA study, 12 of 12 within-harness model contrasts have positive nominal 95\% intervals on generated sets, compared with 4 of 12 on human sets. CoverSynth makes coverage and evidence quality explicit construction objectives, producing corpus-grounded evaluations that reveal retrieval headroom and differences between agent configurations.

---


### 244. [OmniRSI: Taming Latent Diffusion for Unified Multimodal Remote Sensing Image Generation](https://arxiv.org/abs/2610.15414)

**<font color=#1a73e8>作者：</font>** Hebaixu Wang, Jing Zhang, Haonan Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal remote sensing image generation emerges as a promising paradigm for recovering complete and complementary observations from heterogeneous and partially observed remote sensing data. However, existing methods predominantly depend on sensor-specific fine-tuning of natural image generation models, limiting unified multimodal generation capacity due to the absence of shared representations and robust conditioning mechanisms. To address these challenges, we propose OmniRSI, a unified multimodal remote sensing image generation model. Specifically, we develop a remote sensing-specific variational autoencoder that captures multimodal priors and promotes a locally smooth latent space for unified representation and robust reconstruction across diverse observed data. Building upon that, we fully adapt Stable Diffusion 3.5 with a ControlNet branch to support unified multimodal generation and translation conditioned on textual and visual cues. Besides, we devise a training-free cyclic latent alignment mechanism that iteratively enriches incomplete visual conditions with generated multimodal information, progressively improving guidance reliability while preserving observed measurements. We also construct RSI-MM, a large-scale dataset comprising 11.5M multi-resolution images with text annotations and partially paired data for training and evaluation. Extensive experiments verify that OmniRSI achieves superior performance in multimodal reconstruction, generation and translation.

---


### 245. [Pessimistic Latent Task-aware Optimization for Robust Offline Meta-Reinforcement Learning](https://arxiv.org/abs/2610.15428)

**<font color=#1a73e8>作者：</font>** Chang-Hoon Jeong, Kisung Shin, Hanwool Sul 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Context-based offline meta-reinforcement learning (COMRL) has advanced almost entirely through better task representations, which separate task identity from artifacts of the behavior policy so that the latent reflects the task alone. The implicit expectation has been that a clean representation will transfer to out-of-support (parameter-extrapolation) tasks. On such a task, however, the encoder produces a latent outside the training support, where the policy has never been trained. We address this gap with Pessimistic Latent Task-aware Optimization (PLATO), which exposes the policy to off-support latents during training. PLATO assumes a mild manifold hypothesis: task latents lie on a low-dimensional manifold, and out-of-support tasks lie farther from the training centroid. It exploits this geometry by perturbing inferred latents outward from the centroid to synthesize counterfactual tasks. A learned decoder ensemble then rolls out short trajectories at each perturbed latent, and the policy is updated on the imagined transitions under a pessimism weight that down-weights steps on which the ensemble disagrees. We prove that the perturbation leaves the training support by a controllable margin and that the out-of-support generalization gap is bounded by the same perturbation reach, and we give explicit conditions, verified empirically, under which the epistemic disagreement at the perturbed latent stays bounded away from zero. On eight MuJoCo continuous-control benchmarks, PLATO consistently improves out-of-support returns over strong COMRL baselines while remaining competitive on in-distribution tasks. Our code is available at this https URL.

---


### 246. [World Modeling through Spectral Alignment](https://arxiv.org/abs/2610.15429)

**<font color=#1a73e8>作者：</font>** Holger Molin, William Peng, Marco Bagatella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How do we tell a world model what information to preserve? We study this question through the lens of spectral representation learning. We introduce SpecWM, a JEPA framework that explicitly specifies desired relationships between observations through a target similarity kernel and trains the encoder to reproduce those relationships in its embedding geometry. Different kernels provide different supervision, ranging from physical state information to a fully self-supervised temporal kernel requiring only the ordering of observations within trajectories. We characterize the global optima of the objective, establish conditions for linear recoverability and invariance to nuisance information, and connect temporal-kernel similarity to the behavioral successor measure under an idealized setting. Empirically, the choice of kernel strongly controls which physical quantities are recoverable from the representation. More importantly, temporal spectral alignment improves CEM planning success over LeWorldModel from 52% to 68% on OGBench Cube, 49% to 77% on OGBench Scene, and 29% to 51% on CALVIN. These results suggest that explicitly specifying representation geometry provides a simple way to steer what latent world models preserve for control.

---


### 247. [Harnessing SPAD Noise: Test-Time Gated Attention for Indoor Depth Estimation](https://arxiv.org/abs/2610.15431)

**<font color=#1a73e8>作者：</font>** Yiquan Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation (MDE) has emerged as a cost-effective alternative to hardware-dependent 3D sensing modalities, yet predicting precise metric depth remains a persistent challenge due to intrinsic scale ambiguity, edge bleeding, and limited zero-shot generalization in unseen environments. Recent multi-modal approaches incorporate 1D/3D Single-Photon Avalanche Diode (SPAD) data to resolve these ambiguities, but they mainly treat SPAD noise as a harmful artifact required for denoising or leave the noise ignored. In this paper, we present an essentially different insight: native SPAD noise is an informative prior that implicitly encodes deterministic environmental characteristics. Driven by this paradigm shift, we introduce a novel, lightweight Test-Time Gated Attention framework by Harnessing SPAD Noise, therefore dubbed HSN. Tailored for indoor scenarios, HSN leverages the synergistic combination of 1D SPAD histograms and Gate Adapters (GAs). Through three complementary optimization phases, it generates channel-wise gated attention vectors to dynamically adjust encoder feature maps at inference time, effectively resolving ambiguous scale and boundary challenges without the heavy computational overhead or dense 3D modalities that other TTA methods suffer from. Extensive experiments on challenging real-world indoor benchmarks show that HSN achieves state-of-the-art metric depth accuracy in in-domain settings, while exhibiting even greater potential under zero-shot generalization to unfamiliar environments. Furthermore, interpretability analysis reveals that the proposed gated attention mechanism adaptively shifts attention toward deeper semantic layers under intensifying SPAD noise. Code will be made publicly available.

---


### 248. [Rethinking Supervision in Document Unwarping: A Self-consistent Flow-free Approach](https://arxiv.org/abs/2610.15445)

**<font color=#1a73e8>作者：</font>** Shaokai Liu, Hao Feng, Wengang Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, the proliferation of smartphones has led to an upsurge in the digitization of document files via these portable devices. However, images captured by smartphones often suffer from distortions, thereby negatively affecting digital preservation and downstream applications. To address this issue, we introduce DRNet, a novel deep network for document image rectification. Our approach is based on three key designs. Firstly, we exploit the intrinsic geometric consistency inherent in document images to guide the learning process of distortion rectification. Secondly, we design a coarse-to-fine rectification network to leverage the representations derived from the distorted document image, thereby enhancing the rectification result. Thirdly, we propose a unique perspective for supervising the learning of rectification networks, where undistorted document images are employed for supervision, which is free of warping mesh as ground truth in existing methods. Technically, both low-level pixel alignment and high-level semantic alignment jointly contribute to the learning of the mapping relationship between deformed document images and distortion-free ones. We evaluate our method on the challenging DocUNet Benchmark dataset, where it sets a series of state-of-the-art records, demonstrating the superiority of our approach compared to existing learning-based solutions. Additionally, we conduct a comprehensive series of ablation experiments to further validate the effectiveness and merits of our method.

---


### 249. [EmoTrace-Bench: Diagnosing Emotional Expression in Text-to-Video Generation through Controlled Cues and Intensity](https://arxiv.org/abs/2610.15452)

**<font color=#1a73e8>作者：</font>** Yeheng Wang, Liudan Shi, Yi Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) models are increasingly used to generate videos with targeted emotional expressions, yet existing evaluation methods mainly rely on holistic video-text alignment and provide limited insight into whether failures arise from target-emotion expression, intensity control, or specific affective cues. We introduce EmoTrace-Bench, a fine-grained diagnostic benchmark that controls emotion intensity and selected affective cues in prompts and evaluates generated videos at multiple levels. EmoTrace-Bench contains 448 controlled prompts covering eight emotions, two intensity levels, and diverse cue conditions. Using 12 T2V models, we generate 5,376 videos and evaluate target-emotion presence, perceived intensity, and ten audiovisual dimensions of emotional expression with an automated evaluator calibrated and validated against human annotations on a subset of the data. Results reveal substantial differences across models and prompt designs. Prompts that explicitly describe a character's emotional reaction are followed more reliably than prompts that describe only events or scenes, whereas adding more affective cues or using more explicit cinematic audiovisual language does not consistently improve emotional generation. These results illustrate how aggregate alignment scores may overlook localized differences in target-emotion expression, intensity control, and cue realization. EmoTrace-Bench provides a traceable and interpretable framework for diagnosing emotional video generation without modifying existing generation pipelines, and we release the prompts and the automated evaluation rules.

---


### 250. [Split Conformal Interval Length under Huber Contamination](https://arxiv.org/abs/2610.15458)

**<font color=#1a73e8>作者：</font>** Xiao Zhang, Bowen Zhang, Lie He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing analyses of interval length in split conformal prediction largely focus on clean data. However, how contamination at the training and calibration stages alters interval length relative to the corresponding clean population oracle remains understudied. In this paper, we consider Huber contamination and derive a finite-sample upper bound that holds uniformly over contaminating distributions, with leading terms scaling as $L(\delta_1+n_1^{-1/2}) +(n_2^{-1/2}+\delta_2)/((1-\delta_2)r_0)$, in addition to a clean-sample estimation term. We further establish a minimax lower bound matching the upper-bound rate up to constant factors on a regular asymmetric location submodel. For calibration contamination, we obtain an exact worst-case characterization of the population interval-length deviation. We also extend the upper-bound results to conformalized quantile regression and adaptive residual scores. Experiments on synthetic and real-world datasets provide empirical support for our theoretical findings on training and calibration contamination.

---


> [!TIP]
> 当前位于：**201-250**（第 5/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
