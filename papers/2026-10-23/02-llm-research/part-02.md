# 🧠 大模型相关研究 | 2026年10月23日

> 本类共 **204** 篇论文：已确认 **192** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-204](./part-05.md)

---

### 51. [GenXR-Bench: Benchmarking Coding Agents for Interactive XR Development](https://arxiv.org/abs/2610.29014)

**<font color=#1a73e8>作者：</font>** William Huang, David Li, Xiang 'Anthony' Chen 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents are rapidly advancing from single-file generation to long-horizon repository-scale engineering, yet the evaluation of their capabilities to author interactive extended reality (XR) applications remains an open challenge. Unlike traditional software, XR applications operate within dynamic 3D physical environments where runtime robustness depends jointly on continuous user motion, spatial input, and environmental sensing. We introduce GenXR-Bench, the first benchmark for the end-to-end evaluation of coding agents in XR software development. GenXR-Bench contains 112 expert-authored tasks spanning 24 feature implementations, 21 bug repairs, and 67 application generation tasks. Held-out tests combine scripted and adaptive interactions with programmatic and visual assertions to evaluate core functionality and runtime behavior. GenXR-Bench's testing suite achieves 96.5% accuracy against blinded expert judgments of 124 candidate applications executed on consumer XR hardware. Evaluating 10 models on GenXR-Bench, we find that the strongest configuration achieves only 50.9% overall Pass@1. Failure analysis identifies recurring misunderstandings in asynchronous sensor lifecycles, physical grounding, and embodied interaction semantics. GenXR-Bench establishes a reproducible testbed for evaluating coding agents in the interactive and physically situated conditions of spatial computing.

---


### 52. [Inheritance as an Admission Test for LLM Prompt Merge Operators](https://arxiv.org/abs/2610.29023)

**<font color=#1a73e8>作者：</font>** Zan-Kai Chong, Hiroyuki Ohsaki, Bryan Ng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are often improved by iterating until a fixed verifier is done. Once that verifier saturates, the loop has nothing left to climb. We instead score agents against the current population, and a frozen panel records whether anyone got better. The panel mean can rise inside the seeds by elimination alone. We therefore count a run as training only when its final mean beats the best generation-zero member. A merge is admitted only when the child moves toward the donor, past the child the same operator produces at zero dose, and the lower confidence bound on that movement reaches half the requested dose. That is the admission test. A detectable shortfall rejects the operator, and the test is otherwise undetermined. We keep realised fitness \phi as the selector and reference performance \theta as the unused ruler. Every measurement uses gemini-3.1-flash-lite on one negotiation task, and no fixed-oracle arm was run. In the open loop, tactic append grafts short donor rules and is admitted. Free rewrite moves only a third of the requested dose and is rejected. Template append pastes raw donor replies into the child. Its movement clears the bound on the first probe but not on the re-probe, and it is left undetermined. A held-out re-probe on the five situations the merge never saw confirms that both appends move, and it does not rescue free rewrite. Neither append rises with the dose. Constrained rewrite is admitted in the open loop and was not run in the closed loop, which changes only the operator. The population, the scores and the task stay fixed. No free-rewrite run beats the best generation-zero member. Every tactic-append run and every template-append run does. Sampled loop children keep that split. Free rewrite moves no further toward the donor, and both appends still clear the bound, by less than in the open loop.

---


### 53. [Single-Image Food Mass Estimators Do Not Transfer Their Gram Scale Across Datasets](https://arxiv.org/abs/2610.29025)

**<font color=#1a73e8>作者：</font>** Yongsheng Lian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating food mass from a photograph is central to image-based dietary assessment, but whether trained models transfer to new cameras and foods is unclear. We fine-tuned DINOv2-base on 2,253 weighed Nutrition5k dishes to predict mass from one RGB photograph and compared it with a zero-shot vision-language model, Qwen3-VL-32B, on Nutrition5k and three external datasets: ASA24 studio portions, ECUSTFD whole foods and Food Portion Benchmark meal trays. In domain, the fine-tuned model's mean absolute error was 24.8 g, less than half of Qwen's. On external datasets it did not beat Qwen. For a food it had never seen, it ranked portions by size, but no better than a count of food pixels. Its gram scale was wrong in two ways: it changed with how much of the scene the photograph showed, and it was off by a different factor for each food. Training on other foods or trays from the tested dataset cut the external error by 38 to 65%. DINOv2-large, a larger backbone trained on the same dishes, did not reduce the external error. One labeled photograph of the same food cut the model's ASA24 error to 28.3 g, better than that photograph achieved alone. Prediction intervals that held the true mass for 90% of Nutrition5k dishes held it for at most half of external photographs. Nutrition5k often photographed the same plate several times, so a random test split shared near-identical photographs with training and overstated accuracy. Single-image mass estimators therefore need labeled photographs from the setting where they are used.

---


### 54. [Beyond Tokens: NumAnchor for Address-Grounded Numeric Operand Representation in Assembly Language Models](https://arxiv.org/abs/2610.29027)

**<font color=#1a73e8>作者：</font>** Kun Liu, Keith Mitchell, Xin Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Assembly language models (ALMs) are becoming important for automated binary analysis, yet their token-level interfaces often obscure numeric-like operands. In two corpora, such operands account for 45.7% and 40.9% of operand occurrences and may denote branch targets, global data, stack slots, constants, or unresolved pointer-derived values. Existing normalization strategies often lose their identities and structural relationships. We present NumAnchor, an input-boundary adapter that represents recoverable numeric-like operands as typed, canonicalized program entities. NumAnchor encodes code, data, and stack context in compact structural side descriptors, preserving entity identity and locality without increasing the host sequence length. These descriptors are fused into input embeddings before the first Transformer layer, while the host architecture, pretraining objectives, and downstream protocols remain unchanged. Probing frozen instruction-level embeddings yields 98.7% hierarchical-location accuracy and AUROC scores of 0.932 and 0.907 for jump and call target alignment, respectively, showing that the encoded structural information remains recoverable. Across multiple ALM families, NumAnchor achieves relative improvements of up to 35.0% in Recall@1 and 31.7% in MRR on 10k-candidate function retrieval, and improves execution-aware type recovery by up to 5.2 F1 points. Ablations show complementary gains from code, data, and stack descriptors with modest overhead.

---


### 55. [AutoFraming: Synthesizing Dynamic Frames of C Code with LLMs](https://arxiv.org/abs/2610.29046)

**<font color=#1a73e8>作者：</font>** Han Zhou, Yu Luo, Dianxiang Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown considerable promise in synthesizing formal specifications from source code. However, existing approaches primarily focus on functional contracts and loop invariants, while largely neglecting frame conditions, which specify the memory locations that may or may not be modified during execution and constitute an essential part of formal specifications. To address this limitation, we propose an LLM-based approach for synthesizing ACSL frame specifications alongside functional contracts from C code. Our approach analyzes code property graphs (CPGs) to extract frame-relevant information from the input code and leverages this information to guide the LLM in generating accurate frame conditions. The resulting specifications capture both region-separation constraints and data dependencies that govern variable modifications. Experimental results demonstrate the effectiveness of our approach. On a benchmark of 84 ACSL-compliant functions from non-trivial real-world systems, our method successfully synthesizes error-free frame specifications for 92.9% of the functions, representing a 179% relative improvement over state-of-the-art techniques. On a second benchmark consisting of 51 functions, the success rate increases from 80.4% to 96.1%. Furthermore, when integrated as an auxiliary component into existing LLM-based ACSL-synthesis frameworks, our approach improves frame-specification generation performance by up to 61.9%.

---


### 56. [Our Own Jev: Typed Decisions in One Forward Pass, from an In-House Judge to Open LoRA Models](https://arxiv.org/abs/2610.29052)

**<font color=#1a73e8>作者：</font>** Yuchuan Weng, Chi Liu, Xin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A typed decision maps evidence, a question and a fixed set of options to a probability for every option, computed in one forward pass, by reading a language model's logits or a small head over its hidden states, instead of generating and parsing text. The commercial system Jev popularised this System~1 interface, and open reproductions have followed. We report two uses of the pattern. \emph{Part I} describes an in-house System~1 judge that triages about 148K agentic coding session records for a training corpus. It replaces a frontier LLM judge that cost on the order of \$1,000 per pass and whose stored labels matched a fresh two-judge consensus on only 26.9\% of the sessions where the two judges agreed; a self-hosted frozen backbone with a rank-16 LoRA adapter and a pointer head answers three typed questions in one forward pass, judges 1,000 sessions in about three minutes of one GPU, about \$0.06 at a reference rate and roughly 1\% of the frontier judge's cost, and keeps every session inside the organisation. \emph{Part II} asks whether a readout that adds no parameters can be competitive and whether training one helps. Applying the public Eikos recipe and corpus of about 25K decisions to three further backbones (1B, 2B and 35B), we read the frozen output layer of a LoRA-adapted decoder. On the 111 public hard items of JevBench our single-seed 35B, developed with those items in view, scores 79.3\%, not significantly different from the commercial reference (73.0\%, unadjusted $p=0.12$) and ahead of five open systems after Holm--Bonferroni correction; our 2B is ahead of all four kev checkpoints on the leaderboard. A single-seed ablation finds no detectable benefit from training the 26 letter rows of the output layer, and a retrain on a later corpus release moves the 2B's hard-tier accuracy by 11.7 points, which shows how little small evaluations resolve.

