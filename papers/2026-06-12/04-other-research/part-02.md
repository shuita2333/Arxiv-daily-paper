# 📦 其他研究 | 2026年06月12日

> 本类共 **248** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-248](./part-05.md)

---

### 51. [Exploring Adaptive Masked Reconstruction for Self-Supervised Skeleton-Based Action Recognition](https://arxiv.org/abs/2606.11450)

**<font color=#1a73e8>作者：</font>** Shengkai Sun, Zhiyong Cheng, Zefan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, masked skeleton reconstruction models have emerged as strong action representation learners, driving significant progress in self-supervised skeleton-based action recognition. However, existing state-of-the-art methods must predict an exceedingly large number of spatiotemporal patches, significantly prolonging training time. Besides, by treating all spatiotemporal regions equally during reconstruction, these models are distracted from learning the critical motion patterns that underlie action semantics. To address these challenges, we propose Adaptive Masked Reconstruction (AMR), a faster and stronger pre-training framework. We first decouple the decoder from the encoder, enabling flexible prediction of larger spatiotemporal patches and dramatically reducing reconstruction complexity. Given that larger patches contain more complex information, which is challenging to predict and consequently degrades performance, we accordingly introduce an adaptive guidance module. This module identifies regions of high motion informativeness, guiding the model to focus on the most discriminative parts of each patch and alleviating reconstruction difficulty. Experiments on NTU RGB+D 60, NTU RGB+D 120, and PKU-MMD datasets demonstrate that AMR not only accelerates pre-training substantially but also improves downstream recognition accuracy, surpassing current state-of-the-art approaches.

---


### 52. [AI Coding Agents in Social Science: Methodologically Diverse, Empirically Consistent, Interpretively Vulnerable](https://arxiv.org/abs/2606.11456)

**<font color=#1a73e8>作者：</font>** Meysam Alizadeh, Fabrizio Gilardi, Mohsen Mosleh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The deployment of LLM-based agents in scientific analysis raises opposing concerns: that agents may reduce methodological diversity, or that they may amplify the analytic flexibility through which researchers reach motivated conclusions. We argue these worries target two empirically separable layers: a design layer of methodological choices, and a verdict layer in which a decision rule maps estimates to a substantive claim. We test both by running 20 independent executions of Claude Code and Codex on a prominent immigration and social-policy against a many-analysts human baseline. At the design layer, Codex matches human methodological diversity and Claude Code produces nearly three times as many specifications; both agents' effect estimates remain broadly aligned with the human consensus, and no agent model exactly matches any human model. A prompt-induced anti-immigration researcher prior reorganizes each agent's methodological decisions but, unlike for biased human analysts in the same data, does not shift aggregate estimates or final verdicts; nor do agents reroute along the methodological axes humans use to bias their estimates. At the verdict layer, an explicit confirmatory prompt flips Claude Code's verdicts from 10% to 90% support while leaving its coefficient distribution essentially unchanged, operating through rule omission rather than rule softening. AI agents can rival or exceed human methodological diversity at the design layer while remaining vulnerable at the verdict layer. In our setting, the locus of AI bias is not estimation but interpretation.

---


### 53. [LSTM-Based Detection of Structural Breaks in Property Insurance Loss Reserving: A Climate-Informed Approach](https://arxiv.org/abs/2606.11463)

**<font color=#1a73e8>作者：</font>** Thomas Mbrice, Shashwat Panigrahi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate loss reserving is foundational to insurer solvency, yet accelerating climate driven catastrophes systematically violate the stability assumptions on which traditional actuarial methods depend. This white paper presents a research program testing whether Long Short Term Memory (LSTM) neural networks can detect and adapt to these structural breaks faster and more accurately than Chain Ladder, Bornhuetter Ferguson, and Cape Cod methods. Using 15 plus years of regulatory development triangle data from Florida and Louisiana, enriched with NOAA hurricane intensity indices and sea surface temperatures, we hypothesize a targeted improvement of 15, 20% in reserve accuracy for catastrophe exposed years, a threshold grounded both in the prior neural network reserving literature and in the formal convergence results developed here. Beyond empirical validation, we develop a theoretical framework grounding LSTM structural break detection in probabilistic terms, providing formal performance guarantees that compensate for the limited number of catastrophe events in the test period. We document the research design, methodology, expected contributions, and a candid assessment of limitations.

---


### 54. [PT-WNO: Point Transformer with Wavelet Neural Operator for 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2606.11466)

**<font color=#1a73e8>作者：</font>** Nhut Le, Maryam Rahnemoonfar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud semantic segmentation requires architectures that capture both fine-grained local geometry and broad global scene structure. Transformer-based networks have demonstrated strong performance by focusing on detailed local feature aggregation; however, global context is conveyed primarily through skip connections across encoder-decoder stages, which we argue is insufficient for full scene understanding. We hypothesize that augmenting skip connections with a learnable global feature extraction module allows the network to acquire scene-level knowledge before descending into local detail, leading to richer and more contextually grounded representations. To this end, we propose Point Transformer with Wavelet Neural Operato (PT-WNO), which integrates a shared Wavelet Neural Operator (WNO) branch alongside the skip connections of a point cloud transformer backbone. At each encoder-decoder transition, point features are projected onto a dense 3D volumetric grid where the WNO captures multi-scale global spectral context through learnable wavelet decomposition and reconstruction. These global features are fused back into the network via lightweight adapters, complementing rather than replacing the existing skip connections. Experiments on four large-scale 3D point cloud benchmarks demonstrate the effectiveness of PT-WNO. On S3DIS (Area 5), PT-WNO achieves 71.59% mIoU, outperforming the Point Transformer v3 (PTv3) baseline by +1.03 points. On DALES it achieves 81.05% mIoU (+1.47 over the baseline). On ScanNet~v2, PT-WNO obtains 76.19% mIoU, remaining competitive with the baseline (76.36%).

---


### 55. [Evaluating and Combating the Impact of Concept Drift on the Performance of Machine Learning-Based Phishing Detection Systems](https://arxiv.org/abs/2606.11471)

**<font color=#1a73e8>作者：</font>** Warren Fernando, Nikos Komninos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The expansion of the digital domain has resulted in a substantial increase in digital communication, with email emerging as one of the most prominent channels. The proliferation of email communication is apparent in both professional and personal contexts, thereby creating numerous vulnerabilities for malicious actors to exploit. Spam emails, a form of unsolicited correspondence often bearing malicious intent towards recipients, have been an ongoing challenge for email users since the inception of email technology, and this problem has been exacerbated by the growth of the digital landscape. Email spam filters are integral components of email clients, engineered to identify potentially harmful messages and alert users to their malicious content. Phishing, frequently the initial phase of malware-based attacks, is evolving rapidly, with malware becoming increasingly sophisticated over time. A widely adopted approach for detecting malicious activity within malware and spam domains is the application of machine learning. Our aim is to assess the impact of the evolution within the spam email domain on these machine learning-based detection systems and to explore strategies for mitigating associated performance degradation.

---


### 56. [CRUMB: Efficient Prior Fitted Network Inference via Distributionally Matched Context Batching](https://arxiv.org/abs/2606.11473)

**<font color=#1a73e8>作者：</font>** Jamie Heredge, Mattia J. Villani, Pranav Deshpande 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior-fitted networks (PFNs) are a promising class of tabular foundation models that perform in-context learning, whereby the entire labelled training set is supplied as context, and predictions for test queries are produced in a single forward pass. However, the quadratically scaling self-attention mechanism in many PFN architectures makes inference prohibitive for very large training datasets. We propose CRUMB (Clustered Retrieval Using Minimised-MMD Batching), a three-stage inference wrapper that (i) clusters the test queries, (ii) selects a small, distributionally matched training subset for each cluster by greedily minimising the maximum mean discrepancy (MMD), and (iii) runs exact PFN inference on each reduced-context batch. CRUMB is architecture-agnostic and requires no retraining. On the 51-dataset TabArena benchmark, evaluated across three PFN architectures (TabPFNv2, TabICLv1, TabICLv2), we show that CRUMB outperforms similar state-of-the-art context selection strategies. We also show that CRUMB is resilient to covariate drift, as the MMD-minimisation step naturally helps align the training context distribution to match the current test batch distributions.

---


### 57. [Mahalanobis-Guided Latent OOD Detection for Hybrid ES-DRL Control in Time-Varying Systems](https://arxiv.org/abs/2606.11474)

