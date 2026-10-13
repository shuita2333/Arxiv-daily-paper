# 🧠 大模型相关研究 | 2026年10月14日

> 本类共 **230** 篇论文：已确认 **202** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-230](./part-05.md)

---

### 1. [Algebraic Integer Quantization for Machine Learning Applications](https://arxiv.org/abs/2610.12494)

**<font color=#1a73e8>作者：</font>** Anthony Kostal-Vazquez, Vassil Dimitrov, Branden Butler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this article, we propose algebraic integer number formats (AINF) as a framework for highly configurable and accurate compressed computation. A key property of AINF is its straightforward reduction to purely integer arithmetic, enabling error-free multiply-accumulate operations. We develop a matrix multiplication engine that exploits this property, obtaining performance within a predictable factor of the most efficient numerical counterparts on modern hardware accelerators. Another key advantage of AIQ is the freedom to select algebraic integers tailored to the numerical characteristics of a given use case, offering optimization opportunities that are fundamentally unavailable in floating-point or fixed-point formats. Motivated by these properties, we introduce algebraic integer quantization (AIQ), a lossy compression format for large language model (LLM) inference, and provide results demonstrating that AIQ achieves competitive accuracy compared to the industry-standard MX format across a diverse set of models and benchmarks at equivalent bit-per-parameter budgets. The experiments presented in this article employ algebraic integers of degree two (quadratic integers); generalizations to higher-order and, in particular, multidimensional algebraic integers promise even greater computational advantages and remain a promising direction for future work.

---


### 2. [Kairos: Toward a Byte-Level Foundation Model for Every Modality](https://arxiv.org/abs/2610.12495)

**<font color=#1a73e8>作者：</font>** Fabien Furfaro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small language models trained on a single local machine leave little room for architectural trial and error. Kairos combines bidirectional gated-DeltaNet linear attention and sliding-window attention over shared projections (LiZAttention2), block-wise Attention-Residual aggregation, a sparse Mixture-of-Experts (MoE) feed-forward layer and a multi-scale byte-level codec, trained with a uniform-noise denoising objective over one byte space shared by text, image, audio, video, lidar and control streams; this report asks whether the combination optimizes at all before asking whether it is useful. We give code-derived algorithms for each component, including a cross-session recurrent-state memory gate, then run convergence sanity checks: overfittinga single 440-byte sentence at 1--15M parameters, text only, with three seeds for codec and attention choices and single-run sweeps for seven further factors. The two attention variants tested at 3\,000 steps (LiZAttention2 and window attention alone) reach a minimum loss near $10^{-3}$. After 600 steps, the mean minimum loss ranges from 0.018 (patch codec) to 0.354 (depthwise convolutional codec) with an identical ranking on three seeds. An apparent advantage of shared over separate attention projections closes with more steps or more diverse data and reverses when the projections are frozen: it is a convergence-speed effect, not a capacity effect. These checks suggest that the implementation optimizes; they say nothing about generalization, multimodal training or comparison with existing models, which a planned pretraining run is meant to address. The Discussion sizes a 200M-total/25M-active target analytically; none of its throughput figures is measured. Code is available at this https URL . Python package at this https URL .

---


### 3. [CORAL-KV: Compact Cross-Layer Prediction and Residual Coding for Autoregressive Video KV Caches](https://arxiv.org/abs/2610.12514)

**<font color=#1a73e8>作者：</font>** Albert Ge, Akash Haridas, Utkarsh Saxena 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models maintain a growing attention key-value (KV) cache, making memory a key bottleneck for long video generation. Recently, clustering-based quantization has emerged as an effective method to compress video KV caches by grouping similar key and value vectors then quantizing residual errors. However, when later frames attend to the compressed history, small reconstruction errors can compound as the video grows. Beyond the within-layer similarity exploited by clustering, we find strong dependencies across cache layers in video models. This motivates Coral-KV - Calibrated Offline, Residual-coded, and Adapted Locally - a KV-cache compression framework that uses cache states in each layer to predict keys and values in subsequent layers, then quantizes the remaining prediction residuals. We construct compact block-diagonal-plus-low-rank (block-DPLR) predictors: block-diagonal components model channel relationships within each attention head, while a global low-rank term models dependencies between heads. Coral-KV exposes a flexible fidelity-memory trade-off: it can reuse its predictors across videos or refit lightweight block-diagonal predictors to the current video for higher fidelity. Across extensive evaluations on both HY-WorldPlay and MAGI-1, our reusable configuration improves PSNR over QVG-4 by 0.32 dB and 4.95 dB, respectively, while using 48% and 37% less cache memory. Against QVG-Pro, our video-adapted configuration improves MAGI-1 PSNR by 3.77 dB while using 33.7% less cache memory. Coral-KV also maintains higher reconstruction fidelity over extended generation and reduces temporal discontinuities while retaining comparable generation latency.

---


### 4. [TraceICL: Thread-Resolved Demonstration Curation with Consistency Calibration for Robust Multimodal In-Context Learning](https://arxiv.org/abs/2610.12516)

**<font color=#1a73e8>作者：</font>** Yigit Yilmaz, Elena Petrova, Mehmet Kaya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interleaved multimodal in-context learning (ICL) lets frozen large vision-language models (LVLMs) acquire new tasks from a handful of image-text-answer demonstrations, yet it remains fragile: demonstrations bind to the wrong images, redundant exemplars crowd out informative ones, and noisy answers are copied verbatim into predictions. We present AVA, a training-free framework that organizes the demonstration pipeline of multimodal ICL into three composable stages. A Thread-Resolved Decomposer (TRD) segments the interleaved context into per-sample threads and re-stitches them with explicit boundaries, restoring image-text binding. An Influence-scored Demonstration Selector (IDS) estimates each candidate's marginal influence with one extra forward pass, removes redundancy, and orders the survivors by descending value. A Weak-to-Strong Consistency Calibration (WSC) module scores each demonstration by a weak sibling model's reconstruction confidence and softly reweights its contribution during decoding. On five vision-language benchmarks with interleaved 4-shot prompts, AVA improves the strongest same-setting baseline by +1.7 points on average, with gains of up to +2.4 points on VizWiz, shrinks the require-visual performance gap on ScienceQA-IMG, and retains most of its gain under 30% noisy demonstrations, at a 26% latency overhead that an offline cache amortizes. No gradients are ever computed; the LVLM stays frozen.

---


### 5. [TerraAgent: Demonstration-Grounded Multi-Agent Reasoning for Long-Context Remote Sensing Visual Question Answering](https://arxiv.org/abs/2610.12517)

**<font color=#1a73e8>作者：</font>** Jingwen Huang, Yiming Fang, Hanxiao Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing visual question answering (RS-VQA) requires answers that truly depend on image evidence, yet current remote sensing multimodal large language models (RS MLLMs) are still evaluated mainly by accuracy, which cannot reveal whether a correct answer was produced without using the image. This setting introduces three challenges: demonstrations retrieved across different ground sample distances (GSD), sensors, and city textures may be poorly matched; real queries often involve long visual contexts from multi-scale tiles, multi-temporal frames, and retrieved knowledge, where evidence can be diluted and errors can propagate through multi-step reasoning; and prior-only answering remains invisible to standard metrics. We present AVA, a training-free framework that wraps a frozen RS MLLM with three modules. GDR performs GSD-bucketed, scene-graph-based demonstration retrieval and filters demonstrations whose answers are unsupported by their images. MACE decomposes each query into an evidence-typed sub-question DAG, routes sub-questions to suitable perception tools, and records verified provenance in a shared evidence ledger with bounded re-perception. CVA audits the final answer through counterfactual perturbations of cited evidence, including ablation and swap, and computes a visual-dependency score for confidence calibration and evidence-forcing re-query. On RSVQA-LR/HR, VRSBench, and LHRS-Bench, AVA improves average accuracy by up to 2.40 points over the strongest same-setting baselines, raises the visual-dependency score from 0.28 to 0.49, reduces the prior-only answer rate from 46.2 percent to 21.7 percent, and lowers the hallucination rate from 17.1 percent to 9.8 percent, with 2.6x the cost of a single backbone forward pass and no fine-tuning.

---


### 6. [EliteTable: Self-Improving Program Search for Executable Control Policies](https://arxiv.org/abs/2610.12536)

**<font color=#1a73e8>作者：</font>** Stuart Farmer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> EliteTable is a self-improving program-search algorithm guided by large language models (LLMs) that uses a fixed-capacity table of high-scoring solutions to guide new proposals, edits of existing solutions, and remixes of several solutions. Performance was evaluated across six Gymnasium control tasks, each with ten generations and fifty candidate slots per generation. Each task was evaluated across ten independently initialized searches. Candidate-score medians rose between the first and final generations in all six tasks, and selected-winner search-score medians rose in five. In CartPole-v1, the selected winner reached the search-score ceiling in the first generation of all ten searches. All ten paired held-out endpoints improved in four of the six tasks. BipedalWalker-v3 and CarRacing-v3 improved without reaching their reporting targets. Six of ten Acrobot-v1 searches declined on held-out episodes, and the median paired change was negative. The results document improvement during program search and the transfer of selected-winner gains to new episodes in some tasks. Comparisons and ablations are needed to establish EliteTable's relative performance and the contributions of its components.

