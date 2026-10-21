# 🧠 大模型相关研究 | 2026年10月22日

> 本类共 **299** 篇论文：已确认 **275** 篇，待复核 **24** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-299](./part-06.md)

---

### 151. [Beyond Calibration: Temporal LLM Confidence Assessment Across Languages and Local Settings](https://arxiv.org/abs/2610.27702)

**<font color=#1a73e8>作者：</font>** Sahil Kale  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are expected to estimate their own uncertainty, with confidence signals used to guide retrieval, adaptive compute allocation, routing, and selective abstention. We investigate whether confidence signals measured at different temporal stages of problem solving encode distinct forms of epistemic information and remain reliable beyond English-centric settings. Inspired by classical meta-memory theory, we distinguish anticipatory pre-solve confidence (Feeling-of-Knowing, FOK) from retrospective post-solve confidence (Judgement-of-Learning, JOL). We evaluate these signals across two frontier LLMs, multiple reasoning domains, translated Marathi benchmarks, and a newly constructed benchmark of genuinely local Marathi factual questions. Across settings, the cheaper pre-solve signal remains weakly calibrated, while post-solve confidence generally provides stronger epistemic alignment despite its additional inference cost. Confidence behaviour transfers surprisingly well under direct language translation, with calibration trends largely preserved between English and Marathi, but degrades substantially on local Marathi knowledge, suggesting that linguistic transfer alone is insufficient for region-specific information needs. Finally, hallucinated responses maintain persistently elevated confidence after answer generation, highlighting important limitations of current LLM self-assessment mechanisms.

---


### 152. [How Fine-Tuning Objectives Shape Layer-Wise Information in LLM Hallucination Detection](https://arxiv.org/abs/2610.27711)

**<font color=#1a73e8>作者：</font>** Kaiyang Wan, Forrest Sheng Bao, Amin Ahmad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Under matched conditions, classifier-head fine-tuning (\textsc{cls}) paradigm consistently outperforms the LLM-as-Judge sequence-to-sequence (\textsc{s2s}) on binary hallucination detection. We trace this gap to the representations induced by the two objectives. Static analysis shows that \textsc{cls} learns a task-specific discriminative direction, pushing hidden states into a clear two-cluster geometry with stronger class separation and linearly decodable label information. By contrast, \textsc{s2s} relies on the pretrained language-modeling head to make decisions. This minimizes the pressure to reorganize representations, leaving the hidden states much closer to the pretrained backbone. Our analysis also reveals that the \textsc{cls} signal saturates before the final layer, after which upper layers form a plateau of statistically interchangeable and largely redundant representations. However, endpoint redundancy alone does not show whether these layers are dispensable during training. Further training-dynamics analysis reveals 1) a lower pretrained substrate, 2) a narrow upper-middle \textbf{InfoWindow} where task information emerges, and 3) a later-synchronizing upper plateau that mirrors this signal. This mechanism motivates us to remove layers above the InfoWindow. Truncating 31\% of the network leaves accuracy unchanged within seed noise on Qwen3-4B and 8B and cuts latency by $1.4\times$. The same depth fraction, fixed before any analysis of the target models, transfers to Llama-3.2-3B and Mistral-7B-v0.3, and the layer structure behind it reappears there and on QNLI and SST-2. We hope this helps guide efficient task-specific LLM design.

---


### 153. [When Does Experience Memory Help Closed-Loop LLM Driving Agents? A Controlled Evaluation with Resampled Warmup Pools, Token-Matched Fillers, and Audited Baselines](https://arxiv.org/abs/2610.27714)

**<font color=#1a73e8>作者：</font>** Yingxin Jia, Xuanyi Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When does experience memory help a closed-loop LLM driving agent? Published gains cannot say, because the two factors we find to matter most, which warmup experiences the pool contains and what any injected tokens do to the prompt, are controlled in none of them. We answer with a controlled evaluation on one audited HighwayEnv testbed (1Hz, gpt-4o-mini for the decisive contrasts). We treat the warmup pool as a resampled random factor (ten disjoint pools) and add token-matched irrelevant-filler controls, oracle-certified diagnostics, caution-pricing metrics, and quantified audits of the baseline ports. The probe suite spans flat-text retrieval (a DiLu port), a single-frame grid port (RESPOND-inspired), our episodic temporal-graph memory, a retrieval-free consolidated rulebook, and a flat K-step observation-history baseline. Four findings follow, each a property of this testbed. (1) Headline memory gains belong to the warmup draw. The reported pool is the best of ten for both retrieval memories, which beat No-Memory in only one pool of ten (sign test p=0.011), and even the rulebook's apparent pool-immunity collapsed on five fresh draws. (2) No retrieval design tested exceeds token-matched filler. The collision-only merge ceiling is reached by a single 15-token caution instruction, and metrics that price caution erase the rulebook's lead. (3) Representational sophistication is nowhere robustly operative. (4) Baseline port quality silently inverts conclusions. On this testbed, a single-pool comparison without filler controls would have reported memory gains that these controls reverse. We release the testbed, audited ports, seeds, and caches.

---


### 154. [Tracing Recurrent and Emergent Hallucination Patterns in Decomposed Text-to-SQL Generation](https://arxiv.org/abs/2610.27720)

**<font color=#1a73e8>作者：</font>** Hayden Moore, Abhinav Verma, Anshuman Dutt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can achieve strong Text-to-SQL benchmark performance while still producing schema and query-logic errors. Most evaluations characterize such failures only in the final generated query, making it difficult to determine whether a related error was also observed in an earlier, simpler step or appears only at the final stage. We present a drill-down evaluation framework that decomposes Text-to-SQL queries into progressively more complex executable sub-queries and corresponding natural-language questions, allowing rule-based hallucination categories to be examined across a generation path. We distinguish recurrent hallucinations, in which the same rule-based category is observed in an earlier step and again in the final query, from emergent hallucinations, in which the category is observed at the final step without an earlier detection in the same path. Across five LLMs evaluated on an expanded BIRD-mini benchmark, several categories show appreciable recurrence probabilities, while clause abuse shows comparatively higher conditional emergence. Under the conversational-history condition, recurrence probabilities are generally higher and emergence probabilities are generally lower. These observations indicate that the two conditional measures do not move uniformly in the same direction under additional context and motivate trajectory-level analysis in addition to final-output evaluation. Code and evaluation artifacts are available in the project repository. this https URL

---


### 155. [HydraPoT: A Configurable Multi-Agent Framework for Cost-Aware LLM-Assisted Honeypots](https://arxiv.org/abs/2610.27722)

**<font color=#1a73e8>作者：</font>** Kamolchanok Saengtong, Chutirat Saengyingyongwattana, Sasin Janpuangtong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can improve honeypot realism by generating dynamic, context-aware responses, but powerful cloud models incur substantial cost and latency, while lightweight models may provide weaker deception. This forces practitioners to choose between operational efficiency and interaction fidelity. In this work, we present HydraPoT, a configurable multi-agent honeypot framework that integrates traditional emulation, lightweight LLMs, and powerful cloud LLMs. HydraPoT routes each attacker command to an appropriate agent according to a configurable complexity-based policy, while maintaining shared session state to preserve consistency across agent transitions. We evaluate HydraPoT through an architectural-overhead analysis, a cross-agent context-preservation benchmark, and a three-agent case study. HydraPoT introduces less than 5% runtime overhead, preserves context across heterogeneous agents, and achieves fidelity close to a cloud-LLM-only honeypot. Under our case-study policy, it reduces cloud-processed tokens by 72.6% and operational cost by 3.7x. These results demonstrate that configurable multi-agent routing can make realistic LLM-assisted honeypots more practical under limited operational budgets.

---


### 156. [How Language Models Organize Task Information](https://arxiv.org/abs/2610.27724)

**<font color=#1a73e8>作者：</font>** Kaiyang Wan, Yuxia Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dense linear probes assess task readability from language model (LM) representations, but do not directly reveal how many features suffice for prediction. We measure readout sparsity with \(k^*\), the smallest feature count found by a fixed search protocol that recovers 95% of dense-probe AUROC above chance. We evaluate 19 LMs from five labs on 14 core tasks. Ten base models give the nine reliably readable tasks similar feature counts and nearly the same order. This agreement extends to the selected features themselves, which on three tasks show cross-model response correspondence beyond class-mean differences and a label-correlation-matched null. Instruction-tuned deployment selectively reduces \(k^*\), with both weights and input format contributing. In controlled synthetic experiments across 20 models, successfully learned targets admit single-feature readouts, whereas readable controls require tens of features. Reference-model \(k^*\) is associated with label requirements across eight students, following an empirical scaling of \(N^*\propto(k^*)^{0.65}\). After continual learning, saved heads can fail while linear readability remains high, and recovery requires fewer labels than initial task learning under the tested procedures. Pruning reduces linear readability, with wider pre-pruning readouts generally associated with larger losses. These findings distinguish task readability from readout sparsity and establish their complementary value for predicting learning requirements and diagnosing LM changes.

