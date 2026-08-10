# 📦 其他研究 | 2026年08月10日

> 本类共 **190** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-190**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-190**

---

### 151. [SetEasy: A Multi-Modal Classroom Engagement Assessment and Seating Optimization Framework](https://arxiv.org/abs/2608.07188)

**<font color=#1a73e8>作者：</font>** Zhihao Xie, Hongye Yang, Shien Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> SetEasy optimizes classroom engagement in fixed seating grids. It fuses multimodal sensing (wristband physiology, 4K video, environmental data) and trains a v-Gage model grounded in a revised ISEQ. Each week, two-week engagement forecasts are mapped to a student-seat utility matrix, and CP-SAT generates seating plans under visual-access and social-dynamics constraints. In a four-week deployment (23 students, 331 classes), v-Gage converged across affective, behavioral, cognitive, and overall dimensions, cutting RMSE from 0.75 to 0.53. Optimization raised mean engagement from 0.30 to 0.70, with over two-thirds of seats reaching high engagement and back-row low-activity patterns markedly reduced. These results show that, without hardware changes, interpretable, data-driven seating strategies can substantially enhance engagement. The multimodal "assessment + optimization" paradigm offers a transferable, sustainable path to culturally responsive, differentiated spatial design amid global homogenization.

---


### 152. [MAUPITI: On-Device Prototype-Based Learning on a Smart Infrared Sensor](https://arxiv.org/abs/2608.07192)

**<font color=#1a73e8>作者：</font>** Beatrice Alessandra Motetti, Tanguy Dugas du Villard, Matteo Risso 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-resolution infrared (IR) array sensors represent an interesting solution for privacy-preserving human sensing in embedded systems. In this letter, we describe a smart multi-pixel IR sensor integrating a 16$\times$16 thermal MOSFET (TMOS) array and a RISC-V microcontroller extended with low-precision SIMD instructions, capable of on-device learning and continual adaptation for pose and gesture recognition tasks under tight memory and power constraints ($<$32kB on-chip memory, $\approx$1.5mW). To avoid the memory overheads of backpropagation and replay buffers, we adopt a prototype-based Nearest Class Mean (NCM) classifier in which a simple Convolutional Neural Network (CNN) encoder is trained and quantized offline, while class prototypes are stored and updated on the device in streaming mode. With experiments on two datasets, we show that this approach yields accuracy on par with a conventional classifier, with negligible latency overheads in both the classification and the prototype update ($<$0.29% considering both phases), effectively enabling online adaptation of the perception framework.

---


### 153. [Flow-Corrected Shape Optimization: Taming Manifold Drift in High-Dimensional 3D Models](https://arxiv.org/abs/2608.07199)

**<font color=#1a73e8>作者：</font>** Emilien Seiler, Nicolas Talabot, Yingxuan You 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optimizing 3D shapes within the latent spaces of deep generative models is fundamental to computer assisted engineering, yet remains prone to a critical failure mode we term manifold drift: the tendency of gradient-based optimization to move latent vectors away from the manifold of valid shapes. This problem is exacerbated in state-of-the-art 3D shape generative models that operate in increasingly high-dimensional latent spaces where valid shapes occupy a vanishingly small fraction of the full space. Existing mitigation strategies, including latent regularization and flow-matching approaches, either sacrifice expressiveness, demand a difficult trade-off between objective guidance and generative fidelity that remains prone to manifold drift, or are computationally infeasible to scale to modern, large-capacity 3D shape models. We introduce a novel optimizer-corrector framework that alternates between gradient steps for objective minimization and guided flow matching to drive the latent state back to the valid shape manifold. By decoupling objective minimization from flow-based correction, optimizing freely and correcting strictly, this alternating design avoids inherent trade-offs, preserving geometric validity without sacrificing expressiveness while remaining computationally feasible on modern 3D shape models. We demonstrate its effectiveness across generative priors of varying complexity, from simple vector latent spaces to large-scale architectures across a variety of downstream optimization tasks, including aerodynamic drag reduction and object compliance optimization.

---


### 154. [HNR-DAC: Hard-Negative Reranking and Distribution-Aligned Classification for Scientific Claim Verification](https://arxiv.org/abs/2608.07204)

**<font color=#1a73e8>作者：</font>** Zhenchao Wang, Xin Chen, Luoxi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific claim verification over a cited paper requires predicting the claim--paper relation and identifying the paragraphs that justify that prediction. This setting poses two linked challenges: within-paper distractors often resemble genuine evidence, while a classifier trained on gold evidence must operate on retrieved evidence at inference. We present HNR-DAC, a two-stage framework that trains each stage on the cases it will actually encounter. Hard-Negative Reranking (HNR) quantifies evidence confusability using a base reranker's scores on non-gold paragraphs and contrasts gold evidence against the most confusable candidates. Distribution-Aligned Classification (DAC) trains on the Top-1 paragraph produced by the same frozen HNR used to construct inference inputs, while HNR's Top-3 paragraph identifiers provide the evidence output. On the NLPCC 2026 Task 10 Track 2, the final configuration obtains 97.21% Hit@3, 95.79% Macro-F1, 94.47% Joint@3, and an average score of 95.13%. The corresponding submission ranks third on the official Track 2 leaderboard while achieving the highest overall Macro-F1 of 93.05%, alongside 70.16% Joint@3 and an average score of 81.61%.

---


### 155. [From Test-Time Scaling to Reusable Memory: Measuring Crystallization in Text-to-SQL](https://arxiv.org/abs/2608.07213)

**<font color=#1a73e8>作者：</font>** Jiaqian Wang, Yutao Qi, Wenjin Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling can correct difficult text-to-SQL queries, but the extra computation is normally discarded after each answer. Systems increasingly retain verified repair episodes, yet evaluations still report one end-to-end score. It cannot distinguish replay on recurring questions from help on unseen questions, or identify the responsible memory choice. We call measuring this future value the crystallization problem. Our controlled evaluation holds the single-shot solver fixed and varies one memory choice at a time. We separately measure replay, cross-question retention, and held-out same-database transfer. On BIRD, storing verified corrected queries improves held-out first-attempt accuracy by 4.34 percentage points. This gain captures 44.4% of the accuracy headroom provided by on-demand repair on the same questions. Controlled interventions identify database-specific content as the main operating ingredient. Reliable verification and broader retrieval coverage yield supported gains; richer formats and elaborate retrievers do not. Open-source code, evaluation artifacts, and reproduction instructions are available at this https URL.

---


### 156. [Beyond the Black Box: Interpretable Models of Human Randomisation Failures](https://arxiv.org/abs/2608.07220)

**<font color=#1a73e8>作者：</font>** Ngoc Linh Dao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixed strategy equilibrium predicts i.i.d play: past actions should not help predict future decisions. Human players, however, systematically depart from this benchmark, and in O'Neill's zero sum card game, these departures can be predicted by black box sequence models such as LSTMs. This paper asks whether that predictive power can be achieved by transparent alternatives that also reveal the behavioural structure behind it. Using 84,060 decisions from 2,802 pairs, the analysis first benchmarks naive and behavioral models against interpretable machine learning and deep learning models, then evaluates the modified EWA specifications of prior work against these benchmarks and uses the LASSO diagnostics to motivate a further nested frequency tracking extension. The results show that repeat or avoid behavior, especially players' management of their own recent action histories, accounts for most of the interpretable and strategically exploitable signal, while frequency tracking adds little out of sample.

