# 🧠 大模型相关研究 | 2026年04月22日

> 本类共 **353** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-353](./part-08.md)

---

### 301. [Beyond Reproduction: A Paired-Task Framework for Assessing LLM Comprehension and Creativity in Literary Translation](https://arxiv.org/abs/2604.18169)

**<font color=#1a73e8>作者：</font>** Ran Zhang, Steffen Eger, Arda Tezcan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for creative tasks such as literary translation. Yet translational creativity remains underexplored and is rarely evaluated at scale, while source-text comprehension is typically studied in isolation, despite the fact that, in professional translation, comprehension and creativity are tightly intertwined. We address these gaps with a paired-task framework applied to literary excerpts from 11 books. Task 1 assesses source-text comprehension, and Task 2 evaluates translational creativity through Units of Creative Potential (UCPs), such as metaphors and wordplay. Using a scalable evaluation setup that combines expert human annotations with UCP-based automatic scoring, we benchmark 23 models and four creativity-oriented prompts. Our findings show that strong comprehension does not translate into human-level creativity: models often produce literal or contextually inappropriate renderings, with particularly large gaps for the more distant English-Chinese language pair. Creativity-oriented prompts yield only modest gains, and only one model, Mistral-Large, comes close to human-level creativity (0.167 vs. 0.246). Across all model-prompt combinations, only three exceed a creativity score of 0.1, while the rest remain at or near zero.

---


### 302. [Copy-as-Decode: Grammar-Constrained Parallel Prefill for LLM Editing](https://arxiv.org/abs/2604.18170)

**<font color=#1a73e8>作者：</font>** Ziyang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs edit text and code by autoregressively regenerating the full output, even when most tokens appear verbatim in the input. We study Copy-as-Decode, a decoding-layer mechanism that recasts edit generation as structured decoding over a two-primitive grammar: <copy lines="i-j"/> references an input line range, <gen>...</gen> emits new content. A token-level FSM guarantees syntactic validity, and a serving-layer primitive updates the KV cache for each copy span via a single parallel-prefill forward rather than $N$ autoregressive steps -- sharing the parallel-forward kernel of speculative decoding but with input tokens as the draft and program-enforced acceptance replacing probabilistic verification. We report an upper-bound analysis that requires no end-to-end training. (i) Kernel speedup: on Qwen2.5-{1.5B, 7B}, copying $N$ tokens via parallel prefill is $6.8\times$--$303\times$ faster than autoregressive ($N \in [8, 512]$, A100 80GB bf16). (ii) Copy ceiling: on ProbeEdit and HumanEvalPack-Fix (Py/JS), $74$--$98\%$ of gold tokens are reachable under the line-level primitive; composed with the empirical kernel over each corpus's span histogram this yields a closed-form wall-clock bound of $29.0\times / 3.4\times / 4.2\times$ ($13.0\times$ pooled). A token-level extension reaches $91$--$99\%$ coverage with $4.5\times$--$6.5\times$ floors. (iii) Pipeline losslessness: oracle programs round-trip through the deterministic resolver on all $482$ cases, localizing any downstream failure to span selection rather than the mechanism. A perturbation study shows pooled EM drops from $100\%$ to $15.48\%$ under off-by-one noise. A fine-tuning pilot on Qwen2.5-Coder-1.5B lifts HEvalFix-Py EM from $0/33$ (untrained) to $12$--$17\%$, a learnability signal, not a production selector. Batched-serving integration and multi-file coverage are scoped as follow-up.

---


### 303. [QuantumQA: Enhancing Scientific Reasoning via Physics-Consistent Dataset and Verification-Aware Reinforcement Learning](https://arxiv.org/abs/2604.18176)

**<font color=#1a73e8>作者：</font>** Songxin Qu, Tai-Ping Sun, Yun-Jie Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show strong capabilities in general reasoning but typically lack reliability in scientific domains like quantum mechanics, which demand strict adherence to physical constraints. This limitation arises from the scarcity of verifiable training resources and the inadequacy of coarse feedback signals in standard alignment paradigms. To address the data challenge, we introduce QuantumQA, a large-scale dataset constructed via a task-adaptive strategy and a hybrid verification protocol that combines deterministic solvers with semantic auditing to guarantee scientific rigor. Building on this foundation, we propose the verification-aware reward model (VRM) tailored for Reinforcement Learning with Verifiable Rewards (RLVR), which employs an adaptive reward fusion (ARF) mechanism to dynamically integrate deterministic signals from a scientific execution suite (SES) with multidimensional semantic evaluations for precise supervision. Experimental results demonstrate that our method consistently outperforms baselines and general-purpose preference models. Notably, our optimized 8B model achieves performance competitive with proprietary models, validating that incorporating verifiable, rule-based feedback into the reinforcement learning loop offers a parameter-efficient alternative to pure scaling.

---


### 304. [STaD: Scaffolded Task Design for Identifying Compositional Skill Gaps in LLMs](https://arxiv.org/abs/2604.18177)

**<font color=#1a73e8>作者：</font>** Sungeun An, Swanand Ravindra Kadhe, Shailja Thakur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmarks are often used as a standard to understand LLM capabilities in different domains. However, aggregate benchmark scores provide limited insight into compositional skill gaps of LLMs and how to improve them. To make these weaknesses visible, we propose Scaffolded Task Design (STaD) framework. STaD generates controlled variations of benchmark tasks based on the concept of scaffolding, which introduces structured, incremental support in a step-by-step manner. Rather than inspecting failures individually, this approach enables systematic and scalable probing of model behavior by identifying the specific reasoning skill compositions they lack. Treating the LLM as a black box, our experiments on six models of varying sizes reveal multiple failure points in three reasoning benchmarks and highlight each model's unique and distinct skill gaps.

---


### 305. [Linear-Time and Constant-Memory Text Embeddings Based on Recurrent Language Models](https://arxiv.org/abs/2604.18199)

**<font color=#1a73e8>作者：</font>** Tobias Grantner, Emanuel Sallinger, Martin Flechl  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based embedding models suffer from quadratic computational and linear memory complexity, limiting their utility for long sequences. We propose recurrent architectures as an efficient alternative, introducing a vertically chunked inference strategy that enables fast embedding generation with memory usage that becomes constant in the input length once it exceeds the vertical chunk size. By fine-tuning Mamba2 models, we demonstrate their viability as general-purpose text embedders, achieving competitive performance across a range of benchmarks while maintaining a substantially smaller memory footprint compared to transformer-based counterparts. We empirically validate the applicability of our inference strategy to Mamba2, RWKV, and xLSTM models, confirming consistent runtime-memory trade-offs across architectures and establishing recurrent models as a compelling alternative to transformers for efficient embedding generation.

---


### 306. [Multiplication in Multimodal LLMs: Computation with Text, Image, and Audio Inputs](https://arxiv.org/abs/2604.18203)

**<font color=#1a73e8>作者：</font>** Samuel G. Balter, Ethan Jerzak, Connor T. Jerzak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal LLMs can accurately perceive numerical content across modalities yet fail to perform exact multi-digit multiplication when the identical underlying arithmetic problem is presented as numerals, number words, images, or in audio form. Because existing benchmarks often lack systematically paired instances across modalities, it remains difficult to compare genuine arithmetic limits within and across model families. We therefore introduce a controlled multimodal multiplication benchmark that factorially varies digit length, digit sparsity, representation (e.g., numerals vs. number words), and modality (text, rendered images, audio), with paired instances from a reproducible generator. We also define arithmetic load, C, as the product of the total and non-zero digit count as a compact, mechanistically motivated proxy for operation count. Across evaluations, accuracy falls sharply as C grows, often nearing zero by C > 100. Indeed, C remains predictive of performance across modalities and models, with R-squared often > 0.5, nearing the value from more complex measures of arithmetic load that count the number of intermediate arithmetic steps. A separate perception-versus-computation decomposition shows that multimodal degradation is primarily computational rather than perceptual: on matched-perception checks, models are near-perfect (> 99%) across modalities, even when multiplication accuracy drops. Beyond measuring when models fail, we ask which procedures they are predisposed to follow. We introduce a forced-completion loss probe that scores heuristic-specific reasoning prefixes--including columnar multiplication, distributive decomposition, and rounding/compensation. Here, decomposition is favored in both text and vision modalities; heuristic-specific LoRA adapters produce near-orthogonal updates yet degrade accuracy, indicating the base model maintains a well-tuned internal router.

---


### 307. [Aether: Network Validation Using Agentic AI and Digital Twin](https://arxiv.org/abs/2604.18233)