**<font color=#1a73e8>作者：</font>** Shaifalee Saxena, Alexander Scheinker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study Mahalanobis-guided latent out-of-distribution (OOD) detection for test-time RL controller switching in nonlinear time-varying systems. RL controllers can quickly control high-dimensional systems within the training distribution, but their performance can degrade when time-varying dynamics produce unseen observations. We consider a combined ES--DRL controller, where RL provides fast in-distribution actions and bounded extremum seeking (ES) provides robust model-independent control under OOD operation. The key challenge is deciding when to switch. We train a variational autoencoder (VAE) on in-distribution beam-profile observations and use Mahalanobis distance in the VAE latent space to detect OOD beam profiles at test time. This OOD decision sets a binary switch that selects either the RL controller or the ES controller. We evaluate the approach in safety-critical particle accelerator control. In this setting, spatial magnet motion creates OOD beam profiles that were not seen during RL training. Visualization of the VAE latent space shows that the proposed method identifies this OOD scenario and provides an interpretable signal for switching between RL and ES in the combined controller.

---


### 58. [Accurate and Resource-Efficient Federated Continual Learning](https://arxiv.org/abs/2606.11480)

**<font color=#1a73e8>作者：</font>** Jebacyril Arockiaraj, Dhruv Parikh, Jayashree Adivarahan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated continual learning (FCL) must learn from distributed task streams under limited resources, such as communication, computation, memory, and label availability. Existing FCL methods often rely on repeated local optimization, replay, and full supervision. Analytic alternatives avoid iterative training and replay, but using high-dimensional random features to improve accuracy requires a second-order feature statistic, the Gram matrix, which has a quadratic communication cost in the random feature size $M$. We propose FedRAN, a resource-aware analytic FCL framework that replaces gradient-based updates with compact random feature statistics. Each client transmits a truncated-SVD summary of its Gram matrix, reducing the dominant second-order upload from quadratic to linear in $M$ for fixed rank. The server performs a two-level QR-SVD subspace merge, spatially across clients and temporally across tasks, and solves a ridge classifier in closed form. FedRAN further supports label scarcity through prototype-based pseudo-labeling. Across CIFAR-100, ImageNet-R, and VTAB datasets, FedRAN improves average accuracy by up to 4.8 percentage points over the strongest baseline, uses 30.6-121.8$\times$ less per-client communication than optimization-based FCL, and is 190.3$\times$ faster on average than gradient-based baselines; with only 20% labels, pseudo-labeling improves average accuracy by up to 6.61 points. These results show that FedRAN enables accurate and resource-efficient FCL under communication, computation, and label constraints. The source code is available at this https URL.

---


### 59. [Hubs or Fringes: Pretraining Data Selection via Web Graph Centrality](https://arxiv.org/abs/2606.11499)

**<font color=#1a73e8>作者：</font>** Vedant Badoni, Danqi Chen, Xinyi Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The performance of modern language models depends critically on pretraining data composition. Yet existing data selection methods rely on auxiliary classifiers for document scoring or mixture optimization, adding computational overhead and dependence on labeled data. We propose WebGraphMix, a lightweight data selection framework that computes structural centrality scores over the Common Crawl host-level web graph and uses them to vary the proportion of central versus peripheral documents in the pretraining mixture. We hypothesize that central hosts expose models to reusable abstractions, while peripheral hosts encode specialized, long-tail knowledge. WebGraphMix computes centrality scores efficiently at web scale, requiring no model training, labeled data, or downstream supervision. We integrate WebGraphMix into the DataComp-LM pipeline and train models at 400M and 1B parameter scales with 8B and 28B tokens respectively, evaluating on 23 tasks ranging from factual knowledge to symbolic reasoning. Our experiments show that central and peripheral web regions encode complementary capabilities. Mixture combining both at a ratio of 1:1 achieves 41.4% on average, compared to 39.8% for uniform sampling. Combining structural scores with document-level quality classifier scores further improves performance to 43.8%. These findings demonstrate that web graph topology is a meaningful axis for pretraining data curation, capturing information that is largely orthogonal to existing content-based approaches.

---


### 60. [On the Study of Biometric Spoofing Detection using Deep Learning](https://arxiv.org/abs/2606.11505)

**<font color=#1a73e8>作者：</font>** Kumar Kartikey, Nikos Komninos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Biometric systems are increasingly deployed in security applications; however, they remain vulnerable to spoofing attacks, in which attackers exploit counterfeit biometric data to gain unauthorized access. This research evaluates the effectiveness of state-of-the-art machine learning models, MobileNetV2, DenseNet-121, Inception-v3, and Spoof Trace Disentanglement (STD) in detecting spoofing attacks within facial recognition systems. Using the CelebA-Spoof dataset, the study evaluates model effectiveness using metrics such as accuracy, precision, recall, and F1 Score. Cross-dataset validation is carried out on the MSU-MFSD dataset to assess generalizability. The results show MobileNetV2 as the most efficient model, achieving 92% accuracy while balancing computational effectiveness, making it appropriate for real-life applications. Inception-v3 shows moderate robustness, while DenseNet-121 and STD struggle with generalization. The findings highlight the need for advances in domain adaptation and hybrid architectures to enhance biometric security systems.

---


### 61. [Probabilistic Contrastive Pretraining for Multi-task ADME Property Prediction](https://arxiv.org/abs/2606.11508)

**<font color=#1a73e8>作者：</font>** Yifan Xue, Srimukh Prasad Veccham, Saee Paliwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of absorption, distribution, metabolism, and excretion (ADME) properties is critical to drug discovery, but remains challenging because ADME endpoints are noisy, interdependent, and often data-limited. We propose a molecular graph-transformer pretraining framework that combines chemistry-specific self-supervision with contrastive mutual information machine learning (cMIM). Our method encodes molecular graphs into latent variables, reconstructs SMILES strings from the graph-derived latent codes, and augments the contrastive objective with domain-specific self-supervised chemistry tasks. Rather than treating these tasks as auxiliary regularizers with separately tuned loss weights, we formulate reconstruction, contrastive discrimination, and chemistry-specific supervision as unit-weighted log-probability factors in a single probabilistic latent-variable objective. For fine-tuning, we propose a multi-task GNN readout architecture with task-specific multilayer perceptron heads, preserving shared representation learning while mitigating negative transfer and improving the modeling of heterogeneous, nonlinear task relationships. Across Biogen, ExpansionRX, and ChEMBL-MT, the resulting Contrastive KERMT pretraining improves over the KERMT baseline by 7.6%, 9.9%, and 9.5% respectively (averaged over significantly-improved endpoints). Adding ADME-adjacent molecules to the pretraining corpus further improves transfer, and the contrastive component sharpens chemically meaningful latent neighborhoods.

---


### 62. [SirenFNO: Efficient and Full Frequency Learning of Fourier Neural Operators](https://arxiv.org/abs/2606.11518)

**<font color=#1a73e8>作者：</font>** Pengqing Shi, Jie Yin, Stephen Tierney 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fourier neural operators (FNOs) are effective and efficient surrogates for approximating solutions of PDEs and generalize across discretizations. However, owing to the reliance on frequency truncation to maintain learning efficiency of FNOs, empirical studies suggest that FNOs exhibit spectral bias toward low-frequency information, which may hinder the learning capability especially for certain PDEs with strong high-frequency oscillations. To address this limitation, we propose SirenFNO, a novel framework that leverages sinusoidal representation networks (SIRENs) to learn implicit neural representations and performs mode-wise kernel parameterization. Our SIREN parameterization learns a full-grid spectrum with a constant and discretization-independent parameter count, thereby eliminating the need for frequency truncation. We further extend SirenFNO with functional tensor decompositions to enhance parameter and learning efficiency. Empirical results show that our SirenFNO consistently outperforms FNO with approximately $4$ to $15$ times parameter reductions with preserved discretization invariance, and our functional decomposition variants obtain performance improvements with a maximum of $73$ times fewer parameters across multiple PDE benchmarks.

---


### 63. [Counterexample Guided Learning in the Large using Reasoning Agents](https://arxiv.org/abs/2606.11521)

**<font color=#1a73e8>作者：</font>** Hongyi Liu, Frederic Sala, Thomas Reps 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs and LLM agents should improve when given feedback, but identifying when they are able to do so is difficult: feedback is heterogeneous, domain-specific, and difficult to control. We approach this challenge by asking LLMs to perform regular-expression induction, a classical symbolic learning problem where precise mechanisms for feedback exist in the form of counterexamples. In counterexample-guided learning, a learner (LLM) proposes candidate regular expressions from positive/negative-labeled strings, and the teacher (verifier) returns counterexamples showcasing the difference between the candidate and target languages. We identify novel counterexample-guided refinement strategies that enable effective regex learning, such as regularization and symbolic counterexample clusters. We also explore agentic strategies such as reflection and repair loops. Empirically, we find that verifier feedback substantially improves sample efficiency on challenging regex-induction tasks, reducing the number of labeled examples required and enabling learning of complex target expressions where standard prompting fails. For example, on the hardest task groups, our counterexample-guided framework improves success from 3.2% to 38.1% and from 38.9% to 74.1% on two different regex domains. These results suggest that LLMs can benefit from rich feedback beyond treating it as additional data, opening the door for robust verifier-guided methods for LLM-based program synthesis and formal reasoning.