---


### 157. [Learning Suffers More Than the Policy Class Under Partial Observability: A Closed-Form Analysis](https://arxiv.org/abs/2608.07228)

**<font color=#1a73e8>作者：</font>** Idil Gözel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a reinforcement learning agent cannot observe the full state, we usually blame its policies: it cannot see enough to represent a good one. We show that in a solvable case the bigger problem lies elsewhere. Even when a good policy is available and the agent's value function is expressive enough to describe it exactly, learning still ends up somewhere far worse.
We study a partially observed linear-quadratic problem in which a standard actor-critic learner can be solved in closed form. At our default setting the best policy the agent can represent is already close to optimal, costing 10.4% more than the ideal controller that observes everything. Learning does not find it. The algorithm instead comes to rest at a policy that is 35% worse than the best one available to it, and we can say exactly where and why.
The cause is a bias in what the critic learns rather than a limit on what the actor can express. Because the agent cannot attribute what it sees to the part of the state it cannot observe, the critic misreads that unexplained variation as sharp curvature in its own value estimates, and the actor follows that error away from the optimum. We derive closed-form expressions for the resulting policy, for its cost, and for the one design choice that removes the problem, which is how far the learner looks ahead before trusting its own value estimates. Deep reinforcement learning experiments follow these predictions closely. Notably, giving the agent memory of past observations does not help, while changing how far it looks ahead does.

---


### 158. [From probability to causality in probabilistic logic programming](https://arxiv.org/abs/2608.07230)

**<font color=#1a73e8>作者：</font>** Zora Wurm, Kilian Rückschloß, Felix Weitkämper  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Probabilistic logic programming is a formalism of statistical relational artificial intelligence that supports causal queries, including interventions from outside the system. When the structure of a probabilistic logic program is learned from data, however, only probabilistic information is used, and a single probability distribution may be compatible with several causal orders. This leads to ambiguity in interventional reasoning, raising the question of when the causal order is uniquely determined by the distribution. Exploiting the relationship between acyclic probabilistic logic programs and Bayesian networks, we derive conditions under which the probabilistic information encoded in a program determines a unique causal order. We also incorporate constraints arising from relational structure by taking into account prescribed sets of causal symmetries induced by the underlying relational vocabulary. The result is a method for verifying when a learned probabilistic logic program supports well-defined intervention semantics.

---


### 159. [Stoicheia: Character-Level Masked Diffusion for Ancient Greek Textual Restoration, Parsing, and Metrical Scansion](https://arxiv.org/abs/2608.07249)

**<font color=#1a73e8>作者：</font>** Eric Cullhed, Albin Thörn Cleland  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Stoicheia, a 405M-parameter character-level masked-diffusion encoder for Ancient Greek whose input factors into five aligned, independently maskable planes: letters, word and sentence boundaries, diacritics, capitalization, and punctuation. A single backbone can therefore restore lacunae, re-segment, accentuate, and punctuate unspaced text without task-specific retokenization. We pretrain it on an open, revision-pinned corpus of 380M words and release eleven checkpoints: ten rotated, decontaminated folds, guaranteeing that for any given literary passage at least one released model has never seen its text, and one with no exposure to documentary texts. Three experiments - reconstruction of damaged inscriptions and papyri, morphosyntactic tagging and dependency parsing, and macronization with metrical scansion - each carry a matched random-initialization control, isolating what character-level diffusion pretraining contributes: 5.6 CER points on inscription reconstruction, 12.9 LAS on parsing, and 6.0 points of balanced accuracy on macronization. On Ithaca's own test split, with identical frozen samples and strict scoring, Stoicheia reduces character error relative to both prior state-of-the-art systems, from 24.6 (Ithaca) and 23.5 (its 2025 Aeneas-framework successor) to 15.5, and raises top-1 accuracy from 63.0 and 64.0 to 74.5.

---


### 160. [CANIS: Generation-Assisted 3D Canonicalization via an Image-Semantic Bridge](https://arxiv.org/abs/2608.07256)

**<font color=#1a73e8>作者：</font>** Kendong Liu, Yuxin Yao, Junhui Hou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Canonicalizing 3D object orientation is fundamental to 3D understanding and analysis. Existing approaches often rely on geometric cues, although 3D canonicalization ultimately requires a semantically meaningful orientation. To address this gap, we propose CANIS, a category-agnostic, generation-assisted framework that introduces the semantic orientation prior of a frozen image-to-3D generative model into 3D canonicalization, without canonicalization-specific training or category-specific templates. Specifically, CANIS first renders the input object from candidate viewpoints, selects an informative view, and generates a proxy in a canonical orientation. During generation, a sparse structural latent encoded from the input guides the proxy to preserve the geometry of an object. CANIS then uses the selected image as a semantic bridge between the input and the proxy. Image patches identify semantic regions on the proxy, and depth back-projection locates the corresponding regions on the input. The resulting semantic anchors constrain geometric matching, from which we estimate the rigid transformation that canonicalizes the input. Experiments on synthetic benchmarks validate CANIS and its key components, while qualitative results on partial observations and OmniObject3D suggest its applicability to incomplete and real-world scans. CANIS also improves downstream 3D classification, part segmentation, and dense correspondence under arbitrary rotations. Project page: this https URL.

---


### 161. [Incidental Visualizations: Augmented Reality as a Medium for Contextual Information](https://arxiv.org/abs/2608.07271)

**<font color=#1a73e8>作者：</font>** Matilde Heitor, João Moreira, Daniel Gonçalves  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In today's fast-paced world, delivering information efficiently and unobtrusively is essential. While ambient and glanceable visualizations provide real-time data, they can increase cognitive load and disrupt primary tasks. We investigate incidental visualizations, a novel concept in information visualization designed to present contextually relevant information briefly and spontaneously, with minimal user interaction. Augmented Reality offers an ideal medium for this integration, embedding visualizations directly within the user's environment. Through controlled user studies on logic-based game tasks (Sudoku and Connect 4), this work compares ambient, periodic, and incidental visualization patterns in terms of comprehension accuracy, performance, and disruption. Results indicate that IVs deliver information as effectively as ambient displays while minimizing disruption, highlighting their potential for adaptive, context-aware information delivery in AR environments.

---


### 162. [TOFD: Target-Oriented Feature Decoupling against Poisoning Attacks in Split Federated Learning](https://arxiv.org/abs/2608.07274)

