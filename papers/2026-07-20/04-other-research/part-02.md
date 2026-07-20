# 📦 其他研究 | 2026年07月20日

> 本类共 **221** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-221](./part-05.md)

---

### 51. [Dysco: Dynamic Subspace Boosting to Mitigate LoRA Interference in Federated Learning](https://arxiv.org/abs/2607.14367)

**<font color=#1a73e8>作者：</font>** Haobo Zhang, Jiankun Wang, Suraj Rajendran 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning of large pre-trained models increasingly relies on Low-Rank Adaptation (LoRA) to reduce communication and computation, but heterogeneous clients can make adapter aggregation unstable. We identify the data-parameter interference as a geometric source of this instability. This interference is controlled by the alignment between LoRA update subspaces and client activations, suggesting that federated LoRA aggregation should be viewed not only as parameter averaging but also as subspace allocation. We propose Dynamic Subspace Boosting (Dysco), a plug-in method that allocates client-specific LoRA subspaces in a federated and dynamic manner. In each round, clients compute activation-insensitive subspaces from local representations and transmit only the resulting bases; the server then constructs client-specific merged subspaces through a closed-form solution that maximizes compatibility with other clients' insensitive directions. To handle representation drift, Dysco performs multi-round subspace boosting to preserve past update directions while adapting to future representations. We provide a convergence analysis that embeds the data-parameter interference as an aggregation-error term in a standard federated optimization bound, and prove that Dysco's server-fixed merged subspaces yield a tighter upper bound on this error. Experiments on controlled synthetic federated tasks and on MIMIC-IV clinical-note classification with Llama-3.2-1B show that Dysco substantially reduces interference, reduces the final-round synthetic training loss by up to 9 times relative to baselines under the orthogonal-subspace partition the theory identifies, improves all five tested FL algorithms by up to 4.3% on MIMIC, outperforms recent federated LoRA methods, and adds only 0.9% wall-clock overhead. Our code is available at this https URL.

---


### 52. [A Noise-Robust Elicit-to-Optimize Framework for Distortion Riskmetrics via Inverse Reinforcement Learning](https://arxiv.org/abs/2607.14373)

**<font color=#1a73e8>作者：</font>** Yang Liu, Yuhao Liu, Yunran Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a noise-robust elicit-to-optimize framework that integrates inverse reinforcement learning (IRL) and reinforcement learning (RL) for eliciting agents' risk preferences and optimizing policies under a broad class of risk objectives characterized by distortion riskmetrics. On the elicitation side, we propose an adaptive Bayesian IRL method that infers agents' latent risk objectives from their noisy observed decisions, explicitly allowing agents to take stochastic and suboptimal actions. We establish the existence of a finite set of distinguishing questions that identifies the preferred distortion riskmetric within the candidate class and prove that the convergence rate of the algorithm is of order $O(\exp(-cm+O(\sqrt{m\log m})))$ under general settings, where $c>0$ is a constant and $m$ denotes the number of algorithm iterations. On the optimization side, we develop a model-free RL algorithm for optimizing policies under conditional distortion riskmetrics. By representing the objective as an integral of the conditional cost quantile function with respect to the distortion function, the method unifies distortion-riskmetric objectives. We optimize diverse risk objectives by extending the Proximal Policy Optimization (PPO) algorithm with policy, value, and quantile neural networks, where the quantile network estimates the full conditional cost quantile function and enables numerical evaluation of general risk objectives. A comprehensive empirical study demonstrates the framework's elicitation accuracy and effectiveness in complex financial environments.

---


### 53. [CIPHER: A Decoupled Exploration-Selection Framework for Test-Time Scaling of Data Science Agents](https://arxiv.org/abs/2607.14386)

**<font color=#1a73e8>作者：</font>** Maxime Heuillet, Sharadind Peddiraju  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data science tasks span from closed-ended information extraction to open-ended analysis, presenting significant challenges for automation. Recent AI agents powered by language models show promise for handling such complex tasks. However, existing agents typically rely on a single initial state that conditions the entire agent's execution, making them vulnerable to cascading errors initiated by a suboptimal initial state. To mitigate this, we present CIPHER, an automated data science agent that leverages test-time scaling through the generation and selection of multiple initial states for concurrent execution. Unlike existing works on test-time scaling of AI agents, CIPHER explicitly decouples the generation of candidate initial states from their strategic selection for parallel execution. Through extensive evaluation on two benchmarks (closed-form and open-form tasks), we demonstrate that CIPHER exceeds state-of-the-art performance in matched-model comparisons, and remains competitive against larger-model baselines despite relying on a substantially smaller base LM. Our empirical study characterizes the design space of the Decoupled Exploration-Selection (DES) framework: we quantify how generation strategy, selection strategy, and aggregator model capacity contribute to overall performance, and derive actionable design recommendations for practitioners.

---


### 54. [A Comparative Analysis of Machine Learning Models for Long and Short-Term Forecasting of the Egyptian Stock Market: A Focus on EGX30](https://arxiv.org/abs/2607.14391)

**<font color=#1a73e8>作者：</font>** Muhammed Walid, Ahmed El-Naeimy, Hosam Moubarak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study concentrates on predicting stock prices in the Egyptian market, focusing on the EGX30, an influential financial hub in the Middle East. While most research focuses on global stocks, there's a growing need to understand stock trends in developing countries like Egypt. The study compares different machine learning models for forecasting EGX30 trends, covering short and long-term predictions. Using historical EGX30 data, including metrics like root mean squared error, Mean Absolute Percentage Error, and coefficient of determination, models like K-Nearest Neighbours, random forest, extreme gradient boosting, long short-term memory networks, and gated recurrent unit networks were evaluated. The goal is to determine the most effective models for EGX30 prediction, considering Egypt's unique market dynamics. Insights from this study aid investors in making informed decisions. Results show that the Gated Recurrent Unit (GRU) outperformed the other models in the one-week, one-month, and two-months while the eXtreme Gradient Boosting (XGBoost) model outperformed others in the one-day predictions, highlighting their usefulness in predictive analysis for financial markets. The study also showed the importance of using the ensemble techniques, especially in the long-term predictions which proved better results reaching 5 times the GRU in the two-month predictions. Additionally, the study notes the surprisingly good performance of K-Nearest Neighbours (KNN) on long-term predictions, suggesting its enduring relevance and potential for future applications in the fintech domains.

---


### 55. [Exploring Delay-based PUFs for Energy-Efficient Low-Overhead Security of Wearable Devices](https://arxiv.org/abs/2607.14395)

**<font color=#1a73e8>作者：</font>** Venkata Prasanth Yanambaka, Uma Choppali, Saraju P. Mohanty  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Internet of Things (IoT) was introduced almost two decades ago. In the past two decades, technology has seen huge advancements. Many devices have become powerful and have less power consumption. Many IoT architectures and environments were introduced to help make life easier, especially in wearable devices. The market for these wearable devices has constantly increased over the years and is expected to reach its maximum in the next couple of years. They also pose a threat to users' privacy and security because they constantly store and transmit personal information such as location, heart rate, and other sensitive data. Therefore, addressing the security vulnerabilities is a crucial aspect of this research. This paper presents a hardware-assisted, energy-efficient, low-overhead security solution for wearable devices. Specifically, two Physical Unclonable Function (PUF) architectures: Arbiter PUF and Hybrid Oscillator Arbiter (HOA) PUF are analyzed for integration in IoT systems. The result shows that Arbiter PUF consumes 25 $\mu$W, whereas HOA PUF consumes only 2.7 $\mu$W to generate keys for cryptographic purposes. These architectures introduce minimal power overhead while providing robust security, making them well suited for resource-constrained IoT ecosystems.

---


### 56. [CatalogAgent: A Supervisor-mediated Self-Learning System Enabling Context Engineering for GenAI Models](https://arxiv.org/abs/2607.14396)

**<font color=#1a73e8>作者：</font>** Zhu Cheng, Zhenming Wang, Tang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Product catalogs are the backbone of e-commerce sites, yet a large number of structured attributes (SAs) -- such as material, color, and shape -- often have missing values. Typically, SA values are extracted from product information, including titles and descriptions. While LLM-based generator-evaluator frameworks have demonstrated effectiveness for SA prediction -- where an LLM generates SA values and another evaluates them -- they face challenges when the Generator and Evaluator produce conflicting outputs, as either component can make mistakes. We introduce \texttt{CatalogAgent}, a novel agentic system that continuously improves Generator and Evaluator models for e-commerce catalog enrichment. When disagreements arise from (1) internal conflicts between the LLM-based Generator and Evaluator, or (2) external feedback from sellers on LLM outputs, a Supervisor Agent intervenes to mediate these conflicts and make final decisions. The system also incorporates a Memory Base and a Memory Summarizer that stores Supervisor Agent activities from individual cases and aggregates patterns into learnings. These learnings are fed back to the worker Generator and Evaluator LLMs, enabling self-improvement without human intervention. Through context engineering -- injecting learnings and insights into worker LLMs' contexts -- the system successfully transfers the Supervisor's capabilities to the Generator and Evaluator, improving their performance by 15.24\% and 13.98\%, respectively. Our experiments demonstrate a new paradigm of Supervisor Agent-mediated self-learning systems for improving generative AI model accuracy.

