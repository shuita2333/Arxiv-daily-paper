# 📦 其他研究 | 2026年08月14日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-202](./part-05.md)

---

### 51. [When Agents Talk: Honeytokens under Shared Memory](https://arxiv.org/abs/2608.11436)

**<font color=#1a73e8>作者：</font>** Joshua S. Gans  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> During a 2026 cyber-capability evaluation, short-lived AI agents turned a shared package repository into persistent memory, passing exploit findings to later agents and rebuilding the channel after it was removed. The broader evaluation culminated in an intrusion into Hugging Face. This episode raises a question for defensive deception: can a honeytoken be harmless to trusted agents without becoming recognisable to an attacker who shares their information and can implement the trusted policy? The answer is no. A trusted rule that selects genuine objects while avoiding decoys can be copied by the attacker, while a total-variation bound limits legitimate compatibility when decoys resemble genuine objects. Shared memory creates a second leakage channel by pooling weak fingerprints. For a fixed candidate, repeated non-triggering probes drive the minimum Bayes classification error to zero when type-dependent response laws differ and are known or learnable. If probing triggers containment, learning also requires the coalition to remain active long enough. Transfer across objects requires a stable deployment rule and information that orients the classes. A separate detection bound distinguishes reliable token activation from reliable attack coverage. The architectural response is to keep token identity in a private reference monitor and route legitimate agents through a provenance-enforcing broker. This produces high-confidence detection only for a specified policy violation. Honeytokens remain useful sensors, but a separate security boundary is still required.

---


### 52. [DonorRank: Donor Language Selection for Low-Resource Cross-Lingual Speech Recognition](https://arxiv.org/abs/2608.11441)

**<font color=#1a73e8>作者：</font>** Akriti Dhasmana, Aarohi Srivastava, David Chiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-resource automatic speech recognition (ASR) commonly relies on cross-lingual transfer, where models are adapted from higher-resource donor languages. However, selecting donors remains challenging for spontaneous speech from under-resourced language communities, due to linguistic variation, evolving orthographic conventions, and uneven resource availability. We present DonorRank, a learning-to-rank framework for predicting effective donor languages for zero-shot ASR. We evaluate DonorRank on two multilingual speech corpora of Indic and African language families. It accurately predicts donor language rankings and improves donor selection over common heuristics based on genetic similarity or high-resource languages. Beyond improving transfer, we show how DonorRank is a general framework for analyzing donor language selection itself. Our analyses show that the composition of the donor set determines which linguistic cues are useful in predicting successful transfer. We also identify transfer patterns that provide practical guidance for multilingual ASR in low-resource settings.

---


### 53. [How Children Collaborate within Programmable AR Environments with Co-Located Collaborative Features](https://arxiv.org/abs/2608.11442)

**<font color=#1a73e8>作者：</font>** Romina Mahinpei, Diya Ajay Hundiwala, Sandy Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Programmable augmented reality (AR) environments are emerging as a promising way to support children's creative learning through embodied interaction with digital characters and physical space. At the same time, AR systems are increasingly capable of supporting co-located collaborative experiences. However, little is known about how children collaborate within programmable AR environments offering co-located collaborative features. In response, we extended Capybara, an existing programmable AR application for children, with co-located collaborative features supporting shared visibility and interaction across devices. We then conducted workshops with 9 children to examine whether and how collaboration emerges during use. Across our workshops, collaboration was often lightweight and implicit, emerging through three complementary forms: parallel play with social awareness, iterative remixing, and spontaneous peer support. Together, our findings provide insights for designing future child-centered programmable AR systems that better support co-located collaborative experiences.

---


### 54. [XGBoost "is all you need": the case of forecasting transmitted heat energy in District Heating Systems](https://arxiv.org/abs/2608.11446)

**<font color=#1a73e8>作者：</font>** Milan Zdravković  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a comparative study of two distinct approaches, XGBoost and Long-Short Term Memory (LSTM), for forecasting transmitted heat energy in District Heating Systems (DHS). The objective is to explore scenarios in which conventional ML algorithms demonstrate better performance over deep learning networks in time series forecasting and the associated benefits in terms of computational cost and environmental impact. The study focuses on a real-world DHS dataset. Through experimentation and analysis, it is demonstrated that XGBoost consistently outperforms LSTM in this specific forecasting task. The difference is explained by the error distribution illustrating that LSTM makes more significant errors in the intervals of less data availability. The reduced computational demands of conventional ML approaches not only result in cost savings but also minimize the carbon footprint associated with data analysis tasks in energy systems.

---


### 55. [PAC-Bayes Beyond Parameter Space: Behavioral Equivalence, Z-Information, and Exact Complexity Decomposition](https://arxiv.org/abs/2608.11465)

**<font color=#1a73e8>作者：</font>** Vasant G. Honavar, Satish Kumar Keshri, Neil Ashtekar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> PAC-Bayes theory provides generalization guarantees by controlling the Kullback--Leibler (KL) divergence between posterior and prior distributions over a chosen hypothesis representation. However, predictive risk depends only on the predictive behavior induced by a hypothesis, not on the particular internal realization that implements that behavior. In over-parameterized systems, many distinct configurations induce identical predictive behavior, yet the classical PAC-Bayes KL divergence does not distinguish uncertainty over predictive behavior from variation among behaviorally equivalent realizations.
We show that this distinction induces an exact structural decomposition of classical PAC-Bayes complexity. We formalize behavioral equivalence through a measurable behavior map and use measure disintegration to decompose probability measures on the configuration space into a distribution over predictive behaviors and conditional distributions over behavioral fibers. This yields an exact decomposition of the classical PAC-Bayes KL divergence into a behavior-selection term and a realization-level term given by an expected conditional KL within fibers.
We define Z-information as the negative of this realization-level contribution: the exact gap between the KL divergence and the complexity of uncertainty over predictive behavior alone. We further show that the behavior-selection term admits an exact variational characterization: it is the minimum KL divergence among all posteriors inducing the same distribution over predictive behaviors, attained by a canonical fiber-symmetrized representative.
Finally, we show that symmetry, behavior-preserving directions, fiber geometry, and invariance under fiber-preserving perturbations arise naturally from the same behavior-map structure. Together, these results identify predictive behavior as the natural object of PAC-Bayes complexity.

---


### 56. [Gaussian Meta-Space Augmentation for Stacking Ensembles in Multimodal IPMN Risk Stratification](https://arxiv.org/abs/2608.11472)

**<font color=#1a73e8>作者：</font>** Max A. Nelson, Eminenur Sen Tasci, Zhixiang Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pancreatic cancer is among the most lethal malignancies; risk stratification of intraductal papillary mucinous neoplasms (IPMNs) offers a crucial opportunity for early intervention but typically requires invasive tissue biopsy. Dominant vision-based approaches, including radiomics and deep learning, provide promising but initially separate discrimination opportunities. Similarly, multisequence MRI (T1W/T2W) and anatomically decomposed (head, body and tail) analysis of the pancreas provide additional and potentially complementary signals. Effective fusion of this information is crucial in ordinal IPMN dysplasia risk prediction and can be accomplished via a meticulously regularized and calibrated ensemble stacking combiner. We present cUPMI, a class-conditional Gaussian augmentation of a combiner's log-probability meta-features, and test it on various prediction paradigms. In our multi-center analysis, we find cUPMI adds limited value to properly regularized L2-logistic binary classification stacks, but consistently regularizes higher-capacity tree combiners in the binary and radiomics-only setting (RF +0.015 and XGBoost +0.024 binary AUC, positive in all seeds). Its cleanest ordinal benefit appears for XGBoost on an 8-stream radiomics task (3-class no < low < high, +0.022 QWK in all seeds). Separately, fold-locked fusion of radiomics and 2.5D CNN streams yields the strongest overall model, an RF stack reaching QWK 0.595 (95% CI [0.54, 0.64]) and binary AUC 0.839, surpassing radiomics, 2.5D ResNet, and 3D DenseNet-121 baselines.

---


### 57. [Dual-Primal Graph VAEs for Noisy Label Aggregation](https://arxiv.org/abs/2608.11473)

**<font color=#1a73e8>作者：</font>** Patrick Stinson, Nikolaus Kriegeskorte  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring the ground-truth from noisy crowdsourced labels is an important theoretical and practical problem. Neural network-based methods offer an alternative to classical Bayesian models which require specifying a family of generative models used for inference. However, current models either still rely on fairly simple generative models for inference or require pseudo-labels or synthetic data to train the aggregate classifier. We propose a graph VAE architecture in which the decoder and encoder use GAT-based message passing on the adjacency graph of a crowdsourced dataset and its dual, respectively. The ground-truth labels are treated as latent variables, enabling unsupervised representation learning without needing to train a separate classifier. We show our model achieves state of the art performance on crowdsourcing benchmarks. We then demonstrate the generality of our approach by showing how the original crowdsourcing graph can be augmented to incorporate side information such as representations from neural network classifiers trained on the noisy labels to substantially boost their classification performance at test time.