---


### 57. [Dynamics of Hidden Learning Structure](https://arxiv.org/abs/2610.29054)

**<font color=#1a73e8>作者：</font>** Qinyou Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A learner's present predictions do not fully determine how it will learn next. We study the dynamics of hidden learning structure through two related operations. Fiber Regulation Theory (FRT) describes protected repair of existing function and the learning responses left available after repair. Fiber Acquisition Theory (FAT) describes the formation and renewal of trainable structure, distinguishing neutral installation, access to a learning signal, and additional functional directions. The two operations also constrain one another. A repair obligation can force a change in a learning channel, while acquired features can make new protected repairs feasible or reduce the minimum coefficient cost of existing ones. We characterize joint admissibility and response reachability, and give a finite supervised-learning construction in which the two operations together produce a favorable response absent from either operation alone. We implement protected head repair and fixed-capacity LoRA renewal in Qwen2.5-32B with AdamW, under replay and output distillation. Across two training trajectories differing in seed and within-task example order, the coordinated policy achieves higher teacher-forced Exact than either separate policy in all four comparisons. It also has the lowest macro NLL under both learning rules on the second trajectory. The implementations realize structure-conditioned self-regulation within specified information and action constraints: accessible state readouts and arrived evidence guide repairs and structural renewals, and ordinary learning continues from the modified state.

---


### 58. [Does Every Instance Count Equally? Order Effects in LLM Multi-Instance Processing](https://arxiv.org/abs/2610.29057)

**<font color=#1a73e8>作者：</font>** Jingxuan Chen, Mohammad Taher Pilehvar, Jose Camacho-Collados  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Users increasingly rely on large language models (LLMs) to analyse collections of independent inputs, such as product reviews or social media posts, and return a single aggregated answer. This setting requires multi-instance processing (MIP), where a model combines information from multiple instances into one prediction. We study a task in which the model must infer a binary label for each instance, and identify the most frequent label among the full instance set. The correct answer should be invariant to instance order. By evaluating fifteen LLMs across five datasets and seven instance order patterns, with each instance set held fixed across patterns, we find substantial order sensitivity. Accuracy can differ by about 90 percentage points between the best and worst order patterns, with models generally more accurate when majority-label instances appear at the start than when they appear in the middle or at the end. For subsets of models, available reasoning traces and gradient-based attribution reveal uneven emphasis across positions. Traces disproportionately mention early instances, while attribution scores are generally higher near the beginning and end than in the middle. These results show that instance order can systematically bias aggregated predictions, highlighting the need to evaluate MIP across different input arrangements.

---


### 59. [The Price of Choice in Selective Prediction](https://arxiv.org/abs/2610.29067)

**<font color=#1a73e8>作者：</font>** Daniel Cieślak, Andrzej Czyżewski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A selective classifier may be claimed to satisfy a risk-coverage contract if some rule from a predeclared menu (a threshold or a union of $K$ score intervals) attains coverage at least $\kappa$ and error at most $\alpha$. Refuting this existential claim requires ruling out every permitted rule. The intersection-union test (IUT) achieves validity without a multiplicity correction, but its sample cost can increase with menu richness. We characterize this cost and compare it with the optimal audit. For a fixed interior risk target $\alpha$ and gap $\gamma$, the minimax sample size for K-interval menus at coverage floor $\kappa$ is $K(1-\kappa)/(\kappa\gamma^2)$, up to logarithmic factors, in the stated small-gap, large-menu regime; exact IUT attains this rate. The lower bound holds even with a known score distribution, while the upper bound extends to menus of VC dimension $d$. Procedures that refuse to reject whenever any rule appears feasible on the audit sample can pay a linear $K$ cost even when a square-root rate is possible. Reference-free testing reaches a smaller scale under constant-risk alternatives, whereas unknown heterogeneous risks can make the linear cost unavoidable. In simulations with $K=4$, the raw menu cost varies 7.7-fold between $\kappa=.5$ and $\kappa=.95$; after theorem-motivated normalization the endpoint values differ by approximately 5%. Held-out experiments with three VLM judges show positive exact-hiding windows in all 60 split-specific confidence-gate families, with 28/30 contracts chosen on audit-A remaining hidden on untouched audit-B. On a cleaner multi-annotator target, hiding is weaker and transfers in 3/10 resplits. Frozen image and multimodal classifiers show boundary behavior consistent with the IUT guarantee and strong power relative to practical certificates.

---


### 60. [A Large-Scale Evaluation of Role-Enhanced Zero-Shot Chain-of-Thought Prompting](https://arxiv.org/abs/2610.29073)

**<font color=#1a73e8>作者：</font>** Ibrahim Khan, Thai Van Nguyen, Yi Xia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper proposes Role-Enhanced Zero-Shot Chain-of-Thought (RE-ZS-CoT), a prompting framework that systematically integrates domain-specific expert roles to enhance reasoning in large language models (LLMs) without task-specific examples. We assess two versions of our approach. In the first version, static role selection, we evaluate eight predefined expert roles across arithmetic, commonsense, and reading comprehension benchmarks to determine their impact on reasoning performance. In the second version, dynamic role selection, each model autonomously selects the single most suitable role for each benchmark, enabling adaptive task-role alignment without manual specification. Across 20 LLMs and seven benchmarks, RE-ZS-CoT frequently surpasses zero-shot and zero-shot-CoT baselines, achieving performance improvements of up to 44 percentage points. The results reveal a strong correspondence between static and dynamic versions; the benchmarks where static roles yielded improvements were almost always those where dynamic roles also outperformed baselines, though static selection achieved peak performance. Ablation studies further show that unconventional roles degrade performance, underscoring the necessity of task-role alignment. The framework's scalability is validated across model sizes (2b-14b parameters), with smaller models like Granite3.3-8b achieving remarkable proficiency in arithmetic reasoning. RE-ZS-CoT advances zero-shot prompting by unifying role specialization with chain-of-thought reasoning, offering a practical, resource-efficient solution for improving LLM capabilities across diverse domains.

---


### 61. [Same Answer, Different Reasons: Trace-Level Divergence in Multilingual Large Language Models](https://arxiv.org/abs/2610.29092)

**<font color=#1a73e8>作者：</font>** Rui Sun, Peizhao Mei, Xiewei Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multilingual large language models are increasingly deployed in settings where visible reasoning traces support verification, education, and safety auditing, yet standard evaluations typically measure only final-answer agreement or holistic response similarity. As a result, they establish outcome consistency without determining whether users across languages receive comparable supporting evidence. We introduce a trace-level divergence framework that compares visible reasoning traces as structured sequences, decomposing agreement into structural similarity, order consistency, and holistic similarity, with pair-specific calibration to enable comparison across languages. Across three reasoning benchmarks, seven languages, and six frontier LLMs, the natural baseline---embedding each whole response and comparing the two by cosine---systematically overstates agreement: $52.1\%$--$67.3\%$ of examples in the top quartile of holistic similarity are not in the top quartile of structural similarity. This dissociation is stable across sentence encoders and step segmentations, and blind bilingual annotation studies in two English-anchored language pairs show that human judgments align with structural similarity rather than with the holistic baseline. A same-language control shows that the level of divergence is language-specific: two English traces for paraphrases of the same question agree more closely than an English trace and its counterparts in other languages. Our results show that answer-level and holistic evaluations can substantially overestimate the consistency of multilingual explanatory artifacts, motivating trace-level evaluation for reliable multilingual deployment.

---


### 62. [WaFIR: Wavelet-Fourier Mixture-of-Experts with Subband-Adaptive Routing for Blind All-in-One Image Restoration](https://arxiv.org/abs/2610.29108)

**<font color=#1a73e8>作者：</font>** Trong Nhan Nguyen, Vu Hoang Minh Doan, Thanh Dat Le 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blind all-in-one image restoration must adapt a shared model to heterogeneous and sometimes mixed degradations without a task label at test time. We introduce WaFIR, a decoder module that decomposes features into Haar subbands, summarizes each subband with a compact Fourier descriptor, and routes it to prompt-conditioned spectral modulation experts. Unlike image-level frequency conditioning, WaFIR makes routing decisions at the subband level, enabling frequency-specific processing while retaining the task context learned by the backbone. Under a unified training and evaluation protocol for denoising, deraining, and dehazing, WaFIR improves average PSNR over the three tasks by 0.48 dB over the PromptIR baseline and by 0.38 dB over the recent Up-Restorer. Matched-capacity and routing controls show that the gain is not explained by additional parameters alone. On unseen noise intensities, descriptor-based routing is more robust than a discrete label-conditioned alternative and remains on par under compound degradations, while routing analyses show stable subband-dependent expert use across degradation types. These results support subband frequency structure as an interpretable complement to prompt-based conditioning for blind image restoration. Code is available at this https URL

