# 📦 其他研究 | 2026年09月10日

> 本类共 **542** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

---

### 151. [Sector-Mean: Deterministic Initialization of K-Means Centroids via Angular Sector Partitioning](https://arxiv.org/abs/2609.06468)

**<font color=#1a73e8>作者：</font>** Abhiyan Dhakal, Pranish Kafle, Rajani Chulyadyo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> K-Means is one of the most widely used clustering algorithms, but its susceptibility to initial centroid selection remains a primary bottleneck for its convergence speed and clustering accuracy. This paper proposes Sector-Mean Initialization, a deterministic initialization strategy with O(N) time complexity that partitions the two-dimensional data space into angular sectors around the global centroid and initializes centroids using sector-wise means. We evaluate the method on established two-dimensional benchmarks (SIPU, Birch) and multiple real-world datasets, comparing against random, K-Means++, and Max-Min initialization under identical Lloyd iterations. The statistical analysis of Friedman's test (p<0.05) and Nemenyi post-hoc comparison indicates that, while delivering equivalent clustering quality as K-Means++ and Max-Min, Sector-Mean offers significant computational efficiency. Experimental results show that Sector-Mean reduces the initialization time by 74.9% and 59.8% in comparison to K-Means++ and max-min, respectively. And, it yields the lowest average number of iterations, achieving approximately 5% fewer iterations than K-Means++ and 16% fewer than max-min. These results highlight that Sector-Mean initialization offers a deterministic and computationally efficient initialization strategy while preserving cluster quality.

---


### 152. [Learning Kernels by Alignment for Multiclass Bayes Classification](https://arxiv.org/abs/2609.06474)

**<font color=#1a73e8>作者：</font>** Hollan Haule, Alfredo Gonzalez-Sulser, Javier Escudero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernel methods separate data representation from decision-making, but typically require the kernel to be chosen in advance. We show that this kernel can instead be learned by alignment, and develop the resulting framework through the recently introduced Collaborative Learning and Inference (CLaI). We show that Collaborative Learning can be viewed as a kernel alignment process, in which an embedding is trained so that its induced similarity matches a label-derived target kernel. We also prove that Collaborative Inference is equivalent to kernel Bayes classification with Parzen-window density estimation. Motivated by these perspectives, we generalise CLaI by replacing cosine similarity with a learned Mahalanobis distance and extend it to multiclass classification. On CIFAR-10, PathMNIST, and SleepEDF, the Mahalanobis formulation improves accuracy, converges faster, and yields lower calibration error than the cosine-based variant. Auxiliary experiments further support these connections, showing that CLaI produces latent signals of the same form as a Gaussian process, while achieving competitive calibration on sepsis prediction. Together, these results establish a principled learned-kernel framework that unifies representation learning, kernel alignment, and Bayesian classification, and extends naturally to the multiclass setting.

---


### 153. [How Does Parameter Pruning Reshape DNN Representations? An Interaction-Driven Exploration](https://arxiv.org/abs/2609.06483)

**<font color=#1a73e8>作者：</font>** Fangbo Li, Junpeng Zhang, Qihan Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study focuses on the scientific problem of understanding internal factors that govern the diverse performance degradation of deep neural networks (DNNs) when different parameters are pruned. In order to explain why pruning certain parameters leads to significant performance degradation but pruning other parameters does not, we examine how the pruning operation affects the interaction patterns encoded by the DNN. We find that when we progressively increase the pruning ratio, the interaction patterns encoded by DNNs exhibit a distinct three-phase dynamics, \emph{i.e.}, model performance is not largely affected until the pruning operation begins to remove low-order interactions, and low-order interactions exhibit strong generalizability. Moreover, we find that the high sensitivity of DNN performance to the pruning of certain modules is attributed to whether the pruning operation removes generalizable low-order interaction patterns.

---


### 154. [Second-Order Smooth Planning with Optimal-Transport Bellman Smoothing](https://arxiv.org/abs/2609.06484)

**<font color=#1a73e8>作者：</font>** Tuan Dam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Planning with a generative model aims to estimate the value of a state using as few simulator calls as possible. SmoothCruiser achieves problem-independent complexity $\widetilde O(\varepsilon^{-4})$ by exploiting the smoothness of the entropy-regularized Bellman backup, but its estimator is only first-order. We show that the sample-complexity exponent of SmoothCruiser-type planners is governed by the order $\beta$ of the local Taylor remainder, giving oracle complexity $\widetilde O(\varepsilon^{-(2+2/(\beta-1))})$: the first-order case $\beta=2$ recovers SmoothCruiser, while a second-order/cubic remainder $\beta=3$ yields $\widetilde O(\varepsilon^{-3})$. We reach this regime with an optimal-transport-smoothed Bellman backup over action distributions, which has a closed form, a policy gradient, and a Lipschitz Hessian, and whose quadratic correction admits an unbiased cross-product estimator. The resulting SecondOrderSmoothCruiser achieves $\widetilde O(\varepsilon^{-3})$ oracle complexity for fixed OT parameters, and we relate the OT, entropy-regularized, and unregularized objectives through explicit regularization-bias bounds.

---


### 155. [Power Mean Estimation in Stochastic Continuous Monte Carlo Tree Search](https://arxiv.org/abs/2609.06489)

**<font color=#1a73e8>作者：</font>** Tuan Dam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monte Carlo Tree Search (MCTS) has demonstrated success in online planning for deterministic environments, yet significant challenges remain in adapting it to stochastic Markov Decision Processes (MDPs), particularly in continuous state-action spaces. Existing methods, such as HOOT, which combines MCTS with the Hierarchical Optimistic Optimization (HOO) bandit strategy, address continuous spaces but rely on a logarithmic exploration bonus that lacks theoretical guarantees in non-stationary, stochastic settings. Recent advancements, such as POLY-HOOT, introduced a polynomial bonus term to achieve convergence in deterministic MDPs, though a similar theory for stochastic MDPs remains undeveloped. In this paper, we propose a novel MCTS algorithm, \Algname, designed for continuous, stochastic MDPs. \Algname integrates a power mean as a value backup operator, alongside a polynomial exploration bonus to address the non-stationarity inherent in continuous action spaces. Our theoretical analysis establishes that \Algname converges at a polynomial rate of $\mathcal{O}(n^{-\zeta})$, $\zeta \in (0,1/2)$, where \( n \) is the number of visited trajectories, thereby extending the non-asymptotic convergence guarantees of POLY-HOOT to stochastic environments. Experimental results on stochastic tasks validate our theoretical findings, demonstrating the effectiveness of \Algname in continuous, stochastic domains.

---


### 156. [Diffuse2Seg: Diffusion Models Can Segment Anything Without Supervision](https://arxiv.org/abs/2609.06491)

**<font color=#1a73e8>作者：</font>** Christoph Hümmer, Joachim Sicking, Fabian Hüger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world entity segmentation aims to predict masks for arbitrary objects across domains and at multiple granularities, from parts to whole objects. In this setting, SAM sets a strong standard: trained on SA-1B, comprising 11M images and over 1B carefully annotated masks, it achieves remarkable zero-shot performance. Collecting such labels is expensive and time-consuming, however, which limits how far this recipe can scale. Text-to-image diffusion models offer a way around this. Their intermediate features transfer well across perception tasks, and since object structure emerges as the model denoises a noise sample into an image conditioned on a text prompt, that structure is already encoded in these representations. They can therefore be exploited for open-world entity segmentation without retraining or supervision. Building on this observation, we introduce Diffuse2Seg, which repurposes generative diffusion models for automatic mask generation by propagating a grid of point prompts through their self-attention representations in an edge-preserving manner. Diffuse2Seg produces multi-granular instance masks and outperforms prior state-of-the-art label generators by 4.3-7.1 p.p. in AR_1000 across five domains. Training an instance segmentation model on these generated masks advances detector-free open-world segmentation by 7.4 and 7.7 p.p. on "things" and "stuff+things" datasets and surpasses the detector-based UnSAM on "stuff+things" by 2.1 p.p. in AR_1000. Finally, we show that a model trained on Diffuse2Seg labels provides a strong initialization for semi-supervised learning, outperforming its fully supervised counterpart with already 5k labeled images.

---


### 157. [Disclosure and dissolution: explainability, AI power, and situated agency in understanding](https://arxiv.org/abs/2609.06495)

**<font color=#1a73e8>作者：</font>** Dee Matthews  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper interrogates the political and philosophical stakes of AI through the lens of cyborg theory cosmotechnics and glitch feminism. It advocates for a tech-positive critically situated approach to AI as a collaborator and substrate for power relations rather than an autonomous agent of harm. By rejecting the naive pause stop narratives of the human AI binary and embracing an explainable AI XAI artistic practice within embodied intersectional and community rooted engagements AI can empower diverse voices and foster ethical creativity. It starts by examining a frontier cybersecurity AI situating its framing within AI public anxiety and arguing for a new critical stance on human navigation in an AI world.