**<font color=#1a73e8>作者：</font>** Yuhan Xie, Jingrong Huang, Chen Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split Federated Learning (SFL) facilitates privacy-preserving collaborative training with reduced client-side overhead. However, its split architecture introduces unique attack surfaces, rendering it vulnerable to diverse poisoning attacks. Most existing defenses fail to exploit the split paradigm, limiting their ability to detect and contain malicious behaviors at an early stage. To bridge this gap, we propose Target-Oriented Feature Decoupling (TOFD), a unified framework that jointly enables proactive detection and robust optimization against a wide range of poisoning attacks. TOFD operates in three stages: (1) Target Inference, which identifies potential attack targets by refining class-wise safe zones via class-specific Margin Perturbation (MP); (2) Sample Purification, which adaptively filters poisoned smashed data using thresholds calibrated through cross-class min-max normalization of MP; and (3) Decoupling Optimization, which leverages an adversarial guidance model to capture attack-induced patterns and decouple their influence during optimization, thereby suppressing residual adversarial effects. We provide theoretical guarantees for the convergence of TOFD. Extensive experiments on five datasets demonstrate that TOFD consistently outperforms state-of-the-art defenses under diverse attack scenarios, achieving superior robustness with low computational overhead suitable for practical deployment.

---


### 163. [Why Study Emergent Behavior When You Can Regulate It? Aligning Multi-Agent Systems with Reward Prediction](https://arxiv.org/abs/2608.07280)

**<font color=#1a73e8>作者：</font>** Assaf Caftory, Almog Zemach, Moshe Butman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent simulations are widely used to study complex social and ecological systems, where rich and often unexpected emergent behaviors arise from local interactions. A large body of prior work has focused on analyzing such emergent dynamics across domains. In this paper, we move beyond analyzing emergent behavior and introduce a learning-based mechanism for actively shaping it via social reward modeling. We introduce Multi-Agent Reward Prediction (MARP), a simple framework that extends preference-based reward modeling to multi-agent reinforcement learning. While the framework is designed to be applicable across multi-agent settings, the present empirical validation is limited to a single environment, and we therefore present MARP as a proof of concept within the studied domain. Rather than relying on handcrafted rewards, MARP learns a shared reward model from episode-level evaluations of collective outcomes, enabling decentralized agents to align their behavior with global social objectives.
We study MARP in the Harvest Game, a canonical sequential social dilemma modeling common-pool resource management and related real-world challenges. Our results show that MARP can be tuned to produce behavior that is more closely aligned with target social metrics than standard reward-based baselines, while the learned reward model captures subtle environmental structure without explicit programming. Crucially, MARP supports multiple and composite social objectives within a single training regime. By modifying only the high-level evaluation metric, the same framework seamlessly aligns agent behavior with diverse goals, including sustainability, equality, and peace, as well as combinations of individual and group-level objectives. These findings demonstrate that emergent multi-agent behavior can be treated not only as a phenomenon to study, but as a target of principled, data-driven regulation.

---


### 164. [FUSE: Feature-Wise Unified Specialization with Cross-Column Exchange for Mixed-Type Tabular Flow Matching](https://arxiv.org/abs/2608.07294)

**<font color=#1a73e8>作者：</font>** Suman Cha, Seongchan Lee, Dohyun Ko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating mixed-type tabular data requires jointly modeling diverse feature distributions and their complex cross-column dependencies. Variational flow matching handles distinct endpoints via factorized distributions, yet leaves feature-specific processing and cross-column interactions implicit within a shared backbone. We introduce Feature-wise Unified Specialization with cross-column Exchange (FUSE) to explicitly separate these roles. FUSE applies separate adaptive mixture modules to numerical and categorical features, allowing each feature to combine shared specialized subnetworks, while joint attention preserves information exchange across all columns. We also characterize the excess population risk from restricted conditioning contexts and bound the continuous Wasserstein generation error by endpoint-prediction risk. Comprehensive experiments on eight tabular datasets demonstrate that FUSE achieves strong and consistent performance across distributional fidelity and downstream utility metrics.

---


### 165. [EliSeg: Verified Target Construction for Report-Grounded Abnormality Segmentation](https://arxiv.org/abs/2608.07299)

**<font color=#1a73e8>作者：</font>** Chengyi Peng, Haoyu Yang, Meixing Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology reports describe clinical observations but do not specify executable segmentation targets. They may contain present, negated, prior,uncertain, or irrelevant findings, while multiple valid abnormalities may coexist. Existing segmentation methods largely bypass this ambiguity by receiving a target identity or spatial prompt before inference, which acts as a hidden target oracle. We study report-grounded abnormality segmentation, where a model must determine target eligibility, cardinality, and finding-to-mask correspondence directly from an unfiltered report before delineating the corresponding regions. We propose \textbf{EliSeg}, an atcor--verify--revise framework that integrates target construction with mask generation. A grammar-constrained Actor proposes target slots and masks, an independent text-only Verifier reconstructs the eligible finding inventory, and Revision selectively re-executes the shared Actor when their target structures disagree. EliSeg requires no predefined target identity, finding prompt, point, or bounding box. Experiments on MIMIC-CXR-ILS show that EliSeg consistently outperforms direct segmentation methods and extract-then-segment cascades across findings, while effectively suppressing masks for ineligible report mentions. Ablation studies confirm the complementary roles of verification and revision, and evaluation on CheXlocalize demonstrates effective transfer of the EliSeg to an external this http URL is available at this https URL.

---


### 166. [From Optimal Actions to World Models: Identifiability of Transition Kernels in Discounted MDPs](https://arxiv.org/abs/2608.07301)