---


### 63. [GRAM: Group-wise Rank-Aware Model Merging via Subspace Alignment](https://arxiv.org/abs/2610.29110)

**<font color=#1a73e8>作者：</font>** Di Wu, Shuaidong Pan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Merging different models into a single model is highly desirable for multi-task deployment, particularly in regulated domains like healthcare. In such settings, models are often locally fine-tuned due to strict data privacy policies, necessitating that aggregation operates exclusively on the fine-tuned weights. Existing methods apply a uniform merge across all tasks, ignoring the geometric relationships among their learned subspaces. When task updates occupy misaligned subspaces, projecting them onto a shared low-rank basis discards task-relevant directions, a failure mode named \emph{subspace interference}. Through this study, we show that the per-task projection error of a merged model is governed by the principal-angle alignment between each task and the shared subspace, so that grouping geometrically compatible tasks provably reduces this error within each group. Motivated by this observation, we propose \textbf{Group-wise Rank-Aware Model Merging (GRAM)}, which uses the principal-angle geometry of task vectors to decide which tasks should be merged together and then performs a standard SVD-based merge within each coalition; the pipeline requires only the fine-tuned weights at merge time. With only one additional model ($\nK{=}2$), GRAM significantly mitigates subspace interference and consistently outperforms prior merging methods across language understanding (GLUE with Flan-T5), 8-task CLIP vision, and medical instruction tuning (Qwen2-7B-Instruct with four English/Chinese medical LoRAs).

---


### 64. [Recursive Self-Improvement on a Budget: Scoring Code Edits Before They Run](https://arxiv.org/abs/2610.29121)

**<font color=#1a73e8>作者：</font>** Erfan Darzi, Sree Bhargavi Balija, Sheng He  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A coding agent that rewrites its own scaffold has to choose which proposed edit to expand before that edit has been evaluated, and the search then has to return one agent. Each run fits one linear readout on the parent's steering-split solve rate and eight coordinates of the proposed diff, from 96 scaffold edits labeled by four evaluations of a 16-instance fit split, and then freezes the coefficients. HumanEval+ reserves 48 instances as the steering split and Polyglot reserves 64. That split scores parents and keeps an archive of four nodes. Huxley-Gödel Machine selection draws a parent by Thompson sampling on the steering counts of nodes that have already been evaluated, and it expands the child that parent proposes. Every method then returns the earliest evaluated node whose steering-split solve count is maximal. The tables report the held-out score of that node on the other 100 HumanEval+ instances and the other 145 Polyglot instances, next to the root scaffold and the calibration edit with the highest fit-split label. Twelve runs of GPT-4o return a node at 87.0% on held-out HumanEval+, against 84.2% for the parent-rate ablation. On that split Huxley-Gödel Machine selection returns 85.1%, the root is at 81.2%, and the calibration-best edit is at 82.8%. On the same split Claude Sonnet 4.5 returns 86.6%, beside 86.5% for Huxley-Gödel Machine selection, 85.3% for the parent-rate ablation, and 85.1% for the calibration-best edit.

---


### 65. [StochIKM: Automated High-Fidelity Reconstruction of Individual Patient Data from Published Kaplan-Meier Curves](https://arxiv.org/abs/2610.29122)

**<font color=#1a73e8>作者：</font>** Liangze Ke, Daniel Zelterman, Wei Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Individual patient data are the gold standard for secondary analysis of time-to-event evidence, but they are rarely released, and reconstruction from a published Kaplan-Meier figure could help. Existing methods all claim high fidelity, each judged by whichever agreements it happens to achieve, and each returns a single dataset although the map from figure to data is not bijective. We define fidelity explicitly: a dataset is admissible when it reproduces the risk table exactly, follows the digitized curve to within the image resolution, and respects the printed median, interval and event count. We propose StochIKM, a stochastic algorithm that digitizes the figure with a vision-capable language model and uses the high-fidelity definition as constraints, returning an admissible set of individual patient datasets. A solution is guaranteed to exist whenever the figure has been read correctly, so a failure indicts either the published figure or its digitization. In simulation and in 79 arms from published oncology trials, StochIKM reproduces the published risk tables and medians more closely than LLM-improved IPDfromKM, a high-impact alternative.

---


### 66. [GRAFT: Restoring the Missing Sampling Interface in Continuous Diffusion Language Models](https://arxiv.org/abs/2610.29136)

**<font color=#1a73e8>作者：</font>** Haoning Yang, Lili Pan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion language models generate a whole sequence in parallel, never drawing a single word at any intermediate step; only the final step turns embeddings into text. Models such as ELF now report autoregressive-level quality at a fraction of the sampling steps of discrete-token diffusion models, and this design principle -- no step-wise discretization -- is what their own ablations credit for the gain. We show that this same principle carries a hidden cost: a collapse of the lexical long tail. Measured against held-out human text, ELF's output matches the human rate on common words almost exactly, yet its rarest words appear at only 0.30x the human rate, a gap that does not close from 105M to 652M parameters and that no sampler setting these models expose can reach. A same-size GPT-2, in contrast, spans zero to above the human rate by its decoding rule alone. We trace the difference to what continuous diffusion models lack: with no step that ever draws a discrete word, every step is instead driven by an average over the candidates still in play, and averaging a rare candidate together with the common word competing for its slot lands on the common word. An autoregressive model avoids this because its decoding rule samples one candidate rather than averaging over all of them. We propose GRAFT, a training-free method that grafts this missing choice back onto a frozen model: while the model is still undecided, GRAFT commits the rare words the average would otherwise discard, then regenerates the sequence from scratch with those commitments held in place. Across three ELF scales and on LangFlow, an independent continuous dLLM, GRAFT restores the rare-word share of generated text from 0.42-0.77x the human rate to 0.82-1.10x, a relative gain of 34-109%, and moves the entire word-frequency profile closer to human on every model tested, by 2.7x on ELF-B and 12x on LangFlow.

---


### 67. [Steering Black-Box Large Language Model Agents with Pitfall Anticipation World Model](https://arxiv.org/abs/2610.29139)

**<font color=#1a73e8>作者：</font>** Jiongxiao Wang, Han Ding, Youzhi Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier black-box Large Language Model (LLM) agents are proficient at long-horizon reasoning and precise action generation. However, when it comes to a specific agentic task, they have no internalized knowledge of how that particular environment unfolds. A world model offers a natural remedy, providing the agent with environment specific knowledge by foreseeing how the environment will respond to the action it is about to take. Prior world models for LLM agents mainly predict next observations at each step, which is costly and often uninformative because individual observations provide limited task-relevant guidance and not every step requires call for foresight. This raises a key question: what a world model should predict and when should it be invoked for agentic tasks? Our pilot study suggests that world model guidance is most useful when it anticipates pitfalls within a bounded multi-step future. Motivated by this, we introduce Pitfall Anticipation World Model (PAWM), which selectively intervenes when a potential pitfall arises and predicts the impending failure to steer the agent away from it. PAWM is trained in two stages: Supervised Fine-Tuning (SFT) on synthetic data labeled with agent pitfalls, followed by GRPO co-training with a black-box LLM to further optimize it in the target environment. PAWM improves Claude Sonnet 4.5 performance by 24.3% on ScienceWorld and 7.7% on WebArena-Lite, outperforming a range of baselines. These results demonstrate that PAWM provides an effective form of world model guidance for black-box LLM agents.

---


### 68. [From AI-Free Gates to AI-First Work: How Engineering Students in India Navigate University Education and Campus Placements Without AI Guidelines](https://arxiv.org/abs/2610.29140)

**<font color=#1a73e8>作者：</font>** Samhitha Goutham, Ziwei Gu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Engineering graduates in India enter a technology sector that is being reshaped by generative AI, yet the route into that sector runs through examinations and campus placement screens that largely exclude AI. Institutions in India have an approved intake of nearly 2.9 million seats in engineering and technology for 2026-2027, but HCI research on how students prepare for AI-mediated work has drawn mostly on Western and East Asian settings. We interviewed 23 students and recent graduates of Indian engineering and computing programmes about how they used generative AI across coursework, examinations and placements, and how they judged their own readiness for work. Using reflexive thematic analysis, we report five themes, covering AI-first workplaces and AI-free placement screens, how participants prepared for placement, how they used AI in coursework, the role of faculty authority and enforcement, and participants' concerns about their readiness for work. Drawing on signaling theory, we discuss what grades and screen scores certify once AI can help produce them, and we offer recommendations for employers, institutions and AI tool designers.