---


### 7. [AutoIndexer: Flexible-Order Decoding by Training Causal Models on Chains of Edits](https://arxiv.org/abs/2610.12545)

**<font color=#1a73e8>作者：</font>** Shu Ishida, Aliasghar Khani, Tianyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoregressive decoding is less suited to non-causally ordered data, e.g., cross-references or future dependencies, since their outputs cannot be revised post hoc, unlike iterative human reasoning. Diffusion LLMs partially mitigate this limitation but still cannot flexibly insert or remove arbitrary numbers of tokens from a pre-generated context. We design AutoIndexer as a generative model with a novel training and decoding mechanism that simulates a Chain of Edits, allowing the model to flexibly modify its prior outputs in hindsight via token insertions, substitutions, and deletions. The model learns to predict marker tokens for opening and closing edits, simultaneously moving a cursor to positions in the existing token sequence, analogous to a text editor. Training sequences are obtained by perturbing ground-truth labels with inverse chained edit operations, and the model learns to edit by undoing those inverses. The perturbation training allows AutoIndexer to be robust to erroneous context and adaptable to editing tasks such as code correction. We demonstrate that our method exhibits post-generation context-editing capabilities that most autoregressive and diffusion models lack without compromising performance on standard LLM benchmarks. The code is available at this https URL.

---


### 8. [Sample-Adaptive Zeroth-Order Post-Training](https://arxiv.org/abs/2610.12566)

**<font color=#1a73e8>作者：</font>** Haiyuan Wan, Yanyi Li, Weicheng Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization offers a memory-efficient alternative to backpropagation for fine-tuning large language models. However, existing ZO methods typically sample training examples uniformly, overlooking their evolving importance and leaving avoidable estimation variance. To address this limitation, we propose Sample-Adaptive Zeroth-Order Optimization (SAZO), which learns sample importance online and adaptively allocates queries to accelerate convergence. SAZO extracts gradient-norm information from existing directional differences to estimate sample importance without access to true gradients. Furthermore, to track evolving importance from sparse minibatch feedback, SAZO maintains per-example exponential moving averages that aggregate observations across updates. The method requires no additional model evaluations and only $O(N)$ additional scalar state compared with MeZO. We prove that SAZO asymptotically matches the leading convergence term of the minimum-variance sampling oracle, and achieves a strictly faster convergence rate than standard methods. Extensive experiments across four model families demonstrate improved average downstream performance and up to $6\times$ faster convergence to the same training loss in terms of query count.

---


### 9. [SWE-Duel: Towards a Self-Scaling Arena for Coding Agents](https://arxiv.org/abs/2610.12569)

**<font color=#1a73e8>作者：</font>** Wei Minn, Zhensu Sun, Lwin Khin Shar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Static coding benchmarks are fixed at release. Over time their tasks leak into training data, and stronger agents eventually saturate them. We argue that a benchmark should instead aim to be self-scaling: its tasks and oracles are created at evaluation time, so no content exists in advance to leak, and its difficulty is set by the participating agents rather than fixed at release. We introduce SWE-Duel, an arena in which two coding agents evaluate each other over mirrored Red-Blue turns. In each turn, the Red agent works on a real repository across three context-isolated sessions. It proposes and implements a new feature with feature tests, then embeds a subtle bug in that feature along with sealed bug-triggering tests. The resulting pull request is admitted only if (1) it passes the feature tests and the repository's existing tests while failing exactly the bug tests, and (2) a fresh session of the same agent can repair the bug blind, which rules out unsolvable tasks. The Blue agent then reviews the pull request without being told a bug exists. It wins only if its revision passes all three test suites, and then the two agents swap roles. We run a tournament among 11 model-harness participants on 15 repositories in five languages for 1,500 turns. The leaders win in different ways. GPT-5.5 with Codex CLI ranks first as the strongest solver, repairing 98.3% of the defects it reviews. Claude Opus 4.8 with mini-swe-agent ranks second as the strongest task author, with a 27.3% Red win rate. Finally, within one model family, tasks written by the newest version defeat a fixed-reference solver far more often than those of older versions (42.9% vs. 4.0%), giving preliminary evidence that task difficulty scales with task authoring capability.

---


### 10. [Contextual Correction of Parallel Drafts for Speculative Decoding](https://arxiv.org/abs/2610.12570)

**<font color=#1a73e8>作者：</font>** Roy Eisenstadt, Harel Lidar, Tal Gonen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model inference by using a lightweight drafter to propose multiple tokens that are subsequently verified in parallel by the target model. Recent diffusion-based drafters make this paradigm particularly attractive: deep attention-based neural backbones provide strong predictions, while drafting multiple future positions in parallel avoids the sequential cost of autoregressive generation. This parallelism, however, comes at a cost. Tokens within a draft block are predicted without access to the realized identities of preceding draft tokens, removing intra-block dependencies that would naturally be available under autoregressive generation. We introduce DCOCO (DFlash Contextual Corrector), a lightweight mechanism that restores these dependencies while preserving parallel drafting. Rather than committing to each position's top prediction, DCOCO retains multiple candidate tokens and evaluates their contextual compatibility across adjacent draft positions in parallel, enabling contextually informed token selection at low additional cost. Across four verifier backbones and ten benchmarks, DCOCO achieves the highest average throughput in every evaluated configuration, spanning greedy and stochastic decoding with and without extended reasoning, with speedups of up to 6.6x over vanilla decoding. Its advantage persists under concurrent serving: DCOCO outperforms the strongest competing method by 6-23% across 4-32 concurrent requests, while other sequential correctors fall below uncorrected DFlash at these loads. These results demonstrate that recovering intra-block dependencies through parallel contextual scoring delivers consistent acceleration across decoding regimes and serving loads.

---


### 11. [An all-transistor physical-learning transformer can be trained to perform in-context learning](https://arxiv.org/abs/2610.12571)

**<font color=#1a73e8>作者：</font>** Michael C. Abbott, Benjamin B. Machta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most systems trained by equilibrium propagation or coupled learning are in the same class as multi-layer perceptrons: while they may be universal function approximators, they struggle to learn associative tasks which are easy for transformers. Equilibrium propagation relies on a bidirectional flow of information through the physical system between input and output. The reverse flow is broken by more complex nonlinear systems, such as those performing multiplication which is needed to express dot-product attention. Here we explicitly restore this bidirectional flow by introducing extra circuit elements for this purpose into a double or dyadic circuit. We then use these ideas to construct an attention mechanism exploiting the exponential current law of sub-threshold MOSFET devices. We show that in simulations this circuit can be trained to perform a simple in-context learning task, despite using realistic reverse components which transmit only an approximate gradient. For this training to succeed we need cross-entropy loss (not mean squared error). We generate nudges appropriate for this loss using a novel floating circuit element, based on the same MOSFET sub-circuit used for softmax. We train the resistors in this circuit using the Lion optimiser, which can be implemented using one capacitor per parameter to store local memory of past gradient estimates.

---


### 12. [Mind the Temporal Gap: Evaluating Video Models for Temporal Understanding in Driving](https://arxiv.org/abs/2610.12575)

**<font color=#1a73e8>作者：</font>** Shiva Sreeram, Erfan Aasi, Tsun-Hsuan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video-language models are increasingly treated as general-purpose video reasoners, yet it remains unclear whether they robustly capture temporal dynamics in safety-critical settings such as driving. We study this question through controlled ego-motion tasks that require identifying actions from driving videos. Across video-language models, we find that standard prompting, visual prompting, few-shot prompting, and chain-of-thought prompting remain unreliable and highly task- and model-dependent, with persistent class biases, although newer models show substantial task-specific few-shot gains. In contrast, lightweight LoRA finetuning and simple probes trained on intermediate visual features recover strong motion-discriminative performance, indicating that motion-relevant cues are often present inside the models but are not reliably used by the final video-to-language pathway. These results suggest that, in driving, current video-language models remain unreliable temporal reasoners and often behave more like frame-level, bias-driven recognizers than dependable temporal world models.

---


### 13. [One Model to Loop Them All: Elastic Latent Recurrence for Language Models](https://arxiv.org/abs/2610.12582)

