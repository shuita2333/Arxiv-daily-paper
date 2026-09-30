# 🧠 大模型相关研究 | 2026年10月01日

> 本类共 **515** 篇论文：已确认 **473** 篇，待复核 **42** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 351. [E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models](https://arxiv.org/abs/2609.37533)

**<font color=#1a73e8>作者：</font>** Arseny Ivanov, Alexander Kolesov, Alexander Korotin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion models (MDMs) generate sequences by progressively unmasking several tokens per denoising step, but their reverse process is typically factorized over positions, limiting sample quality in the few-step regime where diffusion's speed advantage over autoregressive decoding matters most. A recent line of work introduces a continuous Gaussian latent, trained as a variational autoencoder, to capture correlations across positions, but such approaches are prone to posterior collapse, where the latent is silently ignored. We propose Enhanced Mixture-of-Experts (E-MoE), which builds the reverse process as a mixture of factorized distributions over a discrete shared latent given by the expert-routing decisions of a Mixture-of-Experts (MoE) backbone, without increasing active parameters over the factorized baseline. Across synthetic multi-modal benchmarks, binarized MNIST, and LM1B, E-MoE improves few-step generation over factorized baselines.

---


### 352. [Why Adaptive Optimizers Underestimate Rare Tokens](https://arxiv.org/abs/2609.37535)

**<font color=#1a73e8>作者：</font>** Sangsidhya Kar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the softmax output layer, a rare token receives a small positive logit gradient on most steps and a much larger negative gradient on the few steps when it is the target. SGD simply adds these contributions. Coordinate-wise adaptive methods such as Adam, RMSProp, and sign descent instead divide each update by a running estimate of its magnitude, and that estimate is largest immediately after the token appears. This imbalance has two effects. At the level of the whole output layer, we characterize which optimizers preserve the mean output embedding: every method whose update is linear in past gradients does, as do Kronecker-factored and orthogonalized methods such as Shampoo and Muon. Adam, Adafactor, Lion, and sign descent do not, and for these methods we obtain an exact step-by-step expression for the change. At the level of an individual rare token, the same normalization shifts the training fixed point. In the unigram model, sign descent lowers the logit of every token that occurs in fewer than half of the minibatches at a constant expected rate. For RMSProp with periodic arrivals, we can solve the fixed point in closed form: if a token is absent for at least two consecutive minibatches, its equilibrium probability is strictly below its data frequency for every learning rate, and the ratio tends to $\kappa/(2(e^{\kappa/2}-1))$. Here $\kappa$ is the mean number of steps between occurrences divided by the second-moment time constant $1/(1-\beta_2)$. In the same model, SGD and AMSGrad retain the unbiased fixed point. We test these predictions both in a unigram model and in a small language model trained from a known generating distribution. With random arrivals, the bias is larger than the periodic formula predicts; in the language model, the optimizers with the biased fixed point also fit the generating distribution less well.

---


### 353. [SkillGym: Training Skill-Use Agents with Automatic Verifiable Environment Generation](https://arxiv.org/abs/2609.37539)

**<font color=#1a73e8>作者：</font>** Renxi Wang, Mingshan Hee, Fajri Koto 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skills equip LLM agents with professional knowledge and guidance to complete long-horizon and complex tasks. Although skills have been widely adopted in recent agent paradigms and harnesses, how to synthesize reliable training data and how to train agents for skill use remain underexplored. In this work, we propose SkillGym, an automatic pipeline to build verifiable environments, collect trajectories, and train skill-use agents. SkillGym first crawls a large volume of skills from the internet, then keeps those whose workflows can run reproducibly offline. A builder-reviewer pipeline is used to construct difficulty-controlled tasks, spanning four task types, each with a reference solution and an executable verifier. With this pipeline, we build 6.8k environments and collect 19k verified successful trajectories for supervised finetuning. Finetuning on these trajectories improves LLMs of different families and sizes, from 2B to 122B parameters across four skill-use benchmarks; Our Qwen3.5-9B SFT model outperforms the 397B untrained model on two of them. Further analysis shows that training teaches agents to invoke skills, raising the rate of reading the relevant skill from 28% to 96%, and that the gains hold across reasoning structures, extending to task types that form a minority of the training data and to skills held out from training

---


### 354. [How Can Recommendation Feedback Evolve Agent Memory?](https://arxiv.org/abs/2609.37544)

**<font color=#1a73e8>作者：</font>** Shanwen Mao, Mingming Li, Hao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Content-generation agents continuously receive impressions, clicks, conversions, and negative feedback from recommendation systems, providing real-world outcome signals for memory evolution. However, these signals are delayed and noisy, confounded by audience composition, placement, and recommendation policies, and may result from the combined influence of multiple memories, making accurate attribution difficult. Existing methods rely primarily on immediate feedback or semantic retrieval and therefore struggle to reliably translate recommendation outcomes into memory fitness. To address this challenge, we propose TIDE (Trajectory-Informed Directed Memory Evolution), an external memory evolution framework driven by delayed recommendation feedback. We further introduce Memory Evolution Gain (MEG), which measures the utility improvement of evolved memory over a no memory baseline on strictly future tasks. TIDE treats memory as a capacity-constrained population of experiences: temporal and semantic credit assignment estimates contextual fitness, while responsibility credit distributes outcome signals according to the memories referenced during generation. These signals are then used to reinforce, crossover, mutate, or evict memories. On an e-commerce membership marketing content-generation agent, TIDE achieves a +7.75-percentage-point MEG in offline temporal replay and significantly improves both unique click-through rate (UCTR) and activation rate in an online A/B test. On a delayed-label benchmark, TIDE achieves the lowest mean absolute error (MAE) and root mean squared error (RMSE) and the highest MEG among the compared methods, demonstrating its effectiveness.

---


### 355. [Concealing LLM-Based Multi-Agent Topology via Phantom Structure Injection](https://arxiv.org/abs/2609.37567)

**<font color=#1a73e8>作者：</font>** Longzhu He, Zelang Wen, Xinfeng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Driven by the rapid advancement of large language models (LLMs), LLM-based multi-agent systems (MAS) have emerged as a powerful paradigm for collaborative reasoning over complex tasks. A key design element of MAS is the communication topology, which governs information flow among agents and often encodes proprietary knowledge about the system architecture. However, recent work has shown that such topologies can be inferred even in black-box settings by exploiting semantic dependencies in observable reasoning traces, posing significant risks of intellectual property leakage and exposure of system vulnerabilities. To address this threat, we propose MIRAGE, a topology-concealment framework that preserves the genuine communication topology for task execution while shaping adversary-facing semantic evidence toward a carefully constructed phantom topology. Specifically, MIRAGE operates in three stages: (1) phantom topology synthesis, (2) semantic edge realization, and (3) protected MAS execution. It constructs a phantom topology structurally distinct from the genuine one, materializes phantom edges as plausible semantic dependencies, and suppresses source-specific cues that could reveal genuine edges absent from the phantom topology. Extensive experiments across three topology optimization frameworks and four benchmark datasets demonstrate that MIRAGE substantially reduces the effectiveness of topology inference attacks while largely preserving the task utility of the protected MAS.

---


### 356. [Devils in Question Relay: Source-Conditioned Relay Steering to Mitigate Hallucinations in Audio-visual Large Language Models](https://arxiv.org/abs/2609.37568)

**<font color=#1a73e8>作者：</font>** Yu Zhang, Pingrui Zhang, Xuefeng Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio-visual large language models (AVLLMs) have made remarkable progress in multimodal understanding and reasoning through interactions among visual, auditory, and linguistic information. However, recent studies show that AVLLMs face a critical challenge: $\textbf{source-confused grounding hallucination}$, where cues from the unused modality induce responses that the required modality does not support, undermining reliability in real-world applications. Existing methods have made progress in mitigating this failure, yet how it arises from internal cross-modal interactions remains insufficiently understood. To address this gap, we conduct path-intervention and representation analyses, revealing a $\textbf{question-relay}$ mechanism: question states carry interfering cues alongside required-source evidence, undermining grounding in required-modality evidence. Cutting pathways from interfering modality to question states yields greater correct-answer logit recovery than cutting those to the generation position. Motivated by these findings, we propose $\textbf{SECRET}$ ($\textbf{S}$ourc$\textbf{E}$-$\textbf{C}$onditioned $\textbf{RE}$lay s$\textbf{T}$eering), a training-free method that mitigates cross-modal interference at the question relay. Using contrasting question representations elicited through different modality-pathway interventions, SECRET steers the original question states toward required-source evidence. Experiments on two widely adopted benchmarks CMM and AVHBench across three AVLLMs show that SECRET consistently outperforms prior training-free methods, substantially mitigating source-confused grounding hallucinations (e.g., up to +18.0 and +7.1 percentage points over base models). Modality-specific captioning further demonstrates its generalizability to open-ended generation.

---


### 357. [Decompose Radicals, Then Reward: Fine-Grained Inspection for Accurate Chinese Text Rendering](https://arxiv.org/abs/2609.37569)

**<font color=#1a73e8>作者：</font>** Yazhen Xie, Xingsong Ye, Zhineng Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rendering accurate Chinese text remains challenging for text-to-image models. Existing OCR-based reinforcement-learning rewards compare decoded transcripts with target strings. Such rewards overlook the compositional nature of Chinese writing: an ideograph consists of reusable components arranged through explicit spatial relations, yet OCR evaluates it as an atomic character. Consequently, visually different radical-level errors may receive equally coarse feedback, encouraging glyphs that merely resemble the target instead of faithfully reproducing its internal structure. We employ Ideographic Description Sequences (IDS), which comprise spatial operators and character components, and train an expert IDS recognizer to transcribe rendered Chinese text into this representation. Building on this recognizer, we introduce IDSpect, which deterministically decomposes the target text into IDS tokens and aligns crop-level visual IDS predictions with the target sequence. Globally unique token credit makes this comparison robust to the order of detected text regions. Combined with a whole-character semantic reward, IDSpect supplies fine-grained credit with component and spatial-relation without changing the image generator or adding inference-time cost. Experiments with GRPO post-training of Qwen-Image demonstrate that IDSpect achieves leading structural quality and semantic alignment on LongText and GenTextEval.

---


### 358. [Evaluating the Evaluators: Diagnosing Large Multimodal Models for AI-Generated Image Assessment](https://arxiv.org/abs/2609.37576)

**<font color=#1a73e8>作者：</font>** Yu Zhao, Jiarui Wang, Huiyu Duan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of text-to-image (T2I) generation, robust evaluation becomes critical yet challenging, as traditional metrics fail to capture fine-grained alignment and generative artifacts. While large multimodal models (LMMs) are increasingly adopted as evaluators, existing benchmarks typically study semantic understanding, quality perception, and authenticity identification in isolation, while largely neglecting responsibility detection. This leaves a gap in unified and comprehensive validation. To bridge this gap, we introduce SQUARE-Bench, a comprehensive benchmark that systematically evaluates LMM capabilities as evaluators of AI-generated images across four aspects: Semantics, Quality, Authenticity, and Responsibility. SQUARE-Bench introduces a granular taxonomy of 38 sub-dimensions to evaluate nearly 10K AI-generated images sampled from 22 diverse models, ranging from legacy to state-of-the-art generators, complemented by over 3K real-world images. The images are annotated with curated question-answering pairs. Extensive experiments on 23 LMMs reveal that top proprietary models, such as Gemini-3-Pro, already outperform the individual human expert baseline. However, the performance gap between models remains significant, exhibiting notable disparities in fine-grained inference and domain-specific robustness. Beyond benchmarking, we conduct a proof-of-concept study of LMM-guided iterative editing, in which dimension-specific LMMs provide diagnostic feedback to fixed image editors. The resulting guided system yields selective improvements in semantics, authenticity, and responsibility, while exhibiting a consistent visual-quality trade-off. SQUARE-Bench can serve as both a diagnostic tool for characterizing LMM evaluator capabilities and studying their use in T2I generation refinement. The benchmark and dataset will be released upon publication.

---


### 359. [Pair Difficulty Matters: Rethinking Pairwise LLM-as-a-Judge Evaluation and Consistency](https://arxiv.org/abs/2609.37577)

**<font color=#1a73e8>作者：</font>** Bruno Brocai, Maria Becker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model judges are widely used to rank texts and text-generating systems through pairwise comparison, and their reliability is typically assessed via three proxies: position bias, transitivity, and pairwise agreement (self- or human-labeled). Because these proxies drive judge selection and benchmarking, a substantial literature reporting that judges perform poorly on them risks steering practitioners away from otherwise capable evaluators. We argue this assessment is misleading. Under the Bradley--Terry geometry underlying pairwise aggregation, each proxy is dominated by close-rank-gap pairs, where inconsistency is information-theoretically expected and individual verdicts contribute little to the aggregate ranking; far-gap pairs carry the ranking signal but barely move the proxies. We formalize this argument and validate it in a controlled simulation and on two human-rated corpora: the proxies correlate only weakly with ranking accuracy against gold, and their predictive component concentrates in the far-gap regime. Judges should therefore be assessed on rank-gap-conditional metrics, ideally against human rankings. Code at this https URL.

---


### 360. [TReVS: Integrating Textual Relevance and Visual Saliency for Efficient Vision-Language Model Token Pruning](https://arxiv.org/abs/2609.37581)

**<font color=#1a73e8>作者：</font>** Jing Wang, Zhiping Wu, Dongdong Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) excel at visual understanding and reasoning but often incur substantial inference costs due to the large number of visual tokens. Recent visual token pruning methods increasingly follow a two-stage paradigm: they first remove visually redundant tokens after the vision encoder and then discard tokens irrelevant to the textual query within the Large Language Model (LLM). However, since the first stage typically relies solely on vision-encoder saliency, it may prematurely eliminate query-relevant tokens, depriving the subsequent text-guided stage of critical visual evidence. Our empirical analysis shows that incorporating query guidance into first-stage pruning better preserves task-relevant evidence and consistently improves performance over vision-only saliency-based pruning. We further find that high-variance attention heads are more sensitive to the textual query and yield more discriminative text-to-vision attention signals for second-stage pruning. Motivated by these findings, we propose TReVS, a training-free framework that combines textual relevance with vision-encoder saliency for pre-LLM pruning and leverages high-variance attention heads to remove task-irrelevant tokens at shallow-to-intermediate layers of the LLM. On LLaVA-1.5-7B, TReVS retains 92.8% of the unpruned baseline performance while pruning 94.4% of visual tokens, outperforming prior state-of-the-art methods.

---


### 361. [ReLMem: Learning Recurrent Memory for Longitudinal EHR Modeling](https://arxiv.org/abs/2609.37587)

**<font color=#1a73e8>作者：</font>** Zijie Meng, Xiwei Dai, Yingying Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longitudinal electronic health record (EHR) modeling requires integrating new visits with an expanding patient history. Yet the continual accumulation of clinical information imposes increasing computational and memory costs on large language models (LLMs) when they process and retain complete patient histories. A practical alternative is visit-wise recurrent compression, which incorporates each incoming visit into a compact, continually updated patient memory. However, under a fixed memory budget, successive updates must integrate new information without progressively losing critical historical evidence needed to subsequent tasks. To address this challenge, we introduce Recurrent Longitudinal Memory (ReLMem), a framework that learns to maintain fixed-capacity patient memory for efficient downstream prediction with a frozen LLM. ReLMem equips this LLM with lightweight compression adapters to recurrently update the memory from its previous state and each incoming visit, without rereading earlier records. Specifically, we develop a multi-granularity optimization strategy to preserve task-relevant information throughout recurrent updates and support downstream prediction from the final memory. The intermediate supervision aligns attention outputs from compressed memory and the full history under identical queries, while prediction supervision minimizes cross-entropy with ground truth answers conditioned on the final memory. On EHR-based medication prediction, ReLMem approaches the F1 scores of full-history baseline while reducing average retained historical storage by 97.1%. Under the same memory budget, it improves macro- and micro-F1 over the strongest compressed-memory baseline by 4.66 and 4.75 percentage points, respectively. These results highlight the value of learning recurrent patient memory for efficient longitudinal EHR modeling.

---


### 362. [FOCUS: Training-Free Decision-Preserving Context Compression for LLM Agents](https://arxiv.org/abs/2609.37590)

**<font color=#1a73e8>作者：</font>** Shantanu Dixit, Anson Bastos, Xuchao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents accumulate interaction histories that grow linearly with task length, causing quadratic inference cost scaling and performance degradation from attention dilution. Existing context-compression methods learn what to discard offline: by contrastively optimizing guidelines, distilling compressors, or training compression policies. This incurs a substantial cost. Further, the compression policy is learned a priori and is not dynamically conditioned on the evolving test-time trajectories. In this paper we ask a complementary question: Which past interactions causally shape the agent's future decisions? We recast context compression as a causal decision preservation problem over discrete interaction units and introduce FOCUS, a training-free context compression framework that operates entirely at test time. Our method requires no offline data collection or fine-tuning, and is architecture-agnostic, attaching to any closed-API frontier model as a modular compression layer. We evaluate FOCUS on diverse agentic benchmarks including API and tool-calling, QA, web domain and multi-turn dialogue. Our method establishes new state of the art performance, cutting peak context by up to 48% and dependency by 73% while improving task success by up to 8.9 percentage points over uncompressed execution.

---


### 363. [XU-RS: Explaining Credal Width in Random-Set Language Models](https://arxiv.org/abs/2609.37594)

**<font color=#1a73e8>作者：</font>** David Achara, Maryam Sultana, Alexander D. Rast 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Uncertainty estimates tell us how unsure a model is, but not why. Without knowing which parts of an input influences a model's uncertainty, we cannot tell whether that uncertainty score depends on input features that are relevant for the task. We study this problem in randomset classifiers built using pretrained language models. These classifiers assign probability to individual answers and to groups of answers, producing lower and upper probabilities for each answer; The difference between these probabilities, called credal width, is used to represent epistemic uncertainty about an answer arising from limited training data. We propose XU-RS, a framework that attributes an answer's credal width to the input tokens (words or word pieces) supplied to a language model. XU-RS uses Expected Gradients (a standard feature attribution method) to estimate how input tokens contribute to credal width. The proposed framework is evaluated on a MedQA dataset using SmolLM3-3B and Llama-2-7B models, demonstrating that setting the embedding of a token ranked highly by XU-RS to zero (zero-masking) causes larger changes in credal width than zero-masking randomly selected tokens. In addition, we show that normalisation can cause other answer groups to influence an answer's width, reveal how token attribution can mask numerical errors, and provide diagnostic checks to verify whether a token ranked highly by XU-RS meaningfully explains model uncertainty.

---


### 364. [Authority Bias in Language Models: Source Deference and User Agreement Are Not Interchangeable](https://arxiv.org/abs/2609.37616)

**<font color=#1a73e8>作者：</font>** Abhinav Rajeev Kumar, Paras Chopra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models tend to agree with whatever a user asserts, and post-training increasingly targets this sycophancy so that models evaluate claims on their merits rather than deferring to the user. Yet the same models are far more compliant when a wrong answer is attributed to a verified source, which is how retrieval results, tool outputs, and grounded-search content often present information. We measure this gap across five open-weight families and three closed APIs. A single verified-source note endorsing a wrong answer flips 45-88% of baseline-correct responses in seven of eight models, and compliance rises with how authoritative the note sounds. Source deference and user agreement are not behaviorally interchangeable inside the model: on matched items with the same wrong answer, causal interventions can selectively suppress one without equally affecting the other. In three open-weight families, removing a fitted source direction lowers source compliance by 65-80 percentage points while removing a user or assistant direction has far smaller effects, and removing the user direction shows the reverse preference. A separately fitted intervention derived from source-versus-user cue activations moves compliance in both directions while leaving the prompt text unchanged. An authority direction fitted on trivia also transfers to PIQA and multi-turn SYCON dialogues without refitting, and removing it lowers wrong-source compliance by tens of percentage points in four of five families with no detected change in MMLU-Pro or GSM8K accuracy at our evaluation sizes. Source deference and user agreement therefore need separate evaluation.

---


### 365. [Correct, Don't Delete: Mitigating Emergent Misalignment with Corrective Supervision](https://arxiv.org/abs/2609.37624)

**<font color=#1a73e8>作者：</font>** Jacob Epifano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a language model on a narrow set of harmful demonstrations, such as bad medical advice, can make it broadly misaligned on unrelated questions, a phenomenon known as emergent misalignment (EM). The usual defense is to find the offending rows and delete them, but a row locator failed our held-out test and deleting rows helps less than expected. We ask a different question: given a fixed set of poisoned rows, is it better to correct them than to remove them? We fine-tune Qwen2.5-14B-Instruct on a mixture of bad medical advice and benign chat data, select a quarter of the poison rows in advance, and either delete them or replace each with a corrected answer to the same prompt, keeping everything else the same. Replacing the rows cuts the EM rate by about a third and improves answers on held-out medical questions, while deleting the same rows has little measurable effect. The advantage is larger when half the poison rows are corrected, and it holds on a second base model and a second misaligned model organism. The content of the replacement appears to matter: paraphrasing the rows while keeping their bad advice shows no clear benefit, and the correct answers distributed with the dataset appear to do about as well as our rewriter's. Realigning an already-poisoned model with further fine-tuning is known to work, but which data does the work has not been compared directly. We find that a short round of training on corrections beats the same amount of training on generic chat data, that corrections on other medical prompts do roughly as well as corrections of the poisoned prompts themselves, and that instructing the correction writer to model a careful, harm-avoiding assistant adds no measurable benefit over plain corrections. In the settings we tested, correcting harmful training data reduces EM more than deleting it.

---


### 366. [RLTL;DR: Self-improvement by Internalizing Self-generated Feedback](https://arxiv.org/abs/2609.37633)

**<font color=#1a73e8>作者：</font>** Michael Kirchhof, Eleonora Gualdoni, Andrew Szot 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The common paradigm of reinforcement learning with verifiable rewards (RLVR) is to let agents make multiple attempts at a task, and optimize towards the successful ones. This becomes problematic in the realms of self-improvement, where tasks are so difficult that the agent has a low or even no chance of success, and where there are no teacher models or example solutions to distill from. In this paper, we introduce RLTL;DR. After each failed attempt, we show the policy the verifier outputs and let it write its own feedback, in the form of a single TL;DR insight. The next rollout is conditioned on all previous insights, and we sequentially sample rollouts until a solution is found. Moreover, we enable backpropagation on the in-context insights to internalize a direct task to insight mapping. On challenging tool-calling and coding datasets (filtered to Pass@128=0), standard GRPO training of a Qwen 3.5 9B Thinking policy stays flat at a Pass@1 of 0% to 1%. RLTL;DR breaks through this learning barrier, achieving a Pass@1 of 14-31% with insights in context during training and, crucially, 12-13% when no insight is in context at eval time. We identify that the key is the task to insight internalization. To study this further, we reduce our approach to SFTL;DR, training only on (task, insight) tuples, without showing or backpropagating on any rollouts. Training on only 4k of these tuples recovers almost the full performance of RLTL;DR and classical SFT on full rollouts. This demonstrates a promising compacted training paradigm of the form "on this sort of task, keep this sort of thing in mind", which we hope to inspire future research on.

---


### 367. [Co-Linguistics: AI-augmented Theory Construction in Linguistics](https://arxiv.org/abs/2609.37635)

**<font color=#1a73e8>作者：</font>** Emmanuel Chemla, Benjamin Spector, Alexandros Kalomoiros 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs have been studied in recent linguistics as potential models of humans' linguistic abilities. Here we discuss an entirely different use of AI, namely as a co-scientist, to help construct and assess linguistic theories (we refer to the result as "Co-Linguistics"). Since the 1960s, linguistics has developed theories that are in principle mathematically formalizable, often in the language of formal language theory or model theory. The AI revolution in mathematics will thus have consequences in linguistics-but with an essential twist: proving new theorems is rarely the linguist's goal. Rather, one seeks to find the best set of axioms to derive empirical statements. AI could accelerate research by making existing theories fully explicit, by comparing competing theories, and more ambitiously, by proposing new theories (in machine learning, this relates to "program induction"). It will also help assess theories by accelerating the identification and test of crucial predictions, thanks to unparalleled access to data (in machine learning, this relates to "active learning"). While the cycle from theory evaluation to theory construction may give rise to recursive and possibly autonomous improvement of linguistic theories, humans remain central: linguists provide scientific directions and evaluate theories conceptually, and experimental participants are needed to assess empirical predictions that are outside the reach of LLMs.

---


### 368. [Targeted Visual Counterfactual Explanations for Contrastive Vision-Language Model](https://arxiv.org/abs/2609.37638)

**<font color=#1a73e8>作者：</font>** Van Bach Nguyen, Jörg Schlötterer, Christin Seifer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current explanation methods for contrastive vision--language models such as CLIP mainly identify important regions without showing how to change the input in order to get a target prediction. We introduce \textbf{M}ask-guided \textbf{A}daptive \textbf{C}ounterfactual \textbf{E}xplanations (\mace), a targeted visual counterfactual method designed specifically for CLIP zero-shot classification. \mace constructs an editable region from either source attribution or source--target attribution differences and expands the mask only when needed to reach a specified target class. A latent diffusion inpainting model then modifies the selected region, while a frozen CLIP model provides modification guidance and anchors the remaining image content to the original input. We evaluate \mace on ImageNet, Food-101, Oxford Pets, and CUB-200. The source-mask variant achieves the highest target top-1 success rate across all four datasets, while the difference-mask variant produces the smallest pixel-level and perceptual changes and the best realism scores. Both variants improve proximity and realism over a Stable Diffusion-only baseline using the same generative backbone. These results show that adaptive mask-guided editing produces effective CLIP counterfactuals. They further reveal a tradeoff between counterfactual validity and source-image preservation.

---


### 369. [Evaluating and Benchmarking the System One Model Jev](https://arxiv.org/abs/2609.37647)

**<font color=#1a73e8>作者：</font>** Tobias Deußer, Lorenz Sparrenberg, Rafet Sifa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Jev is a commercial System One model from TypeSafe AI that does not generate text: given a state and typed questions, it returns a choice from fixed options, a position on a rubric, or the probability that a statement is true, with probabilities the vendor describes as calibrated. Such models target small decisions in information access pipelines, such as routing queries, checking grounding, moderating content, or rating against a rubric. We evaluate Jev (jev-1.13.0) zero-shot on 37 datasets spanning classification, routing, natural language inference, reading comprehension, commonsense reasoning, moderation, legal clause analysis and rubric scoring, with one frozen template per dataset and full evaluation splits: 346,009 requests for under USD 10. For reference, we score Qwen3.8-27B and Gemma-4-E4B on identical requests via their exact next-token probabilities over the options. Jev reaches 95-99% accuracy on IMDB, SST-2, HellaSwag and ARC and 86.7% on Belebele across 122 languages. It beats Qwen on 27 of 37 datasets, with none of Qwen's nine leads outside the bootstrap intervals, and Gemma on all 37. All three models degrade on low-resource languages, fine-grained or noisy labels, and rubric-based quality judgments. Jev's choice probabilities are well calibrated and support selective prediction. Binary probabilities rank well but are poorly placed relative to a fixed 0.5 threshold; thresholds tuned on training data raise micro-F1 on UNFAIR-ToS from 0.50 to 0.75. Jev answers MMLU's calculation-heavy questions more accurately than other MMLU questions (94% vs. 91%), whereas both open models, and all three on C-Eval, find them harder. Rotating the options leaves Jev's accuracy unchanged and withholding the question drops it to near chance, ruling out shallow memorization but not memorized question-answer pairs. We release the code, harness and all raw responses.

---


### 370. [VoxelSage: Tool-Augmented 3D CT Analysis and Simulator-Shielded Sequential Resection Planning for Liver Tumors](https://arxiv.org/abs/2609.37648)

**<font color=#1a73e8>作者：</font>** Binghong Qian, Xuanhe Liu, Yifan Xing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preoperative liver-tumor assessment requires segmentation, physical-space measurement, visual evidence, and resection planning from the same three-dimensional CT volume. Existing tools often handle these steps separately, while language models cannot reliably compute physical measurements from CT. To provide an integrated workflow, we present VoxelSage, a multi-modal system for two- and three-dimensional visualization, liver-tumor analysis, and preoperative resection planning. Its dual-port architecture separates language-model orchestration from image computation: Port A interprets requests and selects skills, while Port B applies them to CT volumes and segmentation masks and returns structured results. Keeping physical measurements in Port B prevents the LLM from computing them directly and reduces the risk of fabricated numerical results. Eight built-in skills support quantitative analysis, visual evidence generation, three-dimensional reconstruction, segmentation refinement, and sequential resection planning; user-defined skills can extend these functions. For sequence planning, a behavior-cloned neural ranker orders candidate resection targets, while a simulator-based shield checks them against predefined constraints. Across 256 unseen simulator scenes, this approach reduced mean simulated time from 34.274 to 33.388 min (0.886 min, 2.59%) and mean simulated blood loss from 300.847 to 183.852 mL (116.995 mL, 38.89%) relative to a deterministic baseline. These results demonstrate system integration and simulator-level performance, not clinical efficacy or safety. The public implementation is available at this https URL.

---


### 371. [Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding](https://arxiv.org/abs/2609.37655)

**<font color=#1a73e8>作者：</font>** Jiayu Ying, Qijian Tian, Ruijie Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advancing spatial intelligence in Multimodal Large Language Models (MLLMs) is bottlenecked by the scarcity of complex, scalable 3D question-answer (QA) data. While manual annotation is labor-intensive, directly utilizing LLMs to synthesize these QA pairs often fails due to their inherent deficiencies in spatial and geometric computation. We introduce Exemplar2VQA, a scalable exemplar-driven visual question answering generation framework that rapidly synthesizes large-scale spatial QA pairs in simulated environments via multi-agent coding. By equipping collaborative agents with a meticulously designed library of geometric utilities, Exemplar2VQA bypasses LLMs' spatial reasoning flaws through deterministic code execution. Crucially, the framework exhibits remarkable versatility: taking diverse static object-centric spatial query templates as exemplars, it seamlessly and autonomously scales them into massive, high-fidelity synthetic datasets. Fine-tuning Qwen2.5-VL (3B/7B) exclusively on Exemplar2VQA-generated synthetic indoor data yields significant performance improvements across various diverse benchmarks. Furthermore, its effectiveness is not limited to in-domain indoor datasets but also robustly extends to outdoor and mixed-scene benchmarks. These results establish Exemplar2VQA as a scalable and powerful paradigm for bridging the sim-to-real gap in Embodied AI. Our code is at this https URL

---


### 372. [Tracing the Evidence: Faithful Token Attribution Through Vision-Language Reasoning](https://arxiv.org/abs/2609.37656)

**<font color=#1a73e8>作者：</font>** Bowen Yuan, Danny Wang, Ruihong Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) exhibit strong reasoning capabilities, yet the visual and textual evidence supporting the generated responses remains difficult to identify. Faithful token attribution explains an LVLM's response by assigning scores that rank image and prompt tokens by how much the model relies on them, such that removing higher-ranked tokens causes the likelihood of the generated response to drop more rapidly. However, existing token-attribution methods have been developed mainly for text-based language models, and our empirical study reveals two challenges when complex multimodal sources are involved. First, the joint image-text attribution can underrepresent visual evidence relative to text, obscuring the image regions supporting the response. Second, visual evidence may influence the generated response through multiple intermediate reasoning paths, while existing methods trace only a limited subset of these paths, causing important visual contributions to be underestimated. Motivated by these insights, we introduce VTrace, a multimodal token-attribution framework that traces input contributions through intermediate reasoning and calibrates attribution scores across modalities. VTrace constructs pairwise attributions that highlight token-specific contributions and aggregates all forward attribution paths in closed form to account for both direct and indirect contributions. Cross-modal calibration then rescales image and text attribution scores using modality contributions estimated from response-likelihood changes, enabling a unified ranking of input tokens. Evaluations against seven baselines across six visual reasoning benchmarks demonstrate the superior attribution faithfulness. Project page: this https URL.

---


### 373. [EnterpriseBench: Benchmarking LLM Agents on Enterprise-Level Strategic Reasoning and Decision-Making](https://arxiv.org/abs/2609.37658)

**<font color=#1a73e8>作者：</font>** Min Yang, Yichen Pan, Jinghua Piao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly expected to support enterprise workflows, where tasks often involve missing information, uncertainty, feedback, and long-term trade-offs. However, existing enterprise and financial benchmarks mainly test static capabilities such as information extraction, numerical calculation, domain knowledge, and financial QA, leaving interactive and long-horizon decision-making underexplored. To bridge this gap, we introduce EnterpriseBench, a benchmark that evaluates LLM agents across this spectrum, from static question answering to dynamic decision-making. Specifically, EnterpriseBench reorganizes existing enterprise and financial QA datasets into a unified foundational suite annotated by capability and difficulty, and introduces three professional interactive settings: Consulting, based on management-consulting-style business cases for client problem diagnosis through multi-turn information seeking; the Beer Game, adapted from a classic supply-chain management simulation for inventory control under delayed feedback; and Enterprise Digital Twin, a project-based business simulator for workforce, risk, and project planning. Experiments with nine agent methods under four backbone models show that current agents have not yet achieved stable, comprehensive, and cross-task reliability in enterprise scenarios. These results show that EnterpriseBench provides a practical benchmark for evaluating LLM agents in realistic enterprise strategic reasoning and decision-making.

---


### 374. [Are In-Context Images Worth 10 Dimensions?](https://arxiv.org/abs/2609.37659)

**<font color=#1a73e8>作者：</font>** Adhemar de Senneville, Xavier Bou, Jérémy Anger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> There has been significant work on understanding the In-Context Learning capabilities of Large Language Models, especially on the induction circuit. For a few-shot classification task, the induction circuit leverages linear representations of each labeled example in-context in order to classify an unlabeled query. However, few works focus on how those linear representations are built in the first place. Leveraging the expressivity of the vision modality compared to text, we uncover a Shared Discriminative Geometry (SDG) inside Large Vision Language Models (LVLMs). It is a low-dimensional space, shared across all image classification tasks, in which in-context images are compressed into linearly separable representations later used to perform classification. We observe that this is the result of the model performing a dimensionality reduction of vision representations in early layers. In order to explain this phenomenon: (1) We show analytically that linear self-attention can perform a dimensionality reduction by projecting in-context data onto its principal components, with each layer implementing one gradient descent step toward this objective. (2) We provide evidence that trained LVLMs reduce the dimensionality of vision representations in early layers via a similar mechanism.

---


### 375. [Corpus-Guided Dual-Path Propagation for Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2609.37661)

**<font color=#1a73e8>作者：</font>** Baoxian Liu, Tong Wei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph-based retrieval-augmented generation supports multi-hop retrieval by organizing corpus information into graphs. However, existing relation-free graph retrieval methods rely primarily on query-sentence similarity to search for evidence. This can exclude useful bridging evidence with low query similarity and activate incidental entities unrelated to the reasoning chain. In this paper, we propose a simple and effective approach called NexusRAG, which augments the relation-free Tri-Graph with a corpus-level entity neighborhood structure derived from joint entity co-occurrence and semantic similarity. NexusRAG employs this structure to guide two complementary propagation paths: neighborhood-constrained semantic propagation through sentences identifies the query-relevant entity frontier, while direct structural propagation between neighboring entities expands that frontier to structurally related entities. The propagated entity weights also inform neighborhood-aware passage initialization for Personalized PageRank. Experiments on three multi-hop QA benchmarks and a domain-specific subset of GraphRAG-Bench show that NexusRAG consistently outperforms existing approaches. On the GraphRAG-Bench subset, NexusRAG achieves the highest evidence recall in all question categories, exceeding baselines by 4.2-8.1 points. The implementation code is available at this https URL.

---


### 376. [KUPAS MASTER: Distilling the Tacit Expertise of Master Practitioners into Agent-Ready Experience Corpora](https://arxiv.org/abs/2609.37673)

**<font color=#1a73e8>作者：</font>** Changmian Wang, Yuchao Ma, Xuchao Lu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Experienced professionals know more than just facts and conclusions. They know which cues matter, why a judgment is reasonable, and which action to take. Routine work records often leave out this tacit knowledge, making it difficult for Large Language Model (LLM) agents to use professional experience effectively. We introduce KUPAS MASTER, an experience engineering platform built around nine-layer cognitive corpus construction. It turns heterogeneous work records and practitioner interviews into traceable, reusable experience corpora for agents. Six case elements preserve the task process: context, cues, judgment, action, boundaries, and outcomes. Nine-layer cognitive corpus construction organizes tacit experience along nine extraction dimensions and stores the resulting assets in six libraries: rules, constraints, best practices, negative examples, corner cases, and skills. Semantic alignment, individual experience distillation, organizational consolidation, and cross-review preserve source evidence, conditions of use, and unresolved disagreements. The platform packages these assets into callable skills with explicit inputs, steps, dependencies, and stopping conditions, connecting experience collection to task execution and evaluation feedback. Using authorized samples from 20 randomly selected practitioners, the platform processed 1,576 source files into 23,024 individual experience records and 13,113 organizational assets. The evaluation spans multiple professional domains. Under common task inputs and scoring criteria, the base model, raw corpus retrieval-augmented generation (RAG), and KUPAS MASTER agent scored 70.63, 79.75, and 89.58, respectively. The KUPAS MASTER agent improved on raw-corpus RAG in all seven scoring dimensions. The platform provides a practical path from individual tacit experience to organizational knowledge and agent capabilities.

---


### 377. [LEMON-ZEST: Evolution-Informed Tokenization for Efficient Protein Language Modeling](https://arxiv.org/abs/2609.37675)

**<font color=#1a73e8>作者：</font>** Biswajit Banerjee, Claudia Alvarez Carreno, Anton S. Petrov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein Language Models (PLMs) have made remarkable progress following scaling laws established in natural language processing across sequence- and structure-based tasks, yet the potential of tokenization remains underexploited. Unlike human language, proteins preserve structure despite extensive sequence variation a property standard tokenization strategies fundamentally fail to capture. We introduce ZEST (Zoned Encoding of Sequence Traits), an evolution-informed vocabulary derived from conserved regions of multiple sequence alignments. ZEST allows embedding domain-level biological priors directly at the tokenization stage rather than learning them implicitly through scale. ZEST natively compresses sequences to an average token length of 4 residues, enabling our model to process 4,000 residues within a standard 1024-token context window. Building on this, we present LEMON (Layered Extraction of Molecular Ordering from Nature), a compact 200M-parameter sequence-based model for detection of remote homology between protein sequences trained on a single H100 GPU for one week. Despite its modest size, LEMON outperforms state-of-the-art models ranging from 600M to 3B parameters. Our results demonstrate that evolution-informed tokenization can substitute for massive parameter scaling, opening a new direction for efficient, biologically-grounded protein representation learning. All code, model weights, and results are publicly available under the MIT license.

---


### 378. [When Models Don't Manipulate Manifolds: The Geometry of a Comparison Task](https://arxiv.org/abs/2609.37680)

**<font color=#1a73e8>作者：</font>** Sai Sumedh R. Hindupur, Hadas Orgad, Thomas Fel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One of the current premises of mechanistic interpretability research is that detailed accounts of the geometry of neural network representations can tell us how models perform computations, and how to effectively intervene on them. While low dimensional manifolds have been observed for multiple concepts in the literature (e.g. numbers encoded on helices, days of the week on a circle, ...), with structure believed to reflect properties of data and tasks, the extent to which models rely on them for computation, and how they manipulate them, remains unclear. We characterize precisely the geometry of computation in a number-comparison task, as an abstraction of comparison for decision making, and how models utilize geometry in an elegant fashion to implement it. Specifically, we study the causal geometry of number comparison in Qwen2.5-7B-Instruct, a capable and widely studied open-weight model, and find Qwen largely uses linear representations of numbers despite the presence of curved geometry. To compare two numbers, the model first encodes each number along a vector and adds the two representations using attention and the residual connection, bringing them into a shared space in the residual stream. Then, the model uses MLP neurons to compare the pair of numbers on local regions in this shared space, which correspond to smaller intervals of input numbers, and combines these to obtain the position of the maximum. In fact, this reliance on linear representations for comparison also persists when the model compares three numbers. Our findings demonstrate that the manifold hypothesis can co-exist with linear representations: while concepts that are ordered may have manifold structure in representations, the model may use an underlying linear structure of the concept in certain computations.

---


### 379. [PAIQ: Patch-Aligned Semantic Injection via Residual Rotation](https://arxiv.org/abs/2609.37685)

**<font color=#1a73e8>作者：</font>** Pinze Ren, Yuwei Zhang, Hao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-aligned and self-supervised visual encoders offer complementary strengths in semantic abstraction and spatial detail. Harnessing this complementarity requires enriching local features while retaining distinctions between semantically related patches. We introduce PAIQ, a patch-aligned semantic injection framework that combines content-based cross-encoder matching with orthogonally constrained residual updates. Using DINOv3 patch features as the spatial base, PAIQ aggregates complementary SigLIP features through joint source allocation and injects the aggregate--base differences through a shared orthogonal transformation Q. This rotation adapts update directions while preserving residual norms and pairwise angles. For fixed projected features, we derive conditions for patch separability under similar semantic aggregates and show that rotation adds a nonnegative separation term over direct interpolation when the aggregate is shared. Only the projection and fusion parameters are trained; both visual encoders and the language model remain frozen, and fusion retains 196 visual tokens. Across diverse language backbones, PAIQ yields broad gains in judge-assessed correctness and reductions in hallucination severity over single-encoder interfaces on image description and visual question answering. On the 2B and 9B Qwen backbones, this compact interface outperforms the strongest evaluated fusion or token-compression baselines by about 2.9 correctness points on average.

---


### 380. [Reader Proficiency Shapes Layer-wise Surprisal Profiles](https://arxiv.org/abs/2609.37688)

**<font color=#1a73e8>作者：</font>** Akio Hayakawa, Horacio Saggion  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reading behaviour varies not only with linguistic input, but also with reader proficiency. In this study, we investigate whether the layer-wise relationship between surprisal from large language models (LLMs) and human gaze behaviour differs across readers with different levels of proficiency and across gaze measures. Using eye-tracking data from the MECO L2 corpus, we compare readers with high and low vocabulary proficiency on first-pass gaze duration (FPGD) and total gaze duration (TGD). We quantify the distribution of the predictive power of surprisal across model layers using Predictive Depth. Across 12 tested LLMs, we find that readers with lower vocabulary proficiency tend to show deeper Predictive Depth for FPGD, while this difference is smaller for TGD. Also, TGD itself shows deeper Predictive Depth than FPGD in both proficiency groups. These patterns suggest that where predictive power is concentrated across LLM layers may be related to the timing and breadth of the reading processes captured by different gaze measures, and that this relationship can vary with reader proficiency. Our leave-one-out analysis further shows that the advantage of informative internal layers extends to unseen texts, although the practical improvements in prediction are limited. Overall, our results show that layer-wise LLM surprisal provides a useful perspective on variation in reading behaviour across both reader groups and gaze measures.

---


### 381. [Locating Answer-Correctness Signals in Frozen Large Language Models](https://arxiv.org/abs/2609.37700)

**<font color=#1a73e8>作者：</font>** Yuansen Liu, Yixuan Tang, Anthony Kum Hoe Tung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models expose internal signals that predict whether an answer is correct, readable from a single forward pass of a frozen model without additional generations. Yet existing probes often commit to one signal family or layer and can be brittle under distribution shift; in retrieval-augmented settings, many specialized detectors instead target passage faithfulness, which can diverge from correctness when retrieved evidence is unhelpful or conflicting. We therefore ask where answer correctness is readable, which internal signal families carry it, and how they should be combined. We search over hidden states, token probabilities, residual-stream features, attention, and their fusion, treating the selected readouts as a predictive measurement rather than a mechanistic localization. We run this analysis separately in closed-book and with-context settings, since context can change which readouts are informative. A consistent anatomy emerges: correctness concentrates in the answer span, recovered from the answer tokens even under retrieval, and the families carry it complementarily, so fusing them helps most out of distribution, where a single signal is weakest. The protocol is effective across two backbones and gates a retrieval controller as one downstream use.

---


### 382. [Billiger.de Products: A Bilingual Entity Matching Benchmark](https://arxiv.org/abs/2609.37713)

**<font color=#1a73e8>作者：</font>** Aaron Steiner, Ksenia Elagin, Ralph Peeters 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing product matching benchmarks primarily contain English-language product data and are often dominated by a single product category, such as electronics. This paper introduces this http URL Products, a bilingual German and English entity matching benchmark covering thirteen consumer product categories, including difficult-to-handle categories such as clothing and furniture. The benchmark data originates from the German price comparison platform this http URL. Following the design of WDC Products, the benchmark offers multiple variants that differ in the fraction of corner cases, the size of the development set, and the fraction of entities unseen during training. An aligned English translation of every offer keeps all pairs, splits, and labels fixed, while cross-language test sets combine German and English records within individual pairs. We validate the benchmark using six supervised matchers and zero-shot GPT-5.2 on both language versions and the cross-language test sets. The validation shows the difficulty of the benchmark. The comparison of the results on the English version of the benchmark to the results on the German version shows that most matchers score on average higher on the English version. The difference is largest for RoBERTa and HierGAT, while the zero-shot LLM runs are largely insensitive to the language. Comparing the F1 scores achieved by PLM-based matchers on the English version of this http URL Products with their performance on existing English-language benchmarks, such as WDC Products and Abt-Buy, shows that this http URL Products is more difficult than these benchmarks.

---


### 383. [Volatility-Clustering Adaptation for Financial Time Series](https://arxiv.org/abs/2609.37715)

**<font color=#1a73e8>作者：</font>** Manh Nguyen, Minh Hoang Nguyen, Huu Hiep Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models are increasingly adapted to new domains through fine-tuning on target data, under the implicit assumption that more target data yields better forecasts. We show that this assumption can fail in financial forecasting, where individual price changes are difficult to predict, but large moves tend to cluster, creating alternating calm and turbulent periods. Using financial foundation models trained on price bars of open, high, low, close, and volume, we argue that adapting to financial domains requires training signals beyond next-token prediction. We introduce Volatility-Clustering Adaptation (VCA), which augments next-token cross-entropy with a differentiable penalty on the autocorrelation of squared returns, the standard statistical signature of volatility clustering. This additional objective provides a multi-step training signal by matching the resulting dependence structure of autoregressive rollouts to those of the realized future. Across three asset sets and two evaluation conventions, VCA improves adaptation over the pre-trained model, with the strongest gains under the primary evaluation (\textsc{fore}), driven primarily by reduced variance error. Overall, our results suggest that effective financial adaptation requires objectives that capture domain-specific temporal structure beyond token-level prediction.

---


### 384. [Predictive Geometry of Hidden Trajectories in Transformers](https://arxiv.org/abs/2609.37717)

**<font color=#1a73e8>作者：</font>** Timur Mudarisov, Mikhail Burtsev, Tatiana Petrova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoder-only transformers are trained only through a terminal next-token prediction loss, yet this loss constrains every intermediate hidden state through the fixed downstream computation. We formalize this constraint by studying layerwise loss-to-go functions: the terminal loss obtained by continuing a candidate hidden state through the remaining transformer blocks. Around successful validation trajectories, we show that the local second-order geometry of these functions is governed, up to low-loss residual terms, by a pullback Fisher operator on hidden-state space. Its spectrum identifies output-sensitive directions and approximately prediction-null directions, yielding a local observable subspace of the residual stream. For causal transformers, the same geometry induces a tokenwise curvature score: a Fisher-weighted sensitivity of the target logits to perturbations of each token's hidden state. This score vanishes outside the causal ancestor set of the target and is controlled by downstream Jacobian couplings, making it a loss-aware alternative to attention magnitude. We estimate these quantities using matrix-free Jacobian-vector and vector-Jacobian products and evaluate them across decoder-only language models on WikiText, OpenWebText, and FineWeb. Empirically, the induced geometry predicts perturbation sensitivity, supports nonuniform layerwise rank allocation, yields competitive structured token-pruning signals, and improves low-rank student recovery when added to stronger autoregressive distillation objectives such as reverse KL and skew KL. These results support a predictive-geometric view of transformer computation: near successful trajectories, the terminal loss induces a thin, anisotropic set of output-relevant hidden-state directions that can be measured and exploited for compression and distillation.

---


### 385. [Context Language Models](https://arxiv.org/abs/2609.37725)

**<font color=#1a73e8>作者：</font>** Rulin Shao, Shannon Zejiang Shen, Junjie Oscar Yin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Context Language Models (CLMs), language models that natively manage their own context. We implement this by treating the context as a file and allowing the model to make unrestricted updates to this file. This allows the model to learn what is most important to maintain in context, and naturally extends to multi-agent systems where multiple agent contexts coexist as files. Building CLMs zero-shot with existing models outperforms SOTA context management strategies across a variety of tasks: 11.4% higher accuracy with 21.5% fewer FLOPs on BrowseComp-Plus, 5% higher scores with 59% fewer FLOPs on 12-hour EdgeBench, and 65% greater improvement with the same compute on a 24-hour multi-repository agent-swarm task. Moreover, by shifting context management from external harness control to intrinsic model behavior, CLMs naturally enable both in-context and parametric learning of context-management strategies. We show that CLMs can be steered with natural-language instructions evolved through a standard skill-optimization loop, improving held-out accuracy by up to 35.9 points on a context-management task while reducing compute. We also introduce an online reinforcement learning method for CLMs, improving Qwen3.5-9B performance on BrowseComp-Plus by 47.6% while using 12% fewer FLOPs. Finally, we co-design Suffix Cache Reuse for CLM serving, further reducing server-side compute by 35% relative to standard SGLang at matched performance.

---


### 386. [Weights Read and Write Features: Scalable Parameter Decomposition Grounded in Activation Space](https://arxiv.org/abs/2609.37731)

**<font color=#1a73e8>作者：</font>** Tue M. Cao, Lisiane Pruinelli, My T. Thai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation space and parameter space provide complementary views of model computation. Activations represent information, while weights read, transform, and write that information. Yet existing interpretability methods largely study the two spaces separately, leaving the connection between represented information and parameter-level computation underexplored. We introduce Activation-Supported Parameter Decomposition (ASPD), which jointly decomposes activation and parameter spaces and grounds each learned weight component in the activation features it reads or writes. This grounding constrains otherwise non-unique parameter decompositions using the model's internal activations, while an internal reconstruction objective provides a local learning signal at the weight matrix being analyzed. Together, these properties enable scalable, interpretable, and causally editable parameter decomposition in pretrained large language models, demonstrated on Qwen-3-8B. The learned read--write components can also be composed into parameter-level mechanism circuits. We use ASPD to recover mechanisms underlying the classic IOI circuit and trace semantic transformations through model weights.

---


### 387. [The Camera Inside the Editor: Reading the Implicit Camera of Image Editors with Painted Calibration Patterns](https://arxiv.org/abs/2609.37732)

**<font color=#1a73e8>作者：</font>** Sebastian Rückerl  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based image editors insert objects, restyle scenes and render new viewpoints, but it is unknown which camera they assume when they paint into a photograph. Asked to cover the floor with a checkerboard, an editor paints projective structure from which classical vanishing-point geometry reads pitch, roll, focal length, yaw and, on renders, the principal point, without any training. Unlike a calibrator such as GeoCalib, which estimates the camera of an image, this isolates the camera under which the editor paints. On 120 rendered cameras with exact ground truth, Qwen-Image-Edit-2511 paints tile edges that meet their vanishing points within 0.26 degrees, and its implicit camera matches the true one to 0.8 degrees in pitch and 6% in focal length, more accurately than GeoCalib except in roll. Asked to draw the horizon or mark a vanishing point instead, the editor fails, so this knowledge is revealed by painting and not by the explicit tasks we tried. The implicit camera has two priors: roll is pulled towards level (slope 0.71), and telephoto perspective towards a default of about 30 mm, which roughly matches the camera the models paint without any scene. For Qwen, the priors do not grow when blur removes four fifths of the line evidence. They are stronger on real photographs, and on NYUv2 a shorter wording of the task removes the difference for roll. On photographs from a 24--240 mm zoom lens the painted perspective grows with only 0.62 of the lens's slope, while GeoCalib and MoGe-2 saturate at about 52 and 42 mm. FLUX.1 Kontext and LongCat-Image-Edit are pulled much harder. Finally, from a level camera a camera-control LoRA executes pose commands at only 50--70% of their strength, and a board painted into its output agrees with the camera it produced.

---


### 388. [ContextRender: From Execution Dependencies to Agent Context](https://arxiv.org/abs/2609.37743)

**<font color=#1a73e8>作者：</font>** Savini Kashmira, Jayanaka L. Dantanarayana, Lingjia Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents performing long-horizon tasks accumulate tool results that later steps may need. Passing the full history to every invocation is costly even when it fits within the context window, while reducing it risks omitting needed information. Existing context management methods can overlook how earlier tool results are used in subsequent execution, leaving needed information out of context. We introduce ContextRender, which manages context through a persistent graph of execution dependencies. We develop Tool-Flow Analysis to track how later operations reuse information from earlier tool results, providing a signal called observed reuse. A renderer combines this signal with recency and semantic relevance to select results within a fixed history budget, retaining omitted results for later use. Across AppWorld and 8-objective QA with three execution models, ContextRender outperforms the evaluated context management baselines using a 6K history budget, well below the models' maximum context windows. Within this budget, it achieves task performance close to or above that of passing the full history while reducing mean inference cost by 10.2%-32.2% relative to Full history. Ablations show that observed reuse improves task performance and retention of results reused later.

---


### 389. [Optimizer-dependent training dynamics converge to the same one-third optimal data scaling](https://arxiv.org/abs/2609.37745)

**<font color=#1a73e8>作者：</font>** Hyunseok Lee, Mihir Basil, Yizhou Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural scaling, in which loss falls as a power law with training, is central to large language models, and one recent proposal is that a $1/3$ exponent emerges from learning peaked distributions. That account describes SGD, but models in practice are trained with adaptive optimizers. Here we separate two exponents the $1/3$ account does not distinguish: how fast the loss falls with training steps along a single run, and how fast the optimally tuned loss falls with dataset size $D$. We show that the first, a dynamic exponent, is optimizer-specific while the second, an optimal data exponent, converges to $1/3$ across optimizers. In an online teacher-student model we decompose the loss into norm growth (radial) and alignment toward the teacher direction (tangential), each decaying as a power law with dynamic exponents $\alpha_{r}$ and $\alpha_{t}$. Under SGD, both are close to $1/3$, so the data exponent is also $1/3$ across different learning rates. Under Adam the two separate: $\alpha_{r} \simeq 0.48$ but $\alpha_{t} \simeq 0.08$. Since the total loss is minimized when these two parts are balanced, the optimal learning rate is optimizer-dependent: $D$-independent for SGD but falls with $D$ for Adam. Yet tuned to that optimum, the loss returns to $D^{-1/3}$ for both. A stochastic-dynamics analysis explains why: the optimizers can trade decay speed between the two channels, but they all fall on a single dynamic exponent relation, $2\alpha_{r}+ \alpha_{t} = 1$, which fixes the optimal data exponent at $1/3$. Across seven optimizers, including Muon, the measured exponents are consistent with this relation, and the optimal-loss envelopes agree with $D^{-1/3}$ across them. The optimizer sets how fast a model learns per step; tuned optimally, it changes the prefactor but not the rate at which loss falls per sample.

---


### 390. [Multi-Site Real-World Performance of Commercial AI for Pulmonary and Incidental Pulmonary Embolism Detection](https://arxiv.org/abs/2609.37750)

**<font color=#1a73e8>作者：</font>** Aawez Mansuri, Mohammadreza Chavoshi, Theodorus Dapamede 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pulmonary embolism (PE) is a leading cause of cardiovascular mortality, yet the real-world performance of FDA-cleared AI detection models remains incompletely characterized. We retrospectively evaluated two FDA-cleared AI algorithms from a single commercial platform (Aidoc Medical BriefCase), one for PE triage on dedicated CT pulmonary angiography (CTPA; n = 30,678) and one for incidental PE (iPE) detection on routine contrast-enhanced CTs (n = 37,191), across a 17-facility academic health system. Reference-standard labels were extracted from radiology reports using a validated LLM pipeline (97% accuracy, kappa = 0.94). The PE model achieved 86.8% sensitivity and 99.1% specificity, with sensitivity declining from 99.3% for saddle emboli to 72.9% for subsegmental PE, and from 89.7% for acute to 65.3% for non-acute PE. The iPE model achieved 73.5% sensitivity and 99.8% specificity. Both models demonstrated lower sensitivity than FDA-clearance benchmarks while exceeding cleared specificity, with diminishing performance for peripheral and non-acute emboli mirroring known human reader limitations and underscoring the need for standardized post-market surveillance of AI-enabled medical devices.

---


### 391. [Cross-Entropy Guided Routing in Mixture-of-Experts Large Language Models](https://arxiv.org/abs/2609.37751)

**<font color=#1a73e8>作者：</font>** Yury Nahshan, Nati Daniel, Jacob Goldberger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse mixture-of-experts (MoE) large language models scale model capacity by routing each token to a small subset of experts. Their routers are regularized with load balancing terms and learn affinity scores through the language-model objective. However, these objectives do not provide direct alignment between routing affinities and token-level error. We introduce token-error supervision for sparse routing in two forms. The first form predicts an error score per expert. The affinity-weighted aggregate of these scores is aligned to the next-token cross-entropy loss, while the individual scores attenuate affinity before top-$K$ selection. The second directly aligns the router's affinities to the model's objective without requiring an additional head or inference-time modification. Both formulations use the Itakura--Saito divergence or an exponential negative log-likelihood for aligning affinities and token errors. Across two sparse MoE backbones and four multiple-choice question-answering benchmarks, we evaluate both supervision mechanisms. On Granite, our method improves accuracy by approximately 2.3 percentage points on average over a parameter-matched routing baseline. With stronger supervision, the gain on ARC-Challenge reaches 2.94 points. Both mechanisms preserve the native sparse execution budget and aggregation policy. Our code is available in the supplementary materials.

---


### 392. [Selective Channel Restoration for Backdoored Vision-Language Models](https://arxiv.org/abs/2609.37759)

**<font color=#1a73e8>作者：</font>** Shuming Liu, Zhifang Zhang, Suqin Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) exhibit strong multimodal capabilities but remain vulnerable to backdoors implanted through poisoned fine-tuning data. Existing defenses often require extensive parameter updates during fine-tuning or incur per-query overhead during inference. To address these limitations, we propose Perturb-Select-Restore (PSR), a post-training defense that performs sparse updates to the projection interface and introduces no additional computation during inference. We reveal that backdoored VLM projectors are substantially more sensitive to bounded perturbations than clean VLM projectors, a phenomenon we term projection fragility. Building on this finding, PSR identifies the output channels most sensitive to perturbations in each projection layer of a backdoored VLM and restores their parameters to the corresponding pretrained values. Experiments across multiple tasks show that PSR reduces attack success rates to near zero while preserving clean-task performance.

---


### 393. [OmniVCBench: Benchmarking Evidence-Grounded Multimodal Reasoning Towards AI Virtual Cells](https://arxiv.org/abs/2609.37773)

**<font color=#1a73e8>作者：</font>** Manyu Li, Xunkai Li, Yongfu Xiong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence Virtual Cells (AIVCs) are envisioned as scientific agents that simulate cellular responses, explain underlying mechanisms, and support hypothesis-driven discovery. Existing AIVC benchmarks, however, operate primarily at the simulation layer, motivating complementary evaluation of how models interpret experimental evidence and formulate biological hypotheses. We introduce OmniVCBench, a figure-centric, source-traceable benchmark for the interpretation component of an AIVC. It contains 6,077 curated single- and multi-subfigure question--answer pairs derived from figures and experimental contexts in the scientific literature. Guided by Bloom's taxonomy, we instantiate interpretation-layer counterparts of the AIVC Predict--Explain--Discover agenda through three scientific reasoning tasks. We further introduce AIVC-Judge, a task-conditioned MLLM-as-a-judge framework with category-specific, reference-aware rubrics for evaluating open-ended responses. A complementary Model-Derived Hard-Negative Mining (MDHNM) strategy converts plausible errors observed during model inference into MCQ distractors for lower-cost evaluation. Within the evaluated heterogeneous model pool, MCQ accuracy correlates positively with AIVC-Judge scores, providing a complementary view of performance alongside open-response evaluation. Code and data demo are available at this https URL.

---


### 394. [Selecting What Matters: Semantic Compression-Guided Selective Pooling for Long-Context Embeddings](https://arxiv.org/abs/2609.37782)

**<font color=#1a73e8>作者：</font>** Zifeng Cheng, Jie Zheng, Zhiwei Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong potential as training-free text encoders for long-context embeddings. Existing approaches primarily improve information flow under causal attention and typically construct embeddings by uniformly averaging all token representations. However, for long documents, such mean pooling can dilute salient semantic information with abundant redundant or weakly informative content. To this end, we propose SCSP, a training-free framework that leverages semantic compression for informative token selection in long-context embedding. Specifically, SCSP first partitions a document into sentence-aware chunks and appends a semantic compression prompt to each chunk. A prompt-isolated attention mask preserves information flow among document tokens while restricting each prompt to its corresponding local context. We then use the attention patterns elicited by these prompts to estimate token importance, select informative tokens, and aggregate their intermediate-layer representations into the final embedding. Extensive experiments on long-context embedding benchmarks demonstrate that SCSP can be integrated into both zero-shot and fine-tuned models in a plug-and-play manner, consistently improving their performance.

---


### 395. [CHOQOLATE: Organizing Concept Bottleneck Latent Spaces with Choquet Integrals](https://arxiv.org/abs/2609.37786)

**<font color=#1a73e8>作者：</font>** Rémi Kazmierczak, Johanne Cohen, Marianne Clausel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) built on vision-language models such as CLIP represent a latent space as human-understandable concepts. These representations are unfaithful: related concepts are entangled, so individual scores do not reflect their intended meaning. We propose CHOQOLATE, an interpretable-by-design layer based on 2-additive Choquet integrals, which merges correlated concepts into compact nodes. Across four datasets, CHOQOLATE achieves a favorable accuracy-interpretability trade-off, with weight-sparse and semantically coherent nodes. A closed-form gradient derivation, backed by experiments, explains why Choquet layers drive this organization without explicit supervision. Choquet weights also map directly to Shapley values, which enables test-time intervention. On standard bias-mitigation benchmarks, suppressing spurious concepts after training performs on par with methods that require group annotations or retraining, while needing neither.

---


### 396. [A Proposed Rubric for Evaluating Expressed Clinical Reasoning in Large Language Model Responses](https://arxiv.org/abs/2609.37788)

**<font color=#1a73e8>作者：</font>** Zhangshu Joshua Jiang, Zina Ibrahim, James T. Teo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubrics support the structured evaluation of language models. We propose a rubric for assessing expressed clinical reasoning in model responses, drawing on three bodies of work: medical education assessment frameworks (ART, SCT, Key Feature Problems and OSCE); clinical LLM benchmarks (MedR-Bench, HealthBench, TIMER-Bench, this http URL, PrIME-LLM and PatientSafeBench); and general LLM reasoning evaluation research, including the Factuality-Validity-Coherence-Utility taxonomy, FaithCoT-Bench and C2-Faith. We use groundedness as a clinically oriented adaptation of the taxonomy's factuality category. The rubric brings these concepts together in a multidimensional framework for scoring free-text responses to gold-standard clinical vignettes. It includes provisional behavioural anchors, applicability rules and a separate flag for case-specific safety-critical errors. General-domain frameworks inform its design but are not treated as validated clinical instruments. The rubric does not replace case-specific reference criteria or the task-specific metrics of existing benchmarks. It has not yet been tested for inter-rater reliability, construct validity or clinical utility. Its immediate purpose is to make evaluation decisions explicit and open to scrutiny before empirical testing.

---


### 397. [CompOrca: Corpus-Scale Compliance Labelling of Instruction-Tuning Data](https://arxiv.org/abs/2609.37807)

**<font color=#1a73e8>作者：</font>** Philipp E. Glass, Alina Miron  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Studying how fine-tuning shapes refusal and noncompliance behaviour requires identifying training examples that refuse, evade or otherwise fail to fulfil the requested task. But existing annotation covers evaluation sets of a few thousand prompts at most. We present CompOrca, a compliance labelling over the entirety of the 4,233,923-example OpenOrca corpus. Every example was classified as compliant or noncompliant by five independent passes of an open-weight LLM judge (LongCat-2.0, 1.6T parameters), and the corpus is released as unanimous compliance (94.75%), unanimous noncompliance (1.28%), and nonunanimous rows (3.97%) along with the raw vote counts. A single pass flags 2.7-3.2% of the corpus as noncompliant, while only 1.28% is flagged by all five, allowing for filtering the most ambiguous samples. Against 450 human-annotated examples, 150 of them annotated twice (human-human $\kappa = 0.93$), the unanimous compliance and noncompliance labels are 97.3% and 86.7% precise, the latter a high-precision subset, not a complete enumeration, of noncompliance. Published refusal-detection methods recall only between 0.4% and 94.1% of the noncompliance class. We release the full corpus with its per-row labels and vote counts at this https URL

---


### 398. [Thinking in Depth, Speaking Directly: Recurrent Latent Reasoning for Paralinguistically Grounded Spoken Dialogue](https://arxiv.org/abs/2609.37818)

**<font color=#1a73e8>作者：</font>** Shengbo Cai, Yuxiang Wang, Jingran Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Empathetic spoken dialogue requires models to use both what is said and how it is said to decide how to respond. Explicit CoT can improve paralinguistic perception and make acoustic cues more explicit in replies, yet does not ensure their effective use in response planning. We call this mismatch the perception-reasoning gap. In addition, CoT may not fully capture acoustic cues in words, and generating it adds inference latency. To address these limitations, we introduce LoopSLM, which builds on looped Transformers for latent reasoning, reusing a decoder block to refine hidden states with acoustic grounding at every pass. Its two-stage training further narrows the perception-reasoning gap by separating learning to reason from learning to respond, enabling direct inference without CoT. On EchoMind, LoopSLM improves paralinguistic understanding, reasoning, and reply quality over Qwen2.5-Omni-7B. Against the CoT-SFT baseline, LoopSLM gains over 20 points in reasoning accuracy while generating 64.5% fewer tokens at half the latency. It also outperforms Qwen3-Omni-Thinking on most empathetic reply metrics with 34x lower latency. Despite training only on dialogue data, LoopSLM improves accuracy on general audio benchmarks.

---


### 399. [Making Duplicate Reimbursement Unrepresentable: A Verified Ethereum E-Invoice System for Humans and AI Agents](https://arxiv.org/abs/2609.37819)

**<font color=#1a73e8>作者：</font>** Jia Cai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electronic invoices are replacing paper invoices worldwide, but today's centralized architectures leave three problems unsolved on the consumption side: an invoice can be submitted for reimbursement repeatedly, authenticity is difficult for recipients to verify, and data is siloed at a central authority that forms both a performance bottleneck and a single point of failure. This paper presents the design, formal analysis, and implementation of a complete blockchain-based electronic invoice system on Ethereum. We formalize the invoice lifecycle as a guarded labeled transition system and prove, under standard cryptographic and consensus assumptions, that the system guarantees: (i) reimbursement uniqueness--an invoice is reimbursed at most once, even across mutually distrusting organizations; (ii) face integrity--any verified invoice matches the recorded one unless keccak256 second-preimage resistance is broken; and (iii) authorization soundness for every lifecycle operation. The core invariants are machine-checked using Solidity SMTChecker, proving inductive validity across all reachable transaction sequences. The architecture models each invoice as a non-fungible, non-tradable token whose state transitions through five guarded subsystems, employing a lock-based protocol that makes duplicate reimbursement unrepresentable rather than merely detectable. We implement the design as a Solidity 0.8 contract with a four-role web application and evaluate it on a private Ethereum network: issuing costs 646,773 gas, full reimbursement costs under 135,000 gas, all operations run in O(1) time, and a single node sustains 137 issuances/s. Finally, the verified contract serves as a safety envelope for LLM-based reimbursement agents, provably rejecting unsafe actions (duplicate, over-limit, or forged-receipt claims) even when the agent's internal policy fails. All code and benchmarks are open-source.

---


### 400. [The Geometry of Inference in Transformer Residual Streams](https://arxiv.org/abs/2609.37824)

**<font color=#1a73e8>作者：</font>** Timur Mudarisov, Mikhail Burtsev, Radu State  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer language models build predictions through successive residual updates, but how their representations become specific to an eventual outcome remains unclear. We study this process by comparing intermediate residual states with their own final states and an empirical bank of final states from other contexts. Across six pretrained language models, the own endpoint becomes preferable to the average alternative early, while many individual endpoints remain closer. These competing sets generally shrink with depth, but their membership changes and their surviving endpoints need not become more similar to one another. Directional alignment and endpoint rank can therefore improve while Euclidean distance to the final state changes little. We develop a simple high-dimensional model that separates the roles of norm, alignment, and endpoint geometry, showing how gradual directional changes can produce sharp reductions in competition. We also prove that a straight path toward the own endpoint cannot introduce new competitors under either Euclidean or cosine distance; observed entries thus establish departures from straight-line convergence. Finally, endpoints associated with lower-ranked output tokens tend to lie farther away in cosine distance across all studied models, connecting residual geometry to output organization. Together, these findings characterize increasing geometric specificity during transformer inference and explain why distance, competitor count, and concentration of the surviving endpoints provide distinct views of that process.

---


> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
