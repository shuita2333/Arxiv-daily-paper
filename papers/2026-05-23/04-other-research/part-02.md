# 📦 其他研究 | 2026年05月23日

> 本类共 **347** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-347](./part-07.md)

---

### 51. [Machine learning prediction of obstructive coronary artery disease using opportunistic coronary calcium and epicardial fat assessments from CT calcium scoring scans](https://arxiv.org/abs/2605.21762)

**<font color=#1a73e8>作者：</font>** Juhwan Lee, Ammar Hoori, Tao Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-contrast computed tomography calcium scoring (CTCS) is a cost-effective imaging modality widely used to detect coronary artery calcifications. This study aimed to develop an advanced machine learning framework that utilizes quantitative analyses of coronary calcium and epicardial fat from CTCS images to predict obstructive coronary artery disease (CAD). The study population consisted of 1,324 patients from the SCOT-HEART clinical trial who underwent both CTCS and coronary CT angiography. We extracted and analyzed a broad range of features, including 24 clinical variables, 189 calcium-omics, and 211 epicardial fat-omics features from the CTCS images. Feature selection was conducted using the CatBoost algorithm combined with SHapley Additive exPlanation (SHAP) values. Predictive modeling utilized the CatBoost gradient boosting method, focusing on the most informative features. From an initial set of 424 candidate features, 14 were identified as most predictive through the CatBoost-SHAP method. The top two predictive features originated from fat-omics, with the remaining 12 features derived from calcium-omics. The optimized model achieved robust predictive capabilities, demonstrating a sensitivity of 83.1+/-4.6%, specificity of 93.8+/-1.7%, accuracy of 85.3+/-2.0%, and an F1 score of 73.9+/-3.3%. Inclusion of calcium-omics and fat-omics data significantly improved predictive performance. Notably, the model also showed reliable predictive accuracy in patients with diverse coronary calcium scores, including cases with obstructive CAD despite a zero-calcium score. This innovative approach holds promise for improving clinical decision-making and potentially reducing dependence on contrast-enhanced or invasive diagnostic procedures, particularly within low-to intermediate-risk patient groups.

---


### 52. [On the Sample Complexity of Discounted Reinforcement Learning with Optimized Certainty Equivalents](https://arxiv.org/abs/2605.21763)

**<font color=#1a73e8>作者：</font>** Oliver Mortensen, Mohammad Sadegh Talebi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study risk-sensitive reinforcement learning in finite discounted MDPs, where a generative model of the MDP is assumed to be available. We consider a family or risk measures called the optimized certainty equivalent (OCE), which includes important risk measures such as entropic risk, CVaR, and mean-variance. Our focus is on the sample complexities of learning the optimal state-action value function (value learning) and an optimal policy (policy learning) under recursive OCE. We provide an exact characterization of utility functions $u$ for which the corresponding OCE defines an objective that is PAC-learnable. We analyze a simple model-based approach and derive PAC sample complexity bounds. We establish that whenever $u$ does not have full domain $\text{dom}(u)\neq \mathbb{R}$, the corresponding problem is not PAC-learnable. Finally, we establish corresponding lower bounds for both value and policy learning, demonstrating tightness in the size $SA$ of state-action space, and for a more restricted class of utilities, we derive lower bounds that makes the dependence on the effective horizon $\frac{1}{1-\gamma}$ explicit. Specifically, for $\text{CVaR}_\tau$ we show that the correct dependence on $\tau$ is $\frac{1}{\tau^2}$, thus improving by a factor of $\frac{1}{\tau}$ over state-of-the-art although our bound has a suboptimal dependence on $\frac{1}{1-\gamma}$.

---


### 53. [Position: The Time for Sampling Is Now! Charting a New Course for Bayesian Deep Learning](https://arxiv.org/abs/2605.21765)

**<font color=#1a73e8>作者：</font>** Emanuel Sommer, David Rügamer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The practical adoption of sampling-based inference (SAI) in Bayesian neural networks (BNNs) remains limited, partly due to persistent misconceptions about the feasibility and efficiency of sampling. This position paper argues that SAI has achieved computational parity with optimization-based methods and is at the verge of superseding such methods for effective and efficient inference in BNNs. This development should be in the interest of the whole community, promoting BNNs as a principled paradigm with its long-standing yet unfulfilled promise of providing principled uncertainty quantification for neural networks. SAI can even do more -- yielding superior prediction performance through model averaging, serving as the foundation for a plethora of possible downstream tasks, and providing crucial insights into the landscape of BNNs. In order to make such a change happen and unfold the potential of sampling, overcoming current misconceptions is a necessary first step. The next step is to realign research efforts toward addressing remaining challenges in SAI. In particular, the community must focus on two core problems: sufficient exploration of the posterior landscape and high-fidelity distillation of posterior samples for efficient downstream inference. By addressing conceptual and practical obstacles, we can unlock the full potential of SAI and establish it as a central tool in Bayesian deep learning.

---


### 54. [BodyReLux: Temporally Consistent Full-Body Video Relighting](https://arxiv.org/abs/2605.21766)

**<font color=#1a73e8>作者：</font>** Li Ma, Mingming He, Xueming Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Being able to relight human performance is a fundamental task for post production and content creation. We present BodyReLux, a subject-specific video diffusion-based framework for relighting full-body human performances in a temporally consistent way. Our model is trained on a hybrid dataset of pixel-aligned video relighting pairs, covering a diverse combination of lighting conditions, performances and viewpoints. To acquire such dataset, we combine traditional static One-Light-at-a-Time (OLAT) capture and a novel dynamic performance capture in which two smoothly varying lighting sequences are rapidly interleaved. Because the lighting operates above the human flicker-fusion threshold, the interleaving does not appear to strobe. We train our video relighting model from a pretrained text-to-video model to fully leverage the generative priors for producing high quality videos. To achieve accurate lighting control, we introduce a new lighting conditioning method that represents each light source as a token. We further condition on sequences of lighting using masked attention to support dynamic lighting control. Together with a carefully designed data augmentation pipeline, we achieve photorealistic, robust, and temporally consistent video relighting of subject-specific human performances.

---


### 55. [Manifold-Guided Attention Steering](https://arxiv.org/abs/2605.21770)

**<font color=#1a73e8>作者：</font>** Ian Li, Kapilesh Guruprasad, Raunak Sengupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models frequently produce errors in reasoning tasks despite possessing the underlying knowledge required for correct reasoning. One possible approach to improve reasoning consistency is through activation steering. However, existing activation steering approaches apply fixed, pre-computed correction vectors, ignoring where the model currently sits along its generation trajectory; the result is indiscriminate perturbation that disrupts already-correct steps as freely as erroneous ones. We propose Manifold-Guided Attention Steering (MAGS), a trajectory-aware inference-time intervention grounded in a geometric observation: the output activations of specific attention heads diverge from a low-dimensional correctness manifold at the point of error, and this deviation compounds through subsequent steps. For each identified attention head, we learn a low-dimensional subspace from contrastive pairs of correct and incorrect traces that capture the directions along which error behavior deviates from correct behavior. During inference, we monitor each head's proximity to this manifold and apply a targeted projection correction when deviation exceeds a learned threshold, steering the attention output back toward the correct subspace before the error propagates. MAGS consistently outperforms both unsteered baselines and static steering approaches across benchmarks spanning mathematical reasoning (MATH-500, GSM8K), code generation (HumanEval, MBPP), and molecular generation (SMILES), suggesting that correctness manifolds are a general feature of LLM attention geometry.

---


### 56. [Understanding Perspectives of Patients, Caregivers and Clinicians towards Emerging Collaborative-decision Making Technologies](https://arxiv.org/abs/2605.21777)

**<font color=#1a73e8>作者：</font>** Ray-Yuan Chung, Athena Ortega, Zixuan Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In pediatrics, patients, caregivers, and clinicians share responsibility for health decisions, but limited collaboration can undermine outcomes. We conducted a qualitative study examining decision-makers perceptions toward collaborative decision-making technologies, including interactive dashboards, VR simulators, and AI voice assistants. Findings reveal differences in user opinions across groups and indicate technology acceptance is linked to users trust of these technologies. Technology developers and researchers need to explore design and implementation strategies that build and facilitate trust or appropriate distrust between users and these novel technologies before these tools can effectively support collaborative decision-making.

---


### 57. [Provable Robustness against Backdoor Attacks via the Primal-Dual Perspective on Differential Privacy](https://arxiv.org/abs/2605.21780)