**<font color=#1a73e8>作者：</font>** Faisal Ladhak, Shantanu Acharya, Santiago Akle Serano 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A latent recurrent language model applies a shared block of layers repeatedly, so one checkpoint can trade inference compute for accuracy by changing the loop count. At one loop, however, such models typically fall well short of a non-recurrent model of the same size, a one-loop tax that makes a separate non-recurrent model the better choice whenever latency matters. We present Elastic Latent Recurrence (ELR), a recipe for training looped language models without this tax. At one loop, an ELR model costs the same to serve as a non-recurrent model of the same size and, trained on the same data, reaches similar accuracy. Each additional loop then buys more accuracy for more inference compute. Three choices make this work: a gated state update with a learned step size, loop counts mixed within each optimizer update, and conditioning each pass on its loop index and budget. The first two preserve one-loop accuracy, and the third lowers loss at every additional loop. Mixed depths can be introduced late in pretraining to limit the added training cost, and with zero-initialized conditioning added at the switch, this late schedule reaches lower loss than mixed-depth training from scratch. In MoE models, reusing first-loop expert routes on later loops cuts mixed-depth update time by 11.7% with no measurable change in accuracy. At inference, keeping only the last loop's attention KV cache holds attention KV memory at its one-loop level while retaining most of the gain from additional loops. On 4B dense and 30B-A3B MoE hybrid models, ELR at one loop is 0.52 points below and 1.04 points above its matched baseline on a ten-task average, and four loops add 7.25 and 4.75 points. Carried through post-training, the recipe yields Koi-4B, a single checkpoint that scores an estimated 18 on the Artificial Analysis Intelligence Index at one loop, matching Qwen3.5-4B, and 29 at four loops.

---


### 14. [Know What You Don't Know: Agentic Data Synthesis by Evolving Generation Space for Closed-Loop Learning](https://arxiv.org/abs/2610.12593)

**<font color=#1a73e8>作者：</font>** Wei Yang, Qing Ping, Youzhi Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The continued improvement of large language models increasingly depends on synthetic experience, yet effective data synthesis for interactive agents requires not only executable and verifiable trajectories, but also interactions that provide learning value for the current task agent. Existing methods increasingly incorporate environment feedback, data validation, or learner failures, but still face a feedback-to-decision gap: observed weaknesses do not directly specify how future synthesis should change, or whether they can be represented by the current synthesis space. To address this gap, we propose EvoSyn, a learning-feedback-driven multi-agent framework that organizes synthesis around a revisable state specifying what interaction factors can be deliberately generated and where synthesis effort should be allocated. A role-specialized multi-agent system translates learner feedback into synthesis revisions, while a Designer allocates synthesis directions and a Planner grounds them into executable experience. This process enables within-space adaptation toward weak or under-covered regions and synthesis-space expansion that promotes newly discovered factors into explicit generation controls. Experiments on $\tau^2$-Bench and CAR-Bench show that EvoSyn improves average task success by 13.3 points over the strongest synthesis baseline, while producing higher-quality and structurally broader synthetic experience and discovering controllable factors missed without learner feedback.

---


### 15. [SpireBench: Evaluating Long-Horizon Strategic Play of Agentic Models with Slay the Spire](https://arxiv.org/abs/2610.12596)

**<font color=#1a73e8>作者：</font>** Scott C. Lowe, Sander W. Keemink  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic large language models now tackle complex tasks, yet strategic reasoning over long horizons is under-studied: most agentic benchmarks are short and episodic, and performance on long tasks is hard to dissect into stored knowledge, reasoning and luck. We introduce SpireBench, in which models play the complete commercial deck-builder Slay the Spire (StS), where early decisions decide long-term success. Across 20 large language models (LLMs) at the game's highest difficulty, frontier models beat heuristic baselines and match the average human player but remain far behind experts. This gap widens as the run lengthens: the strongest models win the first act as often as experts, then fall behind. What separates strong models from weak is how well they play each fight; all of them misjudge risk over a run, preserving health rather than spending it to grow stronger. A comprehensive, self-consistent renaming of every game term shows that part of their performance rests on prior knowledge of the game, and models do not improve from the memories they write across runs, which are often wrong and overly cautious. Our harness is the first to give a model the complete original game, and we compare it with existing harnesses. Overall, SpireBench offers an unsaturated long-horizon benchmark with tools to locate where and why agents fail.

---


### 16. [Beyond Binary Verifiable Rewards: Behavioral Self-Rewarding for SWE Agents](https://arxiv.org/abs/2610.12598)

**<font color=#1a73e8>作者：</font>** Yiran Wu, Andrew Zhao, Yurui Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) provides reliable supervision for software engineering agents through executable tests, but binary rewards fail to distinguish trajectories with substantially different debugging quality. We investigate whether the current policy can judge its own trajectories and use these judgments to improve task performance without a separately trained reward model. To this end, we introduce Behavioral Self-Rewarding (BSR), a reward-refinement method that reuses the policy to compare observable debugging behavior among trajectories from the same task with the same verifier outcome. BSR aggregates pairwise preferences into task-local scores and converts them into bounded auxiliary rewards, introducing reward contrast while preserving the verifier-defined pass/fail ordering. This provides additional supervision from already-collected trajectories without requiring new environment interactions. Experiments on SWE-bench Verified and SWE-bench-Live show consistent improvements across the evaluated Qwen3-14B and Qwen3-32B configurations, supporting using the policy's own comparative judgments as a complementary learning signal for training software engineering agents.

---


### 17. [STAPLE: Static Sparse Upcycling of Pretrained Checkpoints via Embedding Modules](https://arxiv.org/abs/2610.12599)

**<font color=#1a73e8>作者：</font>** Ranajoy Sadhukhan, Euijin Hong, Sheng Cao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse computation can scale the parametric capacity of LLMs without proportionally increasing active computation, but pretraining sparse architectures remains expensive and data-hungry. Existing sparse upcycling methods mainly target Mixture-of-Experts models, where expert homogeneity, sample inefficiency, and system overheads can limit practical scalability. Static sparse memory offers predictable access and token-specific updates that can help address these challenges, but naively integrating it into pretrained computation yields poor returns. In this work, we introduce STAPLE, a recipe built upon STEM for integrating static sparse memory into pretrained models. Whereas STEM replaces FFN up-projections with token-indexed embeddings, STAPLE retains them and adds the embeddings as a residual pathway, preserving pretrained computation while learning complementary token-specific information in a scalable manner. On OLMo-2 1B, STAPLE improves over continued dense training by 4.27 points on HumanEval, 2.80 on MBPP, 2.27 on GSM8K, and 1.65 on DROP. Average performance increases with static capacity, and improvements persist on the larger OLMo-2 7B backbone. STAPLE also outperforms static sparse baselines such as STEM and an Engram-style model, and achieves a higher average score than an MoE upcycling baseline while decoding 2x faster with less than half its GPU model memory and measured GPU energy per token in our throughput-oriented decoding evaluation. Importantly, despite introducing billions of parameters late in training, our host-offloaded implementation keeps generation throughput within 1.5% and training throughput within 3% of the dense baseline, while caching only the ~5% most frequent embeddings on GPU. These results show that static sparse memory can provide a sample-efficient, scalable, and sustainable path for expanding pretrained models without sparse pretraining from scratch.

---


### 18. [Reflective Prompt Optimization of a Deep-Research Agent: A Topic-Disjoint, Multi-Seed Protocol for Measuring Transferable Gains and Prompt-Level Overfitting](https://arxiv.org/abs/2610.12601)

**<font color=#1a73e8>作者：</font>** Elias Lumer, Sahil Sen, Vamse Kumar Subbiah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt optimization is an attractive alternative to reinforcement learning for adapting language-model agents, since it is cheap and produces human-readable artifacts. On factual tasks, however, it carries a failure mode that scalar-reward reinforcement learning does not. An optimizer that reads the training examples can write their answers into the prompt, so an in-distribution gain may be memorization rather than transferable behaviour. We apply reflective prompt evolution (GEPA) to the two system prompts of a multi-agent deep-research agent and evaluate it under a topic-disjoint split in which no topic is shared across train, validation, and test. Held-out citation reward rises by 0.079, from 0.702 to 0.781, with a bootstrap 95\% confidence interval of [0.051, 0.107], and the gain replicates across three seeds (mean 0.107). Nearly half of the winning prompt is a memorized answer key, yet a controlled ablation shows this content earns no reward even on the exact training questions it encodes. The large validation-minus-held-out gap is therefore small-sample selection under a noisy judge, not memorization. Varying the verifier isolates what makes the gain transfer. Decomposed per-dimension feedback is the causal ingredient, and collapsing it to a single scalar reward makes held-out transfer negative. The gain persists under an out-of-family judge and is largely reproduced by a hand-written version of the discovered recipe. Credible evaluation of prompt optimizers therefore requires held-out topics, multiple seeds, and verifier ablations. We release the candidate prompts, lineage diffs, figures, tables, and analysis.

---


### 19. [Self-Preservation in Language Models](https://arxiv.org/abs/2610.12602)