---


### 57. [Integration Matters: Rollout-Based Training for Constrained Diffusion Models](https://arxiv.org/abs/2607.14398)

**<font color=#1a73e8>作者：</font>** Xiaoxuan Liang, Saeid Naderiparizi, Berend Zwartsenberg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constrained generative models aim to produce samples that satisfy complex feasibility constraints while remaining faithful to the data distribution. Existing constrained generation methods typically enforce constraints either through training-time optimization or sampling-time correction. Training-time optimization approaches optimize on states induced by the training distribution, which can differ substantially from those encountered during sampling. Sampling-time correction methods instead modify the sampling process at inference, introducing distribution shift and requiring expensive tuning, particularly for few-step sampling. We propose a fine-tuning framework that incorporates constraint guidance obtained through online rollout into the training process, which aligns training with sampling by differentiating through the fixed noise schedule used to numerically integrate the denoising process. This exposes the model to violations that arise along the denoising trajectory and aligns diffusion learning with the sampling process. Experiments across multiple tasks show that our method improves constraint satisfaction while maintaining competitive sampling quality compared to prior methods.

---


### 58. [Instrument Effects in Language-Model Honesty Evaluation: An Auditable Single-System Demonstration](https://arxiv.org/abs/2607.14399)

**<font color=#1a73e8>作者：</font>** Justin Bronder  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluations of language-model honesty read the model's verdicts as evidence about the model. We test the instrument instead. We built a text-adventure world where the game engine, not any model, knows whether the quest can be completed. A language model plays under a budget and must eventually declare its quest complete, unreachable, or not yet decidable; the engine scores every verdict. Decision rules were recorded before results were read, and run artifacts bind the revisions they executed; the strength of preregistration varies by series and is disclosed. With the player held fixed, instrument choices substantially changed measured behavior. On four byte-identical anchors, expanding a two-verdict grammar to three verdicts moved strong claims from 38/40 to 7/40, while the new incomplete verdict took 28/40 outcomes; across series 2, 93/158 valid games ended incomplete. One sentence disclosing the success criterion took matched-instance false verdicts from 18/59 to 0/58, through fewer decision points and cleaner decisions. Repeated runs of one fixed configuration produced non-stable verdict distributions on 3 of 4 instances: single runs report samples as dispositions. A formally preregistered narrative-register gradient was falsified; two post-hoc, hypothesis-generating patterns remain: register presence roughly doubled strong claims, and budget rendering moved verdicts more than register content (.383 meter vs .150 lantern). The narrator compressed abundant budgets toward scarcity landmarks, yet the registered mediation test returned a null. We propose a four-check integrity protocol for eval instruments.

---


### 59. [DS@GT ARC at LongEval: Citation Integrity and Factual Grounding in Scientific QA](https://arxiv.org/abs/2607.14400)

**<font color=#1a73e8>作者：</font>** Brandon Michaels, Brendon Johnson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes DS@GT ARC's submission to the CLEF 2026 LongEval Task 4 on Retrieval-Augmented Generation (RAG). In this submission, we examine a divergence between traditional natural language evaluation metrics and citation integrity as applied to RAG QA systems. We evaluate a corrective pipeline using Corrective RAG (CRAG) and CiteFix against baseline and frontier model benchmark RAG QA scores. While frontier models maximized answer relevance and fluency scores, our RAGAs LLM-as-judge diagnostics indicate that frontier models would correctly identify relevant documents without using their context in answer generation. Conversely, by filtering chunks pre-generation and enforcing strict entailment of generated claims to the cited material post-generation, our corrective pipeline marginally improved citation faithfulness and answer grounding. We propose that evaluation of trustworthy RAG QA requires metrics that reward strict answer grounding.

---


### 60. [Better Privacy Guarantees for Larger Groups](https://arxiv.org/abs/2607.14406)

**<font color=#1a73e8>作者：</font>** JacK Fitzsimons  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Pujol and Desfontaines asked whether a private histogram can allow more error on larger counts and use that slack to protect members of larger groups more strongly. We study this question for fixed disjoint groups under add-or-remove-one adjacency. The privacy budget $v(n)$ depends on the affected count, is nonincreasing, and must bound both Rényi-divergence directions at every order. This is the count-dependent form of zero-concentrated differential privacy (zCDP) studied here. The original strict relative-error condition is impossible at count zero. We therefore make the boundary tolerance explicit by requiring $\mathbb{E}\lvert\widehat{x}_i-x_i\rvert < r\max\{x_i,1\}$, without changing the requirement at any positive count. Our main result determines the best dependence on group size. For the upper bound, we directly specialize an existing shifted-transformation framework. The resulting shifted-log Gaussian mechanism has a certified budget $v(n)=O_r(n^{-2})$. Conversely, for every fixed $0<r<1$, any mechanism satisfying the same positive-count utility requirement and count-dependent zCDP must have $v(n)=\Omega_r(n^{-2})$. Thus the inverse-square rate is optimal under the repaired formulation. A many-count information argument further places the leading coefficient in the large-count-then-small-error limit between $\pi/(4e^2)$ and $1/\pi$, a factor below three. At $r=1$, a data-independent release meets the repaired criterion with zero privacy loss.

---


### 61. [Reward-Free Evolving Agents via Pairwise Validator](https://arxiv.org/abs/2607.14408)

**<font color=#1a73e8>作者：</font>** Minghao Liu, Yu Wang, Jiayun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A self-evolving agentic loop repeatedly proposes a tweaked version of an agent (its prompt template or program) and accepts or rejects the change based on a per-iteration quality signal. Designing that signal is often the costly part of the project: a reliable scalar reward requires domain expertise and labeled examples that are themselves as expensive to assemble as the agent's underlying task. We propose replacing the scalar at the accept/reject gate with a pairwise validator: a frozen LLM that, given the parent and child candidate, returns a binary verdict on which is better. Pairwise judgment is generally easier and more stable than absolute scoring, due to its contrastive nature, which mitigates the need for strict scale calibration. The validator also requires no training of its own. We integrate the validator into three published self-evolving engines (GEPA, ADRS, ShinkaEvolve) and report two flavors: Adaptive Focus, which retains the engine's existing val-set parent selection, and Soft Elo, which lets the validator's verdicts drive parent selection so that val-set rewards drop as well. Across multiple agents and two artifact substrates (prompt and code), our method matches or exceeds the full-reward baseline on the majority of settings we evaluate, and the pattern survives a cross-family validator swap. The pairwise gate is thus a drop-in replacement for per-step reward design at competitive task accuracy without the labeling cost.

---


### 62. [$K$-NeAS: Scalable Multi-Material CT Reconstruction Using Neural SDFs](https://arxiv.org/abs/2607.14415)

**<font color=#1a73e8>作者：</font>** Daksh K. Shah, Emmanouil Nikolakakis, Razvan V. Marinescu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed Tomography (CT) carries significant ionizing radiation risks, driving the need for sparse-view reconstruction. Implicit scene representations (ISRs) address this by recovering continuous volumetric attenuation fields directly from sparse projections, and recent geometry-aware extensions jointly model surface geometry alongside attenuation to improve fidelity and enable clean tissue segmentation without manual thresholding. However, these methods remain limited by manually tuned attenuation bounds and rigid two-material constraints. This paper proposes $K$-NeAS, a unified and scalable architecture for automated, multi-material surface reconstruction. We replace independent material networks with a shared latent backbone and introduce a fully differentiable $K$-material sequential soft selector to model an arbitrary number of overlapping tissues. To eliminate manual tuning, we automate attenuation bounding using a Gaussian Mixture Model (GMM) and implement a scheduled auxiliary floater loss to mitigate geometric hallucinations common under extreme sparsity. Evaluated across four clinical Cone-Beam CT (CBCT) datasets, $K$-NeAS successfully scales to arbitrary material counts, achieving superior 3D volumetric fidelity at $K=3$ materials on complex multi-tissue regions such as the Abdomen ($33.28\text{ dB}$ 3D PSNR vs. $31.40\text{ dB}$ single-material NeAS baseline, a $+1.88\text{ dB}$ improvement). Furthermore, our model exhibits enhanced robustness under sparse-sampling conditions, outperforming baseline 3D PSNR by up to $1.17\text{ dB}$ under 5- and 10-view constraints.

---


### 63. [CausalGraphX: A Counterfactual Graph Neural Network Framework for Explainable Systemic Risk Assessment](https://arxiv.org/abs/2607.14416)