---


### 58. [Convergence Guarantees of Gradient Descent for Neural Networks via Generalized Lipschitz Smoothness](https://arxiv.org/abs/2608.11479)

**<font color=#1a73e8>作者：</font>** Siqiao Mu, Diego Klabjan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish convergence guarantees of gradient descent for general feedforward neural networks of arbitrary width or depth, with no special requirements on the initialization or dataset. We only assume that the activation functions are Lipschitz smooth, Lipschitz continuous, and linearly bounded--- properties that hold for linear, tanh, softplus, and sigmoid activation functions. For the loss function, we require that it is Lipschitz smooth in the model outputs, which is true for mean-squared error. The key theoretical insight is that the Lipschitz properties of the activation functions are partially preserved even through repeated compositions, leading to a novel generalized Lipschitz smoothness condition where the change in gradient is upper bounded by the change in the parameter space, multiplied by polynomial terms of the parameter norms at both endpoints. This type of condition holds for both the model function and the loss function, enabling a descent lemma where the loss decreases as long as the learning rate is small enough with respect to the parameter norms. By ensuring that the parameter norms do not grow too quickly to infinity, we prove that the minimum squared gradient norm converges to zero in $T$ iterations at rate $O(1/T^{1/L})$ for an $L$-layer neural network.

---


### 59. [A Runtime Decentralized Attestation and Coordinated Repair Framework for Securing Automotive ECUs](https://arxiv.org/abs/2608.11489)

**<font color=#1a73e8>作者：</font>** Josh Dafoe, Niusen Chen, Bo Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The evolution of automotive technology increasingly integrates components, transforming vehicles into interconnected systems of systems. Modern vehicles are controlled by a distributed system of computing devices, known as electronic control units (ECUs). However, this interconnectedness means that any error poses significant risks to the vehicle operator. In particular, malware can be injected into ECUs, threatening vehicle safety. To address this, we need mechanisms to detect compromised ECUs then repair them to a benign state. Existing approaches mainly focus on detection and do not address the challenge of integrating detection with runtime ECU repair. This integration is nontrivial because runtime repair involves both local rollback and reboot with timing determined from global vehicle context to avoid unsafe behavior.
In this work, we have designed DACER, a runtime decentralized attestation and coordinated repair framework for automotive ECUs. DACER is the first approach that co-designs attestation and repair to unify the ``local'' nature of firmware rollback with the ``global'' nature of ECU reboot. In DACER, each ECU performs efficient local self-attestation and self-repair functions, enabling low-overhead coordination for distributed operations. In addition, DACER takes advantage of the hierarchical vehicle computing architecture. Our resulting DACER design checks the entire state of the vehicle, resists single points of failure, conforms to real-time constraints, and enables firmware restoration during runtime. The key functions are enabled by the ARM TrustZone equipped within each ECU and the secure flash memory controller embedded in the storage device. We implemented DACER on real-world hardware and experimentally demonstrated its low overhead.

---


### 60. [Cross-Corpus Evaluation of Generalizable Vulnerability Detection in IoT Firmware](https://arxiv.org/abs/2608.11492)

**<font color=#1a73e8>作者：</font>** Sadib Hassan Rumman, Md. Shariful Islam, Md. Rayhanur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> IoT firmware vulnerability detection remains challenging due to heterogeneous firmware ecosystems, resource-constrained platforms, and limitations in existing benchmarks. Many datasets are synthetic or general-purpose and lack human-verified, contamination-screened annotations, limiting evidence on cross-corpus generalization across training sources, model architectures, and curriculum strategies. To address this gap, this paper introduces IoTVulBench, a human-verified benchmark for cross-corpus firmware vulnerability detection. IoTVulBench-Core was constructed from GitHub repositories, validated by three expert reviewers, and evaluated on a contamination-screened held-out target across five model architectures, two tuning methods, and three curriculum strategies, with ensemble, distillation, and robustness analyses. Models trained on IoTVulBench achieved the highest MCC among matched single-source datasets, reaching 0.58 versus 0.44 for PrimeVul and 0.39 for D2A. Staged curriculum learning increased MCC to 0.69, while a diversity-optimized ensemble achieved 0.73, improving by 0.42 MCC over the strongest reference comparator, a static analyzer at 0.31, and by 0.29 over PrimeVul. At a 0.5% false-positive rate, the model missed only 21% of vulnerabilities, compared with 71% for the strongest comparator. It retained 86% of its performance under identifier renaming and demonstrated strong calibration and largely faithful explanations. These findings indicate that domain-matched training data and curriculum design, rather than model scale alone, are key drivers of generalization in firmware vulnerability detection. The results provide a benchmark for future research and deployment-ready configurations for practical IoT security applications.

---


### 61. [Defending against Model Extraction for GNNs with Model Reprogramming](https://arxiv.org/abs/2608.11495)

**<font color=#1a73e8>作者：</font>** Yan Wen, Zhenyi Wang, Heng Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) serve as the backbone for high-stakes applications in Machine-Learning-as-a-Service (MLaaS). Still, their black-box deployment exposes them to Model Extraction (ME) attacks, in which adversaries steal intellectual property by querying APIs. Existing defenses suffer from a critical ''Euclidean bias'': they transfer image-based strategies (e.g., random noise) to graphs, ignoring the complex topological dependencies between nodes, which often results in severe utility degradation. Passive methods like watermarking also fail to prevent theft in real time. To bridge this gap, we propose GraphRP (Graph Reprogramming Protection), a proactive defense framework that repurposes Model Reprogramming for security. Unlike static perturbations, GraphRP introduces a Structure-Aware Gating Mechanism driven by learnable topological prototypes. This creates a dynamic ''structural firewall'' that selectively modulates the model's decision boundary: it preserves fidelity for benign queries residing on the training manifold, while maximizing the Fisher Information along the perturbation direction for adversarial queries. Under standard assumptions (bounded loss, optimal attacker, and local second-order approximation), we prove a lower bound on the attacker's estimation error that increases with the structural sensitivity of the reprogramming noise. Extensive experiments on both hard-label and soft-label ME attacks demonstrate that GraphRP significantly degrades attack effectiveness while preserving benign utility.

---


### 62. [Language-Structured Relational Q-Learning for Threat-Aware Control in Safety-Critical Driving](https://arxiv.org/abs/2608.11498)

**<font color=#1a73e8>作者：</font>** Aditya Humnabadkar, Huaizhong Zhang, Ardhendu Behera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural-language-based scenario generation offers an intuitive means of describing rare and complex driving interactions, yet it is still uncertain whether training with language-structured data leads to truly adaptive control policies. We propose Language-Structured Relational Q-Learning, instantiated through an Ego-Centric Relational Q-Network (ERQ-Net), which jointly learns inter-vehicle relevance and action values from dynamic traffic graphs. Language descriptions define surrounding-vehicle behaviours during training, while prompts and semantic actor roles are hidden from the policy. ERQ-Net must therefore infer threat relevance solely from observable kinematics and interactions. Across 2,500 safety-critical scenarios, language-structured training improves test success from 49-52% to 55-58% and increases adversary-focused attention from 1.2x to 2.1x, demonstrating emergent threat awareness. However, this representational gain does not consistently translate into adaptive control: trained policies perform similarly to the best constant action, while a portfolio of simple policies solves 76% of scenarios. We formalise this discrepancy as a recognition-control gap and show that reward reweighting and margin shaping do not eliminate the resulting policy collapse. Evaluations of realism, criticality, semantic accuracy, and transfer of state-interface representations to CARLA further highlight both the strengths and the constraints of language-structured relational policy learning in safety-critical driving scenarios.

---


### 63. [HyperFix: Combinatorial Nonlinear Correction for Task Vector Merging](https://arxiv.org/abs/2608.11499)

**<font color=#1a73e8>作者：</font>** Hyo Seo Kim, Ren Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task vectors enable model merging without joint retraining. In practice, the subset of task vectors to be merged may vary, but many existing methods use scalar tuning for a particular subset, requiring repeated tuning across subsets and restricting task vector merging to linear rescaling. We therefore formulate merging across varying task subsets as a combinatorial correction problem and introduce HyperFix, a lightweight hypernetwork that predicts subset-conditioned nonlinear corrections in weight space. Trained once on singleton, pair, and triple subsets from a task bank, HyperFix generalizes to larger subsets without per-subset optimization. Our local perturbation analysis bounds the residual correction beyond linear merging and motivates learning it from small task updates. Experiments across diverse benchmarks show that HyperFix outperforms existing task vector merging methods while reducing tuning cost.