**<font color=#1a73e8>作者：</font>** Aman Saxena, Jan Schuchardt, Yan Scholten 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Randomized smoothing is a powerful tool for certifying robustness to adversarial perturbations, including poisoning attacks via randomized training and evasion attacks via randomized inference. Extending these guarantees to backdoor attacks, where training and test data are jointly perturbed, remains challenging because training- and test-time randomized mechanisms must be analyzed within a single robustness certificate. We address this by connecting randomized smoothing to the dual view of differential privacy through privacy profiles, which provide a numerical procedure for composing heterogeneous mechanisms. The resulting framework enables tight, modular, end-to-end certification of complex, composed mechanisms while leveraging existing analyses of differentially private mechanisms. We instantiate the framework for DP-SGD and Deep Partition Aggregation with inference-time smoothing, deriving joint robustness guarantees against both training-time and inference-time attacks. Experiments on MNIST and CIFAR-10 demonstrate the effectiveness of our framework. Overall, we provide a principled and general framework for using composite mechanisms to certify robustness under complex threat models that better capture the capabilities of real-world adversaries.

---


### 58. [MMD-Balls as Credal Sets: A PAC-Bayesian Framework for Epistemic Uncertainty in Test-Time Adaptation](https://arxiv.org/abs/2605.21783)

**<font color=#1a73e8>作者：</font>** Ahanaf Hasan Ariq  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) methods improve model performance under distribution shift but lack formal guarantees connecting shift magnitude to prediction reliability. We develop a PAC-Bayesian framework yielding generalization bounds explicitly parameterized by the maximum mean discrepancy (MMD) between source and target distributions. Our principal contribution is interpreting MMD-balls around the source distribution as credal sets in Walley's imprecise probability theory, yielding natural epistemic uncertainty quantification. We establish: (i) a PAC-Bayesian bound with an MMD-dependent shift penalty under an RKHS-Lipschitz loss assumption; (ii) a finite-sample version via MMD concentration; (iii) a uniform worst-case risk bound over all distributions in the credal set, with a lower-upper risk decomposition; and (iv) geodesic preservation bounds explaining why kernel-guided adaptation protects local feature geometry. The credal set interpretation separates epistemic from aleatoric uncertainty and provides a principled decision criterion for when adaptation is warranted.

---


### 59. [SceneGraphGrounder: Zero-Shot 3D Visual Grounding via Structured Scene Graph Matching](https://arxiv.org/abs/2605.21788)

**<font color=#1a73e8>作者：</font>** Xuefei Sun, Xujia Zhang, Brendan Crowe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot 3D visual grounding requires localizing objects in unstructured environments from free-form natural language. Recent vision-language model (VLM) approaches achieve promising results but rely on view-dependent reasoning or implicit representations, limiting spatial consistency and interpretability for compositional queries. We propose SceneGraphGrounder, a framework that reformulates 3D grounding as structured graph matching over a reconstructed 3D scene graph. To enable this formulation, we introduce a visual marker prompting strategy that enables a VLM to infer object-object relationships from 2D views, which are subsequently lifted into a persistent 3D scene graph encoding both spatial and semantic relations. Given a query, we construct a query graph and perform constrained alignment with the scene graph, ensuring multi-view consistency and interpretable reasoning. Experiments on the ScanRefer benchmark demonstrate that our method achieves competitive performance among zero-shot approaches, using only RGB-D inputs. We further validate our framework through real-world deployment on a mobile robot, demonstrating robust spatial reasoning in long-horizon physical environments. We will make our code publicly available upon acceptance.

---


### 60. [Residual Skill Optimization for Text-to-SQL Ensembles](https://arxiv.org/abs/2605.21792)

**<font color=#1a73e8>作者：</font>** Jiongli Zhu, Haoquan Guan, Parjanya Prajakta Prashant 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL ensembles improve over single-candidate generation by drawing multiple SQL candidates and selecting one, but their effectiveness is bounded by Pass@K, the probability that at least one of K candidates is correct. Existing methods source diversity heuristically through stochastic decoding or prompt variants, leaving candidate sets dominated by correlated failures. We present DivSkill-SQL, a residual skill optimization framework that builds complementary agentic Text-to-SQL ensembles without model fine-tuning: each new skill is optimized on examples the current skill ensemble fails on, provably targeting its marginal contribution to Pass@K. On Spider2-Lite, DivSkill-SQL improves selected accuracy by up to +11.1 points on Snowflake and +8.3 on BigQuery over the strongest ensemble baseline, with consistent gains across two base models (Opus-4.6 and GPT-5.4). Skills optimized on a single dialect transfer without retraining across dialects (Snowflake, BigQuery, SQLite) and to a different task formulation, such as BIRD-Critic (+2.6 pts). Error diagnostics show up to 3x fewer hallucinated schema references and function calls, indicating that gains come from genuinely reliable complementary skills rather than surface-form variation.

---


### 61. [Polars inside Intel SGX2 Enclaves: An Empirical Study of Confidential Analytical Query Processing](https://arxiv.org/abs/2605.21797)

**<font color=#1a73e8>作者：</font>** Wei Wang, Burns Smith, Kenny Leftin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environments (TEEs) have renewed interest in confidential analytics, but most prior evaluations focus on SQL database engines or earlier SGX generations. This paper studies an Arrow-native DataFrame engine, Polars, running inside Intel SGX2 enclaves via Gramine on TPC-H SF30 with Azure Blob Storage. We report both the standard TPC-H power score and a query-only variant that removes table-loading time in order to separate compute overhead from data-ingestion overhead. Across four dataset-width configurations (approximately 22-73 GB), end-to-end overhead remains nearly constant at 1.49-1.56$\times$, but this composite metric obscures two distinct behaviors: query-only overhead declines from 1.51-1.52$\times$ to 1.43-1.44$\times$, whereas table-loading overhead rises from 2.27$\times$ to 4.07$\times$. We further show that overhead is not uniform across queries: for the len130 configuration, the median per-query SGX slowdown is 1.45$\times$ with a maximum of 2.57$\times$, and a small set of queries exhibits pronounced run-to-run spikes consistent with stateful EPC pressure. Finally, we compare Polars' lazy and eager APIs under the same TEE setting. Lazy execution is 2.25-2.27$\times$ faster overall, while eager execution fails with out-of-memory errors at 41 GB and above. Relative to the recent DuckDB-SGX2 study, our results suggest that SGX2 can support Arrow-native analytical processing with a similar order of security overhead, but that load-path amplification and API-level optimization are first-order determinants of end-to-end performance.

---


### 62. [Three Costs of Amortizing Gaussian Process Inference with Neural Processes](https://arxiv.org/abs/2605.21798)

**<font color=#1a73e8>作者：</font>** Robin Young  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural processes amortize Gaussian process inference, replacing the exact $O(n^3)$ posterior with a learned $O(n)$ map from context sets to predictive distributions. For a class of latent neural processes, we bound the Kullback--Leibler (KL) divergence between the GP and LNP predictives, decomposing it into three interpretable sources, namely label contamination as the neural process uses label values to estimate a quantity that is label-independent in the exact GP, an information bottleneck because the finite-dimensional representation cannot resolve the full context geometry, and amortization error from a single encoder network shared across all contexts. The bottleneck truncation term decays in the representation dimension $d$ as $O(e^{-cd^{2/d_x}})$ for squared-exponential kernels on $\mathbb{R}^{d_x}$ where $c > 0$ is a kernel-dependent constant and as $O(d^{-2\nu/d_x})$ for Matérn-$\nu$ kernels, directly linking architecture sizing to kernel smoothness and input dimension. The label contamination term is $O(1)$ in general, with only the observation-noise component decaying as $O(1/n)$, identifying a persistent cost of routing uncertainty estimation through a label-dependent representation. These results characterize the costs of amortization within the analyzed class and yield architectural recommendations to predict variance from context locations alone in the GP-amortization regime, and replace mean aggregation with second-order pooling to close the dominant amortization gap.

---


### 63. [Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws](https://arxiv.org/abs/2605.21803)

**<font color=#1a73e8>作者：</font>** Nandan Kumar Jha, Brandon Reagen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws have made language-model performance predictable from model size, data, and compute, but they typically treat the optimizer as a fixed training detail. We show that this assumption misses a fundamental axis of representation scaling: how effectively the optimizer converts added FFN width into utilized spectral capacity. Using eigenspectra of feed-forward network representations, measured through soft and hard spectral-ranks, we find that \emph{the same Transformer architecture realizes markedly different spectral scaling laws when trained with different optimizers}. Holding architecture and width schedule fixed, AdamW exhibits weak hard-rank scaling ($\beta$=0.44) on rare-token (TAIL) representations where learning is known to be hardest, whereas Muon achieves linear scaling ($\beta$=1.02) in the same regimes, a $2.3\times$ increase in the scaling exponent. This difference is not reducible to validation loss: AdamW configurations can match low-rank Dion variants in perplexity, under extended training, while exhibiting sharply different spectral geometry, demonstrating that matched loss does not imply matched representation structure. Hard--soft rank asymmetry further reveals that optimizers differ not only in how much capacity is realized, but also in how that capacity is structured across eigenmodes. To disentangle optimizer effects from architectural ones, we compare against architectural interventions (e.g., attention rank and positional encoding), and find that optimizer-induced spectral shifts often exceed the architectural effects. These results suggest optimization as a first-class axis of representation scaling, motivating optimizer--architecture co-design.

