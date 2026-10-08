# 📦 其他研究 | 2026年10月09日

> 本类共 **324** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-324](./part-07.md)

---

### 51. [MaRK: Markov-adapted Recurrent Kernels for Dynamic Operator Conditioning in State Space Models](https://arxiv.org/abs/2610.09092)

**<font color=#1a73e8>作者：</font>** Syed Ibrahim Omer, Ginny Y. Wong. Xiangyu Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs) offer an efficient alternative to Transformers for sequence modeling, yet conditioning pre-trained SSMs for iterative generation typically operates outside the recurrent operator, through input injection or activation modulation. While such mechanisms expose the model to conditioning information, they leave the underlying temporal dynamics fixed. We introduce MaRK (Markov-adapted Recurrent Kernels), a dynamic operator-conditioning framework that maps context vectors directly into bounded modulations of a frozen SSM's recurrence ($A$), read-in ($B$), read-out ($C$), skip ($D$), and discretization ($\Delta$) parameters. Viewed through the lens of LPV-SSM systems, MaRK induces a context-indexed family of Markov parameter sequences, allowing each diffusion timestep to reshape the model's input-output memory kernel. We instantiate MaRK on a frozen 111M-parameter Hydra SSM backbone and study three adapter geometries: Hypernet, Chebyshev polynomial, and Discrete Cosine Transform kernels. Since these adapters modify the Markov parameter sequence through low-rank auxiliary maps on the frozen backbone, parameter-efficient fine-tuning arises as a structural consequence of the adaptation mechanism itself, requiring only 6.3--11M trainable auxiliary parameters to transition from a bidirectional objective to an iterative diffusion regime. The bounded recurrence parameterization further yields an analytic Affine Quadratic Stability certificate for the modulated recurrence. Through synthetic LPV recovery experiments and Markov-operator diagnostics, we show that MaRK recovers coordinate-invariant temporal operators under matched assumptions and produces distinct, stable timestep-conditioned memory profiles. Empirically, the Chebyshev variant yields the strongest performance, achieving an average validation loss of 2.55, followed by the DCT (2.59) and Hypernet (3.77) geometries.

---


### 52. [Are We Really Benchmarking Forecasting Models? The Impact of Preprocessing on Time Series Performance](https://arxiv.org/abs/2610.09096)

**<font color=#1a73e8>作者：</font>** Guilherme Afonso Galindo Padilha, Paulo Salgado Gomes de Mattos Neto, Rafael Menelau Oliveira e Cruz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While established literature underscores the pivotal role of preprocessing in forecasting accuracy, this stage remains largely overlooked in current research. Modern benchmarks typically resort to simple scaling, failing to account for critical transformations required to address nonstationarity, such as differencing. This omission creates a significant structural preprocessing bias that favors models with built-in data treatments while obscuring the true potential of simpler architectures. We study this effect through a preprocessing-aware benchmark that evaluates 11 forecasting models across 16 reversible preprocessing pipelines on 29,000 M4 time series. Our results identify preprocessing as a key driver of forecasting performance. Optimizing preprocessing per series yields gains of approximately 27\% to 87\% across all evaluated models, with architectures lacking internalized preprocessing experiencing the most substantial improvements. This allows simpler architectures to become highly competitive with complex, state-of-the-art models in modern forecasting benchmarks. All resources and experimental results from this benchmark are stored in a comprehensive metadataset to support future metalearning tasks.

---


### 53. ["Just Like This": Manner Deixis at the Graphics Interface](https://arxiv.org/abs/2610.09099)

**<font color=#1a73e8>作者：</font>** Hamza El Alaoui, Jeffrey P. Bigham, Jun Rekimoto  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People communicate how things should move by combining words with demonstrations: "open it like this." We present an interaction technique that brings this expressive resource to conversational 3D authoring. Building on "Put-That-There," our system combines speech, pointing, and spatiotemporal demonstrations to specify editable behavior. A hand movement supplies evidence for a mechanism's axis, pivot, range, and pace; an animated preview makes the interpretation inspectable. Users refine behavior through further words or demonstrations, and the system can request a demonstration to clarify intent. In a twelve-participant study comparing three input configurations, our system achieved 89% participant-declared completion versus 47% with speech alone, had the highest observed match rates on six categorical accuracy measures and tied on two, and was preferred by nine participants. This work makes demonstration part of an ongoing authoring conversation: behavior can be shown, inspected, and revised.

---


### 54. [Constraint Tree Exploration for Learning from Language Feedback](https://arxiv.org/abs/2610.09107)

**<font color=#1a73e8>作者：</font>** Shaoang Li, Daniel R. Jiang, Jian Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural-language feedback in interactive learning often explains why an action failed by pointing to violated requirements. Misinterpreting this feedback can lead an agent to rule out valid solutions. We study this setting by modeling user intent as latent constraints over an action space and formulating learning from language feedback as pure exploration over feasible regions. We introduce TRACE, an algorithm that organizes candidate constraints in a tree and tests each proposed refinement by generating actions that satisfy it. TRACE commits to the refinement only if the resulting feedback does not contradict it over repeated tests. We distinguish two ways of using the same feedback: (i) falsification, which detects contradictions to the constraint set currently being tested, and (ii) identification, which may additionally name a violated constraint. We prove high-probability coverage bounds with dependence on the candidate class size $H$ for TRACE-Falsification. With reliable identification, TRACE-Identification can replace this dependence by $K/p_{\mathrm{ext}}$, where $K$ is the number of latent constraints and $p_{\mathrm{ext}}$ lower-bounds the probability of extracting a missing true constraint from informative feedback. We evaluate TRACE across six language-feedback tasks. On RecMovie, TRACE-Identification achieves 73% and 86% final-output success under caps of 20 and 60 evaluated outputs, compared with at most 42% and 48% for the evaluated prompting baselines given the same feedback and output caps. Controlled identity-corruption experiments further show greater robustness than direct accumulation when the falsification detector remains reliable.

---


### 55. [Convex-Concave Reinforcement Learning](https://arxiv.org/abs/2610.09108)

**<font color=#1a73e8>作者：</font>** Shripad V. Deshmukh, Yaswanth Chittepu, Dhawal Gupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy learning drives many of the most consequential and heavily-invested applications of reinforcement learning today. Yet the core optimization problem it rests on (maximizing expected return) is notoriously non-convex, even under a direct policy parameterization, and the field has largely responded by avoiding it: optimizing convex surrogate approximations of the return under trust-region constraints (NPG, TRPO, PPO, AWR). We show that this seemingly unstructured problem is not actually structureless. In log-density-ratio coordinates $y := \log[\pi/\pi_n]$, the exact per-iteration objective, computable via per-decision importance sampling (PDIS), is a difference-of-convex-constrained difference-of-convex (DC-constrained DC) program. This structure lets us move beyond surrogate approximations: it recovers CPI, NPG, TRPO, and AWR as special cases along interpretable axes, and it opens a multi-step axis $k$ that couples consecutive decisions. We solve the per-iteration program with sequential convex programming (SCP), the standard solver for difference-of-convex problems, and give convergence guarantees under mild conditions, bridging the difference-of-convex optimization and RL literatures. Empirically, multi-step Convex-Concave RL (CCRL) wins on diagnostic MDPs where credit must propagate across a horizon (its advantage growing with the dependency length), is competitive with a tuned PPO on classic control, and on a realistic, stochastic, mid-horizon healthcare domain converges markedly faster than tuned PPO to the same near-optimal survival, with an 11.3% higher area under the training curve.

---


### 56. [Breaking Adversarial Transferability in Fine-Tuned Speech Recognition](https://arxiv.org/abs/2610.09109)

**<font color=#1a73e8>作者：</font>** Mojtaba Nafez, Aref Mousavi, Mohammad Ebrahim Mahdavi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many organizations fine-tune publicly available pretrained Automatic Speech Recognition (ASR) models and deploy them in black-box settings, assuming limited access provides protection. We show this assumption is fragile: adversarial perturbations crafted on the public base model transfer effectively to fine-tuned target models, severely degrading performance and posing concerns for safety-critical applications. We propose TransferBreaker, a unified fine-tuning framework that suppresses adversarial transfer by integrating Base Adversarial Fine-Tuning, which restricts adversarial training to base-effective perturbations; Latent Jacobian Regularization, which enforces latent-space invariance by suppressing adversarially sensitive directions; and HybridGrad-AFT, which improves robustness against adaptive attacks by interpolating transferable perturbations from base and target gradients. We theoretically justify all components and evaluate TransferBreaker across three languages and four large ASR models, reducing adversarial WER from 92.6 to 27.8. Our code is publicly available at this https URL.