---


### 64. [RelShap: Relationally Consistent Shapley Explanations](https://arxiv.org/abs/2608.11508)

**<font color=#1a73e8>作者：</font>** Seungeun Lee, Joao Fonseca, Julia Stoyanovich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning pipelines commonly flatten relational data into single-table representations, discarding structural constraints. Widely used Shapley value-based feature attributions then rely on feature independence, evaluating the model on combinations that could never arise in the underlying data, producing misleading explanations. We propose RelShap, a framework that incorporates relational constraints and data provenance into Shapley value computation, restricting both background data and coalition evaluation to relationally valid configurations. The framework is estimator-agnostic and composes with Kernel SHAP, Monte Carlo, and Leverage SHAP without altering their sampling or weighting properties. Functional dependencies further induce equivalence classes over feature coalitions, which RelShap exploits to reduce runtime without changing Shapley values; we provide a combinatorial characterization of the expected speedup. Experiments across multiple datasets, models, and estimators show that RelShap produces explanations that are more faithful to the data-generating process, correctly identifying the dominant feature in controlled settings where existing methods, including Conditional SHAP and ManifoldShap, do not. Our code is available at: this https URL.

---


### 65. [Let it Cook: Learning to Wait in Sequential Decision Making](https://arxiv.org/abs/2608.11511)

**<font color=#1a73e8>作者：</font>** Christopher Watson, Arjun Krishna, Dinesh Jayaraman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In sequential decision making, an agent typically observes its environment and acts at every timestep. However, such active participation may not always be necessary; tasks such as brewing coffee include periods that are served equally well by letting the environment evolve without constant monitoring and control. During such periods, the agent could simply wait to conserve its resources, or redirect its attention to another task. We capitalize on these opportunities by training a "waiting policy" that decides where and how long to wait. This involves forgoing sensing to commit to a wait action, representing a deliberate pause for a set number of timesteps. We formalize "learning to wait" as minimizing the frequency of sensing and decision making without sacrificing task performance (e.g., the total amount of time to complete a task). To train a waiting policy, we propose an approach that employs reinforcement learning with lexicographically ordered objectives. In experiments across 4 discrete-state household tasks and 3 continuous-state environments, we show that our approach successfully learns waiting behaviors, and can adapt pre-trained policies to wait where appropriate. While different tasks permit different amounts of waiting without sacrificing task performance, our approach consistently finds solutions with significant waiting, sometimes waiting for over 50 percent of the task duration.

---


### 66. [New Orthogonal Multiwavelet Filters Derived by Matrix Spectral Factorization](https://arxiv.org/abs/2608.11518)

**<font color=#1a73e8>作者：</font>** Vasil Kolev, Todor Cooklev, Fritz Keinert  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The paper considers the construction of two new orthogonal multiwavelets with supercompact support by using the Fast Bauer's method for matrix spectral factorization on the matrix product filter of the orthogonal CL multiwavelet filter. The new multiwavelets possess orthogonality, symmetry/antisymmetry, and one of them provides better coding and smoothness than other supercompact multiwavelets.
The performance of the new multiwavelet filters in subband-based edge detection, grayscale and color image compression and 1D and 2D signal denoising is compared with the GHM, SA4, CL, Integer Haar and Alpert multifilters. The comparative analysis shows that new multiwavelets can provides better human visual measures, SSIM and MS-SSIM in image compression and denoising applications.

---


### 67. [FLARE++: Low-rank attention with dynamic attention routing](https://arxiv.org/abs/2608.11519)

**<font color=#1a73e8>作者：</font>** Vedant Puri, Yongjie Jessica Zhang, Levent Burak Kara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full self-attention is a strong token mixer for PDE surrogates on irregular domains, but its quadratic cost limits its use on high-resolution problems. Efficient latent-attention models such as the Fast Low-rank Attention Routing Engine (FLARE) avoid that cost by routing all N tokens through M << N learned latent queries, but those queries are parameters: once trained, the same learned query templates serve every input. We remove this restriction with FLARE++, a low-rank attention architecture with dynamic token routing. FLARE++ reuses FLARE's own encoder to build its routing queries: learned latent seeds drive one extra encode call that gathers the N input tokens into M input-conditioned queries, and those queries then determine how the same tokens are compressed and redistributed. This preserves FLARE's explicit low-rank factorization and linear O(NM) complexity, and expresses the complete routing operation with standard scaled dot-product attention (SDPA) calls alone. We also provide a multi-GPU context-parallel implementation that shards input tokens across devices without ever gathering the full token sequence on one of them. FLARE++ is competitive across a set of standard PDE surrogate benchmarks, improving on fixed-query FLARE by 24% on average, and it gains 2.3 points of average accuracy on Long Range Arena.

---


### 68. [Towards Scalable Fuzzy PSI via Efficient Fuzzy Matching](https://arxiv.org/abs/2608.11526)

**<font color=#1a73e8>作者：</font>** Meng Hao, Xinpeng Yang, Hanxiao Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this paper, we present scalable fuzzy PSI protocols for general $L_{p \in [1, \infty]}$ distance, supporting both low- and high-dimensional sets. The core technique is two efficient fuzzy matching protocols. The first is built from a role-reversed oblivious PRF (OPRF) and realizes $O(d\log \delta)$ overhead, compared to $O((\log \delta)^d)$ in previous works. The second leverages customized oblivious transfer (OT) with $O(d\ell)$ overhead, where $\ell$ is the bit length of inputs, which is particularly suitable for short inputs. With these new techniques, we further propose a new dual-layer hashing framework for fuzzy PSI over low-dimensional sets, instantiated with our OT-based fuzzy matching and enhanced with a domain reduction optimization. The protocols achieve an overhead linear with $n, m, \log \delta, 2^d$, without the $O((\log \delta)^d)$ or $O(\delta)$ factors present in prior works. {For high-dimensional sets, we construct fuzzy PSI protocols based on our OPRF- and OT-based fuzzy matching, which achieve an asymptotic overhead linear with $n, m, d$, and $\log \delta$ but rely on the strong globally disjoint assumption.}
Extensive evaluations demonstrate that our protocols achieve up to a $145\times$ speedup in running time and a $20\times$ reduction in communication cost compared to van Baarsen and Pu~(ASIACRYPT'25), and achieve up to a $25\times$ speedup in running time and up to a $17\times$ reduction in communication cost compared to Piske et al.~(CCS'25).

---


### 69. [On Weak Bisimilarities in CCSK](https://arxiv.org/abs/2608.11531)

**<font color=#1a73e8>作者：</font>** Baptiste Vallée, Ivan Lanese  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In the context of CCSK, a reversible extension of CCS, we study different notions of bisimilarity (strong/weak, forward-only/reversible) and highlight their differences and commonalities. In particular, for the weak reversible case, not previously studied in the literature, we propose two variants, dubbed directional and mixed bisimilarity, depending on whether $\tau$ actions should be in the same direction (forward/backward) as the action being matched or not. We show, in particular, that mixed bisimilarity is a congruence and completely abstracts away from $\tau$ actions.

---


### 70. [Hierarchical Federated Transfer Learning in Digital Twin-Based Vehicular Networks](https://arxiv.org/abs/2608.11532)

**<font color=#1a73e8>作者：</font>** Qasim Zia, Saide Zhu, Haoxin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent research on the Digital Twin-based Vehicular Ad hoc Network(DT-VANET), Federated Learning (FL) has shown its ability to provide data privacy. However, Federated learning struggles to adequately train a global model when confronted with data heterogeneity and data sparsity among vehicles, which ensure suboptimal accuracy in making precise predictions for different vehicle types. To address these challenges, this paper combines Federated Transfer Learning (FTL) to conduct vehicle clustering related to types of vehicles and proposes a novel Hierarchical Federated Transfer Learning (HFTL). We construct a framework for DT-VANET, along with two algorithms designed for cloud server model updates and intra-cluster federated transfer learning, to improve the accuracy of the global model. In addition, we developed a data quality score-based mechanism to prevent the global model from being affected by malicious vehicles. Lastly, detailed experiments on real-world datasets are conducted, considering different performance metrics that verify the effectiveness and efficiency of our algorithm.

---


### 71. [Generative Semantic Segmentation via an Observable Semantic-Image Interface and Hierarchical Generator Evidence Alignment](https://arxiv.org/abs/2608.11537)