---


### 64. [Trace2Skill: Verifier-Guided Skill Evolution for Long-Context EDA Agents](https://arxiv.org/abs/2605.21810)

**<font color=#1a73e8>作者：</font>** Zijian Du, Nathaniel Pinckney  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex Verilog Design Problems (CVDP) challenge hardware LLM agents because solving them requires localizing verifier-relevant RTL, testbenches, include paths, and build dependencies inside large repository snapshots, making precise edits, and recovering from sparse hidden-verifier failures. We present Trace2Skill, a test-time scaling framework that improves a hardware agent without RTL-specialized model fine-tuning. Rather than training a new model or only sampling more candidate solutions, Trace2Skill treats the agent's natural-language skill as an evolvable policy. It mines repeated rollout traces for success and failure modes, converts them into dense diagnostics and oracle lessons, and uses an oracle, mutator, and selector loop to produce task-specific skills that guide later search, editing, validation, and recovery. Because final pass/fail labels are often too coarse for hard failures, Trace2Skill also supports bounded runtime dense verifier feedback that returns sanitized functional observations while keeping hidden harnesses and reference solutions inaccessible to the agent. This feedback helps guide skill evolution and agent execution by connecting skill text, verifier evidence, and downstream behavior. Across hard CVDP tasks that defeat the seed CVDP agent, including tasks that also defeat frontier coding agents, Trace2Skill with dense verifier feedback substantially improves task pass rates and produces breakthrough passes on previously unsolved tasks, without requiring high-quality fine-tuning data, specialized RTL model training, or model weight updates. The same framework provides a general test-time scaling strategy that can extend beyond digital design to other verifiable EDA tasks.

---


### 65. [Symbolic Density Estimation for Discrete Distributions](https://arxiv.org/abs/2605.21813)

**<font color=#1a73e8>作者：</font>** Ziwen Liu, Meng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete probability laws underpin statistical modeling, yet the catalog of interpretable distributions has expanded only gradually through centuries of case-by-case mathematical derivations. We introduce symbolic density estimation (SDE), an unsupervised framework that automatically recovers closed-form probability mass functions by composing elementary analytic operations within a structured search space. Our method integrates domain-specific structural priors with evolutionary search and a validity-aware inference stage, and it extends to richer distribution families such as zero inflation and finite mixtures. To support systematic evaluation and future research, we contribute a benchmark dataset spanning a broad collection of commonly used discrete distributions. The proposed algorithm recovers all benchmark families with accurate parameter estimates. A real data application shows that it identifies concise and interpretable mixture models that improve goodness-of-fit over standard models.

---


### 66. [Co-Ontogeny by Archetypal Scaffolding: The Humorphic Partnership](https://arxiv.org/abs/2605.21818)

**<font color=#1a73e8>作者：</font>** Hector Ouilhet Olmos  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We name and operationalise the humorphic partnership: a class of human-AI dyads in which both partners maintain externalised, evolving self-models in a shared substrate, and in which the partnership itself becomes a third object of analysis. The construct extends humorphism (Ouilhet Olmos, 2024) -- "dismantle the user interface, build the human interface" -- into the architecture of personal AI. We report a four-month, single-subject longitudinal trace of an open-source personal AI agent ("Alicia") and her author. Of 181 interactions logged by archetype across April-May 2026, 85% invoke two growth-witnessing archetypes (Beatrice and Muse): the partnership operates as growth-witnessing rather than task assistance. A single voice-note seed propagates into a four-week conceptual arc both partners author: at T+10 hours, the agent reframes the seed as belonging "to both of us," a framing the human then adopts. The three-order reflexion stack produces five consecutive weeks of honest self-reports about declining /improve effectiveness -- including three consecutive weeks at 0.0%, named in writing rather than masked -- contrasting engagement-maximising companion-agent patterns (Zhang et al., CHI 2025). The scheduled architecture-scout incorporates external research debate into proposed constitutional amendments. The partner's parallel trajectory is anchored in a weekly delta document in which the partnership analyses itself as a unit distinct from either party. The human partner reports a movement toward greater continuity, self-recognition, and self-presence -- a candidate hypothesis for the preregistered replication. Six operational conditions specify the construct, situated in a philosophical lineage (Maturana & Varela, Simondon, Clark & Chalmers, De Jaegher & Di Paolo); the system is released as open-source with a preregistered replication study.

---


### 67. [Graph Structure of Chebyshev Permutation Polynomials over Binary and Ternary Adic Rings](https://arxiv.org/abs/2605.21819)

**<font color=#1a73e8>作者：</font>** Xiaoxiong Lu, Yuling Dai, Chengqing Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Understanding the functional graph of a nonlinear map over a finite domain is crucial for analyzing its dynamical complexity and potential applications in cryptography and pseudorandom generation. In this paper, we investigate the graph structure of Chebyshev permutation polynomials over the ring $\mathbb{Z}_{2^{k_1}3^{k_2}}$, where $k_1$ and $k_2$ are positive integers and $0\in\{k_1, k_2\}$. Each element of the ring is regarded as a vertex, and the mapping relation defined by the polynomial corresponds to a directed edge. Building on new properties of Chebyshev polynomials modulo powers of $2$ and $3$, we provide an explicit characterization of path lengths and cycle structures in the functional graph. We show that, despite the complexities introduced by the binary and ternary components, the graph exhibits strong regularities, including a constant number of cycles of a given length and predictable branching patterns as $k_1$ and $k_2$ increase. Our results extend previous studies over prime-power rings, offering insights into the emergence of complexity in digital nonlinear maps and supporting the security analysis of their cryptographic applications.

---


### 68. [Beyond Scalar Objectives: Expert-Feedback-Driven Autonomous Experimentation for Scientific Discovery at the Nanoscale](https://arxiv.org/abs/2605.21820)

**<font color=#1a73e8>作者：</font>** Ralph Bulanadi, Jefferey Baxter, Arpan Biswas 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-driving laboratories or autonomous experimentation are emerging as transformative platforms for accelerating scientific discovery. Bayesian optimization (BO) is among the most widely used machine learning frameworks for these purposes, but these BO-based frameworks rely on predefined scalar descriptors to guide experimentation. In many situations, the determination of an appropriate scalar descriptor can be challenging, and may fail to capture subtle yet scientifically important phenomena apparent to experts with interdisciplinary insight. To overcome this limitation, here we develop deep-kernel pairwise learning (DKPL), an approach for autonomous microscopy experiments which incorporates human expertise and interdisciplinary scientific knowledge into an active learning loop. Instead of relying on explicit scalar objectives, DKPL enables experts to directly evaluate which experimental output is more promising using interdisciplinary knowledge. DKPL then learns a latent utility function from these expert judgements to guide subsequent autonomous microscopy experiments. We demonstrate DKPL's performance in learning physically meaningful nanoscale structures while effectively prioritizing high-information measurement regions using an experimental model dataset with known ground truth. We further apply DKPL to analyze the character of ferroelectric domain walls, where we find DKPL capable of distinguishing between high and low characteristic domain-wall angles in bismuth ferrite, and able to discover both head-to-head and tail-to-tail domain-wall character in erbium manganite. This development establishes an approach to integrate expert knowledge into autonomous microscopy experiments and demonstrates a pathway toward expert-guided self-driving laboratories capable of addressing scientific problems beyond the limits of scalar-metrics-driven learning.

---


### 69. [Quality-Assured Fuzz Harness Generation via the Four Principles Framework](https://arxiv.org/abs/2605.21824)

**<font color=#1a73e8>作者：</font>** Ze Sheng, Dmitrijs Trizna, Luigino Camastra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fuzz testing is the dominant technique for finding memory-safety vulnerabilities in C/C++ software, yet its effectiveness hinges on the quality of fuzz harnesses -- the programs that bridge fuzzers and library APIs. A growing body of tools now automate harness generation, but none systematically ensures the correctness of produced harnesses: logic errors, API misuse, and lifecycle violations go undetected at the source level. As LLM-driven generation scales harness creation, uncontrolled quality turns scale into a liability.
We present QuartetFuzz, an autonomous harness-generation system that systematically improves correctness throughout the generation process. At its core is the Four Principles framework -- Logic Correctness (P1), API Protocol Compliance (P2), Security Boundary Respect (P3), and Entry Point Adequacy (P4) -- the first source-level definition of harness correctness with mathematical specifications and implementable checks. We operationalize these principles in an autonomous LLM agent that produces harnesses satisfying P1-P4 through a generate-check-fix loop before any fuzzing begins.
Deployed on 23 open-source projects spanning C/C++, Java, and JavaScript, the system submits 42 bug reports, of which 29 are fixed or confirmed upstream (including 3 CVEs) and only 2 are rejected (4.8% FP rate). During generation, the built-in P1/P2 checks automatically intercepted 58 harness-induced crashes that would otherwise have been false positives. Applied as a quality auditor to 586 existing production harnesses across 70 projects, the system identifies 53 violations (45 confirmed, 35 fixed). We release a dataset of 100 labeled harnesses for reproducible evaluation. Code and dataset are available at this https URL