---


### 57. [Same Text, Different Prediction: Serving-Context Nondeterminism in Text Classifiers](https://arxiv.org/abs/2610.09111)

**<font color=#1a73e8>作者：</font>** Santhosh Kumar Kasa, Siva Rajesh Kasa, Sumit Negi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deterministic inference is essential for reliable and trustworthy machine learning. Prior studies of text generation have shown that changing factors such as batch size, batch composition, hardware, or inference engine can alter the generated text, even when the prompt, model parameters, and sampling randomness are fixed. These differences have been attributed in part to floating-point non-associativity, shape-dependent kernel selection, and other implementation-level differences in numerical execution. However, it remains unclear whether, when, and to what extent the same factors affect text classification. We present a systematic study of serving-context non-invariance in text classifiers, which prior work has measured only through generated text. We train 180 models spanning discriminative, pseudo-generative, and fully generative classifier formulations and evaluate each across four categories of serving contexts, holding the checkpoint and the text fixed. Label stability does not imply score stability. Changing only the batch shape changes no labels across fp32 comparisons, yet under bf16 it moves up to 56.7 percentage points of predicted probability mass, with label changes concentrated at small margins. Fully generative classifiers change more labels than their discriminative counterparts under the same serving changes. We derive sufficient conditions for label stability under each serving change and give a separate mitigation for each mechanism. Our results identify and quantify the serving conditions that must be fixed for reproducible text classification.

---


### 58. [TopoCurve: Geometry-Aware Topology Reasoning via Bézier Curves in Autonomous Driving](https://arxiv.org/abs/2610.09118)

**<font color=#1a73e8>作者：</font>** Mihai Bogdan Deaconu, Laura Dioşan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Topology reasoning jointly detects 3D lanes and traffic elements from multi-view images and infers their structural connectivity. Current methods model lanes as discrete polylines, lacking smoothness, analytical tangent directions, and global spatial support for attention, while providing sparse topology supervision. We propose TopoCurve, a geometry-driven architecture for 3D topology reasoning grounded in a structured parametric lane representation. Lanes are modeled as endpoint-fixed cubic Bézier curves, enabling continuous geometry with exact endpoints and analytically defined directionality. We exploit this shared curve geometry across the entire pipeline. Endpoint distance and tangent alignment are encoded with multi-scale Fourier features and injected into the topology head. Sampled curve points serve as geometry-aligned references for deformable cross-attention spanning the full lane. Parallel curve-anchored attention branches provide diverse predictions for one-to-many topology supervision. These components form a tightly coupled cascade where representation enables geometric reasoning, guides feature aggregation, and supports denser supervision. TopoCurve achieves 50.6 OLS on the OpenLane-V2 benchmark without any post-processing, establishing a new state-of-the-art among end-to-end camera-only methods, and outperforms all existing approaches on endpoint detection (56.8 vs. 52.6 on DET_p).

---


### 59. [Which Buildings Are Artificial Intelligence-Ready? A Measurement-Based Assessment Framework for AI Question Answering and Actuation](https://arxiv.org/abs/2610.09119)

**<font color=#1a73e8>作者：</font>** Wooyoung Jung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic artificial intelligence (AI) systems are becoming the interface to buildings, answering questions and controlling operations, but a building's readiness for them has not been systematically assessed. This study proposes a framework to quantify it. First, a building's knowledge graph sets two ceilings. The answerable-readiness ceiling is the share of operational questions its data could answer, and the actuation-readiness ceiling is the share of control actions it exposes. Second, a reference AI agent's accuracy on a fixed set of these questions shows how much of the ceilings is realized. On a simulated office, the agent realizes 0.62 of a 0.64 answerable ceiling, so missing data, not the AI, limit readiness, except in naming a fault's cause. Across 37 public real-building graphs, the median answerable ceiling is 0.16, and in 15 of 45, unlinked sensors lower it. The framework turns "is this building AI-ready?" into an auditable, ranked retrofit question.

---


### 60. [The Deceptive Bandit Problem: Exploratory Coupling and the Fragility of Multi-Agent Learning](https://arxiv.org/abs/2610.09120)

**<font color=#1a73e8>作者：</font>** Michael Tang, Mahmoud Abdelgalil, Jorge I. Poveda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Randomized exploration is central to bandit learning, multi-agent reinforcement learning, and zeroth-order policy search, yet its independence and privacy are usually only treated as technical assumptions. We show that these properties are critical for security purposes and demonstrate how an adversarial agent can exploit privileged information on another agent's exploration. We analyze a deceiver-victim pair in the minimal two-player strongly monotone setting, where a deceptive player obtains leaked signals that are merely correlated with the victim's exploration. We show that, by coupling their own exploratory action with this information, the deceptive player injects an externality that steers the learning dynamics to a new steady state, called the deceptive Nash equilibrium (DNE). We prove that the deceptive bandit learning (DBL) dynamics converge to an arbitrarily small neighborhood of the DNE while retaining optimal convergence rates. Interestingly, our analysis attains these optimal rates while relaxing second-order smoothness conditions from standard bandit optimization literature. We characterize conditions under which deception strictly shifts the steady state and its effect on the deceiver's cost, illustrating the results in a resource-allocation game.

---


### 61. [Are Parameter-Efficient Fine-tuning Methods Really Different?](https://arxiv.org/abs/2610.09122)

**<font color=#1a73e8>作者：</font>** Yikuan Li, Pinyan Lu, Fanghui Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) offers many parameterizations, yet their methodological and functional differences remain unclear. We compare six methods in language and diffusion models to examine how their parameterizations relate to task performance, forgetting, and changes in pretrained weight geometry. Motivated by the spectrum-preserving design of orthogonal fine-tuning (OFT), we first ask whether spectral preservation is itself important for adaptation and retention. We find that the selected LoRA-family methods also approximately preserve pretrained geometry, and that restoring their slightly drifted singular-value spectra largely preserves task performance, questioning the necessity of explicit geometric preservation. Beyond this, we observe that some methods exhibit distinct adaptation--retention trade-offs that vary across settings: LoRA most consistently limits forgetting at competitive performance, DoRA achieves higher mean task scores than LoRA in most comparisons, while PiSSA often incurs greater retention costs. Further intervention experiments suggest that while performance gains from different PEFT methods can be attributed to modifications in different groups of spectral components, we consistently find that restoring dominant rather than intermediate or trailing components produces the largest mean reduction in general-text NLL or base-image drift. Together, these results motivate evaluating geometric constraints through their functional consequences rather than preservation alone. Code is available at this https URL.

---


### 62. [Depth-to-RGB: Repurposing a Frozen Depth Estimator for Geometry-Guided Compositing](https://arxiv.org/abs/2610.09125)

**<font color=#1a73e8>作者：</font>** Sanghyun Jo, Chae Yeon Lim, Donghwan Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-based object compositing inserts or replaces an object using a background image, a reference image, and a 2D compositing mask. These inputs guide appearance and placement but leave the completed scene's geometry implicit, which can distort object structure or alter the surroundings. Our Depth-to-RGB (D2R) framework predicts composite depth for a scene not yet observed in the RGB inputs. It learns reference-conditioned corrections to a frozen depth estimator using encoder features of paired completed scenes as targets. The unchanged decoder maps the corrected representation to the intended scene's depth, which a separately trained renderer holds fixed during RGB synthesis. Under matched architecture and training, encoder-feature supervision reduces OOD Stage-1 AbsRel by 31.4% relative to decoded-depth supervision. We also introduce AnyInsertion++ with paired in-distribution and category-disjoint splits to evaluate generalization beyond compositing training categories. The complete D2R system leads 12 open-source and 3 closed-source baselines in estimator-derived geometry and photometric quality on both paired splits. On category-disjoint data, D2R reduces AbsRel by 43.7% and improves PSNR by 2.4 dB over the matched RGB baseline. Across three unpaired benchmarks, D2R leads both identity metrics and reduces mean CLIP reference cosine distance by 55% relative to the strongest baseline. Project page: this https URL

---


### 63. [Domain-informed Adaptive Sampling for Generalizable PINNs in Metal Additive Manufacturing via Conditional Flow Matching](https://arxiv.org/abs/2610.09126)