---


### 69. [From Augmentation to Synthetic Evidence: Evaluating Generated Chest Radiographs at Dataset Intake](https://arxiv.org/abs/2610.29152)

**<font color=#1a73e8>作者：</font>** Shaikh Akib Shahriyar, Zinedine Sehili, Adam Arthur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A generated chest radiograph can be useful as declared augmentation, but the same image becomes unsupported evidence when submitted as the record of a real examination. We study this problem by separating three questions: whether an image passes an automated quality check, whether an origin classifier flags it as generated, and whether a trusted record supports the claimed acquisition. In our experiments, Qwen selects up to 20 images from pools of 1,000 existing Cheff-identified or SynthCheX candidates. A receiver evaluates quality with MedGemma and predicted origin with a classifier on frozen DINOv3 features. Quality-based selection raises quality passes from 12 to 19 of 20 for Cheff-identified images and from 8 to 17 for SynthCheX. We find no evidence that selection improves passage through both checks: no selected Cheff-identified image passes both, while uniform, quality, and quality-constrained surrogate selection produce 2, 1, and 2 SynthCheX passes. On unprocessed test images, the origin classifier flags 4,677 of 5,000 SynthCheX images, but it also misclassify 110 of 2,297 NIH (real) images and 568 of 957 genuine images from another collection as fake. Our results further show that JPEG compression reduces SynthCheX-versus-NIH AUROC from 0.987 to 0.841. Even without processing, 152 SynthCheX images pass both pixel checks. These checks can filter submissions, but they cannot verify an acquisition claim. We strongly advocate that source and intended use must be recorded and checked separately for admission of chest radiographs in medical datasets.

---


### 70. [Why is AI-generated language so hard to understand?](https://arxiv.org/abs/2610.29162)

**<font color=#1a73e8>作者：</font>** Thomas Hikaru Clark, Matias B. Martin, Kyle Mahowald  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There is a widespread sense that AI-generated text has recently become harder to understand. In this study, we investigate a set of psycholinguistic features that are known to correlate with human processing difficulty (e.g., object relative clauses, long syntactic dependencies, low-frequency n-grams). Using a novel corpus of AI-generated text across diverse domains, we find that AI models use these difficult features more often than paraphrases generated by round-trip translation. Compared with human writing, all nine frontier and near-frontier models use more inanimate subjects with animate verbs and more low-frequency n-grams, and most also use longer dependencies, more stacked nouns, and more reduced object relatives in conversation; we also demonstrate substantial variation across model families. We propose and test a hypothesis as to why: while human language is optimized for successful communication, AI-generated text is increasingly optimized for other goals like math, code, and reasoning, in which there is a pressure for \textit{information density} rather than successful communication. We provide a proof-of-concept for this hypothesis by fine-tuning a language model under a length penalty, which leads to a divergence from human-like linguistic behavior. Our findings highlight the axes of misalignment between linguistic processing demands in humans and LLMs, and point toward possible remedies.

---


### 71. [TeachBack: Learning to Teach via Bidirectional Preference Optimization for On-Policy Self-Distillation](https://arxiv.org/abs/2610.29167)

**<font color=#1a73e8>作者：</font>** Linfei Ji, Jiayun Li, Haozhao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) enables a language model to learn from a Teacher instantiated from the same model but given access to privileged information, such as a reference solution. We find that access to sufficient privileged information allows the Teacher to generate highly accurate trajectories; however, accuracy alone does not guarantee that these trajectories are suitable for Student learning. Direct access to a complete solution may encourage shortened, reference-conditioned derivations that omit the exploration, verification, and self-correction required to solve problems without privileged information. We introduce TeachBack, a bidirectional preference-learning framework for on-policy self-distillation that learns not only from the Teacher but also how the Teacher should teach. TeachBack shapes the Teacher's generation behavior by controlling the length of the reference-reasoning suffix injected into the prompt and by varying the prompt style. While maintaining comparable Teacher accuracy, it encourages the Teacher to explore and re-solve problems, thereby reducing its reliance on the reference solution. At each rollout refresh, the shared policy generates both a privileged Teacher trajectory and a problem-only Student trajectory. A pairwise preference objective uses privileged Teacher trajectories to improve Student learning, while the reversed preference uses the Student's behavior to shape future Teacher supervision under the privileged condition. Experiments on mathematical and logical reasoning tasks show that TeachBack consistently improves Student performance over existing OPSD methods and related baselines.

---


### 72. [TrainBridge: Agentic NPU Training Optimization Guided by GPU Compilation Evidence](https://arxiv.org/abs/2610.29171)

**<font color=#1a73e8>作者：</font>** Yupeng Chen, Kunxiang Zhao, Xingjian Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study how to improve training efficiency on Ascend NPUs. In the NPU training programs we study, framework-level compilation optimizations such as operator fusion are only partially applied, leaving fragmented computation and avoidable execution overheads. Profiling-guided tuning can address these inefficiencies, but it often requires costly trial and error. To make training on NPUs more efficient, we propose TrainBridge, an agentic approach for transferring GPU optimization guidance to NPU training. TrainBridge uses the highly optimized execution produced by mature GPU compilation stacks as a task-specific reference for NPU tuning. It extracts optimization intents from the GPU training execution to guide NPU program rewrites and further refines the rewritten program through iterative profiling. Our GPU-to-NPU migration experiments show that TrainBridge achieves an average 1.7x speedup across four workloads covering LLM pretraining, image classification, and vision-language training, and an average speedup of nearly 2.0x across 27 Modded-NanoGPT speedrun records with highly optimized GPU implementations.

---


### 73. [LocalAgent: Collaborative Agentic Verification for Fine-Grained Instance-Level Consistency](https://arxiv.org/abs/2610.29174)

**<font color=#1a73e8>作者：</font>** Jiachen Guo, Xinshan Zhu, Boyun Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have made rapid progress in general visual understanding, yet they still struggle with fine-grained instance-level consistency verification, where the goal is to determine whether two images depict the exact same physical object under varying viewpoints, illumination, and backgrounds. This task requires both global semantic perception and precise examination of subtle local evidence, since semantically similar objects may differ only in small suspicious regions. To address this challenge, we propose LocalAgent, a collaborative agentic framework that integrates the complementary strengths of a generalist MLLM and lightweight specialist verifiers. The MLLM first reasons globally to identify suspicious local regions, which are then delegated to a Local Evidence Verifier (LEV) toolkit for fine-grained appearance and geometric matching. LEV comprises Local Appearance Consistency (LAC), which estimates appearance similarity under illumination and color changes, and Local Geometric Correspondence (LGC), which estimates spatial correspondence under viewpoint changes. LEV returns structured scalar evidence that the MLLM integrates for the final decision. We further introduce an auxiliary-capped reinforcement fine-tuning (RFT) strategy, in which answer correctness dominates auxiliary tool-use and format signals, enabling the policy to learn when verification is necessary. Experiments show that LocalAgent improves mean accuracy by 4.9% over the strongest CoT-RFT baseline while invoking a verifier on only 12.13% of samples and preserving the general multimodal capabilities of the underlying MLLM. The open-source repository is available at this https URL.

---


### 74. [Correlated Failures of AI Approval Monitors](https://arxiv.org/abs/2610.29178)

**<font color=#1a73e8>作者：</font>** Luca Zanolini  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Before an AI agent takes a consequential action, such as paying, messaging or changing code, several monitors check it. Their verdicts are combined by aggregating scores or by counting approvals, whatever inputs the monitors share. Monitors that share a base model or a poisoned input, however, may fail together. We borrow the fail-prone systems of distributed computing: lists of monitor sets that may fail together. A rule is safe if it executes no bad action and live if it blocks no good one. We measured twelve small open-weights monitors on payment approval under two pre-registered protocols. Without pre-registration, we also measured three closed frontier models (Claude Opus 5.5, GPT-6 Astra, Gemini 4 Argon) and the open DeepSeek-V3.2. Every reliable fooling of a monitor into approving a fraud came through an evidence source and reached only that source's readers. Fooling it into blocking a correct payment depended on injection resistance, a monitor's refusal to follow instructions planted in its data. Small models and DeepSeek obeyed such notes. The three closed models ignored them in all but one case, and Opus also resisted persuasion tailored to it. On new data, a rule that counts sources instead of votes blocked 0.9% of correct payments, against 7.4% for the best counting rule, at equal safety. The pre-registered worst-case test failed. One attack left the approvers on a single source, so no rule over the twelve language-model monitors survives every measured attack. Adding a rule engine, which cannot be persuaded, restored the condition for a safe and live rule on the measured attacks. Diversify the inputs, harden the monitors, count sources, not votes.

---


### 75. [LTEM: LLM-Friendly Table-Enhanced Markdown for Table Understanding and Generation](https://arxiv.org/abs/2610.29188)