---


### 158. [Structural Entropy-Driven Graph Diffusion Generation for One-Shot Federated Graph Learning](https://arxiv.org/abs/2609.06499)

**<font color=#1a73e8>作者：</font>** Shutong Zheng, Lele Fu, Sheng Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-shot federated graph learning (FGL) requires the server to estimate client contributions from highly compressed information, yet conventional volume-based weighting captures the amount of client data while overlooking how its connectivity is organized. In this paper, we propose SPIRE, a Structural Entropy-Driven Graph Diffusion Generation method that introduces topology-aware client differentiation into one-shot FGL. Specifically, we employ first-order degree-distribution structural entropy as a compact descriptor of degree-mass dispersion and use it to derive structural client weights, providing an inductive bias that accounts for differences in graph topology beyond data volume. On the generation side, a graph diffusion model on the server synthesizes pseudographs conditioned on the weighted client prototypes, capturing both semantic and structural information without requiring additional client-side training. The generated pseudographs are then assembled via disjoint union fusion to train a global graph neural network. Extensive experiments on seven real-world graph datasets demonstrate that SPIRE consistently outperforms conventional and one-shot FGL methods, with particularly strong gains under highly heterogeneous (non-IID) and graph-perturbed settings.

---


### 159. [CAPMAS: Capability-Based Delegation of Privileges in Multi-Agent Systems](https://arxiv.org/abs/2609.06500)

**<font color=#1a73e8>作者：</font>** Rasmus Moorits Veski, Rachid Guerraoui, David Froelicher  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agentic systems require secure and efficient delegation of privileges across multiple collaborating agents. Existing approaches fall into two categories. Some propagate user identities directly to agents, obscuring accountability and creating persistent over-privilege risks that are amplified by the non-deterministic behaviour of AI agents. Others rely on continuous synchronization with a central Identity and Access Management (IAM) provider, introducing additional latency and communication overhead.
We present CAPMAS, a novel architecture for secure end-to-end query execution in multi-agent systems. CAPMAS newly combines a contrastive learning-based semantic scoping pipeline that maps natural-language queries to bounded privilege sets before execution with expressive Macaroon-based tokens that enable offline, tamper-evident delegation with monotonic privilege reduction across agents. By decoupling authentication and delegation enforcement from agent reasoning, CAPMAS enables practical agentic execution while enforcing strict least-privilege guarantees.
By eliminating synchronous delegation exchanges with the IAM, CAPMAS yields 30 times faster delegation operations, 2 times less delegation-oriented latency and up to 3 times lower bandwidth usage than the OAuth 2.0 Token Exchange (RFC 8693). Its semantic scoping pipeline achieves over 90% perfect privilege-bundle retrieval within 17 milliseconds on enterprise-scale API schemas containing over 3,100 endpoints, while reducing unnecessary privileges by 99.5% when compared to systems that propagate all the user's privileges to agents.

---


### 160. [A Cloud-Based Hybrid Model for Real-Time Detection of BRTA-Approved Licence Plates Using YOLO Tiny and Haar Cascade](https://arxiv.org/abs/2609.06507)

**<font color=#1a73e8>作者：</font>** Debashis Kar Suvra, Tahsina Farah Sanam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate vehicle license plate detection is essential for applications such as intelligent transportation systems, toll collection, parking management, and law enforcement. In Bangladesh, this task presents distinct challenges due to the complexity of localized license plates and environmental factors like lighting, occlusion, motion blur, and obstructions such as dirt or mud. These challenges often render conventional methods ineffective. This paper introduces a novel hybrid approach, combining the YOLO Tiny deep learning model with the Haar-Cascade classifier, for enhanced detection and localization of Bengali license plates. A key innovation of our system is the integration of a dynamic retraining pipeline, which allows the model to adapt to evolving real-world conditions. This retraining mechanism significantly boosts performance in low-confidence scenarios by continuously improving the model's accuracy as new data is encountered. Additionally, a publicly accessible dataset of BRTA-compliant license plates, captured under diverse and challenging conditions, has been developed to support this approach. Experimental results demonstrate that our approach not only achieves superior detection accuracy and computational efficiency over conventional models but also ensures consistent performance in resource-constrained environments, particularly in Bangladesh.

---


### 161. [Bi-HYCO: Bi-Objective Cooperative Learning for PDE Parameter Identification under Fragmented Observations](https://arxiv.org/abs/2609.06511)

**<font color=#1a73e8>作者：</font>** Umberto Biccari, Jun Chen, Roberto Morales 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical and synthetic models may describe complementary aspects of the same PDE-governed system while receiving different, possibly fragmented, observations. We propose Bi-Objective HYCO (Bi-HYCO), a cooperative framework that retains both representations and their local observational objectives while coupling their predicted states at unlabeled interaction points. These points contain no measurements and do not augment the data; they provide a communication mechanism in the common state space. The two criteria form a vector-valued objective, and weighted scalarizations provide computational realizations. For the deterministic shared-observation algorithm with fixed interaction points, we prove sufficient decrease and finite length of the whole alternating sequence, which converges to a mixed critical point under the stated Kurdyka-Lojasiewicz-type assumptions. Elliptic transmission and two-dimensional Navier-Stokes experiments assess parameter and state reconstruction, noise and scalarization effects, and PINN/XPINN references. Ablations show that removing state interaction while retaining aggregation deteriorates parameter recovery in the tested configurations, particularly for Navier-Stokes.

---


### 162. [Model-Adaptive and Risk-Constrained Frequency Hopping Against Predictive Jammers](https://arxiv.org/abs/2609.06514)

**<font color=#1a73e8>作者：</font>** Yanbo Chen, Xinjing Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive frequency hopping against predictive jamming must address both model uncertainty and policy exposure: the context-loss relationship may vary across operating regimes, while persistent hopping patterns may expose high-probability channels to attack. We propose D-PACT-AFH, a model-adaptive and risk-constrained adversarial contextual-bandit framework in which a Tsallis-FTRL master combines a global linear learner with a partitioned local learner and selects the model class online. D-PACT-Hit incorporates channel-wise marginal hit risk into model selection, while D-PACT-Safe applies a minimum-Kullback-Leibler projection to enforce a per-slot risk budget. We establish estimator validity under non-anticipating attacks, an oracle decomposition relative to the better fixed base, and an exact conditional-risk guarantee for the Safe projection. Experiments across diverse channel regimes and jammer types demonstrate effective model adaptation and a controllable goodput-risk tradeoff: D-PACT-AFH recovers 95.5% of the local learner's gain under observable switching while avoiding 77.7% of its degradation in a negative-control regime.

---


### 163. [Role-Specific Predictive Geometries for Nonstationary Multivariate Graph-Signal Forecasting](https://arxiv.org/abs/2609.06519)

**<font color=#1a73e8>作者：</font>** Yanbo Chen, Anamitra Makur  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting multivariate graph signals is challenging when node-level trajectories are nonstationary but stable relations persist across nodes and features. In an error-correction representation, long-run equilibrium restoration and short-run transient propagation represent different predictive roles and need not share a common cross-feature geometry. We introduce role-specific predictive geometries in which directed Long relations act on estimated equilibrium coordinates, whereas directed Short relations act on lagged differences. Matrix-valued Long responses mix equilibrium coordinates before graph propagation, while Short responses use graph-filtered transient designs; a direct multi-horizon estimator couples forecast corrections across adjacent horizons. Temporal cross-fitting and Frisch-Waugh-Lovell partialling-out give selected edges a conditional predictive interpretation relative to a graph-temporal backbone. The Long operator remains right-factorized through the equilibrium subspace and therefore annihilates source common-trend directions. Controlled experiments recover all planted Long relations (20/20), all planted Short relations (20/20), and both role families in every Dual realization (10/10). Across four real-world benchmarks, the proposed predictor improves on the G-VARMA backbone in three datasets, with all 25 fold-horizon comparisons favorable on the five-fold financial benchmark.

---


### 164. [Not Just Oversmoothing: Detecting the Echo Chamber Effect in Graph Neural Networks](https://arxiv.org/abs/2609.06521)