**<font color=#1a73e8>作者：</font>** Hyeonsu Lee, Jihoon Jeong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate thermal modeling is essential in metal additive manufacturing (AM) for understanding the process-structure-property chain. Physics-informed neural networks (PINNs) offer effective surrogate thermal modeling by minimizing physics-based residual losses at collocation points. However, prior works typically rely on manually-crafted, static collocation sampling strategies, which are neither principled nor scalable across process conditions, hindering their generalization capability. In this work, we provide theoretical analysis through empirical risk minimization, showing that process condition-aware adaptive sampling is strictly more favorable than conventional static sampling for generalization. Building on this insight, we propose an adaptive sampling strategy within a two-stage framework: (1) a conditional Flow Matching model that learns approximate high-residual distributions across different process conditions, and (2) a mixed sampling strategy combining this distribution with a domain-informed base distribution to generate adaptive collocation points for refining the PINN predictor. Experiments on metal AM numerical benchmarks demonstrate that our method consistently outperforms state-of-the-art PINN baselines, achieving an average 62.1\% reduction in relative $L_2$ error under an identical collocation budget, by capturing process-dependent heat dissipation regions often overlooked in the literature. To the authors' knowledge, this is the first adaptive sampling strategy for PINNs in metal AM, contributing to the enhanced generalization and broader applicability.

---


### 64. [CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use](https://arxiv.org/abs/2610.09127)

**<font color=#1a73e8>作者：</font>** Gennadiy Savrasov, Maksim Elistratov, Nikita Gavrilov 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reconstructing an editable CAD model from a 3D shape remains a challenging engineering task. Existing methods can propose CAD operations, but no single source of proposals works equally well across different part geometries and stages of reconstruction. We introduce CADFather, an autonomous agentic system that coordinates complementary tools to recover parametric CAD programs from 3D meshes. A vision-language assistant inspects renders of the target and intermediate reconstructions, then decides which candidate CAD programs to extend, which tools to invoke, how many proposals to generate, and when to finish. Learned and algorithmic tools propose CAD operations, while numerical optimization refines the parameters of existing programs. Proposed or refined programs are executed and evaluated to provide feedback for subsequent decisions. The agent maintains alternative candidate programs for each target part and preserves the best valid result throughout reconstruction. CADFather uses pretrained generation and assistant models without additional training. We evaluate reconstruction quality and execution validity on the full DeepCAD, Fusion360, and MCB test sets, as well as on CADENA-Bench, CADBench, and BenchCAD. We additionally analyze computational cost and the trade-off between cost and reconstruction quality.

---


### 65. [Directional Evidence Guided Search-Space Reduction for Exact DAG Learning](https://arxiv.org/abs/2610.09136)

**<font color=#1a73e8>作者：</font>** Upala Junaida Islam, Abdelmonem Elrefaey, Rong Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning a directed acyclic graph (DAG) from observational data is a challenging combinatorial problem due to the exponential growth in the number of candidate parent-set configurations. Existing exact score-based methods often require computationally intensive combinatorial search, whereas constraint-based methods can become unreliable or computationally demanding as graph size and conditioning-set complexity increase. We develop a non-parametric hybrid framework, referred to as DECO (Directional Evidence-guided Configuration Optimization), that extracts dependency and directional evidence from observation data to construct admissible parent sets prior to exact optimization. It reduces the optimization search space by eliminating empirically unsupported parent configurations while preserving flexibility for all plausible edge orientations. Theoretical analysis establishes an exponential reduction in the admissible parent-set configuration space and quantifies how bounded edge-level omission affects the probability of retaining the true parent structure. Experiments on benchmark Bayesian networks and synthetic discrete and continuous DAGs demonstrate substantial search-space reduction while achieving competitive structure-recovery performance, with favorable structural Hamming distance across many evaluated settings. These results show that directional evidence can provide an effective preprocessing mechanism for reducing the computational burden of exact DAG learning without requiring a fixed parametric structural~model.

---


### 66. [SwarmReconGuard: Black-Box Detection of Distributed Collective Reconnaissance by Individually Benign-Looking Agent Populations](https://arxiv.org/abs/2610.09138)

**<font color=#1a73e8>作者：</font>** Vahid Tavakkoli, Kabeh Mohsenzadegan, Kyandoghere Kyamakya  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous and agentic clients can distribute reconnaissance across many identities so that each request remains valid, low-rate, and benign-looking while the population collectively acquires broad system knowledge. We formalize this threat as Distributed Collective Reconnaissance (DCR) and present SwarmReconGuard, a reproducible black-box benchmark in which the defender observes only service-boundary telemetry. The Docker-isolated study evaluates 11 benign and attack behaviors across 10-10,000 virtual identities, comprising 440 test runs and 3,666,300 requests, with complete telemetry integrity. We compare semantic, Gaussian, conditional, graph, kernel, hybrid, and CUSUM-based detectors. Gaussian likelihood-ratio detection achieves 100$\%$ detection with 0$\%$ observed false positives on known attacks but only 3$\%$ on unseen policies. CUSUM yields 36.1$\%$ overall detection at 1.25$\%$ false positives, while hybrid CUSUM reaches 85.7$\%$ detection with 0$\%$ observed false positives at 10,000 identities. Results expose a major policy-generalization gap and motivate exposure-aware, scale-aware defenses.

---


### 67. [A Cognitive-Aware QML-CRL Framework for Detecting Affinity and Romance-Investment Fraud](https://arxiv.org/abs/2610.09141)

**<font color=#1a73e8>作者：</font>** Bibhas Adhikari, Ramya Srinivasan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a hybrid quantum-classical framework that detects affinity and romance-investment fraud by modelling the cognitive biases in a manipulative conversation. In our proposed framework, cognitive biases central to this fraud class are carried by dedicated qubits in a structured parameterized quantum circuit, together with a frame qubit makes the encoding sensitive to the temporal order of manipulative reframing, and a narrative qubit that aggregates co-occurrence through a trainable entanglement layer. The circuit parameters are trained jointly with a classical reinforcement-learning agent that decides, turn by turn, whether to flag the conversation, modeled as an optimal stopping problem. We evaluate the model's performance on synthetic conversations that include hard negatives, legitimate but urgent, and legitimate but pushy sales conversations.

---


### 68. [Finding Blind Spots in AppWorld and WorkArena Task Verifiers](https://arxiv.org/abs/2610.09142)

**<font color=#1a73e8>作者：</font>** Richard Abrich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Execution-based task verifiers decide whether an agent succeeded. We audit shipped AppWorld and WorkArena verifiers with source-informed mutation tests. The main audit never modifies a shipped checker.
In AppWorld, duplicating a non-idempotent write creates an extra record while preserving every checked field value. The verifier accepts all three task variants from two of five eligible generators: 6/15 constructed effects. A cardinality patch applied to checker copies after the census makes all six cells fail while preserving valid controls.
In WorkArena, we prospectively rerun 23 extra-field candidates selected for earlier checker-PASS outcomes. Independent Table API readback confirms nondefault persisted values in 21, while all 23 receive PASS. Two requested strings are aliases of stored defaults. The 21 confirmed wrong effects span three form templates. These selected cases confirm wrong effects under the audit's protocol; they do not estimate a population rate.
No other construction produces an independently confirmed false accept. Other checker-PASS cases are effect-correct degeneracies. We report zero-PASS families separately because retained evidence differs. In fixed intent-swap grids, the checkers return no PASS on 2,689 off-diagonal executions. This is a rejection census: 57 WorkArena cells use session-scoped evidence; the other 2,632 lack classified rejection causes and independent target ground truth.
Each increment is specified before its own cells are scored. A supplement accompanies the OpenReview submission with the construction grammar, evidence, content-bound stage lineage and count reproducer.

---


### 69. [RDGSplat: Render-Dedicated Geometry for Novel View Synthesis](https://arxiv.org/abs/2610.09173)