**<font color=#1a73e8>作者：</font>** Eunbin Kim, Hyeonseok Kang, Sangkeun Jung  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tables in real-world documents, including scientific papers, financial reports, and statistical summaries, frequently use merged cells, multi-level headers, and sectioned layouts. Yet the lightweight formats LLMs handle best (Markdown, CSV) cannot express these structures, while expressive formats (HTML, LaTeX) impose excessive token cost and parsing complexity. To enable systematic analysis of this trade-off, we introduce a taxonomy decomposing table structure into six atomic features (F1-F6) and corresponding complexity levels (L1-L6), and construct STB (Synthetic Table Benchmark), a controlled benchmark with 1,089 tables systematically distributed across complexity levels. Using this framework, we propose LTEM (LLM-friendly Table-Enhanced Markdown), a formally specified, minimal extension of Markdown that explicitly encodes spans and hierarchical headers. Experiments across five state-of-the-art LLMs show that LTEM achieves accuracy comparable to HTML, offers a favorable accuracy-token trade-off relative to HTML and LaTeX, and produces substantially fewer invalid responses than LaTeX; for table generation, LTEM is comparable to MultiMarkdown though HTML is best. We release our taxonomy, benchmark, and format specification to support future research on LLM-table interaction.

---


### 76. [A Unified Evaluation Framework of Physical Adversarial Robustness in the Edge VLM Era](https://arxiv.org/abs/2610.29196)

**<font color=#1a73e8>作者：</font>** Eric Liang, Alan Luo, Kaiwen Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Vision-Language Models (VLMs) enable end-to-end visual grounding via language prompts and generative decoding, demonstrating largely improved zero-shot and open-vocabulary detection capabilities. As a result, VLMs are rapidly being deployed at the edge in safety-critical real-world systems. However, the physical adversarial robustness of edge VLMs has not been systematically studied, and the fundamental differences in output with modern object detectors create methodological challenges for fair evaluation. To compare the two families directly, we evaluate every selected representative model on one outcome: whether an adversarial patch worn on a person evades detection of the model. We report this by introducing a unified metric, conditional attack success rate (cASR), counted only on images the model still localizes under a matched gray occluder, and partition every failure into omission (no box), substitution (a box on the patch), and displacement (a box on neither). We benchmark the physical adversarial vulnerability of compact grounding VLMs against a range of object detectors, and find that the VLMs can be as vulnerable as the detectors. We disclose that failure mode is largely associated with the output format of a model rather than its architecture family. Of the three, only omission is visible to a downstream system; displacement and substitution return confident, well-formed boxes, making them potentially more dangerous failures. Further, we find that, under distribution shift, VLMs that primarily failed by omission instead shift to failing more by displacement/substitution. Thus, a grounding VLM can inherit the detector's vulnerability while showing the possibility to adopt more dangerous failure modes. Our code and data are available at this https URL.

---


### 77. [norregel: a preregistered benchmark of dated numeric values in Norwegian law](https://arxiv.org/abs/2610.29207)

**<font color=#1a73e8>作者：</font>** Eirik Botten Nicolaysen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> norregel asks language models for numeric values in Norwegian statutes, regulations and parliamentary decisions (NOK amounts, percentages, multiples of the National Insurance basic amount (G) and age limits), each at a stated date. The 916 items were extracted mechanically from Lovdata's open data, and each carries the dated history of its provision, so an answer can be classed as correct, outdated, wrong or uninterpretable. We report a first and a second preregistered run on the same items. In the first run (five models, listed publicly only after local analysis), H1, that outdated answers are more frequent for values that took effect after a model's cutoff, could not be tested in substance, and H2 and H3 were inconclusive; Opus 5.5 and Sonnet 4.6 answered 46.7% and 40.2% of the 880 primary items correctly. The second run was preregistered and published before any of its calls, and eight models were analysed. Its pooled primary test supported H1 under the preregistered decision rule (d = 17.8 percentage points, 95% interval [7.7, 28.9], p = 0.0001). In the preregistered sensitivity analysis S8, which counts as outdated only the most recent value that differs from the key, d was 3.9 [-3.6, 12.7] (p = 0.1754), an interval that contains 0. H1 was supported in every other preregistered sensitivity analysis, but S8 is the only one that gives both groups one target value, so we do not regard the support for H1 as robust. The share of outdated answers equal to that most recent value (H2) was 56.1% [46.6, 65.0], an interval that contains 0.5, and the pooled test of a lower share correct in Nynorsk than in Bokmål (H3) was inconclusive. Several models, among them Haiku 4.5, gave mostly uninterpretable answers. Items and keys are withheld; item IDs, per-answer classes, code and results are on Zenodo.

---


### 78. [When Multiple Choices Are Correct: Asymmetric Probability Allocation in Jev and Other Decision Models](https://arxiv.org/abs/2610.29217)

**<font color=#1a73e8>作者：</font>** Rushab Munot  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision models return normalized probability distributions over candidate choices, which downstream applications can use to select among choices. Although their providers emphasize the reliability of these probabilities, calibration on tasks with a single correct choice does not establish their reliability when multiple choices are correct. We evaluate three decision models (Jev, Liquid d1, and GPT-6 Luna Decisions) on three diverse datasets (MetaTool, HotpotQA, and ECtHR) to study probability allocation and thresholding. Even when models rank every correct choice above every distractor, in 28% to 50% of those lists, at least one correct choice receives a probability below the uniform probability of 1/n, where n is the number of choices. We also present each model with five identical copies of a correct choice and observe probability disparities, with mean gaps ranging from 17 to 79 percentage points. We further show how these allocation disparities affect the recovery of multiple correct choices under probability thresholding. Decision-model probabilities can rank correct choices, but a probability threshold does not identify the set of correct choices.

---


### 79. [C$^2$U in RAG: Compositional Concept Unlearning in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.29223)

**<font color=#1a73e8>作者：</font>** Yiyang Duan, Fan Wu, Tiantong Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation can expose unwanted concepts through retrieved evidence even when the generator is moderated. We study query-side concept suppression with a fixed encoder and document index. Compositional Concept Unlearning (C$^2$U) routes a profile-derived direction through an augmented atom bank, adding only a bounded edited-minus-original delta to the raw query. Across five datasets, four encoders, and three seeds, the validation-selected configuration reduces pooled binary target Hit@5 by 4.25 percentage points with non-positive control degradation and target-exposure changes. Under the evaluated query transforms, it suppresses target density without increasing budgeted control-query exposure. Separately, ArXiv four-concept composition improves over an averaged-direction comparator after independent validation gates and first-use test evaluation.

---


### 80. [Cache Locally, Recompute Selectively for Streaming Video Understanding](https://arxiv.org/abs/2610.29229)

**<font color=#1a73e8>作者：</font>** Junhyeok Lee, Sangyoon Lee, Jaeho Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding (SVU) requires video-LLMs to process incoming video continuously while answering user queries with low latency. Recent methods reduce query-time cost by prefilling frames into KV caches during idle time and reusing the cached KVs at query time. To bound per-frame computation over unbounded video streams, these methods restrict the context available during prefill. This creates a fundamental context mismatch: the restricted context may omit information needed to properly contextualize video tokens, yet, still contain information irrelevant to the eventual query, which is unknown during prefill. We propose FrameBlend, a simple yet effective plug-and-play method to address this mismatch through selective KV recomputation, without requiring any additional training. At query time, FrameBlend re-prefills selected video tokens using query-relevant context and replaces their cached KVs with recomputed ones. Crucially, this recomputation enables shorter attention windows during idle-time prefill, substantially reducing prefill cost while improving accuracy. Experiments across three SVU frameworks and five streaming and offline benchmarks demonstrate accuracy gains of up to 3.9 pp. On RVS-Ego, FrameBlend reduces per-frame prefill FLOPs by over 20% and total processing time by 14-59% for retrieval-based frameworks, including the cost of query-time recomputation. These results demonstrate that a simple change in how contextualization is distributed between idle time and query time can improve the accuracy-efficiency trade-off for SVU.

---


### 81. [DisasterRoute: Evidence-Guided Dual-System Routing for Visual Disaster Question Answering](https://arxiv.org/abs/2610.29231)

**<font color=#1a73e8>作者：</font>** Tan Zhang, Xing Deng, Lu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual question answering from low-altitude UAV imagery must deliver timely and accurate judgments to support disaster response under limited edge computing resources. Routine questions may be answered through direct decisions, whereas more challenging questions may benefit from step-by-step reasoning. However, existing research primarily focuses on improving models' visual understanding and generative reasoning capabilities, with limited exploration of efficient direct decision-making and its adaptive coordination with generative reasoning. We develop Disaster-S1 based on a vision-language model adapted to the disaster domain. Trained for option discrimination, it outputs a probability distribution over answer options in a single multimodal forward pass for fast decision-making. We further propose DisasterRoute, a dual-system routing framework that combines prediction confidence with disaster evidence to decide whether to accept the initial answer or invoke the disaster reasoning model DisasterVL for review. By allocating inference computation on demand, the framework retains the efficiency of direct decision-making and improves overall question-answering accuracy through selective review. Experiments on DisasterBench show that Disaster-S1 achieves superior accuracy with low latency, while DisasterRoute further improves accuracy through selective review at substantially lower latency than full reasoning.