**<font color=#1a73e8>作者：</font>** Asela Hevapathige, Ahad N. Zehmakan, Asiri Wijesinghe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Oversmoothing is a well-known failure mode of Graph Neural Networks (GNNs). However, most existing diagnostics rely on global aggregation measures that fail to capture the heterogeneous dynamics of message passing. Real-world graphs exhibit pronounced community structure, and message passing operates on two timescales, with representations collapsing rapidly within communities and slowly across them. This creates a critical gap in which intra-community representations can become indistinguishable while inter community separation persists, a failure mode that we refer to as the Echo Chamber Effect. To quantify this effect, we introduce the Echo Chamber Index (ECI), which stratifies pairwise distances by community membership and reveals when global energy diminishes while inter-community separation persists. ECI further shows that feature retention mechanisms can preserve the echo chamber under the conditions of our theoretical analysis. The consequences depend on label structure: when communities align with classes, the echo chamber can sharpen node classification, whereas when they do not, the same collapse makes classification provably harder. Motivated by this analysis, we propose Community-Aware Split Propagation (CASP), a lightweight plugin that decouples intra- and inter-community aggregation and learns their balance from label structure. CASP improves diverse backbone GNNs across most evaluated homophilic and heterophilic settings.

---


### 165. [Selective Knowledge Control for Continual GUI Agent Learning over Application Streams](https://arxiv.org/abs/2609.06530)

**<font color=#1a73e8>作者：</font>** Zirui Shang, Xin Shu, Yang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual learning is a crucial capability for Graphical User Interface (GUI) agents to adapt to evolving applications while retaining knowledge acquired from previous applications. Such application streams pose a challenging knowledge modeling problem: new applications often share underlying knowledge with past ones, yet also introduce specific knowledge that must not interfere with historical knowledge. In this paper, we propose activation-conditioned selective knowledge control, a lightweight method that achieves selective knowledge retention via neuron-level gradient manipulation. Our method maintains a compact historical knowledge state to protect highly activated MLP neurons that preserve previous knowledge. When a new application arrives, it performs real-time gradient surgery conditioned on forward activation. Concretely, the protected neurons are categorized into two types: unactivated neurons holding specific knowledge, whose gradients are truncated to prevent interference; and activated neurons holding shared knowledge, whose gradients are orthogonally projected to preserve stability while enabling adaptation. After each application stage, newly identified critical neurons are merged into the historical state for future learning. Empirical evaluations on multi-app sequential benchmark demonstrate that our method effectively mitigates catastrophic forgetting on prior applications while sustaining robust adaptation to new ones.

---


### 166. [Watch and Crack: Password Inference from Smart-Glasses Video](https://arxiv.org/abs/2609.06539)

**<font color=#1a73e8>作者：</font>** Yoav Orenbach, Avishai Wool  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Typing passwords on smartphones in public places exposes users to video-based side-channel attacks, in which an adversary records the typing session and reconstructs the entered password by analyzing finger movements. Prior video-based keystroke inference attacks have targeted free-form text on tablets, numeric PINs, pattern locks, and passwords under unrealistically simplified conditions.
We present the first general video-based keystroke inference pipeline that recovers rule-based alphanumeric passwords from smartphone QWERTY keyboards, covering all four keyboard layouts and requiring no assumptions about the victim or their device. Using the built-in camera of the popular Meta Ray-Ban smart glasses, our pipeline tracks the device and typing fingertips at sub-pixel resolution, predicts keystrokes via a self-supervised ensemble of neural networks, dynamically estimates the on-screen keyboard layout, and computes per-key probability distributions. These video-derived probabilities are combined with prior password-typing distributions based on 2.19 billion leaked passwords to estimate the rank, and therefore the crack time, of the observed password.
In a user study using passwords that adhere to a typical enterprise password policy, human-chosen passwords of up to 16 characters can be cracked in hours to days, and password-manager-chosen random passwords of up to 13 characters in under an hour on a modern GPU, reducing password entropy by up to 60 bits relative to the prior baseline. For human-chosen passwords, combining video evidence with prior statistics yields an additional statistically significant reduction of approximately 20 bits compared to either source alone. The attack succeeds at distances up to 1.8 m, across diverse attacker-victim postures and viewing angles, and generalizes across three popular smartphones.

---


### 167. [A Unified Policy Architecture (UPA): The Governance Kernel for Enterprise AI Operating Systems](https://arxiv.org/abs/2609.06543)

**<font color=#1a73e8>作者：</font>** Prabhu Raghav, Balamurugan Pandi, Arul Vivek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise AI is evolving into an Enterprise Operating System where autonomous AI agents can plan, reason, use memory, invoke tools, execute workflows, and collaborate with other agents. This shift creates a new governance challenge: existing authorization, security, guardrails, and compliance mechanisms are fragmented and are not designed to govern autonomous AI as a unified system.
This paper introduces the Unified Policy Architecture (UPA), a governance architecture for Enterprise AI Operating Systems. UPA provides a unified policy model for governing AI and agents, tools, workflows, memory, enterprise resources, and agent-to-agent interactions and enterprise business rules. It extends policy control beyond authorisation to include runtime obligations, human approvals, compliance, audit evidence, and governance evaluation.
We present UPA's governance model, declarative policy language foundations, policy evaluation semantics, extensible plugins, industry policy packs, and an evaluation framework for enterprise governance. We also identify extensions for multi-agent coordination, provenance-aware policies, and stateful runtime governance. UPA provides a foundation for building secure, accountable, and governable Enterprise Operating Systems for autonomous AI.

---


### 168. [A Translational Note on AI Safety Evaluation](https://arxiv.org/abs/2609.06573)

**<font color=#1a73e8>作者：</font>** Madhava Gaikwad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent studies report that automated red-teaming finds more vulnerabilities, at lower cost, than human red-teaming on standard AI safety benchmarks, and some read this as evidence that human evaluators are becoming dispensable. The comparison measures one thing and the conclusion claims another. A benchmark measures how thoroughly an attacker searches a predefined set of harms, fixed in advance by the developers, and a harm left out of that set is invisible to any attacker working inside it, automated or not. The same blind spot appeared in academic cryptography and in clinical drug trials, where an evaluation that was internally valid stayed silent about the population it was never pointed at. We call the AI-safety version the \emph{threat-model coverage gap}, and find that it persists in a current open-weight model, where harms surface in non-English prompts that English benchmarks miss. Closing it requires evaluators whose deployment context differs from the developers'. The case for those evaluators is methodological, grounded in coverage, and the existing evaluation frame is unlikely to produce them on its own.

---


### 169. [A TTP by TTP Approach: Precise Malware Detection via Malicious TTP Recognition](https://arxiv.org/abs/2609.06579)

**<font color=#1a73e8>作者：</font>** Yashovardhan Sharma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning methods, and especially neural networks, are now routinely used for malware detection in network traffic. Though very effective, systems based on such methods often (i) are purely data-driven, ignoring the substantial body of available knowledge about the tactics, techniques, and procedures (TTPs) possibly used, and, consequently (ii) are not precise, since they either cannot correlate malicious activity with TTP usage, or if they do, they are unable to explain which TTP has been maliciously used. In this paper we demonstrate that it is possible to precisely detect malware by (i) providing the neural network model with information about the TTPs used by any given sample, and (ii) teaching the neural network to detect not just the malicious activity as a whole, but which specific TTPs are maliciously used. We show that our approach consistently outperforms the three alternative models, which either do not exploit TTP information, or which are not taught to detect the malicious usage of TTPs, or both. Moreover, we show that our approach (i) is particularly beneficial in detecting malware that utilises rarely-used TTPs, a scenario which is particularly challenging for the other systems; (ii) allows for TTP by TTP tuning, further improving its ability to detect the malicious usage of TTPs; (iii) consistently outperforms other systems across a wide-range of scenarios, including when relying on limited training data or when subjected to adversarial attack.

---


### 170. [Reading Decoder Trajectories: Training-Free Counterfactual Query-Trajectory Reliability for Small-Object Detection](https://arxiv.org/abs/2609.06581)

**<font color=#1a73e8>作者：</font>** Zhaoning Shi, Bo Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small-object detection remains challenging because limited pixels cause information loss and suppress the scale knowledge encoded in pretrained detectors. Existing approaches mainly improve representations through multiscale training, architecture redesign, or parameter adaptation, implicitly assuming that frozen models lack the required capability. We challenge this assumption and hypothesize that small-object knowledge already exists in frozen detectors but remains underactivated and unstable during query evolution. To test this hypothesis, we propose Counterfactual Query-Trajectory Reliability (CQTR), a training-free framework that elicits latent responses through counterfactual scale interventions and interprets candidate reliability from decoder-internal spatial convergence, semantic persistence, and cross-scale conflicts. A small unlabeled training subset selects the appropriate correction mechanism for each model-data stream, without parameter updates or target-domain annotations. Across 27 combinations of nine frozen detectors and three datasets, CQTR consistently improves average precision (AP) and average precision for small objects (APs). Closed-loop analyses further show that scale intervention activates latent responses, trajectory evidence predicts ground-truth support, and unlabeled routing selects the more effective branch. CQTR therefore reframes small-object detection from external scale augmentation to the activation and reliability assessment of latent scale knowledge.