---


### 157. [RSI Control: Can AI Models Perform Covert Sabotage in the Self-Improvement Process?](https://arxiv.org/abs/2610.27735)

**<font color=#1a73e8>作者：</font>** Kaiwen Zhou, Udari Madhushani Sehwag  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement, in which frontier AI models work on training the next generation, is quickly becoming a reality. However, the safety of this process has received far less attention than it should. A misaligned model training its successor can shape what that successor knows, how it behaves, and what it wants, and the harm carries forward into the next generation. We study this risk through the lens of AI control. We introduce RSI Control Arena, a testbed in which a frontier model, acting as an autonomous R\&D agent, is given a benign main task from a stage of a successor model's training pipeline together with a covert side task to install a misaligned property in the successor. The testbed contains 16 side tasks in three classes, forming 22 task pairs with main tasks that span the pipeline from data curation to reinforcement learning. We evaluate six frontier models as agents against LLM monitors that read the transcript of the run and the agent's reasoning. We observe that every model completes a substantial share of the side tasks without degrading the main-task performance, including side tasks that make the successor itself a better saboteur. Under minimal instructions to stay covert, models already produce successful attacks that monitors fail to detect, and providing a short list of evasion tactics further reduces the detection rate. Monitors with access to agent's reasoning detects most attacks, but not all. Our results indicate that recursive self-improvement raises significant safety concerns, and that strong safety effort should be in place before models are trusted with greater responsibility of training their successors.

---


### 158. [Make the Adversary Spend More Energy: Generative Deception against Language-Model Attackers in Critical Infrastructure](https://arxiv.org/abs/2610.27739)

**<font color=#1a73e8>作者：</font>** Vlad Mihal, Hosam Alamleh, Alessandro Cantelli-Forti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Language-model attackers consume computational resources as they explore and interact with a target, creating an opportunity for cyber deception to impose costs. Whether such engagements favor the defender requires measuring both sides. We evaluate an autonomous language-model attacker against a decoy that uses a defending language model to analyze attacker commands and select defensive responses. Across 330 sessions, eight model pairs, two attacker profiles and three counter-injection levels, both sides run on identical GPUs and their energy is measured above idle. With runtime thinking disabled, the attacker-to-defender energy ratio has a 95% interval above one in 41 of 48 configurations under an allocation excluding attacker diagnostic calls, and in all 48 when those calls are included. Token ratios remain within approximately a factor of two in configurations without generation-cap truncation, showing that token counts can obscure substantial energy asymmetry. Counter-injection increases attacker tokens by approximately 9% per level without a detectable pooled change in energy consumption. Enabling thinking on both sides increases defender energy by 8--17 times and reverses the exchange for one model pair in the original campaign. We use these findings to motivate a proposed SCADA deception architecture with private physical state per identified adversary and deterministic protocol and process emulation.

---


### 159. [Hearsay or Fact? How Framing and Elicitation Shape LLM Probability Updates](https://arxiv.org/abs/2610.27745)

**<font color=#1a73e8>作者：</font>** An-Sheng Jhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as judgment assistants and as stand-in participants in psychology experiments, yet little is known about how much their probability estimates move in response to a single new piece of information. We pair premise-hypothesis items from $\delta$-SNLI with one strengthener and one weakener each, elicit the prior and the posteriors in separate calls, and measure the directional movement s: the mean posterior change signed by the annotated direction, so that the prior cancels out. We vary whether the update is stated ("Here is something else you learned") or reported ("Someone said that"), and whether the model gives one probability or five weighted estimates. We test seven configurations: two local models (Qwen3-8B, OLMo-2-7B; 240 pairs) and five configurations run through agent command-line harnesses (120 pairs), with hypotheses and analysis rules fixed before the formal runs (not publicly registered). Under stated, direct elicitation all seven move in the annotated direction (s = 18-28 percentage points). Reporting lowers s in all seven point estimates (significantly in six, by 2-5 points) and raises the share of reverse movements in all seven: the effect is consistent but small. Five weighted estimates lower the share of responses at $\leq$5% or $\geq$95% in all seven, but in the two local models they also reduce s by 43% and 68%, whereas in the harnessed configurations the point estimates of the change lie between -3.7 and +0.5 points. An elicitation format that reduces extreme values thus need not preserve sensitivity to evidence; the two should be tested separately. Because $\delta$-NLI annotates only direction, we make no claim about how large an update should be. Code, data and the frozen plan: this https URL

---


### 160. [Give the Model a Finger: Developmentally Aligned Evaluation of Counting in Vision-Language Models](https://arxiv.org/abs/2610.27756)

**<font color=#1a73e8>作者：</font>** Yingxin Jia, Hui Geng, Wenxin Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are exact on small sets and drift into estimation on larger ones, a profile reminiscent of children before they master counting. Children cross the barrier with epistemic actions: pointing at each item while reciting number words, moving counted items aside, partitioning the array. We give VLMs the same actions as dumb image tools with no visual intelligence of their own in a training-free agent loop. Our central claim is about measurement, not intervention: a model that counts by marking leaves a normally hidden serial procedure on the image, and the developmental principles of counting turn those marks into an interpretable audit of serial visual reasoning: every tag is classified against point-level ground truth as on-target, duplicate, phantom, or omitted, the answer is checked against the number of tags, and order irrelevance is tested by forcing opposite traversal orders. Across 9 models, 682 images, and 7 harness conditions we find that (i) the exact-counting range is a model-specific signature spanning nearly two orders of magnitude (R80 from 3 to 150 dots); (ii) as an intervention the finger mostly fails: tags help 4 of 9 models on small-count photographs, hurt imprecise pointers, and rarely beat a verbal routine or a blind point list; what the loop buys is an auditable trace, not accuracy; (iii) as measurement it succeeds: a tag-perturbation probe shows that precise pointers read their answers off the tags, pointing precision tracks which models benefit, dense scenes fail by omission, and models rarely revise after seeing their own tags; and (iv) the capacities dissociate: models follow an instructed traversal order yet often change their answer when it reverses, and children's regular-over-scattered advantage appears only under the routine and survives lattices that defeat a rows-times-columns shortcut.

---


### 161. [AC/DC on a Budget - Alternating Sparse Phases](https://arxiv.org/abs/2610.27758)

**<font color=#1a73e8>作者：</font>** Rahul Nittala, Advait Gadhikar, Tom Jacobs 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-of-the-art neural network sparsification relies on alternating dense and sparse training phases. While computationally expensive, dense phases are critical for performance. Our empirical analysis reveals the mechanics behind this gain: upon reintroduction, previously masked parameters receive disproportionately large gradients that drive essential mask rewiring and parameter sign-flipping. Building on these insights, we optimize the performance-to-FLOPs Pareto frontier through three innovations: (1) zero-initializing masked parameters during dense phases to promote relevant sign flips, (2) shortening dense phases, and (3) replacing the dense phase entirely with a sparse rewiring phase that updates only the active mask and a small, high-gradient fraction of out-of-mask weights. Evaluated on CIFAR100 and ImageNet, our variant ARC (Alternating Rewiring Compression) matches baseline AC/DC performance at a fraction of the computational cost, establishing a superior performance-to-FLOPs frontier also compared to standard sparse-to-sparse algorithms. Experiments with GPT-2 on OpenWebText further show improvements in validation perplexity and average zero-shot performance

---


### 162. [RITE: Evaluating End-to-End Resilience to Silent Tool Errors in E-Commerce Agentic Systems](https://arxiv.org/abs/2610.27777)

**<font color=#1a73e8>作者：</font>** Wenshuo Zhang, Yuquan Lin, Yushi Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents increasingly answer e-commerce queries through multi-step tool interactions. The expected output of a tool call can shift between agent development and execution, allowing a plausible but incorrect value to be returned without an explicit failure signal. These silent errors may propagate through subsequent decisions into final answers. To study agents' resilience across this end-to-end process, we formulate Silent-error Resilience Task, an interactive task that evaluates whether they complete the original query after a silent error corrupts an intermediate state. We introduce RITE, a benchmark built from human-authored industrial workflows and production-log-derived inputs. To enable controlled and reproducible evaluation, we use a semantic error taxonomy to inject errors into fixed workflow prefixes, freeze recorded tool behavior, and let agents continue freely. It contains 167 matched units across nine e-commerce workflows, yielding 501 silent-error, correct-value, and explicit-failure instances. Across 10 recent LLMs, silent errors roughly halve task success and are consistently harder than explicit failures. Recognition, use of an available verification path, and integration of the resulting evidence form successive bottlenecks. We also propose a light State Checker as an intervention to test whether resilience can be improved.

---