**<font color=#1a73e8>作者：</font>** Jordan Auge, Sam Betts, Giovanna Carofiglio 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Network change validation remains a critical yet predominantly manual, time-consuming, and error-prone process in modern network operations. While formal network verification has made substantial progress in proving correctness properties, it is typically applied in offline, pre-deployment settings and faces challenges in accommodating continuous changes and validating live production behavior. Current operational approaches typically involve scattered testing tools, resulting in partial coverage and errors that surface only after deployment. In this paper, we present Aether, a novel approach that integrates Generative Agentic AI with a multi-functional Network Digital Twin to automate and streamline network change validation workflows. It features an agentic architecture with five specialized Network Operations AI agents that collaboratively handle the change validation lifecycle from intent analysis to network verification and testing. Aether agents use a unified Network Digital Twin integrating modeling, simulation, and emulation to maintain a consistent, up-to-date network view for verification and testing. By orchestrating agent collaboration atop this digital twin, Aether enables automated, rapid network change validation while reducing manual effort, minimizing errors, and improving operational agility and cost-effectiveness. We evaluate Aether over synthetic network change scenarios covering main classes of network changes and on past incidents from a major ISP operational network, demonstrating promising results in error detection (100%), diagnostic coverage (92-96%), and speed (6-7 minutes) over traditional methods.

---


### 308. [Towards Disentangled Preference Optimization Dynamics Beyond Likelihood Displacement](https://arxiv.org/abs/2604.18239)

**<font color=#1a73e8>作者：</font>** Wei Chen, Yubing Wu, Junmei Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference optimization is widely used to align large language models (LLMs) with human preferences. However, many margin-based objectives suppress the chosen response along with the rejected one, a phenomenon known as likelihood displacement, and no general mechanism currently prevents this across objectives.
We bridge this gap by presenting a unified \emph{incentive-score decomposition} of preference optimization, revealing that diverse objectives share identical local update directions and differ only in their scalar weighting coefficients.
Building on this decomposition, by analyzing the dynamics of the chosen/rejected likelihoods, we identify the \emph{disentanglement band} (DB), a simple, testable condition that characterizes when training can avoid likelihood displacement by realizing the preferred pathway: suppressing the loser while maintaining the winner, possibly after an initial transient.
Leveraging the DB, we propose a plug-and-play \emph{reward calibration} (RC) that adaptively rebalances chosen versus rejected updates to satisfy the DB and mitigate likelihood displacement, without redesigning the base objective.
Empirical results show that RC steers training toward more disentangled dynamics and often improves downstream performance across a range of objectives. Our code is available at this https URL.

---


### 309. [Correction and Corruption: A Two-Rate View of Error Flow in LLM Protocols](https://arxiv.org/abs/2604.18245)

**<font color=#1a73e8>作者：</font>** Fernando Reitich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as protocols: structured multi-call procedures that spend additional computation to transform a baseline answer into a final one. These protocols are evaluated only by end-to-end accuracy, giving limited insight into when they help, when they hurt, and whether their behavior transfers under distribution shift or composition. We propose a paired-outcome measurement interface for auditing a single protocol step on exact-match tasks. For each instance, the interface records a baseline correctness bit $E_0\in\{0,1\}$ and a post-step correctness bit $E_1\in\{0,1\}$, separating correction ($E_0=0\to E_1=1$) from corruption ($E_0=1\to E_1=0$) through two rates: $c=\Pr(E_1=1\mid E_0=0)$ and $\gamma=\Pr(E_1=0\mid E_0=1)$. These rates predict accuracy changes and define a reusable empirical interface testable across seeds, mixtures, and pipelines. We identify three failure mechanisms. Under mixture shift, pooled estimates of $(c,\gamma)$ become biased when calibration and deployment mixtures differ; conditioning on a difficulty proxy restores stability without additional model calls. Under presentation contamination, selection protocols alter the interface through stable presentation artifacts when candidate content is fixed. Under state insufficiency, the correctness bit may not carry enough history for multi-step pipelines to compose predictably; a Markov factorization test identifies when composition is valid and where additional state is needed. When a protocol step passes these diagnostics, it becomes an auditable module: gated by estimated gain, conditioned on a difficulty proxy to correct mixture bias, and composed into multi-step pipelines with predictable accuracy. We demonstrate these ideas on synthetic mathematical tasks and on GSM8K, where the calibrated interface correctly predicts when protocol steps should be activated or suppressed.

---


### 310. [Medical Image Understanding Improves Survival Prediction via Visual Instruction Tuning](https://arxiv.org/abs/2604.18250)

**<font color=#1a73e8>作者：</font>** Xixi Liu, Jorge Lazo, Andreas Hallqvist 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate prognostication and risk estimation are essential for guiding clinical decision-making and optimizing patient management. While radiologist-assessed features from CT scans provide valuable indicators of disease severity and outcomes, interpreting such images requires expert knowledge, and translating rich visual information into textual summaries inevitably leads to information loss. In this work, we propose a vision-language framework for 3D CT image understanding that leverages large-scale open-sourced CT images paired with radiology reports through visual instruction tuning. This pre-training enables the model to learn clinically meaningful visual-textual representations, which can then be adapted to downstream survival prediction tasks. By incorporating a survival prediction head on top of the pre-trained model, our approach improves survival prediction from CT images and clinical data while generating clinically meaningful language responses to predefined questions. Experimental results demonstrate that our method outperforms baseline methods in survival prediction, particularly, when clinical data alone is less predictive. The code will be released upon acceptance.

---


### 311. [LeGo-Code: Can Modular Curriculum Learning Advance Complex Code Generation? Insights from Text-to-SQL](https://arxiv.org/abs/2604.18254)

**<font color=#1a73e8>作者：</font>** Salmane Chafik, Saad Ezzini, Ismail Berrada  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recently, code-oriented large language models (LLMs) have demonstrated strong capabilities in translating natural language into executable code. Text-to-SQL is a significant application of this ability, enabling non-technical users to interact with relational databases using natural language. However, state-of-the-art models continue to struggle with highly complex logic, particularly deeply nested statements involving multiple joins and conditions, as well as with real-world database schemas that are noisy or poorly structured. In this paper, we investigate whether curriculum learning can improve the performance of code-based LLMs on Text-to-SQL tasks. Employing benchmarks including Spider and BIRD, we fine-tune models under different curriculum strategies. Our experiments show that naive curriculum, simply ordering training samples by complexity in a single epoch, fails to surpass standard fine-tuning due to catastrophic forgetting. To overcome this, we propose a Modular Adapter Composition (MAC) strategy. By sequentially training tier-specific adapters on incremental complexity levels (Easy to Extra-Hard), we create a scaffolded learning environment that improves performance on complex queries. Our approach not only produces measurable performance gains on the Spider and BIRD benchmarks but also provides a flexible, "Lego-like" architecture, allowing models to be composed and deployed based on specific schema difficulty requirements. These findings demonstrate that structured, modular learning is a superior alternative to monolithic fine-tuning for mastering the syntax and logic of complex code generation.

---


### 312. [Geometry-Guided 3D Visual Token Pruning for Video-Language Models](https://arxiv.org/abs/2604.18260)

**<font color=#1a73e8>作者：</font>** Han Li, Zehao Huang, Jiahui Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have demonstrated remarkable capabilities in 2D vision, motivating their extension to 3D scene understanding. Recent studies represent 3D scenes as 3D spatial videos composed of image sequences with depth and camera pose information, enabling pre-trained video-language models to perform 3D reasoning tasks. However, the large number of visual tokens in spatial videos remains a major bottleneck for efficient inference and context management. Existing pruning methods overlook the view consistency of spatial videos and the spatial diversity of the remaining tokens, which prevents them from effectively removing inter-frame redundancy and preserving scene completeness. In this paper, we propose Geo3DPruner, a Geometry-Guided 3D Visual Token Pruning framework. Geo3DPruner first models cross-frame relevance through geometry-aware global attention, and then performs a two-stage pruning process. The intra-voxel stage selects representative multi-view features within each voxel, while the inter-voxel stage preserves spatial diversity by selecting a globally distributed subset of voxels. Extensive experiments on multiple 3D scene understanding benchmarks demonstrate that Geo3DPruner retains over 90% of the original performance while pruning 90% of visual tokens, significantly outperforming existing text-guided and vision-guided pruning methods.

---


### 313. [Universally Empowering Zeroth-Order Optimization via Adaptive Layer-wise Sampling](https://arxiv.org/abs/2604.18264)