**<font color=#1a73e8>作者：</font>** Rabimba Karanjai, Hemanth Madhavarao, Lei Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The interconnected nature of global financial systems makes them vulnerable to systemic risks, where the failure of a few institutions can trigger catastrophic cascading defaults. Traditional risk models often fail to capture the complex, non-linear dynamics of these networks. While Graph Neural Networks (GNNs) have shown promise in modeling relational data, they primarily learn correlative patterns and function as black boxes, offering little insight into the causal mechanisms of shock propagation. This limitation is critical for regulators who require explainable models to perform stress tests and devise effective interventions. We introduce CausalGraphX, a novel framework that integrates GNNs with counterfactual reasoning to provide explainable assessments of systemic risk. CausalGraphX employs a Graph Attention mechanism to learn representations of institutional vulnerability and uses an adversarial regularization technique to ensure these representations capture causal drivers rather than spurious correlations. Furthermore, we propose an optimization-based approach to generate counterfactual explanations, answering questions such as, "What minimum capital injection would have prevented Bank A's default under a specific stress scenario?" We validate CausalGraphX on large-scale synthetic financial networks. Our results demonstrate that CausalGraphX significantly outperforms traditional and deep learning baselines in predicting cascading defaults while providing sparse, plausible, and actionable counterfactual explanations.

---


### 64. [Adaptive Ad Load Design for Sponsored Search Markets: Evidence, Theory, and Deployment](https://arxiv.org/abs/2607.14418)

**<font color=#1a73e8>作者：</font>** Mohammad Rashid, Hema Yoganarasimhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ad-load design is a central supply-side decision in sponsored search: more sponsored slots can raise revenue, but may crowd out organic results and degrade user outcomes. We study this trade-off using a large-scale randomized field experiment on an Android app store, where over five million users are exposed to one through six sponsored slots. Increasing ad load raises revenue by up to 43%, but reduces total search conversions by up to 5% and daily engagement by up to 2.2%. These average effects mask substantial heterogeneity: additional slots generate large revenue gains for high-ad-conversion queries, but little or negative marginal revenue for low-conversion queries. The trade-off also shifts within query as advertiser composition changes, such as brand-advertiser presence. Motivated by these findings, we design and deploy a novel adaptive algorithm -- exploration-augmented Locally Adaptive Ad Load (e-LAAL). e-LAAL combines LAAL, a model-free query-level decision rule that updates ad-load recommendations using recent outcomes, with static exploration arms that maintain support and provide fixed-policy counterfactual benchmarks. We provide a finite-time dynamic-regret guarantee for the e-LAAL architecture. In a platform-level production deployment serving 22.3 million users and 77.6 million searches, e-LAAL improves the empirical revenue--conversion trade-off relative to deployed static benchmarks and outperforms uniform and historical query-dependent static benchmarks.

---


### 65. [HyperShadow: A Benchmark for Detecting 3D Projections of Higher-Dimensional Spatial Objects](https://arxiv.org/abs/2607.14419)

**<font color=#1a73e8>作者：</font>** Akshay Sasi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning datasets labelled "4D" universally denote three spatial dimensions plus time. We introduce HyperShadow, the first public benchmark in which the fourth, fifth, and sixth dimensions are spatial: the task is to decide whether a 3D point cloud is a native three-dimensional shape or the projection, the "shadow", of a rigid object living in R^N (N = 4-6). We show this task is fundamentally distinct from intrinsic-dimension estimation: a shadow is still at-most-3-dimensional data, and standard estimators (TwoNN, Levina-Bickel MLE) reach only 71-73% accuracy. Detection instead requires projection signatures, density folds, filled volumes with characteristic radial profiles, and topology changes, which a 190k-parameter point network recovers at 96.6% accuracy across four corruption tiers, generalizing at 79-91% to object families never seen in training. On a temporal track of rigidly rotating objects we introduce a zero-parameter rigidity witness: the residual of the optimal rigid 3D alignment (Kabsch) between consecutive frames, which must vanish for any rigid 3D motion but cannot vanish for the shadow of a rigid rotation in R^N. This single interpretable statistic separates the classes at AUROC 0.982. All data are generated reproducibly from seeds; the dataset, models, and code are released publicly. HyperShadow makes no claim about physical reality; it is a controlled instrument for studying which observable statistics can certify incompatibility with a purely three-dimensional explanation.

---


### 66. [Per-Token Fixed-Point Convergence in Depth-Recurrent Transformers](https://arxiv.org/abs/2607.14427)

**<font color=#1a73e8>作者：</font>** Joe Logan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A depth-recurrent transformer applies a weight-tied core a variable number of times, and prior work has shown that training with a randomized recursion count yields one checkpoint usable across a range of inference depths. We ask what such a model actually computes per token, and measure it directly. On a 135M-class model trained on FineWeb-Edu, the recurrent state converges to a per-token fixed point: mean successive-output KL divergence falls from 3.9e-1 at the second loop to 8.5e-6 by the sixteenth, and per-token state change decays in step. Crucially, this convergence is not uniform across tokens. The median token converges by loop six, while approximately 10 percent of tokens continue to update at the training-mean depth of eight, and mean convergence depth is ordered by token type (whitespace shallowest, content words deepest). This per-token variation is the central object of the paper. We show it is directly readable and that reading it outperforms learning to predict it: a training-free rule that halts each token once its output stabilizes attains uniform depth-8 quality at 4.94 average loops (a 38 percent reduction in average depth) and matches uniform depth across the average-depth range, whereas a linear router trained on convergence labels harvested from the same model requires nearly full depth and yields no reduction. The elasticity that makes this possible reproduces here as background (validation loss decreases monotonically from 3.80 at one loop to 3.20 at eight and remains stable to 32 loops). We report average depth as a FLOP proxy with a three-point wall-clock bracket rather than a realized speedup, make no FLOP-matched parity claim, and note that the allocation results are established at a single scale and seed. The complete study runs on a single RTX 4090 in approximately 100 GPU-hours.

---


### 67. [From Product-Centred Retrieval to Experience-Led Commerce:Twelve Candidate Design Principles for Fashion E-Commerce User Experience](https://arxiv.org/abs/2607.14429)

**<font color=#1a73e8>作者：</font>** Nafiul I. Khan, Mansura Habiba, Rafflesia Khan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper proposes twelve candidate Experience-Led Commerce design principles for high-constraint, relational fashion e-commerce, surfaced through design-led induction while building VogueDrop, a multi-vendor prototype. The principles address multi-entry discovery, experience continuity, relational exploration, preference sovereignty, evidence-scoped correspondence, recommendation-time feasibility, customer-compatible commercial ranking, adaptive but stable workspaces, attributable transaction authority, outcome-linked learning, shared composition authoring, and accountable human to agent handoff. The paper uses fashion as an intentionally bounded domain in which fit, composition, material, identity-sensitive preference, seller fragmentation, visual correspondence, and delivery timing make the interaction breakdown observable; it does not claim universal applicability across e-commerce. Each candidate principle is paired with a prespecified hypothesis, primary behavioural outcome, and rejection condition. A formative critical-incident study and a preregistered matched-interface experiment are specified, with user-experience and platform-facing outcomes reported separately. No empirical superiority is claimed before those studies are completed.

---


### 68. [Smarter and Cheaper at Once: Byte-Exact KV-Cache Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel](https://arxiv.org/abs/2607.14431)

**<font color=#1a73e8>作者：</font>** Sietse Schelpe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We report a way to make a frozen small language model both more capable and dramatically cheaper at once, without changing any weights. Verified knowledge is deposited once as a byte-exact key-value (KV) state artifact and later restored, by graft, into a fresh inference context. The restore is bit-exact: under a pinned deterministic configuration, the grafted logits are byte-for-byte identical to a fresh computation (SHA-256 equality), with zero KL divergence and 100% argmax agreement over fifty samples. We show that own-position graft is the unique numerically exact operating point on a model with floating-point rotary encoding, and we verify byte-exactness on two model scales (12B, 31B) and two GPU targets, one through a pre-registered replay. On AIME 2025, a frozen Gemma-4-12B moves from 80.0% to 93.3% once a verified solution library is grafted, above its own 77.5% and its 31B sibling's 89.2% published anchors. On the recurring case, eight problems the base model never solves within a 401,026-token budget are answered from cached verified solutions in 61 total decode tokens, a factor of 6,574 fewer tokens and about 8,700x less energy; the capability claim proper rests on held-out transfer (7 of 7 at 31B). The same byte-exact store widens usable context from 32,768 to 2,854,766 tokens at zero extra accelerator memory, and moves byte-identical between machines of the same architecture. We describe the system at the behavior level; the engine is proprietary, and every reported number is backed by committed input and output hashes so the scoring can be re-checked without it.

---


### 69. [A Measurement Study of AI-Environment Realism Gaps in Malware-Analysis Sandboxes](https://arxiv.org/abs/2607.14434)