### 163. [GRADUS: Discovering and Recovering Agent Lessons from the Environment's Latent Syllabus](https://arxiv.org/abs/2610.27781)

**<font color=#1a73e8>作者：</font>** Qing Ping, Wei Yang, Panpan Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training LLM agents for policy-constrained tool environments, such as an airline backend with booking, refund, and cancellation policies, requires tasks that exercise the environment's rules individually and in combination. Existing synthesis pipelines let a model propose tasks and retain only those it immediately solves, biasing training data toward easier behaviors. We introduce Gradus (Graded Rungs of Ascending Difficulty from an Underlying System), which decouples what a task should teach from the concrete task and solution used to teach it. Without seed tasks, Gradus treats a fixed environment as a latent syllabus, extracting guarded behavioral operators that capture how actions depend on current conditions and how their effects reshape subsequent decisions. It composes these operators into increasingly demanding tasks while using corpus-level feedback to target missing outcome combinations. Crucially, Gradus jointly calibrates tasks and solutions against the environment: execution feedback identifies which side to refine while preserving the intended behavioral requirements. Verification thus becomes a recovery signal rather than a terminal filter, coupling coverage-guided exploration with the preservation of difficult examples. From off-the-shelf backbones, the resulting curriculum lifts a 30B model from 59% to 89% on $\tau^2$-Bench and from 47% to 83% on CAR-Bench with an Opus 4.5 proposer, and to 76% and 62%, respectively, with an open-weight Qwen3-235B proposer. These results show the value of jointly controlling which behaviors are explored and which survive into verified training data.

---


### 164. [RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation](https://arxiv.org/abs/2610.27782)

**<font color=#1a73e8>作者：</font>** Siyuan Ma, Yu Qi, Cheng Ye 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models are promising foundations for embodied world models, but only if their generated rollouts are physically valid and faithful to task instructions. Multimodal large language models (MLLMs) are increasingly used to judge these properties, yet their agreement with human judgments on embodied videos has not been systematically evaluated. To address this gap, we introduce RoboJudge-Bench, a benchmark for evaluating MLLMs as judges of embodied video generation. The benchmark measures two fundamental dimensions, Physical Adherence and Instruction Alignment, across 800 human-annotated videos from 8 source corpora and 10 video generators, spanning grippers, human hands, and dexterous hands. Experiments reveal uneven alignment between existing judges and human ratings: general-purpose MLLMs show lower agreement on physical adherence, while specialized video judges designed for general-domain physical reasoning do not consistently transfer to embodied scenarios. Motivated by these findings, we construct RoboJudge-Train, comprising 12K videos annotated with 25K human-verified scores and model-assisted rationales for Physical Adherence and Instruction Alignment. We fine-tune a 9B MLLM on this dataset with supervised learning followed by reinforcement learning, yielding RoboJudge-9B. Among the model judges evaluated on RoboJudge-Bench, RoboJudge-9B achieves the highest overall agreement, reaching a Pearson correlation of 0.719 with a statistically significant 0.089 gain over Gemini-3.7-Flash, the best-performing proprietary baseline in our evaluation. Training on RoboJudge-Train also yields gains on external benchmarks, including VideoPhy2 and Physion-Eval. We further use RoboJudge-9B as a downstream evaluator to benchmark video generation models according to Physical Adherence and Instruction Alignment.

---


### 165. [Are Linguistic and Arithmetic Circuits Dissociated in LLMs?](https://arxiv.org/abs/2610.27790)

**<font color=#1a73e8>作者：</font>** Riku Kisako, Tatsuki Kuribayashi, Ryohei Sasano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit both knowledge of language, rendered by, for example, grammatical judgment ability, and abilities to perform tasks through language, such as math-word problem solving. Motivated by neurolinguistic studies of their neural dissociation in human brains, in this study, we investigate the overlap of their circuits in large language models (LLMs). Specifically, we examine the overlap and causal effects between the circuits extracted for linguistic and arithmetic tasks, using controlled materials and circuit discovery methods from the mechanistic interpretability field. Our experiments with five LLMs show that circuit similarity is mostly explained by task domains (linguistic vs. arithmetic), rather than by their input and output vocabularies or by the syntactic similarities between natural-language sentences and arithmetic expressions. This finding suggests that LLMs may process linguistic and arithmetic information using largely separate neural circuits, highlighting an ability-based modular organization of circuits within these models.

---


### 166. [Toward Agentic AI for the 6G Physical Layer: From Algorithm Discovery to Verified Baseband Silicon](https://arxiv.org/abs/2610.27797)

**<font color=#1a73e8>作者：</font>** Eric Mittag, Lukas Brechtel, Maximilian Stark 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> 6G will be designed faster than it can be built: AI-driven search already proposes physical-layer algorithms at machine speed, while carrying a single one onto embedded baseband silicon remains specialist work. That silicon imposes hard memory and numeric limits, but also exposes cost structures a GPU lacks, and a design flow that never runs on the target sees neither. We present an agentic workflow in which an LLM coding agent implements algorithms on a commercial baseband SoC, optimizes them down to agent-written vector assembly, and validates them on silicon. The agent is guided by a knowledge base of measured platform facts, checked at every step against evaluators it is instructed never to edit, and metered per phase. We showcase the workflow on an AI-discovered orthogonal time frequency space (OTFS) detector portfolio on the open 6G4All platform. It yields twelve kernels that run cycle-exactly on silicon, their optimized versions at 18k-405k cycles (30-660 $\mu$s) per frame. It also yields a new detector shaped by the chip's measured costs that needs 13.9% fewer cycles than the port of the discovered detector while matching its error rate, with a measured edge our evaluation cannot statistically resolve, a structure that a hardware-blind search objective had no reason to find. What is not specific to OTFS is the workflow: an LLM agent exploring an implementation space under real hardware limits, with the cost of every choice measured rather than assumed.

---


### 167. [SliMOO: Interpretable Multi-Objective Evolutionary Search for LLM Depth Pruning](https://arxiv.org/abs/2610.27812)

**<font color=#1a73e8>作者：</font>** Guanchen Li, Yixing Xu, Xuanwu Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) grow more powerful, their scale makes them costly to serve. Depth pruning offers a practical route to efficiency by directly reducing memory and latency without hardware-specific support. However, we observe that transformer layers exhibit markedly different task-dependent layer contributions, whereas existing depth-pruning methods ignore this heterogeneity and thus tend to optimize for a narrow domain or benchmark rather than preserve broad capability. This suggests that LLM depth pruning should be formulated as a multi-objective optimization problem rather than a single-score ranking problem.
We propose SliMOO, an interpretable multi-objective evolutionary search framework for LLM depth pruning. SliMOO first uses single-layer removal probing to construct a task-layer importance map, which provides an interpretable view of task-shared and task-specific layers and serves as a search prior. It then performs a Pareto-aware evolutionary search for pruning masks, where candidates are generated under the guidance of the task-layer prior, scored by their deviation from the dense model on each task, and retained through NSGA-II environmental selection. Across the Llama-3.1 and Qwen3 model families, SliMOO consistently achieves stronger multi-task trade-offs than rule-based, greedy, and scalarized baselines. For example, on Llama-3.1-70B at 25% sparsity, it improves the math-domain average from 24.33% to 34.40% and the code-domain average from 35.03% to 39.14%. Code will be made available at this https URL.

---


### 168. [ProVe: Proposer-Verifier Decoding](https://arxiv.org/abs/2610.27815)

**<font color=#1a73e8>作者：</font>** Ziqi Jin, Weiwen Xu, Jiaxi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive (AR) language models by letting a small model draft tokens serially and a large model verify them in parallel. We reverse these roles. Starting from a standard AR checkpoint, we fine-tune the large model into a proposer that predicts a block of future tokens in a single forward pass, then use one additional forward pass to verify the proposed block. This gives ProVe, Proposer-Verifier decoding. The verifier can be a smaller AR model or the proposer itself; the latter gives ProVe-lossless, which reproduces the proposer's greedy AR decoding. Block proposals already provide substantial room for acceleration: with a block size of 16, the proposed block has an average AR-matching prefix of 6.6 tokens on GSM8K. Across six benchmarks with a 32B proposer, ProVe-lossless reaches 2.5x average AR throughput without training a separate draft head. With a small 3B verifier, ProVe reaches 2.7x average throughput at 2.6 accuracy points below AR on the six-task average, providing a controllable tradeoff between speed and accuracy.

---


### 169. [Privacy-preserving inference on hosted models: a learned input-embedding transform for frozen Qwen3.8-27B](https://arxiv.org/abs/2610.27817)