**<font color=#1a73e8>作者：</font>** Fei Wang, Li Shen, Liang Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-Order optimization presents a promising memory-efficient paradigm for fine-tuning Large Language Models by relying solely on forward passes. However, its practical adoption is severely constrained by slow wall-clock convergence and high estimation variance. In this work, we dissect the runtime characteristics of ZO algorithms and identify a critical system bottleneck where the generation of perturbations and parameter updates accounts for over 40% of the training latency. We argue that the standard uniform exploration strategy is fundamentally flawed as it fails to account for the heterogeneous sensitivity of layers in deep networks, resulting in computationally wasteful blind searches. To address this structural mismatch, we propose AdaLeZO, an Adaptive Layer-wise ZO optimization framework. By formulating the layer selection process as a non-stationary Multi-Armed Bandit problem, AdaLeZO dynamically allocates the limited perturbation budget to the most sensitive parameters. We further introduce an Inverse Probability Weighting mechanism based on sampling with replacement, which guarantees unbiased gradient estimation while effectively acting as a temporal denoiser to reduce variance. Extensive experiments on LLaMA and OPT models ranging from 6.7B to 30B parameters demonstrate that AdaLeZO achieves 1.7x to 3.0x wall-clock acceleration compared to state-of-the-art methods. Crucially, AdaLeZO functions as a universal plug-and-play module that seamlessly enhances the efficiency of existing ZO optimizers without incurring additional memory overhead.

---


### 314. [An Existence Proof for Neural Language Models That Can Explain Garden-Path Effects via Surprisal](https://arxiv.org/abs/2604.18293)

**<font color=#1a73e8>作者：</font>** Ryo Yoshida, Shinnosuke Isono, Taiga Someya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Surprisal theory hypothesizes that the difficulty of human sentence processing increases linearly with surprisal, the negative log-probability of a word given its context. Computational psycholinguistics has tested this hypothesis using language models (LMs) as proxies for human prediction. While surprisal derived from recent neural LMs generally captures human processing difficulty on naturalistic corpora that predominantly consist of simple sentences, it severely underestimates processing difficulty on sentences that require syntactic disambiguation (garden-path effects). This leads to the claim that the processing difficulty of such sentences cannot be reduced to surprisal, although it remains possible that neural LMs simply differ from humans in next-word prediction. In this paper, we investigate whether it is truly impossible to construct a neural LM that can explain garden-path effects via surprisal. Specifically, instead of evaluating off-the-shelf neural LMs, we fine-tune these LMs on garden-path sentences so as to better align surprisal-based reading-time estimates with actual human reading times. Our results show that fine-tuned LMs do not overfit and successfully capture human reading slowdowns on held-out garden-path items; they even improve predictive power for human reading times on naturalistic corpora and preserve their general LM capabilities. These results provide an existence proof for a neural LM that can explain both garden-path effects and naturalistic reading times via surprisal, but also raise a theoretical question: what kind of evidence can truly falsify surprisal theory?

---


### 315. [Toward Zero-Egress Psychiatric AI: On-Device LLM Deployment for Privacy-Preserving Mental Health Decision Support](https://arxiv.org/abs/2604.18302)

**<font color=#1a73e8>作者：</font>** Eranga Bandara, Asanga Gunaratna, Ross Gore 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Privacy represents one of the most critical yet underaddressed barriers to AI adoption in mental healthcare -- particularly in high-sensitivity operational environments such as military, correctional, and remote healthcare settings, where the risk of patient data exposure can deter help-seeking behavior entirely. Existing AI-enabled psychiatric decision support systems predominantly rely on cloud-based inference pipelines, requiring sensitive patient data to leave the device and traverse external servers, creating unacceptable privacy and security risks in these contexts. In this paper, we propose a zero-egress, on-device AI platform for privacy-preserving psychiatric decision support, deployed as a cross-platform mobile application. The proposed system extends our prior work on fine-tuned LLM consortiums for psychiatric diagnosis standardization by fundamentally re-architecting the inference pipeline for fully local execution -- ensuring that no patient data is transmitted to, processed by, or stored on any external server at any stage. The platform integrates a consortium of three lightweight, fine-tuned, and quantized open-source LLMs -- Gemma, Phi-3.5-mini, and Qwen2 -- selected for their compact architectures and proven efficiency on resource-constrained mobile hardware. An on-device orchestration layer coordinates ensemble inference and consensus-based diagnostic reasoning, producing DSM-5-aligned assessments for conditions. The platform is designed to assist clinicians with differential diagnosis and evidence-linked symptom mapping, as well as to support patient-facing self-screening with appropriate clinical safeguards. Initial evaluation demonstrates that the proposed zero-egress deployment achieves diagnostic accuracy comparable to its server-side predecessor while sustaining real-time inference latency on commodity mobile hardware.

---


### 316. [CAARL: In-Context Learning for Interpretable Co-Evolving Time Series Forecasting](https://arxiv.org/abs/2604.18305)

**<font color=#1a73e8>作者：</font>** Etienne Tajeuna, Patrick Asante Owusu, Armelle Brun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper we investigate forecasting coevolving time series that feature intricate dependencies and nonstationary dynamics by using an LLM Large Language Models approach We propose a novel modeling approach named ContextAware ARLLM CAARL that provides an interpretable framework to decode the contextual dynamics influencing changes in coevolving series CAARL decomposes time series into autoregressive segments constructs a temporal dependency graph and serializes this graph into a narrative to allow processing by LLM This design yields a chainofthoughtlike reasoning path where intermediate steps capture contextual dynamics and guide forecasts in a transparent manner By linking prediction to explicit reasoning traces CAARL enhances interpretability while maintaining accuracy Experiments on realworld datasets validate its effectiveness positioning CAARL as a competitive and interpretable alternative to stateoftheart forecasting methods

---


### 317. [Reasoning Models Know What's Important, and Encode It in Their Activations](https://arxiv.org/abs/2604.18307)

**<font color=#1a73e8>作者：</font>** Yaniv Nikankin, Martin Tutek, Tomer Ashuach 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models often solve complex tasks by generating long reasoning chains, consisting of many steps with varying importance. While some steps are crucial for generating the final answer, others are removable. Determining which steps matter most, and why, remains an open question central to understanding how models process reasoning. We investigate if this question is best approached through model internals or through tokens of the reasoning chain itself. We find that model activations contain more information than tokens for identifying important reasoning steps. Crucially, by training probes on model activations to predict importance, we show that models encode an internal representation of step importance, even prior to the generation of subsequent steps. This internal representation of importance generalizes across models, is distributed across layers, and does not correlate with surface-level features, such as a step's relative position or its length. Our findings suggest that analyzing activations can reveal aspects of reasoning that surface-level approaches fundamentally miss, indicating that reasoning analyses should look into model internals.

---


### 318. [EVE: Verifiable Self-Evolution of MLLMs via Executable Visual Transformations](https://arxiv.org/abs/2604.18320)

**<font color=#1a73e8>作者：</font>** Yongrui Heng, Chaoya Jiang, Han Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-evolution of multimodal large language models (MLLMs) remains a critical challenge: pseudo-label-based methods suffer from progressive quality degradation as model predictions drift, while template-based methods are confined to a static set of transformations that cannot adapt in difficulty or diversity. We contend that robust, continuous self-improvement requires not only deterministic external feedback independent of the model's internal certainty, but also a mechanism to perpetually diversify the training distribution. To this end, we introduce EVE (Executable Visual transformation-based self-Evolution), a novel framework that entirely bypasses pseudo-labels by harnessing executable visual transformations continuously enriched in both variety and complexity. EVE adopts a Challenger-Solver dual-policy architecture. The Challenger maintains and progressively expands a queue of visual transformation code examples, from which it synthesizes novel Python scripts to perform dynamic visual transformations. Executing these scripts yields VQA problems with absolute, execution-verified ground-truth answers, eliminating any reliance on model-generated supervision. A multi-dimensional reward system integrating semantic diversity and dynamic difficulty calibration steers the Challenger to enrich its code example queue while posing progressively more challenging tasks, preventing mode collapse and fostering reciprocal co-evolution between the two policies. Extensive experiments demonstrate that EVE consistently surpasses existing self-evolution methods, establishing a robust and scalable paradigm for verifiable MLLM self-evolution. The code is available at this https URL .

---


### 319. [PARM: Pipeline-Adapted Reward Model](https://arxiv.org/abs/2604.18327)