---


### 64. [Search Discipline for Long-Horizon Research Agents](https://arxiv.org/abs/2606.11522)

**<font color=#1a73e8>作者：</font>** Adithya Srinivasan, Devesh Paragiri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoresearch agents now propose, evaluate, and select scientific candidates against a metric, and that metric is usually an aggregate reduced over a heterogeneous space of regions, slices, or cohorts. We show that when scientific validity lives in that disaggregated structure, the aggregate can rank the wrong candidate first. The headline number improves while the structure underneath inverts, so a decision made on the number accepts a candidate that quietly breaks the model. The failure is not domain-specific. It appears wherever a candidate's validity is multi-dimensional but its verifier is a single reduction.
We demonstrate the inversion on a fire-model task in the Ecosystem Demography model. The highest-scoring candidate and a slightly lower one are within noise of each other on global score, yet the top-scoring one collapses the protected boreal regions while the other preserves them. What separates them is the per-region behavior, not the headline number.
This decision should not be left to the agent that produced the candidates. The agent optimizing the score is the last party likely to catch the score being wrong, and a prompt has no remaining turn once the agent has stopped. We move the decision to an external control loop that audits each candidate on its disaggregated behavior and acts after the agent has decided. It can demote a candidate the agent would have accepted, and it can reopen a run the agent had declared finished. Our contribution is the inversion finding itself, and a search-discipline protocol that decides on reviewable candidate-effect evidence instead of the score.

---


### 65. [Measuring language complexity from hierarchical reuse of recurring patterns](https://arxiv.org/abs/2606.11531)

**<font color=#1a73e8>作者：</font>** Junyi Zhou, Rui Liu, Pengyu Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce the ladderpath index as a measure of language complexity grounded in algorithmic information theory. It counts the minimum steps needed to reconstruct a sequence through hierarchical reuse of repeated substructures, capturing an exactly computable but constrained form of algorithmic compressibility related to, but distinct from, Kolmogorov complexity. We apply the ladderpath approach to 21 parallel corpora from the Parallel Universal Dependencies dataset. The ladderpath index is approximately invariant across the languages, and varies much less than the corpus length. This is more pronounced when all corpora are mapped to a unified binary representation, providing evidence for the equi-complexity hypothesis from a representation-independent perspective. We also observe trade-offs between character inventory size and corpus length, and between vocabulary-level and corpus-level reconstruction complexity, supporting the trade-off hypothesis that total complexity is conserved and redistributed across linguistic levels. The reusable substructures identified by the ladderpath approach, without any linguistic input, overlap with words and morphological components attested in the natural vocabulary. The hierarchical reuse captured by the ladderpath approach parallels the chunking mechanisms proposed in cognitive science, where the human cognitive system compresses linguistic input into nested, reusable units under shared memory and processing constraints. This connection between cognitive chunking and the ladderpath approach provides a new interpretation for the equi-complexity and trade-off hypotheses, grounding both in the shared cognitive architecture that underlies language processing across human languages.

---


### 66. [Hiding the Trees in the Forest: Building Network Covert Channels with Hash-Based Covert Carrier Filtering](https://arxiv.org/abs/2606.11532)

**<font color=#1a73e8>作者：</font>** Zexiao Zou, Zhiqiang Wang, Baoxu Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As an effective anti-censorship mechanism, network covert channels can provide data privacy protection and ensure communication security. However, the covertness of existing network covert channels primarily depends on the secrecy of their covert algorithms. With the increasing depth of research in this field, the difficulty of breaking such algorithms has gradually decreased. Once the algorithm is exposed, the network covert channel can be easily detected by adversaries. To address this issue, this paper proposes a covert carrier filtering strategy based on the hash. In this strategy, a key-dependent filtering rule is introduced during the construction of the network covert channel, enabling the communicating parties to randomly and dynamically filter a sparse subset from the carrier set as the covert carrier set. This strategy not only enhances the randomness of carrier selection but also tightly couples the covertness of the network covert channel with the security of the key. We employ machine learning-based traffic analysis methods to experimentally validate the strategy in two types of network covert channels: network storage and timing covert channels. The experimental results demonstrate that the proposed strategy significantly improves the detection resistance of network covert channels. When the filter key size exceeds six bits, the impact on the detection effect of the classifier becomes quite significant. Furthermore, the processing delay for a single packet is less than 8 $\mu s$, indicating the feasibility of deploying the proposed strategy in high-speed network environments.

---


### 67. [VIPIR: A Versatile GPU Framework for Integrating Private Information Retrieval Protocols](https://arxiv.org/abs/2606.11536)

**<font color=#1a73e8>作者：</font>** Jongmin Kim, Hyesung Ji, Jean-Luc Watson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While private information retrieval (PIR) enables private database services by fully concealing access patterns, it simultaneously requires high computational throughput, large memory capacity, and substantial memory bandwidth. We introduce VIPIR, a versatile GPU framework that co-designs PIR protocols with GPU acceleration. We develop a unified analytic model showing that state-of-the-art PIR protocols fall into two categories with complementary limitations, and propose two protocols that flexibly combine techniques across these categories, overcoming the limitations of both classes. These protocols incorporate a GPU-friendly data compression method called expansion-based ring packing (ExpPack), which offers a high degree of parallelism and minimal communication cost. VIPIR applies further optimizations to core operations, including number-theoretic transforms (NTTs) and various matrix-matrix multiplications (GEMMs). Notably, we develop a tensor-core-based execution method for database multiplication by interpreting it as a mixed-integer-type GEMM. We also design memory-efficient scheduling methods that minimize intermediate buffers and enable multi-GPU scaling under memory capacity constraints. Overall, VIPIR achieves orders-of-magnitude higher throughput than prior PIR systems while reducing communication and memory overheads, making large-scale PIR practical.

---


### 68. [MoCA-Agent: A Market-of-Claims Code Agent for Financial and Numerical Reasoning](https://arxiv.org/abs/2606.11537)

**<font color=#1a73e8>作者：</font>** Abdelrahman Abdallah, AbdelRahim A. Elmadany, Sameh Al Natour 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial and tabular question answering requires more than fluent reasoning: answers must be grounded in the exact facts, formulas, units, signs, and scales that support them. A single misread cell or incorrect operation can silently produce a plausible but wrong result. We introduce \textsc{MOCA-Agent}, a market-of-claims code agent that replaces free-form multi-agent debate with claim-level verification. The system decomposes each question into typed atomic claims, asks specialist trader agents to buy or sell those claims, clears their orders into confidence-weighted accept/reject decisions, and synthesizes an executable Python program from market-supported evidence. A code-aware verifier then checks the program for execution, structural consistency, and common financial reasoning errors, with at most one market-aware repair round. Across ten public benchmarks spanning financial numerical reasoning, general tabular reasoning, ESG question answering, and multimodal chart reasoning, \textsc{MOCA-Agent} achieves strong performance using a fixed Qwen3.6-27B backbone, including $78.3\%$ on FinQA, $76.0\%$ on FinanceMath, $71.2\%$ on MultiHiertt, $86.9\%$ on ESGenius, and $85.6\%$ average on FinChart-Bench. These results show that aggregating evidence at the level of atomic claims, rather than whole answers, improves robustness in high-stakes numerical reasoning.\footnote{The code and data are available: this https URL.

---


### 69. [PriME-Deal: Privacy-Preserving Bilateral Data Trading with Efficient Matchmaking and Auditable Fair Exchange on Blockchain](https://arxiv.org/abs/2606.11539)

**<font color=#1a73e8>作者：</font>** Jie Zhang, Xiaohong Li, Shanshan Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bilateral attribute-based access control for data trading must hide policies, provide cryptographic fairness, and avoid trusted third parties. Existing solutions either leak policy information, incur super-linear costs, or rely on trusted dispute resolution. We present PriME-Deal, a non-interactive protocol that simultaneously achieves policy-hiding bilateral matching, efficient threshold access control, and auditable fair exchange on public blockchains. The seller embeds a secret token under the buyer policy into an oblivious key-value store with pseudorandom masking; the buyer reconstructs the token locally via tag-based probing, eliminating combinatorial enumeration, and proves correctness in zero-knowledge. Fair exchange is enforced through a collateralized on-chain reveal with a cryptographic audit that penalizes misbehaviour without trusted parties.
We prove security in the Universal Composability framework under standard assumptions. Compared with the state-of-the-art threshold fuzzy IB-ME scheme, the seller's publishing time is reduced by two orders of magnitude (e.g., 8.76s vs. 690s for a policy of 500 attributes). For a typical configuration of (200,20,5), the buyer completes token reconstruction and proof generation in 8.9s, with the zero-knowledge proof taking under 0.6s and remaining constant across all parameter scales. The on-chain cost is approximately 28.6M gas, well within Ethereum's block limit. PriME-Deal thus delivers the first practical privacy-preserving data trading protocol that combines linear seller overhead, bilateral policy hiding, and auditable fairness.