**<font color=#1a73e8>作者：</font>** Zhijie Zheng, Xinhao Xiang, Jiawei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D foundation models enable efficient novel view synthesis by carrying a Gaussian head on the representation they already use for reconstruction. However, the views they render fall short of the geometry they recover, because that geometry is estimated under a metric objective and never scored on how it renders. Recent methods alleviate this by updating the backbone weights, but they thereby discard the metric predictions the model was built for and must be repeated for every new backbone. To this end, we propose RDGSplat, a framework that decodes a second geometry dedicated to rendering from a frozen 3D foundation model, leaving its metric predictions intact. In particular, we devise Render-Dedicated Geometry Decoding, which duplicates the pretrained decoders and optimizes the duplicates under photometric supervision alone. Then, a Target-Pose Conditioned Adapter is introduced to reformulate the representation those decoders read, conditioned on the target camera pose rather than the target image. Extensive experiments show that RDGSplat improves novel view synthesis across three feed-forward backbones on four benchmarks, with every pretrained weight frozen. On RE10K, it raises WM2.0 from 20.918 to 24.266\,dB while training 205.5\,M added parameters against a frozen 1.4\,B backbone, and the depth and pose the same model predicts are unchanged.

---


### 70. [Context-aware Attention-based Gaussian Mixture Models for Vehicular Trajectory Prediction](https://arxiv.org/abs/2610.09174)

**<font color=#1a73e8>作者：</font>** Arash Raftari, Babak Ebrahimi Soorchaei, Yaser P. Fallah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable and interpretable trajectory prediction is critical for cooperative and autonomous driving in complex and uncertain environments. This paper introduces a Context-Aware Attention-based Gaussian Mixture Model (CAA-GMM) for multimodal, uncertainty-aware motion forecasting. The proposed approach models future motion as a probabilistic mixture conditioned on both scene context and agent dynamics, capturing diverse behavioral modes with interpretable Gaussian components. A lightweight attention mechanism adaptively encodes inter-agent interactions and contextual salience, enabling efficient fusion of rasterized environment cues and motion history in dense traffic scenes. Comprehensive evaluations on the nuScenes and Argoverse 2 datasets demonstrate that CAA-GMM achieves competitive or superior accuracy compared with state-of-the-art raster-based baselines, while maintaining low computational complexity. Ablation analyses confirm the importance of the attention module for robust contextual reasoning and predictive precision. Furthermore, evaluations under imperfect communication and perception conditions highlight the framework's resilience to uncertainty, establishing CAA-GMM as an efficient and scalable solution for cooperative trajectory prediction in intelligent transportation systems.

---


### 71. [One Frame, Full Heartbeat: ECG-Free 4D Cardiac Cine MRI Synthesis via Radial-Decomposed Flow Matching](https://arxiv.org/abs/2610.09185)

**<font color=#1a73e8>作者：</font>** Shiyi Wang, Ruochen Sun, Xiang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cine cardiovascular magnetic resonance (CMR) captures the cardiac cycle as a four-dimensional (4D) sequence, but standard acquisition requires electrocardiogram (ECG) gating and repeated breath holds. Visual realism alone does not establish accurate patient-specific ejection fraction (EF) or ventricular volumes. We present PhaseFlow3D, a generative framework that synthesizes a complete 4D cine sequence from a single end-diastolic (ED) three-dimensional (3D) volume without ECG. To capture asymmetric systolic and diastolic dynamics, it represents the cardiac cycle as a piecewise linear phase anchored at ED and end-systolic (ES) time points. At inference, a population-level canonical template supplies this phase without patient-specific temporal information. A phase-conditioned rectified flow model generates a cardiac motion trajectory in latent space. Radial Contraction Decomposition converts each latent state into a 3D displacement field, combining a physics-informed radial component for centripetal myocardial contraction with an image-conditioned residual for rotation and out-of-plane motion. Each frame is generated by directly warping the ED volume, bypassing variational autoencoder decoding. On the combined ACDC and M&Ms benchmark, PhaseFlow3D achieves the lowest EF mean absolute error, the only positive left-ventricular volume-curve $R^2$, and the best distributional quality among compared methods. Ablations confirm each component's contribution. Downstream evaluations demonstrate the utility of the synthesized sequences and displacement fields for segmentation, pathology classification, label propagation, and myocardial strain analysis.

---


### 72. [R-CNN-Based Chess Position Recognition](https://arxiv.org/abs/2610.09191)

**<font color=#1a73e8>作者：</font>** Paras Govind, Ognjen Arandjelović  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Performing chess game position recognition solely from a single image of a three-dimensional board requires predicting the position and orientation of the board relative to the camera, the occupancy of squares and the piece type, which includes its colour. We propose an R-CNN-based framework with independent components for piece recognition and board geometry estimation, whose predictions are combined to reconstruct the position. For piece recognition, we adapt Faster R-CNN using a class-weighted objective and a deeper classification head. The detector operates directly on the input image, retaining alternative piece hypotheses that are subsequently refined using constraints on piece counts and square occupancy. For board detection, we introduce an octagonal arrangement of eight labelled boundary keypoints, predicted using the keypoint head of Mask R-CNN. These provide redundant correspondences for homography estimation and encode board orientation. The estimated homography maps representative points from the piece boxes to an 8x8 grid. On a synthetic dataset, the modifications to piece detection increase mean average precision from 61.59% to 90.14%. Of the predicted board keypoints, 97.11% are within 1% of the image diagonal of their labelled targets. Using ground-truth piece boxes with the predicted homographies gives correct square assignments for every test position. The complete framework recovers 76.61% of test positions exactly and 96.49% with at most one incorrect square.

---


### 73. [Bookkeeping, Composition, or Unreachable Gold? Reading MemoryAgentBench's Conflict-Resolution Scores Against a Frozen Last-Write Resolver](https://arxiv.org/abs/2610.09193)

**<font color=#1a73e8>作者：</font>** Egor Pakhomov, Erik Nijkamp  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> MemoryAgentBench's Conflict Resolution split is read as measuring "selective forgetting". We execute the benchmark's own rule - the newest statement about a fact wins - as a zero-learning resolver frozen on one of the four fact lists. Under the official metric the rule answers 80.25% of the questions (74.5% on the three held-out lists). Of the rest, 67 items have a released gold that the last-write graph cannot reach but overwritten statements would ("The capital of India is New Delhi." superseded by "The capital of India is Grosseto."; gold New Delhi); such items are a third of the multi-hop questions at 262K. Two long-context models and our pre-registered approximate re-implementation of the benchmark's BM25 agent, one retained run per item and outcomes only, score 84.7%, 82.6% and 41.6% on the items the rule solves against 10.4%, 11.9% and 6.0% on those 67. The failures are a reachability split plus a small parser-scope residual; the per-item split, not the aggregate, is the unit at which a score here can be read.

---


### 74. [Patient, Place, Prior (P$^3$): What Counts as Personalization in Medical World Models?](https://arxiv.org/abs/2610.09194)

**<font color=#1a73e8>作者：</font>** Xingrui Gu, Hanxue Gu, Yuxiang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longitudinal models forecast how a patient's imaging state evolves, but accuracy does not show whether the patient's observed trajectory drives the prediction. A population-average forecast may be useful but cannot establish a patient-specific world-model claim. We introduce Patient, Place, Prior (P$^3$), an audit asking whether a forecast benefits from the patient's longitudinal imaging history (Patient), benefits from patient-matched externally supplied spatial support (Place), and gains predictive value beyond a population-average prediction under matched support and context (Prior). We also propose Cancer JEPA, a one-step model that forecasts frozen representations of future breast dynamic contrast-enhanced MRI examinations during neoadjuvant therapy. It adds a lesion-constrained neural correction, trained with an occlusion-based latent objective, to a patient-conditioned low-complexity reduced-rank regression baseline. This factorization permits a post-hoc P$^3$ audit of the frozen model. In a validation cohort previously used in development, forecast error is lower when the neural correction receives the patient's history rather than another patient's and patient-matched lesion occupancy maps rather than substituted maps. However, the descriptive 95% interval comparing the correction computed from patient history with the population-average neural correction includes zero. P$^3$ thus separates input use from evidence of patient-specific predictive value beyond a population-level pattern.

---


### 75. [StableGrasp: Reconstructing Physically Stable Human Hand Grasps from Single Images](https://arxiv.org/abs/2610.09195)

**<font color=#1a73e8>作者：</font>** Han Jiang, Etienne Vouga, Qixing Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing a physically stable human grasp from a single RGB image is challenging because physically modeling grasps is itself difficult, and the problem requires estimating not only a visually constrained hand pose but also a control target that stabilizes the grasp. Existing methods either model only visual hand geometry without considering physics, or rely on less plausible physical modeling, which limits the physical validity of the resulting grasps. In this paper, we present StableGrasp, a differentiable simulation-based optimization framework that explicitly separates the visual hand pose from the control target that determines the grasping forces. Our method jointly optimizes hand geometry and control by minimizing the kinetic energy of the grasp in a differentiable simulator, while regularizing the hand geometry to preserve visual consistency and geometric plausibility. The reconstructed grasps are substantially more stable under rigorous physical simulation, while remaining visually consistent with the input images and geometrically plausible. Experiments show that our approach produces far more stable grasps than alternative hand-control strategies, benefiting visual-only grasp reconstruction pipelines by turning their outputs into physically stable grasps.