---


### 82. [Think-Capture: Active 3D Geometry Acquisition for Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.29232)

**<font color=#1a73e8>作者：</font>** Junjie Wang, Zhihao Yuan, Yunhan Tang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) excel at 2D recognition but often fail to maintain consistent 3D relations across sparse viewpoints, leading to spatial hallucinations under occlusion and perspective changes. Existing methods commonly fuse all frames with dense geometry, incurring substantial computation and context overhead while encouraging blind reliance on imperfect estimators. We present Think-Capture, a query-conditioned framework that first identifies task-critical objects and then acquires their geometry on demand. A 3D toolkit lifts zero-shot masks into a common coordinate frame, and a Symbolic 3D State Abstraction compresses object and camera states into structured text. Hierarchical Group Relative Policy Optimization (GRPO) trains the VLM on cases in which geometry either helps or misleads, teaching it when to use tool evidence and when to fall back on visual cues. Think-Capture-4B reaches 54.4% on MindCube-Tiny (+21.5 points over its backbone), 39.1% on the MMSI-Bench positional subset (+7.9), and 42.8% on ViewSpatial (+5.2). It also remains robust under coordinate and mask perturbations. The full stack fits one 24 GB GPU and serves as an asynchronous high-level reasoner on an Agibot G1. Our code is available at this https URL.

---


### 83. [Encoded but Unused: Bounding the Sources of VLM Errors](https://arxiv.org/abs/2610.29241)

**<font color=#1a73e8>作者：</font>** Anat Veikherman, Mor Ventura, Nitay Calderon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we investigate why vision-language models (VLMs) produce errors by decomposing them into two sources: visual-representation failures, in which the visual evidence required for the correct answer is not encoded, and visual-utilization failures, in which this evidence is encoded but not successfully used. We propose to estimate the visual-utilization failure rate using lightweight probes and derive theoretical bounds on the true rate that account for probe imperfections. We introduce VELens (Visual Evidence Lens), a rank-based probe that traces visual evidence for both a target object and its ground-truth attribute, such as color, material, or shape, across VLM layers. We evaluate VELens on over 6,000 images using LLaVA-1.6-7B and Qwen2.5-VL-7B. Our method achieves ROC-AUC scores of 0.95 and 0.91, respectively, and outperforms alternative probes in both low-resource and unseen-attribute settings. Using it to diagnose errors, we estimate that visual-utilization failures account for 84.4% of LLaVA errors and 70.0% of Qwen errors, with conservative lower bounds of 77.5% and 61.0%, respectively. Overall, our study identifies visual utilization as the dominant bottleneck in VLMs and suggests that a central opportunity for improvement lies in developing better mechanisms to locate, route, and use the visual information they already encode.

---


### 84. [Failure Modes of Vision-Language Models for Human Activity Understanding in Thermal HRI](https://arxiv.org/abs/2610.29244)

**<font color=#1a73e8>作者：</font>** Han Hu, He Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal cameras enable robots to perceive human activities in darkness while revealing less personally identifiable appearance information and fewer details of the surrounding environment than RGB cameras. As vision-language models (VLMs), originally developed for RGB imagery, are increasingly integrated into embodied systems for scene understanding and high-level planning, thermal sensing offers a promising way to extend activity perception to low-light and privacy-sensitive settings. However, the failure modes of VLMs in thermal human activity understanding for human-robot interaction (HRI) remain underexplored. We fill this gap by evaluating seven locally deployable VLMs, including models developed for physical AI and robotics, on two person-centric thermal datasets. Our diagnostic tasks examine fine-grained action recognition, activity timeline reconstruction, and the ability to withhold unsupported answers. Paired RGB recordings serve as a performance reference, while controlled variations in frame sampling, thermal input presentation, and reasoning are used to assess whether the observed errors can be mitigated. Our results show that models can recognize broad activity categories but struggle with fine-grained actions such as coughing, sneezing, and yawning. They also produce inaccurate event timelines and hallucinate actions involving objects. Simple thermal input preprocessing and additional reasoning offer only limited, model-dependent gains. Abstention behavior also varies across models even under explicit instructions, limiting their reliability for practical robotic use.

---


### 85. [CrashGym: Measuring the Decision Value of Experimentation for LLM Agents in Counterfactual Market Crashes](https://arxiv.org/abs/2610.29245)

**<font color=#1a73e8>作者：</font>** Haocheng Lu, Haoxuan Cheng, Mingyang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents are increasingly asked to run experiments, yet benchmarks rarely measure whether those experiments improve the decisions they are meant to inform. We introduce CrashGym, a deterministic, replayable limit-order-book simulator in which an agent must choose between a deleveraging intervention and a liquidity backstop for a market about to suffer a shock-triggered crash. Before committing, the agent may query intervention experiments in a laboratory realization of the market. Its choice is then scored on an independently seeded target realization in which the simulator executes every feasible intervention, so regret relative to the best intervention is computed by directly simulating every alternative on the same target repeats, with no human or model-based judging. The simulator implements each amplification channel---persistent price impact, liquidity withdrawal, margin-driven liquidation, and an evolving strategy mix---as an explicit mechanism that can be switched on in stages. In a prospectively specified study on 24 newly sampled worlds, laboratory access reduces the mean regret of the one deployment with a complete record (Luna) from 8.878 to 3.785, a paired reduction of 5.092 utility units (nominal 95% world-bootstrap interval: 1.028--9.507), or 57.4% of the OBSERVE-ONLY mean. Prospective comparisons for two further deployments are incomplete; in a separate exploratory study, mean regret is lower with laboratory access for all four deployments evaluated. A laboratory whose strategy mix evolves endogenously yields no established advantage over one with a fixed mix. CrashGym thus measures the value of experimentation as avoided decision loss and lets simulator detail be judged by the decisions it supports.

---


### 86. [Let Agents Design How They Search: Automatic Interface Optimization for Agentic Search](https://arxiv.org/abs/2610.29250)

**<font color=#1a73e8>作者：</font>** Sangjune An, Jaeyoon Jung, Yumin Choi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic search depends on the interface through which a language-model agent accesses and explores a corpus. Existing interface designs are fixed by hand and applied unchanged to every corpus, although effective designs may depend on the corpus. We introduce SearchWeaver, a framework for automatic search interface optimization guided by downstream search performance. A proposer uses execution trajectories and task rewards to jointly revise corpus artifacts, executable tools, and usage instructions. This pro cess optimizes what information is prepared in advance, which operations tools perform, and which decisions remain with the search agent. With GPT-5.4-nano, the optimized interfaces improve answer accuracy from 71.6% to 78.4% on BrowseComp-Plus and average nDCG@10 from 45.7 to 55.0 across four BRIGHT subsets over Direct Corpus Interaction. These findings highlight the value of jointly optimizing corpus artifacts, executable tools, and usage instructions to develop effective search interfaces.

---


### 87. [Intergroup Bias Predicts Expressions of Social Judgment and Empathy in the r/AmITheAsshole Reddit Community](https://arxiv.org/abs/2610.29254)

**<font color=#1a73e8>作者：</font>** Yu Hou, Hal Daumé III, Rachel Rudinger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> People share and understand others' experiences differently based on their social identities; often, people empathize more when the other person belongs to their ingroup compared to an outgroup. While this intergroup empathy gap is well-studied in social psychology, it remains unclear how it manifests in naturally occurring online social interactions. To this end, we measure how commenters express social judgments, as an indirect outcome of their understanding towards the posters, and empathy in text, based on whether commenters share the poster's gender or are of similar ages. We focus on posts where the poster self-reports these demographics, and analyze 126,716 comments associated with 36,163 posts from 18,111 commenters in r/AmItheAsshole, while controlling for commenter and poster group identities, post features (topic, length, and score), and both commenter- and post-level variance. Our results show that when commenters and posters are ingroup, in either gender or age, commenters are more likely to provide a Not the Asshole verdict and show greater text-based understanding as measured by LLMs. We also observe that older commenters behave differently from younger ones. Furthermore, in a subset of posts where the gender and age of the other party in the conflict are explicitly mentioned, we find that commenter-poster ingroup effects are moderated by the group relationships between the poster and the other party when commenters make social judgments. Our work highlights the importance of intergroup context and social group nuances in understanding online discourse.

---


### 88. [Hierarchical Masked Diffusion Language Models](https://arxiv.org/abs/2610.29255)