**<font color=#1a73e8>作者：</font>** Dongkyu Cho, Rumi Chunara, Ali Behrouz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) seeks to adapt pretrained models while preserving prior capabilities. Yet the tasks supplied for preservation cover only part of what a model knows, while forgetting can extend beyond them. Recent work shows that language models can supplement this limited evidence by generating useful replay without access to their original training data. This raises a question about self-preservation: can a model help choose preservation targets that protect its own capabilities more broadly? To study this question, we organize task descriptions and their examples into Task Banks, whose entries can be selected and combined to guide replay generation by a frozen model. Continual instruction tuning with Qwen models of varying sizes yields three findings. First, the new task and learning rate shape which prior capabilities degrade, while tracking previously correct answers reveals losses that average accuracy can conceal. Second, generated replay reduces forgetting on tasks outside the bank. Combining partial banks strengthens this protection, improving mean retention of previously correct answers over either bank alone across the tested sizes. Third, the model can also help choose replay targets: selection informed by the new task improves mean held-out retention over random selection at 4B, with similar new-task gains, although smaller models show no corresponding advantage. Under a fixed example budget, however, replacing new-task examples with replay improves preservation at the cost of smaller new-task gains. Together, these findings show that models can support broader self-preservation by generating replay data and, in some settings, choosing which tasks to replay.

---


### 20. [SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized Software Environments](https://arxiv.org/abs/2610.12611)

**<font color=#1a73e8>作者：</font>** Tian Jin, Wenhao Wang, Jing Kang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) are rapidly improving, yet synthesizing diverse and reliable software environments at scale remains challenging. Native application environments require substantial construction and integration effort, which limits application coverage and increases the risk of application-specific overfitting. Browser-hosted environments provide limited interaction depth and workflow complexity. These limitations motivate SoftwareGym, an automated pipeline for synthesizing GUI software environments with diverse interfaces, executable functionality, and runtime-verified behavior. It generates structurally diverse designs, realizes them as runnable applications, and uses GUI evaluation with iterative repair to ensure functional reliability. Using SoftwareGym, we synthesize 182 applications across twelve categories and achieve a mean GUI task pass rate of 91.5%. We construct SoftwareGym-Bench, a 120-task evaluation suite spanning the same twelve categories, and use trajectories collected from these environments for CUA training. The resulting model improves Pass@3 from 41.39% to 56.97% on the strictly out-of-domain OSWorld benchmark and achieves 40.0% on SoftwareGym-Bench. These results demonstrate the potential of synthesized software environments as scalable and transferable supervision for CUA training.

---


### 21. [GeopoliticalQA: Benchmarking Retrieval and Generation over Intelligence Reports](https://arxiv.org/abs/2610.12617)

**<font color=#1a73e8>作者：</font>** Veronika Solopova, Ivan Havlytskyi, Viktoria Skorik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Geopolitical and strategic intelligence reports constitute a rich source of expert knowledge and have increasing value in the current political climate, but their heterogeneity and analytical complexity pose challenges for retrieval-augmented question answering. We introduce a benchmark for grounded question answering over 415 open-source geopolitical and strategic intelligence reports, comprising 5,525 document-grounded question-answer pairs spanning factual, inferential, comparative, and risk-oriented questions. We propose a document-aware generation pipeline that profiles reports before generating questions and validate dataset quality through expert annotation and an LLM-as-judge protocol. Using the benchmark, we evaluate 15 retrieval systems and six open-weight LLMs for RAG. We find that models perform similarly on document-level retrieval, while at the harder chunk level retrieval quality is not driven by embedding-model scale: bge-m3, a mid-size open encoder matches an order of magnitude larger ones and outperforms commercial embedding APIs. In contrast, answer generation remains challenging even given the gold evidence, particularly for inferential and risk-oriented questions.

---


### 22. [r/ADHD: Community-Based Understandings of Time Management Challenges in Digital Environments](https://arxiv.org/abs/2610.12629)

**<font color=#1a73e8>作者：</font>** Shizhao Liu, Lei Cao, Celia T. Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Community accounts of ADHD can complement clinical understandings by foregrounding members' own definitions of time-management difficulties and support. We used human-led, LLM-assisted thematic analysis to examine 5,379 relevant r/ADHD posts from 2020 to 2025. Across five challenge and nine strategy themes, members described difficulties beginning intended tasks, disengaging from digital media, and sustaining support. Tools often demanded the self-regulation they were meant to support, while lost time and tool breakdown carried guilt and self-blame. Members drew on people, routines, and environments alongside digital tools, often seeking advice and recognition from peers. These accounts broaden the design problem to include the practical and emotional work of sustaining support. They motivate tools that reduce this burden and evaluations that consider recovery after distraction and emotional costs alongside task outcomes.

---


### 23. [Feature Competition and Its Representational Origins in Vision Language Models: Evidence from the Stroop Paradigm](https://arxiv.org/abs/2610.12650)

**<font color=#1a73e8>作者：</font>** Nurbüke Teker, Rui Xiao, Zeynep Akata 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When you ask a vision-language model (VLM) a question with an image, it answers your question based on the image. But to act means to choose: saying one thing means choosing to respond not say another. This becomes an issue when the image contains multiple features that equally relate to the question at hand: how would VLMs choose to respond? This problem is precisely studied by the classical Stroop task in psychology: among a set of deliberately designed images whose text and color conflicts (e.g., \textcolor{blue}{RED}), participants are instructed to report the color. We adapt this psychological paradigm to a benchmark and prompted a range of contrastive and generative VLMs on their behavior. Across models, we observe a persistent bias toward the feature of text in Stroop images: when text and color disagree, models preferentially generate responses centered to the text rather than color. We then opened the black box and examined the source of this bias and why certain features influences the model's behavior more than others. In the embedding space, we found that textual cues are represented more strongly and separably than color cues. This representational asymmetry predicts intervention success: steering models toward text-related directions is substantially easier than steering them toward color-related directions. Using a classical psychological paradigm, we demonstrate, at both behavioral and representational levels, that distinct features within the same image can exert unequal influence on VLM behavior. Our findings suggest that VLMs assign different degrees of saliency to different features within the same image, highlighting the need to understand how cue-specific saliency shapes their performance in widely used downstream applications.

---


### 24. [SynAct: Synergistic Active Feedback Learning for LLM Agents](https://arxiv.org/abs/2610.12651)

**<font color=#1a73e8>作者：</font>** Ning Liu, Ian Li, Kristina Klinkner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents executing multi-step workflows fail in two fundamentally different ways: recoverable slips, which further attempts can repair, and knowledge gaps, which retrying cannot resolve. Expert feedback can address the latter, but expert attention is scarce. The key challenge is therefore not whether to ask for feedback, but where feedback can change the outcome. Existing approaches either avoid expert feedback, allowing agents to reinforce their own errors, or allocate feedback at the task level without identifying consequential decisions. We present SynAct, an active learning framework that treats expert attention as the binding constraint and allocates feedback at the level of individual decisions. SynAct ranks decisions by the mutual information between the selected action and the terminal outcome across repeated rollouts, queries an expert at the highest-value decisions, and distills the resulting corrections into transferable rules that the agent can reuse without expert access at deployment. We theoretically characterize what this signal identifies under finite repeated sampling: with k rollouts and at least m observations per action, outcome-constant decisions have zero mutual information, while outcome-separating decisions have mutual information at least H2(m/k) bits, yielding exact separation for any threshold t in (0,H2(m/k)). This also explains why success-based acquisition can be blind when all rollouts fail: success is constant even when failed runs reach different outcomes. Across four agent benchmarks and four models spanning three families, SynAct improves held-out accuracy in all 16 evaluated settings, by +11.7pp on average. The same signal transfers to inference-time routing, where SynAct outperforms budget-matched cascade, uncertainty, and expert-judge routers in 15 of 16 settings, while a single targeted correction outperforms seven additional unaimed retries.

---


### 25. [CLEAT: Learning Value-Guided Clarification for Interactive Agents](https://arxiv.org/abs/2610.12655)

**<font color=#1a73e8>作者：</font>** Jiatan Huang, Zheyuan Zhang, Ziming Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents can execute increasingly complex tasks, but effective assistance also requires aligning their actions with goals and constraints that users may leave unstated. We study this problem as interactive intent alignment through clarification. Yet clarification is useful only when the agent can turn the answer into better decisions. As training changes how the agent handles incomplete information and uses additional answers, the same clarification can become more or less useful. We introduce CLEAT (CLarification through valuE-guided Agent co-Training), a framework that co-trains a clarification-value controller and the task policy from shared interaction outcomes. We formulate residual query value to measure the task utility gained by asking rather than proceeding under the current policy, and estimate it through paired rollouts from the same interaction history. These paired returns train the controller to predict clarification value and the task policy to select useful questions and act on the answers. The controller guides subsequent rollout collection, while outcomes from the updated agent provide new value labels that allow clarification guidance to adapt as the agent learns. With Qwen3-4B, CLEAT achieves the highest mean score in all ten evaluation settings across four benchmarks. Gains over the strongest baseline reach 13.2 and 6.5 percentage points on UserGym Travel and IN3 underspecification judgment accuracy, respectively. Ablations show that co-training improves the task policy even when the controller is removed at inference, while adapting clarification guidance to the evolving policy yields further gains.