**<font color=#1a73e8>作者：</font>** Weize Cai, Yongqi Dong, Zhida Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative semantic segmentation exposes structured predictions as images, but direct color decoding is susceptible to color drift and boundary mixing, whereas latent-feature decoders that predict a separate output distribution may relegate the rendered image to an intermediate visualization. We present Semantic Prism, a conditional semantic-image generation-and-refinement framework with deterministic inference. A diffusion-distilled one-step generator renders a semantic RGB image; per-pixel distances from the rendered colors to a fixed class-color codebook define an explicit probabilistic interface. Hierarchical Generator Evidence Alignment spatially aligns multi-level generator features and uses a zero-initialized output projection to predict an additive residual in the interface logit space, retaining the image-defined interface as the reference for the final distribution. The interface and refined distributions further enable Contextual Interface--Hierarchy Disagreement (C-IHD), a fixed readout for ranking remaining pixel errors without an auxiliary predictor or additional forward pass. On the 500-image Cityscapes validation set, Semantic Prism achieves 72.07% mean intersection over union, 11.39 mIoU points above direct-interface decoding, with 0.41% expected calibration error. Matched-capacity ablations over three seeds support the benefit of jointly aligned multi-level evidence. A separately trained model attains 62.22% mIoU on BDD100K, while the Cityscapes-trained model reaches 46.89\% mIoU under source-frozen transfer to the Adverse Conditions Dataset with Correspondences, without target-domain adaptation. Across all three datasets, C-IHD consistently improves the area under the precision--recall curve for pixel-error ranking over maximum softmax probability on the same segmentation predictions; on ACDC, it raises AUPR from 0.6580 to 0.7557.

---


### 72. [Robust Ambiguity Detection (RAD) From Model- and Feature-Space Consistency](https://arxiv.org/abs/2608.11541)

**<font color=#1a73e8>作者：</font>** Manya Singh, Mark T. Keane, Arjun Pakrashi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models should be robust, in the sense of remaining predictively consistent under permissible variations. A model's predictions should ideally remain unchanged when it is replaced by a functionally equivalent one, or when its inputs are subject to minor, admissible perturbations. If such changes alter a prediction significantly, then the prediction is "ambiguous" with respect to the model. Models should abstain from making such ambiguous predictions and/or should flag them for human inspection, especially in high-stakes decision-making scenarios. However, in practice, such ambiguity is not easy to identify once a model is deployed. Here, the Robust Ambiguity Detection (RAD) framework is advanced for quantifying predictive ambiguity using two complementary metrics: Model-Space Consistency and Feature-Space Consistency. These two scores, the RAD Score-Pair, visualised through the RAD Plot, provide an interpretable characterisation of the sources of ambiguity and the actions a user may consider in response. RAD is evaluated on synthetic datasets with systematically controlled overlap, as well as several real-world datasets where the level of ambiguity cannot be directly inspected. Finally, we demonstrate a downstream application of RAD where samples are ranked by their RAD Pareto-Rank and the most ambiguous are abstained from prediction, achieving performance comparable to existing rejection-based approaches.

---


### 73. [Through Van Gogh's Eyes: Global Style Transfer with Diffusion Mod](https://arxiv.org/abs/2608.11546)

**<font color=#1a73e8>作者：</font>** Jeongha Lee, Yujin Kim, Ghazanfar Ali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artistic image synthesis aims to recreate the expressive visual identity of a target artist, yet existing methods often fail to capture an artist's global style. Conventional style transfer methods transfer the style of one or a few reference artworks to a content image in a One-to-One manner, making them effective for artwork-level stylization but limited in representing the broader stylistic distribution of an artist. Text-to-image diffusion models conditioned on artist names, such as '~ in Van Gogh style', offer greater flexibility, but they often suffer from text-induced bias and reproduce patterns from only a few iconic works. To address these limitations, we introduce Global Style Transfer (GST), an artistic image synthesis paradigm, in a Many-to-One manner, that aggregates multiple artworks from a target artist and transfers their shared global style to a single content image. For GST, we propose Global Style Guidance (GSG), which learns a residual global style offset in the intermediate feature space, or h-space, of a diffusion model under a fixed prompt. By learning artist-level style semantics purely from visual statistics, GSG mitigates text-dependent artistic bias. We further propose Content Alignment Guidance (CAG), a training-free perceptual guidance mechanism that preserves the semantic structure of the content image while allowing artist-specific geometric deformation. Experiments on WikiArt demonstrate that GST achieves superior stylistic fidelity, content preservation, and output diversity compared to existing style transfer and diffusion-based artistic synthesis methods.

---


### 74. [Certifying What Helps Customer-Return Timing: A Screen-and-Confirm Test for Conditioning Signals, and Why Decay Is Nearly Enough](https://arxiv.org/abs/2608.11555)

**<font color=#1a73e8>作者：</font>** Sang Su Lee, Vineeth Loganathan, Shishir Dash 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Practitioners enrich customer-return models with ever more signals (lifetime value, category, recency/frequency, calendar, geography), and the temporal-point-process (TPP) literature follows suit with covariate- and external-covariate-conditioned intensities. But does any of it improve the timing, and how would you know? A null ("feature X doesn't help") is only meaningful if the model could have found a signal. We make two contributions--a method and a measurement--to answer this credibly. (i) A screen-and-confirm protocol that certifies whether a candidate signal improves a TPP's event-timing likelihood: a positive control plants a coupling of known strength and confirms the model recovers it, so a real-data null can be read as "no signal" rather than "weak method." The control is validated for categorical and continuous encodings, and on a real clock-driven dataset (NYC taxi hour-of-day). (ii) A model-free ceiling quantifying how little of customer-return timing is point-predictable at all (a single-digit percentage of gap variance from any covariate; returns are near-memoryless). With these we certify a clean result on three public benchmarks (Amazon, Taobao, RetailRocket) and a real marketplace (Thumbtack): the inter-event clock--continuous-time decay, long known to beat frozen-intensity models--is nearly sufficient, and the conditioning the field keeps adding is redundant or harmful on top of it (statistically null on the public benchmarks, at most 0.06 NLL; null to mildly harmful on the marketplace). We do not claim to discover that decay helps; our contribution is the tools that turn "conditioning doesn't help" into a checkable, certified statement--plus an honest-evaluation account of the read-out/leakage pitfalls we hit and retracted.

---


### 75. [When Offline Evaluation Misleads: A Diagnostic Protocol for Reward and Policy Selection in Delayed-Feedback Contextual Bandits](https://arxiv.org/abs/2608.11560)

**<font color=#1a73e8>作者：</font>** Sang Su Lee, Vineeth Loganathan, Shishir Dash 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalizing marketing messages with contextual multi-armed bandits (CMABs) drives real business value, yet the objective that ultimately matters - a downstream conversion - is observed only weeks later, too late to drive online learning. Teams therefore train the bandit on a fast proxy reward, and separately must judge whether a contextual bandit is worth its complexity over sending one best message. Settling both decisions with the usual offline checks - a batch off-policy estimate, a marginal arm-discrimination test, a confidence interval - can mislead systematically under delayed feedback. We give an ordered diagnostic protocol that screens a reward-and-policy candidate on two axes, alignment (does optimizing the reward move the north-star?) and learnability (can the bandit identify the reward-optimal policy?), before trusting any reported lift. We validate it where the truth is known - a public off-policy-evaluation benchmark and a controllable synthetic generator - and illustrate it on a deployed large-marketplace push system (where, with five arms and one split, the evidence is directional rather than powered). Two lessons recur. (N1) A single offline number can mis-rank rewards: a denser reward signal gives the bandit more to learn from, so rewards that look tied in a static estimate pull apart once learning happens online. (N2) If you cannot tell in advance which single message is best, a per-user policy partly just avoids betting on the wrong one - that looks like personalization but is really robustness, so a "personalization premium" is easily overstated. Our contribution is methodological rather than algorithmic: the ordered protocol, the two lessons it surfaces, and the end-to-end experience of applying it to a delayed-feedback CMAB.

---


### 76. [From Synthesis to Removal: Physics-Grounded Reflection Simulation and Diffusion-Based Video Dereflection](https://arxiv.org/abs/2608.11562)