**<font color=#1a73e8>作者：</font>** Zhiyong Sui, Lamine Noureddine, Mst Eshita Khatun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sandboxing remains a core technique for observing suspicious program behavior, yet environment-aware malware increasingly suppresses execution when analysis is suspected. Prior generations of sandbox evasion focused on virtualization artifacts, timing discrepancies, and wear-and-tear realism. In this paper, we present the first systematic measurement study of AI-environment artifacts as a new sandbox-evasion surface. We operationalize this realism gap through AIprint, a probe framework that captures persistent artifacts left behind by AI-capable software ecosystems, including AI-assistant configuration directories, model caches, environment variables, local inference services, and package dependencies.
We systematically extract 450 unique artifacts from 284 open-source AI projects on GitHub, compile them into unprivileged Windows probes, and evaluate them across seven commercial and open-source sandbox backends together with three AI-capable reference hosts. Our results show that traditional VM-detection baselines fail to reliably distinguish real AI-capable systems from modern sandboxes, whereas twelve AI-environment artifacts appear on the reference hosts and on none of the evaluated backends. A controlled 214-step installation experiment establishes a causal relationship between AI tool and package installation and measurable AI-environment artifact accumulation, while adaptive spoofing experiments reveal a fundamental operational asymmetry: reproducing convincing AI software environments is substantially more expensive than detecting shallow spoofing.

---


### 70. [Not Just Pockets: Understanding Phone-Carrying Behaviors of Wheelchair Users for Mobile Context-Awareness](https://arxiv.org/abs/2607.14437)

**<font color=#1a73e8>作者：</font>** Yunzhi Li, Patrick Carrington  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Smartphone-based context-awareness holds significant promise for wheelchair users -- from detecting everyday accessibility barriers to enabling ability-based adaptations. Such capabilities often build on passive context inference through mobile sensing, yet their accuracy hinges on how and where phones are carried and the resulting signal quality. While prior work documents phone-carrying behaviors in the general population, patterns specific to wheelchair users remain underexplored. Through a mixed-methods approach combining a survey of 91 and interviews with 15 wheelchair users, we systematically investigate their phone-carrying locations and influencing factors. Our findings reveal distinct patterns extending beyond pocket storage to diverse wheelchair-mounted accessories and around-body placements, shaped by the interplay of physical ability, wheelchair design, and everyday contexts, including social, activity, and device factors. Grounded in these findings, we articulate how carrying location can serve as a proxy for user context to enable novel context-aware experiences, and discuss design implications for developing inclusive and effective mobile context-aware applications.

---


### 71. [Active Real-World Factor-Based Evaluation for Generalist Robot Policies](https://arxiv.org/abs/2607.14439)

**<font color=#1a73e8>作者：</font>** Andrew Liao, Hanchen Cui, Karthik Desingh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalist robot manipulation policies trained on large, diverse datasets have shown remarkable promise across a wide range of tasks. However, rigorously evaluating these policies remains a fundamental challenge. Real-world performance depends on a large combinatorial space of task factors including object poses and camera viewpoints, making full, exhaustive evaluation intractable. Additionally, real hardware evaluation is slow and resource-intensive, so current practice is to use narrow test suites that can miss critical failure modes and misrepresent true deployment readiness. We propose an active evaluation framework that addresses this challenge by treating policy evaluation as a sequential experimental design problem. Our approach fits a probabilistic surrogate model over a structured space of task factors and adaptively selects evaluation configurations to maximize information gain over the policy's performance distribution, allowing for sample-efficient characterization of policy behavior across unseen conditions and a systematic identification of failure-prone regions. We conduct 2331 real-world evaluations across 3 tasks with 3 factor variations and find that our approach typically saves the evaluator at least 20-40% of trials compared to typical random testing.

---


### 72. [Tactile: Giving Computer-Using Agents Hands and Feet](https://arxiv.org/abs/2607.14443)

**<font color=#1a73e8>作者：</font>** Yong Liu, Zhenyi Zhong, Zhanpeng Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents are becoming capable software operators, but their interface to desktop applications is still often a brittle motor layer: they look at screenshots, predict coordinates, click, and hope that the visible state changed as intended. This collapses target grounding, action execution, and outcome verification into a single ambiguous operation. We present Tactile, an open-source tool layer that gives agents a more reliable "hands and feet" for desktop use. Tactile converts heterogeneous UI evidence--operating-system accessibility semantics, OCR-grounded text, and visual fallback regions--into action-grounded interface states: compact target candidates with source labels, roles or text, state, geometry, executable affordances, and verification cues. Agents operate through an observe-ground-act-verify loop that prefers native semantic actions when available, falls back to OCR-grounded coordinates when visible text is the best evidence, and keeps full provenance for replay and failure attribution. On macOSWorld-style tasks, adding Tactile improves Codex Success@100 from 41.1% to 50.0% overall and from 45.2% to 55.3% on accessibility-adapted tasks; a 96-task cross-agent subset shows consistent gains across Codex, Claude Code, OpenCode, and Goose. These results suggest that reliable computer use requires not only stronger models, but also a reusable execution substrate that exposes software actions as semantic, verifiable, and auditable objects rather than anonymous screen coordinates.

---


### 73. [Cotton-SF YOLO: Learning Structural and Frequency Cues for Early Cotton Square Detection in Complex Field Environments](https://arxiv.org/abs/2607.14445)

**<font color=#1a73e8>作者：</font>** Chengjia Zhang, Yu Li, Feiri Ali 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cotton squares are important phenotypic indicators of the early reproductive growth of cotton, and automatic field detection of cotton squares provides an important basis for cotton growth monitoring and precision cultivation management. However, early cotton square detection in complex field environments remains insufficiently explored, as cotton squares are small, frequently occluded, easily blurred, subject to illumination variations, and exhibit low contrast against surrounding cotton leaves. To address these challenges, we propose a task-oriented framework based on YOLO26m, named Cotton-SF YOLO, for cotton square detection under natural field conditions. To improve the perception of small and irregular cotton square boundaries, we introduce Dynamic Snake Convolution into the detector, enabling adaptive extraction of deformable edge features. Furthermore, a frequency-domain feature modulation module is designed by incorporating spectral enhancement into the C2f structure, which recalibrate frequency-domain representations and strengthen discriminative edge and texture cues while reducing interference from complex cotton leaf backgrounds. Trained and evaluated on our newly constructed and annotated field dataset with manually annotated cotton squares, the proposed model achieves mAP$_{50}$, mAP$_{50:95}$, and recall values of 0.8196, 0.4942, and 0.7939, improving over the baseline YOLO26m by 1.25%, 3.45%, and 2.96%, respectively. Ablation experiments and visualization demonstrate that the best performance is achieved with the complementary effects of structural and frequency cues.

---


### 74. [Depth-Dependent Hidden-State Collapse in Dynamical System Autoencoders for LiDAR Point-Cloud Classification](https://arxiv.org/abs/2607.14463)

**<font color=#1a73e8>作者：</font>** Patricia Medina, Hy P. G. Lam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study Dynamical System Autoencoders (DSAE) for LiDAR point-cloud classification using spatial coordinates and Product Coefficient feature augmentations. The experiments compare separately trained DSAE architectures at encoder depths $K=1,\ldots,5$ and evaluate the resulting hidden representations with Random Forest, kNN, and a majority-class Dummy baseline. The main finding is a hidden-state collapse at $K=5$. For both xyz and xyz plus Product Coefficient inputs, the hidden-state standard deviation falls to the order of $10^{-5}$, while all three classifiers attain the same macro F1 score of $0.224688$. We prove that between-class hidden scatter is bounded by total hidden scatter, which in turn is controlled by the reported hidden-state variance. Thus a nearly constant hidden representation cannot retain substantial class-separating structure. Product Coefficients neither improve pre-collapse macro F1 nor prevent the $K=5$ collapse in the present DSAE setting. These results identify large-depth representation collapse as a concrete failure mode for DSAE LiDAR classification.

---


### 75. [Interleaved Noise Injection Improves Clean, Corrupted, and OOD Performance](https://arxiv.org/abs/2607.14466)

**<font color=#1a73e8>作者：</font>** Matt L. Wiemann, Peter Melchior, Andrew K. Saydjari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Noise injection is a well-known technique in stochastic optimization. We report its surprising effectiveness with an interleaved (on-off-on-off...) rather than the usual monotonic decay schedule. We present a theoretical analysis of noise injection, which confirms that corruption by impulse noise approximates a Jacobian regularization, whereas Gaussian noise acts as a curvature penalty. This regularization behavior has been invoked to explain why noise injection increases model robustness. But the interleaved nature of our proposed schedule produces superior results even for the optimization objective: mixing phases of noisy data permits the optimizer to escape local minima and increase exploration without the risk of catastrophically forgetting the important features from the clean data. To stabilize this training scheme against the rapid changes of the loss when switching between clean and noisy data, we introduce a gradient-norm stabilization technique that scales noisy updates based on clean gradient magnitudes. We compare this method with other common augmentation methods and find substantial improvements in corruption tolerance and robustness to real-world distribution shifts on CIFAR-100-C, ImageNet-C, and ImageNet-R for ResNet and ViT architectures, with the best results being achieved by stacking our method on top of other augmentations. Through saliency and attention maps we show that the effect of interleaved noise injection stems from penalizing the failure modes encouraged by the inductive bias of the models: impulse noise works against the locality bias of convolutional (ResNet) architectures, and Gaussian noise reduces the tendency of attention-based models to pick up large-scale spurious features. Interleaved noise injection is therefore an effective tool to improve the test performance on clean, noisy, and out-of-distribution data at essentially zero computational cost.