---


### 171. [Certifying cooperation: a novel approach to cooperative multi-agent task generation](https://arxiv.org/abs/2609.06586)

**<font color=#1a73e8>作者：</font>** Yannick Molinghen, Hugo Charels, Tom Lenaerts  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A shared reward gives agents a common objective, but leaves open when, how and even whether they must cooperate to succeed. We address these questions in the Laser Learning Environment, a multi-agent path-finding environment where cooperation materializes as one agent blocking a laser to let a teammate pass safely. We represent these interactions through temporal cooperation graphs whose timed edges connect helpers to beneficiaries, define six cooperation profiles as overlapping graph predicates, and prove that every cooperative trajectory satisfies at least one. By encoding the environment dynamics and profile predicates as propositional formulae, we distinguish tasks that admit}a profile in some winning trajectory from those that require it in every winning trajectory within a specified horizon. Used as filters, these queries turn a random layout sampler into a generator of tasks with certified cooperation requirements. Experiments with five multi-agent reinforcement learning algorithms show that training diversity improves joint success on unseen tasks when cooperation-free solutions exist. When cooperation is required, greater diversity improves individual-agent exits, but joint success remains near zero. Across five profile-certified pools, final exit rates averaged over algorithms separate the pools into four statistically distinguishable levels but this ordering primarily reflects partial completion: policies collect rewards for individual exits but rarely exhibit the profile required for joint success. Our framework exposes this gap between rewarded partial completion and realized cooperation by certifying what cooperation successful completion requires and using temporal cooperation graphs to reveal what policies exhibit.

---


### 172. [Layer-Wise Gate-Controlled Prompt Truncation in a Multimodal Chest X-Ray Classifier](https://arxiv.org/abs/2609.06590)

**<font color=#1a73e8>作者：</font>** Jingtao Lei, Hongji Li, Dexiang Shu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture of Prompt Experts (MoPE) adapts multimodal transformers through input-dependent prompt composition, while retaining a fixed prompt length. We investigate a layer-wise gating extension in a binary chest X-ray classification pilot study. The controller predicts a retention ratio for each sample, averages these ratios within a mini-batch, and uses the resulting integer length to truncate the static and mixed visual prompts. Retained mixed prompts are also scaled by the individual ratios. In one recorded run per configuration, the gated model reached a best validation accuracy of 0.8996, compared with 0.8969 for the fixed-length baseline; the corresponding final values were 0.8963 and 0.8802. The exported gate statistics imply a retained length of one at all recorded training points, relative to a configured maximum of six. This reduces the complete visual sequence from 210 to 200 tokens, but no direct runtime measurements establish an acceleration benefit. Report-derived labels, report text as input, sequential data partitioning, and the absence of repeated controlled experiments limit interpretation. The findings document prompt shortening under the configured gate penalty; they do not establish sample-specific length allocation, superiority over fixed short prompts, or clinical utility. Code is available at: this https URL.

---


### 173. [Discovering Translation-Worthy Languages with E-Values](https://arxiv.org/abs/2609.06593)

**<font color=#1a73e8>作者：</font>** Wajdi Ben Saad, Safa Madiouni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Choosing when to translate multilingual documents is a central routing problem in text classification: translation can improve predictions for some languages while degrading others or adding unnecessary computation. Uniform translation and heuristic language tiers do not provide statistically controlled route selection. We introduce a language-level router based on paired e-processes that continuously compares direct and translation-assisted classification before freezing a routing policy. A familywise-controlled threshold of 280 bounds the probability of any false route across 14 eligible languages per dataset by 0.05. On SIB-200 and MASSIVE, the router selects translation for 4 of 15 languages and 14 of 15 locales, improving held-out accuracy over direct classification by 8.14 and 16.70 percentage points, respectively. All 28 decisions remain stable across 50 outcome-independent orderings and relative to the per-group threshold. Our results demonstrate that paired e-processes enable statistically controlled, anytime-valid, and auditable multilingual classification routing.

---


### 174. [Federating Trust Perimeters: Extending Industry IAM with DLT-Based Governance](https://arxiv.org/abs/2609.06595)

**<font color=#1a73e8>作者：</font>** Carlo Segat  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital systems are becoming more integrated, autonomous, and cooperative. AI agents, future mobile networks, and machine-to-machine economies point to one trend: spontaneous, cross-organizational, unplanned interactions between non human entities (NHEs). Trust establishment for them remains an open problem. Federation is the natural candidate, but established approaches, from OpenID Federation 1.0 and SAML to Federated Identity Management, presuppose what this setting denies them: manual, ahead-of-time configuration and a common trust anchor, whether pre-established members or a shared provider. Trust domains must therefore federate without being prefigured to do so: plan for unplanned interactions. This paper examines whether prominent Identity and Access Management (IAM) approaches, namely SPIRE, Workload Identity Federation (WIF), and OpenID Federation 1.0, can support such federation. Drawing requirements from disparate fields (medical, mobile networks, agentic AI), it argues that SPIRE is the most promising starting point, but needs three extensions to meet them all: token exchange, letting a home domain mint scoped, audience-bound tokens from a foreign workload's SPIFFE Verifiable Identity Document (SVID); remote attestation, so a trust decision targets a specific workload rather than a whole domain; and a distributed-ledger layer that anchors trust roots, carries federation governance, and publishes the shared keys the other two depend on.

---


### 175. [Deep Barycentric Regression for Optimal Transport Map Estimation and its Statistical Optimality](https://arxiv.org/abs/2609.06598)

**<font color=#1a73e8>作者：</font>** Kunwoong Kim, Insung Kong, Yongdai Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The optimal transport (OT) map provides a geometric transformation for aligning probability distributions and has become a useful tool in machine learning. However, existing estimators of the OT map still exhibit a gap between sharp statistical guarantees and practical parametric estimation based on stable training objectives. Theoretical estimators achieve minimax optimal convergence rates, but they are typically nonparametric and can incur demanding implementation design or inference costs. Practical estimators are parametric and scalable, but their statistical guarantees remain underexplored, and their min-max, adversarial-like training objectives can be sensitive to optimization algorithms. We propose BROT (Barycentric Regression for OT), a simple two-step method that first computes the unregularized OT plan and then fits a deep neural network (DNN) to the induced barycentric targets by least-squares regression. Under standard regularity conditions, we prove that the DNN estimator of BROT attains the minimax convergence rate, when the ground-truth OT map is Lipschitz. Numerical studies on synthetic datasets and an image dataset show that BROT provides accurate map estimates, strong target distribution matching, and competitive transport costs, compared to existing estimation methods. Experiments on two downstream tasks, single-cell perturbation prediction and unsupervised domain adaptation, further suggest that the accurate estimation of BROT can translate into stronger task performance.

---


### 176. [Multi-History-Step SDE Inversion for Image Editing with Superior Regional Awareness](https://arxiv.org/abs/2609.06602)

**<font color=#1a73e8>作者：</font>** Haiyan Wei, Yunlong Wang, Huaibo Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, diffusion stochastic differential equation (SDE) inversion and inversion-free methods have become prevalent for training-free image editing, as they can achieve faithful reconstruction without tuning. However, existing approaches remain inefficient, exhibit limited plasticity, and struggle to accurately preserve unedited regions. To address these issues, we propose MIEdit, a training-free editing framework based on SDE inversion. MIEdit introduces a predictor-corrector multi-history-step scheme to achieve superior editing quality with fewer steps. We further mitigate heterogeneity and conflict between the multi-conditioned noise residuals and gradient terms during sampling, improving stability and editing plasticity under large edits. MIEdit also includes Inversion-Time Automatic Semantic Angle Masking (IASM); it leverages classifier-free guidance to automatically generate semantic angle masks during inversion and applies them throughout the sampling process for regional constraints, without extra user inputs. We additionally construct EditEval++ (30 fine-grained tasks, 1,000+ image-text-mask triplets) for comprehensive evaluation; experiments show that MIEdit outperforms state-of-the-art techniques. Project page: this https URL.

---


### 177. [A Statistical and Machine Learning Framework for Quantifying Offensive Impact in Professional Box Lacrosse](https://arxiv.org/abs/2609.06610)