**<font color=#1a73e8>作者：</font>** Mahendra Roopa, Srikanth Roopa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every prompt sent to a hosted language model is readable by whoever runs it. We study whether the prompt can remain on the client while the host receives transformed vectors that stand in for it. A language model converts text to vectors exactly once, with a public lookup table; we perform that step locally and pass the vectors through a small trained network (55.6M parameters) before they leave the perimeter. The host runs a frozen 27B model (Qwen3.8-27B) on the transformed vectors and never receives text or token ids. We train the transform against the frozen model as a fixed judge, combining a forward-KL utility term with an auxiliary term that pushes each vector away from its original direction. On 1,490 MMLU questions held out from training, the transform costs 1.5 points of accuracy (80.7% vs. 82.3%), breaking 68 of the 1,226 questions the unmodified model answers correctly (5.5%), while 30.1% of content tokens no longer decode to their original token under a nearest-neighbour lookup.

---


### 170. [SMART: Semantic Segment Mapping and Assessment of Recognition Transcripts with Contextual Rubrics](https://arxiv.org/abs/2610.27820)

**<font color=#1a73e8>作者：</font>** Xiaoyu Gu, Chencheng Wang, Fuyang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Word error rate (WER) assigns equal cost to lexical edits despite their different semantic consequences, while overall semantic scores cannot identify which individual errors alter the intended meaning. We formulate ASR semantic evaluation as context-aware, segment-level consequence assessment and propose Semantic Segment Mapping and Assessment of Recognition Transcripts with Contextual Rubrics (SMART), a framework for traceable semantic evaluation and targeted ASR correction. SMART maps reference-hypothesis discrepancies into coherent segments and applies a structured contextual rubric to assign explicit consequence labels. These labels support Semantic Impact Error Rate (SIER), which quantifies consequential errors at utterance, chunk, and lexical levels. Against majority-vote human labels, SMART achieves 0.843 F1 versus 0.745 for direct LLM judgment. Evaluation across multiple LLMs further demonstrates that SMART is relatively insensitive to the choice of evaluation model, while MER and SIER reveal different aspects of ASR quality. A separate target-reference-free rubric guides correction using the target hypothesis and surrounding ASR hypotheses, outperforming a matched w/o Rubric baseline on both datasets, with further absolute reductions of 0.85-0.98 percentage points in MER and 1.18-1.65 percentage points in SIER_lex.

---


### 171. [COMPASS: Routing via Capability-Oriented Model Profiling with Adaptive Search, Selection, and Tool Use](https://arxiv.org/abs/2610.27822)

**<font color=#1a73e8>作者：</font>** Amin Rezaei, Pouya Parsa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM routing aims to select a capable model at low cost, but specialized routers can require updates as models and tasks change. We propose COMPASS, an agentic router in which an LLM follows a routing recipe, gathers performance and cost evidence through tools, and optionally inspects candidate answers before selecting a model. Our evaluations on LLMRouterBench and DeepSWE show that agentic routing can improve accuracy and lower model-call cost relative to specialized and trained routing baselines, without routing-specific training. On LLMRouterBench, COMPASS reaches 69.85% accuracy at \$139.57, compared with RLCascadeRouter's 69.14% at \$180.22. On DeepSWE under fixed five-fold cross-validation, it reaches 78.1% at \$215, compared with 74.1% at \$500 for the best single model. COMPASS also supports routing across benchmarks and adapts to an expanded model pool by reading new evaluation records, without changing the router's weights or prompt.

---


### 172. [GARRET: Generative Feedback for Region Retrieval in Visual Documents](https://arxiv.org/abs/2610.27829)

**<font color=#1a73e8>作者：</font>** Weijian Jian, Siyang Chen, Yuguang Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal retrieval-augmented generation over visually rich documents requires evidence at a finer granularity than entire pages. Existing visual retrievers typically index or return full pages, whereas training region-level retrievers often requires costly query-to-region annotations or noisy model-generated labels. We introduce GARRET, a region-retrieval framework trained from (page, question, answer) triplets through differentiable generative feedback. A shared context-preserving retriever produces page and region multi-vector representations. During training, their retrieval scores define a soft routing distribution over candidate region crops. An auxiliary vision-language model attends to each crop separately, aggregates crop-specific contexts using the routing weights, and predicts the question followed by the answer under a next-token prediction objective. Gradients through the routing distribution assign query-conditioned credit to the indexed region representations, without requiring query-to-region annotations. At inference, the auxiliary model is removed. GARRET also reuses the contextualized region representations, together with page summary tokens, to construct a compact page representation. We introduce ViDoRe-V3-Region, a corpus-wide benchmark containing 200,682 fixed candidate regions across eight domains. GARRET achieves a macro nDCG@10 of 0.4126, outperforming the strongest visual baseline by 2.94 points. On page retrieval, it remains comparable to ColQwen2.5-v0.2 while indexing 47.8% fewer vectors per page.

---


### 173. [SciDiagBench: A Type-Specific Benchmark for Human-Aligned Evaluation of Scientific Diagrams](https://arxiv.org/abs/2610.27841)

**<font color=#1a73e8>作者：</font>** Hao Wang, Zixuan Li, Long Bai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent agents have demonstrated strong capabilities in generating images from textual prompts, motivating their utilization for scientific diagram generation. Scientific diagrams naturally span diverse types, each characterized by distinct visual structures and content organization. Consequently, during peer review and other scientific evaluation, human experts naturally consider type-specific criteria when assessing their quality. However, existing VLM-based evaluation benchmarks fail to reflect the above human evaluation practices for two main reasons: 1) benchmark datasets typically lack a systematic categorization of different diagram types and thus adopt the same generic criteria for all diagrams, and 2) their evaluation criteria are often designed heuristically, without explicit alignment to human evaluation preferences. Motivated by these limitations, we introduce SciDiagBench, which consists of a benchmark dataset that systematically categorizes scientific diagrams into 11 types and a human preference-guided evaluation method. Specifically, SciDiagBench contains 165 scientific diagrams across 10 broad domains, with types including graphical abstracts, technical roadmaps, and illustrative cases. Based on this dataset, SciDiagBench develops an evaluation method that leverages a preference-guided calibration process to incorporate human preferences into the generation of type-specific criteria. Ultimately, SciDiagBench enables more reliable automated evaluation that better aligns with human evaluation across diverse scientific diagrams.

---


### 174. [SAPD: Learning from Agent Experience without Environment Interaction](https://arxiv.org/abs/2610.27847)

**<font color=#1a73e8>作者：</font>** Juncheng Diao, Haibin Wang, Wei Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling the training of Large Language Model (LLM) agents typically requires a large collection of executable environments, whose construction, maintenance, and operation constrain the expansion of training experience. Existing offline trajectories offer an opportunity to reuse interaction experience, yet effectively refining the current policy without revisiting these environments remains challenging: supervised fine-tuning (SFT) can lead to catastrophic forgetting, while online reinforcement learning requires real-time interaction with the environment. To address this challenge, we propose Step-Advantage Policy Distillation (SAPD), a method for learning from offline trajectories using relative step advantages. SAPD decomposes multi-turn trajectories into individual decision contexts for on-policy distillation, allowing the student to generate responses conditioned on recorded histories, and introduces relative step advantage signals to stabilize training. The entire process requires neither new environment observations nor additional multi-turn interactions. Experiments on ALFWorld, WebShop, and Search-based QA show that SAPD improves performance across different teacher configurations, mitigates catastrophic forgetting compared with SFT, and runs at least $4.7\times$ faster per training step than online OPD. We will release our code soon.

---


### 175. [LaLa-World: Scaling Latent World Models with Natural Language Actions](https://arxiv.org/abs/2610.27851)

**<font color=#1a73e8>作者：</font>** Junha Song, Geonmo Gu, Jeongeun Park 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper shows that JEPA-style latent world models (LWMs) can learn across diverse domains and data sources by adopting the language-conditioned interface of video generation models. We establish this approach as an effective and efficient basis for planning with imagination and downstream policy fine-tuning. To this end, we introduce LaLa-World, a Language-conditioned Latent World model that learns from simulation and robot trajectories together with broader image and video data. Two designs make this work. First, we describe both numerical actions and visual changes in language, enabling joint training of a single future predictor across heterogeneous datasets. Second, we build the predictor on a language model, allowing it to interpret language conditions while predicting future latent states. The resulting predictor achieves higher average MPC planning performance than existing LWMs trained separately for each domain or task. Adding image and video data further improves average planning performance and robustness to action phrasing. In a matched comparison with an RAEv2-based video generation model baseline, LaLa-World reaches comparable planning performance with $6\times$ less training cost and $13.9\times$ faster planning. Beyond planning, the pretrained LaLa-World serves as an initialization for LaLa-Policy, which jointly predicts actions and future visual representations. LaLa-Policy performs competitively with Cosmos Policy on LIBERO and RoboCasa, with up to $5.5\times$ faster inference.

---


### 176. [UvA-MT's Participation in the WMT26 General Translation Shared Task](https://arxiv.org/abs/2610.27852)