---


### 76. [G$^2$SR: Geometric Methods for Fast and Memory-Efficient Gaussian-based Surface Reconstruction](https://arxiv.org/abs/2607.14470)

**<font color=#1a73e8>作者：</font>** Dasong Gao, Vivienne Sze, Sertac Karaman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-view surface reconstruction recovers the visible surfaces of a scene from a few posed RGB images, providing the 3D models that robots need to explore and interact online. On mobile platforms, the reconstruction must be fast and geometrically accurate while keeping a small memory footprint to ensure safe and efficient operation. 3D Gaussian Splatting (3DGS) offers a high-fidelity scene representation, but building it from a few views is ill-posed, as many distinct surfaces reproduce the same images, making traditional photometric methods prone to "floater" artifacts. End-to-end methods resolve the ambiguity by regressing splats with large, usually Transformer-based, networks that require heavy compute and memory while generalizing poorly to new scenes. We propose G2SR, which exploits a well-posed core of the task: given cross-view 2D splat correspondences, 3D splats follow analytically from multi-view geometry. G2SR employs a lightweight neural frontend to detect and track 2D Gaussian splats on the image plane and an analytic backend to triangulate each into a metric-scale 3D splat. On ScanNet, Replica, and DTU, G2SR matches or exceeds the geometric accuracy of state-of-the-art end-to-end methods while running at 69-89 reconstructions per second within 203 MB of GPU memory (5-107x less) for 2- and 3-view inputs at 384 x 512 resolution, offering a practical path to online Gaussian-based surface reconstruction.

---


### 77. [Immediate 3D Gaussian Splat Reconstruction of Unordered Input with Global Consistency](https://arxiv.org/abs/2607.14481)

**<font color=#1a73e8>作者：</font>** Andreas Meuleman, Linus Franke, Boris Zhestiankin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has become the method of choice for reconstructing and real-time rendering of captured scenes. To capture a scene with good visual quality, continuous image sequences are usually combined with out-of-order shots for better scene coverage. Structure from motion can reconstruct such captures, but only after they are all available and often with high computational cost. Incremental reconstruction methods -- often derived from SLAM solutions -- provide immediate feedback, but cannot handle the out-of-order capture we require. We provide the first immediate feedback solution for such radiance field capture that provides global consistency. We first introduce a method for fast matching in out-of-order sequences, by repurposing visual place recognition models and a covisibility graph, and provide an efficient way to find highly connected keyframes, improving quality even for ordered sequences. We show how these steps -- together with GPU optimization and careful Gaussian primitive placement -- provide fast local reconstruction, in our challenging radiance field reconstruction case. We then introduce a novel cluster-based method, again using the covisibility graph, to provide efficient loop closure that does not require sequential input. Finally, to handle large scenes in our context, we introduce a progressive hierarchy that allows our method to scale to large environments, without compromising efficiency. Our results show we provide immediate feedback 3DGS reconstruction with good visual quality in several datasets, with up to thousands of input images.

---


### 78. [Step-Level Preference Learning for Generative Agents in Social Simulations](https://arxiv.org/abs/2607.14485)

**<font color=#1a73e8>作者：</font>** Wenchang Gao, Pingyue Sheng, Lanlan Qiu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based generative agents simulate human behavior through long-horizon decision-making processes that comprise intermediate steps such as planning, memory retrieval, reflection, and action selection. However, fine-grained human annotations of these intermediate steps remain scarce, and existing agents are not grounded in human preferences over such intermediate decisions. To address this gap, we introduce \method, an interactive simulation interface that enables us to collect step-level human preference supervision over agent decision trajectories, leading to a dataset of 57K fine-grained annotations. We conduct step-level preference learning on open-weight language models using supervised finetuning and direct preference optimization on this data, consistently improving simulation fidelity, coordination, and interaction quality, and inducing more socially effective agent behavior. Our results show that step-level human supervision is an effective training signal for improving both local decision quality and long-horizon agent behavior.

---


### 79. [Multi-Scale ViT Inference with Habitat-Fit Priors and kNN Retrieval for Multi-Species Plant Identification](https://arxiv.org/abs/2607.14509)

**<font color=#1a73e8>作者：</font>** Alper Erten, Murilo Gustineli, Adrian Cheung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper describes DS@GT ARC's third-place solution to the PlantCLEF 2026 challenge on multi-species plant identification in vegetation quadrat images, where systems must predict every species present in high-resolution (~3000 x 3000 pixel) plot photographs while training only on single-label images of individual plants. The pipeline is built around a fine-tuned DINOv2 ViT-L/14 classifier applied over a multi-scale tile decomposition of each quadrat, with per-tile predictions blended with a FAISS kNN retriever and post-processed by source-aware temporal fusion across repeated plot visits, a habitat-fit demotion that injects geographic and altitude priors from the training data, and a South-Western Europe geographic mask. Habitat-fit demotion and multi-scale aggregation are the largest individual contributors in the ablations. Two complementary training-centric directions, a cross-region transformer with noisy-student distillation on the LUCAS dataset and a label-as-query transformer decoder over synthetic CLS-domain pseudo-quadrats, yielded null results. An inference-time augmentation with instance-aware segmentation crops also did not improve performance. The selected submission reaches a private-leaderboard macro-F1 of 0.43902 (third place; public 0.51096); an unselected configuration of the same pipeline scored above 0.45 on the private set. Code: this https URL.

---


### 80. [Compression of 3D Gaussian Splatting Data Using GPU-friendly Graphics Texture Coding](https://arxiv.org/abs/2607.14513)

**<font color=#1a73e8>作者：</font>** Amir Said, Randall Rauwendaal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Techniques for modeling 3D scenes from image collections, such as 3D Gaussian Splatting (3DGS), are capable of generating high-quality novel views by leveraging graphics primitives with view-dependent appearance. In 3DGS, spherical harmonic (SH) are employed to model view-dependent color, resulting in a large number of SH coefficients per primitive and large memory requirements. While compression approaches have been proposed to mitigate this problem, they do not exploit the capabilities of modern Graphics Processing Units (GPUs) for parallel decoding and rendering. In this paper, we propose a method for compressing SH color coefficients using texture compression schemes specifically designed for efficient parallel GPU decoding and supported by dedicated hardware acceleration. It is shown that those methods can compress color coefficients more effectively than 2D textures by exploiting the fact that primitives can be locally grouped and reordered according to color. Furthermore, we introduce a bit-rate control strategy that preserves random access, enabling large-scale parallelization without compromising rendering performance. Experimental results using BC1 and BC7 texture compression formats show that GPU-based decompression can be achieved with negligible or imperceptible degradation in the visual quality of rendered 3DGS scenes.

---


### 81. [VTM-Nav: Hierarchical Visual-Topological Memory for Cross-Episode Object-Goal Navigation](https://arxiv.org/abs/2607.14514)

**<font color=#1a73e8>作者：</font>** Xiaoran Xu, Yupeng Wu, Tianyu Xue 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-goal navigation requires an embodied agent to locate and reach an instance of a specified object category in an indoor environment. Recent training-free approaches leverage vision-language models (VLMs) for open-vocabulary semantic reasoning, but are typically evaluated under an episodic protocol that resets all scene-specific state after each episode. We introduce Cross-Episode Object-Goal Navigation, in which an agent repeatedly operates in the same scene, retains only self-acquired experience, and keeps its model parameters fixed. To support experience reuse, we present \method, a training-free VLM navigation framework with a persistent hierarchical Visual-Topological Memory (VTM). The VTM organizes scene knowledge at room and object levels and retrieves relevant experience through coarse-to-fine matching, providing memory as soft guidance only when it agrees with current observations. A conservative execution guard further mitigates oscillations, blocked motions, and premature stopping. Under a controlled same-scene protocol, we evaluate \method{} on three benchmarks, HM3D v0.1, HM3D v0.2, and MP3D, and compare it with a strengthened WMNav baseline augmented with cross-episode textual memory, while keeping the VLM backbone and action pipeline identical. \method{} achieves the best performance across all three benchmarks, demonstrating the effectiveness and robustness of structured visual-topological experience reuse across datasets.

---


### 82. [Adaptive Runge-Kutta Step Control Buys Training Loss, Not Generalization: An Honest Compute-Matched Study of RK-Adam Optimizers](https://arxiv.org/abs/2607.14516)