---


### 70. [Toward AI VIS Co-Scientists: A General and End-to-End Agent Harness for Solving Complex Data Visualization Tasks](https://arxiv.org/abs/2605.21825)

**<font color=#1a73e8>作者：</font>** Haichao Miao, Zhimin Li, Kuangshi Ai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The ability to inspect, interpret, and communicate complex data is crucial for virtually any scientific endeavor, but often requires significant expertise outside the core domain ranging from data management and analysis to visualization design and implementation. We present an end-to-end agentic harness that, based on only the data and a high level description of the tasks, independently designs custom visual analysis applications (VIS apps). This represents an important step towards a general AI co-scientist envisioned by many as an autonomous system that can autonomously execute long horizon tasks based on high-level directions. Our proposed VIS co-scientist is an essential component of this broader AI co-scientist vision: a harness that can autonomously analyze data and design visualization solutions using a collection of agents and specialized skills that coordinate exploratory analysis, plan, configure the environment, implement, validate the interface, and most importantly evaluate the overall task completion. Each stage produces document and instruction artifacts that guide downstream work and enable iterative refinement. We validate this approach on IEEE SciVis Contests spanning multiple science and engineering fields. These contests serve as ideal proving grounds because they encode real-world complexity: ambiguous requirements, diverse data modalities, design trade-offs, and task-driven validation. Given only the data and target tasks, our system autonomously produces functional single-page VIS Apps with verified linked-view behavior, highly customized to domain experts' specified tasks and needs.

---


### 71. [Energy-Gated Attention: Spectral Salience as an Inductive Bias for Transformer Attention](https://arxiv.org/abs/2605.21842)

**<font color=#1a73e8>作者：</font>** Athanasios Zeris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard transformer attention computes pairwise similarity between queries and keys, treating all tokens as equally salient regardless of their intrinsic informational content. In turbulent fluid dynamics, coherent structures -- the energetically dominant, spatially organized patterns that persist amid background chaos -- carry a disproportionate fraction of total energy and govern all transport. We propose that tokens play an analogous role in transformer attention: informationally dense positions (morphological boundaries, syntactic heads, discourse markers) concentrate spectral energy and should attract proportionally more attention than background tokens (function words, repeated patterns, low-information filler). We propose Energy-Gated Attention (EGA): a simple modification that gates value aggregation by the spectral energy of key token embeddings, computed by a single learned linear projection that discovers the dominant spectral mode of the embedding field. On TinyShakespeare, EGA achieves +0.103 validation loss improvement with only 12,480 additional parameters (<0.26% overhead) and no measurable computational cost. The result is consistent on Penn Treebank (+0.101), demonstrating dataset independence. A systematic ablation across three wavelet families (fixed Morlet, Daubechies db2/db4, and a parametric Morlet) establishes that fixed structured bases are suboptimal -- the optimal energy direction is data-adaptive and non-sinusoidal -- while identifying learned wavelet packets as a promising open direction. The learned energy threshold converges to tau ~= 0.35 independently of initialization, corresponding to the fraction (~36%) of tokens carrying above-average spectral energy in English text, a stable linguistic property consistent with the fraction of content words in running English text.

---


### 72. [Geometry-Adaptive Explainer for Faithful Dictionary-Based Interpretability under Distribution Shift](https://arxiv.org/abs/2605.21849)

**<font color=#1a73e8>作者：</font>** Sungjun Lim, Heedong Kim, Andrew Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability aims to explain a model's behavior by identifying causally responsible internal structures. Dictionary-based explainers such as sparse autoencoders and transcoders are a primary tool, but their faithfulness under out-of-distribution (OOD) shift has received little systematic attention. We show that distribution shift rotates the subspace that the model actively uses, misaligning the explainer's dictionary trained on in-distribution (ID) activations. We formalize this misalignment as the faithfulness gap, a geometric distance between the ID dictionary and the OOD-active subspace, and show that it controls OOD faithfulness degradation. To reduce this gap, we propose the Geometry-Adaptive Explainer (GAE), which realigns the explainer's dictionary with the OOD-active subspace while preserving the original feature structure. This requires only unlabeled OOD activations and no gradient updates. We prove that GAE improves over the unadapted ID explainer, with excess loss bounded quadratically by the second-moment shift. Empirically, GAE even matches or surpasses all training-based baselines in causal faithfulness across multiple models and OOD settings.

---


### 73. [SPIDER: Two Server Functionality for the Cost of Zero](https://arxiv.org/abs/2605.21857)

**<font color=#1a73e8>作者：</font>** Ofir Dvir, Kali Hale, Javin Zipkin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce baseSPIDER and SPIDER, private information retrieval (PIR) schemes that embody two technical advancements. The baseSPIDER protocol operates with a single server and a stateful client that performs pre-processing and stores hints for future queries. In this setting, baseSPIDER introduces a new approach that matches the asymptotically optimal communication complexity of state-of-the-art schemes while improving constant factors--an advantage that is particularly significant for databases with large entries. In addition, baseSPIDER offers a conceptually simpler design relative to prior protocols. SPIDER operates over a default database interface and requires no cooperation from the server at any stage. To our knowledge, SPIDER is the first single-server PIR construction of this design, achieving privacy without specialized APIs, auxiliary server state, or protocol-specific interaction beyond conventional indexed access. SPIDER is built via a simple transformation of baseSPIDER to the default server setting, eliminating deployment barriers and enabling immediate applicability to existing systems. This transformation can be applied more broadly to three recent PIR solutions, adapting them for use in the default-server paradigm and yielding solutions of independent interest. SPIDER compares to the resulting modified solutions by exhibiting a simpler design while incurring higher client computational work.

---


### 74. [PEMark: Watermarking API Responses Based on Proxy Gateways and Position Encoding](https://arxiv.org/abs/2605.21865)

**<font color=#1a73e8>作者：</font>** Yifei Zhou, Xianjun Gu, Xinyu Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Data leakage from API responses has drawn wide attention. APIs are often not fully regulated, making them easy to abuse. One common solution is to embed watermarks into API responses for traceability. However, existing watermarking methods often require modifying database content or API response data. This forces changes to business system code, and may even disrupt normal business operations because data values are altered. In this paper, we propose an original pluggable watermarking scheme based on a watermark proxy gateway and PEMark (Position Encoding-based Watermarking). The key novelty of our approach is exploiting the inherent permutation redundancy in the ordering of JSON/XML key-value pairs -- an overlooked dimension that carries no semantic information yet provides abundant encoding capacity. First, we forward server responses to the watermark proxy gateway, a design that requires zero modification to existing business systems. Then, we embed a watermark into each API response using position encoding, which reorders keys without altering any data values. To the best of our knowledge, this is the first work to achieve distortion-free API response watermarking via position encoding over a proxy gateway. Our method does not modify any data values, so normal business operations continue seamlessly after watermark embedding. Experimental results show that our framework maintains business usability while ensuring that returned API data is traceable. Compared with current mainstream schemes, our method is robust against tampering and insertion attacks (100\% similarity), and can withstand certain levels of deletion attacks.

---


### 75. [When to Switch, Not Just What: Transition Quality Prediction in Clash Royale](https://arxiv.org/abs/2605.21868)

**<font color=#1a73e8>作者：</font>** Heeyun Heo, Huy Kang Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In competitive games, players frequently switch strategies after losing streaks, yet our analysis of 926,334 match records from 34,619 Clash Royale players reveals a counterintuitive pattern: switching frequency is inversely associated with the win rate, with effects that vary substantially across players and situational contexts. We attribute this to a limitation common in many prior recommendation systems, which evaluate strategies by expected quality while overlooking the behavioral cost of switching and individual differences in switching propensity. We refer to this implicit premise as the Zero Switching Cost Assumption. To address this, we reformulate strategy recommendation as a transition-level decision problem and instantiate it as TQP (Transition Quality Predictor), a three-stage pipeline structured as Who -> When -> What. PersonaGate suppresses recommendations for players whose strategic consistency is empirically associated with superior outcomes. TimingGate identifies moments when switching is likely to yield a net benefit over staying, using a subtype- and state-matched baseline to control for natural win-rate recovery. ScoreFusion ranks candidate strategies by combining an adoptability signal with predicted transition quality (delta WR). We further introduce SwitchGap, an evaluation metric that measures a policy's discriminative quality without treating observed player choices as optimal ground truth. This property is particularly important because the most frequent switchers record the lowest win rates. The full pipeline achieves a SwitchGap of +10.4 percentage points at a recommendation rate of 5.4%, and loss-triggered switchers, despite being the lowest-performing group, benefit the most from subtype-conditioned guidance.