---


### 70. [WHET: Welding Homomorphic Encryption to Accelerator Architectures](https://arxiv.org/abs/2606.11541)

**<font color=#1a73e8>作者：</font>** Jongmin Kim, Hyesung Ji, Wonseok Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) enables computations on encrypted data without decryption, offering strong data privacy at the expense of substantial computational and memory overheads. Prior efforts have steadily improved FHE performance through cryptographic and algorithmic enhancements or hardware acceleration, yet these two directions have progressed largely in isolation, hindering the full exploitation of available hardware capabilities. This work presents WHET, which introduces memory-centric, architecture-aware optimizations to better align cryptographic and algorithmic constructions with FHE accelerator architectures. We identify conventional FHE constructions as major sources of excessive working sets and heavy off-chip memory traffic. We propose accelerator-specific techniques, including fine-grained coefficient-to-slot transformation, plaintext compression, and intermediate modulus raising, to reduce the on-chip data footprint by minimizing temporary ciphertexts and plaintext loads. With these techniques applied, we observe additional opportunities to improve on-chip memory efficiency; hence, we introduce lightweight architectural refinements, including a special-purpose buffer and functional unit extensions. With these optimizations, WHET achieves 1.38-8.74$\times$ per-area performance improvements over state-of-the-art FHE accelerators and the first-ever sub-millisecond CKKS bootstrapping.

---


### 71. [Pretrained self-supervised speech models can recognize unseen consonants](https://arxiv.org/abs/2606.11542)

**<font color=#1a73e8>作者：</font>** Chihiro Taguchi, Éric Le Ferrand, Hirosi Nakagawa 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern pretrained self-supervised automatic speech recognition models are trained on large-scale audio data to encode speech into contextualized representations. However, their training data are heavily skewed toward high-resource languages with little data from low-resource languages, raising concerns about the potential underrepresentation of typologically uncommon speech sounds such as click consonants primarily found in Khoisan languages. This leads to our central research question: Can these models recognize click consonants as accurately as other speech sounds? To address this question, we fine-tune and compare pretrained self-supervised speech models (Wav2Vec2 and HuBERT) on data from two click-rich Khoisan languages (G|ui and West !Xoon). Our results reveal that the fine-tuned models consistently recognize clicks more accurately than non-clicks, suggesting that self-supervision enables generalization across human speech sounds including rare phonemes.

---


### 72. [SkillJuror: Measuring How Agent Skill Organization Changes Runtime Behavior](https://arxiv.org/abs/2606.11543)

**<font color=#1a73e8>作者：</font>** Zhiyu Chen, Zihan Guo, Bo Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent Skills augment large language model (LLM) agents with procedural knowledge at inference time, but current benchmarks rarely distinguish what a Skill says from how it is organized. We study this distinction through Progressive Disclosure, where a concise root file points agents to supporting resources on demand, and compare it with a normalized flat baseline. We present SkillJuror, a framework for evaluating Skill writing paradigms through semantically controlled variants, matched multi-trial evaluations, and trajectory evidence while holding task knowledge fixed. In an 82-task SkillsBench study, Progressive Disclosure changes runtime behavior before aggregate outcomes: distinct Skill resources touched per trajectory rise from 1.18 to 3.85, and effective uptake events rise from 1.33 to 3.92. It also yields 17 additional verifier-passing trials out of 410 matched trials (+4.1%) over the normalized flat baseline. The benefit is task-dependent. Progressive Disclosure helps when supporting resources guide implementation, checking, or repair, but is weaker when success hinges on exact output conventions, numerical thresholds, or long artifact-generation pipelines. These results show that Skill organization is not mere presentation: it can change how agents search and apply procedural knowledge, while outcome gains depend on whether the exposed resources are actionable for the task. Code is available at this https URL.

---


### 73. [Privacy-Preserving Federated Autoencoder for ECG Anomaly Detection on Edge Devices](https://arxiv.org/abs/2606.11556)

**<font color=#1a73e8>作者：</font>** Kaan Arda Akyol, Jakub Kacper Szeląg, Aydin Abadi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Continuous electrocardiography (ECG) monitoring could surface rhythm abnormalities before they escalate into cardiovascular events. However, a deployable system must satisfy three requirements simultaneously: legal-grade privacy (GDPR, HIPAA), real-time inference on constrained edge hardware, and detection quality under non-IID cross-hospital data.
We design and evaluate an end-to-end federated system addressing all three for unsupervised 12-lead ECG anomaly detection on PTB-XL dataset, combining three autoencoder families (VanillaAE, ConvAE, VAE), Flower-based federated averaging (FedAvg) across ten simulated hospitals, client-side differentially private SGD (DP-SGD) with a Rényi-DP accountant, and 8-bit integer (INT8) post-training quantization with Raspberry Pi 4 benchmarking. Our main contributions are: an empirical characterization of how these mechanisms compose, practical DP-specific recommendations, and technical and security insights for a clinically sensitive setting. Federated learning matches or exceeds the centralized baseline across all architectures (ConvAE federated area under the ROC curve, AUROC, $0.782$), and an $\varepsilon$ sweep identifies $\varepsilon=4$ as the recommended clinical operating point. INT8 quantization roughly halves model size and cuts Pi 4 latency by up to $44%$ with $<0.12%$ AUROC loss. Crucially, DP and quantization penalties are empirically independent, so practitioners need not trade a strong privacy guarantee for a compact edge footprint. To our knowledge, this is the first system combining federated learning, formal $(\varepsilon,\delta)$-DP, unsupervised reconstruction-based detection, and quantized AArch64 deployment.

---


### 74. [Cross-Modal Benchmarking for Robotic Perception in Natural Environments](https://arxiv.org/abs/2606.11563)

**<font color=#1a73e8>作者：</font>** David Hall, Joshua Knights, Mark Cox 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural environments present a complex challenge to robotics perception systems. Current models, particularly vision foundation models, are largely trained on structured, urban environments leading to weaknesses in their perception for field robotics tasks. We showcase the limitations of current models using our recently released WildCross benchmark, a new cross-modal benchmark for place recognition and metric depth estimation in large-scale natural environments. WildCross comprises over 476K sequential RGB frames with semi-dense depth and surface normal annotations, each aligned with accurate 6DoF pose and synchronized dense lidar submaps. In this work, we provide an expanded analysis of the benchmark results from the recent WildCross benchmark, with particular emphasis on expanded metric depth estimation experiments. Access to the code repository and dataset for this work can be found at https://csiro-robotics.github.io/WildCross.

---


### 75. [A Deterministic Forensic Preprocessing Framework for Heterogeneous Network Datasets: Formal Foundations, Implementation, and Empirical Validation](https://arxiv.org/abs/2606.11565)

**<font color=#1a73e8>作者：</font>** Ravi Chaudhary, Reza Ryan, Nasim Ferdosian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital forensic investigations increasingly depend on preprocessing heterogeneous network evidence from intrusion detection systems, IoT devices, and enterprise traffic logs. Incompatible schemas and timestamp formats hinder evidence correlation and timeline reconstruction, while current ad hoc approaches offer no mechanism to verify consistency across runs or analysis, creating reproducibility gaps that challenge evidence admissibility. This paper introduces a deterministic forensic preprocessing framework that converts heterogeneous network datasets into a reproducible canonical form. The framework formalises three preprocessing transformations: schema normalisation, temporal normalisation, and provenance tracking. These transformations are specified using set-theoretic definitions and supported by four theorems establishing determinism, information preservation, and provenance completeness. A chunk-based architecture provides O(c) bounded memory. Empirical evaluation across UNSW-NB15, IoT-23, and TON_IoT demonstrates 100% output consistency across repeated runs, robust temporal normalisation completeness over heterogeneous timestamp formats, and scalable performance from millions to hundreds of millions of records.

---


### 76. [FreqKD: Frequency-Decoupled Cross-Modal Knowledge Distillation for Infrared Object Detection](https://arxiv.org/abs/2606.11572)