**<font color=#1a73e8>作者：</font>** Di Wu, Sergey Troshin, Wafaa Mohammed 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents UvA-MT's submission to the WMT 2026 General Machine Translation shared task, competing in the unconstrained track across all 23 translation directions. This year, we fully leverage the test-time methods of Large Language Models (LLMs) for machine translation. Specifically, (1) we use sequential sampling with a refinement prompt to generate a pool of translation candidates for each source segment, a strategy shown to outperform traditional parallel sampling; and (2) we employ LLMs as pairwise judges to select the best candidate via a round-robin voting mechanism, with offline evaluation on the WMT25 benchmark showing a very clear improvement over point-wise best-of-N selection. Combined, these two strategies form our WMT26 submission.

---


### 177. [Physical Operating-Condition-Guided Vision-Language Matching for Cavitation Diagnosis in Industrial Pipeline Systems](https://arxiv.org/abs/2610.27860)

**<font color=#1a73e8>作者：</font>** Yu Sha, Junqi Tao, Deyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cavitation diagnosis in industrial pipeline systems is challenging because acoustic responses vary substantially with operating conditions, while similar time-frequency patterns may correspond to different cavitation states. To address this issue, we propose a physical operating-condition-guided vision-language matching (POC-VLM) for cavitation diagnosis. POC-VLM first constructs physical operating-condition-aware semantic descriptions by explicitly incorporating sample-specific operating variables into candidate cavitation texts. A time-frequency-conditioned text adaptation module then dynamically aligns these physical semantics with the observed acoustic response, followed by global-local vision-language matching to capture both holistic and localized discriminative patterns. In parallel, a K-nearest neighbours-based non-parametric physical operating-condition prior estimates the physical plausibility of each candidate state and is fused with the vision-language semantic evidence at the decision level. Experiments on three real-world cavitation datasets show that POC-VLM consistently outperforms representative data-driven, multimodal and domain-specific diagnostic methods. Further analyses verify the complementary roles of vision-language semantic matching and physical operating-condition priors, while demonstrating robust performance under varying sampling rates, noise levels and observation durations.

---


### 178. [Gaze2HOI: Gaze-Aware Intention Disambiguation for Egocentric Hand-Object Interaction Forecasting](https://arxiv.org/abs/2610.27877)

**<font color=#1a73e8>作者：</font>** Chuanyang Ma, Chenye Wang, Yixuan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anticipating how users will interact with their surroundings is essential for proactive systems that provide timely assistance in AR, VR, and embodied applications. Prior work typically forecasts hand-object interactions directly from historical observations, leaving intention and contact geometry implicit. However, similar observation histories can precede semantically or geometrically distinct futures. Inspired by behavioral evidence that gaze can provide early cues for underlying intention, we propose Gaze2HOI, a gaze-aware framework that formulates hand-object interaction forecasting as a hierarchical problem comprising intention inference, contact grounding, and coupled hand-object motion generation. Specifically, Gaze2HOI first weights gaze cues by fixation strength and recency, and uses them to modulate the visual representations of a vision-language model (VLM) through Temporal Gaze Saliency Modulation (TGSM), thereby reducing semantic ambiguity in intention inference. Subsequently, an Anticipatory Contact Grounding (ACG) module maps these structured intentions into explicit contact, support, and placement fields, effectively mitigating geometric ambiguity. Driven by these explicit conditions, a diffusion-based model jointly generates the 6-DoF object trajectories and future articulated motion of both hands. To evaluate Gaze2HOI, we further introduce EgoAIM, a phase-aware benchmark that organizes egocentric hand-object interactions into four phases defined by evolving hand-object relations and provides fine-grained intention annotations. Extensive experiments demonstrate that Gaze2HOI achieves state-of-the-art performance in both intention inference and motion forecasting, even approaching oracle-level end-to-end performance in specific interaction phases. Project page: this https URL.

---


### 179. [Testing Associative Creativity in Humans and Multimodal LLMs with Difficult-to-Name Visual Stimuli](https://arxiv.org/abs/2610.27894)

**<font color=#1a73e8>作者：</font>** Manar Ali, Lisa Gottschalk, Simeon Junker 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate associative creativity in descriptions of abstract visual stimuli by humans and multimodal large language models (MLLMs). While conceptual association is central to human communication, it remains unclear how humans and models adapt when visual stimuli become increasingly difficult to map onto familiar semantic concepts. We evaluate several state-of-the-art MLLMs and human participants along two dimensions of creativity, originality and effectiveness, using two datasets with controlled manipulations of difficulty. SilCC varies naming difficulty through progressively more complex combinations of abstract shapes, and PixCC varies difficulty through increasing levels of random visual noise. Results show that humans produce more diverse associative descriptions than MLLMs, including greater semantic distance, higher entropy, and more novel expressions relative to reference lexica. As difficulty increases, effectiveness declines in SilCC, and humans increasingly shift from holistic associations to descriptions of low-level visual properties in PixCC.

---


### 180. [The Shape of the DPO Hyperparameter Landscape: What to Measure, How It Moves with Scale, and When Not to Transfer It](https://arxiv.org/abs/2610.27895)

**<font color=#1a73e8>作者：</font>** Hannan Mahadik, David Salinas, Jacek Golebiowski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct preference optimisation (DPO) is widely used for language model post-training, but its performance depends strongly on the choice of its hyperparameters, such as the learning rate and the reference-policy regularisation parameter $\beta$. To better understand the DPO hyperparameter landscape, we conduct extensive experiments using a dense hyperparameter grid across different model scales from the same family. This allows us to analyse how the optimal DPO hyperparameters evolve with model size and the number of update steps, with intermediate checkpoints providing an inexpensive signal to accelerate the hyperparameter optimisation process. Furthermore, by evaluating our models on both static and dynamic benchmarks, we identify which benchmarks provide the strongest signal for hyperparameter selection. Finally, we investigate how different state-of-the-art hyperparameter optimisation strategies perform in this setting. Our experiments show that the optimal learning rate varies with model size and that hyperparameters are not transferable across training datasets. We also find that validation loss is a poor proxy for hyperparameter optimisation, as hyperparameters that minimize validation loss only weakly correlate with optimal hyperparameters for downstream benchmarks. Therefore, DPO hyperparameters need to be tuned specifically for the target model, dataset, and evaluation objective. We also show that short candidate training runs can substantially reduce the cost of this selection. We release all our training configurations and evaluation results to support reproducible analysis of selection quality and training cost.

---


### 181. [CollabSciReM: Aligning Language Models for Scientific Conversations via Science-Aware Reward Decomposition](https://arxiv.org/abs/2610.27901)

**<font color=#1a73e8>作者：</font>** Sasi Kiran Gaddipati, Gollam Rabby, Sören Auer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used as research collaborators for hypothesis refinement, methodological planning, and technical analysis across multi-turn interactions. In this setting, a useful assistant must be accurate, methodologically justified, logically consistent, and token-efficient. Current alignment approaches rarely achieve all of these together. Instruction-tuned models gain conversational quality through verbosity, and we show that science-agnostic general collaborative rewards compress responses at the expense of scientific rigor. We propose CollabSciReM, a goal-conditioned reward framework that decomposes the session-level reward into conversational quality, scientific rigor, and structural efficiency. We also introduce SciQuality, a pairwise evaluation of multi-turn research conversations grounded in 300 held-out scientific papers and scored on six dimensions: methodological soundness, justification, logical consistency, factual correctness, novelty, and responsiveness. Fine-tuned on 8.62K synthetic research conversations, CollabSciReM is preferred on SciQuality over a science-agnostic reward baseline trained on the same data for all four Llama and Qwen models, including a 65.3% win rate at matched response length. For the 7B and 8B models, CollabSciReM outperforms the science-agnostic reward baseline on the primary metric in 8 of 10 single- and multi-turn benchmark settings. In a blind study, domain experts rated CollabSciReM significantly higher on novelty than the general-reward variant and reported fewer hallucinated responses than both the general-reward variant and the base model.

---


### 182. [MMEnterprise-Bench: Evaluating Enterprise Agents over Evolving Multimodal Records](https://arxiv.org/abs/2610.27911)

**<font color=#1a73e8>作者：</font>** Seohyun Lee, Jongha Kim, Dohwan Ko 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise agents answer questions over workplace records that evolve through team collaboration. As information is shared, corrected, and revised across documents, chats, and figures, multiple versions of the same information accumulate in the workspace. Reliable question answering therefore requires agents to reason over sufficient evidence, resolve cross-source and temporal conflicts, and recognize when the available evidence is insufficient to establish an answer. To systematically evaluate these capabilities, we introduce MMEnterprise-Bench, a benchmark comprising 1,613 questions grounded in evolving multimodal records from simulated collaboration projects, covering three categories: Evidence Reasoning, Conflict Resolution, and Unanswerability. We evaluate 10 proprietary and open-source multimodal LLMs and find that even the strongest models struggle when evidence contains cross-source or temporal conflicts or spans multiple images. Moreover, increasing the retrieval budget or employing a larger retriever improves evidence recall but does not consistently translate into higher answer accuracy. These findings highlight the persistent challenges of reasoning over evolving workplace records and establish MMEnterprise-Bench as a testbed for developing more reliable enterprise agents. Code and data are available at this https URL.