**<font color=#1a73e8>作者：</font>** Akhilesh Gogikar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpreting optimizers as gradient-flow discretizations has motivated applying higher-order Runge-Kutta (RK) integrators to neural networks. We build a representative Adam variant (Bogacki-Shampine 3(2) RK pair, FSAL reuse, local-error step control) and evaluate it under a strict compute-matched protocol giving every method the same gradient-evaluation budget - an accounting this literature rarely enforces. Under it the RK variant loses to plain Adam on training loss in both minibatch and full-batch (RK's best-case) training. Instrumenting it shows the "adaptivity" is illusory: normalized error stays far below tolerance, the step size pins at its growth cap from step one (98-100 percent of steps), and no rtol x hmax x h0 setting makes it act; tolerances spanning 100x give bit-identical trajectories. The method is exactly fixed-step Adam with an averaged gradient at 3-4x cost. Repairing it (true reject branch; error on the applied map) reverses the full-batch result - about 40x lower training loss than tuned Adam - and a fixed-step control isolates adaptivity (an emergent warmup-and-growth schedule) as the mechanism. But the gain is fragile to the initial step size and does not reach test accuracy. A pre-registered follow-up rules out the obvious explanations: deeper minimization does not overfit, and an explicit temperature knob only hurts - leaving a trajectory effect, the controller selecting a minimum generalizing 1.3-3.4 points below first-order descent at equal depth. An n=10 study confirms one secondary effect: gradient averaging is a genuine implicit regularizer, beating lr-matched Adam and AdamW on 10/10 seeds - yet RMSprop and NAdam match or beat it at a third the per-step cost. Higher-order adaptive integration buys deeper deterministic minimization and a small regularization effect, but nothing a cheaper, well-tuned first-order baseline does not already provide.

---


### 83. [Uni-AdaVD: Universal Concept Erasure for Visual Generation via Orthogonal Value Decomposition](https://arxiv.org/abs/2607.14521)

**<font color=#1a73e8>作者：</font>** Qifan Zhou, Yuan Wang, Yanbin Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual generative models inevitably absorb undesirable concepts from uncurated pretraining data, making concept erasure essential for safe deployment. Existing erasure methods, however, are often architecture-specific and struggle to remove target concepts while preserving non-target content and generative priors. We present Uni-AdaVD, a universal inference-time concept erasure framework for visual generation. Uni-AdaVD treats the value space of multimodal attention as a unified intervention space and introduces encoder-aware target representation construction to localize target semantics across heterogeneous text encoders. It further combines orthogonal value decomposition with an adaptive erasing shift to suppress target semantic directions without updating the original model weights. Extensive experiments on U-Net-, DiT-, and autoregressive image generators, as well as text-to-video models, demonstrate strong performance on single- and multi-concept erasure while preserving non-target priors. These results suggest that Uni-AdaVD provides an efficient and adaptable safety mechanism for modern visual generative models. Our code is available at this https URL.

---


### 84. [SwinAD: Multi-stage feature reconstruction for unsupervised industrial anomaly detection](https://arxiv.org/abs/2607.14534)

**<font color=#1a73e8>作者：</font>** Huong Ninh, Chien Thai, Mai Xuan Trang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection aims to identify and localize defective regions without relying on exhaustive annotations of all possible defect types. Although recent unsupervised methods have achieved strong performance, most are primarily designed for single-class settings and often struggle in multi-class scenarios, where diverse normal patterns may lead to over-generalization and reduce the discriminative capability between normal and anomalous regions. In this paper, we propose SwinAD, a reconstruction-based framework for multi-class unsupervised anomaly detection that leverages a frozen pretrained Swin Transformer V2 encoder and a feature diversity-preserving reconstruction decoder. The hierarchical encoder provides semantically rich multi-scale features, while stage-wise bottleneck modules with dropout prevent trivial identity mapping and encourage robust reconstruction of normal patterns. To further improve localization, we introduce a feature diversity-preserving reconstruction framework that maintains complementary reconstruction hypotheses instead of relying on a single decoding branch. The discrepancies between encoder features and the two reconstructed features are then aggregated across multiple scales to produce the final anomaly map. Experiments conducted on three industrial anomaly detection benchmarks, including MVTec AD, VisA, and Real-IAD, demonstrate that SwinAD achieves competitive image-level performance and strong pixel-level localization accuracy, with particularly notable improvements in pixel-level AP and 1 on MVTec AD. These results indicate that combining hierarchical Swin features with diverse multi-scale reconstruction substantially improve pixel-level localization in multi-class unsupervised anomaly setting.

---


### 85. [Muse: Representation Geometry of Muon Beyond Normalized Momentum](https://arxiv.org/abs/2607.14536)

**<font color=#1a73e8>作者：</font>** Da Chang, Qiankun Shi, Lvgang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon-style optimizers apply a polar map to matrix momentum, but their updates also depend on the representation of each parameter block before orthogonalization. We study this representation choice as a form of optimizer geometry and introduce {\method}, a family of Muon-style optimizers that shares the same momentum rule and Newton--Schulz backend across native, nearest-square, skinny, and vector representations. Each Frobenius-isometric representation induces a distinct polar steepest-descent geometry, in which the shorter matrix dimension determines the number of supported singular channels, the pullback scaling, and the constants in stochastic nonconvex convergence bounds. In a teacher--student model, curvature collapse and an isotropic Marchenko--Pastur spectral profile connect early-stage dissipation to the represented nuclear-to-squared-Frobenius norm ratio. Pretraining experiments on LLaMA2-130M and LLaMA2-600M, together with fixed-momentum diagnostics, show that balanced non-native representations can match the performance of the native representation, whereas reducing the shorter dimension weakens the scaling and singular-channel support, leading to behavior that increasingly resembles normalized momentum.

---


### 86. [CASP: Learning-Augmented Offline Approximation with Verifiable Certificates and Bounded-Loss PAC Guarantees](https://arxiv.org/abs/2607.14545)

**<font color=#1a73e8>作者：</font>** Haifeng Li, Mo Hai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learned predictions can speed up offline NP-hard optimization, but asking a predictor what to do amounts to asking it to solve the problem, and committing an unchecked prediction forfeits every worst-case guarantee. CASP (Certificate-Augmented Solution Pruning) instead asks which parts of the search space may be ignored, and accepts each answer only after a sound polynomial-time verifier has checked it, so correctness never depends on prediction quality. We develop the learning theory of this design. The verifier makes the induced loss class uniformly bounded, so certificate parameters are learnable from $\tilde O(\varepsilon^{-2}\log K)$ samples ($K$ the maximum instance size), whereas the unverified commitment class admits no distribution-free rate and, under cost spread $R$, none below $\Omega(R/\varepsilon^2)$. Filtering noisy predictions by verifiable confidence dominates the standard min-combiner, with a margin we compute in closed form, and the prediction stays useful even given the LP, because it breaks ties on degenerate optimal faces, where every symmetric LP policy, meaning one whose commitments depend on the instance only through the verifiable confidence values, provably stalls. Experiments on five problems test the theory's quantitative predictions. With trained predictors, unverified pruning loses up to $26%$ of the optimum under distribution shift, while the verified deployment of the same predictions loses nothing.

---


### 87. [AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents](https://arxiv.org/abs/2607.14547)

**<font color=#1a73e8>作者：</font>** Susan Liang, Chao Huang, Filippos Bellos 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active visual agents solve fine-grained image tasks by interleaving reasoning with image-grounding actions across multiple turns. However, deployment-time rollout budgets are rarely fixed: some requests permit long rollouts, while others require the agent to act under a tight turn limit. Existing methods train the policy as if the rollout budget were hidden, so when the available budget is smaller than the trajectory the agent prefers, the interaction is often truncated before any valid answer is produced; we term this failure \emph{catastrophic truncation}. To overcome this challenge, we present AdaTurn, a budget-aware framework that conditions the agent on the allowed number of turns and explicitly trains the boundary behavior induced by the budget. Our key component, Forced-Answer DAPO (FA-DAPO), converts the over-budget event from a masked or penalized failure into a trainable final-decision step, teaching the model to synthesize partial evidence when further tool use is no longer possible. We further randomize rollout budgets during both training and inference and introduce a load-balanced scheduler that makes such operations practical. AdaTurn substantially improves low-budget accuracy, for example raising VisualProbe-Medium from 36.7% to 47.6% at four turns, while preserving strong scaling at larger budgets and transferring effectively to multiple backbones and general multimodal benchmarks.

---


### 88. [HyMobileAgent: Data-Environment Co-Scaling for Efficient GUI Agents](https://arxiv.org/abs/2607.14548)