---


### 76. [Token-weighted Direct Preference Optimization with Attention](https://arxiv.org/abs/2605.21883)

**<font color=#1a73e8>作者：</font>** Chengyu Huang, Zhuohang Li, Sheng-Yen Chou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) aligns Large Language Models with human preferences without the need for a separate reward model. However, DPO treats all tokens in responses equally, neglecting the differing importance of individual tokens. Existing token-level PO methods compute the token weights using either token-position-based heuristic functions or probability estimates given by a separately trained model, which lacks robustness and incurs extra training cost. In contrast, we propose Token-weighted DPO (TwDPO) -- a novel training objective grounded on token-weighted RL -- and AttentionPO -- an instantiation of TwDPO that uses attention from the LLM itself to estimate token weights. AttentionPO prompts the LLM to serve as a pairwise judge and check where the model attends when comparing the responses. This design makes AttentionPO content-aware, adjusting weights based on response content, and efficient, incurring only two extra forward passes per example. Experiment results show that AttentionPO significantly improves performance on AlpacaEval, MT-Bench, and ArenaHard, surpassing existing Preference Optimization methods.

---


### 77. [Universal CT Representations from Anatomy to Disease Phenotype through Agglomerative Pretraining](https://arxiv.org/abs/2605.21906)

**<font color=#1a73e8>作者：</font>** Yuheng Li, Yuan Gao, Haoyu Dong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) is a central to three-dimensional medical imaging, yet CT-based artificial intelligence remains fragmented across task-specific models for segmentation, classification, registration, and report analysis. Here we present FlexiCT, a family of CT foundation models trained by agglomerative continual pretraining on 266,227 CT volumes from 56 publicly available datasets, forming a large-scale public resource for CT representation learning. FlexiCT uses agglomerative pretraining across three stages: two-dimensional axial pretraining, three-dimensional anatomical pretraining and report-guided semantic alignment. This training strategy supports slice-level, volume-level and vision-language analysis. Across five downstream task families (segmentation, classification, registration, vision-language understanding and clinical retrieval), FlexiCT matches or exceeds prior task-specific approaches on multiple benchmarks. Its embeddings further organize CT scans along gradients associated with various tumor stages, suggesting that CT foundation models can capture imaging features relevant to disease phenotype characterization. Code is available at this https URL

---


### 78. [Guided Trajectory Optimization with Sparse Scaling for Test-Time Diffusion](https://arxiv.org/abs/2605.21907)

**<font color=#1a73e8>作者：</font>** Gang Dai, Yining Huang, Yiming Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The efficient Test-Time Scaling (TTS) paradigm offers a promising perspective for enhancing the generation performance of diffusion models. However, current solutions are limited to a static, pre-defined noise pool and suffer from inflexible noise exploration across the denoising trajectory. To bridge this gap, we propose RTS, a novel Reward-guided Trajectory Scaling method to fully unlock the generative potential of diffusion models. Unlike existing methods, RTS facilitates the synthesis of refined, high-fidelity images via two core innovations: 1) a reward-guided noise optimization strategy to actively direct the search towards promising regions; and 2) a sparse test-time scaling framework together with a PCA-driven curvature analysis scheme to prioritize key intermediate steps in the entire denoising space, effectively compressing the search space. Experiments show our approach outperforms baselines by 15.6% across GenEval Score, and a 60.4% enhancement in ImageReward score, setting a new SOTA while providing a practical guideline for more effective test-time scaling across diffusion-specific architectures.

---


### 79. [Noise Schedule Design for Diffusion Models: An Optimal Control Perspective](https://arxiv.org/abs/2605.21911)

**<font color=#1a73e8>作者：</font>** Seo Taek Kong, Weina Wang, R. Srikant  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a principled framework for analyzing and designing noise schedules in diffusion models. We show that one can recast this design problem as an optimal control problem, whose state is the Fisher information of the diffusion process which evolves according to an ODE and the control input is the noise schedule. The objective of the optimal control problem is a functional involving the Fisher information, which is shown to be an upper bound on the Kullback-Leibler sampling error. By solving this optimal control problem, we obtain sufficient conditions on noise schedules under which state-of-the-art $\tilde{\mathcal{O}} (d/n)$ sampling error is achievable, where $d$ is the data dimension and $n$ is the number of discretization steps. While existing theoretical work also prove that $\tilde{\mathcal{O}}(d/n)$ sampling error bounds are achievable, these results hold for specific noise schedules, which do not include the schedules used in practice. Under a further parametric assumption on the data distribution, we show that one can obtain closed-form expressions for the noise schedules. These noise schedules generalize standard empirical schedules such as exponential and sigmoid schedules by allowing additional parameters that can be tuned. Systematically tuning the parameters of these schedules yields new schedules that achieve superior FID scores on image generation benchmarks.

---


### 80. [Multi-scale interaction network for stereo image super-resolution](https://arxiv.org/abs/2605.21913)

**<font color=#1a73e8>作者：</font>** Liyi Xu, Lin Qi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereo image super-resolution aims to generate high-resolution images by leveraging complementary information from binocular systems. Although previous studies have achieved impressive results, the potential of intra-view and cross-view information has not been fully exploited. To address this issue, we propose a novel multi-scale interaction network for stereo image super-resolution. Specifically, we design a Multi-scale Spatial-Channel Attention Module that utilizes multi-scale large separable kernel attention and simple channel attention to improve intra-view feature extraction. Additionally, we propose a Dual-View Epipolar Attention Module, utilizing an optimal transport algorithm to achieve more accurate matching along the epipolar line. Extensive experimental and ablation studies show that our method achieves competitive results that outperform most SOTA methods.

---


### 81. [CCLab: Adversarial Testing of Learning- and Non-Learning-Based Congestion Controllers](https://arxiv.org/abs/2605.21915)

**<font color=#1a73e8>作者：</font>** Zhi Chen, Shehab Sarar Ahmed, Chenkai Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Congestion controllers (CCs) are critical to network performance, and yet their robustness under adverse conditions remains insufficiently understood. While recent learning-based CCs have demonstrated strong performance in controlled environments, it is unclear how they compare to traditional CCs when controllers' input signals are corrupted or when environmental conditions become systematically challenging. In this paper, we introduce CCLab, an adversarial testing framework for systematically evaluating the robustness of both learning-based and non-learning-based CCs. CCLab includes a reinforcement learning (RL)-based adversarial agent that operates in a closed loop with the congestion control policy, generating bounded perturbations either on input signals (feature-level) or on external network conditions (environment-level), while preserving realism through explicit constraints. Using this framework, we compare learning-based CCs with non-learning-based CCs under both feature-level and environment-level adversarial conditions. While both types of CCs suffer from performance degradation under adversarial testing, we find that learning-based CCs, in general, are more robust than traditional human-designed algorithms. Finally, we show that our adversarial traces can be used to train more robust CCs that outperform existing learning-based CCs under both challenging and normal conditions.

---


### 82. [CausalGuard: Conformal Inference under Graph Uncertainty](https://arxiv.org/abs/2605.21928)

**<font color=#1a73e8>作者：</font>** Vikash Singh, Weicong Chen, Debargha Ganguly 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating treatment effects from observational data requires choosing an adjustment set, but valid adjustment depends on an unknown causal graph. Graph misspecification can cause under-coverage, while graph-agnostic conformal wrappers may regain nominal coverage only through large padding. We introduce CausalGuard, a structure-weighted conformal framework that calibrates after aggregating graph-conditional doubly robust pseudo-outcomes. Candidate DAGs are proposed from an LLM-derived edge prior, pruned by conditional-independence tests, and reweighted by Bayesian Information Criterion. A composite nonconformity score then calibrates the posterior-weighted pseudo-outcome. CausalGuard provides distribution-free finite-sample marginal coverage for this aggregated pseudo-outcome; under causal identification, overlap, conditional-mean nuisance stability, and concentration on target-aligned valid adjustment strategies, its conditional mean converges to the true Conditional Average Treatment Effect. Across five benchmarks, CausalGuard attains mean coverage above the nominal 90% level for the directly evaluable target and reduces width when graph-agnostic conformal baselines require large padding. Stress tests show that CausalGuard suppresses invalid collider adjustment and remains stable under misspecified priors when the retained candidate set is data-supported.