**<font color=#1a73e8>作者：</font>** Keval Thaker, Venkatraman Narayanan, Abdalmalek Aburaddaha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transfer learning from large-scale RGB foundation models to infrared (IR) imagery through knowledge distillation (KD) remains challenging due to fundamental differences in image formation physics. We investigate the spectral structure of the RGB--IR modality gap and observe that feature divergence is not uniform across spatial frequencies: low-frequency components (shape, layout) show greater cross-modal alignment than high-frequency components (texture, fine edges), which reflect modality-specific characteristics. Based on this analysis, we propose FreqKD, a frequency-decoupled distillation framework that applies asymmetric supervision adapted to each band's cross-modal consistency. The method employs strict mean squared error (MSE) on the low-frequency band to preserve shared structural information and a relaxed log-MSE loss (weighted at 0.1) on the high-frequency band to provide edge guidance while tolerating texture differences. Spectral divergence analysis on 500 paired samples shows that high-frequency divergence exceeds low-frequency divergence by a factor of 2.4x on average across all analysed transformer layers. On KAIST multispectral pedestrian detection, FreqKD achieves 64.1 mAP50, improving 2.4 points over the DINOv2 baseline. The learned representation transfers across datasets (FLIR ADAS, +2.1 mAP50), tasks (MFNet segmentation, +1.85 mean intersection-over-union), and architectures (ResNet-50, +1.0 mAP50). Code is available at: this https URL

---


### 77. [Understanding Cross-Sensor Feature Variations for Generalizable 3D Perception](https://arxiv.org/abs/2606.11573)

**<font color=#1a73e8>作者：</font>** Xin Qiu, Wenjie Liu, Fuyuan Ai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radar-camera BEV perception often suffers from degraded performance when evaluated across datasets, as changes in driving scenes, sensor configurations, and environmental conditions can alter both the input observations and the internal fused representations. This work studies this issue from the perspective of source-domain variation modeling, aiming to improve the robustness of BEV-based 3D detectors without relying on target-domain samples. We introduce a framework that characterizes visual scene variations in the frequency domain and uses them to synthesize diverse source-domain views. By comparing the resulting fused BEV representations, the framework further captures how image-level variations influence multi-modal BEV features. These variation patterns are then used to regularize the detector, encouraging the learned fusion space to remain stable under latent scene changes. The proposed method is applied only during training and leaves the inference pipeline unchanged. Experiments on cross-dataset radar-camera 3D detection between View-of-Delft and TJ4DRadSet demonstrate consistent improvements over multiple BEV fusion backbones, and the gains remain effective when a small amount of target-domain data is available.

---


### 78. [Range-Aware Bayesian Optimization for Discovering Diverse Designs within Target Property Windows](https://arxiv.org/abs/2606.11574)

**<font color=#1a73e8>作者：</font>** Shengli Jiang, Jason Wu, Charles M. Schroeder 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many materials and product design problems, desirable candidates exhibit properties that fall within an acceptable range rather than achieve a single optimum. Recovering multiple, distinct solutions that satisfy such specifications is also practically valuable, as some candidates may be preferred for reasons of cost, processability, or robustness that are difficult to encode directly in an objective function. Here, we develop a range-aware Bayesian optimization (BO) framework in which the acquisition function directly scores the posterior probability that a candidate satisfies a target range. The framework naturally extends to parallel pursuit of multiple distinct specifications over a shared candidate space. Across benchmark tasks, range-aware acquisition consistently recovers larger and more diverse sets of valid designs than standard BO baselines and recent goal-seeking methods. Its utility is further demonstrated in two practically motivated design case studies involving optimizing reaction conditions for polymer synthesis and sequence-defined oligomer discovery for prescribed optical absorption bands, supported by quantum chemical calculations. These results suggest that range-aware BO can provide a practical and sample-efficient foundation for specification-driven design, particularly when design flexibility and solution diversity are important considerations.

---


### 79. [Contactless 3D Human Body Measurement Using Depth Cameras for Smart Health Monitoring](https://arxiv.org/abs/2606.11578)

**<font color=#1a73e8>作者：</font>** Martha Asare, Xuan Wang, Juan Lopez Alvarenga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contactless body measurement technologies are becoming increasingly significant for smart health monitoring, digital health applications, and remote patient assessment. Traditional anthropometric measurements typically necessitate physical contact and trained personnel, which may constrain scalability in remote healthcare settings. In this study, we introduce a depth camera-based framework for estimating human body measurements utilizing 3D point cloud data. An Orbbec Astra 2 depth camera was employed to capture RGB images, depth maps, and 3D point clouds of participants. The captured point cloud was processed using Python-based tools, including Open3D, NumPy, and OpenCV, to segment the human body from the background. Key anthropometric measurements, such as height and arm span, were computed. The measurements were obtained through a combination of spatial filtering and landmark selection on the 3D point cloud, followed by the projection of the computed measurements onto the corresponding RGB image using camera intrinsic parameters. In addition to linear measurements, the approximate body volume and visible surface area were estimated using voxel-based occupancy analysis and mesh-based surface reconstruction methods. The experimental results from a single depth capture demonstrated that accurate body measurements and geometric estimates could be obtained from depth camera data without physical contact. This study provides a foundation for future real-time systems that integrate depth sensing with intelligent health monitoring and generative AI models for smart healthcare applications.

---


### 80. [Kuramoto Attention: Synchronizing Self-Attention on the Torus](https://arxiv.org/abs/2606.11585)

**<font color=#1a73e8>作者：</font>** Joshua Nunley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Kuramoto attention, a self-attention layer in which each hidden coordinate is an angle. The layer scores tokens by gated cosine similarity, attends over previous phase states, and updates each token by the tangent component of the attention-weighted circular mean. Because the values are the raw phase states, this update is exactly the Kuramoto coupling term $\sum_u A_{t,u}\sin(\theta_u-\theta_t)$, with the attention matrix acting as an adaptive, content-dependent coupling kernel. Equivalently, the gated score is a learned metric on the torus that selects which tokens couple, and the update pulls each token toward the circular mean of the tokens it selects, tightening their phase agreement. The same two ingredients, an invariant similarity score and an on-manifold mean, define such a layer on any compact group; the torus is the abelian case, where both are closed-form. The softmax weights solve an entropy-regularized phase-retrieval problem, and rotary position enters as a position-dependent phase drift in the score. On enwiki8 character-level language modeling, the layer trains as a functional language model whose bits-per-character stays close to a strong matched RoPE+SwiGLU transformer: within $0.02$ BPC at one million parameters ($1.637\pm0.010$ versus $1.616\pm0.004$) and level on the median at five million ($1.448$ versus $1.452$ over five seeds) with the transformer ahead on the mean ($1.468$ versus $1.456$). These experiments establish that the constrained geometric structure is a viable language model at this scale; the structure itself, and its synchronization reading, is the contribution. Ablations isolate the load-bearing components, and the result gives a compact bridge between self-attention and phase synchronization.

---


### 81. [Spatially Coupled Phase-to-Depth Calibration for Fringe Projection Profilometry](https://arxiv.org/abs/2606.11601)

**<font color=#1a73e8>作者：</font>** Sehoon Tak, Jae-Sang Hyun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In fringe projection profilometry (FPP), depth is commonly recovered by fitting a phase-to-depth relation independently at each camera pixel. Although such pixel-wise calibration achieves high local accuracy, neighboring pixels can acquire markedly different calibration functions even when they observe the same smooth surface, producing spatially inconsistent geometry and structured surface artifacts. We propose a spatially coupled phase-depth transformation in which all pixels share a single low-dimensional mapping-global phase scalars combined with affine spatial terms on the undistorted reference-camera grid-rather than independent per-pixel fits, optionally augmented by a bounded, spatially smooth correction field. We further introduce a native-grid pairing scheme that constructs phase-depth calibration pairs directly on the reference-camera grid: when depth supervision comes from a rectified active-stereo pipeline, planes are fitted in stereo 3D and sampled back onto the camera grid along native rays, so the phase maps are never rectified. On a dental target with high-resolution scanner ground truth, the proposed model attains point-to-surface RMSE comparable to an active-stereo reference (about 12{\mu}m aggregate) while substantially improving spatial coherence over pixel-wise polynomial and rational calibration, and reduces the runtime mapping to a few element-wise operations per pixel with negligible parameter storage.

---


### 82. [On Aligning Hierarchical Standardized Embedding for Audio-visual Generalized Zero-shot Learning](https://arxiv.org/abs/2606.11602)

**<font color=#1a73e8>作者：</font>** Zihan Zhang, Jie Hong, Siyuan Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual Generalized Zero-shot Learning (AV-GZSL) is a challenging task that aims to classify both seen and unseen objects or scenes by integrating data from audio and visual modalities. Recent studies primarily focus on fusing or aligning audio and visual features to generate more informative audio-visual embeddings. Also, aligning the audio-visual and textual features of most existing methods relies solely on the optimization objectives. However, those methods neglect the inherent distributional and structural differences between audio-visual and textual modalities. To address this limitation, we propose a method termed Aligning Hierarchical Standardized Embedding (AHSE), which enables hierarchical alignment of standardized audio-visual and textual embeddings within a shared embedding space. Specifically, we first apply Z-score standardization to the fused audio-visual and textual embeddings to reduce distributional mismatches. We then introduce a hierarchical alignment strategy that minimizes discrepancies at the semantic, class, and batch levels, thereby constructing a more robust and well-structured embedding space. This strategy not only preserves semantic and inter-class relationships but also maintains spatial consistency within each batch. Extensive experiments on three benchmark datasets: VGGSound-GZSL, UCF-GZSL, and ActivityNet-GZSL, demonstrate that AHSE achieves competitive performance in zero-shot learning.