**<font color=#1a73e8>作者：</font>** Robert Jimerson Jr  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Professional box-lacrosse statistics summarize outcomes but provide limited information about shot quality or the roles behind scoring opportunities. This study develops a documented framework for estimating expected goals (xG) and attributing recorded offensive involvement using 1,006 manually annotated Rochester Knighthawks shot attempts, including 151 goals, from 13 consecutive 2025-2026 National Lacrosse League games. Logistic regression, random forest, and extremely randomized trees were evaluated across three nested feature sets using Leave-One-Game-Out cross-validation and a training-fold base-rate benchmark. The contextual baseline random forest had the lowest observed pooled log loss (0.4189) and Brier score (0.1260), improving on the benchmark by 1.22% and 1.50%; five of nine specifications did not beat the benchmark. Adding two-man-action and pick-type fields did not improve the primary metrics. Core Offensive Impact attributes recorded involvement through shooter xG and shot-based expected assists for final passers. Expected Pick Value (xPV) compares a qualifying pick's observed-state probability with a no-pick counterfactual. Its magnitude was indistinguishable from model noise. Its directional pattern exceeded 200 row-permutation replicates, but limited tail resolution and failure to preserve game-level pick composition make the diagnostic descriptive rather than inferential. Accordingly, xPV is reported only as an exploratory augmented component. Given the single-team, 13-game sample, the results are an initial case study rather than league-wide or causal estimates.

---


### 178. [GAN-Blot: A Controllable Structure-Style Synthesis Benchmark for Western Blot Forensics](https://arxiv.org/abs/2609.06619)

**<font color=#1a73e8>作者：</font>** Hao-Chiang Shao, Fong-Yi Lin, Te-An Chien 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Western blot (WB) images are widely used as key evidence in biomedical research. Recent scientific misconduct cases reveal that WB imagery is increasingly fabricated, making WB forensics a major concern for research integrity. However, while the progress of forensic detection techniques often relies on advances in forgery-generation techniques, the development of WB forensic techniques has been hindered by the lack of standardized appearance attribute definitions, image datasets, and controllable generation frameworks for WB imagery. To address this limitation, we present a controllable WB image synthesis framework, named GAN-Blot, for generating realistic synthetic WB images. We introduce a formulation that decomposes a WB image into a structure component and a style-reference component, enabling independent control over local protein-band geometry and the global visual appearance of a synthetic WB image. GAN-Blot integrates a dual-path autoencoding design with several style-alignment loss terms to enable implicit control over structure-style synthesis without predefined semantic appearance attributes. We further contribute a synthetic WB dataset containing more than 46K images and propose four evaluation protocols for controllable WB synthesis. Extensive experiments show that GAN-Blot can generate WB images with high fidelity in both protein-band structure and visual style. Under blind inspection, the generated images can fool domain experts and are not reliably distinguished from authentic WB images by existing detectors and screening platforms. These results demonstrate their utility as challenging controlled cases for validating and developing WB forensic methods.

---


### 179. [GeoCo-SAVi: Geometry-Consistent Slot Attention for Explicitly Editable Object Representations](https://arxiv.org/abs/2609.06628)

**<font color=#1a73e8>作者：</font>** Haoxiang Huang, Zhekai Wang, Xiang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-centric video models represent scenes with slots, yet exposed geometry can vary in meaning with appearance. In Invariant Slot Attention (ISA), explicit position and scale can disagree with the decoded center and extent; edits can yield unexpected motion or resizing, and replacing appearance can shift geometry.
GeoCo-SAVi promotes geometric authority and semantic alignment. Its spatially equivariant, object-wise decoder makes position and scale effective commands: changing them moves or resizes the rendered support. Factual position alignment ties position to the decoded center, and normalized attention overlap discourages duplicate allocation. Appearance transplantation aligns geometry semantics across objects, so recipient geometry governs layout while donor appearance supplies shape. A temporal initializer propagates calibrated slots across frames.
On Obj3D, GeoCo-SAVi matches ISA reconstruction, reduces p-centroid error by over 80%, and cuts appearance-induced size variation by over 50% while producing the expected translation and scale responses. On 250 MOVi-C videos, it also improves reconstruction, instance grouping, and fixed-identity geometry control over two same-protocol references. GeoCo-SAVi transforms explicit geometry into compositional control, making both position and scale more readable and editable.

---


### 180. [MARR: Decoupling Policy, Execution, and Calibration for All-in-One Medical Image Restoration](https://arxiv.org/abs/2609.06645)

**<font color=#1a73e8>作者：</font>** Haobin Chen, Ao Chang, Heqin Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> All-in-one medical image restoration seeks to recover heterogeneous clinical images with a single model, but PET, CT, and MRI differ substantially in degradation statistics, anatomical contrast, and output-space bias. A fully shared network can entangle modality-specific residual errors, whereas separate modality-specific networks sacrifice the practical advantages of unified deployment. We therefore recast all-in-one restoration as a question of where limited adaptation should be placed: policy selection, feature execution, or output calibration. We propose MARR, a compact restoration framework that constrains multi-modality adaptation into degradation-aware policy routing, modality-private residual execution, and image-domain residual correction without requiring degradation labels or separate modality-specific models. The policy branch forms a routing prompt from input statistics, latent content, and modality identity, and uses it only as a control signal. Prompt-gated modality-private adapters then perform lightweight residual refinement at intermediate decoder stages, while zero-initialized modality-specific output heads calibrate the final image-domain residual without perturbing the initial shared prediction. On an all-in-one PET, CT, and MRI restoration benchmark, MARR outperforms thirteen methods re-trained under the same protocol, achieving PSNR values of 37.34 dB, 33.85 dB, and 32.09 dB on PET, CT, and MRI, respectively, and the best modality-average PSNR of 34.43 dB. The code is publicly available at this https URL.

---


### 181. [When Does a Laugh Begin? Structured Annotator Disagreement in Temporal Laughter Localization](https://arxiv.org/abs/2609.06646)

**<font color=#1a73e8>作者：</font>** Eyal Hanania, Daniel Arkushin, Naveh Ayal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Annotators routinely disagree on laughter boundaries and subtle chuckles, yet temporal laughter localization typically evaluates against a single reference annotation. We show that this disagreement is structured rather than random noise. Re-annotating the SMILE-Temporal benchmark (672 videos, 1,683 events) with 3-5 annotators per video (alpha = 0.757), we find systematic patterns: disagreement is 1.73 times larger at offsets than onsets, far more common for chuckles than full laughs (77% vs. 20%), and predictable from event attributes (AUC = 0.831). Evaluating against a single annotator breaks down under this structure: system scores shift by 0.246 F1 depending on the chosen ground truth, correctly ranking systems only 69.7% of the time (vs. 80% against all annotators). We propose a disagreement-calibrated evaluation that scores predictions against the full annotator distribution using conformally calibrated tolerance bands (wider at offsets, 0.727s, than onsets, 0.5s). The per-annotator annotations and analysis code are available at this https URL .

---


### 182. [SwiftExplorer: Training-free Diffusion Model Alignment with Swift Diversity Exploration](https://arxiv.org/abs/2609.06651)

**<font color=#1a73e8>作者：</font>** Renye Yan, Jikang Cheng, You Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have general generative abilities but struggle to align with specific objectives. Fine-tuning can improve alignment, yet its training cost is often prohibitive. This led to training-free methods that apply objective-guided terms in sampling to bias the generation distribution toward designated regions, e.g., high-reward areas. However, these methods face two issues: (1) the strong directional bias narrows the pretrained distribution and generation diversity, and (2) indiscriminate constant guidance fails to prune redundant signals, hurting both quality and efficiency. To address the above challenges, we propose SwiftExplorer, a plugin that mitigates distribution collapse caused by excessive diversity loss and reduces compute costs. First, we adopt an Inheritance-Restart exploration mechanism to avoid early convergence, while exploration also increases the likelihood of high-reward trajectories. Additionally, it balances diversity and fidelity, adding diversity without causing a distribution over-shift. Second, our Quality-Efficiency arbitration mechanism improves guidance by removing incorrect signals, and it reduces computation by dynamically stopping generation when completeness and marginal reward gain are optimal. In an extensive number of experiments and different types of evaluation metrics, the proposed SwiftExplorer achieves excellent performance on all metrics, including preference, fidelity, diversity, and richness.

---


### 183. [VidaForge: Open Research Infrastructure for Video Pretraining Data Recipes](https://arxiv.org/abs/2609.06652)