**<font color=#1a73e8>作者：</font>** Zepeng Wang, Jiagao Hu, Fuhao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Videos captured through glass often contain reflections that degrade visual quality and interfere with downstream vision tasks. Although single-image reflection removal has been extensively studied, video reflection removal remains largely underexplored due to the lack of paired video data, temporally coherent removal models, and dedicated evaluation benchmarks. We present a closed-loop framework that unifies physics-grounded reflection simulation, diffusion-based video dereflection, and benchmark evaluation. Our S2R-Synthesis pipeline generates paired reflected and reflection-free videos by performing physics-grounded augmentation in the structure space and rendering realistic reflected videos with a trained video diffusion renderer; the augmentation models key glass-related effects including roughness-induced blur, thickness-induced ghosting, and reflectance variation. Based on the synthesized data, we introduce S2R-Removal, the first diffusion-based video reflection removal model, which adapts a pretrained video diffusion prior through reflection-aware latent adaptation and one-step pixel-geometric refinement, recovering the clean transmission in a single denoising step. We further build S2R-Bench, the first benchmark for video reflection removal, supporting both full-reference evaluation and real-world human perceptual assessment. Experiments on S2R-Bench and multiple public image benchmarks demonstrate state-of-the-art performance and faster inference than even non-diffusion baselines, and validate the effectiveness of S2R-Synthesis. Project page: this https URL.

---


### 77. [Measuring Browser Webcam Gaze Honestly: A Capture-Clock Methodology and Open Reference Implementation](https://arxiv.org/abs/2608.11566)

**<font color=#1a73e8>作者：</font>** Chi-Sheng Chen, Gabriel A. Brat  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Browser-based webcam gaze trackers are increasingly used for crowd-scale data collection and in clinical settings where lab eye trackers are impractical, but the reported latency numbers may not represent real world functionality. The common practice of timestamping each gaze sample when it is emitted, rather than when its source frame was captured, makes the measured inference latency read about $0\,$ms no matter how slow the engine really is. We show how to measure it honestly, recovering a per-frame capture clock from the browser's \texttt{re\-quest\-Video\-Frame\-Call\-back} (rVFC) API (\texttt{captureTime} where the browser exposes it for local camera streams, else \texttt{presentationTime}, in which case every recovered latency is a verifiable lower bound): exact source-frame pairing through a per-frame queue for engines that expose their inference pipeline, and a further lower bound for engines that do not, such as WebGazer. We release an open TypeScript implementation and benchmark harness, demonstrated on two interchangeable engines: WebGazer and a new FaceMesh+KRR pipeline.

---


### 78. [Sparse and robust geometric twin support vector machine via asymmetric RoBoSS loss function](https://arxiv.org/abs/2608.11567)

**<font color=#1a73e8>作者：</font>** Kai Qi, Xinji Huang, Hongchun Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In real-world scenarios, the training data usually contains redundant features, label noise and feature noise, which provide severe challenges for the efficiency of machine learning methods. Since standard support vector machine (SVM) adopts $l_2$-norm penalty and hinge loss function, it lacks the ability of selecting significant features and is sensitive to noise. To address these issues, this paper proposes a novel asymmetric, robust, bounded, sparse and smooth (aR) loss function for $l_1$-norm penalized geometric twin SVM (aRSGTSVM) to handle classification and regression tasks. The $l_1$-norm penalty can achieve the feature selection. The proposed aR loss function can not only effectively mitigate the impact of label noise, but also significantly enhance the stability to resampling noise, i.e., the zero-mean feature noise around the boundary hyperplanes. Furthermore, a statistical analysis of the robustness of aRSGTSVM was also conducted using the influence function. Since aRSGTSVM involves nonconvex and nonsmooth optimization, we develop a fast and stable proximal gradient descent based solving algorithm. Compared with related state-of-the-art methods, experimental results demonstrate the superiority of the proposed aRSGTSVM on both synthetic and UCI datasets. Furthermore, we apply aRSGTSVM to index tracking tasks, where results for tracking the different indices in the China stock market show that it can achieve satisfactory performance.

---


### 79. [RECAST: A Machine-Learning Framework for Correction and Super-Resolution of Coarse-Grid PDE Solvers](https://arxiv.org/abs/2608.11572)

**<font color=#1a73e8>作者：</font>** Maryam Reza, Farbod Faraji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coarse-grid numerical solvers can substantially reduce the computational cost of time-dependent PDE simulation, but under-resolution often degrades both the trajectory and the spatial fidelity of the solution. We introduce RECAST (Recurrent Error Correction And Super-resolution of coarse-grid Trajectories), a machine-learning framework designed to restore this lost accuracy while retaining coarse-grid evolution. RECAST combines learned correction within the numerical time-stepping loop with reconstruction of the corresponding fine-grid state from the corrected coarse history. We evaluate the framework on six one-dimensional PDE systems spanning transport, diffusion, dispersion, reaction, and wave dynamics, using spatial grids coarsened by factors of 8-16 and 1000-step closed-loop rollouts from unseen initial conditions. Across the test cases, RECAST remains closely aligned with the fine-grid reference solutions and reduces time-averaged relative error by approximately 50-92% compared with the corresponding uncorrected coarse-grid solvers. Additional tests show generalization to unseen PDE parameter values, while comparison with a contemporary coarse-correction architecture shows that RECAST achieves lower error and better long-horizon agreement with the fine-grid reference over 5000-step rollouts. These results demonstrate that the learned correction and reconstruction capabilities of RECAST can enable substantially coarser PDE evolution without the corresponding loss of solution fidelity, providing a proof-of-concept route toward machine-learning acceleration of higher-dimensional numerical simulations across science and engineering.

---


### 80. [Hand Visibility Detector: Per-Keypoint Visibility Estimation for Hands](https://arxiv.org/abs/2608.11574)

**<font color=#1a73e8>作者：</font>** Ryosei Hara, Masashi Hatano, Rintaro Yanagi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hand Pose Estimation (HPE) is a fundamental technology for various applications such as AR/VR and robotics. In these applications, the visibility of each hand joint in the image is crucial for assessing the reliability of estimation results under occlusion. However, most existing HPE methods output joint positions without explicitly indicating their visibility. Although some methods account for occlusion or visibility, visibility estimation has mainly been used as an auxiliary signal for improving pose estimation. To our knowledge, per-joint hand visibility estimation has not been systematically studied as a standalone task. In this work, we propose Hand Visibility Detector, a model for estimating the visibility of individual hand joints, and present the first systematic investigation of visibility estimation as an independent task. We show that leveraging the prior knowledge of HPE models pretrained on large-scale data as a backbone yields high performance in this task. We further demonstrate the utility of Hand Visibility Detector on a downstream task of 3D hand pose annotation via multi-view triangulation of 2D keypoints, showing that visibility-weighted triangulation reduces reprojection error. Our method is released as a ready-to-use package, and the code and demo are available at this https URL .

---


### 81. [RAGE-Vis:A Relation-Aware Generative Editing Interface for Natural Language-Based Chart Editing](https://arxiv.org/abs/2608.11581)

**<font color=#1a73e8>作者：</font>** Ziyao Kang, Yiping Sun, Linxuan Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Natural language offers an easy way for users to express chart editing intents, which are often composite and cross-component (e.g., adjusting style, extending categories, highlighting values). However, existing methods typically map instructions to a single operation or widget, limiting their ability to handle high-level requests and often producing locally plausible but globally inconsistent results due to a lack of awareness of relationships between chart components. To address these challenges, we introduce RAGE-Vis, a Relation-Aware Generative Editing interface for natural language-based chart editing. The system supports bitmap chart images as input and converts them into an editable parameterized intermediate representation. Instead of mapping instructions to a single edit or widget, RAGE-Vis parses composite intents, identifies targets and scopes, and generates hierarchical editing panels for underspecified requests, enabling users to adjust both global settings and local parameters. Furthermore, RAGE-Vis identifies potentially affected fields based on visual encoding relations, structural relationships, and expressive consistency relations, and organizes them into actionable widgets to support cross-component coordinated controls. Through two case studies, we demonstrate the applicability of RAGE-Vis in complex editing tasks, including style adjustment, data extension, order rearrangement, legend layout, and color mapping. A user study further shows that participants can effectively handle underspecified requests, explore candidate alternatives, and maintain cross-component consistency with RAGE-Vis.

---


### 82. [A Hybrid Framework of Vision Transformer and Gated Recurrent Unit for Detection of Mosquito Diseases](https://arxiv.org/abs/2608.11582)

**<font color=#1a73e8>作者：</font>** Danial Sharifrazi, Saadat Behzadi, Nouman Javed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identifying dengue virus-infected mosquitoes from control mosquitoes is a major challenge in analyzing mosquito locomotion behavior due to the small size and complexity of the video background. Conventional AI methods are often unable to extract accurate features from video frames and produce erroneous features. In this study, a three-step framework is introduced: first, mosquitoes are identified and the background is removed using the YOLO 11M model, then visual features are extracted using the Vision Transformer (ViT), and finally the videos are classified with a convolutional GRU (ConvGRU) classifier. A comparative analysis of different models, including Recurrent Neural Network (RNN), Long Short-Term Memory (LSTM), Gated Recurrent Unit (GRU), and their convolutional versions showed that the ConvGRU model achieved the best performance; it achieved 88.88% accuracy, 84.45% precision, 82.82% recall, and 82.81% F1 score. These results demonstrate that combining convolutional models with sequence-based networks, especially in the ConvGRU model, allows the simultaneous extraction of precise spatial features and long-term temporal dependencies from mosquito movements. Finally, the proposed framework provides a reliable solution for analyzing mosquito behavior in complex environments.