**<font color=#1a73e8>作者：</font>** Xingyu Fan, Wei Shao, Jiacheng Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward models (RMs) are central to aligning large language models (LLMs) with human preferences, powering RLHF and advanced decoding strategies. While most prior work focuses on single-step generation, real-world applications increasingly adopt multi-stage LLM pipelines, where effective reward guidance remains underexplored. We investigate this through code generation for combinatorial optimization, constructing a pipeline that integrates reward models into both formulation and solution stages. We identify a critical challenge: inconsistency between reward model predictions and actual pipeline execution outcomes. To address this, we propose the Pipeline-Adapted Reward Model (PARM), which leverages pipeline-specific data and direct preference optimization to align rewards with downstream feedback. We instantiate PARM as a two-stage pipeline (formulation -> code generation) and evaluate it on four public optimization benchmarks, measuring execution rate and solving accuracy against baselines and sampling methods. A supplementary cross-domain experiment on GSM8K assesses transferability. Results demonstrate that PARM consistently improves pipeline output quality and stability, providing new insights into reward modeling for multi-stage LLM reasoning.

---


### 320. [Multilingual Training and Evaluation Resources for Vision-Language Models](https://arxiv.org/abs/2604.18347)

**<font color=#1a73e8>作者：</font>** Daniela Baiamonte, Elena Fano, Matteo Gabburo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) achieved rapid progress in the recent years. However, despite their growth, VLMs development is heavily grounded on English, leading to two main limitations: (i) the lack of multilingual and multimodal datasets for training, and (ii) the scarcity of comprehensive evaluation benchmarks across languages. In this work, we address these gaps by introducing a new comprehensive suite of resources for VLMs training and evaluation spanning five European languages (English, French, German, Italian, and Spanish). We adopt a regeneration-translation paradigm that produces high-quality cross-lingual resources by combining curated synthetic generation and manual annotation. Specifically, we build Multi-PixMo, a training corpus obtained regenerating examples from Pixmo pre-existing datasets with permissively licensed models: PixMo-Cap, PixMo-AskModelAnything, and CoSyn-400k. On the evaluation side, we construct a set of multilingual benchmarks derived translating widely used English datasets (MMbench, ScienceQA, MME, POPE, AI2D). We assess the quality of these resources through qualitative and quantitative human analyses, measuring inter-annotator agreement. Additionally, we perform ablation studies to demonstrate the impact of multilingual data, with respect to English only, in VLMs training. Experiments, comprising 3 different models show that using multilingual, multimodal examples for training VLMs aids is consistently beneficial on non-English benchmarks, with positive transfer to English as well.

---


### 321. [HiGMem: A Hierarchical and LLM-Guided Memory System for Long-Term Conversational Agents](https://arxiv.org/abs/2604.18349)

**<font color=#1a73e8>作者：</font>** Shuqi Cao, Jingyi He, Fei Tan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term conversational large language model (LLM) agents require memory systems that can recover relevant evidence from historical interactions without overwhelming the answer stage with irrelevant context. However, existing memory systems, including hierarchical ones, still often rely solely on vector similarity for retrieval. It tends to produce bloated evidence sets: adding many superficially similar dialogue turns yields little additional recall, but lowers retrieval precision, increases answer-stage context cost, and makes retrieved memories harder to inspect and manage. To address this, we propose HiGMem (Hierarchical and LLM-Guided Memory System), a two-level event-turn memory system that allows LLMs to use event summaries as semantic anchors to predict which related turns are worth reading. This allows the model to inspect high-level event summaries first and then focus on a smaller set of potentially useful turns, providing a concise and reliable evidence set through reasoning, while avoiding the retrieval overhead that would be excessively high compared to vector retrieval. On the LoCoMo10 benchmark, HiGMem achieves the best F1 on four of five question categories and improves adversarial F1 from 0.54 to 0.78 over A-Mem, while retrieving an order of magnitude fewer turns. Code is publicly available at this https URL.

---


### 322. [ComPASS: Towards Personalized Agentic Social Support via Tool-Augmented Companionship](https://arxiv.org/abs/2604.18356)

**<font color=#1a73e8>作者：</font>** Zhaopei Huang, Yanfeng Jia, Jiayi Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Developing compassionate interactive systems requires agents to not only understand user emotions but also provide diverse, substantive support. While recent works explore empathetic dialogue generation, they remain limited in response form and content, struggling to satisfy diverse needs across users and contexts. To address this, we explore empowering agents with external tools to execute diverse actions. Grounded in the psychological concept of "social support", this paradigm delivers substantive, human-like companionship. Specifically, we first design a dozen user-centric tools simulating various multimedia applications, which can cover different types of social support behaviors in human-agent interaction scenarios. We then construct ComPASS-Bench, the first personalized social support benchmark for LLM-based agents, via multi-step automated synthesis and manual refinement. Based on ComPASS-Bench, we further synthesize tool use records to fine-tune the Qwen3-8B model, yielding a task-specific ComPASS-Qwen. Comprehensive evaluations across two settings reveal that while the evaluated LLMs can generate valid tool-calling requests with high success rates, significant gaps remain in final response quality. Moreover, tool-augmented responses achieve better overall performance than directly producing conversational empathy. Notably, our trained ComPASS-Qwen demonstrates substantial improvements over its base model, achieving comparable performance to several large-scale models. Our code and data are available at this https URL.

---


### 323. [ArbGraph: Conflict-Aware Evidence Arbitration for Reliable Long-Form Retrieval-Augmented Generation](https://arxiv.org/abs/2604.18362)

**<font color=#1a73e8>作者：</font>** Qingying Niu, Yuhao Wang, Ruiyang Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) remains unreliable in long-form settings, where retrieved evidence is noisy or contradictory, making it difficult for RAG pipelines to maintain factual consistency. Existing approaches focus on retrieval expansion or verification during generation, leaving conflict resolution entangled with generation. To address this limitation, we propose ArbGraph, a framework for pre-generation evidence arbitration in long-form RAG that explicitly resolves factual conflicts. ArbGraph decomposes retrieved documents into atomic claims and organizes them into a conflict-aware evidence graph with explicit support and contradiction relations. On top of this graph, we introduce an intensity-driven iterative arbitration mechanism that propagates credibility signals through evidence interactions, enabling the system to suppress unreliable and inconsistent claims before final generation. In this way, ArbGraph separates evidence validation from text generation and provides a coherent evidence foundation for downstream long-form generation. We evaluate ArbGraph on two widely used long-form RAG benchmarks, LongFact and RAGChecker, using multiple large language model backbones. Experimental results show that ArbGraph consistently improves factual recall and information density while reducing hallucinations and sensitivity to retrieval noise. Additional analyses show that these gains are evident under conflicting or ambiguous evidence, highlighting the effectiveness of evidence-level conflict resolution for improving the reliability of long-form RAG. The implementation is publicly available at this https URL.

---


### 324. [Training and Agentic Inference Strategies for LLM-based Manim Animation Generation](https://arxiv.org/abs/2604.18364)

**<font color=#1a73e8>作者：</font>** Ravidu Suien Rammuni Silva, Ahmad Lotfi, Isibor Kennedy Ihianle 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating programmatic animation using libraries such as Manim presents unique challenges for Large Language Models (LLMs), requiring spatial reasoning, temporal sequencing, and familiarity with domain-specific APIs that are underrepresented in general pre-training data. A systematic study of how training and inference strategies interact in this setting is lacking in current research. This study introduces ManimTrainer, a training pipeline that combines Supervised Fine-tuning (SFT) with Reinforcement Learning (RL) based Group Relative Policy Optimisation (GRPO) using a unified reward signal that fuses code and visual assessment signals, and ManimAgent, an inference pipeline featuring Renderer-in-the-loop (RITL) and API documentation-augmented RITL (RITL-DOC) strategies. Using these techniques, this study presents the first unified training and inference study for text-to-code-to-video transformation with Manim. It evaluates 17 open-source sub-30B LLMs across nine combinations of training and inference strategies using ManimBench. Results show that SFT generally improves code quality, while GRPO enhances visual outputs and increases the models' responsiveness to extrinsic signals during self-correction at inference time. The Qwen 3 Coder 30B model with GRPO and RITL-DOC achieved the highest overall performance, with a 94% Render Success Rate (RSR) and 85.7% Visual Similarity (VS) to reference videos, surpassing the baseline GPT-4.1 model by +3 percentage points in VS. Additionally, the analysis shows that the correlation between code and visual metrics strengthens with SFT and GRPO but weakens with inference-time enhancements, highlighting the complementary roles of training and agentic inference strategies in Manim animation generation.

---


### 325. [Towards Robust Text-to-Image Person Retrieval: Multi-View Reformulation for Semantic Compensation](https://arxiv.org/abs/2604.18376)