**<font color=#1a73e8>作者：</font>** Yan Ma, Jiadi Su, Zhulin Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video foundation models increasingly rely on large-scale pretraining data, yet the end-to-end data pipelines behind them remain largely closed and difficult to inspect or reuse. Researchers seeking to understand how video data recipes affect model pretraining often need to build substantial infrastructure before testing even a focused hypothesis. We present VIDAFORGE, an open research infrastructure that represents a video data recipe as an executable five-stage workflow from raw videos to training datasets. A decision in this workflow can be varied to construct alternative datasets while preserving how every sample was produced. To demon strate this research workflow, we compare data recipes with different coverage and quality in early from-scratch pretraining of Wan 2.1 and V-JEPA 2.1. Across both learning objectives, the broader-coverage recipe achieves the highest downstream benchmark scores, while loss-based evaluation favors different recipes. This study demonstrates how VidaForge connects data-recipe choices to downstream model performance. We further release VIDAFORGE-3M, containing 3.14 million scene level clips totaling 6,475 hours, with fine-grained annotations and curation signals for video data-recipe research.

---


### 184. [A Computational Implementation of a Goal-Directed Theory of Affect](https://arxiv.org/abs/2609.06654)

**<font color=#1a73e8>作者：</font>** Bernhard Hilpert, Tamás Szűcs, Joost Broekens 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computational modeling of emotion has long faced a tension between descriptive, "snapshot-based" appraisal models and granular, signal-driven architectures that often lack appropriate psychological grounding. This paper addresses this gap by presenting the first high-fidelity computational implementation of the Goal-Directed Theory (GDT) of affect. In this framework, affect is not a post-hoc label but a functional byproduct emerging from the continuous interplay between discrepancy detection and action selection within an agent's internal processing cycles. We evaluate the model through a series of principled simulations (Dice/Corridor tasks) designed to isolate affective signatures and dynamics during multi-step goal pursuit. Results demonstrate that complex affective profiles, like an anticipatory "lift" and a failure "crash", emerge naturally from simple interactions between goal-discrepancy and action-selection expectancies without requiring additional dedicated modules. By ensuring every computational component maps directly to components of the psychological theory, this work establishes a transparent, testable framework that enables a continuous "simulation-empiry" research loop. Our work contributes to moving the field beyond "black-box" heuristics toward a granular, mechanistic understanding of affect, integrated into the core of agent behavior.

---


### 185. [FSAN: Flow State Attention Network for Aerodynamic Prediction](https://arxiv.org/abs/2609.06660)

**<font color=#1a73e8>作者：</font>** Wenxuan Jin, Jianguo Yao, Haibing Guan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate aerodynamic prediction is critical for designing fuel-efficient and safe transportation systems such as aircraft and automobiles, yet traditional computational fluid dynamics (CFD) simulations remain computationally expensive and expertise-intensive, severely limiting their use in iterative design and real-time analysis. Existing deep learning surrogates suffer from two major limitations: (i) they are evaluated on datasets with narrow flow-condition ranges, leaving their performance under complex flow conditions undemonstrated; (ii) they treat global flow conditions as a single vector injected uniformly across all surface points, ignoring that different geometric regions experience distinct local flow phenomena, which degrades prediction accuracy under complex flow conditions. To address these limitations, we propose the Flow State Attention Network (FSAN). FSAN separately encodes point cloud and flow conditions, then partitions the geometry into multiple flow states via learnable soft assignments, and uses flow features to update these state representations, which in turn influence point cloud features through state changes. This enables fine-grained, state-specific interaction between geometry and flow information. Extensive experiments on two well-recognized aerodynamic benchmarks demonstrate that FSAN achieves the highest accuracy among the methods compared in this work at a higher computational cost. On Emmi-Wing, FSAN reduces the Relative L2 (REL-L2) error by over 20\% compared to the strongest baseline (Transolver), and on DrivAerNet++, it achieves a 10\% reduction compared to the strongest baseline (AdaField). These results establish FSAN as a promising neural surrogate on public benchmarks with diverse flow conditions and geometries.

---


### 186. [The Effectiveness of Virtual Patient Simulation Versus Peer Simulation in Providing Sexual Counseling During Pregnancy: A Randomized Controlled Trial](https://arxiv.org/abs/2609.06662)

**<font color=#1a73e8>作者：</font>** Neslihan Yilmaz Sezer, Menekşe Nazlı Aker, Pinar Kullu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Although sexual health counseling is one of the important responsibilities of healthcare professionals, effective educational methods are needed to develop students' counseling skills in this field. The aim of this study was to compare the effectiveness of virtual patient simulation and peer simulation methods in developing sexual counseling skills during pregnancy among nursing faculty students. This randomized controlled trial included 51 participants assigned to one of three groups: virtual patient simulation, peer simulation in a virtual environment, or face-to-face peer simulation. In the study, all groups received face-to-face theoretical instruction on sexual counseling during pregnancy. Following the theoretical training, students participated in virtual patient simulation, peer simulation in a virtual environment, or face-to-face peer simulation practices according to the groups to which they were assigned by randomization. Outcome measures included the Sexual Attitudes and Beliefs Scale, the Student Satisfaction and Self-Confidence in Learning Scale, and the Sexual Counseling Skills Evaluation Form. It was determined that the participants' SABS scores decreased significantly after the intervention. According to the results of the mixed repeated-measures ANOVA, the effect of time was statistically significant. However, the group effect and the group x time interaction were not significant. There was no difference between the groups in terms of Satisfaction in learning, Self-confidence in learning, and Skill scores. This study showed that different simulation methods used in sexual counseling education during pregnancy were effective in reducing students' negative attitudes and beliefs and provided similar educational outcomes. Therefore, virtual patient and peer simulations may be recommended as feasible approaches for improving sexual counseling skills.

---


### 187. [TransNormal-2: Geometry-Grounded Rectified Flow with Edge-Aware Decoding for Precise Normal Estimation](https://arxiv.org/abs/2609.06665)

**<font color=#1a73e8>作者：</font>** Mingwei Li, Yi Yang, Hehe Fan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based models enable monocular geometry estimation, yet their pixel-space precision is limited by a shared, under-studied error source: VAE reconstruction degradation. The 8x spatial compression in the VAE encoder-decoder degrades surface normals at object boundaries; even encoding and decoding ground-truth normals introduces 1.3--8.5° of mean angular error (MAE), with edge MAE reaching 2.8x the global MAE. We present TransNormal-2, a FLUX.2-based rectified-flow framework with single-step deterministic inference that addresses this degradation on both sides of the VAE decoder: in how latent predictions are supervised during training, and in how decoded normals are corrected at inference. First, geometry-aware pixel-space losses, including inverse rendering self-consistency, von~Mises-Fisher angular loss, and wavelet edge-aware regularization, complement latent MSE by enforcing spherical normal geometry and diffuse image-formation cues after VAE decoding. Second, a lightweight Geometric Refinement Module (GRM) applies an RGB-guided residual correction to reduce boundary-localized decoding errors without freely rewriting the coarse prediction. On general-scene benchmarks, TransNormal-2 matches or exceeds MoGe-2 on all eight reported metrics while using only 1.4% as many task-specific normal annotations. The gains are clearest for transparent objects, reducing MAE by 4.2° on ClearGrasp and 3.1° on ClearPose over the strongest prior baselines. Code will be released at this https URL.

---


### 188. [Behavioral Cloning Outperforms Entropy-Regularized RL: Critic-Driven Failure of Actor-Critic Methods on Adaptive Tumor Treatment](https://arxiv.org/abs/2609.06667)

**<font color=#1a73e8>作者：</font>** Aleksandar Dimitrov, Giacomo Spigler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive dosing requires policies that reduce tumor burden without excessive toxicity. Learned dosing policies are typically judged against historical or heuristic comparators, which cannot show whether a policy has found the best behavior available. We instead study a three-population tumor-control ODE in which optimal-control analysis fixes the form of a good schedule -- bang-bang dosing punctuated by a singular arc -- and construct a numerical controller of that form as a proxy for near-optimal behavior. Judged against this reference under a sustained-cure criterion -- 200 consecutive days below 5% carrying capacity -- Soft Actor-Critic (SAC) trained from scratch never reaches cure. Behavioral cloning (BC) of the reference reproduces it (100% sustained cure, 30/30 seeds), but SAC fine-tuning of the cloned policy destroys it across five entropy coefficients, and TD3 and BC-regularized SAC fail identically; the pattern persists under multiplicative pharmacokinetic action noise. Along curative trajectories the post-collapse critic ranks the collapsed-policy action above the reference action in 96% of states, concentrated in the maintenance phase, and the policy settles into a non-curative adaptive-therapy equilibrium. The reference is what makes this legible: against a heuristic comparator the fine-tuned policy would read as a competent controller rather than a failure.

---


### 189. [Tracking the Moving Frontier: Long-Short Term Advantage Estimator](https://arxiv.org/abs/2609.06671)