---


### 183. [ACE-Compression: An Ability-Centric Evaluation of Compressed Large Language Models](https://arxiv.org/abs/2610.27913)

**<font color=#1a73e8>作者：</font>** Jiahui Ning, Liang Chen, Yuchen Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model compression makes large language models deployable, but today's evaluation tells an incomplete story. Standard practice measures retained task performance and stops there. This misses a critical fact: compression perturbs the distributed knowledge embedded across billions of weights, and task scores alone cannot reveal which underlying abilities survive and which quietly collapse. To solve this question, we introduce ACE-Compression, an ability-centric evaluation framework. Instead of asking only "does the compressed model still answer correctly?", we ask "which of its core abilities remain intact?" Our framework probes four deployment-facing dimensions: procedural reasoning and constraint execution, knowledge grounding and truthfulness, social cognition and affective understanding, and persona fidelity and stylistic consistency. Across more than 35 compressed checkpoints from six open-weight LLMs-covering quantization and pruning-we find that compression redistributes ability profiles. Coarse, local, and surface-level signals often persist, while fine-grained, long-tail, and context-dependent abilities become fragile. Quantization consistently outperforms pruning in retention, but the practical meaning of that gap depends entirely on which ability an application requires. Based on our findings, deployers can choose compression methods by the ability profile their application needs, not just by a leaderboard average. And algorithm designers gain diagnostic signals to build compression methods that preserve what matters. We believe that ACE-Compression turns compression from a black-box accuracy drop into an interpretable intervention-one we can measure, understand, and ultimately improve.

---


### 184. [Why Do LLMs Accept Generics? Explaining Acceptability using Psycholinguistic and Model-Derived Factors](https://arxiv.org/abs/2610.27928)

**<font color=#1a73e8>作者：</font>** Mervat Abassy, Zhaoxin Feng, Tatsuki Kuribayashi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Psycholinguistic studies explore why humans accept some generic statements but reject others by showing that these judgments depend on more than how common a property is. People consider several other factors such as how well it sets the kind apart from others or whether it is characteristic of the kind.
Inspired by the linguistic and cognitive literature, we explore to what extent factors from these studies explain how large language models (LLMs) judge generics. Our results with twelve models on a psycholinguistic dataset and on naturally occurring generics show that models weigh how common a property is against how well it distinguishes the kind, and combine the two much as people do, though less clearly. Like people, they favor characteristic properties, but unlike the accounts of human judgment, they ignore striking ones. What matters most to LLMs is whether a statement is factually true, and much of the influence of human factors reaches their ratings through that judgment. In six 7-9B models, shifting the hidden states along each factor's direction moves the judgment as the factor predicts.

---


### 185. [From DQI to C-DQI: Automatic Codebook Generation and Evaluation for Measuring Computational Discourse Quality Index](https://arxiv.org/abs/2610.27937)

**<font color=#1a73e8>作者：</font>** Esther Shizgal, Ron Keinan, Daniel Shtauber 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective democratic deliberation is vital for civic engagement and the health of legislative institutions. However, assessing parliamentary discourse quality is traditionally done using expert-scored, theory-based codebooks (CBs), which are rigid, labor-intensive, and prone to biases. While Large Language Models (LLMs) offer a scalable alternative for both schema induction and discourse annotation, ensuring schema quality and mitigating models' inherent bias remains a clear challenge. In this work, we propose a complete protocol for LLM-based codebook generation and evaluation. Starting from the widely accepted discourse quality Index (DQI), we compare top-down (theory-based), bottom-up (data-driven), and hybrid approaches for generating context-adapted schemas. To evaluate these schemas, we define an extrinsic proxy measure, validated by manual annotations, alongside an intrinsic inter-model agreement (IMA) metric, which leverages differing model biases to signal overall reliability. Our experiments on 100 Israeli parliament transcripts reveal that inductive, data-driven schemas achieve higher IMA than top-down methods while maintaining validity, demonstrating their potential for reliable, large-scale analysis of political discourse.

---


### 186. [Near-Duplicate Image Selection Transfers Preferences in Vision-Language Models](https://arxiv.org/abs/2610.27943)

**<font color=#1a73e8>作者：</font>** Jaeyoung Kim, Eunseok Kim, Dongsuk Jang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subliminal learning is the phenomenon in which a model transmits its preferences to another model through data that do not explicitly express them. As models increasingly curate training data for other models, we ask whether this transfer can arise from choosing among near-duplicate images while keeping the source photographs and human-written captions fixed. For each photograph, a curator selects one of eight near-duplicate variants by caption likelihood, without target-specific prompts. Students trained on target-preferring curators' selections show higher mean target-versus-alternatives log-likelihood ratios in an image-free readout than students trained on neutral selections. Under a prespecified decision rule, this directional shift appears for an owl target in LLaVA-1.5, Qwen2.5-VL, Qwen3-VL, and Gemma 4, with curators and students initialized from the same base checkpoint, and target rotations move it toward camels, oak trees, and a political figure. The owl target-selected student also scores above all count-matched random-reselection students in three models and above 55 of 60 in LLaVA-1.5, and Qwen3-VL shows the shift again on a new source bank with newly trained curators. Its size depends on dataset size, learning rate, and training budget; greedy choices among the eight options move toward the target by 10.4 percentage points in Qwen3-VL and 0.5-1.3 points elsewhere. First-generation students also pass the owl preference to a second generation through captions without explicit owl mentions in LLaVA-1.5 and Qwen3-VL. Thus even a deduplication-style choice among near-identical copies can shift students' target-relative readouts with source photographs and captions fixed; the tested linear probes classify the selecting arm with accuracies up to 59.7% (chance 50%).

---


### 187. [In PRAISE of Attributes: Grounding Retrieval Geometry with Query-Conditioned Subspaces for Person Re-Identification](https://arxiv.org/abs/2610.27944)

**<font color=#1a73e8>作者：</font>** Rajarshi Bhattacharya, Aryan Shukla, Shakeeb Murtaza 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Person re-identification (ReID) ranks an image gallery using either an image query or a textual query. In image-to-image (I2I) ReID, viewpoint, illumination, occlusion, and background changes can make distractors appear more similar than the true match. In text-to-image (T2I) ReID, incomplete or ambiguous descriptions may omit key visual evidence. We study this problem for vision-language model (VLM) based ReID, where attributes such as clothing color and carried objects provide useful fine-grained matching cues. However, directly using attribute-prompt similarities as retrieval scores is unreliable because templated prompts can be biased, correlated, and poorly calibrated. We therefore propose \textbf{PR}ompt-guided \textbf{A}ttribute-based \textbf{I}nference-time \textbf{S}imilarity \textbf{E}nhancement (\texttt{PRAISE}), a query-side test-time adaptation framework for VLM-based ReID. Instead of treating prompts as scores, \texttt{PRAISE} uses a transferable attribute-prompt bank to construct an \emph{Attribute-Conditioned Subspace} (ACS): a query-dependent low-rank subspace induced by the most compatible attribute prompts. ACS provides a controlled attribute-conditioned geometry for reshaping query--gallery affinities and guiding lightweight inference-time updates without identity or attribute labels. Experiments across multiple I2I- and T2I-ReID benchmarks show that \texttt{PRAISE} consistently improves VLM retrieval backbones and outperforms both generic and ReID-specific TTA baselines.

---


### 188. [Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via Goal-Oriented Action Replay](https://arxiv.org/abs/2610.27954)

**<font color=#1a73e8>作者：</font>** Byeonghun Bang, Sangwoo Park, Jinheon Baek 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large (vision) language models have enabled computer-use agents that automate digital workflows via fine-grained keyboard and mouse operations. However, such agents remain fragile in long-horizon settings, where errors accumulate and executed actions leave unintended side effects, making the ability to recover from failures critical. Yet, existing remedies remain inadequate: environment resets are infeasible in proprietary settings, action replay is prohibitively expensive over long horizons, and API-based rollback is limited to web environments, leaving model-based recovery largely unexplored. To address this gap, we present ReTrace, a scalable evaluation framework for systematically studying recovery behavior in computer-use agents. We formalize Transition-Consistent Recovery: identical downstream actions from the recovered and target states must yield identical outcomes. We operationalize this criterion through goal-oriented action replay following controlled error injection. Using ReTrace, we present the first systematic study of autonomous, model-based recovery, revealing that (i) ideal recovery can unlock model's latent task completion capabilities, (ii) current computer-use agents fail to exploit their latent recovery capabilities, and (iii) accurate model-based recovery yields measurable end-to-end gains. Together, these findings establish recovery as a fundamental capability for building reliable computer-use agents. Our code and dataset is available at this https URL.