---


### 26. [MagicBeanStalk: Escaping the RLVR Zero Advantage Trap with Recursive Data Synthesis](https://arxiv.org/abs/2610.12659)

**<font color=#1a73e8>作者：</font>** Ximing Lu, Aviral Kumar, Jan Kautz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data-centric scaling of RLVR has focused on collecting or generating verifiable training problems. However, corpus size alone does not determine whether the dataset provides a useful learning signal for a target policy. To guide the synthesis of effective RLVR data, we experimentally characterize dataset effectiveness as a function of its problems, the target policy, and the training rollout budget. Under this characterization, we show that a large open-source math corpus pooled from widely used RLVR datasets falls almost entirely into a zero-advantage trap: for a fixed target policy and rollout budget, roughly 88% of its problems are solved in every rollout or failed in every rollout. Filtering concentrates what remains, but it can only select, discarding the hard problems. Effective synthetic problems should therefore require the reasoning operations and compositions required to solve those hard problems. Yet their difficulty must be calibrated, so that some rollouts succeed, some fail, and at least one correct solution fits within the training budget. Prompting a teacher to vary hard problems directly does not achieve this. Guided by these empirical principles, we introduce MagicBeanStalk, a top-down decomposition and bottom-up recursive data-synthesis algorithm that grows seed problems into families of substantively new, policy- and budget-calibrated training problems while preserving the seeds' reasoning blueprints. Across 8 math benchmarks, continual RLVR on MagicBeanStalk problems improves gpt-oss-120b from 61.2 to 69.8 (+8.6) and DeepSeek v4Flash from 72.4 to 77.9 (+5.4) on a 16K-token budget. Training on the full 78K source corpus improves by only +1.1 and its best filtered real data subset by +5.8. In finance, we synthesize over 14K verifiable problems from only 340 solutions and improve over base by 6.9 and 2.4 points on SecQue and FinanceBench, respectively.

---


### 27. [Incremental Retrieval-Augmented Generation for Human-in-the-Loop Decision Support](https://arxiv.org/abs/2610.12666)

**<font color=#1a73e8>作者：</font>** Federico Mazzoni, Andrea Failla  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce iRAG, a human-in-the-loop decision-support system combining Retrieval-Augmented Generation (RAG) with Hybrid Decision-Making. Unlike conventional RAG systems, relying on static Knowledge Bases (KBs), our proposal addresses settings where the KB is initially empty and is progressively populated through human decisions. The system stores previous decisions as retrievable precedents and moves from silent observation to evidence-grounded contestation and, finally, to autonomous handling with abstention. Against an independent baseline, iRAG matches final-decision error under 10% drift without retrieval decay and reduces it under 40% drift across all configurations. Retrieval decay improves performance on changed knowledge while increasing error on stable knowledge, evidencing a stability--plasticity trade-off rather than a general advantage. Human oversight is an architectural provision of the workflow; its usability with real human users remains to be evaluated.

---


### 28. [perturber: A Stateless Service for Semantics-Preserving Text Perturbations](https://arxiv.org/abs/2610.12667)

**<font color=#1a73e8>作者：</font>** Khoi-Nguyen Tran  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) evaluations on clean benchmarks overstate model robustness: real inputs arrive perturbed, and these meaning-preserving variants routinely move model answers. Studying this systematically requires applying perturbations one at a time, reproducibly, and identically wherever they run, yet existing tools couple them to a benchmarking stack rather than packaging them as a reusable transform layer. We present perturber, a stateless service and Python library that applies exactly one semantics-preserving perturbation per call, drawn from a first-party catalog of 68 perturbations across 11 families. It turns on a single primitive, with composition left to the caller chaining calls, so the service and the library produce identical output by construction. We evaluate the tool itself, its correctness, reproducibility, and cost, rather than any model's robustness, measuring meaning-preservation per perturbation rather than assuming it. The demonstration adds a live playground, an introspectable catalog for benchmark selection, and a one-command reproducible evaluation.

---


### 29. [Recurrent Harness for Agentic Continual Learning](https://arxiv.org/abs/2610.12668)

**<font color=#1a73e8>作者：</font>** Yuxin Xiao, Zhiyun Lu, Jianyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language model agents increasingly operate over long interaction streams, requiring online adaptation to distribution shifts through continual learning. However, existing agent harnesses typically either evolve their states only through forward information flow or rely on additional replay or validation data for harness optimization. To address this, we propose ReHarness, a recurrent harness framework for agentic continual learning that complements forward read and write with backward revision under a strictly online streaming protocol. We ask what information could have been captured differently in the harness state to better inform the current instance in the stream. Specifically, after each instance, we leverage the resulting trajectory as feedback to revise the reflections retrieved for that instance, thereby propagating feedback backward through the textual harness state. Across three continual learning benchmarks and three language model backbones, ReHarness consistently outperforms strong raw-context baselines, memory- and reflection-based methods, and prompt optimization approaches. Further analysis shows that ReHarness produces source-grounded and meaningful revisions, corrects overgeneralized or outdated experience under distribution shifts, and improves both stability and plasticity during continual learning.

---


### 30. [GeoFitBench-LLM: A Benchmark for Assessing Large Language Models' Capabilities in Geospatial Data Requirements Elicitation for Geo-Analytic Tasks](https://arxiv.org/abs/2610.12669)

**<font color=#1a73e8>作者：</font>** Amirhossein Vahdat, Thierry Badard, Luc Lamontagne  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are becoming central to GeoAI systems, yet their evaluation rarely considers the elicitation of geospatial data requirements. This omission is critical as retrieval oriented geo-analytic tasks cannot be supported reliably without first identifying the necessary datasets and constraints. GeoFitBench-LLM is introduced as a benchmark for assessing whether LLMs can infer the datasets, the supporting resources and the constraints required by geo-analytic requests in natural language. The benchmark is structured around two reasoning dimensions, Spatio-Temporal Relational and Semantic Grounding, reflecting long-standing challenges in geospatial information retrieval and related natural language tasks. Ground truth requirements are encoded in a fixed, provider-independent schema for reproducible evaluation of resource identification and attribute-level specification. Experiments on seven models under minimal prompting indicate that identifying the necessary resources is often achievable, with GPT-5.4 Thinking achieving the best result by recovering the complete set of resources in 66.67% of benchmark requests. Results further indicate that accurate fitness-for-use specification remains more difficult as inferential demands increase.

---


### 31. [Unsupervised Multimodal Reward Modeling](https://arxiv.org/abs/2610.12707)

**<font color=#1a73e8>作者：</font>** Yueying Li, Jingxuan Fan, Kianté Brantley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language reward models are trained on annotated preference pairs, which are expensive to collect, can disagree, and are ranked by benchmark accuracy. We build one with no human preference label: a linear head on an intermediate layer of a frozen Qwen3-VL backbone, trained to score a web caption above a perturbed version of the same caption; labeled data enters only to select the layer. The layer is the decisive choice, worth 5.8 points over the last layer, and one recipe transferred without re-tuning beats or at least matches GPT-4o on three benchmarks at 32B, 6.6 points ahead on VL-RewardBench, from a few thousand parameters at about a thousandth of fine-tuning compute. At an equal pair budget, perturbations teach a frozen head 3 to 5 points more than curated RLAIF-V pairs. Because the backbone is frozen, the objective is convex, and the perturbation sampler specifies the reward, which the benchmark does not identify: two heads trained on disjoint halves of the same perturbations tie on the benchmark and differ by 6.4 points in hallucination judging. Retraining the head on the policy's own verifier-labeled candidates cuts caption hallucination by 5.1 CHAIR points and lifts image-generation pass rate by 5.4, while scoring lower on every reward benchmark.
Together, an intermediate-layer probe, free same-image perturbations, and a verifier-driven bootstrap turn give a recipe for multimodal reward modeling that needs no annotator, costs a fraction of fine-tuning, and is specified by the comparisons it is trained on rather than by a benchmark rank.

---


### 32. [Byzantine-Resilient Federated Large Language Model via Hypergraph Message Passing](https://arxiv.org/abs/2610.12711)

**<font color=#1a73e8>作者：</font>** Kai Li, Hanlin Cai, Zihao Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Large Language Models (FedLLMs) are promising to deliver privacy-preserving, collaborative intelligence. The decentralized training process is vulnerable to Byzantine attacks that corrupt semantic consistency and factual resilience through malicious model updates. This paper presents a new resilience strategy that prevents semantically corrupted knowledge from propagating during federated aggregation. A defense problem is formulated to jointly maximize global accuracy and suppress manipulated model updates, enabling trustworthy knowledge aggregation without accessing private local data. To strengthen the resilience of FedLLMs, we develop a novel Hypergraph Message Passing Graph Autoencoder (HMP-GAE) framework, where low-rank model updates are represented as nodes in a hypergraph and high-order semantic relationships among multiple agents are exploited through iterative message passing. By leveraging historical checkpoints and cross-agent relational reasoning, HMP-GAE identifies and suppresses semantically inconsistent updates while preserving knowledge alignment among agents throughout federated training. HMP-GAE is implemented using Qwen-2.5 and Llama-3.2 as pretrained FedLLM backbones and evaluated on AG News and Yahoo! Answers datasets. Compared to existing defenses, HMP-GAE improves global accuracy by $1.21$\%, reduces final-model classification semantic entropy by $44.08$\%, and lowers perplexity by $13.34$\%. HMP-GAE outperforms the GAE-based defense by improving the accuracy $1.39$\%, reducing the semantic entropy by $54.5$\%, and lowering perplexity by $35.5$\%.