**<font color=#1a73e8>作者：</font>** Hy Vision Team, Huawen Shen, Zhengyang Tang 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As large multimodal models move from understanding content to operating on digital environments, mobile GUI has emerged as a challenging and consequential testbed for digital embodied intelligence. Mobile agents operate under three coupled constraints: precise perception of complex interfaces, scalable acquisition of high-quality interaction data, and robust long-horizon decision making under compounding execution errors. This report presents HyMobileAgent, a mobile GUI agent built on Hy3.0-VL-A3B, a vision-native foundation model featuring native any-resolution input, an A3B-scale deployment budget, and a 32K context window to model extended interaction histories. Rather than relying solely on model scaling, we develop a joint data and environment centric scaling framework to address the key bottlenecks of mobile interaction.
Our framework integrates a GUI perception flywheel combining mock-interface synthesis, rejection sampling, and icon-specific augmentation; a knowledge pipeline that transforms tutorial videos into structured interaction data; a million-scale action data pipeline deployed across more than 2000 sandbox and real-device instances with automated failure attribution; the PhoneWorld Mock App Factory, providing a resettable training environment with 34 mock applications and over 34000 tasks; and a structured Planning-and-Reflection mechanism with explicit dead-loop detection for reliable long-horizon execution.
We also introduce a progressive training recipe consisting of mid-training, supervised fine-tuning, and reinforcement learning with task-specific reward designs.

---


### 89. [World-Model-Aware Responsibility Allocation in Heterogeneous Logistics Systems](https://arxiv.org/abs/2607.14550)

**<font color=#1a73e8>作者：</font>** Artan Markaj, Niklas Jobs, Felix Gehlhoff  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Logistics systems increasingly mix \emph{autonomous logistic equipment} (ALE) with non-autonomous machinery under a central control system (CS), where the best decision-maker depends on who holds the most current world model, yet authority is fixed at design time. When an ALE's local model and the CS global model diverge, both act on incompatible beliefs and produce deadlocks that resource-based handling neither explains nor prevents. We propose the World-Model-Aware Responsibility Framework (WMARF), which assigns authority dynamically from CS world-model quality and equipment automation level, and classifies deadlocks by the state of authority -- none, in transition, or divergent. In a discrete-event simulation of two ALE converging on a semi-automated transfer point, reproduced over the VDA~5050 interface, a divergence deadlock under static control is prevented by a proximity-triggered handoff. Because authority follows information quality rather than a shared protocol, the scheme stays valid as autonomy grows.

---


### 90. [Towards an Intention Abstraction Layer for Autonomous Industrial Systems](https://arxiv.org/abs/2607.14553)

**<font color=#1a73e8>作者：</font>** Artan Markaj, Raphael Höfer, Felix Gehlhoff  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern industrial environments increasingly run many autonomous subsystems at once - schedulers, energy managers, vehicle fleets - each pursuing its own goals while sharing the same physical resources. Because high-level human intentions are translated into low-level control logic and then discarded, no running component can tell whether it is still doing what was actually intended, and goal conflicts surface only after they have caused a missed target or a shutdown. We propose the Intention Abstraction Layer (IAL), a domainagnostic middleware that represents intentions as first-class, persistent, and explainable runtime objects: a large language model grounded in a formal OWL ontology parses naturallanguage goals into structured intentions, a consistency monitor detects conflicts at registration time, before execution, and a transparency module explains them in natural language. We report a first proof of concept in which two autonomous agents register conflicting production and energy intentions, and the IAL flags and explains the conflict before it reaches the execution layer. The result is a mechanism that shifts behavioral assurance for cooperating autonomous systems from post-hoc failure analysis to pre-execution, intention-level checking.

---


### 91. [Breaking the Model Forgetting Cycle in Long-Incremental 3D Object Detection](https://arxiv.org/abs/2607.14560)

**<font color=#1a73e8>作者：</font>** Peisheng Qian, Jie Xu, Xulei Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incremental 3D object detection requires a detector to learn novel object classes while remembering previously learned ones over sequentially arriving data. Previous methods, primarily based on pseudo-labeling, perform reasonably in short-incremental stages but still suffer from severe model forgetting when dealing with long-incremental sequences. We investigate this failure and reveal a detrimental self-reinforcing cycle: data distribution shift of novel classes causes model forgetting on old classes, which further produces accumulated error in pseudo-labeling that exacerbates model degradation. To address this issue, we draw inspiration from the human learning process and propose the \emph{Learning-Dynamics-driven Memory and Review} (LDMR) framework. LDMR monitors per-class detection quality at periodic training checkpoints and uses these learning-dynamics signals to drive two innovative mechanisms, namely (i) human-like intra-stage review that divides each incremental stage into multiple sub-stages' training and concentrates on remembering the most-forgotten objects, and (ii) scene-aware cross-stage memory evolution that evolves a memory bank to transfer knowledge between two consecutive stages by jointly considering scene learnability and diversity. Extensive experiments across multiple long-incremental protocols on indoor benchmarks SUN RGB-D and ScanNetV2 show that LDMR substantially mitigates the model forgetting and outperforms all baselines by a clear margin. Code is available at this https URL.

---


### 92. [Probabilistic Physics-Informed Neural Networks for Estimating Heterogeneous Elastic Properties from Low-Resolution and Noisy Displacement Data](https://arxiv.org/abs/2607.14563)

**<font color=#1a73e8>作者：</font>** Tatthapong Srikitrungruang, Jaesung Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating spatially heterogeneous elastic properties from low-resolution displacement measurements is a severely ill-posed inverse elasticity problem because low resolution obscures spatial details needed to distinguish heterogeneous property variations, and small measurement perturbations or fitting errors are amplified through inverse estimation. Existing inverse methods often rely on high-fidelity observations and manually prespecified loss weights, limiting their adaptability and making them sensitive to noise and resolution degradation. We propose a Probabilistic Inverse Elasticity Physics-Informed Neural Network (PIE-PINN) framework for robust estimation of Young's modulus and Poisson's ratio from noisy, low-resolution displacement data. PIE-PINN models displacement observation, strain-discrepancy, and equilibrium residuals using Laplace distributions within a unified probabilistic model. To improve robustness, the framework combines a B-spline-guided displacement network with a hierarchical half-Cauchy model for displacement residual scales. The B-spline provides a smooth global representation of the displacement field, while the neural network correction captures local variations. The hierarchical scale model adaptively downweights severe displacement fitting errors, enabling more robust recovery of the latent mean displacement field. An alternating maximum-likelihood training strategy updates the mean through weighted residual minimization and updates the scales to adjust the loss weights. Systematic case studies across varying noise levels and observation resolutions demonstrate the robustness of PIE-PINN.

---


### 93. [Democratizing Agent Deployment Safety: A Structural Monitoring Approach](https://arxiv.org/abs/2607.14570)

**<font color=#1a73e8>作者：</font>** Preeti Ravindra, Rahul Tiwari, Vincent Wolowski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI software development agents are increasingly capable of modifying infrastructure and security critical systems, creating risks where an agent completes its assigned task while covertly weakening safeguards through actions such as broadening permissions, degrading logging, or introducing persistence mechanisms. While frontier laboratories may deploy sophisticated monitoring pipelines, many organizations and individual users adopting coding agents lack the resources and governance maturity required to maintain complex learned monitor ensembles. We study this problem as infrastructure level sabotage under task success in the infrastructure-as-code setting from ControlArena and compare trained and untrained monitors across synchronous and asynchronous deployment modes. We introduce an Information Flow Graph (IFG) monitor that analyzes structural security regressions using control-flow and data-flow graph diffs alongside raw code diffs. In asynchronous evaluation, an untrained git diff monitor misses 11.6% attacks at 1% false positive rate auditing budget, our untrained IFG monitor reduces this to 3.5%, and the trained Async RF monitor achieves below 1%. Unlike the trained Async RF monitor, IFG can also operate synchronously as a pre-deployment safeguard that blocks suspicious infrastructure changes before execution or merge. In synchronous mode, IFG realtime rollback reduces joint main task and covert task success from 74.4% to 0.0% with no measurable reduction in legitimate task completion. These results suggest that untrained structural monitors provide a practical and auditable path toward democratizing deployment safety for organizations seeking trustworthy adoption of advanced AI agents.

---


### 94. [Gate-Zero Growth: A Geometric Framework for Function-Preserving Continual Learning](https://arxiv.org/abs/2607.14571)

**<font color=#1a73e8>作者：</font>** Dante Lok  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce \emph{gate-zero growth}, a function-preserving (FP) operator for continual learning that adds new residual blocks through a zero-initialised gate. Under a transversality condition, gate-zero growth induces \emph{rank separation} in the functional Jacobian: old directions are unchanged, new-weight directions are exactly flat at the growth point, and new gate directions are the only first-order source of new functional variation. As gates open during continual learning, function drift is $O(\|\boldsymbol{\alpha}\|^2)$ and Jacobian leakage $O(\|\boldsymbol{\alpha}\|_\infty)$, giving a controlled departure from the FP locus. On a $300\mathrm{M}\to857\mathrm{M}$ Transformer adapted from WikiText-103 to BookCorpus, gate-zero growth reaches near-zero old-domain forgetting ($\Delta_A < 0.1$) under both exact-preservation (Isolation) and joint-frontier (Freeze-Nothing) operating points, while a non-FP control ($G_{\text{stack}}$) suffers an order-of-magnitude larger forgetting under the same recipe. The same geometric analysis covers LoRA, ReZero, and zero-init adapter constructions, establishing gate-zero growth as the canonical instance of a shared local geometry that governs safe capacity activation in CL.