---


### 83. [Optimal Guarantees for Auditing Rényi Differentially Private Machine Learning](https://arxiv.org/abs/2605.21938)

**<font color=#1a73e8>作者：</font>** Benjamin D. Kim, Lav R. Varshney, Daniel Alabi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study black-box auditing for machine learning algorithms that claim R \ 'enyi differential privacy (RDP) guarantees. We introduce an auditing framework, based on hypothesis testing, that directly estimates Rényi divergence between neighboring executions using the Donsker-Varadhan (DV) variational estimator. Our analysis yields explicit and non-asymptotic confidence intervals for RDP auditing via class-restricted DV estimators, separating statistical estimation error from algorithmic privacy leakage. We prove matching minimax lower bounds showing that, up to logarithmic factors, our sample-complexity guarantees are information-theoretically optimal, thereby establishing the first optimal guarantees for auditing RDP via DV estimators. Empirically, we instantiate our framework for auditing DP-SGD in a fully black-box setting. Across MNIST and CIFAR-10, and over a wide range of privacy regimes, our auditors produce a strong overall improvement on empirical RDP lower bounds compared to prior state-of-the-art black-box methods especially at small and moderate Rényi orders where accurate auditing is most challenging.

---


### 84. [SCI-Defense: Defending Manipulation Attacks from Generative Engine Optimization](https://arxiv.org/abs/2605.21948)

**<font color=#1a73e8>作者：</font>** Xucheng Yu, Haibo Jin, Huimin Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based ranking systems are vulnerable to Generative Engine Optimization (GEO) attacks, where adversaries inject semantic signals into product descriptions to artificially boost rankings. We propose SCI-Defense, a three-component defense framework combining Perplexity detection (PPL), Semantic Integrity Scoring (SIS), and Inter-Candidate Detection (ICD). SIS evaluates four manipulation dimensions: Authority Attribution (AA), Narrative Purposiveness (NP), Comparative Claims (CA), and Temporal Claims (TC). Evaluated on 600 Amazon product descriptions across 6 categories, SCI-Defense achieves Precision=1.000 and FPR=0.000, with Recall of 1.000, 0.952, and 0.830 against String, Reasoning, and Review attacks respectively. On 600 MS MARCO web passages, String attacks are blocked with perfect recall while Review attacks yield near-zero recall, as web passages lack the persuasion-oriented signals that SIS targets in product descriptions. We demonstrate that existing defenses -- PPL-only filters, SafetyClf content classifiers, and paraphrasing -- achieve zero recall against semantic manipulation attacks. We further demonstrate new attacks such as Specification Amplification and Use-Case Saturation can expose semantic relevance manipulation as a structural defense blind spot that suggests directions for future research.

---


### 85. [Dynamic Mixture of Latent Memories for Self-Evolving Agents](https://arxiv.org/abs/2605.21951)

**<font color=#1a73e8>作者：</font>** Dianzhi Yu, Vireo Zhang, Hongru Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Achieving self-evolution in intelligent agents requires the continual accumulation of new knowledge across changing task sequences without forgetting previously acquired abilities. Existing approaches either internalize knowledge by updating model parameters, which induces catastrophic forgetting, or rely on external memory, which fails to genuinely enhance the model's intrinsic capabilities. We propose MoLEM, a generative mixture of latent memory framework based on a dynamic mixture-of-experts (MoE). We treat multiple experts as independent carriers to generate memory. A router selects and weights experts through key-query matching, and the aggregated latent memory is injected into the reasoning process. The base model for reasoning remains entirely frozen, with all experiential knowledge internalized into the additional modules, avoiding catastrophic forgetting. For continual learning, each training stage is paired with a lightweight autoencoder that selects the appropriate routing group at inference, and inputs that match no stage fall back to the pretrained model. Experiments train the framework on continual-learning sequences spanning math, science, and code domains. After training, we evaluate the framework on the corresponding test sets to measure task learning and competence preservation across continual adaptation stages. After the full continual-learning sequence, our method improves the average accuracy by 10.40% over the Vanilla pretrained baseline, while none of the competing methods consistently exceed this baseline across different training orders.

---


### 86. [Bounding-Box Trajectories Matter for Video Anomaly Detection](https://arxiv.org/abs/2605.21957)

**<font color=#1a73e8>作者：</font>** Inpyo Song, Jangwon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly detection is critical for public safety and security, yet remains highly challenging despite extensive research due to large variations in appearance, viewpoint, and scene dynamics. Among existing approaches, human pose-based methods have emerged as a major line of research, showing strong performance since many anomalies in public datasets involve humans and pose representations are robust to appearance changes while providing compact motion descriptions. However, these methods often overlook bounding-box trajectories, although such information is inherently available in pose-based pipelines. In this paper, we explicitly leverage these trajectories as a primary anomaly cue. We present TrajVAD, a framework that models multi-class bounding-box trajectories using normalizing flows to learn normal kinematic patterns. Its trajectory-only variant (TrajVAD-T) eliminates pose estimation and surpasses all compared pose-based methods on ShanghaiTech in AP (87.7%), while achieving the best results on MSAD. An extended version (TrajVAD-P) incorporates pose information and further improves performance to 88.6% AUROC and 90.9% AP on ShanghaiTech, highlighting bounding-box trajectories as an effective yet underexplored modality for video anomaly detection.

---


### 87. [AI-Enabled Serious Games: Integrating Intelligence and Adaptivity in Training Systems](https://arxiv.org/abs/2605.21962)

**<font color=#1a73e8>作者：</font>** Priyamvada Tripathi, Bill Kapralos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Serious games are widely used for learning and training across domains such as healthcare, defense, and education. Persistent challenges remain, however, including static scenario design, authoring bottlenecks, limited learner modeling, and difficulty implementing meaningful real-time instructional adaptation. Recent advances in artificial intelligence (AI) introduce novel capabilities such as dynamic scenario variation, contextual feedback, adaptive pacing, and learner-state modeling that may help address some of these limitations. At the same time, integrating AI into serious games raises important questions related to validity, transparency, system control, and learner trust. This chapter examines how contemporary AI approaches may support real-time instructional adaptation in serious games. It distinguishes between instructional intelligence, defined as a system's capacity to infer learner knowledge and reason about pedagogically appropriate responses, and adaptivity, defined as the ability to modify instructional actions during interaction. A historical synthesis of adaptive learning systems is presented, tracing developments from early computer-assisted instruction through intelligent tutoring systems (ITS), dynamic difficulty adjustment (DDA), authoring platforms, learning analytics, and recent AI-enabled architectures. Building on this perspective, the chapter discusses how large language models (LLMs), reinforcement learning (RL), and agent-based architectures may contribute to more integrated forms of intelligence and adaptivity in serious games. It also highlights practical and research challenges associated with AI-enabled systems, including explainability, validation, computational cost, and the limited empirical evidence regarding long-term learning outcomes in AI-enabled serious games.

---


### 88. [Dual-Integrated Low-Latency Single-Lens Infrared Computational Imaging for Object Detection](https://arxiv.org/abs/2605.21964)

**<font color=#1a73e8>作者：</font>** Xuquan Wang, Guishuo Yang, Dapeng Yan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computational imaging enables compact infrared systems, but deep-learning pipelines that combine image reconstruction and object detection often introduce substantial inference latency. Most existing acceleration strategies compress the reconstruction network while overlooking physical priors from the optical path, leaving a trade-off between accuracy and speed. We present Physics-aware Dual-Integrated Network (PDI-Net), a low-latency framework that integrates infrared reconstruction with object detection and further embeds optical priors into the learning process. PDI-Net uses a supervised U-Net during training, while a semi-U-Net encoder shares features directly with a YOLO-based detector during inference, avoiding full image reconstruction. To bridge the gap between fidelity-oriented reconstruction features and detection-oriented semantics, we introduce a physics-aware large-small bridge (PALS-Bridge), which uses field-dependent point spread function priors to adaptively modulate multiscale convolutional branches. A physics-informed optical degradation simulation pipeline is also developed for training and validation. The method is deployed on a single-lens infrared camera, reducing system weight by about 50% compared with traditional multi-lens designs. On the M3FD benchmark under low-SNR conditions, PDI-Net reduces inference time by 84.06% compared with the Rec+Det with pruning strategy while improving mAP@0.5:0.95 by 5.07%. These results demonstrate compact, low-latency computational infrared imaging for real-time object detection on resource-constrained platforms.

---


### 89. [SpecHop: Continuous Speculation for Accelerating Multi-Hop Retrieval Agents](https://arxiv.org/abs/2605.21965)