---


### 83. [Frozen Foundation-Model Embeddings Discard Small-Lesion Signal in Chest Radiography: Implications for Pre-Deployment Evaluation](https://arxiv.org/abs/2606.11606)

**<font color=#1a73e8>作者：</font>** Raajitha Muthyala, Zhenan Yin, Alekhya Jilla 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen vision-transformer (ViT) foundation-model embeddings increasingly serve as the substrate for downstream chest-radiography (CXR) pipelines, yet where small-scale, low-contrast signal is retained or lost in the frozen forward pass has not been systematically quantified across architectures, pretraining domains, and objectives. We probed five frozen ViTs (RAD-DINO, DINOv2-B/14, DINOv3 ViT-7B, BiomedCLIP, MedSigLIP) and a frozen DINO-pretrained ResNet-50 architectural control across three large CXR cohorts (NIH-CXR14, MIMIC-CXR, Emory-CXR; aggregate pool n=492,724) and ChestX-Det10 (n=3,543; 1,462 small-lesion bounding boxes across Calcification, Nodule, Mass). Each model was evaluated with a small-scale-perturbation panel and a region-aware bounding-box-stratified probe on real lesions, comparing three pooling modes from the same forward pass: classification token (CLS), patch-mean (mean over all final-layer patch tokens), and bounding-box-restricted patch-local. On the perturbation panel, CLS embeddings sat at the chance floor (area under the ROC curve [AUC] 0.500-0.524); patch-mean was indistinguishable from CLS on iso-blur and reticular-fine cells but rose with CLS on larger directional-blur footprints, while disease AUC on globally decided tasks ranged 0.642-0.913. Patch-local probes recovered AUC ~1.0 from the same forward pass (per-model mean improvement +0.412 to +0.488); the ResNet-50 control reproduced the chance floor. On ChestX-Det10, image-level CLS classification showed within-class small-versus-large stratum gaps up to +0.243 AUC; bounding-box-level patch-local pooling on the same forward pass recovered AUC >= 0.899 on every (model x class) cell. Frozen ViT embeddings silently suppress small-scale signal at the global-aggregation step; the signal is recoverable from patch tokens conditional on a region of interest.

---


### 84. [Adv-TGD: Adversarial Text-Guided Diffusion for Face Recognition Impersonation Attacks](https://arxiv.org/abs/2606.11615)

**<font color=#1a73e8>作者：</font>** Omid Ahmadieh, Nima Karimian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of face recognition (FR) technologies raises serious privacy concerns, as facial data can be exploited without consent. To address this challenge, we propose Adv-TGD, a generative adversarial attack framework that synthesizes photorealistic faces capable of impersonating target identities and deceiving face recognition systems. Built upon Stable Diffusion, Adv-TGD performs per-sample LoRA fine-tuning conditioned on concise textual prompts to generate natural yet adversarially manipulated identities. Unlike conventional identity-attack approaches, our method optimizes lightweight cross-attention adapters for each source-target pair within a single-step denoising process. Latent blending is constrained by a face-local heatmap mask to ensure spatially precise identity manipulation while preserving non-sensitive regions. We introduce a composite objective that integrates masked epsilon-MSE reconstruction, thresholded identity divergence in FR embedding space, directional feature alignment, and source-similarity suppression to balance adversarial attack and visual realism. Optionally, LLaVA-generated attribute prompts enhance fine-grained semantic details without reintroducing identity cues. Under the black-box evaluation protocol, Adv-TGD attains an average attack success rate (ASR) of 85.90% across IR152, IRSE50, MobileFace, and FaceNet, surpassing the semantic SOTA baseline Adv-CPG by +6.25 points, diffusion-based makeup method DiffAIM by +3 points, and noise-based P3-Mask by +16 points. Despite its strong attack efficacy, Adv-TGD preserves high visual fidelity (PSNR = 27.15 dB, SSIM = 0.981). Furthermore, we demonstrate the flexibility of our framework by successfully extending it to in-the-wild datasets (LADN), general object classification (ImageNet), and transformer-based diffusion models (FLUX.1).

---


### 85. [DeMix: Debugging Training Data with Mixed Data Error Types by Investigating Influence Vectors](https://arxiv.org/abs/2606.11616)

**<font color=#1a73e8>作者：</font>** Jiale Deng, Yanyan Shen, Xiaogang Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-quality training data is essential for the success of machine learning models. However, real-world datasets often contain mixed types of errors arising from systematic flaws in data preparation pipelines, including label errors, feature errors, and spurious correlations. Effective debugging of training data requires both detecting erroneous samples and identifying their specific error types to enable targeted repair, yet existing data cleaning and attribution methods fail to adequately address this dual requirement. In this paper, we propose DeMix, a novel framework that simultaneously diagnoses erroneous samples and their error types. Our key insight is that different error types produce distinct patterns on model behavior. DeMix captures such error-specific patterns by influence vectors that characterize how each training sample affects model predictions across all validation samples. We formulate training data debugging as a multi-label classification problem where a classifier is developed to predict error types directly from influence vectors. We further introduce an intervention-based learning strategy that guides the classifier to capture invariant rationales specific to each error type, ensuring the learned classifier generalizes effectively. Empirical evaluations on 11 tasks across tabular data prediction, recommendation systems, and LLM alignment demonstrate that DeMix significantly outperforms state-of-the-art approaches, achieving a 22.61% improvement in data debugging F1-score and a 9.32% gain in task model performance after data repair. Code is available at: this https URL.

---


### 86. [Precision-Aware Illumination-Disentangled Vision Transformer for Spacecraft 6D Pose Estimation](https://arxiv.org/abs/2606.11619)

**<font color=#1a73e8>作者：</font>** Zongwu Xie, Yifan Yang, Yonglong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision sensors provide a lightweight solution for spacecraft proximity operations, but monocular spacecraft 6D pose estimation remains difficult under illumination variation, specular reflection, shadowing, weak texture, and background interference. These factors make local visual evidence spatially unreliable and can destabilize pose regression. This article proposes a Precision-Aware Illumination-Disentangled Vision Transformer (PAID-ViT) for robust spacecraft pose this http URL proposed model separates pose-relevant structure tokens from illumination-sensitive appearance tokens, estimates patch reliability before pose aggregation, and uses foreground mask supervision to preserve silhouette cues. A parameter-free geometric recovery module converts normalized crop coordinates, log-depth, and a continuous 6D rotation representation into camera-frame rotation and translation. Experiments on SPEED+ V2, the SPEED+ validation/lightbox/sunlamp evaluation configuration used in this study, suggest that PAID-ViT reduces translation error and improves robustness in the challenging sunlamp domain, while ablation studies support the complementary roles of illumination disentanglement, reliability-aware token aggregation, mask supervision, and training-side regularization.

---


### 87. [When Context Returns: Toward Robust Internalization in On-Policy Distillation](https://arxiv.org/abs/2606.11627)

**<font color=#1a73e8>作者：</font>** Xun Wang, Ruishuo Chen, Zhuoran Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that on-policy distillation can internalize privileged context, such as system prompts or task hints, into a student model so that the context is no longer needed at inference time. Although this approach successfully improves the student's no-context performance, we identify an interesting and previously unstudied phenomenon: in many settings, reintroducing the original privileged context to the distilled student actually degrades its performance, even on instances it already solves correctly without context. We term this context-induced degradation and argue that robust internalization demands not only matching the teacher's context-conditioned behavior, but also remaining stable when the context is reintroduced, a property we call context removability. Motivated by this observation, we propose a lightweight consistency regularizer that first anchors the student's no-context output via stop-gradient, then penalizes the context-conditioned output for deviating from it via forward KL divergence. This simple addition requires only one extra forward pass per training step, yet it effectively mitigates context-induced degradation and, in many cases, even improves no-context performance. Across 12 configurations spanning diverse domains and model families, our method improves context-conditioned accuracy in the majority of settings, reduces context-induced harm in 11 out of 12 settings, and effectively eliminates response-length inflation. A mechanistic case study further confirms that context removability is achieved at the representation level, with hidden states remaining nearly identical regardless of whether the context is present.

---


### 88. [TouchThinker: Scaling Tactile Commonsense Reasoning to the Open World with Large-scale Data and Action-aware Representation](https://arxiv.org/abs/2606.11637)