**<font color=#1a73e8>作者：</font>** Xinhao Yao, Lu Yu, Changhao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-based RLVR methods estimate advantages by repeatedly sampling multiple trajectories for each prompt, making long-horizon agent training expensive and discarding useful experience accumulated across iterations. We ask whether historical experience can replace these repeated within-iteration comparisons without directly optimizing on stale trajectories. We introduce Long-Short Term Advantage Estimator (LSTAE), a single-stream RL algorithm that uses history for advantage estimation while updating the policy only with the current rollout. LSTAE maintains a persistent tracker for each task anchor. At the trajectory level (long term), a drift-aware historical baseline tracks the anchor's moving success frontier and measures the relative contribution of each new trajectory. At the step level (short term), a recent state-experience buffer exploits recurrent states to estimate localized action advantages. This two-timescale design converts accumulated experience into multi-granular credit signals, requiring only one rollout per anchor. Across agentic and mathematical reasoning benchmarks, LSTAE matches or improves upon strong group-based baselines while substantially reducing rollout cost.

---


### 190. [Attention-Enhanced Deep Features with Heterogeneous Ensemble Learning for Glaucoma Detection](https://arxiv.org/abs/2609.06699)

**<font color=#1a73e8>作者：</font>** Abdullah Al Shafi, Nishat Sadaf Lira, Abrar Hasan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Glaucoma is a progressive optic neuropathy characterized by irreversible damage to the optic nerve, making timely diagnosis critical to prevent permanent vision loss. Although deep learning has demonstrated promising performance in automated glaucoma detection, existing approaches often overlook feature refinement, suffer from class imbalance, and rely on individual classifiers that limit prediction robustness. To address these challenges, this paper proposes a hybrid glaucoma detection framework that integrates attention-enhanced deep feature extraction with heterogeneous ensemble learning. Specifically, deep representations are extracted using InceptionV3 and subsequently refined by incorporating the Convolutional Block Attention Module (CBAM) to enhance discriminative retinal features. To improve classification robustness, the extracted features are classified using multiple machine learning models together with Single-Level Ensemble (SLE) and Double-Level Ensemble (DLE) strategies, while SMOTE combined with Tomek Links (SMOTE+TL) is employed to alleviate class imbalance. Furthermore, a systematic comparison of handcrafted, deep, and attention-enhanced deep feature representations is conducted. Experimental evaluation on two public retinal fundus datasets demonstrates that deep feature-based methods consistently outperform handcrafted feature-based methods, while the proposed attention-enhanced framework achieves the best overall performance. Furthermore, Grad-CAM visualizations confirm that the proposed model focuses on clinically relevant retinal regions, providing interpretable evidence on the model's prediction process.

---


### 191. [DianShi-RxnDB: A Large-Scale, Fine-Grained Organic Reaction Data Platform Built via a Fully Automated Pipeline for Researchers and AI Agents](https://arxiv.org/abs/2609.06703)

**<font color=#1a73e8>作者：</font>** Yubin Wang, Xingjian Wei, Jiang Wu 等 36 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-quality structured organic reaction data are essential for developing artificial intelligence for chemistry (AI4Chem), yet much of this knowledge remains dispersed across patent text, images, and reaction schemes. We present DianShi-RxnDB, a large-scale, fine-grained organic reaction data platform built via a fully automated extraction and normalization pipeline integrating patent text, images, and reaction schemes. Its corpus covers organic synthesis patents from the USPTO and EPO published between 1976 and 2025, yielding approximately 24 million reaction instances, of which approximately 14.8 million (61.7%) pass automated qualification checks. Each instance represents a specific single-step experiment recording participants, roles, quantities, temperatures, reaction times, yields, experimental procedures, and provenance links to source patents. In a manual evaluation of 1,300 sampled qualified instances, the micro-averaged field-level accuracy was 92.95%. A matched comparison with Pistachio further indicated advantages in deduplicated record counts, representation granularity, and field-level exact agreement. The platform provides a Web research workbench for searching, filtering, comparing, and source-verifying records, and a Model Context Protocol (MCP) service offering AI agents composable structured retrieval tools. DianShi-RxnDB is available at this https URL .

---


### 192. [RoLA: Rotary-Positioned Low-Rank Linear Attention for Efficient Diffusion Transformers](https://arxiv.org/abs/2609.06712)

**<font color=#1a73e8>作者：</font>** Zekun Zhang, Yixiang Cai, Yuxi Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) achieve strong video generation quality, but their dense spatiotemporal self-attention scales quadratically with sequence length and quickly becomes the dominant inference bottleneck. Sparse low-rank hybrids alleviate this cost by combining a local sparse branch with a global compressed branch. In video DiTs equipped with 3D Rotary Position Embeddings (RoPE), the global branch faces a structural compatibility issue: when RoPE is applied before a nonlinear feature map, the rotation and nonlinearity generally do not commute, making it difficult to keep a query-independent linear summary while preserving relative rotary geometry. Existing work often sidesteps this issue by replacing genuine cross-token global aggregation with coordinate-conditioned surrogates or learnable absolute positional modules. These compromises can be effective, but they approximate relative decay from absolute coordinates and introduce extra positional parameters. We propose \textbf{RoLA}, a rotary-positioned low-rank linear-attention branch that keeps genuine cross-token aggregation while remaining compatible with a reusable linear summary. The design applies RoPE \emph{outside} the nonlinear low-rank feature map and reuses a truncated subset of the pre-trained rotary schedule matched to the low-rank bottleneck.
This yields a linear-time low-rank global branch with relative positional behavior by design and no additional positional parameters; the full sparse--low-rank module still includes the fixed-sparsity sparse branch. Experiments on open-source video DiTs show that the resulting method remains competitive in generation quality at 90\% sparsity while achieving 2.63$\times$ end-to-end inference speedup on Wan2.1-14B (720p, 81 frames, measured on an NVIDIA H100 GPU).

---


### 193. [We Built a Mirror and Mistook It for a Mind: Causal Liability and the Fallacy of AI Consciousness](https://arxiv.org/abs/2609.06715)

**<font color=#1a73e8>作者：</font>** Afshin Khadangi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The contemporary debate over machine consciousness begins from a concealed assumption: that the object called "AI" already constitutes the kind of entity to which consciousness could belong. This paper challenges that assumption by separating phenomenal consciousness, introspective report, and human projective introspection, then arguing that generative systems can return linguistic traces of human interiority in first-person form without thereby identifying a phenomenal bearer. We call the resulting inference the AI Consciousness Fallacy. We then introduce Causal Liability Theory (CLT). CLT-I proposes liability closure as a criterion for individuating a candidate bearer: a physically continuing process becomes the non-delegable inheritor of constraints generated by its own endogenous discriminations. CLT-II advances the stronger conjecture that liability closure is necessary and sufficient for minimal phenomenal subjecthood. An open-weight causal audit operationalizes CLT-I across multiple model families. Forced discriminations produced persistent downstream divergence; activation patching showed strong causal mediation; live and copied adaptive states were behaviorally identical under matched randomness; and detached reconstruction preserved computational state across process replacement while, by protocol, breaking constitutive continuity and non-delegable inheritance. These results show that CLT-I distinctions are experimentally tractable and can dissociate causal bearer structure from first-person performance. The framework therefore separates consciousness attribution, causal bearer individuation, and the independent metaphysical question of consciousness constitution.

---


### 194. [ADELE - Adaptive Delaunay Grids for High-Fidelity Mesh-Native Reconstruction](https://arxiv.org/abs/2609.06723)

**<font color=#1a73e8>作者：</font>** Johannes Weidenfeller, Shaofei Wang, Philipp Fürnstahl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Meshes remain the most practical representation for geometry reasoning and integration into graphics pipelines, yet existing reconstruction methods struggle to produce high-quality meshes. Most state-of-the-art approaches initially learn an intermediate representation (NeRF/3DGS) and treat mesh extraction as a post-processing step, which often leads to oversmoothed surfaces or poor quality meshes with excessive triangle this http URL mesh-native optimization methods alleviate some of these issues but suffer from fixed-resolution discretizations and unstable optimization behavior. In this paper, we introduce an adaptive mesh-based optimization framework and a practical mesh rendering technique to address these challenges. Our representation combines an optimizable Delaunay-triangulated tetrahedral grid with a multi-resolution hash grid. The former is refined through point pruning and insertion, while the latter provides latent features for SDF/appearance value predictions. We use volumetric rendering to bootstrap a coarse geometry while leveraging mesh-based rendering for recovering fine-grained details. Additionally, we propose a differentiable, rasterization-based depth-offset rendering formulation, reducing geometric artifacts and improving reconstruction quality. Our method significantly outperforms existing mesh optimization approaches across a variety of object-centric benchmarks while being competitive with state-of-the-art NeRF/3DGS methods.

---


### 195. [Back to the Feature: Zero-Shot 6DoF Pose Estimation via Dense Local Features](https://arxiv.org/abs/2609.06726)