---


### 76. [Exact Dynamics and Finite-Sample Trajectory Recovery of Linear Recursive Feature Machines](https://arxiv.org/abs/2610.09196)

**<font color=#1a73e8>作者：</font>** Andrew Cheng, Bobak T. Kiani, Yue M. Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive feature machines (RFMs) learn representations of data by alternating between fitting a predictor to a dataset and updating features of that predictor using the average gradient outer product (AGOP). Connections between AGOPs and feature learning in neural networks motivate linear RFMs as a simple setting for analyzing how representations evolve during training. Here, we study the dynamics and statistics of linear RFM in noisy multi-output regression with isotropic sub-Gaussian input data and targets generated by a low-rank teacher matrix of dimension $d$. We extend the known connection between linear RFM and iteratively reweighted least squares from the interpolating setting to ridge-regularized multi-output regression with noise. We show that the learned feature matrix remains close to its infinite-data ideal counterpart at every iteration. Namely, for $n$ samples, we show the error in the feature matrix decays as $O(\sqrt{d/n})$ with high probability. Experiments on real-world text and single-cell gene-expression data illustrate the features learned by this simple linear model.

---


### 77. [StyleFields: Multi-Scale AdaIN-Modulated Implicit SDFs for Coarse-to-Fine 3D Shape Reconstruction and Editing](https://arxiv.org/abs/2610.09200)

**<font color=#1a73e8>作者：</font>** Ehsan Garaaghaji, Nicolas Talabot, Pascal Fua 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce StyleFields, a DeepSDF-based architecture for high-fidelity 3D reconstruction that enables controllable geometric style mixing: the coarse structure of one object can be combined with the fine-scale details of another. The core idea is depth-aware modulation: instead of a single global code, we inject latents via multi-level Adaptive Instance Normalization at several decoder depths, and supervise matching auxiliary heads with a coarse-to-fine schedule while gradually growing network depth. This aligns early layers with global shape and later layers with high-frequency detail, achieving content-style decoupling without part labels or adversarial training. StyleFields delivers faithful reconstructions, convincing cross-instance hybrids, and consistent gains in ablations over injection depth and supervision granularity. We further demonstrate a practical application in automotive aerodynamics: a learned surrogate drag predictor serves as a differentiable objective to optimize reconstructed cars, allowing targeted edits of global form or surface details by freezing the complementary latent stream. StyleFields offers a simple, effective recipe for controllable implicit reconstruction and downstream performance-driven design.

---


### 78. [An Accuracy--Information Tradeoff for Loss-Difference Conditional Mutual Information](https://arxiv.org/abs/2610.09206)

**<font color=#1a73e8>作者：</font>** Hazar Yueksel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Loss-difference conditional mutual information (ld-CMI) uses the smallest of the standard observations in the supersample hierarchy of generalization bounds: it measures what a learner's loss differences reveal about which candidate of each pair it was trained on. Accuracy is known to force information into the model; data processing does not carry such lower bounds to losses. We show, by bounding three moments of the loss differences, that accuracy also forces ld-CMI. For linear predictors with a smooth convex loss of nonzero slope at zero, such as the logistic loss, plus a regularizer whose curvature and growth are both of power $r\ge2$, on product distributions over a scaled sign cube in dimension at least linear in $n$, every proper learner with expected excess risk at most $\varepsilon$ on these distributions at the optimal sample size $n\asymp\varepsilon^{-2+2/r}$ has worst-case ld-CMI of order $n$ bits, and $\Theta(n/(1+(\tau/\varepsilon)^2))$ bits under Gaussian noise of standard deviation $\tau$ on the loss differences. The same holds without a regularizer, at $n\asymp\varepsilon^{-2}$. Consequently, range-scaled ld-CMI bounds cannot vanish on these distributions, although every proper learner's generalization gap is $O(n^{-1/2})$. We also show that model-level information does not determine noisy loss-difference information, and that the growth, slope and dimension conditions are needed, the last up to a logarithm.

---


### 79. [Consistent Distribution Matching for Data-Free Diffusion Distillation](https://arxiv.org/abs/2610.09221)

**<font color=#1a73e8>作者：</font>** Yuxiang Fu, Qi Yan, Zike Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow and diffusion models suffer from slow inference due to computationally expensive numerical integration. Distillation provides a promising way for a student model to learn from a teacher's dynamics, enabling one-step or few-step generation. However, existing methods often depend on curated distillation datasets, costly teacher rollouts, or auxiliary proxy networks, which complicate model training and scaling. In this work, we propose Consistent Distribution Matching, a simulation-free and data-free distillation method for accelerating diffusion and flow models while preserving strong generative capacity. Our key insight is to unify sample generation and score estimation with one student network. Thus, our framework uses only two models, a frozen teacher and a trainable student, and optimizes one objective. We prove that minimizing our objective indicates Wasserstein convergence of the student flow-map pushforwards to the teacher marginals. On ImageNet 256$\times$256, our method attains an FID of 2.04 with a single function evaluation (1-NFE) and a 4-NFE FID of 1.37 within 40 epochs of training, surpassing the state-of-the-art distillation baselines without data. Our code code and model are available at this https URL.

---


### 80. [PVSync: A Unified Lip-Sync Expert for Timing and Articulation](https://arxiv.org/abs/2610.09223)

**<font color=#1a73e8>作者：</font>** Kevin Stephen, Varun Menon, Timo Mertens 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lip movements can match the timing of speech without matching the spoken sounds. We introduce PVSync, a unified model for audio-visual offset estimation and phoneme-level articulation scoring. PVSync combines window-level contrastive learning for synchronisation with a phoneme-level articulation objective that aligns audio and video embeddings of the same viseme class across clips. Visemes group phonemes with similar visible articulation. Viseme labels are derived automatically from forced-aligned transcripts, without manual annotations. On offset-corrected videos from 13 talking-head video generation models, PVSync matches human rankings of lip-sync quality more closely than LSE-C, achieving a Spearman correlation of 0.83 versus 0.34. On an automatically constructed benchmark from held-out speech, PVSync distinguishes viseme-matched from mismatched audio-visual pairs with an ROC AUC of 0.91. PVSync also outperforms SyncNet and MTD-VocaLiST in temporal offset recovery on held-out in-the-wild clips. Code and benchmark data will be released upon acceptance.

---


### 81. [Symmetry-Informed Causal Partial Identification](https://arxiv.org/abs/2610.09230)

**<font color=#1a73e8>作者：</font>** Uzair Akbar, Zulfiqar Zaidi, Niki Kilbertus 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial identification (PI) entails estimating bounds on causal effects by encoding different assumptions on data generation as a constrained optimization problem. Such bounds can suffice to inform policy decisions even if the causal effect itself is not identifiable. Often vacuous in practice, practitioners seek to exhaustively encode domain knowledge as additional constraints to make the PI bounds more informative. We introduce known data symmetries -- invariance of the causal effect under certain data transformations -- as a new source of constraints to inform PI. We operationalize this as a shape constraint on the causal function, and via a change of measure against which PI is posed using simple data pre-processing. Both approaches are shown to sharpen bounds under two canonical PI models. This is shown both theoretically for the population case, and via experiments in the finite-sample case. More broadly, our framework establishes data symmetries as a natural, underutilized source of background knowledge for robust causal inference.

---


### 82. [Pooling Representation Autoencoders for Efficient Diffusion](https://arxiv.org/abs/2610.09242)

**<font color=#1a73e8>作者：</font>** Ramón Calvo-González, Youssef Saied, François Fleuret  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation Autoencoders (RAEs) generate images from pre-trained visual fea- tures, but their dense token grids make generative modeling expensive. Motivated by local feature correlations, we introduce PoolDINO, a learned affine pooling operator that merges neighboring tokens. Training the pooling operator jointly with the RGB decoder preserves the standard two-stage RAE procedure without a separate feature auto-encoder. On ImageNet-256, 4x token compression retains comparable generation quality under internal guidance, while 16x compression trades some quality for greater efficiency. At a fixed budget of 100 sampling steps, latent-sampling throughput increases by 3.7x and 9.0x, respectively, relative to the unpooled baseline. Classification and dense prediction evaluations show that comparable guided generation quality can coexist with weaker performance on other tasks.