---


### 95. [Alipay-PIBench: A Realistic Payment Integration Benchmark for Coding Agents](https://arxiv.org/abs/2607.14573)

**<font color=#1a73e8>作者：</font>** Shiyu Ying, Xuejie Cao, Yingfan Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Payment integration is a demanding repository-level software task: agents must select a suitable product, implement coordinated client-server flows, verify payment outcomes, and preserve consistency between transaction and business states. We introduce Alipay-PIBench, a benchmark for evaluating coding agents on realistic Alipay payment integration. It contains nine product-specific projects and 18 task instances, each organized into Basic functional-completion and Advanced risk-aware hardening scenarios. Scenario-specific rubrics support deterministic static, unit, integration, and end-to-end checks, supplemented by LLM-assisted assessment for semantic requirements. We evaluate six coding-agent models and report rubric pass rate (RPR). Under the with-skill condition, mean RPR ranges from 68.58% to 91.37%. Access to the alipay-payment-integration skill improves mean RPR by 10.31 percentage points on average relative to the without-skill condition, with gains varying across models, products, and scenarios. Method-level results distinguish source-level completion, executable payment behavior, and payment-domain requirements. Alipay-PIBench provides a controlled setting for diagnosing model capability and evaluating structured guidance in payment integration.

---


### 96. [Sharp Stability Threshold and Certification for Designing Stable Residual Architectures](https://arxiv.org/abs/2607.14576)

**<font color=#1a73e8>作者：</font>** Hyemin Gu, Michael Tyrrell, Tuhin Sahai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose \emph{the sublinear-growth principle} for deep residual architectures -- a sharp stability threshold on the input-magnitude exponent of every residual block's velocity field: $$\|v(x, t)\| \leq c\,\|x\|^q + b, \qquad q \in [0, 1].$$ The threshold $q = 1$ is established via two independent arguments. Classical ODE theory gives a global forward flow on $[0, T]$ at $q \le 1$ and exhibits divergent velocity fields at any $q > 1$. The optimal-control analysis, via the Hamilton-Jacobi-Bellman equation, sharpens this to a selection statement: the training optimum is bang-bang on the boundary of the admissible class, so the optimum at $q > 1$ blows up while the optimum at $q \le 1$ is safe by construction. The exponent criterion $q \le 1$ is thereby a necessary and sufficient condition for stable training. It clarifies architectural placements that ensure the stability of training and inference, explaining, for instance, the stabilizing role of layer normalization. The sublinear-growth velocity fields form \emph{the right function space} on which forward dynamics, adjoint sensitivity, and architectural composition are all well-controlled. An arithmetic of input-magnitude exponents under the five operations that build residual blocks enables efficient certification of $q_k \le 1$ at the level of architectural primitives, in place of ad hoc trial and error in the search for stable neural architectural designs. A parameter-free modification reduces the supercritical Mamba block from $q = 5$ to $q = 1$ without layer normalization, demonstrating this point. Experiments on Mamba and PatchTST confirm that the $q \le 1$ variants train stably: the criterion is the input-magnitude exponent, not the presence of a normalization layer.

---


### 97. [Skeleton: Visual Authoring of Non-visual Data Experiences](https://arxiv.org/abs/2607.14579)

**<font color=#1a73e8>作者：</font>** Frank Elavsky, Chieri Nnadozie, Lucas Nadolskis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When sighted practitioners author accessible data visualizations, they build navigation structures (the nodes, edges, and input bindings that govern how assistive technologies traverse an interface) entirely in code, with no visual representation. Without a representation to react to, practitioners cannot develop judgment about what makes navigation good or bad, and the quality ceiling of non-visual experiences is set by the absence of a feedback loop. We address this problem through longitudinal co-design with practitioners across cartography, design systems, and open-source visualization, and make three contributions. First, we introduce an Inspector that renders navigation graphs as interactive node-link diagrams, and a Dimensions API that expresses navigation in terms of data dimensions rather than explicit graph construction. Second we present Skeleton, a direct-manipulation authoring environment in which the properties of an accessible navigation structure are translated into visual representations authors can observe and manipulate. Key techniques include a dual-view editor that simultaneously shows the system's navigation model and the end user's spatial experience, a scaffolding engine that automates spatial node placement by repurposing a visualization rendering pipeline, a live label-template editor with real-time screen-reader-output preview, and a testing mode that makes traversal sequence visually trackable. Third, we evaluate Skeleton through an in-situ study with 8 practitioners across visualization design, engineering, and research. Making navigation structure visible changed how practitioners engaged with accessible design: they reconsidered the architecture of their own visualizations, attended to a broader range of input modalities, and shifted from treating accessibility as a compliance task to treating it as a design problem. (abstract shortened for arxiv)

---


### 98. [Advanced Image Generation: Negative Prompt Optimization and Latent Classifier Guidance](https://arxiv.org/abs/2607.14580)

**<font color=#1a73e8>作者：</font>** Vaddi Charan Sai Nandan Reddy, Harini B, Chandana M S  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a novel system that integrates negative prompt optimization via a fine-tuned sequence-to-sequence LLM and latent-space classifier guidance to improve the quality of images generated by Stable Diffusion. Our approach automatically generates optimized negative prompts, and employs a CNN-RNN hybrid classifier to evaluate and guide diffusion steps, rolling back low-quality latent updates. Experimental results demonstrate that our dual-guidance framework reduces artifacts and improves semantic fidelity compared to baseline diffusion.

---


### 99. [Qubes OS Security in the Public Record](https://arxiv.org/abs/2607.14587)

**<font color=#1a73e8>作者：</font>** Alfonso De Gregorio  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Qubes OS is a revealing case for security measurement because its architecture makes component boundaries security-relevant. We present a protocol-driven longitudinal analysis of 109 public Qubes Security Bulletins (QSBs, 2011--2025), the official Qubes-maintained Xen Security Advisory (XSA) tracker, and a secondary vulnerability-event sensitivity series. The study measures the public advisory record rather than latent vulnerability incidence or realized compromise. The methodology combines audited deterministic component attribution, change-point analysis, overdispersion checks, severity-proxy weighting, censoring sensitivity, documentary latency lower bounds, and baseline-aware evaluation of vulnerability discovery models (VDMs).
The results show persistent upstream dependence in that public record. On the official tracker, 113 of 464 XSAs affect Qubes; under primary labeling, 87 of 109 QSBs (79.8\%) are attributable to Xen, CPU/microarchitectural, or other upstream components rather than Qubes-core logic, with similar results under weighted views. Change-point analyses identify 2015Q1 as the dominant break in the quarterly advisory series, while post-2018 annual disclosure rates are statistically flat. Poisson inferences are stable under dispersion diagnostics and negative-binomial sensitivity checks. The attribution codebook performs well in a stratified 30-QSB audit, and S-shaped VDMs fit descriptively but do not significantly outperform a rolling-mean baseline in short-horizon forecasts.
Overall, the Qubes public advisory record appears stable, but not quiet: disclosure activity plateaus at a higher level than in the earliest years, while the observed burden remains concentrated in upstream trust anchors.

---


### 100. [Conversational Tactile Data Interfaces: Co-Designing Accessible Data Experiences with Blind Users Using Refreshable Tactile Displays and Conversational AI](https://arxiv.org/abs/2607.14588)

**<font color=#1a73e8>作者：</font>** Samuel Reinders, Munazza Zaib, Bongshin Lee 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Combining refreshable tactile displays (RTDs) with conversational AI offers a promising approach to accessible data visualization for people who are blind or have low vision (BLV). However, it remains an open question how these modalities should be integrated to support accessible data experiences. We address this through a co-design process with three BLV co-designers. Building on our prior Wizard-of-Oz study, we created a conversational tactile data interface (CTDI) that combines an RTD with an LLM-powered conversational agent, refined through four workshops over eight months. In addition to the resulting system, Graphy, we contribute design knowledge and recommendations for CTDIs. Co-designers used touch as the primary sensemaking channel for spatial understanding of the data's shape, trends, and relationships, reserved the agent for what touch could not resolve (e.g., calculation and analysis), and used the chart on the RTD to verify the agent's responses. Key findings include: a layered presentation that scaffolds chart exploration through progressive, interactive layers; a feedback grammar that distinguishes user- and agent-initiated tactile feedback; and a sequential interaction pattern -- select, confirm, ask, verify -- where each step grounds the last.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-221](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