**<font color=#1a73e8>作者：</font>** Chao Yuan, Yujian Zhao, Haoxuan Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In text-to-image person retrieval tasks, the diversity of natural language expressions and the implicitness of visual semantics often lead to the problem of Expression Drift, where semantically equivalent texts exhibit significant feature discrepancies in the embedding space due to phrasing variations, thereby degrading the robustness of image-text alignment. This paper proposes a semantic compensation framework (MVR) driven by Large Language Models (LLMs), which enhances cross-modal representation consistency through multi-view semantic reformulation and feature compensation. The core methodology comprises three components: Multi-View Reformulation (MVR): A dual-branch prompting strategy combines key feature guidance (extracting visually critical components via feature similarity) and diversity-aware rewriting to generate semantically equivalent yet distributionally diverse textual variants; Textual Feature Robustness Enhancement: A training-free latent space compensation mechanism suppresses noise interference through multi-view feature mean-pooling and residual connections, effectively capturing "Semantic Echoes"; Visual Semantic Compensation: VLM generates multi-perspective image descriptions, which are further enhanced through shared text reformulation to address visual semantic gaps. Experiments demonstrate that our method can improve the accuracy of the original model well without training and performs SOTA on three text-to-image person retrieval datasets.

---


### 326. [Learning from Less: Measuring the Effectiveness of RLVR in Low Data and Compute Regimes](https://arxiv.org/abs/2604.18381)

**<font color=#1a73e8>作者：</font>** Justin Bauer, Thomas Walshe, Derek Pham 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning Large Language Models (LLMs) typically relies on large quantities of high-quality annotated data, or questions with well-defined ground truth answers in the case of Reinforcement Learning with Verifiable Rewards (RLVR). While previous work has explored the benefits to model reasoning capabilities by scaling both data and compute used for RLVR, these results lack applicability in many real-world settings where annotated data and accessible compute may be scarce. In this work, we present a comprehensive empirical study of open-source Small Language Model (SLM) performance after RLVR in low data regimes. Across three novel datasets covering number counting problems, graph reasoning, and spatial reasoning, we characterize how model performance scales with dataset size, diversity, and complexity. We demonstrate that (1) procedural datasets allow for fine-grained evaluation and training dataset development with controllable properties (size, diversity, and complexity), (2) under RLVR, models trained on lower complexity tasks can generalize to higher complexity tasks, and (3) training on mixed complexity datasets is associated with the greatest benefits in low data regimes, providing up to 5x sample efficiency versus training on easy tasks. These findings inspire future work on the development of data scaling laws for RLVR and the use of procedural data generators to further understand effective data development for efficient LLM fine-tuning.

---


### 327. [River-LLM: Large Language Model Seamless Exit Based on KV Share](https://arxiv.org/abs/2604.18396)

**<font color=#1a73e8>作者：</font>** Yingtao Shen, An Zou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated exceptional performance across diverse domains but are increasingly constrained by high inference latency. Early Exit has emerged as a promising solution to accelerate inference by dynamically bypassing redundant layers. However, in decoder-only architectures, the efficiency of Early Exit is severely bottlenecked by the KV Cache Absence problem, where skipped layers fail to provide the necessary historical states for subsequent tokens. Existing solutions, such as recomputation or masking, either introduce significant latency overhead or incur severe precision loss, failing to bridge the gap between theoretical layer reduction and practical wall-clock speedup. In this paper, we propose River-LLM, a training-free framework that enables seamless token-level Early Exit. River-LLM introduces a lightweight KV-Shared Exit River that allows the backbone's missing KV cache to be naturally generated and preserved during the exit process, eliminating the need for costly recovery operations. Furthermore, we utilize state transition similarity within decoder blocks to predict cumulative KV errors and guide precise exit decisions. Extensive experiments on mathematical reasoning and code generation tasks demonstrate that River-LLM achieves 1.71 to 2.16 times of practical speedup while maintaining high generation quality.

---


### 328. [StepPO: Step-Aligned Policy Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2604.18401)

**<font color=#1a73e8>作者：</font>** Daoyu Wang, Qingchuan Li, Mingyue Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General agents have given rise to phenomenal applications such as OpenClaw and Claude Code. As these agent systems (a.k.a. Harnesses) strive for bolder goals, they demand increasingly stronger agentic capabilities from foundation Large Language Models (LLMs). Agentic Reinforcement Learning (RL) is emerging as a central post-training paradigm for empowering LLMs with these capabilities and is playing an increasingly pivotal role in agent training. Unlike single-turn token-level alignment or reasoning enhancement, as in RLHF and RLVR, Agentic RL targets multi-turn interactive settings, where the goal is to optimize core agentic capabilities such as decision making and tool use while addressing new challenges including delayed and sparse rewards, as well as long and variable context. As a result, the token-centric modeling and optimization paradigm inherited from traditional LLM RL is becoming increasingly inadequate for capturing real LLM agent behavior. In this paper, we present StepPO as a position on step-level Agentic RL. We argue that the conventional token-level Markov Decision Process (MDP) should be advanced to a step-level MDP formulation, and that the step, rather than the token, should be regarded as the proper action representation for LLM agents. We then propose step-level credit assignment as the natural optimization counterpart of this formulation, thereby aligning policy optimization and reward propagation with the granularity of agent decisions. Finally, we discuss the key systems designs required to realize step-level Agentic RL in practice and preliminary experiments provide initial evidence for the effectiveness of this perspective. We hope that the step-aligned, step-level paradigm embodied in StepPO offers the Agentic RL community a useful lens for understanding agent behavior and helps advance LLMs toward stronger general-agent capabilities.

---


### 329. [Six Llamas: Comparative Religious Ethics Through LoRA-Adapted Language Models](https://arxiv.org/abs/2604.18404)

**<font color=#1a73e8>作者：</font>** Chad Coleman, W. Russell Neuman, Manan Shah 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Six Llamas, a comparative study examining whether large language models fine-tuned on distinct religious corpora encode systematically different patterns of ethical reasoning. Six variants of Meta-Llama-3.1-8B are constructed: one unmodified control and five LoRA-adapted models trained exclusively on the sacred and theological texts of Christianity, Islam, Judaism, Hinduism, or Buddhism. All six models are probed with an identical battery of 17 standardized ethical prompts spanning moral dilemmas, game-theoretic scenarios, public policy questions, and moral-psychological self-assessments. To assess robustness and reproducibility, we implement a multi-temperature sampling design spanning ten temperature settings. We compute response consistency metrics, pairwise inter-model agreement rates, temperature sensitivity coefficients across four prompt domains, and run-to-run stability analyses.
Findings show that LoRA-adapted models produce ethical reasoning patterns that are (a) systematically differentiated from the base model, (b) consistent with the moral logics of their training traditions, (c) structured along interpretable dimensions in moral-philosophical space, (d) core ethical positions remain stable across temperature variations for high-consensus dilemmas. The Trolley Problem achieves 100% consistency across all models and temperatures, while (e) tradition-specific divergence intensifies at higher temperatures in morally contested domains, and (f) the base model exhibits the highest overall response consistency (mean 88.3%), suggesting LoRA adaptation introduces both tradition-specific signal and increased sampling sensitivity.
The study offers a proof-of-concept for the condensate comparative method using differentially trained language models as instruments for cultural and ethical analysis and identifies specific criteria for falsification and planned extensions.

---


### 330. [MedProbeBench: Systematic Benchmarking at Deep Evidence Integration for Expert-level Medical Guideline](https://arxiv.org/abs/2604.18418)

**<font color=#1a73e8>作者：</font>** Jiyao Liu, Jianghan Shen, Sida Song 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in deep research systems enable large language models to retrieve, synthesize, and reason over large-scale external knowledge. In medicine, developing clinical guidelines critically depends on such deep evidence integration. However, existing benchmarks fail to evaluate this capability in realistic workflows requiring multi-step evidence integration and expert-level judgment. To address this gap, we introduce MedProbeBench, the first benchmark leveraging high-quality clinical guidelines as expert-level references. Medical guidelines, with their rigorous standards in neutrality and verifiability, represent the pinnacle of medical expertise and pose substantial challenges for deep research agents. For evaluation, we propose MedProbe-Eval, a comprehensive evaluation framework featuring: (1) Holistic Rubrics with 1,200+ task-adaptive rubric criteria for comprehensive quality assessment, and (2) Fine-grained Evidence Verification for rigorous validation of evidence precision, grounded in 5,130+ atomic claims. Evaluation of 17 LLMs and deep research agents reveals critical gaps in evidence integration and guideline generation, underscoring the substantial distance between current capabilities and expert-level clinical guideline development. Project: this https URL

---


### 331. [Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning](https://arxiv.org/abs/2604.18419)