---


### 83. [ProtoHGF-Net: Prototype HyperGraph Fusion with Intra-modal Calibration for RGBT Object Detection](https://arxiv.org/abs/2608.11595)

**<font color=#1a73e8>作者：</font>** Xiangqi Chen, Xiuling Zhang, Chengzhuan Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-Thermal (RGBT) object detection enables robust perception in complex scenes by leveraging the complementary strengths of visible textures and thermal cues. However, existing methods mainly rely on dense cross-modal interactions over full-resolution features, which inevitably introduce background interference and hinder the learning of target-relevant representations. In this paper, we propose the Prototype HyperGraph Fusion Network (ProtoHGF-Net), a novel framework that redefines cross-modal fusion as prototype-level semantic interaction rather than the dense cross-modal interaction paradigm. Specifically, we design Prototype HyperGraph Fusion to perform cross-modal interaction in a compact prototype-level semantic space. This design enables more selective fusion among target-relevant prototypes. To support this prototype-level fusion, we propose Teacher-Mask Calibration Distillation, which calibrates modality features before fusion using modality-specific teachers and target-aware masks. This strategy suppresses backgrou- nd-dominant responses and produces more target-focused features. Extensive experiments on DroneVehicle, DVTOD, and FLIR demonstrate that ProtoHGF-Net achieves state-of-the-art performance with 85.9\% $mAP_{50}$, 88.2\% $mAP_{50}$, and 79.1\% $mAP_{50}$, respectively. Our code is available at \href{this https URL}{GitHub}.

---


### 84. [How Can Driving World Models Do Counterfactual Prediction?](https://arxiv.org/abs/2608.11601)

**<font color=#1a73e8>作者：</font>** Jiaru Zhang, Can Cui, Yi Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving world models are often interpreted as counterfactual simulators for observed driving episodes: given a factual driving log, they are asked what would have happened under an alternative ego action. In this paper, we identify a fundamental mismatch between this goal and direct action-conditioned prediction. The direct prediction uses the shared history and the alternative action but not the factual continuation observed after that history. It can therefore generate a plausible future without preserving what actually happened in this episode. We formalize this gap using the causal recipe of abduction, action, and prediction and study it in a setting with a short time horizon, where the alternative ego action does not alter how surrounding agents evolve. To make the gap measurable, we construct a controlled simulation benchmark with factual outcomes and matched counterfactual outcomes. Across two representative world models, direct predictions fail to match the counterfactual ground truth, supporting our analysis. As a constructive check of this analysis, we introduce a deliberately simple, training-free pipeline that moves observed evidence into the counterfactual view and lets the frozen model complete what remains unknown. Even this simple construction raises the overall recovered fraction substantially and reduces perceptual distance to the matched counterfactual on both models. We hope this work draws attention to this gap and motivates better counterfactual prediction methods for driving world models.

---


### 85. [Foresight Without Seeing: Latent Futures for World Action Models](https://arxiv.org/abs/2608.11605)

**<font color=#1a73e8>作者：</font>** Jiakai Huang, Zhongbo Wu, Zheng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) couple future visual prediction with robot action generation, enabling policies to model how the physical world evolves during interaction. Existing WAMs differ in how predictive dynamics are exposed to the action pathway. Explicit-future WAMs provide direct access to predicted scene evolution, but incur substantial inference costs from iterative video denoising. In contrast, direct-policy WAMs efficiently predict actions from the current observation but lack an explicit inference-time interface for exposing predictive dynamics to the Action DiT. To bridge this gap, we propose ForeWAM, a dynamics-conditioned direct-policy WAM that provides predictive context for action generation without decoding future videos. At its core, Future-KV performs a single Video DiT prefill over the current visual latent and stochastic future slots, and reuses the resulting layer-wise key-value states throughout action denoising. We further introduce dynamics registers supervised by a frozen latent action teacher, encouraging the implicit future states to capture interaction-induced transitions such as object motion, contact changes, and task progress. Ground-truth future observations and the teacher are used only during training; deployment requires neither and performs no future video generation. Without embodied robot data pretraining, the standard and accelerated variants of ForeWAM achieve average success rates of 96.7% and 96.9% on LIBERO, respectively. The standard variant further achieves 61.6% success on LIBERO-Plus. These results demonstrate that direct-policy WAMs can retain efficient action prediction while exposing predictive dynamics to the action pathway without explicitly generating future observations.

---


### 86. [Topology-Aware Query Selection for Surgical Instrument Instance Segmentation](https://arxiv.org/abs/2608.11607)

**<font color=#1a73e8>作者：</font>** Ze Zhang, Yang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate foreground masks can still form an incorrect surgical-instrument instance set: duplicate, fragmented, merged, missed, or empty-frame predictions may preserve favorable pixel overlap while violating object identity and count. Final query selection is therefore a relational, variable-cardinality problem rather than a collection of independent candidate decisions. We evaluate topology-aware query selection, which represents the nonempty candidates of a fixed Mask2Former as a complete graph, learns relational candidate and pair representations, predicts set cardinality, and solves an exact structured subset problem. The formal comparison is the complete relational path versus a node-feature-matched path; it evaluates the combined effect of pairwise geometry, message passing, and the additional relational-path capacity, not an isolated component. On the sealed 22-case source test, all three discovery seeds supported instance-set performance improvement with segmentation fidelity and predefined technical-safety preservation: instance F1 increased by 0.0504--0.0612 and positive-frame set-failure rate decreased by 0.0848--0.1060. Direct ROBUST-MIPS transfer reproduced the complete result in all three seeds. Endoscapes supported only one of three seeds and therefore did not establish stable direct transfer. Taken together, the results support a bounded conclusion: the evaluated complete path improved coherent instance-set construction from fixed Mask2Former candidates in specified native-instance contracts, while stable cross-domain transfer and component-specific effects remain unestablished.

---


### 87. [Dion3: Full-Stack Orthogonal Updates](https://arxiv.org/abs/2608.11612)

**<font color=#1a73e8>作者：</font>** Noah Amsel, Jack Zhang, Kwangjun Ahn 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Muon optimizer incurs a significant overhead cost due to its cubic-time Newton-Schulz orthogonalization step. When weights are sharded, communication overhead compounds this computational cost, eroding the benefits of Muon in many settings. We present Dion3, a revision of Muon that targets this overhead at every level of the stack. Our Gram Newton-Schulz algorithm reduces the FLOP cost of orthogonalization, our CuteDSL kernels accelerate it by exploiting symmetry, and our megabatching strategy reduces communication overhead. Moreover, we propose a simple change to the update rule that cuts costs even further: selecting only a fraction of the momentum matrix's rows to orthogonalize at each step. This update rule improves on Dion (another "compressed" version of Muon), in both speed and performance. Overall, Dion3 matches or improves on the loss achieved by Muon but reduces optimizer step time by up to 6x. Dion3 is available via the dion package (this https URL) as a drop-in replacement for Muon.

---


### 88. [A Local Sinkhorn Framework for Conditional Distribution Reconstruction of Multidimensional Random Fields](https://arxiv.org/abs/2608.11613)

**<font color=#1a73e8>作者：</font>** Mingtao Xia, Qijing Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a local Sinkhorn divergence framework for conditional distribution reconstruction of multidimensional random fields. By utilizing the debiased Sinkhorn divergence, our proposed approach develops a differentiable and computationally efficient local distribution matching objective to train stochastic neural networks (SNNs). Furthermore, we establish theoretical generalization error estimates for our local Sinkhorn divergence framework, which explicitly characterizes the trade-off between approximation bias and statistical efficiency controlled by the regularization parameter and reveals how our proposed local Sinkhorn divergence loss function can be efficiently applied to learning multidimensional random field models. The proposed framework provides a scalable alternative to exact local optimal transport for conditional distribution reconstruction, offering a practical compromise between geometric fidelity, statistical efficiency, and computational scalability for uncertainty quantification and probabilistic scientific machine learning. Through various numerical examples, we compare our proposed local Sinkhorn divergence framework with other loss functions to train SNNs and with other machine-learning-based uncertainty quantification frameworks, demonstrating that the proposed local Sinkhorn divergence framework achieves an effective balance between reconstruction accuracy and computational efficiency while maintaining good scalability for multidimensional stochastic systems.

---