---


### 83. [An Informational Curse of Horizon in Goal-Conditioned Policy Learning](https://arxiv.org/abs/2610.09247)

**<font color=#1a73e8>作者：</font>** John L. Zhou, Yuxuan Dong, Jonathan C. Kao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The difficulty of learning goal-reaching policies is often attributed to a "curse of horizon" that manifests as bias accumulation in temporal-difference backups and noisy advantage estimates. In this work, we identify an additional informational curse of horizon in goal-conditioned policy learning, where increasing the goal relabeling horizon can significantly reduce policy generalization and performance. Through a series of controlled experiments with oracle planners, we decouple the goal horizons sampled during training from those that the policy is asked to reach at test time. Even when evaluated only on a sequence of nearby subgoals, goal-conditioned behavioral cloning (BC) policies suffer from severe, training horizon-dependent performance degradation that is mitigated by reinforcement learning (RL) objectives. We explain this phenomenon as a horizon-dependent decrease in the conditional mutual information between actions and hindsight-relabeled goals, and find empirically that both BC and RL policies trained on longer-horizon goals exhibit a shift in sensitivity from goal to state information, as measured by the policy's input Jacobians. Motivated by this observation, we find that distilling the input Jacobians of short-horizon policies into long-horizon policies yields significant performance gains, especially in combinatorial manipulation tasks. Taken together, our results highlight goal relabeling horizon as an important consideration when learning generalist policies from offline data.

---


### 84. [Efficient Best-of-N policy evaluation for inference-time alignment](https://arxiv.org/abs/2610.09250)

**<font color=#1a73e8>作者：</font>** Jonas Schweisthal, Yuxin Wang, Athiya Deviyani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Best-of-N (BoN) is a common inference-time alignment method that selects the highest-scoring response among N samples from a reference model. Evaluating BoN policies from logged data is challenging under sample-only access because standard off-policy estimators require density ratios that depend on unavailable response likelihoods. In this paper, we propose a sample-only framework for evaluating and selecting BoN policies without access to these likelihoods. We show that the order-statistic structure of BoN allows the required density ratios to be expressed through score-rank probabilities that are estimable from samples alone. We then develop a doubly robust estimator of the BoN policy value (BoN-DR) that efficiently reuses a shared auxiliary sample pool across candidate budgets. We establish valid asymptotic inference even under reward estimator misspecification and prove the efficiency of our BoN-DR estimator. Since larger budgets can amplify errors in the score function and lead to reward overoptimization, we derive two selection rules: (i) maximizing the estimated policy value and (ii) maximizing a lower confidence bound on the improvement over the reference policy, which accounts for estimation uncertainty and provides a no-harm guarantee. Across synthetic experiments and GSM8K with multiple reference and reward models, our framework accurately estimates BoN policy values and selects effective sampling budgets.

---


### 85. [PhyDiCT: Plug-and-Play CT Reconstruction from Sparse X-Rays via Differentiable Rendering and Strong Priors](https://arxiv.org/abs/2610.09253)

**<font color=#1a73e8>作者：</font>** Weicheng Dai, Shantanu Ghosh, Kayhan Batmanghelich  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 3D Computed Tomography (CT) images from a few X-ray projections is a highly ill-posed inverse problem due to the loss of volumetric information. We propose PhyDiCT, a training-free framework that integrates a differentiable Physics-based forward model, grounded in the Beer-Lambert law, with a text-conditioned Diffusion as a strong prior to reconstruct 3D lung CT images. We refer to our approach as training-free since the prior model is used without fine-tuning, and our goal is to steer the denoising procedure to generate samples consistent with X-ray observations. We guide the diffusion generation using Split Gibbs sampling to jointly optimize for projection fidelity (reward) and consistency with prior knowledge. Also, we introduce a test-time refinement step that enhances image realism and anatomical coherence. We extensively evaluate our method on publicly available 3D CT datasets using both perceptual and semantic metrics, demonstrating that it surpasses existing plug-and-play diffusion and fully trained reconstruction approaches. Our findings highlight that combining a strong generative prior with the underlying physics of image formation substantially improves reconstruction quality, e.g., 7.5\% improvement on SSIM compared to full training methods. Code will be released at this https URL.

---


### 86. [The Symbol of the Surrogate: Measuring Numerical Provenance in Neural PDE Solvers](https://arxiv.org/abs/2610.09255)

**<font color=#1a73e8>作者：</font>** Ridham Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural PDE surrogates are trained on numerical solver outputs that contain both physical evolution and solver-specific discretization errors. Because surrogates are also evaluated against held-out trajectories from the same solver, standard benchmarks cannot distinguish fidelity to the exact evolution from imitation of the numerical scheme. We introduce an empirical Fourier-symbol diagnostic that probes a trained surrogate's linearized one-step operator with individual Fourier modes and compares it with both exact-evolution and training-scheme references. To address architectural spectral bias, we train identical networks on schemes with orthogonal dissipative and dispersive signatures and compare their learned operators. In linear advection, the learned surrogates reproduce the training schemes' amplitude and phase errors, with the twin-scheme difference reaching more than 99.8\% of the analytically predicted full-imitation ceiling. The same behavior occurs for a non-local Fourier neural operator and at the operator level for nonlinear Burgers dynamics. These results show that agreement with solver-generated test data does not by itself establish fidelity to the exact evolution. Fourier-symbol measurements provide a direct diagnostic of numerical provenance.

---


### 87. [Hardware-aware Calibrated Clustered Attention for Efficient Visual Geometric Transformers](https://arxiv.org/abs/2610.09274)

**<font color=#1a73e8>作者：</font>** Weitian Wang, Shubham Rai, Cecilia De La Parra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Visual Geometry Grounded Transformer (VGGT) marks a significant leap forward in 3D scene reconstruction, as it is the first model that directly infers all key 3D attributes (camera poses, depths, and dense geometry) jointly in one pass. However, this joint inference mechanism requires global attention layers with extremely long sequences that causes a significant latency bottleneck. In this paper, we propose blockwise clustered attention (BC attention) to accelerate the global attention layers in VGGT. By limiting the clustering within HW-friendly neighborhood blocks, BC attention reduces the computation overhead of query clustering as well as the costly data movement between on- and off-chip memory. This enables BC attention to scale to long sequences and deliver practical latency improvements on GPUs. Moreover, we introduce a hashing hyperplane calibration method and a threshold-based error compensation method to reduce clustering errors efficiently, which is a bottleneck in the current clustered attention mechanism. Overall, our experiments on GPU demonstrate that calibrated BC attention accelerates the global attention layers by 2.10-2.63$\times$ and the whole backbone by 1.77-2.35$\times$ with negligible loss (1%) for large scenes. With a small performance loss (< 5%), calibrated BC attention further achieves a 2.26-2.87$\times$ latency improvement on the global attention layers and a 1.90-2.55$\times$ improvement on the backbone.

---


### 88. [EM-SNN: Efficiently Modulated Spiking Neural Network for Remote Sensing Image Dehazing](https://arxiv.org/abs/2610.09275)

**<font color=#1a73e8>作者：</font>** Jie Shao, Jiaqi Ma, Wenwen Min 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although spiking neural networks (SNNs) provide an energy-efficient alternative to artificial neural networks (ANNs), their application to remote sensing image dehazing remains limited. A key challenge arises from the coupling between haze-induced high-frequency attenuation and discrete spike thresholding. This interaction suppresses weak responses and fundamentally limits the recovery of edges, textures, and fine details in spiking dehazing models. To address this challenge, we propose the Efficiently Modulated Spiking Neural Network (EM-SNN), a dedicated spiking framework tailored to remote sensing image dehazing. EM-SNN integrates a statistics-driven Threshold-Modulated Leaky Integrate-and-Fire (TM-LIF) neuron to adaptively compensate for haze-induced contrast compression, together with a Spike Sobel Modulation (SSM) module that enhances structural cues and reduces depth-wise attenuation during spiking feature propagation. By jointly modulating activation scales and structural representations, EM-SNN improves dehazing performance while preserving the inherent event-driven sparsity of SNNs. Experiments on HRSD, RICE, RRSHID, and SateHaze1K demonstrate that EM-SNN achieves competitive dehazing performance while consuming only one quarter of the energy of the strong ANN baseline SFRDP-Net.