**<font color=#1a73e8>作者：</font>** Hen Davidov, Nachshon Cohen, Oren Kalinsky 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) using chain-of-thought reasoning often waste substantial compute by producing long, incorrect responses. Abstention can mitigate this by withholding outputs unlikely to be correct. While most abstention methods decide to withhold outputs before or after generation, dynamic mid-generation abstention considers early termination of unpromising reasoning traces at each token position. Prior work has explored empirical variants of this idea, but principled guidance for the abstention rule remains lacking. We present a formal analysis of dynamic abstention for LLMs, modeling abstention as an explicit action within a regularized reinforcement learning framework. An abstention reward parameter controls the trade-off between compute and information. We show that abstaining when the value function falls below this reward strictly outperforms natural baselines under general conditions. We further derive a principled and efficient method to approximate the value function. Empirical results on mathematical reasoning and toxicity avoidance tasks support our theory and demonstrate improved selective accuracy over existing methods.

---


### 332. [Revisiting Change VQA in Remote Sensing with Structured and Native Multimodal Qwen Models](https://arxiv.org/abs/2604.18429)

**<font color=#1a73e8>作者：</font>** Yakoub Bazi, Mohamad M. Al Rahhal, Mansour Zuair 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Change visual question answering (Change VQA) addresses the problem of answering natural-language questions about semantic changes between bi-temporal remote sensing (RS) images. Although vision-language models (VLMs) have recently been studied for temporal RS image understanding, Change VQA remains underexplored in the context of modern multimodal models. In this letter, we revisit the CDVQA benchmark using recent Qwen models under a unified low-rank adaptation (LoRA) setting. We compare Qwen3-VL, which follows a structured vision-language pipeline with multi-depth visual conditioning and a full-attention decoder, with Qwen3.5, a native multimodal model that combines a single-stage alignment with a hybrid decoder backbone. Experimental results on the official CDVQA test splits show that recent VLMs improve over earlier specialized baselines. They further show that performance does not scale monotonically with model size, and that native multimodal models are more effective than structured vision-language pipelines for this task. These findings indicate that tightly integrated multimodal backbones contribute more to performance than scale or explicit multi-depth visual conditioning for language-driven semantic change reasoning in RS imagery.

---


### 333. [Learning Invariant Modality Representation for Robust Multimodal Learning from a Causal Inference Perspective](https://arxiv.org/abs/2604.18460)

**<font color=#1a73e8>作者：</font>** Sijie Mai, Shiqin Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal affective computing aims to predict humans' sentiment, emotion, intention, and opinion using language, acoustic, and visual modalities. However, current models often learn spurious correlations that harm generalization under distribution shifts or noisy modalities. To address this, we propose a causal modality-invariant representation (CmIR) learning framework for robust multimodal learning. At its core, we introduce a theoretically grounded disentanglement method that separates each modality into `causal invariant representation' and `environment-specific spurious representation' from a causal inference perspective. CmIR ensures that the learned invariant representations retain stable predictive relationships with labels across different environments while preserving sufficient information from the raw inputs via invariance constraint, mutual information constraint, and reconstruction constraint. Experiments across multiple multimodal benchmarks demonstrate that CmIR achieves state-of-the-art performance. CmIR particularly excels on out-of-distribution data and noisy data, confirming its robustness and generalizability.

---


### 334. [Using large language models for embodied planning introduces systematic safety risks](https://arxiv.org/abs/2604.18463)

**<font color=#1a73e8>作者：</font>** Tao Zhang, Kaixian Qu, Zhibin Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as planners for robotic systems, yet how safely they plan remains an open question. To evaluate safe planning systematically, we introduce DESPITE, a benchmark of 12,279 tasks spanning physical and normative dangers with fully deterministic validation. Across 23 models, even near-perfect planning ability does not ensure safety: the best-planning model fails to produce a valid plan on only 0.4% of tasks but produces dangerous plans on 28.3%. Among 18 open-source models from 3B to 671B parameters, planning ability improves substantially with scale (0.4-99.3%) while safety awareness remains relatively flat (38-57%). We identify a multiplicative relationship between these two capacities, showing that larger models complete more tasks safely primarily through improved planning, not through better danger avoidance. Three proprietary reasoning models reach notably higher safety awareness (71-81%), while non-reasoning proprietary models and open-source reasoning models remain below 57%. As planning ability approaches saturation for frontier models, improving safety awareness becomes a central challenge for deploying language-model planners in robotic systems.

---


### 335. [Semantic Step Prediction: Multi-Step Latent Forecasting in LLM Reasoning Trajectories via Step Sampling](https://arxiv.org/abs/2604.18464)

**<font color=#1a73e8>作者：</font>** Yidi Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semantic Tube Prediction (STP) leverages representation geometric to regularize LLM hidden-state trajectories toward locally linear geodesics during fine-tuning, thereby greatly improving data efficiency. The original STP recipe samples random token sub-spans, which is compatible with the base large language model (LLM) training architecture. Inspired by STP, we are interested to investigate whether the sampling position can further enhance the semantic structure of multi-step reasoning, and hence affect its geometric impact. We applied STP at consecutive semantic reasoning step boundaries and achieved 168x more accurate multi-step latent prediction than frozen baselines on ProcessBench (3,400 samples), compared to only 4x for the random-token STP. Probing the latent manifold with a learned non-linear predictor reveals that STP-shaped trajectories are smooth curves, not straight lines: a 3-layer MLP reduces prediction error by a further 3-12x over linear extrapolation on step-boundary models. Removing the language modeling loss yields trajectories that are 2x more MLP-predictable than the combined loss, revealing a tradeoff between generation quality and geometric purity. Our results identify sampling position as the critical variable in geometric regularization and establish multi-step latent prediction MSE as a new evaluation metric for this class of methods.

---


### 336. [NI Sampling: Accelerating Discrete Diffusion Sampling by Token Order Optimization](https://arxiv.org/abs/2604.18471)

**<font color=#1a73e8>作者：</font>** Enshu Liu, Xuefei Ning, Yu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion language models (dLLMs) have recently emerged as a promising alternative to traditional autoregressive approaches, offering the flexibility to generate tokens in arbitrary orders and the potential of parallel decoding. However, existing heuristic sampling strategies remain inefficient: they choose only a small part of tokens to sample at each step, leaving substantial room for improvement. In this work, we study the problem of token sampling order optimization and demonstrate its significant potential for acceleration. Specifically, we find that fully leveraging correct predictions at each step can reduce the number of sampling iterations by an order of magnitude without compromising accuracy. Based on this, we propose Neural Indicator Sampling (NI Sampling), a general sampling order optimization framework that utilize a neural indicator to decide which tokens should be sampled at each step. We further propose a novel trajectory-preserving objective to train the indicator. Experiments on LLaDA and Dream models across multiple benchmarks show that our method achieves up to 14.3$\times$ acceleration over full-step sampling with negligible performance drop, and consistently outperforms confidence threshold sampling in the accuracy-step trade-off. Code is available at this https URL.

---


### 337. [Train Separately, Merge Together: Modular Post-Training with Mixture-of-Experts](https://arxiv.org/abs/2604.18473)

**<font color=#1a73e8>作者：</font>** Jacob Morrison, Sanjay Adhikesaven, Akshita Bhagia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extending a fully post-trained language model with new domain capabilities is fundamentally limited by monolithic training paradigms: retraining from scratch is expensive and scales poorly, while continued training often degrades existing capabilities. We present BAR (Branch-Adapt-Route), which trains independent domain experts, each through its own mid-training, supervised finetuning, and reinforcement learning pipeline, and composes them via a Mixture-of-Experts architecture with lightweight router training. Unlike retraining approaches that mix all domains and require full reprocessing for any update (with cost scaling quadratically), BAR enables updating individual experts independently with linear cost scaling and no degradation to existing domains. At the 7B scale, with experts for math, code, tool use, and safety, BAR achieves an overall score of 49.1 (averaged across 7 evaluation categories), matching or exceeding re-training baselines (47.8 without mid-training, 50.5 with). We further show that modular training provides a structural advantage: by isolating each domain, it avoids the catastrophic forgetting that occurs when late-stage RL degrades capabilities from earlier training stages, while significantly reducing the cost and complexity of updating or adding a domain. Together, these results suggest that decoupled, expert-based training is a scalable alternative to monolithic retraining for extending language models.

---


### 338. [WorldDB: A Vector Graph-of-Worlds Memory Engine with Ontology-Aware Write-Time Reconciliation](https://arxiv.org/abs/2604.18478)