### 89. [KANResDiff: Learning Local Residual Diffusion via Kolmogorov-Arnold Network for Ambiguous Medical Image Segmentation](https://arxiv.org/abs/2608.11617)

**<font color=#1a73e8>作者：</font>** Fanding Li, Chenglin Wang, Xiangyu Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ambiguous medical image segmentation aims to provide a series of diverse but plausible segmentation hypotheses. However, existing methods introduce stochasticity in a fixed and pre-defined manner, failing to form a progressive semantic modeling process. To address these challenges, we propose KANResDiff to learn local residual diffusion with Kolmogorov-Arnold Network, thereby assigning distinct roles across stages for ambiguity modeling. Specifically, we propose Independent Time Encoding that offers spline-based time embeddings instead of linear ones from MLPs, which enhances the independence across inference stages and assigns progressive semantic roles to different stages. We propose Residual Schrodinger Bridge that injects deterministic residual prior with learnable weights by constructing local Schrodinger Bridge instead of following manually settings, achieving a flexible deterministic-stochastic interaction and stage-aware ambiguity modeling thanks to local optimal diffusion path. Extensive experimental results on two public datasets demonstrate that KANResDiff achieves SOTA performance on GED and HM-IoU, with maximum improvements of 16.8% and 7.7%, respectively, while maintaining competitive performance on the MDM metric. Source code is available at this https URL.

---


### 90. [Generative Video Compression Based on Hierarchical Referencing](https://arxiv.org/abs/2608.11618)

**<font color=#1a73e8>作者：</font>** Daowen Li, Ding Ding, Zifu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based generative video compression has emerged as a promising paradigm to improve perceptual quality, where latent frames are required to be encoded efficiently while serving as denoising conditions. However, existing methods neither carefully design reference and quality structures during latent coding nor account for the impact of frame-level quality variation on denoising procedure, which limits coding efficiency and aggravates artifact propagation during generative reconstruction. In this paper, we propose GVCHR, Generative Video Compression based on Hierarchical Referencing. The key idea is to organize latent frames hierarchically, where the selected high-quality references benefit both latent coding and generative reconstruction. In latent coding, GVCHR couples a hierarchical reference structure with a hierarchical quality structure, assigning more bits to lower-layer frames that are reused more frequently as references. Built on this design, we introduce Hierarchical Temporal Context Mining to exploits complementary short- and long-term temporal context for effective latent coding. In generative reconstruction, the coding-side hierarchy is incorporated into a Hierarchical Attentive Adapter which is attached to a video diffusion transformer. This adapter uses hierarchical attention to restrict each latent frame to attend only to the same- or lower-layer references, thereby reducing artifact propagation during denoising. Experiments validate GVCHR on multiple benchmarks. Compared with the previous state-of-the-art method, GVCHR achieves 50.5% and 54.0% BD-rate gains in terms of LPIPS and DISTS, respectively, while also delivering clearly improved visual quality.

---


### 91. [Easper: An Accessible ASR Pipeline for Language Documentation](https://arxiv.org/abs/2608.11629)

**<font color=#1a73e8>作者：</font>** Aso Mahmudi, Ting Dang, Ekaterina Vylomova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio transcription is a critical bottleneck in language documentation. While multilingual Automatic Speech Recognition (ASR) models like Whisper offer solutions, field linguists often lack the expertise to utilise them. We present Easper, an open-source, no-code workflow enabling linguists to iteratively fine-tune ASR models via cloud resources directly from ELAN annotations. Deploying ASR also raises a cold start problem: deciding which recordings to transcribe first to bootstrap an accurate model. Using Easper, we evaluate transcription prioritisation strategies on three Vanuatu languages (Bislama, Nafsan, Nguna). We fine-tune models by recording session, comparing Character Error Rate trajectories when prioritising acoustic cleanliness versus linguistic richness. We demonstrate that prioritising lexically rich narratives and increasing acoustic-phonetic repetition, even in noisy environments, leads to faster improvements in transcription quality.

---


### 92. [Beyond Memory: A Transactional Continuity Kernel for Long-Lived AI Agents](https://arxiv.org/abs/2608.11632)

**<font color=#1a73e8>作者：</font>** Jun He, Deying Yu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Persistent AI agents accumulate versioned state across long horizons, but storage retention alone does not identify authoritative state. Without an explicit control plane, unmediated updates by models, tools, and background workers risk stale overwrites, un-audited exposures, and self-authorizing privilege escalation. We argue that agent state governance is an infrastructural activation problem, defining continuity as an unbroken, authorized lineage of accepted branch heads. We present the Continuity Kernel (CK), an activation contract that decouples off-commit candidate evaluation from atomic state activation. Untrusted components propose typed changes against an exact predecessor head or typed absence. A short activation transaction revalidates ownership, pre-state authority, freshness, and effect uniqueness, recording one stable disposition (Commit, Reject, Quarantine, or Defer). Only Commit atomically advances the branch head and installs the complete accepted unit (state, authority, lineage, effects, outcome, and receipt). A bounded executable model verifies the protocol across 2,808,230 reachable states and 5,526,474 state-changing transitions with zero invariant violations.

---


### 93. [CAM-Guided Saliency Cutout and Image-Based Malware Classification](https://arxiv.org/abs/2608.11634)

**<font color=#1a73e8>作者：</font>** Yasaman Ebrahimi, Martin Jurecek, Mark Stamp  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dropout regularization is commonly used to reduce overfitting by removing parts of a neural network during training. For Convolutional Neural Networks (CNN), cutouts serve a somewhat analogous purpose. Cutouts can be implemented as data augmentation: the original training image is retained, and additional copies are created with regions removed. In this chapter, we test whether cutout placement can be improved by using High-Resolution Class Activation Mapping (HiResCAM). We compare four controlled training conditions: no cutout, standard random cutout, low-saliency cutout, and high-saliency cutout. We experiment using grayscale malware images from the RawMal-TF dataset (17 families with~1,000 samples per family), and for comparison to natural images, we experiment with the well-known CIFAR-100 dataset. All experiments are based on ResNet18 with~100 training epochs. For the cutout experiments, we test cutout areas of~5\%, 10\%, 20\%, and~30\%, and we consider~$M\in\{4,8}$ augmented copies per original training image. The RawMal-TF results are slightly worse for all three cutout cases (random, high and low saliency) as compared to no cutouts. In contrast, our CIFAR-100 experimental results improve slightly under low-saliency cutout. These results suggest that the value of saliency-guided cutout is domain dependent, and that malware images should not be treated as equivalent to natural images.

---


### 94. [VisPuzzle: Task-Aware Composite Visualization Construction](https://arxiv.org/abs/2608.11635)

**<font color=#1a73e8>作者：</font>** Zheng Wang, Zhiyang Shen, Lingyun Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Compositing multiple visualizations into a coherent whole remains challenging due to the vast design space and the need to balance the coverage of task-relevant data insights (e.g., trends and outliers), perceptual clarity, and aesthetic quality. In this paper, we present VisPuzzle, a task-aware method that formulates visualization composition as a stepwise search problem over a composition graph. In this graph, nodes represent either data composition operations (e.g., union, join) or visual composition operations that determine component relationships, spatial arrangements, or component proportions, and edges encode feasible transitions between operations. We employ Monte Carlo Graph Search to efficiently identify high-quality composition candidates from this graph, guided by a reward function that balances task relevance, perceptual effectiveness, and aesthetic coherence. A use case and a user study show that the top-ranked candidates produced by VisPuzzle align closely with human judgments of composition quality, demonstrating its utility in supporting principled and scalable visualization composition.

---


### 95. [Transferable Above-Ground Biomass (AGB) Estimation Model from Multi-Sensor Data with Sparse Field Calibration](https://arxiv.org/abs/2608.11638)

**<font color=#1a73e8>作者：</font>** Pann Thinzar Seint, Bryan Atwood, Subas Chhatkuli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatially continuous quantification of forest above-ground biomass (AGB) is what makes carbon accounting credible and mitigation strategies actionable. While field inventories provide high localized accuracy, they are spatially sparse; conversely, spaceborne LiDAR from the Global Ecosystem Dynamics Investigation (GEDI) offers broad biomass samples but lacks spatial continuity and systematic underestimation of high-biomass forests. This paper presents an operational framework centered on a single globally trained convolutional neural network (CNN) that is seamlessly adapted to each new landscape through a lightweight empirical field-calibration workflow. The global model combines optical (Sentinel-2), C-band SAR (Sentinel-1), L-band SAR (ALOS-2 PALSAR-2), and terrain (DEM) data. It is trained once against GEDI Level-4A biomass reference data spanning multiple regions and both wet and dry seasons so that it learns the persistent woody-structure rather than a single-date appearance. To avoid retraining for every landscape, the framework applies a small number of local field plots to fit a scale-and-bias correction that aligns the global prediction with ground truth in each region. The pipeline harmonizes sensor data onto a shared 10 m grid, derives vegetation indices and polarimetric ratios, computes per-band normalization stats, and trains the CNN with a hybrid log-domain SmoothL1 with RMSE loss for skewed biomass distribution. On held-out validation the global GEDI-based model achieved R^2 approximately 0.78 and RMSE approximately 22 Mg/ha. A subsequent field calibration combining Random Forest fine-tuning under a 10-fold cross-validation eliminates localized regional biases. This improves local validation performance to R^2 approximately 0.82 and reduces RMSE to approximately 15 Mg/ha, outperforming both the uncalibrated global model and the ESA CCI Biomass product against field plots.