---


### 89. [Twist Flow for Inverse Problems](https://arxiv.org/abs/2610.09281)

**<font color=#1a73e8>作者：</font>** Shiqin Zeng, Zijun Deng, Felix J. Herrmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Bayesian inverse problems, posterior sampling requires generating samples that are consistent with given observations while capturing the range of plausible solutions. Direct conditional generative models introduce latent noise to model this ambiguity, but paired inverse-problem training can still encourage an almost deterministic map from the observation to the target. As a result, generated samples may be observation-consistent while under-representing posterior variability, especially when the posterior is multimodal, leading to undercoverage, mode distortion, or artificial transitions between distinct feasible solutions. We propose joint twist-flow, an augmented flow-matching formulation that learns a continuous transport from the augmented source state $(z_x, y)$ to the augmented terminal state $(x, z_y)$. Here x is the target variable, $y$ is the observation, $z_x$ is the Gaussian reference coordinate for posterior sampling, and $z_y$ is a Gaussian likelihood-side coordinate associated with the observation branch. Under a Gaussian observation model, $z_y$ is motivated by the normalized observation residual associated with observation compatibility. Its role is not to replace uncertainty in $x$, but to couple generated samples of x to observation consistency, helping reduce likelihood-inconsistent variation while preserving variability in weakly constrained directions. We validate the method on low-dimensional inverse problems with reference posterior samples, where joint twist-flow better preserves multimodal posterior support than a direct conditional-flow baseline. We further evaluate the method on image restoration and seismic subsurface velocity-model inversion, showing increased posterior variability while maintaining observation consistency.

---


### 90. [Self-attention summary networks for subsurface velocity-model building from common-image gathers](https://arxiv.org/abs/2610.09282)

**<font color=#1a73e8>作者：</font>** Shiqin Zeng, Yunlin Zeng, Abhinav Prakash Gahlot 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Common-image gathers (CIGs) contain physically meaningful information about velocity-model errors through reflector focusing and residual moveout, but in conventional imaging workflows they are typically used only as diagnostic tools. In this work, we propose a multiscale self-attention summary network that maps high-dimensional 3D CIG volumes into compact conditioning embeddings for probabilistic subsurface velocity inversion. These learned embeddings preserve offset-dependent kinematic structure and spatial coherence while reducing variability caused by background-velocity mismatch. Conditioned on these summary embeddings, a flow-matching model learns a transport from a Gaussian source distribution to the posterior distribution of plausible velocity fields. Numerical experiments show that, compared with direct conditioning on raw CIGs, the proposed summary network improves posterior velocity inference. In particular, the multiscale attention design provides greater robustness to background-model mismatch, yielding more accurate posterior reconstructions and lower predictive uncertainty.

---


### 91. [Beyond Activation: Gaze Invocation with Visible Status for an Embodied AR Assistant in Co-Located Collaboration](https://arxiv.org/abs/2610.09284)

**<font color=#1a73e8>作者：</font>** Chenrui Ma, Yoshio Ishiguro, Qing Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wake words face an inherent trade-off: higher sensitivity reduces missed commands but increases accidental activations. In co-located augmented reality (AR), the system must also determine whether the user is speaking to the assistant or to a nearby person. We introduce a new perspective on this problem: combining gaze-based address with an embodied assistant, visible listening status, and turn management across activation, continued interaction, and release. In our implementation, users look at an assistant anchored in the scene and see activation progress and listening status on its body. Sustained gaze opens a local interaction channel; speech and playback keep it open when attention returns to the task; and inactivity closes it. We evaluated this design with 25 participants. After selecting the assistant's placement and dwell duration, each participant worked with a partner to plan a trip while using the assistant. The study recorded 500 interaction outcomes, including 496 assistant-directed utterance attempts. Gaze acquisition completed before speech for 490 of these attempts (98.8\%): 467 began while the channel remained open, whereas 23 began after it had been released. The other 6 attempts began before acquisition completed. Among 102 reviewed attempts in which gaze left after acquisition but before speech, the configured retention policy kept the channel open for 79 and released it before 23. The results show that an embodied target with visible status can support clear entry into an assistant interaction while revealing a different problem at release: after users look back to their work, they may not see that the assistant has stopped listening. We contribute the implemented gaze-invocation design and design implications for communicating assistant state after visual attention moves elsewhere.

---


### 92. [LeCuration: A Tiny World Model as a Data Curation Multi-Tool](https://arxiv.org/abs/2610.09285)

**<font color=#1a73e8>作者：</font>** Mayank Sengupta, Nirmit Desai, Eric Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many applications of physical AI run within finite or closed physical worlds with a limited set of physical laws governing object behavior. Examples include robots working in a warehouse and agents moving around in a video game. In order to better organize, filter, and curate data for physical AI applications, we propose a new approach centered on the unique settings and physical laws of individual datasets. We train LeCuration, a small world model intended to serve as a data curation tool for a separate, larger downstream model. To build this model, we choose LeWorldModel (LeWM)as our latent encoder and predictor, adding a diffusion transformer (DiT) decoder to add visuals to autoregressive gameplay rollout. We find that the embeddings of this model can be used as an anomaly detection signal and as a content-based clustering heuristic, and that auto-regressively predicting the game state with this model allows us to qualitatively check for action-state consistency. This paper presents a qualitative, proof-of-concept case study on CS:GO gameplay data; we do not yet report quantitative curation metrics or downstream training results, which we identify as the key next step.

---


### 93. [Node-level Graph Neural Architecture Search Framework](https://arxiv.org/abs/2610.09297)

**<font color=#1a73e8>作者：</font>** Lintao Yanga, Sirui Lia, Yaqing Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, Graph Neural Networks (GNNs) and architecture search frameworks have gained extensive application in non-Euclidean data processing, attributable to their superior capacity in managing unstructured data. Nevertheless, traditional approaches typically apply uniform convolution operations to all nodes, regardless of their varying structural and feature characteristics, which can undermine model performance and result in over-smoothing issues as the number of layers increases. To overcome this limitation, in this work, we propose a \textbf{N}ode-Level \textbf{G}raph \textbf{N}eural \textbf{A}rchitecture \textbf{S}earch (N-GNAS) algorithm. It can automatically choose an appropriate network architecture for each subset of nodes when updating node features. N-GNAS also introduces a contrastive learning loss to separate sample features from different categories and vice versa. In experiments conducted on eight datasets for node and graph classification, our methodology outperforms current leading GNAS techniques and traditional human-designed GNNs. For example, it achieves an accuracy rate of 78.26\% on the CiteSeer dataset.

---


### 94. [Kuration SDK: Addressing the Virtual2Real Gap via Data Curation](https://arxiv.org/abs/2610.09305)

**<font color=#1a73e8>作者：</font>** Nirmit Desai, Eric Song, Mayank Sengupta 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmarks for measuring the quality of action-conditioned world models are still evolving and shifting away from visual similarity-based metrics to action-semantic and physically-grounded metrics. However, for domain and task-agnostic action-conditioned world model training, existing benchmarks provide a limited signal. By training and evaluating diffusion world models on CounterStrike gameplay data, we confirm that qualitative playability does not correspond with metrics such as FVD, LPIPS, and JEDi. We term this the Virtual2Real gap. We posit that, in lieu of reliable benchmarks, curating raw gameplay data and measuring a variety of diagnostic properties provides a more robust signal to bridge the gap, before the training even begins. We present several curation strategies and a general-purpose kit for physical AI data curation called Kuration SDK, which is being open-sourced with this paper. The SDK was instrumental in uncovering the root cause of the virtual2real gap in a specific case: why two world models trained on identical gameplay map, action and state distribution, behaved very differently when played in spite of having very similar LPIPS and FVD scores. Thus, Kuration SDK has the potential to uncover the root causes of Virtual2Real gap in specific datasets and accelerate development of sample-efficient training datasets.

---


### 95. [MovieSTAGE: Scene, Transition, and Global Encoding for Movie-fMRI ADHD Classification](https://arxiv.org/abs/2610.09306)