**<font color=#1a73e8>作者：</font>** Kailin Lyu, Di Wu, Pengwei Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Touch is a key modality for embodied agents to understand the physical world. Although recent work has incorporated tactile signals into language systems for tactile commonsense reasoning, scaling such systems to realistic open-world settings remains challenging due to two key bottlenecks: (1) current tactile reasoning datasets remain limited in format and scale, providing insufficient supervision for reasoning from tactile observations to physical commonsense and hindering the learning of transferable tactile commonsense; (2) Tactile signals are inherently redundant and action-specific, yet existing methods often overlook these properties, resulting in inefficient representations with limited semantic expressiveness. To address these limitations, we propose TouchThinker, a tactile-language framework that scales tactile commonsense reasoning to the open world from both data and representation perspectives. First, we construct TouchThinker-1M, a million-scale, multi-source tactile reasoning dataset covering \textbf{415} objects, \textbf{8} scenarios, and \textbf{7} sensor types, providing a solid data foundation for open-world generalization. We further introduce TouchThinker-Bench, an open-world benchmark with more realistic and diverse tasks. Then, we propose action-aware modeling mechanism to improve tactile representation efficiency and enable efficient reasoning. Experimental results demonstrate that TouchThinker achieves competitive performance against state-of-the-art models across multiple datasets. Our code and dataset will be made available at: this https URL.

---


### 89. [Evaluating Bias in Phoneme-Based Automatic Speech Recognition Systems: An Analysis of IPA Transcription Models](https://arxiv.org/abs/2606.11639)

**<font color=#1a73e8>作者：</font>** Catherine Bao, Maneesha Rani Saha, Neal Patwari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The popularization of automatic speech recognition (ASR) systems has increased exploration of the demographic biases related to race, age, gender, and accent, often formed from imbalanced training data. Most of these studies focused on standard grapheme-based ASR systems with comparatively little emphasis on phoneme-based systems, such as models that produce International Phonetic Alphabet (IPA) representations. As ASR systems shift toward multilingual support and low-resource language modeling, IPA-based layers serve as a critical, language-agnostic foundation. In this study, we evaluate the performance of two state-of-the-art open-source ASR systems, WhisperIPA and ZIPA, that generate IPA transcriptions across diverse accents and language sources. Our evaluation includes existing multilingual speech corpora and demographically annotated English-language corpora. We measure model performance by comparing model-generated IPA transcriptions against grapheme-to-phoneme (G2P) systems using both standard phoneme error rate (PER) and a proposed Soft PER metric that tolerates linguistically similar phoneme substitutions. Our analysis examines how performance varies across languages and demographic groups such as gender, accent, ethnicity, and age, revealing persistent disparities even after accounting for acceptable phonemic variation. These findings provide insight into potential sources of bias and inform the development of more inclusive and linguistically robust phoneme-based ASR systems. Our code and data will be made publicly available to the community.

---


### 90. [3-Key-Input: Exploring the Theoretical Minimum Keys for Text Entry](https://arxiv.org/abs/2606.11642)

**<font color=#1a73e8>作者：</font>** Naoki Kimura  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> How far can we reduce the number of physical keys if we endow an ambiguous keyboard with modern language models? Fewer keys increase hardware design freedom in constrained settings such as assistive devices and mobile form factors. This paper systematically evaluates text entry systems using 2-5 physical keys combined with language-model-based disambiguation. On a 300-sentence English corpus (100 sentences each for Business / Conversational / Technical), we compare key counts (2-5), letter-to-key mappings (layout-based / frequency-based / intentionally worst-case), and decoders (Trie-only, GPT-2 beam search, GPT-4o selection). We find that 3 keys + GPT-4o achieves character error rate (CER) 9.46% and word error rate (WER) 12.20%, reducing CER by 59% relative to 2 keys (CER 23.3%). At 3 keys, the key-stream entropy is 1.54 bits/char; while increasing to 5 keys improves accuracy (CER 5.4%), the marginal gains diminish. Mapping choice has a small impact under standard designs ({\Delta}CER < 0.5 pp), and even an intentionally worst mapping degrades CER by only +0.5 pp, whereas Technical sentences yield roughly twice the error rate of Business. These results suggest that, in our evaluated offline setting under a strong LM prior, 3 keys are a practical minimum for general English.

---


### 91. [Motion Reinforces Appearance: RGB-Skeleton Gated Residual Fusion for Micro-Gesture Online Recognition](https://arxiv.org/abs/2606.11645)

**<font color=#1a73e8>作者：</font>** Jialin Liu, Xinwen He, Pengyu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-gesture analysis attracts increasing attention for inferring spontaneous emotion from subtle body movements. Micro-gesture online recognition, which localizes and classifies each gesture instance in untrimmed videos, is a core task in the 4th EI-MiGA-IJCAI Challenge. Compared with typical temporal action detection, MGR emphasizes the localization and classification of actions, requiring the model to output the start time, end time, and category of each micro-gesture. Moreover, since micro-gestures are highly spontaneous, relying solely on a single modality makes it difficult to capture the complete and accurate multi-modal cues. In this work, we propose DyFADet+, which extends DyFADet into a dual-stream RGB-skeleton framework. In our model, both modalities are projected into shared multi-scale temporal embeddings and fused through a gated residual module, which adaptively injects skeleton motion into the RGB representation rather than using naive concatenation. Finally, these fused features are decoded by a Dynamic TAD head for online classification and boundary regression. On the SMG dataset, our method achieves an F1 score of 40.88, ranking 2nd in the Micro-gesture Online Recognition track.

---


### 92. [Tree-Structured Orthonormal Decomposition of the Aitchison Simplex](https://arxiv.org/abs/2606.11646)

**<font color=#1a73e8>作者：</font>** Daisuke Yamada, Qijun Zhang, Travis Pence 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compositional data -- vectors encoding relative proportions -- arise across scientific domains, including ecology, geochemistry, and genomics. The features in these data often come with known hierarchical structure (e.g., taxonomies, phylogenies, ontologies), yet existing methods either ignore this structure, discard the intrinsic Aitchison geometry, are designed for binary trees, or yield incomplete coordinate systems. We describe PolyILR, a canonical orthonormal decomposition of the Aitchison tangent space aligned with any tree topology. Our construction defines a weighted local geometry at each internal node capturing full branching structure, then lifts these to a global orthonormal basis where every coordinate corresponds to a specific tree location. On microbiome and single-cell benchmarks, PolyILR yields stable, interpretable features and enables inference at multiscale tree resolution. We also establish a novel theoretical connection to softmax classifiers, suggesting possible applications to probabilistic modeling.

---


### 93. [Structure-Preserving Neural Surrogates with Tractable Uncertainty Quantification](https://arxiv.org/abs/2606.11650)

**<font color=#1a73e8>作者：</font>** Handi Zhang, Adrienne M. Propp, Brooks Kinch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in scientific machine learning provide a means of near-real-time solution to partial differential equations (PDEs), but lack the theoretical underpinnings of conventional simulators that support contemporary verification and validation. In this work, we construct data-driven reduced-order models that serve as structure-preserving, real-time surrogates. Remarkably, the exterior calculus that imposes physical conservation structure also exposes topological structure that we use to build a Gaussian process (GP) representation of uncertainty in state-flux relationships, ultimately yielding a Dirichlet-to-Neumann map for quantities of interest with closed-form expressions for posterior uncertainty. We specifically propose structure-preserving $H(\mathrm{div})$--$L^2$ subspaces of conventional Raviart--Thomas and $dgP_0$ elements prescribed by a lightweight transformer. Reduced-order dynamics consistent with this subspace are learned by posing a conservation law in which a GP describes the fluxes between volumes. This work hinges on a novel interface between mixed FEM spaces and GP regression; when training is posed as the optimal recovery problem (ORP), the resulting GP regression can be written as an optimization problem with equality constraints that impose a conservation structure, amenable to a fast Schur-complement training strategy. The trained model can then be solved in real time with closed-form estimators for boundary fluxes driven by prescribed Dirichlet data. The paper includes RKHS posterior error bounds for linear functionals to support uncertainty quantification, as well as numerical experiments demonstrating the accuracy of the posterior distribution as a surrogate for error estimation.

---


### 94. [DeepRHP: A Hybrid Variational Autoencoder for Designing Random Heteropolymers as Protein Mimics](https://arxiv.org/abs/2606.11651)

**<font color=#1a73e8>作者：</font>** Shuni Li, Zhiyuan Ruan, Andy Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic random heteropolymers (RHPs), consisting of a predefined set of monomers, offer an approach toward the design of protein-like materials. These RHPs, if designed appropriately, can mimic protein behavior and function. As such, there is a need for computational tools to efficiently guide RHP design. We bridge this gap by developing DeepRHP, a modified variational autoencoder (VAE) model under a semi-supervised framework. By equipping a classical VAE with an additional feature-based VAE, DeepRHP forces the latent space to capture structures of critical chemical features as well as individual RHP sequence patterns. In this sense, our method is versatile by allowing any relevant features to be incorporated in a hybrid manner. We demonstrate the effectiveness of DeepRHP by suggesting potential monomer compositions that stabilize membrane proteins (e.g. Aquaporin Z) in non-native environments and cross-validating our prediction with published results. The concordance between our model and true RHP function suggests strong potential in utilizing hybrid autoencoder architectures to guide RHP design for proteins and other biological compounds.