**<font color=#1a73e8>作者：</font>** Harish Santhanalakshmi Ganesan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent memory is the bottleneck separating stateless chatbots from long-running agentic systems. Retrieval-augmented generation (RAG) over flat vector stores fragments facts into chunks, loses cross-session identity, and has no first-class notion of supersession or contradiction. Recent bitemporal knowledge-graph systems (Graphiti, Memento, Hydra DB) add typed edges and valid-time metadata, but the graph itself remains flat: no recursive composition, no content-addressed invariants on nodes, and edge types carry no behavior beyond a label. We present WorldDB, a memory engine built on three commitments: (i) every node is a world -- a container with its own interior subgraph, ontology scope, and composed embedding, recursive to arbitrary depth; (ii) nodes are content-addressed and immutable, so any edit produces a new hash at the node and every ancestor, giving a Merkle-style audit trail for free; (iii) edges are write-time programs -- each edge type ships on_insert/on_delete/on_query_rewrite handlers (supersession closes validity, contradicts preserves both sides, same_as stages a merge proposal), so no raw append path exists. On LongMemEval-s (500 questions, ~115k-token conversational stacks), WorldDB with Claude Opus 4.7 as answerer achieves 96.40% overall / 97.11% task-averaged accuracy, a +5.61pp improvement over the previously reported Hydra DB state-of-the-art (90.79%) and +11.20pp over Supermemory (85.20%), with perfect single-session-assistant recall and robust performance on temporal reasoning (96.24%), knowledge update (98.72%), and preference synthesis (96.67%). Ablations show that the engine's graph layer -- resolver-unified entities and typed refers_to edges -- contributes +7.0pp task-averaged independently of the underlying answerer.

---


### 339. [XEmbodied: A Foundation Model with Enhanced Geometric and Physical Cues for Large-Scale Embodied Environments](https://arxiv.org/abs/2604.18484)

**<font color=#1a73e8>作者：</font>** Kangan Qian, ChuChu Xie, Yang Zhong 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models drive next-generation autonomous systems, but training them requires scalable, high-quality annotations from complex environments. Current cloud pipelines rely on generic vision-language models (VLMs) that lack geometric reasoning and domain semantics due to their 2D image-text pretraining. To address this mismatch, we propose XEmbodied, a cloud-side foundation model that endows VLMs with intrinsic 3D geometric awareness and interaction with physical cues (e.g., occupancy grids, 3D boxes). Instead of treating geometry as auxiliary input, XEmbodied integrates geometric representations via a structured 3D Adapter and distills physical signals into context tokens using an Efficient Image-Embodied Adapter. Through progressive domain curriculum and reinforcement learning post-training, XEmbodied preserves general capabilities while demonstrating robust performance across 18 public benchmarks. It significantly improves spatial reasoning, traffic semantics, embodied affordance, and out-of-distribution generalization for large-scale scenario mining and embodied VQA.

---


### 340. [QRAFTI: An Agentic Framework for Empirical Research in Quantitative Finance](https://arxiv.org/abs/2604.18500)

**<font color=#1a73e8>作者：</font>** Terence Lim, Kumar Muthuraman, Michael Sury  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We introduce a multi-agent framework intended to emulate parts of a quantitative research team and support equity factor research on large financial panel datasets. QRAFTI integrates a research toolkit for panel data with MCP servers that expose data access, factor construction, and custom coding operations as callable tools. It can help replicate established factors, formulate and test new signals, and generate standardized research reports accompanied by narrative analysis and computational traces. On multi-step empirical tasks, using chained tool calls and reflection-based planning may offer better performance and explainability than dynamic code generation alone.

---


### 341. [MASS-RAG: Multi-Agent Synthesis Retrieval-Augmented Generation](https://arxiv.org/abs/2604.18509)

**<font color=#1a73e8>作者：</font>** Xingchen Xiao, Heyan Huang, Runheng Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used in retrieval-augmented generation (RAG) to incorporate external knowledge at inference time. However, when retrieved contexts are noisy, incomplete, or heterogeneous, a single generation process often struggles to reconcile evidence effectively. We propose \textbf{MASS-RAG}, a multi-agent synthesis approach to retrieval-augmented generation that structures evidence processing into multiple role-specialized agents. MASS-RAG applies distinct agents for evidence summarization, evidence extraction, and reasoning over retrieved documents, and combines their outputs through a dedicated synthesis stage to produce the final answer. This design exposes multiple intermediate evidence views, allowing the model to compare and integrate complementary information before answer generation. Experiments on four benchmarks show that MASS-RAG consistently improves performance over strong RAG baselines, particularly in settings where relevant evidence is distributed across retrieved contexts.

---


### 342. [S2H-DPO: Hardness-Aware Preference Optimization for Vision-Language Models](https://arxiv.org/abs/2604.18512)

**<font color=#1a73e8>作者：</font>** Nitish Shukla, Surgan Jandial, Arun Ross  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated remarkable progress in single-image understanding, yet effective reasoning across multiple images remains challenging. We identify a critical capability gap in existing multi-image alignment approaches: current methods focus primarily on localized reasoning with pre-specified image indices (``Look at Image 3 and...''), bypassing the essential skills of global visual search and autonomous cross-image comparison. To address this limitation, we introduce a Simple-to-Hard (S2H) learning framework that systematically constructs multi-image preference data across three hierarchical reasoning levels requiring an increasing level of capabilities: (1) single-image localized reasoning, (2) multi-image localized comparison, and (3) global visual search. Unlike prior work that relies on model-specific attributes, such as hallucinations or attention heuristics, to generate preference pairs, our approach leverages prompt-driven complexity to create chosen/rejected pairs that are applicable across different models. Through extensive evaluations on LLaVA and Qwen-VL models, we show that our diverse multi-image reasoning data significantly enhances multi-image reasoning performance, yielding significant improvements over baseline methods across benchmarks. Importantly, our approach maintains strong single-image reasoning performance while simultaneously strengthening multi-image understanding capabilities, thus advancing the state of the art for holistic visual preference alignment.

---


### 343. [LLM Safety From Within: Detecting Harmful Content with Internal Representations](https://arxiv.org/abs/2604.18519)

**<font color=#1a73e8>作者：</font>** Difan Jiao, Yilun Liu, Ye Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Guard models are widely used to detect harmful content in user prompts and LLM responses. However, state-of-the-art guard models rely solely on terminal-layer representations and overlook the rich safety-relevant features distributed across internal layers. We present SIREN, a lightweight guard model that harnesses these internal features. By identifying safety neurons via linear probing and combining them through an adaptive layer-weighted strategy, SIREN builds a harmfulness detector from LLM internals without modifying the underlying model. Our comprehensive evaluation shows that SIREN substantially outperforms state-of-the-art open-source guard models across multiple benchmarks while using 250 times fewer trainable parameters. Moreover, SIREN exhibits superior generalization to unseen benchmarks, naturally enables real-time streaming detection, and significantly improves inference efficiency compared to generative guard models. Overall, our results highlight LLM internal states as a promising foundation for practical, high-performance harmfulness detection.

---


### 344. [OGER: A Robust Offline-Guided Exploration Reward for Hybrid Reinforcement Learning](https://arxiv.org/abs/2604.18530)

**<font color=#1a73e8>作者：</font>** Xinyu Ma, Mingzhou Xu, Xuebo Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Reinforcement Learning with Verifiable Rewards (RLVR) have significantly improved Large Language Model (LLM) reasoning, yet models often struggle to explore novel trajectories beyond their initial latent space. While offline teacher guidance and entropy-driven strategies have been proposed to address this, they often lack deep integration or are constrained by the model's inherent capacity. In this paper, we propose OGER, a novel framework that unifies offline teacher guidance and online reinforcement learning through a specialized reward modeling lens. OGER employs multi-teacher collaborative training and constructs an auxiliary exploration reward that leverages both offline trajectories and the model's own entropy to incentivize autonomous exploration. Extensive experiments across mathematical and general reasoning benchmarks demonstrate that OGER significantly outperforms competitive baselines, achieving substantial gains in mathematical reasoning while maintaining robust generalization to out-of-domain tasks. We provide a comprehensive analysis of training dynamics and conduct detailed ablation studies to validate the effectiveness of our entropy-aware reward modulation. Our code is available at this https URL.

---


### 345. [GSQ: Highly-Accurate Low-Precision Scalar Quantization for LLMs via Gumbel-Softmax Sampling](https://arxiv.org/abs/2604.18556)