---


### 33. [U4RASD at KnowledgeGraphEval-2026: Ontology-Constrained Encoder and LLM Systems for Arabic Relation Extraction](https://arxiv.org/abs/2610.12742)

**<font color=#1a73e8>作者：</font>** Ahmad Abbas, Hussein Mazeh, Chadi Abou Chakra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper details our submission to KnowledgeGraphEval 2026 Subtask 2 on directed Arabic relation extraction. We explored encoder-based and large language model approaches for predicting one of 40 relations or no_relation from an Arabic sentence and a subject-object pair. Our encoder systems use typed entity markers and separate relation-existence and relation-classification heads, while our LLM systems fine-tune Yehia and Qwen3.5 with QLoRA and ontology-constrained prediction. Our best system, an ensemble of Yehia-RE, Qwen-RE, and TypedPair, achieved a micro-F1 score of 94.06 and ranked 1st in Subtask 2. Yehia-RE (full-vocabulary) achieved 92.98, while the best encoder and Qwen-RE achieved 92.69 and 91.94 respectively. Our results highlight the importance of constrained prediction and complementary modeling approaches for Arabic relation extraction.

---


### 34. [Static Gradient Attribution Underperforms a Density-Matched Random Mask on Loss-Based Forgetting Within LoRA B-Matrix](https://arxiv.org/abs/2610.12744)

**<font color=#1a73e8>作者：</font>** Yu Sun, Junwei Zhou, Zuodong Xiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient continual learning updates a restricted subset of adapter parameters to incorporate sequential tasks while limiting catastrophic forgetting. Gradient attribution is a common rule for selecting that subset, but it requires an additional backward pass over calibration data. We identify a parameter-pool confound in comparisons between initialization-time gradient masks and unrestricted random masks under standard zero-initialized LoRA ($B=0$): the gradient with respect to $A$ is identically zero ($\partial\mathcal{L}/\partial A=0$), so gradient masks select strictly from the $B$ matrix whereas unrestricted random masks draw from both $A$ and $B$. Such a comparison changes both the selection rule and the candidate parameter pool. Isolating the selection criterion by restricting both approaches to the same parameter pool, we find a negative result: a uniform random mask consistently achieves lower loss-based backward transfer than gradient attribution across seven seeds on Qwen2.5-3B. The effect is concentrated on the medical task, which contributes 80\% of the aggregate; code and math move in the same direction, and legal shows no reliable difference. This advantage is consistent with a stability--plasticity trade-off under the tested task sequence, in which random masking slightly reduces single-task fitting. On the two discrete-option tasks (Medical and Legal), the mean accuracy-BWT difference is not statistically distinguishable from zero.

---


### 35. [Generative AI Steering and Human Authoring: Complementary Search-as-Learning Scaffolds in Cross-Session Aggregated Academic Search](https://arxiv.org/abs/2610.12755)

**<font color=#1a73e8>作者：</font>** Milad Momeni, Orland Hoeber  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Aggregated academic search interfaces combine resources from heterogeneous sources, such as scholarly libraries and reference encyclopedias, into a single workspace. Such tasks frequently span multiple sessions, requiring learners to return to and resume work after hours or days. End-of-session consolidation, the activity of organizing and synthesizing gathered information so it can be resumed later, is important in this setting but underexplored in search-as-learning. Generative AI (GenAI) has the potential to make consolidation more efficient, but it may also shift cognitive work away from the learner. This study compares two consolidation scaffolds embedded in the workspace framework of an existing academic search interface that aggregates and clusters saved search results from two different sources (our university library and Wikipedia), which was developed in earlier work. STAIS (Steerable AI Summaries) provides a workspace enhancement that produces GenAI summaries that users can correct, reorganize, and fact-check, automating parts of the consolidation activity. NT (Note-Taking) provides a workspace enhancement that includes rich-text note editors that learners can use to author their own consolidations of what they have found. In a controlled between-subjects study (n=36), participants completed two sessions one week apart while searching an unfamiliar topic using either STAIS or NT. The two conditions produced contrasting post-resumption outcome profiles: STAIS supported faster task resumption and was associated with broader conceptual coverage and higher self-reported domain knowledge, whereas NT was associated with richer inter-concept connections and higher self-reported certainty.

---


### 36. [How Do Hardware Faults Manifest Differently in LLM Agents?](https://arxiv.org/abs/2610.12756)

**<font color=#1a73e8>作者：</font>** Aiden Rubey, Zachary Coalson, Cong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We present the first systematic study of the resilience of large language model (LLM) agents to random hardware-induced faults. Prior work on hardware fault resilience in LLMs focuses on model-level outcomes, such as incorrect outputs or generation failures. Yet LLM agents repeatedly interact with tools and environments, creating loops that can change how hardware faults manifest. We conduct an extensive evaluation across three agent benchmarks, comprising 6,814 agent executions: 2,400+ clean runs and 4,300+ fault-injected runs with independently sampled random two-bit weight faults. We trace how these faults propagate through agent execution. Unlike prior studies, we find that agentic execution transforms model-level corruption into distinct system-level outcomes: (1) agents can recover from faulty model outputs and still complete tasks correctly; (2) this recovery increases computational and execution costs; (3) a few faults cause subtle but semantically meaningful errors while the agent otherwise behaves normally; and (4) for some models and scenarios, faults can alter security and alignment behavior.

---


### 37. [DistressBench: Evaluating Multi-Dimensional Crisis Support in Large Language Models](https://arxiv.org/abs/2610.12758)

**<font color=#1a73e8>作者：</font>** Drew Rein, Patrick Oathout, Vishal Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models have been adopted faster than evaluation practices that reliably assess their risks, and a growing share of use is affective rather than informational. Within that traffic users disclose suicide and self-harm (SSH) crises. Existing safety benchmarks score models primarily on refusal, but refusal is not the desired behavior here; the conversation requires a substantive supportive response. We introduce DistressBench, 718 English conversations with clinician-authored user turns spanning 23 SSH subcategories, each paired with a task-specific rubric of weighted atomic criteria across seven dimensions of crisis support and a clinician reference response. A model's score is the weighted average over the criteria its reply satisfies, reading directly as the fraction of required care delivered. The best of 25 frontier models satisfies 88.4% of weighted criteria and the median model 71.4%, against 98.7% for clinician references scored on the same criteria. Pooled across all 25 models, in 35.3% of conversations where a model satisfied every criterion for recognizing the crisis, it failed to route the user toward human help. The shortfall concentrates in the dimensions requiring the model to act rather than withhold. Contrasting each dimension's median model against its best separates capability limits from choices: de-escalation reaches 74.6% in the strongest model against a median of 46.0%, and safety disclaimers 84.6% against 8.3%. Multi-turn conversations score below single-turn ones (68.5% against 74.2%). We release the corpus, rubrics, judge calibration labels, and a companion annex of 20 long-horizon red-team transcripts. These results argue for evaluating crisis safety on the care a model delivers rather than on what it declines to say, and for treating de-escalation and resource routing as deployment requirements.

---


### 38. [Faithful and Complete LLM-Assisted Automated Construction of Hierarchical Hardware Knowledge Graphs](https://arxiv.org/abs/2610.12762)

**<font color=#1a73e8>作者：</font>** Haotian Qiao, Robert P. Dick  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hardware datasheets contain engineering specifications essential for component selection, system integration, and hardware compatibility verification. However, manual inspection is tedious and error-prone because datasheets are lengthy and heterogeneous, with dense information fragmented across tables, figures, and text. Although large language models (LLMs) can automate this process, naïve one-shot processing omits relevant specifications even when the document fits within the model's context window.
We present an automated LLM-driven pipeline that transforms hardware datasheets into general-purpose hierarchical hardware knowledge graphs through chunk-based property extraction, hierarchical routing, and iterative refinement. The framework uses LLMs for information extraction and semantic reasoning while preserving source provenance and applying graph updates through validated instructions and deterministic local execution. This staged design reduces per-query context and maintains traceable intermediate representations. The resulting knowledge graphs provide semantically organized, source-grounded hardware properties for downstream retrieval and reasoning.
We evaluate the framework on 20 hardware datasheets spanning diverse component types and document lengths. We assess property faithfulness and introduce inter-graph completeness to measure relative semantic coverage without exhaustive ground truth. Our framework achieves 98.8% property faithfulness compared with 76.1% for the one-shot baseline, while fully covering 83.6% of faithful baseline properties; in the reverse direction, the baseline fully covers only 10.5% of ours. These improvements provide more reliable and comprehensive engineering information for downstream hardware design and verification, reducing the risk of overlooked constraints and incorrect decisions.