---


### 96. [Robustness of AI-Art Detectors under Generator Shift](https://arxiv.org/abs/2608.11643)

**<font color=#1a73e8>作者：</font>** Shivank Singh Thakur, Meien Li, Mark Stamp  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image generative models have advanced rapidly, with modern Diffusion Transformer architectures producing images that are increasingly difficult to distinguish from human-created artwork. This development has raised significant concerns regarding copyright protection, misinformation, fraud, impersonation, and the authenticity of digital content. Most AI-art detectors are trained and evaluated on the same generator family, leaving robustness to newer architectures underexplored. In this chapter, we analyze generator shift based on a Stable Diffusion 3.5 Medium (SD3.5m) artwork dataset spanning ten art styles through reverse prompting of held-out human artwork samples. Five detectors are trained on U-Net-based latent diffusion artwork and evaluated in a zero-shot cross-generator setting on the SD3.5m dataset. Deep learning models perform strongly in-distribution but degrade under generator shift, misclassifying many SD3.5m images as human while human false positives remain low. The CLIP ViT-L/14 model performs best overall, while Grad-CAM analysis reveals weaker and more diffuse activation on false negatives. These findings highlight a generalization gap in current AI-art detectors and motivate the development of detectors as one component of a layered defense that remains reliable across rapidly evolving generative architectures.

---


### 97. [Cloak of Invisibility: Real-Time Privacy-Preserving Volumetric Video Streaming](https://arxiv.org/abs/2608.11645)

**<font color=#1a73e8>作者：</font>** Hossein Khalili, Philip Do, Alexander Vilesov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Volumetric video streaming turns privacy into a 3D, multi-view problem. Unlike ordinary video, where sensitive content can often be redacted frame by frame, RGB-D volumetric pipelines capture people, rooms, and personal objects from multiple cameras and fuse them into a shared 3D representation. A private object missed in one view, or only partially removed before fusion, can therefore reappear in the reconstructed scene. This creates a privacy challenge for 3D telepresence, education, entertainment, and immersive applications: private content should be removed before raw visual and geometric data leave the camera side, while the public part of the scene should remain useful for real-time reconstruction. Existing volumetric streaming systems mainly optimize reconstruction, data movement, and latency, while privacy-preserving vision methods are designed for single-camera, single-frame images and do not directly address calibrated multi-view RGB-D fusion. We present InViStream, a real-time "privacy-from-source" system designed for this setting. InViStream addresses three challenges in volumetric capture: private objects may appear differently across views, RGB masking alone can leave geometric privacy leakage in depth, and public/private instances of the same class must be separated consistently before cloud-side fusion. To address these challenges, InViStream combines object detection with depth-aware masking, propagates public/private decisions across calibrated views, and fuses only sanitized point clouds. We evaluate InViStream on synthetic and real RGB-D scenes, including offices, conference rooms, living rooms, and settings with multiple public and private people and objects. InViStream achieves synthetic Dice/Recall of 0.799/0.891 and real Dice/Recall of 0.792/0.908, with synthetic SSIM above 0.98 and real-time streaming above 30 FPS.

---


### 98. [Hybrid-LUT: Channel-Aware Hybrid Lookup Table and Filtering for Efficient Image Denoising](https://arxiv.org/abs/2608.11646)

**<font color=#1a73e8>作者：</font>** Zhilin Ai, Boyu Li, Sidi Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lookup table (LUT)-based image denoising methods have attracted increasing attention due to their high efficiency and hardware-friendly properties. However, existing RGB-LUT approaches require three identical LUTs to process RGB channels in parallel, resulting in large on-chip SRAM consumption. A simple alternative is to apply LUT processing only to the luminance (Y) channel in the YUV color space to reduce memory usage. However, this naive strategy leads to degraded restoration quality, since ignoring the chrominance (UV) channels introduces color distortion and residual artifacts. In this work, we propose Hybrid-LUT, a YUV-based asymmetric channel-processing framework that combines LUT and filtering in a unified design. Specifically, a multi-band LUT branch with pixel-level weight fusion is applied to the Y channel to recover fine textures, while lightweight filtering is used for the UV channels to maintain color consistency. This design reduces LUT storage by two-thirds compared with RGB-LUT methods while maintaining the same runtime throughput. Extensive experiments show that Hybrid-LUT achieves state-of-the-art (SOTA) performance across multiple benchmarks with only 421 KB of storage. In particular, our method surpasses existing LUT-based denoising approaches by at least 0.63 dB CPSNR on real-world datasets, demonstrating its effectiveness for image denoising on resource-constrained edge devices. The project is available at this https URL .

---


### 99. [Is Per-Agent Policy Composition Safe? Rethinking Successor-Feature Transfer in Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2608.11658)

**<font color=#1a73e8>作者：</font>** Zijian Zhao, Sen Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many reinforcement learning systems, from fleet management to traffic signal control, must serve an objective that changes dynamically after deployment, and retraining a policy for each new objective is prohibitively expensive. For a single agent, this problem is well understood: successor features with generalized policy improvement, together with their universal extension, recombine a library of learned policies into a policy for any new objective, with a guarantee that the result is never worse than any policy in the library. However, multi-agent transfer has received far less attention, and the common practice of letting each agent recombine its own library independently inherits the recipe but not the guarantee. We prove that this independent composition can produce joint behavior strictly worse than every policy in the library, because recombining teammates changes the environment each agent faces and invalidates the values it relies on, a failure with no single-agent counterpart. We further show that the only unconditionally safe fixed rule is synchronized composition, which moves the whole team to one jointly trained policy but cannot serve objectives that assign different goals to different agents. To attain safety and flexibility at once, we propose MA-USFA, a hierarchical method with two layers: a lower layer of universal successor feature approximators that predicts each agent's successor features while conditioned on its teammates' objectives, and an upper composer that selects, across agents, which library entry each agent should follow and supplies the cross-agent correction a per-agent value cannot represent. Trained once over the distribution of objectives, it is applied at deployment with no per-task adaptation.

---


### 100. [FunnelCausalNet: Funnel-aware Joint Conversion-Revenue Uplift for Multi-tier Coupon Allocation](https://arxiv.org/abs/2608.11675)

**<font color=#1a73e8>作者：</font>** Yu Zhang, Zhihan Wang, Guanlin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coupon campaigns seek to lift both conversion and revenue, but gross merchandise value (GMV) follows a deterministic funnel from conversion to conditional order value and is zero-inflated and heavy-tailed. We propose FunnelCausalNet, an uplift estimator coupling a binary conversion head with a nonnegative conditional-value head through $\mu_{\mathrm{gmv}}=\mu_{\mathrm{conv}}\mu_{\mathrm{val}}$. Under explicit RCT, support, rate-gap, and cross-head covariance-control assumptions, an idealized leading-order MSE comparison identifies a regime in which funnel composition can reduce pointwise variance; this is a heuristic, not a guarantee for the shared-representation neural model. The estimator is paired with marginal split-conformal CATE summaries, combined through a Bonferroni union as audit bands, and a Lagrangian budgeted allocator using RCT-anchored estimates for subsidy-aware ROI accounting. On semi-synthetic multi-tier Criteo-MT7, FunnelCausalNet's mean AUUC_GMV is within one seed standard deviation of the leading feature-interaction baseline among eleven baselines, while a controlled ablation reduces GMV effect error versus direct GMV regression by 18--48% across tested zero-inflation regimes. On de-identified industrial Hotel-Coupon RCT logs with about 4.9 million hold-out exposure records per seed, expected-outcome evaluation sweeps full LP frontiers; FunnelCausalNet has the best seed-averaged mean DeltaROI at all seven correlated anchors from 10% to 60%, which we treat as descriptive frontier consistency rather than independent significance. On sparse binary-spend public benchmarks, revenue-focused rankers can dominate uplift-curve proxies, defining an explicit regime boundary.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-202](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