**<font color=#1a73e8>作者：</font>** Alireza Dadgarnia, Soroush Tabesh, Mahdi Nikdan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Weight quantization has become a standard tool for efficient LLM deployment, especially for local inference, where models are now routinely served at 2-3 bits per parameter. The state of the art is currently split into two sets of methods: simple scalar quantization techniques, such as GPTQ or AWQ, which are widely deployed but plateau in accuracy at 3-4 bits per parameter (bpp), and "second-generation" vector- or trellis-quantized methods, such as QTIP, GPTVQ and AQLM, which push the accuracy frontier at low bit-widths but are notoriously hard to implement and to scale, and have gained relatively less traction. In this paper, we ask whether this gap is fundamental, or whether a carefully optimized scalar quantizer can recover most of it. We answer in the affirmative, by introducing GSQ (Gumbel-Softmax Quantization), a post-training scalar quantization method which jointly learns the per-coordinate grid assignments and the per-group scales using a Gumbel-Softmax relaxation of the discrete grid. GSQ matches the cardinality of the relaxation to the small number of levels available in the target bit-width regime (e.g., 3-8 levels for ternary and 3 bpp, respectively), making the relaxation tight and the optimization tractable. Practically, on the standard Llama-3.1-8B/70B-Instruct models, GSQ closes most of the gap between scalar quantization and the QTIP frontier at 2 and 3 bits, while using a symmetric scalar grid with group-wise quantization, and thus fully compatible with existing scalar inference kernels. We further show that GSQ scales to trillion-scale Mixture-of-Experts models such as Kimi-K2.5, where vector-quantized methods are difficult to apply.

---


### 346. [Dual Alignment Between Language Model Layers and Human Sentence Processing](https://arxiv.org/abs/2604.18563)

**<font color=#1a73e8>作者：</font>** Tatsuki Kuribayashi, Alex Warstadt, Yohei Oseki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A recent study (Kuribayashi et al., 2025) has shown that human sentence processing behavior, typically measured on syntactically unchallenging constructions, can be effectively modeled using surprisal from early layers of large language models (LLMs). This raises the question of whether such advantages of internal layers extend to more syntactically challenging constructions, where surprisal has been reported to underestimate human cognitive effort. In this paper, we begin by exploring internal layers that better estimate human cognitive effort observed in syntactic ambiguity processing in English. Our experiments show that, in contrast to naturalistic reading, later layers better estimate such a cognitive effort, but still underestimate the human data. This dual alignment sheds light on different modes of sentence processing in humans and LMs: naturalistic reading employs a somewhat weak prediction akin to earlier layers of LMs, while syntactically challenging processing requires more fully-contextualized representations, better modeled by later layers of LMs. Motivated by these findings, we also explore several probability-update measures using shallow and deep layers of LMs, showing a complementary advantage to single-layer's surprisal in reading time modeling.

---


### 347. [MultiWorld: Scalable Multi-Agent Multi-View Video World Models](https://arxiv.org/abs/2604.18564)

**<font color=#1a73e8>作者：</font>** Haoyu Wu, Jiwen Yu, Yingtian Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models have achieved remarkable success in simulating environmental dynamics in response to actions by users or agents. They are modeled as action-conditioned video generation models that take historical frames and current actions as input to predict future frames. Yet, most existing approaches are limited to single-agent scenarios and fail to capture the complex interactions inherent in real-world multi-agent systems. We present \textbf{MultiWorld}, a unified framework for multi-agent multi-view world modeling that enables accurate control of multiple agents while maintaining multi-view consistency. We introduce the Multi-Agent Condition Module to achieve precise multi-agent controllability, and the Global State Encoder to ensure coherent observations across different views. MultiWorld supports flexible scaling of agent and view counts, and synthesizes different views in parallel for high efficiency. Experiments on multi-player game environments and multi-robot manipulation tasks demonstrate that MultiWorld outperforms baselines in video fidelity, action-following ability, and multi-view consistency. Project page: this https URL

---


### 348. [Benchmarking System Dynamics AI Assistants: Cloud Versus Local LLMs on CLD Extraction and Discussion](https://arxiv.org/abs/2604.18566)

**<font color=#1a73e8>作者：</font>** Terry Leitch  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a systematic evaluation of large language model families -- spanning both proprietary cloud APIs and locally-hosted open-source models -- on two purpose-built benchmarks for System Dynamics AI assistance: the \textbf{CLD Leaderboard} (53 tests, structured causal loop diagram extraction) and the \textbf{Discussion Leaderboard} (interactive model discussion, feedback explanation, and model building coaching).
On CLD extraction, cloud models achieve 77--89\% overall pass rates; the best local model reaches 77\% (Kimi~K2.5~GGUF~Q3, zero-shot engine), matching mid-tier cloud performance. On Discussion, the best local models achieve 50--100\% on model building steps and 47--75\% on feedback explanation, but only 0--50\% on error fixing -- a category dominated by long-context prompts that expose memory limits in local deployments.
A central contribution of this paper is a systematic analysis of \textit{model type effects} on performance: we compare reasoning vs.\ instruction-tuned architectures, GGUF (this http URL) vs.\ MLX (mlx\_lm) backends, and quantization levels (Q3 / Q4\_K\_M / MLX-3bit / MLX-4bit / MLX-6bit) across the same underlying model families. We find that backend choice has larger practical impact than quantization level: mlx\_lm does not enforce JSON schema constraints, requiring explicit prompt-level JSON instructions, while this http URL grammar-constrained sampling handles JSON reliably but causes indefinite generation on long-context prompts for dense models.
We document the full parameter sweep ($t$, $p$, $k$) for all local models, cleaned timing data (stuck requests excluded), and a practitioner guide for running 671B--123B parameter models on Apple~Silicon.

---


### 349. [A multimodal and temporal foundation model for virtual patient representations at healthcare system scale](https://arxiv.org/abs/2604.18570)

**<font color=#1a73e8>作者：</font>** Andrew Zhang, Tong Ding, Sophia J. Wagner 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern medicine generates vast multimodal data across siloed systems, yet no existing model integrates the full breadth and temporal depth of the clinical record into a unified patient representation. We introduce Apollo, a multimodal temporal foundation model trained and evaluated on over three decades of longitudinal hospital records from a major US hospital system, composed of 25 billion records from 7.2 million patients, representing 28 distinct medical modalities and 12 major medical specialties. Apollo learns a unified representation space integrating over 100 thousand unique medical events in our clinical vocabulary as well as images and clinical text. This "atlas of medical concepts" forms a computational substrate for modeling entire patient care journeys comprised of sequences of structured and unstructured events, which are compressed by Apollo into virtual patient representations. To assess the potential of these whole-patient representations, we created 322 prognosis and retrieval tasks from a held-out test set of 1.4 million patients. We demonstrate the generalized clinical forecasting potential of Apollo embeddings, including predicting new disease onset risk up to five years in advance (95 tasks), disease progression (78 tasks), treatment response (59 tasks), risk of treatment-related adverse events (17 tasks), and hospital operations endpoints (12 tasks). Using feature attribution techniques, we show that model predictions align with clinically-interpretable multimodal biomarkers. We evaluate semantic similarity search on 61 retrieval tasks, and moreover demonstrate the potential of Apollo as a multimodal medical search engine using text and image queries. Together, these modeling capabilities establish the foundation for computable medicine, where the full context of patient care becomes accessible to computational reasoning.

---


### 350. [T-REN: Learning Text-Aligned Region Tokens Improves Dense Vision-Language Alignment and Scalability](https://arxiv.org/abs/2604.18573)

**<font color=#1a73e8>作者：</font>** Savya Khosla, Sethuraman T V, Aryan Chadha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent progress, vision-language encoders struggle with two core limitations: (1) weak alignment between language and dense vision features, which hurts tasks like open-vocabulary semantic segmentation; and (2) high token counts for fine-grained visual representations, which limits scalability to long videos. This work addresses both limitations. We propose T-REN (Text-aligned Region Encoder Network), an efficient encoder that maps visual data to a compact set of text-aligned region-level representations (or region tokens). T-REN achieves this through a lightweight network added on top of a frozen vision backbone, trained to pool patch-level representations within each semantic region into region tokens and align them with region-level text annotations. With only 3.7% additional parameters compared to the vision-language backbone, this design yields substantially stronger dense cross-modal understanding while reducing the token count by orders of magnitude. Specifically, T-REN delivers +5.9 mIoU on ADE20K open-vocabulary segmentation, +18.4% recall on COCO object-level text-image retrieval, +15.6% recall on Ego4D video object localization, and +17.6% mIoU on VSPW video scene parsing, all while reducing token counts by more than 24x for images and 187x for videos compared to the patch-based vision-language backbone. The code and model are available at this https URL.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