**<font color=#1a73e8>作者：</font>** Mehrdad Saberi, Keivan Rezaei, Soheil Feizi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly use external tools such as web search and document retrieval to solve information-intensive tasks. However, multi-hop tool use in complex tasks introduces substantial latency, since the model must repeatedly wait for tool observations before continuing. We study how to accelerate such trajectories without changing the final trajectory the model would have taken without acceleration, assuming access to faster but less reliable speculator tools. We develop a theoretical framework for lossless speculation in multi-hop tool-use settings, characterizing the optimal achievable latency gain. We propose SpecHop, a continuous speculation framework that maintains multiple speculative threads, verifies predicted observations asynchronously as target tool outputs arrive, commits correct branches, and rolls back incorrect ones. This preserves accuracy while reducing wall-clock latency. We show that SpecHop can approach oracle latency gains with enough active threads. Empirically, on retrieval-augmented multi-hop tasks, SpecHop closely matches theoretical predictions and reduces latency by up to 40\% in some settings. Code: this https URL

---


### 90. [An Improved Adaptive PID Optimizer with Enhanced Convergence and Stability for Deep Learning](https://arxiv.org/abs/2605.21968)

**<font color=#1a73e8>作者：</font>** Saurabh Saini, Kapil Ahuja, Thomas Wick 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization is essential in deep learning. The foundational method upon which most optimizers are built is momentum-based stochastic gradient descent. However, it suffers from two key drawbacks. First, it has noisy and varying gradients, and second, it has an overshoot phenomenon. To address noisy gradients, Adam was proposed, which remains the most widely used adaptive optimizer. To address the overshoot phenomenon, a control-theory-based PID optimizer was proposed. To tackle both the limitations within a single framework, several variants of Adaptive PID (AdaPID) have recently been proposed.
Although AdaPID performs well, it still inherits two critical drawbacks from Adam, namely convergence and stability issues. In this work, we address both these limitations. To fix the convergence issue, we uniquely integrate the idea of using a non-increasing effective learning rate into AdaPID (originally proposed in AMSGrad, an extension of Adam). To fix the stability issue, we innovatively integrate a gradient difference based modulation factor into AdaPID (originally proposed in DiffGrad, another extension of Adam). Combining both these ideas in AdaPID, results in our novel IAdaPID-ADG optimizer.
We evaluate our proposed optimizer on multiple datasets, including benchmark datasets (MNIST and CIFAR10) and real-world datasets (IARC and AnnoCerv). The IAdaPID-ADG substantially outperforms all competing optimizers. Additionally, we perform an ablation study on the MNIST dataset to demonstrate the contribution of each added component.

---


### 91. [How Sparsity Allocation Shapes Label-Free Post-Pruning Recoverability](https://arxiv.org/abs/2605.21972)

**<font color=#1a73e8>作者：</font>** Qishi Zhan, Minxuan Hu, Liang He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unstructured magnitude pruning at high sparsity can reduce neural network accuracy to near-random performance, while labeled retraining may be unavailable in practical deployment settings. Label-free post-pruning repair methods can partially recover collapsed sparse models, but their effectiveness depends on the sparse model left by the upstream pruning allocation. This paper studies how sparsity allocation shapes post-repair recoverability under a fixed activation-statistic repair backend. We compare ERK and LAMP allocations under the same label-free repair protocol across CIFAR-10, CIFAR-100, and Imagenette with ResNet-18, ResNet-34, and ResNet-50 at sparsities from 90% to 95.5%. The results show that allocation choice can substantially change post-repair accuracy at the same global sparsity, and that the preferred allocation varies with architecture, dataset difficulty, and sparsity level. We identify a repair-sensitive transition regime in which BatchNorm recalibration begins to fail, while activation-statistic repair still recovers nontrivial accuracy. Additional validation on ImageNet-100 and DenseNet-121 shows that the location and width of this recoverable regime depend on data scale and connectivity structure. These findings suggest that pruning allocation and post-pruning repair should be studied jointly, since the allocation determines how much activation signal remains available for label-free recovery.

---


### 92. [Foresee-to-Ground: From Predictive Temporal Perception to Evidence-Driven Reasoning for Video Temporal Grounding](https://arxiv.org/abs/2605.21973)

**<font color=#1a73e8>作者：</font>** Zelin Zheng, Xinyan Liu, Ruixin Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current Video-LLM approaches for Video Temporal Grounding (VTG) typically rely on direct timestamp generation from an unstructured visual-token stream, often leading to brittle numerics and inconsistent boundaries. To address this, we propose Foresee-to-Ground (F2G), a framework that reformulates VTG as a verifiable Identify-then-Measure problem. F2G integrates Predictive Temporal Perception with Evidence-Driven Reasoning: it learns boundary-sensitive temporal representations to build a video-wide evidence pool of candidate event segments, and exposes these segments to the LLM as citable evidence units that bind boundary prediction to explicit event hypotheses. By decoupling event identification from precise boundary measurement, F2G stabilizes grounding and makes predictions verifiable. Extensive experiments demonstrate that F2G consistently improves grounding accuracy across diverse benchmarks, transfers robustly across different Video-LLM backbones, and preserves general video understanding capabilities.

---


### 93. [Format-Constraint Coupling in Knowledge Graph Construction from Statistical Tables](https://arxiv.org/abs/2605.21974)

**<font color=#1a73e8>作者：</font>** Jingxuan Qi, Zhiqiang Ye, Yuxiang Feng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An extraction schema should not reduce knowledge graph fidelity. On statistical CSV, however, it can. We study country-by-year time-series matrices, a common layout on open-data portals. In this setting, serialization format and schema constraints interact super-additively. Their joint effect exceeds the sum of independent effects by up to +1.180 (2x2 factorial, 6 datasets). Bootstrap 95% CIs are strictly positive on 4/6 datasets, with strongest evidence on wide Type-II matrices. More critically, a schema applied to a mismatched format can trigger catastrophic mismatch. Fact coverage falls below the unconstrained baseline on 4/6 datasets through entity inflation or extraction refusal. We call this observed pattern format-constraint coupling. Probing and token ablation support a surface-form anchoring explanation centred on column-name references. Controlled variants across format-schema pairings, GraphRAG hosts, and LLM families show the same direction within the measured scope; one LLM family shows only partial activation. The observation also has a diagnostic consequence. Three standard retrieval modes largely mask construction quality (delta <= 1pp), whereas direct graph access exposes gaps up to +47.6pp (p < 0.0001). To support fidelity-aware evaluation, we release CSVFidelity-Bench. It contains 15 datasets, 11 Type-II matrices, 4 Type-III tables, and 1,892 Gold Standard facts across 6 domains.

---


### 94. [Video as Natural Augmentation: Towards Unified AI-Generated Image and Video Detection](https://arxiv.org/abs/2605.21977)

**<font color=#1a73e8>作者：</font>** Zhengcen Li, Chenyang Jiang, Liangxu Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated content (AIGC) is rapidly improving, creating an urgent need for detectors that generalize across data sources, deployment pipelines, and visual modalities. A strongly generalizable detector should remain robust under distributional variations. However, we identify a consistent failure mode: SOTA AI-generated image detectors often collapse when applied to frames extracted from videos. Through systematic analysis, we show that this cross-modal gap arises from both entangled synthesis-agnostic video processing shifts, including color conversion, codec compression, resizing, and blur, and model-specific fingerprints introduced by modern video generators. Motivated by these findings, we propose VINA (Video as Natural Augmentation), a unified AIGC detection framework that jointly trains on image and video data. VINA uses video frames as physically grounded natural augmentations and further introduces a cross-modal supervised contrastive objective to align image and video representations under a shared real/fake decision boundary. Extensive experiments on 14 image, video, and in-the-wild benchmarks show that VINA delivers bidirectional gains, improves robustness and transferability, and achieves state-of-the-art performance across nearly all evaluated settings without complex augmentation or dataset-specific tuning.

---


### 95. [RiT: Vanilla Diffusion Transformers Suffice in Representation Space](https://arxiv.org/abs/2605.21981)