**<font color=#1a73e8>作者：</font>** Neal Batra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study what can be recovered about the transition probabilities of a Markov decision process from optimal actions alone. This is closely related to the inverse problem considered by Letcher et al., who ask when the dynamics can be recovered from numerical \(Q\)-values. Here the numerical values themselves are not observed; only the optimal actions are known, for every reward in a given class.
For state-action rewards \(r(s,a)\), knowing the optimal actions for every reward also tells us how much better one action is than another when each is followed by the same fixed policy. This is still not enough to determine the transition probabilities uniquely. We prove that two kernels give the same optimal actions for every reward exactly when \[ Q_{s,a} =
\Bigl(P_{s,a}+\tfrac1\gamma e_s^{\mathsf T}(L-I)\Bigr)L^{-1} \] for one invertible matrix \(L\) satisfying \(L\mathbf 1=\mathbf 1\). Near a kernel with strictly positive entries, there is an \(n(n-1)\)-dimensional family of different kernels with this property. The result is unchanged if we consider only rewards having a unique optimal action at every state.
We then compare this with rewards of the forms \(r(s)\) and \(r(s,a,s')\). Rewards that depend on the next state can usually recover the transition kernel itself: every row at a state with at least two actions is determined, and we describe exactly when a row at a state with one action can remain hidden. State rewards reveal less: two kernels give the same optimal actions exactly when every deterministic policy is optimal for the same set of rewards. The results show how the form of the reward affects what can be learned about the dynamics from optimal actions alone.

---


### 167. [Winning by Peeking: Unenforced Budgets and Test-Set Selection Inflate Short-Budget AutoML Comparisons](https://arxiv.org/abs/2608.07303)

**<font color=#1a73e8>作者：</font>** Guilin Zhang, Kai Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Comparisons between AutoML systems at short time budgets -- tens of seconds rather than hours -- are common in tool READMEs and workshop papers, and they are easy to get wrong. We report a case study in which a simple AutoML engine, Orcetra, appeared to beat FLAML and AutoGluon on 513 OpenML datasets, winning 57.1% of them at a nominal 60-second budget and 78.4% of datasets against FLAML alone at 30 seconds. Both margins came from protocol defects that a results table cannot show. The search loop scored every candidate on the test split and reported the best, making the headline metric a maximum over dozens of noisy estimates while the baselines selected on training data and touched the test set once; and the budget was checked before launching a candidate but never enforced during one, so the system consumed a median of 120 s against a 60-second budget, 2.24x the wall-clock AutoGluon used. Re-running with selection moved to a validation split, the deadline enforced externally and every framework pinned to an equal share of the machine, Orcetra's win rate on the re-run subset falls from 59.4% to 34.3% and no pairwise difference against either competitor remains significant. Recording both estimands inside a single search lets us attribute the collapse: the selection rule accounts for 4.8 percentage points and unequal compute for most of the rest. The same traces give the selection bias as a function of budget, measured rather than assumed: it grows with $K$ but reaches only 0.27 accuracy points, about five times below the $\sigma\sqrt{2\ln K}$ bound a marginal-standard-error argument predicts, because candidates scored on shared test rows cancel most of the noise. We close with a checklist for short-budget comparisons. Code, per-dataset results and the scripts that regenerate every number and figure in the paper are released with it.

---


### 168. [Is SwiGLU's Open Positive Tail Necessary? Evidence from Closed-Tail Gating with MemGLU](https://arxiv.org/abs/2608.07323)

**<font color=#1a73e8>作者：</font>** Yuting Ge, Pengju Yang, Mingkai Nie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We test whether decoder-only language-model FFNs require SwiGLU's open positive tail. We introduce MemGLU as a closed-tail comparator derived from a memristive branch geometry. Across paired 9M and 30M pretraining runs with three seeds, MemGLU remains within about 0.1% of SwiGLU in validation NLL. Trained SwiGLU checkpoints are sensitive to positive-tail suppression, while mechanism diagnostics show that the two models use their gates differently despite similar losses. These results suggest that models adapt to the gate geometry available during pretraining. At the tested scales, SwiGLU's open positive tail is not necessary for decoder-only language-model FFNs.

---


### 169. [When GNNs Fail: Quantifying and Overcoming Temporal Correlation Volatility in Time Series](https://arxiv.org/abs/2608.07333)

**<font color=#1a73e8>作者：</font>** Chen Shao, Yue Wang, Zhenyi Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling multivariate time series by representing them as graphs, where individual series act as nodes and pairwise temporal corre- lations serve as edges, has gained significant traction. Recent advances in Graph Neural Networks (GNNs) have demonstrated strong perfor- mance by assuming a static graph topology and aggregating information from neighboring series. In this work, we investigate the representa- tional power of GNNs for forecasting under both static and dynamic settings (i.e., when pairwise correlations evolve drastically over time) and identify critical limitations in current architectures. To formalize this, we first propose Temporal Correlation Volatility (TCV), a model- agnostic metric designed to quantify the distributional evolution of these latent structures. We establish a clear connection between TCV and performance degradation, demonstrating that many popular models, including Transformers, generalize poorly in high-TCV settings and are often outperformed by simple structure-agnostic baselines. To address these limitations, we propose Graph Layer for Inference in Dynamic En- vironments (GLIDE), a novel GNN layer enhanced by two theoretically grounded design mechanisms: (D1) Path-based Message Passing, which captures path-based neighborhoods and (D2) Static and Dynamic Propagation Separation, which identifies optimal dynamics via local static approximation. These components significantly improve learning under dynamic topology while preserving robustness in static scenarios. Ex- tensive experiments on synthetic and real-world benchmarks show that GLIDE improves average performance by up to 45.6% across static and dynamic settings, with the largest gain reaching 85.7%. The source code is available at this https URL.

---


### 170. [Aftab: A Comprehensive Benchmark of CNN Encoders and Advanced Value Functions in Parallelized Q-Networks](https://arxiv.org/abs/2608.07335)

**<font color=#1a73e8>作者：</font>** Taha Shieenavaz, Shabnam Zareshahraki, Loris Nanni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advancements in deep reinforcement learning have increasingly favored simplified, highly parallelized paradigms. Notably, the Parallelized Q-Network (PQN) algorithm achieves stable off-policy learning without relying on computationally expensive replay buffers or target networks. However, the representational capacity and parameter efficiency of visual encoders operating in these buffer-free settings remain underexplored. In this work, we systematically investigate the architectural design space of Convolutional Neural Networks for PQN. We design and rigorously evaluate eight distinct CNN topologies, optimizing for sample efficiency under strict parameter constraints. Furthermore, we study the impact of representation and value estimation enhancements by integrating the Hadamax encoding paradigm and advanced Q-learning extensions, including distributional, ensemble, and dueling heads. Extensive experiments on the Atari-57 benchmark demonstrate that our proposed composite architecture, Aftab, achieves an Interquartile Mean (IQM) Human-Normalized Score of 6.479, establishing a 0.86 Probability of Improvement over the standard PQN baseline. Additionally, structural resilience evaluations on the highly non-stationary Procgen Hard benchmark confirm out-of-distribution generalization, with Aftab yielding an IQM Procgen Normalized Score of 0.418 compared to the baseline's 0.382. Ultimately, this work establishes an efficient, probabilistically superior structural reference for model-free reinforcement learning, all while preserving the simplicity and memory efficiency of unbuffered, parallelized optimization.
The complete Aftab framework, including all model definitions, training configurations, and raw experimental logs, is open-sourced and available on our GitHub repository: this https URL

---


### 171. [H2AL: Hyperbolic Hierarchy-aware Aggregative Learning for Registration-based Few-shot Medical Image Segmentation](https://arxiv.org/abs/2608.07340)

**<font color=#1a73e8>作者：</font>** Jia Wang, Jiaming Cai, Zunying Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Registration-based Few-shot medical image segmentation (RFMIS) aims to generate pseudo-labels for unlabeled images by warping a labeled image through registration. However, existing methods primarily perform pixel-level optimization and inference in Euclidean space, treating anatomical structures as flat and disjoint. This neglect of inherent hierarchies degrades pseudo-label quality and weakens the discrimination of ambiguous regions, limiting the segmentation performance. To overcome this challenge, we propose a Hyperbolic Hierarchy-aware Aggregative Learning framework for RFMIS, termed H2AL, that enhances both deformation plausibility and anatomical discrimination for dual-task learning. Specifically, we introduce a Hyperbolic Hierarchy-aware Infusion (H2I) module, which leverages the hierarchical modeling capability of hyperbolic space to learn precise hierarchy-aware representations via transformation-guided supervised hyperbolic contrastive learning, and injects such hierarchical priors into Euclidean space through a gated infusion block while preserving semantic richness. Furthermore, we propose an end-to-end joint optimization algorithm by gradient aggregation, where the gradients from the registration and segmentation decoders, embedding semantic and hierarchical cues, are aggregated to update the shared encoder to promote collaborative learning across tasks. Extensive experiments on two anatomical regions, with five experimental settings, demonstrate the effectiveness and efficiency of our method in both registration and segmentation. The code is publicly available at this https URL.

---


### 172. [Zero Gap Is Not Restoration: Stratified Per-Question Probability Evaluation and Step-wise Mitigation of Benchmark Contamination](https://arxiv.org/abs/2608.07341)

**<font color=#1a73e8>作者：</font>** Ruijie Hou, Yueyang Jiao, Zhao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test data from public benchmarks inevitably leaks into pretraining corpora, inflating evaluation scores once memorized. \textbf{Contamination mitigation evaluation} intervenes in the decoding process to suppress memorization and restore a contaminated model's genuine capability, but its prevailing metric, the \textbf{G-AP} (\textbf{G}ap of \textbf{A}ggregate \textbf{P}erformance), is flawed. Discrete correct/incorrect readouts cannot characterize per-question performance, averaging before differencing lets over- and under-suppression cancel out, and uniform per-question weighting invites strategies to push solve probabilities onto the clean model's high-frequency values. We propose \textbf{SA-PPG} (\textbf{S}tratified \textbf{A}ggregate of \textbf{P}er-question \textbf{P}robability \textbf{G}aps): estimate each question's solve probability by sampling, difference it against the clean model per question, and aggregate within groups defined by the clean model's solve probability. Existing mitigation strategies first estimate where contamination lies and then operate on the estimate, so they are only as correct as the estimate. \textbf{RailCap} instead judges contamination during generation: whenever a sample falls back onto the greedy trajectory, the next trajectory token is capped to the runner-up, accumulating suppression until the response distribution becomes sufficiently dispersed. Across multiple contaminated models and benchmarks, SA-PPG reveals that prior strategies' restoration is substantially overestimated, while RailCap attains the lowest SA-PPG.

---


### 173. [Residual Algebra for Representation-Preserving Learning](https://arxiv.org/abs/2608.07349)

**<font color=#1a73e8>作者：</font>** Yao Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning from heterogeneous representations is usually reduced to feature concatenation, which erases which representation produced an error. We instead algebraize the residual: a representation is a typed object that owns both a coordinate system and the residual it leaves unresolved, and learning is an ordered composition of operators that preserve or deliberately erase that type. Fold realizes the objects as point-in-time conditional-mean fields on 10x10 rank grids. FPRC-PQ realizes the algebra as relax-aggregate-close: each field is relaxed by a correction fitted to its own residual in its own coordinates; corrected fields meet at a fixed mean that is the sole identity-erasure boundary; and a shared learner closes only the aggregate's fresh residual. The composition telescopes exactly into representation, local residual estimate, and residual-of-residual estimate. Its aggregate is a learned control-variate interface with population variance reduction, while refitting the closer along perturbations of the backbone yields first-order coupled-path mean orthogonality. As an analytical extension, a reflective rumination operator reads the displacement of a global reconstruction from the aggregate anchor, reflects it, and fixes its gain by a unique orthogonal projection rather than return-tuned grid search. On 3.67M Chinese A-share stock-day observations (2023-2026) under a frozen point-in-time protocol, the evaluated base algebra raises net-of-cost return from 13.52% to 19.10% and Sharpe from 1.42 to 2.09. Matched-capacity, unified-residual, identity-free two-stage, and pairwise-only controls all trail it. The gain is therefore not explained by more features or more trees, but by making residual ownership and composition explicit while representation identity is still available.

---


### 174. [QFCQT: A Chaotically Gated Quantformer Framework for Volatile Time-Series Forecasting](https://arxiv.org/abs/2608.07363)

**<font color=#1a73e8>作者：</font>** Junkai Lin, Siqi Hou, Raymond Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting non-stationary time series remains difficult due to long-range dependencies, local volatility bursts, structural shifts, and nonlinear oscillatory behaviors. Although Transformer-based forecasters are effective for modeling long-term temporal dependencies, their feed-forward blocks typically rely on smooth static activations that are insufficiently sensitive to abrupt regime changes. Motivated by quantitative Transformer designs and oscillator-based nonlinear activations, we propose QFCQT, short for Quantum-Fractal-inspired Chaotically Gated Quantformer, for robust forecasting under complex volatile dynamics. Here, "quantum-fractal-inspired" denotes a computational analogy based on soft oscillator superposition and multi-scale nonlinear responses, rather than a formal quantum-mechanical or fractal-theoretic derivation. QFCQT consists of three main components: (1) a Quantformer-style numerical encoder that directly processes multivariate inputs via linear embedding; (2) a learnable Lee-oscillator activation module that maps scalar pre-activations to dynamic oscillatory responses and summarizes them through Max-over-Time pooling; and (3) a smooth-chaotic gated fusion mechanism that adaptively balances conventional smooth activations and chaos-sensitive responses. Furthermore, instead of using a single fixed oscillator, QFCQT employs a soft superposition of eight parameterized Lee oscillator families to adaptively capture different nonlinear response patterns across regimes. Experiments on ETTh1, ETTh2, and A-share Stock Index benchmarks show that QFCQT consistently outperforms strong baselines, including Informer, LogTrans, LSTMa, HAT, and COTN.

---


### 175. [Curriculum as Code: An AI-Assisted Architecture for Instructional Design in STEM Education](https://arxiv.org/abs/2608.07364)

**<font color=#1a73e8>作者：</font>** Henrique Mohallem Paiva  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contribution: This paper presents a six-phase AI-assisted instructional design architecture based on the Curriculum as Code paradigm, integrating Generative AI with LaTeX and Python to automate the creation of reproducible, visually consistent, and technically precise materials for STEM education. Background: Creating customized instructional materials for active learning imposes a heavy workload on faculty. Standard presentation tools lack robust support for technical content, while current AI applications often hallucinate and fail to formalize the instructional authoring process, limiting their utility for rigorous academic design. Intended Outcomes: The framework aims to reduce preparation time while ensuring mathematical accuracy, adherence to institutional visual identity, and preservation of the instructor's tacit pedagogical knowledge through explicit rules. Application Design: The solution comprises a six-phase pipeline that replaces ad-hoc prompt engineering with a systematic workflow, utilizing text-based interfaces and code-driven generation (LaTeX/Beamer for slides, Python for figures), governed by pedagogical constraints, contextual calibrations, and automated review cycles. Findings: Validated over one year across 8 modules and 28 project contexts in a Project-Based Learning environment, the architecture significantly reduced instructor workload. Generated assets underwent independent peer review and were deployed by six different faculty members, confirming scalability beyond a single author. Based on over 600 voluntary student evaluations, materials achieved high quality ratings from 8.5 to 9.9/10. Results indicate high reproducibility, minimized hallucinations, and sustained pedagogical and visual fidelity, suggesting viability for broad STEM educational applications.

---


### 176. [Beyond Call and Response: Modelling Reciprocal Coordination in Human-AI Vocal Ensembles](https://arxiv.org/abs/2608.07376)

**<font color=#1a73e8>作者：</font>** Polina Proutskova  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Musical interaction with AI is often organised as a response loop: a human performs, the system interprets that action, and the system answers, accompanies, or schedules a musical event. Unconducted vocal ensembles pose a different problem. Singers act simultaneously and continuously affect one another; neither timing nor pitch is fixed by a conductor, metronome, accompaniment, score, or tuning source. Collective organisation emerges from many-to-many reciprocal adjustment. This paper frames such ensembles as coupled dynamic systems and proposes a research architecture for vocal agents that enter, rather than merely track, their collective states. Some target repertoires are metrical, while others exhibit non-isochronous temporal contours that cannot be reduced to a beat grid; we treat the latter as a hard case for a general framework. The architecture connects multichannel capture in the field to dialect- and singing-aware representation, collective-state inference, vocal generation, and in-situ evaluation. The resulting agenda asks not only whether an artificial singer can synchronise, but how its presence reorganises human coordination, leadership, style, and musical transmission.

---


### 177. [SkySeaLand: A Wide-Format Satellite Transportation Benchmark with an Ultra-Lightweight Detection Baseline](https://arxiv.org/abs/2608.07382)

**<font color=#1a73e8>作者：</font>** Md. Zahid Hasan Riad, Md Sultanul Islam Ovi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite object detection is challenged by small targets and wide-format scenes that lose detail under standard square-input resizing. We introduce SkySeaLand, a public dataset of 1,307 high-resolution satellite images and 19,101 verified bounding boxes across airplane, boat, car, and ship classes in terrestrial and maritime scenes. Native COCO and YOLO annotations are provided. The collection is dominated by large source images and wide scene geometry: 84.5 percent exceed 3,836 pixels on the longest side and 73.1 percent are near a 3:1 aspect ratio. We evaluate twelve detectors from the YOLO, RT-DETR, DETR, and Faster R-CNN families using a common split and COCO metrics. The tested YOLO and RT-DETR variants obtain 84.4--88.2 mAP50, with no consistent accuracy gain from larger parameter counts under the reported model-specific recipes. We also report SkyDet, a 1.22 M parameter anchor-free baseline that obtains 60.5 mAP50 and 24.32 mAP50-95 in a 4.90 MB footprint, with 13.74 ms latency (72.8 FPS) on a Tesla T4. SkySeaLand provides a compact benchmark for mixed land--maritime transportation detection, while SkyDet establishes a documented low-footprint reference rather than a state-of-the-art accuracy claim.

---


### 178. [Omni-modal decomposition autoencoders learn full-stack wearable disentangled representations](https://arxiv.org/abs/2608.07385)

**<font color=#1a73e8>作者：</font>** Ioannis Ziogas, Ensieh Khazaei, Bilal Taha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning disentangled representations is a key requirement for developing versatile, general-purpose, and sustainable models in multi-modal wearable computing. However, existing approaches do not operate as full-stack wearable processors, i.e., they do not simultaneously address task-specific classification performance, disentangled and interpretable representation learning, fusion, and generative modeling of highly heterogeneous multi-modal time series. To address this gap, we introduce Omni-modal Variational Decomposition Autoencoders (OmniDecVAEs), a framework that efficiently learns multi-purpose representations in a unified and scalable manner from arbitrarily many modalities. OmniDecVAEs extend DecVAEs by learning modality-conditioned time-frequency latent subspaces through a multi-view self-supervised decomposition loss and a shared asymmetric autoencoder (AE) architecture. Results on a challenging omni-modal human activity recognition (HAR) setting with up to thirty modalities, demonstrate the ability of OmniDecVAEs to learn full-stack wearable representations. When compared to transformer-based and VAE-based methods, OmniDecVAEs full-stack disentangled representation properties lead to accuracy improvements of 1.01% and 6.75% in activity and identity recognition, respectively. Furthermore, OmniDecVAEs synthesize realistic omni-modal time-frequency data that manifest with enhanced reconstructions (mean absolute error improves by 76.84%) and distributional similarity between real and synthetic data (maximum mean discrepancy improves by 13.85%). Our results highlight OmniDecVAEs potential as a lightweight model suitable for intelligent edge wearables and clinical healthcare, unifying processing requirements and abilities in a single model, through its enhanced representational capacity, modality-invariant spatial complexity (4.1M parameters), and real-time latency.

---


### 179. [FedDOSE: Federated Learning Framework Decomposing Site Effects for Modeling Brain Dynamic Functional Connectivity](https://arxiv.org/abs/2608.07393)

**<font color=#1a73e8>作者：</font>** Deepank Girish, Yi Hao Chan, Yubin Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Functional Magnetic Resonance Imaging ( fMRI ) data are often pooled into collaborative multi-site consortia, as deep learning models for analyses require large datasets to generalize well. While Federated Learning (FL) offers a privacy-preserving paradigm for collaborative training, standard approaches continue to struggle with statistical heterogeneity. In particular, site differences pose a key challenge in multi-site data settings. Additionally, existing FL approaches for fMRI rely on static Functional Connectivity ( FC), omitting dynamic information in brain networks. To address this, we propose FedDOSE, a novel framework that explicitly decomposes site differences for analysis of dynamic FC (dFC). FedDOSE introduces a Modularity-Guided Tucker Decomposition block to encode high-dimensional dFC tensors and capture modular-level spatio-temporal patterns efficiently. Class-specific prototypes are generated across all sites and subsequently aligned at the global level by using a combination of Optimal Transport (OT) barycenter formulation and Procrustes analysis. Extensive experiments for diagnosing Autism Spectrum Disorder (ASD) and Attention-Deficit Hyperactivity Disorder (ADHD) on three multi-site resting-state fMRI datasets: ABIDE-I, ABIDE-II, and ADHD-200, demonstrate that FedDOSE outperforms state-of-the-art methods in ASD and ADHD detection. Our results highlight its effectiveness in learning robust representations from multi-site datasets for reliable analysis.

---


### 180. [FinRank: An Evidence-Grounded Benchmark for Financial Question Answering and Retrieval over SEC Filings](https://arxiv.org/abs/2608.07400)

**<font color=#1a73e8>作者：</font>** Sasan Mansouri, Daniel Saad, Mark Wahrenburg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial question answering is typically evaluated by answer correctness, yet in SEC filings a plausible and even numerically correct answer can be grounded in the wrong evidence. Similar facts and disclosures recur across sections of a filing, across reporting periods of the same firm, and across comparable firms. FinRank targets this provenance-sensitive retrieval problem by requiring systems to identify evidence for the intended entity, reporting period, and disclosure context. The benchmark contains 1185 manually authored question-answer records over the 10-K and 10-Q filings of 22 companies. Each record includes a reference answer, gold supporting passages, and hand-curated hard negatives drawn from confusable passages within filings, across reporting periods, and across comparable firms. FinRank evaluates passage retrieval, reranking, and hard-negative discrimination as separately measured tasks. Baseline results demonstrate the difficulty of this setting: among the evaluated systems, even a 7B instruction-tuned embedder reaches only 44.8% Recall@10 on the pooled evidence corpus; sub-billion-parameter encoders gain at most 3.5 points over BM25, a finance-adapted embedder trails BM25 by 9.7 points, and pairwise accuracy falls by 13.0-20.5 percentage points when random negatives are replaced with the curated hard negatives. FinRank provides an evidence-first benchmark for developing financial question answering systems that are not only accurate but also grounded in the correct disclosure.

---


### 181. [GeoDistill-Refine: Silhouette-First Geometry Distillation for Annotation-Free Spacecraft Segmentation](https://arxiv.org/abs/2608.07405)

**<font color=#1a73e8>作者：</font>** Yonglong Zhang, Zongwu Xie, Yang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation segmentation models can provide supervision for spacecraft imagery without manual training masks, but their predictions vary with textual prompts and may contain geometric errors that are amplified during distillation. This paper presents GeoDistill-Refine, a two-stage framework that transfers offline SAM 3 pseudo-masks to a compact segmentation network. Six fixed prompts are fused by an unweighted 50% vote to stabilize the teacher output. The student first learns the foreground silhouette and is then refined with signed-distance-field, skeleton, and area objectives derived from the pseudo-mask. A sample-level gate, computed from prompt agreement, the valid-prompt ratio, and pseudo-mask area plausibility, reduces the influence of unreliable pseudo-geometry. On the SpaceSense-Bench HJM lockbox set, GeoDistill-Refine improves Image IoU and Boundary F1 by 0.0456 and 0.1380, respectively, over a plain pseudo-label student. External evaluations on the SPEED+ Lightbox and Sunlamp domains and on TANGO show competitive regional overlap together with gains in boundary quality or foreground precision. The deployed TinyUNet contains 0.263 M parameters and requires approximately 1.1 ms per image on an RTX 4090; SAM 3 pseudo-mask construction and the auxiliary geometry branches are used only during training.

---


### 182. [Addressable Memory for Video World Models](https://arxiv.org/abs/2608.07408)

**<font color=#1a73e8>作者：</font>** Xindi Wu, Sven Elflein, James Lucas 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study visual persistence in interactive video world models. These models rely on a Key-Value (KV) cache as a growing visual memory to carry forward previously generated frames. However, we find that models can no longer reliably address stored content once rollouts extend beyond the training horizon, because temporal Rotary Positional Embeddings (RoPE) offsets then fall outside the range seen during training and the model struggles to retrieve the relevant visual information through attention. Moreover, naively compressing the cache in the RoPE-rotated space corrupts memory by averaging together incompatible positional phases. To address this, we propose WorldTrace, a training-free memory framework for long-horizon visual persistence. WorldTrace keeps compressed memory addressable by assigning each summary slot a distinct, in-distribution virtual position. Within this addressable cache, we study two memory compression approaches: WorldTrace-Field compresses history for temporal coherence, while WorldTrace-Landmark stores verbatim scene traces at detected transitions for episodic recall. We further introduce LoopBench, a benchmark evaluating whether a compressed cache can reconstruct a previously visited scene after a long detour. WorldTrace-Field improves temporal consistency by +15.5%, and WorldTrace-Landmark improves episodic recall by +19.5% on LoopBench, extending visually persistent generation without retraining.

---


### 183. [UniJEPA: A Unified Joint-Embedding Predictive Architecture for Task-Agnostic Visual World Modeling](https://arxiv.org/abs/2608.07409)

**<font color=#1a73e8>作者：</font>** An Lanji, Dawei Liu, Jin Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) have emerged as a principled framework for self-supervised learning of world models in compact latent spaces, yet existing methods are fragmented: some predict masked parts of a single image in latent space (I-JEPA), others learn to predict global photometric transformations (Image World Models), while video-scale JEPAs predict future temporal states and are post-trained for action-conditioned planning (V-JEPA~2, DINO-World, DINO-WM). These objectives are treated as distinct recipes with separate encoders, predictors, and anti-collapse regularizers, hindering a single model from unifying image-level and video-level world modeling. We present UniJEPA, a unified JEPA that jointly learns photometric prediction (image-level transformations) and temporal prediction (video-level next-state dynamics) in one shared latent space. A single end-to-end objective, composed of a next-embedding prediction loss and a Gaussian regularizer, yields a provably anti-collapse encoder-predictor pair trainable from raw pixels without EMA, stop-gradient, or pre-trained encoders. We show that the same latent space supports controllable abstraction: photometric prediction learns invariant structure while temporal prediction learns equivariant dynamics. After action-conditioned post-training on offline trajectories, UniJEPA enables zero-shot planning by treating goal features as prediction targets. On image, video, and control benchmarks, UniJEPA matches or surpasses task-specific JEPAs while requiring a single loss hyperparameter, and plans up to tens of times faster than generative world models at comparable accuracy.

---


### 184. [Beyond Myopic World Models: Long-Horizon End-to-End Training for Direct Future Prediction](https://arxiv.org/abs/2608.07420)

**<font color=#1a73e8>作者：</font>** Xinyi Li, Zaishuo Xia, Chenjie Hao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models are expected to support imagination over extended temporal horizons, yet most are still trained through local few-step prediction objectives and deployed by recursively rolling out their own predictions. This creates a fundamental mismatch: few-step losses optimize local transition fidelity, while long-horizon prediction depends on how errors and gradients propagate through the entire trajectory. As a result, transitions with different downstream influence on the endpoint are treated uniformly during training, and small local errors are amplified through recursive inference. We argue that long-horizon accuracy is better achieved by optimizing directly, through an end-to-end endpoint prediction objective. To instantiate this paradigm, we introduce the Direct Prediction World Model (DPWM), a non-recursive architecture that compresses an action sequence of arbitrary length into a single embedding and predicts the endpoint observation in a single forward pass. This design avoids recurrent rollout in both prediction and gradient propagation, making long-horizon end-to-end training practical at horizons where unrolled autoregressive training becomes unstable. Empirically, DPWM substantially improves long-horizon endpoint prediction over recursive world-model baselines on continuous-control and pixel-based benchmarks, with larger gains as the prediction horizon increases. We further show that recurrent baselines benefit similarly when retrained with the same long-horizon endpoint objective, supporting our central claim that the training objective, rather than the particular backbone choice, is the main driver of long-horizon prediction accuracy. Our results suggest that world models can benefit from being trained and evaluated at the temporal scales where they are ultimately used, shifting the focus from local transition modeling toward long-horizon predictive accuracy.

---


### 185. [CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing](https://arxiv.org/abs/2608.07424)

**<font color=#1a73e8>作者：</font>** Yan Zhou, Yue Ouyang, Kaiyang Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling is often implemented by spending more compute along one axis: sampling more solutions, extending a chain of thought, or applying a stronger evaluator. Under a fixed inference budget, these choices compete. This paper formulates test-time reasoning as a compute-allocation problem in which a system must decide whether the next unit of compute should be spent on generation, verification, or stopping. We introduce CoBa, a compute-balanced routing policy that first obtains a small set of candidates, applies cheap verification broadly, and routes uncertain or high-value candidates to stronger verification. On 3,129 example-generator evaluations spanning MATH-500, AIME 2024/2025, AMC 2023, and procedural symbolic reasoning, CoBa-Routed-Strong reaches 85.13% macro accuracy, statistically matching a self-evaluation weighted-voting proxy at 85.20% while using 49.1% fewer parameter-weighted tokens. It also matches best-of-16 majority voting within 0.01 macro-accuracy points while using 58.9% fewer parameter-weighted tokens; paired tests retain a small best-of-16 edge at substantially higher cost. Paired bootstrap tests show significant gains over single-sample decoding, while the remaining gap to the pool oracle exposes headroom for sharper routing. For local reasoning systems, test-time scaling becomes a question of where the next computation is most valuable.

---


### 186. [Hands-Off or Hands-On? Variation in Area Chair Practices and Implications for AI Support](https://arxiv.org/abs/2608.07425)

**<font color=#1a73e8>作者：</font>** Ines Arous, Neha Nayak Kennard, Andrei Mircea 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Area chairs (ACs) play a critical role in the peer-review process, managing conflicts and ensuring fair outcomes. Although AI tools have been proposed to support ACs, little is known about the challenges they face and their perceptions of these technologies. In this paper, we conduct interviews including a design probe with 27 ACs in AI to explore their challenges, strategies, and perspectives on potential AI tools. Through thematic analysis, we identify key tensions arising from the growing volume of submissions, uneven reviewer expertise, and the complex task of managing the relationship between reviewers and authors. Most importantly, we find substantial variation in how ACs engage with submissions and influence outcomes: some adopt a largely hands-off approach, while others take a more hands-on role in guiding discussions and decisions. This variation challenges the notion of a single, universal AC practice and highlights the need to account for diverse approaches. When reflecting on the potential use of AI tools, ACs expressed a cautious stance, drawing on their domain knowledge and heightened awareness of AI limitations. From these findings, we derive three design implications: tailoring AI assistance to diverse AC practices, design assistance for discussion moderation, and embedding human-centered AI principles that preserve human agency in decision-making.

---


### 187. [Post-Grokking Collapse at the Representation-Readout Interface in Muon-Trained Transformers](https://arxiv.org/abs/2608.07436)

**<font color=#1a73e8>作者：</font>** Ali Janati, Kaoutar El Maghraoui, Andrei Kanavalau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Under the standard split, Muon gets hidden matrices and AdamW embeddings/output head. Muon groks modular addition faster, but its solutions do not hold. All nine configurations on $(a+b) \bmod 113$ grok and later lose generalization. Across five seeds the selected AdamW reference falls below threshold on four, reaching 27.59%. Instability persists across two moduli, two widths, two training fractions, subtraction, and depth.
The failure arises at the representation-readout interface, identified only jointly up to an invertible map unselected by the loss. After solving the training set, the gradient falls to order $10^{-6}$ and the optimizers respond differently: step-size elasticity is -0.03 for Muon versus +1.5 for AdamW, and the Muon group moves 8.0 times faster per parameter. From bit-identical states, freezing either group prevents failure. Freezing embeddings/readout removes it in five runs over 451,400 post-grokking steps and five paired seeds: unfrozen arms record 137-321 sub-threshold evaluations, frozen arms none. Removing Muon's normalization and orthogonalization is no substitute: it collapses representation from 326 effective conjugate pairs to 4, shows no recurrent collapse, and fails terminally.
Fourier filtering separates circuit failure from masking. Across 43 checkpoints over five seeds and three regimes, the task-aligned family reaches exactly 100% alone. In circuit failure it no longer solves the task; in masking it remains perfect while the full model reaches 45.85%, giving a positive margin on every example, including errors, but being outvoted by a near-equal adversarial remainder. Rescaling it restores 99.9%; grokking is the same condition resolving upward. The task selects the family, swapping $(k,k)$ for $(k,-k)$ under subtraction. Across an abrupt collapse, standard Fourier support is unchanged and the power-distribution cosine remains 0.9899.

---


### 188. [An Analysis of Architectural and Operational Dynamics of Phishkits in the Wild](https://arxiv.org/abs/2608.07451)

**<font color=#1a73e8>作者：</font>** Behzad Ousat, Mohammad Ali Tofighi, Estefan Schafir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing attacks have always been a favored vector for adversaries to defraud users, bypass modern defense mechanisms, and penetrate critical systems. Among all the elements contributing to the creation and deployment of successful phishing attacks, phishkits stand out as a crucial parameter. Phishkits often facilitate creating and deploying compelling phishing pages, implement evasion strategies, and establish and maintain backdoors with remote adversaries for exchanging leaked data. In this work, we performed an analysis of 1,300 modern phishkits collected from 2020 to 2023. We analyzed the architecture, source code, communication channels, and the nature of leaked data shared with adversaries. We identified mechanisms for dynamic redirection and attributing incoming web traffic as part of the evasion and cloaking mechanism. We also observed heavy reliance on current messaging services for exchanging stolen data with phishers. That said, our analysis shows that the number of phishkits with advanced functionalities is quite small. We identified 284 (21.8%) phishkits that did not use any form of evasion mechanism. We also observed that while there were differences in the implementation details of phishkits, the major components that keep phishing pages functional were very similar or even identical across kits. The level of code reuse and heavy reliance on known tricks to build pre-packaged phishing pages make a large number of cases predictable, which can potentially make the detection of these adversarial operations even easier at scale.

---


### 189. [Interaction Creates Dynamical AI Behavior Absent in Isolation](https://arxiv.org/abs/2608.07457)

**<font color=#1a73e8>作者：</font>** Bella Xinrui Li, Frank Yingjie Huo, Neil F Johnson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What will happen when AI agents interact in daily life, e.g. when one AI starts bossing another around? We find a counterintuitive answer that opens new avenues for out-of-equilibrium Physics. When a boss AI directs a stream of messages at the subordinate AI while ignoring its replies, it drives the subordinate into an alien behavioral state that it would never have exhibited alone. Although the two AIs share the same well-defined (decoding) temperature, the subordinate neither copies its boss nor returns to how it behaves on its own; instead, it adopts an entirely different behavior. The boss's added value is similar to a pre-recorded tape. When the boss listens, they both adopt a similar alien dynamical state. A simple kinetic theory captures the principal effects, such as why the way in which the same messages are delivered will matter in future AI-AI interactions.

---


### 190. [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468)

**<font color=#1a73e8>作者：</font>** Zongchuang Zhao, Xin Zhou, Tianyang Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-Action Models (WAMs) improve end-to-end autonomous driving by transferring video dynamics priors to action prediction, but existing methods require costly future generation at inference. We present SimWAM, a simple yet effective WAM that uses video generation purely as a training signal. It co-trains a pretrained video expert and a lightweight action expert with joint flow matching. An isolated attention mask keeps action prediction independent of future frames, allowing the video branch to be discarded after training and leaving a self-contained planner that directly predicts trajectories. Since the two experts share no parameters and interact only through a unified attention interface, the video backbone could be replaced and the action expert scaled independently without modifying the learning objective or inference pipeline. We further apply reinforcement learning to optimize a compositional driving reward beyond trajectory imitation. Our SimWAM achieves $91.5$ PDMS on NAVSIM, surpasses state-of-the-art WAM-based planners with substantially lower latency, and transfers zero-shot to nuScenes. These results position SimWAM as a simple yet solid baseline that could readily benefit from advances in video generation for efficient autonomous driving. The code and model weights are available at this https URL

---


> [!TIP]
> 当前位于：**151-190**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-190**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