**<font color=#1a73e8>作者：</font>** Parul Gupta, Satwik, Avni Aggarwal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models have emerged as an alternative to autoregressive models, enabling parallel token generation. However, standard masked diffusion language models use a shared noise schedule across positions without explicitly encoding which positions should be resolved first. Many tasks exhibit a natural priority among positions: document titles and section headings can guide the generation of body text, while Sudoku cells determined directly from the initial clues can help resolve more difficult cells. To incorporate this notion of priority (or hierarchy) among token positions, we introduce the Hierarchical Masked Diffusion Language Model (HMDLM), which augments each token position with a hierarchy level available as part of the training data, and requires zero or minimal additional annotations. It factors generation into two passes: the first predicts a hierarchy distribution over masked positions, the second predicts token distributions conditioned on it. Giving each hierarchy level its own noise schedule induces a soft, controllable preference for revealing higher-priority positions earlier while keeping decoding fully parallel. Our formulation is mathematically grounded, and we re-derive the forward and reverse processes and the NELBO for this factorization. Our evaluation shows that for the task of language generation on LM1B, HMDLM reduces perplexity by more than 1.5 points over Anchored Diffusion Language Model (ADLM), a recently proposed strong diffusion baseline; on WikiHow, we see a drop in perplexity of up to 4.4 pts on ADLM and up to 7 pts against MDLM. An LLM judge on WikiHow prefers HMDLM generations (the two variants combined) more than $2\times$ as often as the baseline. On the task of solving Sudoku puzzles requiring multi-step reasoning, it improves solution accuracy by up to $8.6\%$ absolute points over existing diffusion baselines.

---


### 89. [ARCANA: A Benchmark for Abstraction and Analogical Reasoning](https://arxiv.org/abs/2610.29271)

**<font color=#1a73e8>作者：</font>** Ruqi Chen, Zilei Wang, Wei Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Analogical reasoning is widely considered a fundamental component of human intelligence. Few benchmarks are designed to explicitly test far analogical reasoning - reasoning between domains that are superficially dissimilar yet share deep relational or structural similarities. In this work, we introduce an analogical reasoning benchmark called Abstraction and Reasoning Corpus of ANAlogy (ARCANA). The tasks of ARCANA require performing far analogical mappings from real-world objects or physical phenomena to abstract grid-based transformations, different from the well-known ARC-AGI benchmark which primarily emphasized innate human priors. We validate ARCANA through a human study, demonstrating that humans solve these tasks reliably. In contrast, evaluations across a range of large language models show a distinct performance gap compared to humans, revealing systematic failure modes that remain challenging for current models. To address this gap, we propose ConceptSIR, a reasoning framework based on concept slippage, introspection, and reflection. Experiments demonstrate that ConceptSIR enables standard LLMs to solve several challenging ARCANA tasks that were unsolved by direct prompting in our evaluation. Overall, our results suggest that far analogical reasoning remains an open problem for contemporary LLMs. All the materials are available at this http URL. The complete codebase, including benchmark, and ConceptSIR, is publicly available at this https URL. All ARCANA data and task instances can be accessed and explored at this https URL.

---


### 90. [Design and Tuning of Multi-Agent Systems Using Bayesian Evolutionary Optimization](https://arxiv.org/abs/2610.29276)

**<font color=#1a73e8>作者：</font>** Dominik Jehle, Tom Zehle  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing effective multi-agent systems (MAS) remains a challenging and resource-intensive task. We propose a Bayesian Evolutionary Optimization framework for automatically discovering task-specific MAS topologies. The approach combines evolutionary operators to generate diverse workflow graphs with Bayesian optimization to focus cost intensive evaluations on promising candidates. In contrast to LLM-based candidate selection, our approach uses a graph-aware Gaussian Process and Expected Improvement to provide an explicit selection criterion during evolutionary search. We evaluate the method on BigCodeBench for code generation and on a tabular preprocessing benchmark using TabPFN. On BigCodeBench, evolved architectures achieve the highest overall performance among the evaluated agent systems. On temporal tabular datasets, optimized MAS preprocessing improves over the default TabPFN model on several tasks, while remaining competitive on IID datasets. Overall, the results demonstrate the potential of Bayesian selection for guiding evolutionary MAS search under expensive evaluation budgets.

---


### 91. [Flat-RLVR: Sharpness-Aware Reinforcement Learning with Verifiable Rewards for Reasoning Capacity in LLMs](https://arxiv.org/abs/2610.29281)

**<font color=#1a73e8>作者：</font>** Yeonbum Kim, Hyun Kyu Lee, Sung Whan Yoon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR), particularly through group-relative policy optimization (GRPO), has emerged as a central paradigm for the post-training of large language models (LLMs). While RLVR is highly effective at enhancing the reasoning capabilities of LLMs, it commonly induces \textit{distribution sharpening}, whereby the policy distribution becomes excessively peaked and rare-yet-correct trajectories are progressively suppressed, thus diminishing sample diversity. To this end, we promote flat-reward optima in RLVR to smooth the policy distribution. We theoretically link flat reward RLVR to reduced distribution sharpening, and empirically show improved sample diversity while maintaining single-attempt accuracy. Our method, called \texttt{Flat}-RLVR, searches for flat reward regions via sharpness-aware minimization during LLM post-training, combining this with GRPO variants to achieve better trade-offs between sampling efficiency and reasoning capacity.

---


### 92. [Computer Vision and Knowledge-Grounded Language Models for Intelligent Beekeeper Assistance](https://arxiv.org/abs/2610.29283)

**<font color=#1a73e8>作者：</font>** Asaduz Zaman, Mohaimenul Azam Khan Raiaan, Malika Nisal Ratnayake  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Managed and wild bees sustain roughly a third of the global food products, yet colonies face mounting stress from climate-change including extreme weather patterns, altered parasite and disease patterns. Timely assessment of colony condition such as understanding colony strength, brood area, honey and pollen storage, comb usage, is essential to adaptive management. However, manual hive frame inspection is slow, costly, and quality depends on scarce expertise. We present an artificial targeted intelligent system framework focusing on edge deployable pipeline that turns hive frame photographs into interpretable and action-oriented inspection report. The pipeline includes an object detector to detect biologically-meaningful comb-cell classes; detections are distilled into structured fact schema; facts are converted into constrained factual text; the text triggers a grounded knowledge-base for interpretations and recommendations. Knowledge-base entries are required to be triggerable by evidence expressed in the fact schema. We built our system based on open source FAIRHiveFrames-1K dataset and favour reproducible, edge-deployable models over large general purpose frontier models. We additionally release FAIRHiveText-1K dataset that turns FAIRHiveFrames-1K dataset into interchangeable facts and text interpretation of the facts, making it easy for further LLM-based research into this area. We also propose a pathway to develop the grounded knowledge-base that will be helpful in providing interpretable and actionable reports from the facts.

---


### 93. [Approximate Solomonoff Induction: On the Robustness of Learned Universal Predictors](https://arxiv.org/abs/2610.29289)

**<font color=#1a73e8>作者：</font>** Qian Li, Shang-Hua Teng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Why large language models trained via log-loss minimization over massive and diverse datasets exhibit broad capabilities and generalizable skills is not yet fully understood. Grau-Moya et al. (ICML 2024) offer a conceptual explanation through the lens of meta-learning: if sequence-generating environments $\nu$ are drawn from a prior $w_{\nu}$, minimizing population log-loss recovers the corresponding Bayesian mixture predictor $\xi=\sum_\nu w_\nu\nu$. In the idealized limit in which $w$ is a universal prior, the optimal predictor corresponds to Solomonoff universal induction. Practical machine learning algorithms, however, generally produce only \emph{approximately} optimal predictors. This raises a natural question: \emph{Does the prediction performance remain robust under approximation}? In this paper, we first provide a tight bound on the worst-case effect of approximation on prediction error. We show any predictor $\rho$ satisfying $D_{KL}(\xi \|\rho)\leq \eta$ retains bounded cumulative-expected-squared prediction error. However, while the Bayesian mixture predictor $\xi$ has error $O(\log(1/w_\mu))$ in an environment $\mu$, we establish a tight $\Theta(\eta/w_\mu)$ bound on the excess error of $\rho$ relative to $\xi$. Thus, approximation can substantially degrade performance in environments assigned small prior probability. In sharp contrast, when environments are averaged according to prior $w$, we prove that the excess prediction error is only $O(\eta)$. Furthermore, we establish a distribution-shift theorem for dominated shifts from a training prior $w$ to a test prior $w'$, interpolating our average-case and worst-case guarantees. Finally, we extend our robustness analysis to a finite-sampling setting relevant to learning universal predictors with neural networks and Transformers, where $D_{KL}(\xi\|\rho)$ could be unbounded. [For the full abstract, see the paper.]

---


### 94. [Credit Where Credit Is Due: Contrastive Attribution Topology Search for Multi-Agent Systems](https://arxiv.org/abs/2610.29292)