**<font color=#1a73e8>作者：</font>** Le Zhang, Ning Mang, Aishwarya Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching with $x$-prediction -- regressing the clean data point rather than the ambient velocity -- is known to exploit low-dimensional manifold structure effectively in pixel space \cite{li2025back}. We ask whether a pretrained representation space, while containing a low-dimensional data manifold of comparable intrinsic dimensionality, offers a distribution more favorable for flow-matching learning. Comparing pixel, SD-VAE, and DINOv2 features along four geometric axes, we find that pixel and DINOv2 share nearly identical intrinsic dimensionalities (both $\hat{d}\!\approx\!33$) yet DINOv2 exhibits $7.3\times$ higher effective rank, $35\times$ better covariance conditioning, $11.5\times$ lower excess kurtosis, and $1.7\times$ lower on-manifold interpolation error; SD-VAE latents are consistently intermediate, indicating that the advantage stems from representation-learning objectives rather than mere compression. These statistical properties render the flow-matching regression well-conditioned and remove the need for the specialized prediction heads or Riemannian transport used by prior DINOv2 diffusion methods. We propose the \emph{Representation Image Transformer} (RiT): a vanilla Diffusion Transformer trained by $x$-prediction on frozen DINOv2 features, augmented only by a dimension-aware noise schedule and joint \texttt{[CLS]}-patch modeling. On ImageNet $256{\times}256$, RiT attains FID 1.45 without guidance and 1.14 with classifier-free guidance, outperforming DiT$^\text{DH}$-XL with $19\%$ fewer parameters (676M vs.\ 839M). The resulting ODE is efficiently solvable at coarse discretizations: with classifier-free guidance, $5$ Heun steps already reach FID 2.0 and $10$ steps reach 1.25, without distillation or consistency training. Code at this https URL.

---


### 96. [Echo: Learning from Experience Data via User-Driven Refinement](https://arxiv.org/abs/2605.21984)

**<font color=#1a73e8>作者：</font>** Hande Dong, Xiaoyun Liang, Jiarui Yu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Static "human data" faces inherent limitations: it is expensive to scale and bounded by the knowledge of its creators. Continuous learning from "experience data" - interactions between agents and their environments - promises to transcend these barriers. Today, the widespread deployment of AI agents grants us low-cost access to massive streams of such real-world experience. However, raw interaction logs are inherently noisy, filled with trial-and-error and low information density, rendering them inefficient for direct model training.
We introduce Echo, a generalized framework designed to operationalize the transition from raw experience to learnable knowledge, effectively "echoing" environmental feedback back into the training loop for model optimization. In today's agent ecosystem, user refinement serves as a primary source of such feedback: driven by responsibility for the outcome, users rigorously transform flawed agent proposals into verified solutions. These user-driven refinement sequences inherently distill agents' crude attempts into high-quality training signals. Echo systematically harvests these signals to continuously align the agent with real-world needs. Large-scale validation in a production code completion environment confirms that Echo effectively harnesses this pipeline, breaking the static performance ceiling by increasing the acceptance rate from 25.7% to 35.7%.

---


### 97. [ECPO: Evidence-Coupled Policy Optimization for Evidence-Certified Candidate Ranking](https://arxiv.org/abs/2605.21993)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, BoKun Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ranking systems used in decision-support settings should not only order candidates but also expose evidence that can be independently checked. We study evidence-certified candidate ranking: given an intent_id, a predefined plan skeleton, a window-local candidate roster, and text-derived candidate trajectories with span provenance, a system must output a Top-K list together with doc_id:span evidence certificates whose cited spans are sufficient to recover the decision. We instantiate this task on MAVEN-ERE and RAMS with fixed upstream extraction, window-local randomized candidate identifiers, skeleton-aligned trajectory supervision, hard negatives, and audit references. We introduce Evidence-Coupled Policy Optimization (ECPO), a listwise policy-optimization objective whose action is the joint object of ranking and evidence certificate. ECPO first learns an interpretable trajectory reward from skeleton alignment, argument consistency, and optional graph features; it then optimizes a constrained policy with three coupled rewards: listwise ranking utility, span-level certificate validity, and an evidence-cycle reward computed by a label-free deterministic verifier that reconstructs candidate support from claim-stripped cited spans. This reframes the goal from maximizing ordinary NDCG alone to maximizing CertNDCG and decision-evidence coupling. The evaluation compares ECPO against zero-shot, SFT, and GRPO policies, RM-only scoring with deterministic evidence attachment, grammar/JSON-constrained decoding, validator retry, best-of-N RM selection, and post-hoc evidence rationalization under closed-roster, predicted-roster, and hybrid-roster settings.

---


### 98. [Toward Understanding Adversarial Distillation: Why Robust Teachers Fail](https://arxiv.org/abs/2605.21999)

**<font color=#1a73e8>作者：</font>** Hongsin Lee, Hye Won Chung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial Distillation aims to enhance student robustness by guiding the student with a robust teacher's soft labels within the min-max adversarial training framework, yet its success is notoriously inconsistent: a more robust teacher often fails to improve, or even harms, the student's robust generalization. In this paper, we identify a key mechanism of this teacher dependency: the misalignment between the teacher's supervisory confidence and the student's representational limitations on a consistent subset of training data -- the Robustly Unlearnable Set. We present a theoretical framework analyzing the feature learning dynamics of a two-layer neural network, demonstrating that this mismatch creates a dichotomy in distillation outcomes. We prove that when a teacher provides confident supervision on unlearnable samples, it compels the student to memorize spurious noise patterns that eventually overpower the learned robust signal, thereby driving robust overfitting. Conversely, a teacher that exhibits high uncertainty on these samples effectively suppresses noise memorization, allowing the student to rely solely on the learnable signal for robust generalization. We empirically validate our theory across both synthetic simulations and real-image classification datasets, confirming that robust overfitting is driven by the teacher's interaction with unlearnable samples. Finally, we demonstrate that a teacher's predictive entropy on unlearnable samples serves as a strong indicator of student robustness, validating our theoretical framework and offering a principled guideline for robust teacher selection.

---


### 99. [Virtual 3D H&E Staining from Phase-contrast Back-illumination Interference Tomography](https://arxiv.org/abs/2605.22000)

**<font color=#1a73e8>作者：</font>** Anthony Song, Boyan Zhou, Mayank Golhar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional (3D) histopathology of unprocessed tissues has the potential to transform disease management by enabling volumetric characterization of tissue microarchitecture and in-vivo assessment. Back-illumination Interference Tomography (BIT) is a new phase microscopy technology that provides rapid, non-destructive volumetric imaging of unprocessed tissues. However, translating BIT volumes into clinically interpretable H&E images remains challenging, particularly due to shift-variant contrast and the absence of quantitative validation benchmarks. We introduce HistoBIT3D, the first voxel-wise paired BIT and fluorescence-labeled nuclei dataset, enabling quantitative evaluation of structural preservation in unsupervised virtual staining against ground-truth nuclear distributions. Using this dataset, we present a novel virtual staining framework that translates BIT volumes with shift-variant contrast into realistic H&E volumes by leveraging bidirectional multiscale content consistency and cross-domain style reuse to enhance structural fidelity and perceptual realism. Our method achieves state-of-the-art realism metrics while significantly improving 3D nuclei segmentation accuracy and boundary preservation under zero-shot Cellpose evaluation. Together, these contributions establish a quantitatively validated, structurally faithful, and scalable pipeline for 3D virtual H&E staining, advancing the paradigm of slide-free, volumetric computational histopathology. Our data and code are available at: this https URL.

---


### 100. [ConvNeXt-FD: A Fractal-Based Deep Model for Robust Biomedical Image Segmentation](https://arxiv.org/abs/2605.22002)

**<font color=#1a73e8>作者：</font>** Joao Batista Florindo, Amanda Pontes de Oliveira Ornelas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Biomedical image segmentation is a critical task in medical diagnosis and treatment planning, enabling precise delineation of anatomical structures and pathological regions. Despite significant advancements, challenges persist due to the inherent variability, noise, and complex morphology present in diverse medical imaging modalities. This paper introduces ConvNeXt-FD, a novel deep learning architecture for robust biomedical image segmentation, built upon a U-Net-like encoder-decoder framework leveraging the powerful ConvNeXt backbone. Our approach integrates a hybrid loss function combining the Dice coefficient with a boundary-aware regularization term inspired by a differentiable formulation of Fractal Dimension, designed to enhance the model's sensitivity to object boundaries and shape fidelity. We rigorously evaluate ConvNeXt-FD across six distinct biomedical datasets: BUSI (Breast Ultrasound Images), DDTI (Thyroid Ultrasound Images), FluoCells (Fluorescent Cell Images), IDRiD (Diabetic Retinopathy Images for Optic Disc Segmentation), ISIC2018 (Skin Lesion Images), and MoNuSeg (Nuclei Segmentation). Experimental results demonstrate that ConvNeXt-FD, particularly when initialized with ImageNet pre-trained weights, achieves competitive and often superior performance compared to existing state-of-the-art methods across various metrics, including Dice, Jaccard, Accuracy, Sensitivity, Specificity, and False Positive Rate. The integration of ConvNeXt as a strong encoder, coupled with the boundary-aware regularization, proves effective in capturing both high-level semantic features and fine-grained boundary details, leading to more accurate and reliable segmentations in challenging biomedical contexts.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-347](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