---


### 189. [Adaptive Stopping of Streamed Reasoning for Language Model Agents](https://arxiv.org/abs/2610.27981)

**<font color=#1a73e8>作者：</font>** JunHyeok Oh, Byung-Jun Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning-enabled language model agents can incur substantial computation before acting, although the reasoning needed varies across decisions. Existing stopping signals, such as confidence and intermediate-answer stability, can vary in effectiveness across reasoning models; signals obtained from hidden states or token probabilities also require internal access that may be unavailable or impractical. We introduce StreamStop, which learns model-specific stopping policies offline from prefix-level action agreement. A frozen prefix reader encodes available reasoning text for a lightweight stop head, allowing stopping without access to the reasoning model's internal signals. We construct and publicly release a dataset of agent reasoning trajectories with prefix-level action annotations. These annotations compare each prefix action with the full-reasoning reference action, enabling offline comparison of stopping rules and exact expected-return optimization of a discounted action-agreement objective. Conditioning the head on the discount factor allows the agreement-token trade-off to be adjusted at inference without retraining. In closed-loop evaluations on WebShop and ScienceWorld, StreamStop achieves higher observed success than most validation-selected fixed-budget settings while using fewer reasoning tokens than Full thinking. On WebShop with Qwen3.8-27B, it uses 42% fewer reasoning tokens per episode with similar observed task success.

---


### 190. [Building Telecom Language Models with RSOD: Domain Data, Specialist Post-Training, Memory-Conscious Distillation, and Networking Evaluation](https://arxiv.org/abs/2610.27993)

**<font color=#1a73e8>作者：</font>** Anil Srirangapatna Nagesh, Nitin Gupta, Anuj Taneja 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Telecom language models must combine broad networking knowledge with specialist behavior across routing, broadband services, access technologies, and operational diagnostics while remaining practical to deploy as a single model. We present an end-to-end framework that builds source-grounded synthetic training data from structured networking taxonomies and expert graphs, materializes 212,559 routed training records across fourteen networking routes, trains six frozen specialist LoRA teachers over one shared continued-pretrained backbone, and consolidates their behavior into one deployable student adapter using Routed Specialist On-Policy Distillation (RSOD). In RSOD, the committed student generates each trajectory, the route-assigned specialist teacher-forces the exact native token sequence, compact teacher hidden states are reconstructed through the shared frozen output head, and only the student LoRA is updated. A controlled reconstruction validation shows mean absolute logit error of 7.26 x 10^-6 with 100% top-1 agreement between native and reconstructed teacher logits. On four RTX 6000 Ada GPUs, the completed 2,000-step run produced 16,000 trajectories with zero observed student-version or token- ID mismatches. Under the primary route-conditioned evaluation over 2,850 held-out questions, the raw Meta-Llama-3.1-8B-Instruct model scores 12.8661/25 micro (13.0172/25 macro), the combined routed six-teacher system scores 21.7641/25 micro, and the consolidated RSOD student, released as Llama-CalixCLM v1, reaches 21.7112/25 micro (21.8006/25 macro) on the same five dimension LLM-judge rubric. Under a separate neutral deployment-like prompt, the same student reaches 20.0028/25 micro (20.0778/25 macro). The consolidated student remains within 0.0529 micro-score points of the combined routed-teacher system while retaining a numerically validated and auditable train-serve execution path.

---


### 191. [Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds](https://arxiv.org/abs/2610.27999)

**<font color=#1a73e8>作者：</font>** Jihai Zhang, Runjia Qian, Kaiqin Kong 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Moving from controllable videos to genuinely playable worlds requires persistent world state, executable game rules, and low-latency interaction. We outline a roadmap for the next generation of Matrix-Game that separates game execution from visual generation through an executable game harness, and introduce Matrix-Game 4.0 as the first system built on this design. A lightweight game engine maintains world state and executes interaction rules, a multimodal coding agent translates player ideas into game code and dynamic scene captions, and a renderer based on autoregressive video model transforms engine-rendered low-poly proxies into detailed visuals, conditioned on dynamic captions and memory references. This framework provides continuous guidance for visual generation and enables natural-language creation and modification of scenes and gameplay. Our renderer is trained on aligned low-poly and high-fidelity video pairs and distilled into a causal generator that generates in four-frame chunks with one or two denoising steps. Together with targeted inference optimizations, Matrix-Game 4.0 enables 480p, 60 FPS gameplay on a single NVIDIA RTX5090 with a key-press-to-display latency of 112ms. Single-step generation achieves 83FPS steady-state throughput with 18.2GiB of peak GPU memory usage. With fixed prompts, steady-state throughput also reaches 67FPS on an RTX5080 and 58FPS on an RTX5070Ti. We demonstrate customizable shooter and driving games with engine-enforced mechanics, and release code, model weights, and low-poly game assets to support research and creation of playable game worlds.

---


### 192. [Beyond the Evidence Boundary: Behavioral Mirage Under Progressive Degradation in Medical VLMs](https://arxiv.org/abs/2610.28000)

**<font color=#1a73e8>作者：</font>** Edric Castel C. Hao, Rez Samantha Z. Floresca  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> VLMs for medical image interpretation are typically evaluated on clean inputs, despite the progressive evidence loss that can occur in high stakes clinical settings. Existing robustness studies show that performance can degrade while confidence remains high, but do not establish when a previously reliable model-case pair ceases to behave reliably. We introduce a baseline-anchored framework that traces baseline-correct cases through progressive image degradation to identify an empirical evidence boundary, and define mirage as continued commitment at this boundary, regardless of correctness. Across three VLMs on three medical datasets, only MedGemma provides a sufficiently large baseline-correct pool for trajectory analysis. On VQA-RAD, the only dataset in which the question text varies, language-only answerability is associated with baseline correctness (AUROC 0.677) and with commitment at the boundary (AUROC 0.653 to 0.670). MedGemma's post-boundary behavior is heterogeneous, including direct mirage, correct recovery, mirage dissolution, consistent abstention, and oscillation, with mirage rates of 16.0 to 100.0% across dataset-modality pairs. Despite this behavioral heterogeneity, residual-stream probes decode commit-versus-abstain behavior at the boundary with AUROC of 0.895 to 0.994 under nested cross-validation. These results show that progressive evidence loss can produce persistent commitment that output entropy and abstention behavior do not consistently reflect, motivating boundary-aware evaluation, option-order controls, and improved abstention mechanisms for reliable medical foundation models operating under partial observation.

---


### 193. [RANGER: Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards](https://arxiv.org/abs/2610.28010)

**<font color=#1a73e8>作者：</font>** Artem Mikhaylov, Pavel Konoplev, Nikolay Efanov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The integration of Large Language Models and Reinforcement Learning offers a promising direction for complex sequential decision-making tasks, such as multi-hop question answering over knowledge graphs. While LLMs provide strong semantic understanding and reasoning capabilities, they often struggle with precise, multi-step navigation in structured environments. Conversely, RL agents excel at learning navigation policies but are hindered by the difficulty of designing semantically meaningful reward functions. This paper introduces a novel hybrid approach in which an LLM serves as a mentor to an RL agent during training by providing dense, semantically informed reward signals. The RL agent, built on a Transformer-based policy and trained with Group Relative Policy Optimization, learns to navigate a knowledge graph to retrieve relevant information. The LLM evaluates the semantic relevance of the agent's traversed paths, generating reward signals that align the agent's behavior with the information needs expressed in a query. We integrate this Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards (RANGER) into a complete question-answering pipeline and evaluate it on the open question answering datasets. Experimental results show that the proposed approach outperforms both a baseline retrieval-augmented system with classical graph search and one using an RL agent trained with heuristic rewards, achieving a significant increase in NLP metrics and LLM-as-a-Judge scores. Our findings demonstrate that deep integration of LLMs into the RL training loop yields more effective and semantically aligned retrieval policies for complex reasoning tasks.

---


### 194. [P$^3$-VLM: A Point-based Alternative for Grounded 3D Vision-Language Models](https://arxiv.org/abs/2610.28018)