**<font color=#1a73e8>作者：</font>** Fabian Tritthart, Tom Zehle  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An LLM multi-agent system (MAS) is only as good as the agents it chooses to trust: its accuracy and cost hinge on its topology, meaning which agents are included and how they communicate. A single task score, however, does not reveal which agents help or hinder performance. We propose Contrastive Attribution Topology Search (CATS), which searches for compact teams within a fixed supergraph of specialized agents. An LLM attributer compares execution traces across candidate topologies and assigns credit to individual agents. CATS uses these credits to update supergraph edges while progressively pruning weak edges and agents, yielding a small team for deployment. With small open-weight models and matched candidate evaluations, CATS improves mean accuracy on BigCodeBench by 5.3 percentage points over score-only heuristic search while using 54\% fewer deployment tokens. On MBPP, CATS matches the strongest baselines with fewer tokens than the other searches. In a HotpotQA prompt-poisoning stress test, CATS excludes all adversarially prompted agents in all three runs, whereas random search retains some at comparable accuracy. Per-agent credit thus supports both team optimization and the pruning of potentially harmful agents.

---


### 95. [Same Probabilities, Different Advice: Gain-Loss Framing Effects in High-Stakes LLM Decision Support](https://arxiv.org/abs/2610.29294)

**<font color=#1a73e8>作者：</font>** Yuyao Zhang, Yakun Cui, Han Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to support consequential decisions, yet their reliability under equivalent representations of uncertainty remains unclear. Existing work has documented prompt sensitivity, cognitive biases, and confidence miscalibration, but it is still unknown whether high-stakes advice changes when the same probability is expressed through complementary gain and loss frames. We introduce FrameBench-HPS, a controlled benchmark of 2,880 prompts derived from 240 high-stakes scenarios across healthcare, finance, education/career, and legal/consumer-rights domains. Across seven LLMs, gain-loss framing changes the recommendation category in 32.4% of complete groups, with most changes involving uncertainty rather than direct reversals. Human evaluation confirms corresponding shifts in perceived risk and directiveness. Robustness experiments show that framing effects persist under conversational paraphrases and exceed ordinary repeated-generation variability. Probability canonicalization substantially reduces framing sensitivity, identifying probability representation as a practical target for improving consistency in high-stakes LLM decision support.

---


### 96. [ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery](https://arxiv.org/abs/2610.29303)

**<font color=#1a73e8>作者：</font>** Yongqiang Chen, Chenxi Liu, Deyu Zou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evolutionary coding agents such as AlphaEvolve are one of the notable successes in using Large Language Models (LLMs) to build AI Scientists. These agents tackle open-ended scientific problems by iteratively improving and evolving programs, leveraging the prior knowledge and reasoning capabilities of LLMs. Despite their success, mutations over programs are mostly low-level upon surface heuristics, without a persistent unit of control. In contrast, science compounds through ideas. In this work, we propose ExpEvolve, which injects idea-level extraction and control into evolution: it discovers and leverages the high-level factors from programs that explain scoring differences among different programs. We characterize theoretical conditions on when discovery with idea factors improves sample efficiency. We also build a practical framework to show that the extracted high-level idea factors are helpful for guiding exploitation from experience and exploration when discovery comes to a plateau. Across 11 open-ended mathematical tasks, ExpEvolve significantly improves the final performance and sample efficiency up to 5.0x. The improvements also transfer to 4 other LLMs and to 6 machine learning tasks from MLS-Bench. Analysis shows that ExpEvolve can discover idea-level factors to provide better exploration and exploitation for evolutionary discovery.

---


### 97. [LLM-Based Exogenous World Modeling for Dynamic Scheduling](https://arxiv.org/abs/2610.29308)

**<font color=#1a73e8>作者：</font>** Ni Zhang, Haofeng Yuan, Jianan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dynamic scheduling requires dispatching online arrivals while anticipating future jobs, as poor decisions can compound downstream costs under nonlinear tardiness objectives. We show that a pretrained large language model (LLM) can serve as the exogenous component of a structured world model, forecasting uncertain future job arrivals. Specifically, we exploit an afterstate decomposition, which separates known deterministic shop transitions from uncertain exogenous job arrivals, enabling the LLM to forecast only the latter through a compact belief representation. Building on this, we develop Afterstate World-Model Planning (AWMP), which combines an evolved, belief-conditioned dispatching strategy with short scenario-based rollouts. A surprise-triggered refresh mechanism queries the LLM only when newly observed arrivals deviate sufficiently from previous forecast, and online residual self-calibration further conditions the LLM on its recent forecast errors to handle nonstationary arrivals. Across diverse arrival distributions, AWMP reduces weighted tardiness by 6-21% on dynamic job-shop and 22-46% on flexible job-shop benchmarks, relative to the best of eight classical priority-dispatching rules.

---


### 98. [A Stratified Multi-Rater Evaluation of LLM-Based Virtual Standardized Patients with a Deployed Data-Generation Platform](https://arxiv.org/abs/2610.29312)

**<font color=#1a73e8>作者：</font>** Yongjin Yi, Jinyong Park, Sejoong Kim  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The Objective Structured Clinical Examination (OSCE) is widely used to assess clinical communication skills in medical education, requiring trainees to take histories and reason clinically with standardized patients (SPs). Large language model (LLM)-based virtual standardized patients (VSPs), typically built by persona-injected prompting, offer a practical alternative. However, existing evaluations rely on a single backbone LLM, small human rater panels, or LLM-as-a-judge scoring without an utterance-aligned human-expert reference, and so cannot identify the specific shortcomings of individual models. We evaluated four LLMs (GPT-4o, Claude 3.5 Sonnet, Llama-3.1 70B, and HyperCLOVA X), spanning commercial, open-source and Korean-developed models, against a human-expert reference across three Korean OSCE cases (hematuria, fever in pregnancy, and chronic cough). In a double-blind, fully crossed design, 17 senior medical-student raters scored every model utterance on three sentence-level and six encounter-level Likert metrics, yielding 7,480 data points. We analyzed the scores using a stratified linear mixed-effects model based on an 11-category history-taking and 3-level linguistic-form taxonomy. At the encounter level, three of the four LLMs fell 0.08 to 0.47 Likert points below the human-expert reference on Comprehensibility, Consistency and Hallucination-freeness. The difference was not statistically significant for Hallucination-freeness in Claude 3.5 Sonnet and GPT-4o, Consistency in GPT-4o, and Engagement in HyperCLOVA X. Llama-3.1 70B fell significantly below the reference on all six metrics. We also introduce a web-based OSCE platform that supports virtual practice across diverse clinical cases and continuously collects student-VSP dialogues under research and privacy consent.

---


### 99. [Asking What a Director Sees Can Change What Vision-Language Models Choose](https://arxiv.org/abs/2610.29318)

**<font color=#1a73e8>作者：</font>** Jiaxuan Guo, Xingyu Ren, Kejia Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models are now routinely tested on theory of mind: whether they can work out what another person sees, knows, and means. A common design asks the model to report that perspective and then to act for the person, and reads a correct report beside a wrong action as a failure to use the perspective. That reading rests on a quiet assumption: that asking for the report leaves the action unchanged. We show that it does not. In a rendered Director Task, a partition hides the largest block from a director who asks for "the largest block". Asking first which blocks the director can see raises the share of replies that choose this hidden block by 12 to 88 percentage points on six GPT models and by 17 on Qwen3.8-27B, even though the models mostly report correctly which blocks the director sees. Reasoning traces and prompt rewordings suggest why: the question shifts how the request is read, from the director's view toward the model's own. When the prompt states what the director knows and refers to, fewer than 1% of replies pair a correct report with a hidden-block choice. Any evaluation that elicits a perspective report before the action it scores needs a baseline without the question, and we deliver one: paired prompts that differ only in that question, a design any perspective-taking benchmark can adopt.

---


### 100. [OSynth: A Longitudinal, Context-Sensitive Evaluation of Meeting Understanding](https://arxiv.org/abs/2610.29319)

**<font color=#1a73e8>作者：</font>** Ian Porada, Suraj Tripathi, Chaitanya Animesh 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Meeting notetakers are increasingly deployed in settings where longitudinal context is available including calendar metadata, prior meetings, emails, slides, and speaker enrollments; however, meeting corpora remain limited in terms of size, domain coverage, and available context. We present OSynth, a large-scale synthetic dataset of simulated organizations comprising 570 hours of meeting audio together with associated artifacts and a latent ground-truth state. In a pairwise comparison, human raters distinguish OSynth meetings from real meeting transcripts with only 56% accuracy based on excerpts of 150-300 words. Across state-of-the-art LLMs, additional context yields significant gains on several entity-sensitive dimensions, demonstrating limitations of contemporary approaches and the potential usefulness of OSynth in developing better-contextualized meeting-understanding systems.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-204](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