**<font color=#1a73e8>作者：</font>** Boseong Kim, Haejun Chung, Ikbeom Jang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Naturalistic movie-fMRI provides a shared, temporally structured probe of brain dynamics, yet predictive models commonly rely on whole-run functional connectivity (FC) or temporally generic representations that are not aligned with narrative events. We introduce MovieSTAGE (Scene, Transition, and Global Encoding), a multiscale framework that combines hypergraph-structured FC-profile organization within scenes, unsigned FC-profile differences across adjacent scenes, and whole-movie FC. We evaluated 260 participants from the CMI-HBN Despicable Me cohort on case-control, ADHD-subtype, and three-class classification using 10 repetitions of stratified five-fold cross-validation, complete out-of-fold (OOF) predictions, and paired subject-cluster bootstrap and permutation tests. MovieSTAGE achieved AUROCs of 0.69, 0.73, and 0.75 and balanced accuracies of 67.6%, 69.8%, and 58.3%, respectively, yielding the highest mean point estimates among the evaluated methods. On the three-class task, the full model outperformed all two-branch variants, the HGNN scene encoder outperformed MLP, GAT, and BNT alternatives under matched settings, and the human-annotated partition outperformed duration-matched random and fixed-count GSBS controls. These controlled results support incremental predictive value from event-aligned scene and transition representations when combined with whole-movie FC in this cohort. Post-hoc model-derived analyses generated network-level hypotheses involving frontoparietal and default-mode systems.

---


### 96. [VIS-Ground: Video Interactive Storytelling with Contextual Grounding](https://arxiv.org/abs/2610.09326)

**<font color=#1a73e8>作者：</font>** Bingxuan Li, Yiwen Song, Xueqing Wu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video interactive storytelling enables viewers to actively steer how a video unfolds. However, once we allow viewers to intervene during generation, a new challenge arises: The viewer's request can have latent dependencies on both the grounding source and the current rendered video state. These dependencies may not be explicitly stated in any individual input, but emerge only when the source, rendered history, and new viewer intent are considered jointly. Existing interactive video generation systems primarily emphasize following viewer instructions, while source-grounded video generation methods focus on aligning generated content with an external narrative or knowledge source. This leaves a fundamental question underexplored: What context should a generation model ground on during interactive continuation, and how can heterogeneous, unstructured inputs be transformed into such grounding context? In this work, we formulate contextual grounding as the process of transforming heterogeneous input context into an executable constraint model for video generation. To address this challenge, we introduce VIS-Ground, which performs Structured Context Abstraction to recover grounded states and cross-context dependencies, Generation Constraints Induction to project relevant dependencies into candidate-specific constraints, and Constrained Video Generation to enforce these constraints through planning, verification, revision, and rendering. Across three video generation backbones, VIS-Ground consistently achieves the highest overall composite score, reaching an average absolute improvement of 10.3 points over the strongest per-backbone baselines. Detailed analysis further shows gains across both narrative and knowledge grounding, and reveals remaining challenges in dependency extraction, and faithful realization during video rendering.

---


### 97. [GRC-Net: Global Representation Consistency Network for Unsupervised Multimodal Anomaly Detection](https://arxiv.org/abs/2610.09329)

**<font color=#1a73e8>作者：</font>** Seyoung Jeong, Jong Pil Yun, Sang Jun Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated quality inspection is essential for ensuring product reliability in this http URL image-based methods effectively capture appearance-related defects, these methods are limited in detecting structural and geometric anomalies, motivating multimodal approaches incorporating 3D information. However, existing methods mainly rely on local patch-level representations, which often lead to unstable reconstruction errors even in normal regions. To address this limitation, we propose GRC-Net, which integrates a global-attention MLP to enforce global representation consistency across patch embeddings with a stable reconstruction module to improve reconstruction stability. The proposed method captures holistic contextual information through a global token and suppresses reconstruction noise by minimizing discrepancies between original and predicted embeddings. Experiments on MVTec 3D-AD and Eyecandies demonstrate that GRC-Net consistently outperforms existing methods at both image and pixel levels. Qualitative results further demonstrate reduced reconstruction errors in normal regions and more distinct reconstruction differences between normal and anomalous regions.

---


### 98. [CRT-HMAR: Causal Requirement Tracing-Guided Hierarchical Multi-Agent Regulation for Open-Task-Aware Infrared-Visible Image Fusion](https://arxiv.org/abs/2610.09330)

**<font color=#1a73e8>作者：</font>** Zengyi Yang, Shuai Yuan, Zhong-Cheng Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared and visible (IR-VIS) image fusion integrates complementary multimodal information into a single fused image to support downstream vision tasks. However, existing methods are typically tailored to seen tasks within a fixed task set and struggle to generalize to unseen tasks, which restricts their applicability in real-world open-task scenarios. To address this issue, this paper proposes CRT-HMAR, a Causal Requirement Tracing-Guided Hierarchical Multi-Agent Regulation Framework for open-task-aware IR-VIS image fusion. CRT-HMAR introduces a Causal Requirement Tracing Task Localization mechanism, which actively intervenes in key image information and observes task-network response variations to map task-specific semantic preferences into image-level causal requirement maps. Based on these maps, a requirement analysis agent aggregates task-specific requirement knowledge to adaptively guide requirement-customized image fusion. Moreover, CRT-HMAR incorporates History-Analysis Multi-Objective Balancing and Task-Level-Correction Conflict Mitigation mechanisms, jointly constructing a hierarchical regulation chain of "requirement interpretation - task balancing - conflict mitigation". Through multiple collaborative agents, CRT-HMAR dynamically regulates key processes including open-task requirement modeling, multi-task balanced optimization, and gradient conflict mitigation. Extensive experiments on open-task scenarios involving five downstream tasks demonstrate that CRT-HMAR significantly improves generalization to unseen tasks while maintaining the performance and balance of seen tasks. Overall, CRT-HMAR shifts IR-VIS image fusion from task-oriented modeling toward requirement-oriented modeling, promoting its extension from closed-task settings to real-world open-task scenarios.

---


### 99. [SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models](https://arxiv.org/abs/2610.09335)

**<font color=#1a73e8>作者：</font>** Yatai Ji, Zhengqiu Zhu, Yong Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous unmanned aerial vehicle (UAV) object search involves a closed loop of perception, decision-making, and action under partial observability. Urban environments pose several challenges: large search areas and narrow egocentric views limit coverage, dense 3D geometry constrains safe motion, and open-world instructions require identifying a specific target among distractors. Many existing methods mitigate partial observability through explicit maps or memory representations, yet remain largely reactive, reasoning over past observations without explicitly predicting future states. World models enable prospective reasoning through imagined rollouts. However, image-generating world models can incur high inference latency, while spatially grounded planning remains challenging for latent world models. We propose SearchWorld, a recurrent state-space world model that connects explicit spatial memory with value-guided imagination. The model maintains BEV exploration and obstacle memory and decodes a task-aware spatial value layer to guide search. A cognition-action network uses this learned spatial value prior to improve the policy through imagined rollouts, without training a separate scalar critic. Training progresses from world-model learning to expert imitation and imagination-based exploration refinement. On UAV-ON, SearchWorld improves the success rate to 23.8% (19.5% for the strongest published agent) and raises oracle success to 35.5%, while remaining robust on unseen scenes (19.9% success rate). By grounding imagination in explicit spatial representations, SearchWorld enables UAV agents to plan prospectively rather than react.

---


### 100. [Benign Overfitting under Heterogeneous Input Fusion](https://arxiv.org/abs/2610.09340)

**<font color=#1a73e8>作者：</font>** Houzhen Liu, Xiaobo Xia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benign overfitting is extensively studied when learning from a single high-dimensional input, but its behavior under heterogeneous input fusion remains largely unexplored. We study this question for minimum-norm linear interpolation under a heterogeneous Gaussian design, comparing two statistically dependent input blocks with their fusion while holding the underlying population task fixed. For regression, we identify a full-spectrum covariance certificate whose asymptotic status is independent of the cutoff threshold and prove that it is preserved by every positive-semidefinite joint covariance consistent with the two marginals. This protection is sharp, yet it does not extend to all benign regression problems: outside the certified regime, two benign marginals can have a harmful fusion. For one-sparse Gaussian classification, benignity in the regular regime is characterized by the balance between surviving predictive signal and nuisance contamination. Fusion can move these two quantities in opposite directions, and within this model class every marginal-to-joint benign/non-benign pattern is attainable. We further show that the same fused input can have qualitatively different effects on regression and classification. These results establish that benign overfitting under heterogeneous fusion is determined by the joint signal and spectral geometry created by input interaction, rather than by marginal benignity alone.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-324](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