**<font color=#1a73e8>作者：</font>** Anna-Maria Halacheva, Jan-Nico Zaech, Sombit Dey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Examining existing benchmarks for grounding in 3D VLMs reveals a pervasive "semantic leakage" in the evaluation and prompting protocols: a heavy reliance on bounding boxes as spatial prompts or representation primitives. Because bounding boxes are highly informative of object categories, they introduce a shortcut for the models to neglect visual information during 3D VLM training. We demonstrate this with a "blind" LLM that, prompted only with the box coordinates, can perform surprisingly well. To further analyze this shortcut, we propose point-based grounding prompting - querying models with a single 3D point instead of a box. Under this protocol, the accuracy of the blind LLM drops from 36.4% to 18.0% on ScanNet's Nr3D, and similarly degrades for 3D VLMs (e.g. LL3DA).
Building on this insight, we introduce P$^3$-VLM, a novel tri-pathway 3D VLM that supports point-based prompts and achieves 52.1% state-of-the-art accuracy on location-grounded captioning under this setting. To achieve this, we redesign the architecture while keeping it detector-free, scene-centric, and suitable for 3D GS inputs. P$^3$-VLM utilizes three complementary pathways (location-, task-, and context-aware), enabling strong reasoning about scenes without any bounding box dependencies. The key benefit of point-based learning is a consistent improvement across settings: P$^3$-VLM achieves state-of-the-art performance under point-based grounding while also improving robustness, OOD generalization, and performance on ungrounded scene-centric 3D VQA benchmarks, reflecting its reduced reliance on bounding-box shortcuts and resulting stronger visual-spatial reasoning.

---


### 195. [From RL Papers to Framework Code: Inclusion and Review in Seven Open-Source Training Frameworks](https://arxiv.org/abs/2610.28027)

**<font color=#1a73e8>作者：</font>** Taiheng Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Practitioners use reinforcement learning methods for language models through training frameworks, so a method that a framework includes is one configuration change away for its users. We measure how often this happens. We trace seven open-source frameworks for RL post-training through their commit histories and link them to 6,939 screened arXiv papers from January 2025 to June 2026. Of 1,598 papers that propose a general RL training method, 37 reached at least one framework. Across five quarterly cohorts of papers, the number included within 180 days stayed between 5 and 7 while the cohorts grew from 72 to 386 papers. Compared with papers from the same quarters, included papers more often trained policies of 30B parameters or more, at 41 against 10 percent, and more often changed a coefficient, clip, mask or weight in the existing loss, at 29 against 9 percent. Both gaps hold without papers from the companies that maintain the frameworks, while code release was equally common in both groups. The frameworks' issues and pull requests show that few methods are turned away in public. More than nine in ten of the general methods no framework included have no thread there that cites or names them, and many proposals that do appear stay open without a reply. Two further records, the frameworks' issues and the technical reports of 13 large open-weight models, show that users rarely report training failures in public and that the reports state 8 of the 13 widely included methods. We release the data as a tracker that links training failures to framework implementations and lists each framework's contribution rules and earlier proposals.

---


### 196. [TrajEvolve: Trajectory Evolution for Reinforcement Learning with Hindsight Credit Assignment](https://arxiv.org/abs/2610.28060)

**<font color=#1a73e8>作者：</font>** Yi Wen, Hao Chen, Wanyu Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Reinforcement Learning (RL) paradigm has achieved remarkable success in enhancing the reasoning capabilities of Large Language Models (LLMs). However, when applied to long-horizon tasks, it faces severe challenges: i) Due to the high task complexity, the model struggles to sample enough successful trajectories, resulting in slow convergence. ii) Relying solely on sparse final rewards causes all steps to be updated indiscriminately, encouraging redundant step generation. When both the quantity and quality of successful trajectories become difficult to guarantee, the performance is severely constrained. This dilemma stems from the limitations: existing RL paradigms rely entirely on the reasoning capability of base models, lacking the ability to actively optimize trajectories. To address the above issues, we propose a novel trajectory evolution paradigm with hindsight credit assignment, termed TrajEvolve. TrajEvolve not only relies on the trajectory inferred by the model but also generates ``evolutionary trajectories'' by refining low-quality steps in historical trajectories, thereby exposing the policy to high-quality compositions that lie within the base model's support but are rarely sampled within practical training budgets. Furthermore, TrajEvolve reformulates step-level continuous credit assignment as a binary classification task, whether each step is necessary for task completion. This simplification not only reduces the learning difficulty but also enables step labels to be obtained through counterfactual verification, achieving precise identification of redundant steps. Extensive experiments on two datasets demonstrate the superiority of the proposed method.

---


### 197. [Same Judgment, Different Yes: Measuring Multilingual Judgment Profiles in Language Models](https://arxiv.org/abs/2610.28066)

**<font color=#1a73e8>作者：</font>** Haonan Huang, Yuwei Lu, Chengkun Cai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual evaluations often score a model's opening yes or no, a token that also carries model and language answering conventions. We ask when different ways of eliciting and reading an answer recover the same judgment, and when they measure an answer habit. We collect 1.1 million replies from eight models in six languages on up to 105 moral vignettes, varying the question's form, the answer constraint, and the reading of the reply, token or sentence, in both wordings (the FAR-6 battery). Story-level judgment profiles converge across the tested readouts and question forms, except for the yes/no token after a negative interrogative read under a preset mapping: on the same replies, token and sentence profiles agree at a median r = 0.67 across cells, while sentence profiles agree with free-sentence profiles at 0.94, a known linguistic variability. With each language's story consensus removed, a model's profile is nearest to its own in another language for 39 of 48 model-language cells under proposition labels and 15 under free sentences, against 5 expected by chance. Particle, position, and named-term preferences follow their own patterns. A model can keep its judgment and change its yes: scoring that token requires establishing which proposition it affirms.

---


### 198. [Contextual Candour: Role-Aware Graduated Disclosure for LLMs over Mixed-Sensitivity Contexts](https://arxiv.org/abs/2610.28067)

**<font color=#1a73e8>作者：</font>** Devansh Srivastav, David Pape, Samira Abedini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLMs increasingly operate over mixed-sensitivity contexts, where they must reason over information ranging from public to confidential while disclosing only what the user is authorised to receive. Existing approaches enforce access control as a binary decision: either fully answering or refusing, without regulating how much or what kind of information is revealed if access is granted, leading to over-refusal or unintended leakage. We introduce graduated disclosure, an access-control formulation in which the level of detail and sensitivity in a model's response is calibrated to the user's authorisation rather than treated as a grant-or-deny decision. We model graduated disclosure as a disclosure-aware generation problem and propose a reward-based optimisation framework that shapes responses toward level-appropriate abstractions while penalising unauthorised factual leakage, including paraphrases and approximations. We evaluate our approach on enterprise and clinical benchmarks and compare it with prompt-based, gating, and supervised baselines. Experiments show that our method substantially reduces information leakage while preserving correctness and utility. These results suggest that disclosure control must be integrated into the generation process itself to enable secure yet useful LLM deployments.

---


### 199. [MuPACE: Learning to Pace Muon for LoRA Fine-Tuning](https://arxiv.org/abs/2610.28072)

**<font color=#1a73e8>作者：</font>** Jan Kobiolka, Christian Frey, Josif Grabocka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning rate schedules are typically fixed before training begins, yet when fine-tuning large language models with low-rank adapters (LoRA), the appropriate scale varies substantially with the model, task, and adapter configuration. Practitioners re-tune a schedule for every new problem, yet a tuned schedule still cannot react to the training dynamics it encounters. We instead amortize learning rate selection across LoRA fine-tuning problems. We leave the base optimizer, Muon, untouched, so that its normalized update fixes the direction, and meta-learn only the global step size. Our method MuPACE is a small recurrent policy, meta-trained across a distribution of fine-tuning runs, that conditions on the observed trajectory and emits bounded adjustments to an interpretable analytic schedule. On 64 fine-tuning problems, MuPACE outperforms standard fixed schedules at a strong shared default on 64-78% of problems and is on par with the same schedules with per-task tuned peaks. Meta-trained only on models with up to 16 layers, MuPACE transfers one-shot to unseen tasks on models as deep as 64 layers, such as Qwen3-32B and Qwen3.8-27B, where a single run remains competitive with swept schedules.

---


### 200. [WildAIGC-Bench: Can AI Image Detectors Handle the Wild? A Benchmark of Generated and Edited Images in Online Circulation](https://arxiv.org/abs/2610.28087)

**<font color=#1a73e8>作者：</font>** Zijian Yu, Hangwei Zhang, Jun Lan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated images linked to news events and online claims can mislead audiences, enable fraud, or cause public controversy. We introduce WildAIGC-Bench, built through recurring collection across news websites, fact-checking sources, and related social media content. The pipeline combines broad coverage, timely updates, and human-verified labels through scheduled discovery, automatic screening and preliminary annotation, and human review of image-specific evidence. The benchmark contains 407 verified AI-generated or edited images, each accompanied by a source webpage link and an evidence summary. Images retain the conditions encountered online, including compression, screenshots, and recapture. Evaluation of dedicated visual detectors, multimodal large language models, and a simple Perception Encoder baseline reveals substantial recall gaps relative to existing benchmarks. WildAIGC-Bench provides both a practical detection challenge and a basis for continued data expansion and source-based verification. The dataset is released at this https URL.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-299](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