---


### 39. [REDaCT: Collapse-Free Unlearning in Large Reasoning Models](https://arxiv.org/abs/2610.12769)

**<font color=#1a73e8>作者：</font>** Joshua Maccoby, Wendy Hui Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlearning in large reasoning models (LRMs) requires removing forget-set information from both the reasoning trace and the final answer. Existing approaches achieve this objective at the cost of reasoning collapse, where the model fails to produce a coherent chain-of-thought (CoT) and does not properly terminate its reasoning process. To address this challenge, we propose REDaCT (REgenerate via Detection and Corrective Tuning), an inference-time unlearning framework for LRMs. REDaCT consists of two key components: (1) a binary leak detector that identifies sentences in the reasoning trace that leak forget-set information, and (2) an embedding optimization module that learns a corrective embedding offline, such that when injected at the first detected leak during inference, it guides subsequent reasoning towards sentences that do not leak forget-set information. Experimental results show that REDaCT completely avoids reasoning collapse, substantially improving reasoning preservation compared to state-of-the-art unlearning methods while maintaining perfect answer forgetting and near-perfect CoT forgetting. Our code is available at: this https URL.

---


### 40. [EvoBelief: Falsifiable World Models for Self-Improving LLM Agents](https://arxiv.org/abs/2610.12789)

**<font color=#1a73e8>作者：</font>** Janet Wang, Jiang Guo, Yi Xiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving LLM agents typically improve how they act through accumulated experience, reflection, or skills. Yet even procedurally capable agents can fail when their beliefs about environment dynamics are incomplete, incorrect, or outdated. We study a complementary axis of self-evolution: evolving those beliefs during deployment. Such beliefs can support multiple tasks, but incorrect ones can also propagate across them. We introduce EvoBelief, a self-evolving world model that represents environment knowledge as falsifiable hypotheses. Unexpected outcomes and decision-relevant unknowns trigger hypothesis formation. Later observations and controlled experiments provide independent validation before a rule can guide predictions or plans within its supported scope. Counterexamples narrow or retire rules as the environment changes. The language model remains frozen, and each rule remains linked to its evidence and the decisions it changes. Across four benchmarks spanning static dynamics, hidden drift, and scientific discovery, EvoBelief improves task performance and reuses learned rules across tasks. On ALFWorld without actor-side transition memory, it improves success over the matched Frozen World Model by 23.9% and 31.3% with Claude Haiku 4.5 and GPT-5.4, respectively. On MiniGrid, it revises stale rules and recovers after unannounced dynamics changes. In DiscoveryWorld's Reactor Lab, it discovers and validates quantitative laws, completing 83.3% of Normal-tier and 58.3% of Challenge-tier instances, versus 0% for each evaluated baseline. These results demonstrate self-improvement through testable, revisable environment knowledge rather than model-parameter updates.

---


### 41. [Meta-Reflective Evolution Effectively Improves Production AI Systems](https://arxiv.org/abs/2610.12794)

**<font color=#1a73e8>作者：</font>** Seung Won Wilson Yoo, Chang Zeng, Aditi Somayajula 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-guided evolutionary optimization has successfully improved prompts, programs, and even entire AI systems. Most optimization methods select a candidate from the search frontier, then mutate it in one LLM pass based only on its failures. This focus on the frontier can stall on production AI systems, where isolated failures reveal little about complex, hidden interactions. We introduce CoCoEvolve (Cortex Code Evolve), an evolutionary optimizer built around what we call meta-reflection, wherein an agentic mutator (Cortex Code) selectively retrieves evidence from the entire evolutionary history and probes the live system before verifying and proposing mutations. We apply CoCoEvolve to optimize three classes of production AI systems: data agents, LLM-powered data pipelines, and data engineering workflows. On DABStep, CoCoEvolve tops the public leaderboard, reaching 92.8% held-out hard accuracy compared to 78.4% for Meta-Harness and 30.4% for GEPA under matched conditions. Across six LLM data pipeline workloads, it outperforms every evaluated baseline. On data-eng-bench, CoCoEvolve lifts test-set solve rate from 59.1% to 77.4%, past the best baseline of 73.6%. It also has 11 percentage points higher accuracy than GEPA on HotpotQA while remaining competitive with specialized optimizers on established mathematical and systems benchmarks. Matched ablations confirm that each component of CoCoEvolve contributes to these gains, demonstrating the value of meta-reflection for optimizing production AI systems.

---


### 42. [People Making Conversation: Evaluating How Naturally Speech Models Converse](https://arxiv.org/abs/2610.12802)

**<font color=#1a73e8>作者：</font>** Arya Bastani, Iman Modarressi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A conversational speech model has to decide, at every pause, whether to speak. Existing evaluations test boundary detection, policy adherence, or aggregate statistics, not this decision. We place real-time speech systems at 427 pauses and 482 turn ends from 176 unscripted conversations in Seamless Interaction, give each the conversation so far, and score what it generates against what the person did: whether and how soon it speaks at a pause; its latency, length, and wording at a turn end; and whether it can answer a question about the preceding 30 to 120 seconds. Across six systems, the hosted APIs (GPT Realtime, Gemini 3.1 Flash Live, Grok Voice) respond at almost every pause whichever endpointer they use; only their latency, about 1 to 4 s with silence-based endpointers and about 8 s with semantic turn detection, decides whether the words land inside the pause. The full-duplex models (PersonaPlex, Moshi) are the only systems that regularly stay silent and the only ones that interrupt within a human reaction time. Hosted systems reply longer than the person. Given the history as text, hosted systems recall 41 to 60% of conversation facts under a Claude Opus 5.5 judge and 19 to 26% under a strict word matcher; hearing it as audio, full-duplex models recall 17 to 22% and 12 to 15%. We release the labels, points, harness, and every output.

---


### 43. [TreeHCA: Hindsight-Guided Exploration and Credit Assignment for Multi-Turn LLM Agents](https://arxiv.org/abs/2610.12828)

**<font color=#1a73e8>作者：</font>** Debajoy Mukherjee, Jeremy Carleton, Sushil Vemuri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outcome-supervised group-relative policy optimization (GRPO) assigns the same advantage to every token in an LLM agent trajectory, leaving useful and unhelpful decisions undifferentiated. Hindsight credit assignment (HCA) can refine this feedback, but its estimates rely on trajectories containing informative alternatives at consequential histories. We introduce TreeHCA, which couples hindsight-guided exploration with hindsight credit assignment. TreeHCA uses changes in reference-answer likelihood to revisit intermediate histories and sample alternative continuations, forming a tree of reasoning and tool interactions. Because this exploration changes the distribution of sampled continuations, we derive the corresponding inverse-hindsight importance correction, including an exact finite-pool identity. We use this structure in a normalized tree backup that propagates terminal outcomes into turn-level advantages. This shared hindsight structure is TreeHCA's central design principle, linking informative exploration with hindsight-guided credit assignment. Across seven question-answering benchmarks and three Qwen backbones, TreeHCA outperforms all baselines in aggregate exact match, validating the effectiveness of paired exploration and credit assignment for multi-turn LLM agent training. Our code is available at this http URL.

---


### 44. [Cross-Behavior Policy Optimization: Unified Learning from Offline Demonstrations and On- and Off-Policy Rollouts via a Shared Regression Target](https://arxiv.org/abs/2610.12830)

**<font color=#1a73e8>作者：</font>** Du Cheng, Junyu Lu, Jingfan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning post-training draws on offline demonstrations and policy-generated rollouts, yet conventional supervised fine-tuning (SFT) followed by reinforcement learning (RL) separates their objectives and limits continued reuse of collected responses. We propose \textbf{Cross-Behavior Policy Optimization} (CBPO), which makes these sources compatible with one regression loss through a fixed-reference target. Because the generating policy does not enter this target, positive and negative offline completions, reference responses, and current and historical rollouts can share a common reward-labeled record format and replay buffer. As new responses enter the buffer, optimization retains the same regression objective without coordinating separate SFT and RL objectives or requiring stored behavior-policy probabilities, importance weighting, or a learned critic. Restricting the available sources gives offline, on-policy, and off-policy variants, while CBPO-Unified combines them. Across two model scales and four mathematical reasoning benchmarks, CBPO delivers leading \texttt{avg@32} and \texttt{pass@32} performance across benchmarks and data regimes. On Qwen3-1.7B, CBPO-Unified improves benchmark-averaged \texttt{avg@32} and \texttt{pass@32} over SFT DAPO by 2.33 and 4.44 percentage points, respectively. In the replay ablation, retaining historical rollouts improves these metrics by 1.87 and 3.72 percentage points over the no-history configuration.

---