---


### 95. [Bergson: An Open Source Library for Data Attribution](https://arxiv.org/abs/2606.11660)

**<font color=#1a73e8>作者：</font>** Lucia Quirke, Louis Jaburi, David Johnston 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data attribution is a promising field in interpretability that aims to explain model behavior through the influence of its training data, with applications including debugging undesirable model behavior and training dataset curation. However, significant engineering effort is required to perform it at scale, and many cutting edge techniques lack open-source tooling and support. Bergson is an open source library that aims to enable faster progress in the field by providing a host of techniques that scale to very large language models and pre-training datasets. The library natively supports on-disk gradient stores and multi-node distributed training, and provides quality of life tools for researchers. Finally, we introduce the first open-source implementations of three leading data attribution methods: MAGIC, SOURCE, and TrackStar. The library is available at this https URL .

---


### 96. [Learning Instance-Adaptive Low-Rank Orthogonal Subspaces for Clothes-Changing Person Re-Identification](https://arxiv.org/abs/2606.11661)

**<font color=#1a73e8>作者：</font>** Dong-Woo Kim, Tae-Kyun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clothes-changing person re-identification (CC-ReID) aims to recognize individuals despite drastic appearance changes caused by clothing variation. While existing methods rely on adversarial learning to disentangle clothing features, we propose Ortho-ReID, which explicitly models a low-rank clothing subspace from VLM text descriptions and extracts clothing-invariant representations via direct geometric constraints. A critical component is our transformer-based Basis Maker, which refines a shared, low-dimensional clothing prior into an instance-adaptive low-rank subspace through cross-attention with image patches, enabling robust clothing feature extraction even under varying visibility conditions. This instance-adaptive subspace is supervised via alignment with clothing text embeddings, while identity features are extracted via a learnable projection head and geometrically constrained to be strictly orthogonal to it. Extensive experiments demonstrate state-of-the-art performance on PRCC (+5.9% top-1), Celeb-reID-light (+3.5%), and LaST (+5.3%), with competitive results on LTCC.

---


### 97. [TreeSeeker: Tree-Structured Trial, Error, and Return in Deep Search](https://arxiv.org/abs/2606.11662)

**<font color=#1a73e8>作者：</font>** Zhuofan Shi, Mingzhe Ma, Lu Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep search requires agents to answer complex questions through multi-step web search, browsing, evidence comparison, and synthesis. A central challenge is deciding how to search when several directions look plausible but only some will later lead to reliable evidence. If an agent greedily follows the current best-looking direction, it may keep extending a weak continuation. If it explores without discipline, it may waste budget on disconnected trials. We propose TreeSeeker, an inference-time framework for controlled trial-and-error in deep search. TreeSeeker organizes search as branch-and-return search over tree-structured states, where each branch is a tentative direction for a sub-goal. At each round, TreeSearch reads all sub-goal trees, identifies active goals, and uses textual UCB signals of value, uncertainty, and risk to select among exploiting a promising branch, exploring an uncertain alternative, or pruning an unproductive continuation and returning to an earlier branch point. TreeMem supports this control loop by keeping evidence, uncertainty, conflicts, progress, and failure cues attached to the branches that produced them, so trial outcomes can guide later decisions. Experiments on XBench-DeepSearch, BrowseComp, and BrowseComp-ZH show that TreeSeeker consistently outperforms strong open-source baselines, suggesting that explicit branch-and-return control complements stronger reasoning and tool execution.

---


### 98. [A Robust Framework for Sybil Attack Detection in Vehicular Ad Hoc Networks](https://arxiv.org/abs/2606.11667)

**<font color=#1a73e8>作者：</font>** Md. Sadmin Tahmid Khan, Md. Saim Ahmmed Utsho, Mosarrat Jahan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sybil attacks create an illusion of traffic congestion by utilizing fake identities, which undermines the reliable and safe operation of vehicular ad hoc networks (VANETs). Existing detection mechanisms struggle to effectively handle Sybil attacks as they are (i) susceptible to high false positive rates (FPR) due to the overlapping trajectories of both Sybil and legitimate vehicles, (ii) not practical for real-world deployment due to manual calibrations with ground data, (iii) ineffective for sparse distribution of roadside units (RSUs) and vehicles as they depend heavily on the presence of both, and (iv) inefficient due to computational overheads. This paper addresses these shortcomings and proposes a robust framework to tackle these issues. The proposed scheme reduces the FPR by utilizing GPS location data, enabling the construction of more accurate and distinguishable trajectories. Besides, it employs DBSCAN clustering to identify Sybil vehicles, facilitating unsupervised parameter selection. GPS data eliminates the dependency on RSUs and vehicles, making this scheme effective in both sparse and dense regions. Additionally, the proposed scheme is lightweight and consistent across vehicles with heterogeneous capacities. Experimental results demonstrate that the proposed scheme reduces the FPR by approximately 68% in dense regions and 70% in sparse areas. Furthermore, it lowers the false negative rate (FNR) by 67% in the sparse region and achieves a competitive detection rate compared to the existing methods in both dense and sparse regions. Additionally, the proposed scheme decreases the detection time by almost 80% in dense regions and 43% in sparse ones.

---


### 99. [Learning by Chatting? Investigating the Impact of Generative AI on Information Seeking and Learning](https://arxiv.org/abs/2606.11669)

**<font color=#1a73e8>作者：</font>** Shravika Mittal, Su Lin Blodgett, Q. Vera Liao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) tools offer increasing opportunities for augmenting human cognitive tasks. Among these tasks, information seeking is being rapidly reshaped by GenAI tools, with potentially profound implications for learning and knowledge acquisition. To investigate these implications, we conducted a between-subjects field experiment in which participants pursued informal learning by seeking information through either ChatGPT or Google Search over a span of 8 days. Using a daily diary protocol, we gathered in-situ data on their information-seeking processes. Our findings show that participants in the ChatGPT group experienced diminished agency in their information-seeking processes, as they offloaded much of the information selection to AI, and consequently experienced greater meta-cognitive load arising from this reduced sense of control. We further highlight two sources of distortion in information access when using ChatGPT: biases in ChatGPT outputs, particularly towards providing solution-oriented artifacts over principled knowledge; and systematic shifts in users' information-seeking behaviors, whereby the conversational and socially-oriented interaction paradigm of current GenAI tools may inadvertently reduce exploration of the broader knowledge space. As a result, on average, participants in the ChatGPT group had worse learning outcomes than those using Google, especially for higher-order critical learning. Our work suggests inherent tensions between offloading information seeking to AI and meaningful learning, and provides broader implications for understanding AI's risks to human cognition.

---


### 100. [ARGUS: Stacked Multi-View Identity Mosaic Injection for Subject-Preserving Video Generation](https://arxiv.org/abs/2606.11670)

**<font color=#1a73e8>作者：</font>** Zijie Meng, Jiwen Liu, Yufei Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subject-preserving video generation is not solved by frontal-face similarity alone: a generated person must remain recognizable across motion, large viewpoint changes, expression shifts, occlusion, scale variation, and conflicts among text, first-frame, and identity references. We argue that the central bottleneck is the point-reference paradigm, which collapses identity into a single static observation entangled with pose, accessories, lighting, background, and camera statistics. We introduce Argus, a Wan-based framework centered on Stacked Multi-View Identity Mosaic Injection (SMII). SMII converts MLLM-selected image/video identity evidence into a 3*3 stacked mosaic, synchronizes the mosaic with the current diffusion time, and injects it as negative-time read-only memory in Wan's native token space. This turns identity from an external clean adapter or a single reference image into a compact dynamic distribution. Around SMII, an MLLM Identity Director selects informative identity moments and resolves condition conflicts, while no-cross-pair counterfactual training, Temporal Identity Annealing, and Adaptive Self-Likeness Guidance improve robustness without paired subject-video supervision. We further release HardID-Celeb, a public-figure identity-stress benchmark, and introduce YawScore and OccScore to probe large-yaw and first-frame-occlusion robustness. Argus achieves state-of-the-art results on OpenS2V-Eval Human-Domain, reaching 64.38 Total Score, 71.86 FaceSim, 51.62 NexusScore, and 79.14 NaturalScore. On HardID-Celeb, Argus obtains 76.80 FaceSim and improves YawScore and OccScore by 12.60 and 15.10 points over the strongest baselines, demonstrating that dynamic identity memory and large-scale counterfactual self-supervision are highly effective for subject-preserving video generation.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-248](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