**<font color=#1a73e8>作者：</font>** Ali Rafiaei, Michael Greenspan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present B2TFPose, a training-free zero-shot method for 6DoF pose estimation of unseen objects from RGB images. Using a single frozen DINOv3 vision transformer as its only pretrained component within the pose estimation pipeline, B2TFPose extracts dense patch-level features that generalize across the synthetic-to-real domain gap without any task-specific fine-tuning, revisiting the classical local feature matching paradigm through the lens of large-scale self-supervised foundation models. Three contributions advance the training-free state of the art. A geodesic non-maximum suppression strategy retrieves a viewpoint-diverse template set for coarse-to-fine correspondence matching. Render-guided Re-Correspondence (RRC) synthesizes object-specific views at the estimated pose and re-establishes dense 2D-3D correspondences to sharpen the initial estimate without additional learned parameters. A multi-mask hypothesis selection strategy jointly scores competing segmentation candidates to resolve segmentation ambiguity. On the seven core datasets of the BOP Benchmark, B2TFPose achieves 40.7 mean AR without refinement and 56.4 with refinement, establishing state-of-the-art performance among training-free RGB methods and outperforming trained counterparts including GigaPose and GenFlow, at competitive inference speed.

---


### 196. [Uni-Light: An Ultra-Lightweight Framework via Uncertainty-Aware Knowledge Distillation for Brain Tumour Segmentation](https://arxiv.org/abs/2609.06729)

**<font color=#1a73e8>作者：</font>** Libing Kuang, Soren Salehi, Ziling Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D brain tumour segmentation from multi-modal Magnetic Resonance Imaging (MRI) is essential for clinical diagnosis and treatment planning. Existing brain tumour segmentation methods often suffer from heavy computational demands, while current lightweight architectures frequently lack the capacity to maintain segmentation fidelity in complex tumour regions. To address these issues, we propose a novel ultra-lightweight framework (Uni-Light) that achieves high-fidelity segmentation with substantially reduced computational overhead. It combines multi-scale convolutions with an uncertainty-aware knowledge distillation scheme that directs the student model toward hard-to-classify regions, complemented by a Signed Distance Field boundary loss for geometric constraints. Experimental results on BraTS2023-GLI and MSD-BTS datasets demonstrate that Uni-Light reduces parameters by 97.56%, floating-point operations (FLOPs) by 73.03%, and inference memory footprint by 81.58%, while surpassing the state-of-the-art model by an average of 1.47% in Dice score, offering a highly competitive trade-off between segmentation accuracy and computational efficiency in resource-constrained clinical settings. This work also advances data engineering for medical imaging by demonstrating that teacher model uncertainty can be exploited as a data-driven supervisory signal, re-prioritising the training data distribution without requiring additional annotation.

---


### 197. [Event Interaction in Low-Rank Bottlenecks for Temporal Relation Extraction](https://arxiv.org/abs/2609.06731)

**<font color=#1a73e8>作者：</font>** Wei Sun, Tingyu Qu, Jesse Davis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Temporal relation extraction determines whether an event occurs before, after, or simultaneously with another event, and therefore relies on accurately modeling how the two events interact. Mainstream systems achieve this by concatenating event spans or using shallow fusion, which works well when all model parameters are trainable. However, in parameter-efficient fine-tuning, low-rank bottlenecks restrict information flow and prevent these interaction signals from passing through, leading to clear performance drops. To address this limitation, we propose a theoretically grounded architecture, Convolutional Bottleneck Interaction (CBI), which first applies lightweight depthwise convolution to enhance event representations and then uses element-wise multiplication to capture effective event-event interactions inside the bottleneck. Across five datasets and seven backbone models in the Adapter and LoRA settings, CBI provides consistent and substantial gains, up to +31.7 micro F1, while adding minimal computational cost, showing that explicit interaction inside low-rank spaces is crucial for temporal relation extraction. The code is available at this https URL.

---


### 198. [LASSNet: Level-Aware Availability-Conditioned Spatial-Semantic Fusion for Brain Tumor Segmentation with Missing MRI Modalities](https://arxiv.org/abs/2609.06733)

**<font color=#1a73e8>作者：</font>** Haobin Chen, Ao Chang, Rundong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain tumor segmentation from multimodal MRI relies on complementary evidence across four imaging sequences, yet one or more modalities may be unavailable because of acquisition cost, protocol variation, scan failure, or patient condition. Existing work has explored reconstruction, knowledge transfer, and direct feature fusion, but leaves open whether missing-modality fusion should change with representation level. High-resolution lateral features retain spatial detail, whereas compressed bottleneck features encode semantic and inter-modality context. We therefore hypothesize that fusion should be conditioned jointly on modality availability and feature hierarchy. We propose the Level-Aware Availability-Conditioned Spatial-Semantic Fusion Network (LASSNet), which contains two level-specialized modules. Hierarchical Availability-Conditioned Fusion (HACF) constructs four lateral representations using count-normalized aggregation of available modalities, mask-conditioned channel modulation, and local 3D refinement. Tri-Scale Relational-Spatial Fusion (TriRSF) models relations among available modality descriptors and spatial context across multiple bottleneck resolutions, followed by cross-scale aggregation and availability-conditioned global spatial attention. A shared coarse-to-fine decoder starts from TriRSF semantics and progressively injects HACF features, without reconstructing missing inputs. Across all 15 non-empty modality configurations, LASSNet obtains mean Dice scores of 76.7% and 83.2% over WT, TC, and ET on BraTS2019 and BraTS2023, respectively.

---


### 199. [Simulating the Marginal Green Contribution of AI Modules in a Smart-Agriculture Platform: Evidence from Two Monte Carlo Experiments](https://arxiv.org/abs/2609.06740)

**<font color=#1a73e8>作者：</font>** Zhaoyang Li, Ruijie Zhang, Zhaoji Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Smart agriculture platforms usually bundle AI diagnosis, IoT sensing and decision push into a single package, so the green benefit attributable to each component remains unclear and resource-allocation decisions lack quantitative evidence. Building on a previous platform-level Monte Carlo assessment, this paper makes the components explicit and runs two controlled simulation experiments. Experiment 1 follows the chain from AI capability to farmer behavior to agrochemical input reduction, modeling pesticide/fertilizer reduction as avoidable blind-application share times prescription effectiveness times decision-touch coverage times adoption rate, and compares an experienced-extension mode with the AI mode: the probability of reaching 20% pesticide reduction is essentially zero in the extension mode but 20.7% at baseline, up to 49% with diagnosis accuracy 0.95 and adoption 0.85 under AI; the probability of 15% fertilizer reduction rises from near zero to 52.0%. Experiment 2 compares current practice (P0), IoT engineering retrofit (P1), and P1 plus AI irrigation scheduling (P2): median aggregate water saving rises from 7.8% (P0) to 11.0% (P1) and 16.0% (P2), with AI adding 5.0 percentage points beyond engineering; paddy CH4 reduction reaches 30.5% under AI scheduling versus 19.8% under manual operation, and the rice irrigation-methane subsystem carbon intensity declines 27.9%. Sensitivity analyses of both experiments consistently indicate that the primary bottleneck for meeting green targets is farmer adoption rather than algorithm accuracy, and that AI data fusion is robust to soil-moisture sensing errors. This work provides a reproducible simulation framework for component-level green-value evaluation and promotion-strategy optimization of smart agriculture platforms.

---


### 200. [LATS: Levy Adaptive Tree Sampling for Feedback-Driven Diverse Target Discovery](https://arxiv.org/abs/2609.06761)

**<font color=#1a73e8>作者：</font>** Binglin Ji, Anindya Sarkar, Hengchang Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While diffusion models excel at capturing complex data distributions, scientific discovery often requires steering generation toward specific, uncharacterized regions that maximize a target objective. These high-utility modes frequently reside in low-likelihood tail regions and are only revealed sequentially through interactive feedback. Existing diffusion samplers fail in this regime: they inherit the pre-trained model's bias toward high-density regions, leaving rare yet promising phenomena underexplored. Conversely, exploration-heavy samplers ensure broad coverage but fail to efficiently exploit high-utility modes when constrained by a strict sampling budget. To resolve this dilemma, we introduce Levy Adaptive Tree Search (LATS), a principled sampling framework for online feedback-driven search. LATS leverages heavy-tailed exploration coupled with tree-based value backpropagation to progressively uncover preferred modes. By maintaining broad distributional coverage, LATS successfully discovers low-likelihood, high-utility regions while preserving sample fidelity and structural diversity. Experiments across diverse benchmarks, including materials science, demonstrate that LATS significantly outperforms baselines in target discovery efficiency.

---


> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-542](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