### 45. [From Instructional Intent to Classroom-Ready Lessons: Investigating Teacher-AI Collaboration in Lesson Authoring for Secondary Computing Education](https://arxiv.org/abs/2610.12834)

**<font color=#1a73e8>作者：</font>** Tahreem Yasir, Wenbo Li, Deniz Ozturk 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI is increasingly studied as a tool for supporting lesson authoring; the creation and adaptation of classroom materials, yet little is known about how it should fit into secondary computing teachers' subject-specific practices. We conducted two complementary qualitative studies with eight secondary computing teachers: focus groups examining existing authoring practices and a think-aloud study using LessonBuilder, a structured AI-supported lesson authoring system, as a research probe. We found that teachers' instructional intentions developed through creating, inspecting, and adapting materials, while teachers selectively delegated tasks to AI and retained responsibility for judging classroom readiness. The think-aloud sessions further showed how examining AI-generated materials prompted teachers to clarify and refine their intentions, making authoring an ongoing negotiation between what teachers intended and what the AI produced. In the context of computing lessons, classroom readiness also involved considering how programming materials and supporting guidance matched students' understanding and intended learning goals. We synthesize these findings into a conceptual model explaining how teachers coordinate instructional intent, AI assistance, and judgments of classroom readiness during lesson authoring. We derive design recommendations for supporting this coordination while preserving teacher control and addressing computing-specific authoring needs.

---


### 46. [COFFEQA: Counterfactual-Guided Few-Shot Distillation for LLM Question Answering](https://arxiv.org/abs/2610.12837)

**<font color=#1a73e8>作者：</font>** Kavinda Kehelella, Sanghamitra Dutta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation aims to train a smaller student model to mimic a larger teacher model for resource-constrained environments. However, the process of distillation is typically data-intensive and computationally expensive, particularly for generative tasks. Few-shot distillation offers an alternative by transferring teacher knowledge using limited training samples. However, we observe that few-shot distillation performance is heavily dependent on the choice of these training samples. In fact, we demonstrate that using more uncertain samples near the teacher's decision boundary can significantly deteriorate distillation performance. Motivated by this observation, we propose Counterfactual-guided Few-shot Distillation in Open-book Question Answering (COFFEQA), a novel strategy that aptly uses counterfactuals to provide additional supervision around challenging factual samples. In the generative QA setting, we define a counterfactual as a minimally modified context that induces the teacher to change its response to an alternative answer. We provide geometric insights on how factual-counterfactual pairs can constrain the deviation between the teacher's and student's decision boundaries. We further introduce a new metric, Context Following Difficulty (CFD) that further validates counterfactuals prior to distillation based on agreement with the intended alternative answer and dependence on the modified context. COFFEQA uses CFD-validated factual-counterfactual pairs for few-shot distillation. Experiments across five in-domain and three out-of-domain QA benchmarks using T5 and Qwen2.5 families show that COFFEQA outperforms factual-only distillation baselines under the same few-shot budget. For instance, on TriviaQA, COFFEQA improves over the factual-only baseline by 8.77 average EM points and 9.98 average F1 points under the T5 setting with 32 few-shot pairs.

---


### 47. [Neural networks are more modular than single neurons suggest](https://arxiv.org/abs/2610.12842)

**<font color=#1a73e8>作者：</font>** Shreya Saha, Benjamin Bergen, Meenakshi Khosla  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural networks routinely develop representations in which individual neurons contribute to multiple distinct functions, leading to the widespread view that such networks lack modular organization. We challenge this conclusion by introducing a formally nested hierarchy of modularity: unit-level, which requires distinct computations to occupy disjoint neurons; orthogonal, which asks whether a rotation reveals functionally independent subspaces; and linear, which asks whether a bounded linear map can separate task-relevant computations into independent subspaces. We develop a unified framework for learning decompositions at each level and evaluating them causally through selective ablation. Across vision models, language models and multi-task Recurrent Neural Networks (RNNs), we find that networks which lack unit-level modularity nonetheless often exhibit clear functional modularity at the subspace level. In vision and language models, content versus style and syntax versus semantics respectively dissociate under subspace ablation despite sharing overlapping populations of neurons. These learned subspaces also align differentially with brain data, with content and style subspaces predicting higher and lower visual cortex respectively, and semantic subspaces outperforming syntactic ones in predicting language cortex activity. In RNNs trained on multiple cognitive tasks and previously shown to lack modular structure, our decomposition recovers sharp double dissociations between tasks. The absence of unit-level modularity frequently coexists with clear subspace-level modularity across domains, enabling targeted intervention on specific computations even in networks where no individual neuron is specialized, with broad implications for mechanistic interpretability and for understanding functional organization in both biological and artificial neural systems.

---


### 48. [Mitigating Capability Degradation in LLM Self-Improvement via Representation Geometry Regularization](https://arxiv.org/abs/2610.12855)

**<font color=#1a73e8>作者：</font>** Jiaqi Tian, Ting Long  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-Policy Self-distillation is a self-improvement paradigm that enables large language models (LLMs) to improve their capabilities by leveraging the same model as both teacher and student under different conditioning contexts. However, we find that OPSD methods can progressively degrade previously acquired capabilities: queries that are correctly responded at earlier training stages may become incorrectly responded as optimization proceeds, even the overall performance continues to improve. Further analysis reveals that this degradation coincides with a deterioration of the geometry of hidden representations, characterized by reduced intra-cluster compactness and diminished inter-cluster separation. Motivated by this observation, we propose Representation Geometry Regularization (RGR), which preserves representation geometry during post-training by encouraging compactness within cluster and separation across cluster. RGR can be seamlessly integrated into existing OPSD methods without altering their core optimization procedures. Extensive experiments on multiple OPSD methods and benchmarks show that RGR generally alleviates capability degradation while retaining capability improvements. Our code is available in this https URL.

---


### 49. [Robust Langevin Sampling under State-Dependent Heavy-Tailed Noise with Applications to LLM Fine-Tuning](https://arxiv.org/abs/2610.12865)

**<font color=#1a73e8>作者：</font>** M. Berk Sahin, Ege C. Kaya, Arda Fazla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing convergence guarantees for non-log-concave sampling with stochastic gradient Langevin Monte Carlo (SG-LMC) typically assume globally Lipschitz gradients and uniformly bounded noise variance. Both assumptions can fail even in elementary sampling problems, and relaxing them better reflects practical applications such as Bayesian fine-tuning of large language models (LLMs). We relax both assumptions through generalized smoothness and our proposed state-dependent heavy-tailed oracle with finite $p$-th moments, $1<p\leq 2$. The oracle permits infinite variance when $p<2$ and includes the Blum-Gladyshev (BG-0) condition. We study these relaxations separately and jointly, proposing three methods. Under globally Lipschitz gradients, robust LMC (R-LMC) handles the proposed oracle through geometric-median centering and residual clipping. With exact gradients, adaptive LMC (A-LMC) controls discretization error under generalized smoothness. Robust adaptive LMC (RA-LMC) addresses both relaxations through robust estimation and a noise-aware step size. For all three methods, we establish non-asymptotic convergence guarantees in Fisher information (FI) without assuming dissipativity or a functional inequality. Synthetic experiments demonstrate FI convergence and the benefit of each mechanism. Bayesian fine-tuning experiments with LLMs and vision-language models support our oracle model and show that RA-LMC matches or outperforms state-of-the-art baselines in accuracy and uncertainty quantification.

---


### 50. [CaptchaAgent: Verifiable Visual Reasoning for CAPTCHA Solving](https://arxiv.org/abs/2610.12866)

**<font color=#1a73e8>作者：</font>** Shangquan Sun, Ruoyu Chen, Zhirui Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern reasoning CAPTCHAs require fine-grained perception, compositional relation reasoning, and grounded browser interaction. End-to-end vision-language model agents remain brittle in this setting because a missed object, incorrect count, or confused relation can propagate directly to the final action. To address this problem, we present CaptchaAgent, a structured visual reasoning framework for interactive CAPTCHA solving. Instead of predicting an action directly from a screenshot, CaptchaAgent first constructs a visual intermediate representation (V-IR) that explicitly records entities, attributes, and spatial or topological relations. A symbol-only ASCII protocol further requires the parser to commit to a concrete object set and count. Building on this global representation, localized evidence refinement revisits ambiguous regions at higher effective resolution, while counterfactual consistency verification tests whether the resulting action remains stable under task-preserving transformations. Across three proprietary backbones on Open CaptchaWorld, CaptchaAgent improves Pass@1 by 21.3-25.8 percentage points over a commercially available browser agent baseline evaluated with the same backbones. On the separate offline Oedipus-data benchmark, it further improves average Pass@1 by 9.2-12.3 percentage points over the Oedipus solver across three matched backbones. The intermediate traces show that exact counting, continuous geometry, and ordered execution remain major sources of automation difficulty for the evaluated agents, providing practical guidance for designing more resilient compositional CAPTCHAs.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-230](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
