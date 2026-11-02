# 🧠 大模型相关研究 | 2026年11月03日

> 本类共 **188** 篇论文：已确认 **175** 篇，待复核 **13** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-188**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-188**

---

### 151. [ReX-GG: a LLM Ensemble Pipeline for Relation-extraction and Graph Generation](https://arxiv.org/abs/2610.41901)

**<font color=#1a73e8>作者：</font>** Giacomo Magnifico, Eduard Barbu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current LLM ensemble frameworks focus on multi-step setups with additional modules for answer ranking, often opting for token and span analysis rather than structured outputs, leading to heavyweight architectures with potential fail states along the pipeline. Faster, lighter solutions are more vulnerable to hallucination propagation and can lack output control in more complex pipelines. This paper proposes a customisable, lightweight ensemble workflow of coordinated Large Language Models that leverages JSON-structured outputs and anonymous peer-review ranking to mitigate hallucinatory outputs and single-model failure points. The pipeline is demonstrated on a relation extraction task applied to popular science articles in English, targeting four ontologically-grounded relation types (strong causation, weak causation, contrastive, and compositional), with semantic node canonicalisation and interactive, colour-coded HTML causal graphs as the final output. Performance is evaluated through an anonymous user study, achieving an average perceived accuracy of 0.778 against a human-annotated gold standard. The modular architecture supports flexible deployment across both API-based and in-house LLM setups, and the full framework is released under an open license to foster reproducibility and collaborative research.

---


### 152. [Structure-Aware Skill Retrieval and Arbitration for Optimization Modeling](https://arxiv.org/abs/2610.41909)

**<font color=#1a73e8>作者：</font>** Anran Liu, Benzhao Hou, Zongsheng Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can turn natural-language optimization tasks into solver-checked answers, but current agents remain brittle under narrative rewrites and often store reusable experience at the instance level. We introduce \textsc{ArchOR}, an archetype-centric skill agent that builds on \textsc{OptSkills} by adding two retrieval-focused modules. \emph{Centroid-Aware Representation Learning} (CARL) refines the ordering of cached skill representations through a low-rank prototype residual. \emph{Signature-Guided Retrieval} (S\textsuperscript{3}R) attaches open-dimensional structural signatures to skills, prioritizes candidates by weighted Jaccard overlap, and bounds semantic re-ranking to a top-$K$ set. A baseline-preserving arbitration rule determines when the structural route should replace the original selector. With the same DeepSeek-V4.1-Flash backbone and released skill library, \textsc{ArchOR} reaches 65.00\% Micro-Avg.\ Pass@1 across five benchmarks, improving over \textsc{OptSkills} by 1.64~pp Micro-Avg.\ and 2.68~pp Macro-Avg.

---


### 153. [Aligning MLLMs with the Latent Structure of Human Cognition via Behavior-Derived Semantic Dimensions](https://arxiv.org/abs/2610.41951)

**<font color=#1a73e8>作者：</font>** Ning E, Changde Du, Yizhuo Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved impressive performance across a wide range of reasoning tasks, yet it remains unclear whether their internal representations and decision criteria align with the latent structure of human cognition. In this work, we propose a novel framework to align MLLMs with the multidimensional mental representations underlying human similarity judgements. We build on a previously established behavior-derived semantic embedding space, in which objects are represented along 66 interpretable dimensions derived from 4.70 million human Odd-One-Out (O1O) judgements. For each triplet, we infer the most salient decision dimension and convert it into a dimension-grounded linguistic rationale. This enables MLLMs to learn both the final choice and a justification consistent with the inferred behavioral criterion. Experimental results demonstrate that our approach improves model consistency with human similarity judgements while retaining competitive performance on standard multimodal benchmarks. Furthermore, using searchlight Representational Similarity Analysis (RSA) on an independent fMRI Natural Scenes Dataset (NSD), we observe increased representational alignment between model and human. Ultimately, our findings point to a data-driven route for incorporating human cognitive structure into MLLMs alignment. The code is available \href{this https URL}{here}.

---


### 154. [Prune Gradually, Adapt Sparsely: Efficient Pruning of Large Language Models at Extreme Sparsity](https://arxiv.org/abs/2610.41968)

**<font color=#1a73e8>作者：</font>** Jean Lucien Randrianantenaina, Hung Nguyen, Nasib Ullah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Weight pruning can reduce the storage and inference cost of large language models (LLMs), but preserving quality at high sparsity levels remains challenging. Existing methods face a quality-cost trade-off in this regime. One-shot pruning is cheap but degrades sharply as sparsity increases, even when followed by post-pruning recovery. A growing line of work instead optimizes the mask directly from the dense model under the end-to-end objective; among these methods, [Lee et al.,2026], the recent state of the art at extreme sparsity, reaches high quality but at the cost of model-sized optimizer state and auxiliary variables. To address this gap, we propose ETAPS, which prunes gradually and adapts sparsely: it tightens a global sparsity constraint in progressive stages while training a sparse delta with a small, fixed budget. Our key observation is that gradual weight removal keeps each pruning step small enough for sparse adaptation to compensate, allowing the adapted model to provide end-to-end gradients that guide the next pruning decision without model-sized optimizer state. Across six models from 125M to 13B parameters, ETAPS achieves lower perplexity than ELSA at every evaluated sparsity from 50% to 90%, with perplexity reductions of up to 42%. ETAPS is also far cheaper: at 90% sparsity, it prunes LLaMA2-7B on a single H200, where ELSA uses four, with $5.0\times$ smaller total persistent state and 49% fewer GPU-hours. Together, our findings point to a promising direction for achieving high quality in demanding regimes such as extreme sparsity at substantially lower cost.

---


### 155. [TwinPast: Benchmarking Historical Evidence Use in Streaming Video Understanding with Evidence Contrastive Video Pairs](https://arxiv.org/abs/2610.41983)

**<font color=#1a73e8>作者：</font>** Haotian Yang, Yong Chen, Cheng Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High accuracy on streaming video benchmarks does not establish whether a model uses visual history. Our review of OVO-Bench and StreamingBench finds that recent frames suffice for 32% of sampled historical questions, while models also answer many questions correctly from the question and options alone. We introduce TwinPast to test whether answers correctly follow changes in history, using 350 human-reviewed video pairs spanning five historical tasks. Each pair holds the recent video context, question, and ordered options fixed while changing critical historical evidence and the correct answer. Each video is evaluated independently, and PairAcc requires correct answers for both histories. We evaluate 34 model and input configurations. For Qwen3-VL-8B and DeepSeek-Flash, historical inputs improve performance on TwinPast, reversing the recent-frame advantage on existing benchmarks. The strongest evaluated streaming system reaches 49.14% PairAcc, compared with 66.57-91.43% for the evaluated general-purpose models. This gap persists across all five tasks. Case studies further show that models select states from the wrong time or contradict recorded event order despite retaining the relevant evidence. These findings highlight the need to connect historical memory and retrieval with reasoning that uses evidence according to the question's temporal references and event relations.

---


### 156. [MoETok: Sparse Expert Routing for 1D Visual Tokenizers](https://arxiv.org/abs/2610.41992)

**<font color=#1a73e8>作者：</font>** Jiahao Guo, Bao Tang, Haoxiang Cao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern visual tokenizers aim to preserve fine-grained visual details while learning high-level semantic representations for downstream generation and understanding. Query-based 1D visual tokenizers encode images into flexible latent sequences, yet how individual learnable queries gather and encode image information remains poorly understood. We reveal that these queries spontaneously develop complementary roles under semantic supervision: a small set of Content queries captures high-level semantic information, while a larger set of Detail queries preserves fine-grained visual details for reconstruction. To adapt token processing to these heterogeneous roles, we introduce MoETok, a 1D visual tokenizer that routes tokens through sparsely activated experts. Jointly optimized with reconstruction and semantic objectives, the router learns role-specialized processing paths adapted to each token's representation. Across model scales and token budgets, MoETok consistently improves reconstruction, semantic representation, and autoregressive generation over dense tokenizers under matched supervision and active computation. On ImageNet, it combines strong reconstruction and semantic representation with state-of-the-art class-conditional generation within the 1D tokenizer family. We further validate MoETok at scale in a unified autoregressive model jointly trained for understanding and generation with a next-token cross-entropy objective. The resulting model combines competitive visual understanding with state-of-the-art generation among unified discrete models, matching or surpassing diffusion-based models such as BAGEL and Qwen-Image on benchmarks including DPG-Bench (87.61), GenEval2 (40.04 GM), and WISE (0.49).

---


### 157. [DAMI: Dual-Axis Memory Initialization for Enhanced Long-Context Retrieval in Gated Linear Attention](https://arxiv.org/abs/2610.41994)

**<font color=#1a73e8>作者：</font>** Zhangchi Feng, Harry Jiang, Yangyifei Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Linear attention scales linearly with sequence length, but its finite-state memory can limit long-context retrieval. In gated linear recurrences, memory retention depends on state decay, which is shaped jointly by gate parameters A_log and dt_bias and by input activations. In controlled Gated DeltaNet (GDN) experiments, both parameters remain highly correlated with their initial values after training, highlighting the importance of initialization. Therefore, we introduce Dual-Axis Memory Initialization (DAMI), which jointly configures these parameters before training. DAMI assigns geometric timescales across heads for varied retrieval distances and a low-high-low input-sensitivity profile across layers. A small activation sample calibrates the GDN-family implementation to match both behavioral targets without adding trainable parameters. Across GDN, KDA, GDN2, Mamba-2, and RWKV-7, DAMI improves average RULER-style retrieval accuracy by 5.29 to 16.71 percentage points over the corresponding random-initialization baselines. Performance on language modeling, commonsense reasoning, and 2K real-world retrieval remains broadly comparable to those baselines. Our code is available at this https URL.

---


### 158. [Less Loss, Fixed Weights: Logit Corrections for Forgetting](https://arxiv.org/abs/2610.42000)

**<font color=#1a73e8>作者：</font>** Hanyu Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a language model is fine-tuned to follow instructions, or further pretrained on a new subject, it often gets worse at predicting standard web text. This is known as "forgetting." We ask whether this loss can be undone by simple, fixed adjustments to the model's final token predictions. Across 14 pairs of base and derived models, from 1B to 7B parameters, we fitted a fixed bonus or penalty for each token (a vocabulary bias), alone or together with a temperature. On text held out from correction fitting, the largest top-4K bias recovery estimate is under 10%, with loss conditional on the retained vocabulary. Combining the bias with a temperature recovers up to 36%. Models further pretrained on math lose the most and recover almost nothing. Finally, in a controlled simulation where a model is damaged at random, with no planted bias or temperature change, the bias-plus-temperature fix still recovers 29%. Most of the real-model loss increase stays out of reach of our restricted fits.

---


### 159. [TradeWar: A Benchmark for Execution-Grounded Trade Negotiation with Adaptive LLM Agents](https://arxiv.org/abs/2610.42004)

**<font color=#1a73e8>作者：</font>** Xiangyu Kong, Ruirui Yang, Xia Hou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-turn negotiation remains a challenging problem for large language model (LLM) agents. While LLMs can conduct natural-language dialogue, existing benchmarks predominantly assess only agreement rates, overlooking whether negotiated commitments actually create value once executed. To address this gap, we introduce TradeWar, a multi-country simulation benchmark that translates negotiation dialogues into concrete tariff and trade-share policies, enforces capacity and network constraints during settlement, and evaluates outcomes via an Economic Health Index (EHI). To solve this execution-grounded task, we propose TACTIC (Trade-aware Adaptive Consolidation and Theory-of-mind for International Commerce), an agent that iteratively refines its negotiation strategy across episodes-without updating base LLM weights-by leveraging prior experience, opponent behavior, and past settlement outcomes. Despite using zero-shot chain-of-thought (CoT) prompting, PromptLLM attains a 75% agreement rate but only 57.1 final EHI (*100), whereas TACTIC reaches 68.8. Across 20 sequential episodes and three seeds, TACTIC's final EHI improves from 58.2 to 73.2, compared with 65.2 for an ablation without cross-episode updates. Under technology-controls and energy-crisis shocks, TACTIC also exhibits smaller performance degradation than PromptLLM and MemoryLLM. These results indicate that CoT deliberation and interaction memory alone do not fully address delayed execution feedback, whereas settlement-grounded adaptation improves long-horizon negotiation in TradeWar.

---


### 160. [TurnTurk-GPT: Text-Based Turn-Taking Prediction for Turkish](https://arxiv.org/abs/2610.42010)

**<font color=#1a73e8>作者：</font>** Ahmet Tuğrul Bayrak, Fatma Nur Korkmaz, Nur Yağmur Tuncer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents TurnTurk-GPT, a text-based turn-taking predictor for Turkish obtained by fine-tuning a Turkish GPT-2 model with the TurnGPT objective on synthetic and real dialogue, and evaluates it on real Turkish conversation against rule baselines, a zero-shot Turkish language model and a widely used multilingual end-of-turn detector. Evaluation uses word-level decision points on unpunctuated, lower-cased text approximating the output of streaming speech recognisers, recording-disjoint and speaker-disjoint folds, nested threshold selection and paired cluster bootstrap tests. TurnTurk-GPT outperforms the multilingual detector under both recording-disjoint and speaker-disjoint evaluation. It outperforms the zero-shot language model only when the test speakers occur in training; on unseen speakers the two are statistically indistinguishable. Removing the suffixes of the turn-final word reduces AP by up to 44%, against 2% for a sentence-internal word, locating the Turkish end-of-turn cue in verb-final morphology. Synthetic dialogue alone yields the weakest trained model, and when a speaker pauses the zero-shot and multilingual baselines remain close to chance. The model and the evaluation protocol are publicly released.

---


### 161. [Asynchronous Flow Map Language Models](https://arxiv.org/abs/2610.42018)

**<font color=#1a73e8>作者：</font>** Chanhyuk Lee, Wonjung Kim, Patrick Pynadath 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The order in which tokens are predicted in language modeling has a profound impact on the quality of generated sequences. Autoregressive and masked diffusion models iteratively fill in tokens and can exploit such orderings across generation steps, but how to leverage an ordering for one-step parallel language modeling is unclear. We introduce asynchronous flow map language models (aFMLMs), which incorporate prediction order into one-step modeling by learning the flow maps of asynchronous flows. These flows specify an ordering through a tokenwise time schedule that controls the relative denoising progress of tokens. We formulate a general class of asynchronous flows that admit both prescribed and learned, state-adaptive schedules, show that they define valid flow maps, and develop new methods for their flow map distillation. The resulting models can generate all tokens in a single forward pass by internalizing the ordering encoded in the flow into their hidden computations. On Sudoku solving and code generation for GSM8K math word problems, aFMLM establishes new state-of-the-art one-step performance.

---


### 162. [Know When the Equation Is Wrong: Structural Uncertainty for LLM-Guided Symbolic Regression under Extrapolation](https://arxiv.org/abs/2610.42024)

**<font color=#1a73e8>作者：</font>** Mostafa Cham, Bayu Adhi Tama, Jianwu Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can help discover mathematical equations from data, but most LLM-guided symbolic regression methods focus on a single best equation without quantifying uncertainty over alternative functional forms. This is challenging because distinct equations can fit the observed data similarly while producing substantially different extrapolations. Our experiments on the LLM-SRBench dataset show that standard conformal intervals achieve nominal in-distribution coverage but frequently fail under extrapolation. To tackle this challenge, we introduce LLM-SR-UQ, a framework that retains competing equation structures and uses their disagreement to characterize uncertainty about the underlying functional form. We extend the standard fixed-width conformal approach to quantify structural intervals, which measure disagreement among candidate equations and identify where prediction intervals should widen. Extensive experiments show our framework substantially improves coverage attainment by incorporating structural disagreement while preserving in-distribution coverage. Our approach also shows good generalizability when it is applied to other symbolic-regression methods.

---


### 163. [There Is No Free Loop: When Does Looping a Trained Model Pay for Its Inference Compute?](https://arxiv.org/abs/2610.42030)

**<font color=#1a73e8>作者：</font>** Rhea Sanjay Sukthanker, Pashmina Cameron  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looping re-applies a block of layers so that each token passes through the block more than once. Adding a loop to a trained model is attractive because it leaves the parameter count, and hence the disk size, the memory footprint and the training cost unchanged. Unfortunately, every generated token pays for the loop. Re-applying m of N layers makes each token about (N+m)/N times as expensive. Loops that a model learns during large-scale pretraining justify this price, but whether loops added after pretraining justify this cost remains unclear. We compare a looped model with two simple baselines. We first compare it with the same model trained identically without the loop (equal parameters). Secondly, we compare it with the best unlooped use of the same inference floating-point operations (equal FLOPs). Across Qwen3 and Qwen3.5 models from 0.8B to 9B parameters, only the looped 0.8B model beats both baselines. At 4B and 9B, the looped model does not beat the first baseline, i.e. the same model trained without the loop. This is not because the benchmarks are too easy, since on the same benchmarks the unlooped 9B model still scores up to 13 points higher than the 4B model, showing that there is ample room for improvement. Introducing loops in an already pretrained model therefore only pays for small models with a fixed parameter budget.

---


### 164. [Beyond Smart Homes: Characterizing IoT Vulnerabilities Across Sectors, Vendors, and Products](https://arxiv.org/abs/2610.42032)

**<font color=#1a73e8>作者：</font>** Tina Rezaei, Suzan Bayhan, Andrea Continella 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Internet of Things (IoT) has expanded beyond consumer smart homes to sectors, such as industrial systems, healthcare, and smart cities, broadening the IoT attack surface. Prior empirical work has focused on studying aggregate IoT vulnerability characteristics or specific protocols, so patching is directed by aggregate security guidance. However, if dominant weaknesses differ substantially across sectors or products, such uniform guidance misdirects the remediation effort. To address this gap, we present a fine-grained, data-driven analysis of IoT vulnerabilities using a dataset of more than 15,000 IoT specific CVEs. We design a pipeline to enrich noisy CPE (Common Platform Enumeration) metadata, normalizing vendors and products, then assigning product type and sector labels using lexical matching, fuzzy clustering, and LLM-assisted classification. We find meaningful differences in the weakness profile of IoT sectors. For example, healthcare is dominated by authentication and credential weaknesses, while automotive faces memory issues. More importantly, we find that weakness profiles are more similar across different product types from the same vendor than across the same product type built by different vendors. This suggests vendor-level factors such as shared code and development practices dominate weakness inheritance, making a vendor's disclosure history informative about its other products. Our findings suggest weakness classes should be used to prioritize remediation efforts.

---


### 165. [Same Question, Different Answers: Auditing Persona-Dependent Variation in Six LLMs on Smoking-Cessation Advice](https://arxiv.org/abs/2610.42039)

**<font color=#1a73e8>作者：</font>** Artin Yousefi, Aizierjiang Aiersilan, Lorien C Abroms 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hundreds of millions of people now ask large language model (LLM) chatbots for health advice, which raises a question that is simple to pose and hard to answer: does everyone get the same advice? We audit six widely deployed LLMs from four providers on smoking cessation, a domain with codified clini- cal guidance and substantial public-health stakes, by putting the same four cessation questions to twelve user personas that differ in life stage, self-described expertise, and smoking history, for a total of 2,880 responses. What the models say depends on who appears to be asking. Every model named FDA-approved prescription cessation medications less often to teen personas than to adult personas, by 32 to 67 percentage points, and in five of six models a persona presenting health- care expertise received fewer facts than a persona presenting none. We then evaluate one deployable intervention: a short system prompt specifying a factual floor, the set of core med- ical facts every user should receive when they are relevant, while leaving tone, vocabulary, and framing free to adapt. The prompt narrows persona differences in every model, but its effect on overall fact coverage varies in both magnitude and direction across models, so a prompt validated on one system cannot be assumed to transfer to another. Two cautions frame these results. Equal mention rates are not always the correct clinical target, because prescription cessation pharmacother- apy is not recommended for minors, so a defensible factual floor must be age-aware rather than uniform. And because our personas vary on several attributes at once, we report scenario- level differences rather than isolated effects of age or expertise. We release all 2,880 responses and the analysis code.

---


### 166. [CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness](https://arxiv.org/abs/2610.42054)

**<font color=#1a73e8>作者：</font>** Xiao Yu, Justin Chih-Yao Chen, Zaid Khan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become the standard method for training language models to reason. However, RLVR typically relies solely on outcome correctness, which does not guarantee that the CoT causally contributes to the final answer. Without this connection, outcome rewards may fail to reinforce high-quality reasoning. Existing causality metrics assess CoT causality by perturbing the CoT, such as deleting reasoning steps or injecting errors, and measuring changes in the final answer. However, these perturbations inevitably alter information in each step. Consequently, high causality scores may reflect sensitivity to information changes introduced by perturbation rather than true causality. Such confounding effects further induce undesirable reasoning behaviors when these metrics are used as training rewards, including generating less informative CoTs and reducing exploration and self-correction. To address this problem, we propose CRoS (Causality Reward on Scrambled CoTs), a novel CoT causality metric that perturbs the order of reasoning steps without altering content, thereby preserving information within each step. On Reasoning Gym with Gemma-3-4B, CRoS outperforms existing causality and outcome rewards in out-of-domain accuracy, CoT quality, and CoT faithfulness. Specifically, CRoS achieves 46.8% accuracy on five unseen logic and games datasets, outperforming the strongest baseline (43.8%). It also achieves better CoT quality, consistently outperforming baselines in CoT-Pass@K from K=1 to 128, averaging 43.4% vs. 41.4%. For CoT faithfulness, CRoS achieves a hint acknowledgment score of 34.0% vs. 20.2%.

---


### 167. [PersonaChatBench: Evaluating Chat Assistants with Diverse Simulated Users](https://arxiv.org/abs/2610.42060)

**<font color=#1a73e8>作者：</font>** Zheyuan Deng, Taoran Li, Jingwen Zhang 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational assistants are expected to help people with diverse backgrounds, preferences, and communication styles. Yet evaluations centered on a single cooperative user provide limited insight into how reliably an assistant serves users with different personas. We introduce PersonaChatBench, a framework for evaluating task competence and responsiveness to diverse user needs. PersonaChatBench pairs the same underlying task with multiple simulated users, each guided by a private persona card that specifies distinct needs, preferences, and interaction behaviors. By holding the task fixed while varying the user, the framework examines how assistant performance changes across user conditions. We evaluate 20 language models across six domains, separately assessing native task outcomes, fulfillment of expressed persona needs, and simulator fidelity. Our results show that task performance and need fulfillment vary across personas and domains. Strong task performance does not necessarily translate into satisfying individual needs, and models' relative strengths in meeting those needs are not consistent across domains. PersonaChatBench makes these differences measurable, revealing gaps obscured by aggregate scores and helping identify which users an assistant serves well and where adaptation is needed. It provides a basis for evaluating consistency across users and guiding the development of assistants that better accommodate diverse needs in everyday applications.

---


### 168. [Think in 360°: Benchmarking and Bootstrapping Panoramic Video Reasoning](https://arxiv.org/abs/2610.42082)

**<font color=#1a73e8>作者：</font>** Lidong Lu, Lidong Zou, Xinyi Mao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A panoramic video captures all directions around the camera, but relevant evidence can appear in different directions and at different times. Understanding it requires models to connect observations across the viewing sphere and time. We introduce PanoVideoBench, the first manually annotated benchmark for comprehensive panoramic video understanding. Its 1,000 questions span five categories and 15 question types, with diagnostic annotations for target search and panoramic capabilities. Evaluation of 11 proprietary, open-source, and panoramic-specialized models identifies cross-view tracking and sphere-time evidence integration as their weakest capabilities. To strengthen these capabilities, we construct PanoVideoCoT, the first reasoning dataset grounded in real panoramic video, through sphere-time-grounded synthesis that converts verified panoramic observations and successful agentic explorations into 13,465 QA-CoT pairs. Starting from a general video MLLM, PanoVideoReasoner learns from this corpus through Panoramic CoT SFT and Evidence-Privileged On-Policy Self-Distillation, a panoramic instantiation of Vision-OPD's OPSD in which the teacher uses verified perspective views to guide student-generated trajectories. It reaches 55.7% on PanoVideoBench, improving the backbone by 12.5 points and the previous SOTA by 2.6. The gains concentrate on the same spatial, cross-view, and temporal capabilities exposed by the benchmark, showing that grounded sphere-time supervision can equip a general video MLLM with panoramic reasoning.

---


### 169. [RangeSWA: Training-Free Length Extrapolation for Continuous Diffusion Language Models](https://arxiv.org/abs/2610.42084)

**<font color=#1a73e8>作者：</font>** Guangfu Guo, Xiaoqian Lu, Linsey Pang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion language models show promising potential in text generation tasks, but are prone to problems such as text repetition, semantic drift, and generation quality degradation when the generation length exceeds the training length. To address these challenges, we propose RangeSWA, a training-free length extrapolation method. The method combines local sliding-window attention, remote block summaries, and dynamic content retrieval to preserve local details and support long-range context access. In addition, generation degradation caused by length extrapolation is mitigated through positional remapping, conditioning attention correction, and denoising-stage-adaptive window scheduling. We conducted experiments on multiple continuous diffusion language models, and the results show that RangeSWA can effectively reduce generative perplexity and text repetition rates in long-text generation.

---


### 170. [Subquadratic Attention with a Hierarchical Tree-Structured Indexer](https://arxiv.org/abs/2610.42112)

**<font color=#1a73e8>作者：</font>** Leon Lufkin, Cutter Dawes, Alexander Speicher 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The quadratic scaling of attention is a fundamental bottleneck limiting the long-context capabilities of large language models (LLMs). A variety of approaches have attempted to circumvent this, but they either fail to match attention's expressiveness (e.g., sliding-window or linear attention variants with fixed-size state) or only achieve constant-factor speedups (e.g., sparse attention methods whose indexers themselves scale quadratically). In this paper, we derive an asymptotically subquadratic sparse attention method based on a hierarchical, tree-structured indexer, which we call Zyphra Hierarchical Attention (ZHA). ZHA constructs a tree of recursively compressed key summaries over the KV cache, which future queries traverse from the top down to retrieve a sparse subset of keys. Crucially, by iteratively growing the tree's depth, the total cost including routing and final attention grows sublinearly in sequence length, resulting in overall subquadratic (but superlinear) scaling for attention. We demonstrate that ZHA can be cheaply applied to existing pretrained models with only a short KL distillation training stage over a few billion tokens, and maintains performance on long-context retrieval and challenging reasoning, mathematical, and agentic coding evaluation tasks. Moreover, we show that our method is highly robust to tree geometry including very deep trees of up to 6 levels. Finally, we develop a detailed performance model and show that our approach scales subquadratically, dramatically outperforms competing methods beyond 1 million context, and ultimately has the potential to extend effective context windows to the hundreds of millions or billions of tokens.

---


### 171. [ACCT: Asymmetric Cross-LLM Context Transfer](https://arxiv.org/abs/2610.42116)

**<font color=#1a73e8>作者：</font>** Yuzhe Liu, Haolin Tian, Tonghan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In real-world deployments, large language model (LLM) systems are increasingly evolving from single-model invocation toward heterogeneous deployments in which different models are dynamically invoked for inference. When the same context is reused across models, however, each newly selected target model typically has to process it again, repeatedly incurring substantial computational costs. Therefore, we propose ACCT (Asymmetric Cross-LLM Context Transfer), which targets KV cache transfer between models of different scales within the same model family. ACCT transforms the KV cache produced by a source model into sparse KV states that can be directly consumed by a target model, thereby enabling cross-model reuse of context computation and decoupling context computation from downstream inference. ACCT consists of three lightweight components: the Cartographer identifies query-relevant context tokens for each target layer and KV head; the Allocator determines how many context tokens each target layer and KV head retains under a shared total KV budget; and the Compiler transforms selected source KV into sparse target KV. The target model can therefore perform inference using the transferred KV without reprocessing the original context. We evaluate ACCT in two complementary settings comprising five general-capability benchmarks and six highly context-dependent tasks. Experiments show that ACCT matches or exceeds the target model's original inference performance even when reducing the KV cache size by 75%. At a context length of approximately 19K tokens, ACCT's KV conversion achieves a 6.5-21.2 times speedup over target context prefill. These results demonstrate the feasibility of transferring context computation across models under a limited KV budget.

---


### 172. [DecisionRank: On-Policy Distillation for Decision-Model Rerankers](https://arxiv.org/abs/2610.42128)

**<font color=#1a73e8>作者：</font>** Yanran Wu, Dian Yu, Chongyang Bai 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decision models target structured tasks by directly predicting choices or scores, avoiding autoregressive decoding latency. However, transferring a generative LLM's ranking knowledge to a decision model remains challenging: the teacher expresses preferences through a ranked list of document ID sequences, while the student determines the ranking using scores from the first-token position. To bridge this gap, we introduce DecisionRank, a decision model trained through item-space on-policy distillation (OPD). Item-space OPD constructs the student's rollout by sorting its document scores into a ranked sequence. A generative teacher takes the resulting ranking list as inputs and provides conditional feedback to directly supervise those scores. Combined with offline ranking supervision, DecisionRank achieves state-of-the-art performance on both general and reasoning-intensive retrieval benchmarks such as TREC DL, BEIR, and BRIGHT. Across four benchmarks, item-space OPD consistently outperforms alternative training objectives. Even at 1.7B parameters, DecisionRank surpasses its 27B generative teacher on TREC DL19--23. At 8B, it outperforms its generative listwise counterpart while running $24.5\times$ faster on TREC DL and $16.7\times$ faster on BRIGHT.

---


### 173. [Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention](https://arxiv.org/abs/2610.42147)

**<font color=#1a73e8>作者：</font>** Ales Kubicek, Andrea Caciolai, Liangzu Peng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic workflows are increasingly shifting towards long-horizon tasks, such as open-ended scientific work, where models benefit from long context windows. However, at ultra-long context (above 1M tokens), full attention is prohibitively expensive. A promising approach is sparse attention, in which a dedicated indexer selects a subset of keys for the attention. Yet current methods of indexing either still have quadratic cost in context size or lose accuracy at ultra-long context scale. We address this with Latent Sparse Attention (LSA), an efficient attention method that maintains accuracy at ultra-long context. In LSA, keys are hierarchically clustered in a learned latent space, and queries score the hierarchy of clusters instead of scoring every key, making prefill, decode and training faster at long context. We propose two variants, Distilled-LSA (D-LSA), which can be applied to pre-trained models via distillation, and Native-LSA (N-LSA), which is trained natively on the next-token loss alone. On GLM-5.3-FLASH (QWEN-3.8-27B) at 10M tokens, D-LSA speeds up one attention layer by 22.7x (72.4x) in prefill and 4.6x (42.5x) in decode over its original sparse attention (full attention), while keeping similar accuracy across a variety of tasks. N-LSA matches the accuracy of full attention with a training speedup of 1.6x per layer at 128k tokens. LSA offers practical and efficient attention for models to benefit from ultra-long context.

---


### 174. [Flide: Accelerating Decision Inference with Exact State Forking](https://arxiv.org/abs/2610.42148)

**<font color=#1a73e8>作者：</font>** Bobo Li, Jiajia Song, Hao Fei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decision models such as Jev have emerged as a highly promising paradigm for LLM agent systems, providing lightweight and reliable categorical reasoning for rapid System One execution. However, existing generation-oriented inference engines fail to support these workloads effectively, suffering from severe prefix recomputation overheads or distorted output probabilities. To address this challenge, we propose Flide, an efficient and exact inference engine that decouples the logical tree structure of a decision request from its physical execution within a single flattened token stream. Through ForkAttention, Flide navigates request dependencies using GPU-resident indices across both standard attention and recurrent Gated DeltaNet layers, guaranteeing in exact arithmetic that every query branch evaluates identically to an isolated forward pass. By expressing branch topologies directly in GPU-resident metadata, Flide accommodates diverse request mixtures with a compact set of pre-recorded execution graphs while enabling expanding agent histories to resume from checkpoints saved in earlier passes. Extensive evaluations on public hybrid and decision models demonstrate that Flide answers queries up to 9.5 times faster than vLLM and SGLang while staying closest to a float32 reference in total variation distance. By unifying physical execution throughput with mathematical exactness, Flide establishes a principled foundation for scalable, latency-critical decision intelligence in agent systems.

---


### 175. [Latent Reasoning in Continuous Space for Unified Multimodal Models](https://arxiv.org/abs/2610.42149)

**<font color=#1a73e8>作者：</font>** Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit the test-time scaling and fine-grained controllability observed in large language models. We attribute this failure to a fundamental modality mismatch: reasoning is performed in a discrete token space, whereas image generation operates in a continuous space. To bridge this gap, we introduce a Latent Reasoning framework in Continuous space (LARC), which alleviates the token-level bottleneck by reasoning over continuous hidden states. Specifically, the training framework consists of two stages: (i) curriculum supervised fine-tuning (SFT), and (ii) information-gain reinforcement learning (RL). First, the curriculum SFT stage gradually converts token-level reasoning into latent reasoning. Subsequently, the information-gain RL stage self-evolves latent reasoning without ground truth supervision. Experiments across diverse text-to-image generation benchmarks show that LARC consistently improves generation quality, prompt following, and compositional fidelity. Notably, LARC achieves state-of-the-art performance on GenEval with a 7%p gain over BAGEL and demonstrates clear test-time scaling behavior, outperforming token-based generation under both parallel and sequential test-time scaling strategies.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 176. [Frozen in Time: How a Physics Foundation Model Forgets Under Sim-to-Real Adaptation](https://arxiv.org/abs/2610.40857)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haaris Mian, Miles Cranmer, Alessandro Favero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific foundation models (SciFMs) have achieved remarkable performance on a wide range of PDEs, including the ability to efficiently adapt to unseen data distributions with additional finetuning. As with all neural architectures, finetuning such models comes with the risk of catastrophic forgetting, whereby adapting to new tasks degrades prior knowledge of the model. We study catastrophic forgetting in Walrus-1.3B, a SciFM for continuum dynamics, over the course of a two-stage sim-to-real adaptation: first finetuning on simulated flow around a cylinder and then adapting to experimental data of the same system. We find that finetuning on the simulations rapidly degrades rollout performance on the original pretraining datasets, with one-step errors increasing up to 35x after just 20 epochs. Subsequent adaptation to real data further erodes performance on the simulated task. We characterize the potential drivers of forgetting, such as dataset dependence and task representation similarity. We then show that replaying as little as 1% simulated data during real-data finetuning recovers most of the lost simulation performance while retaining effective adaptation to the experimental dynamics. Our results identify catastrophic forgetting as a practical obstacle to sim-to-real adaptation of SciFMs and show that lightweight replay strategies significantly improve retention.

---


### 177. [Sparse Autoencoders for Expert-Assisted Interpretation of Histopathology Foundation Model Embeddings](https://arxiv.org/abs/2610.40905)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Šimon Šmída, Wanda Benesova  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Histopathology foundation models learn rich embedding representations, but their internal structure remains difficult to inspect. Concept-level interpretability is particularly relevant in computational pathology because pathologists reason through recurring morphological and tissue-level patterns, including tissue architecture, cellular morphology, staining variation, and artifacts. In this work, we investigate whether sparse autoencoders (SAEs) can decompose embeddings from histopathology foundation models into sparse latent features suitable for expert-assisted interpretation. We train vanilla and Batch-TopK SAE variants on NCT-CRC embeddings, using CONCH as the primary foundation model and UNI2-h as an additional robustness evaluation, and characterize the resulting latent features through reconstruction fidelity, sparsity, coherence, label enrichment, and downstream class-signal preservation. The learned sparse representations preserve most downstream tissue-class information, and their latent features retrieve more coherent and label-concentrated patch groups than raw embedding dimensions or PCA components. Discussions with pathology experts further motivated a WSI-level latent visualization workflow that places feature activations into larger tissue context. Overall, the additional UNI2-h evaluation suggests that the observed behavior is not specific to CONCH, supporting the use of sparse autoencoders for expert-assisted analysis of histopathology foundation-model embeddings, while emphasizing that latent features should be treated as candidate concepts requiring pathological assessment rather than automatically validated histopathological concepts.

---


### 178. [Towards Portable Specification of the Agent Harness](https://arxiv.org/abs/2610.40917)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nicolas Gertler, Claudio Novelli, Luciano Floridi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models act only through the infrastructure that surrounds them. That infrastructure, the harness, determines what a model can accomplish and how it fails, yet it has no settled definition. To address this gap, we decompose the harness into eight functional components that can be specified and compared across systems, and we propose a portable specification framework that records which model ran in which harness. The record is needed because different harness configurations can yield several-fold differences in reported scores for the same model, and because much of an agent's attack surface lies in its harness. Existing model cards and agent cards provide release and operational information, but do not establish the sequence of effective configurations within a run. Harnesses can change between releases and between runs, and, where agents edit their own tools and configuration, within a run. Enacted AI laws contain documentation duties relevant to covered systems, subject to their respective scopes and application dates, but do not prescribe the common harness record proposed here. Therefore, the harness has to be explicitly described and specified as a versioned part of the system.

---


### 179. [A Theoretical Framework for Understanding and Building "Any-task inference" Capable Foundation Models](https://arxiv.org/abs/2610.40934)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Matthew McDermott, Florent Pollet, Payal Chandak 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we provide a formal framework and mathematical definition for the subset of foundation models focused on enabling the property of "any-task inference" (ATI) (similar to zero-shot inference), rather than those designed for pre-training fine-tuning. To achieve this mathematical definition, we formalize the notion of a "space of tasks of interest," which we include in the problem domain, then provide an interface-based formal definition for ATI foundation models as those that map samples of data $x$ and tasks $t$ to predictions over the space of labels directly. While simple, this definition allows us to show that all ATI foundation models can be decomposed through a "universal task reduction" lens into encoder, model, and decoder aspects. We can leverage this decomposition to also decompose foundation model error into terms corresponding to different aspects of this reduction, stratified into a collection of "design terms," which are theoretical properties that can inform one of whether a particular proposed ATI foundation model can achieve optimality or not due to the structure of the proposed task reduction, and "realized model excess" terms which capture interactions between learned and programmatic components of foundation model systems. Lastly, we can use this perspective to offer two "prototypical" recipes for realizing ATI foundation models in diverse domains, which we term generative and discriminative variants of ATI foundation models. This exercise is grounded throughout by 5 real-world examples of foundation models in different settings, varying greatly in how these capabilities are realized, showing the applicability of this definition to real-world settings.

---


### 180. [CAMEL: Cross-Architecture Masked Embedding Learning for Ultra-Lightweight Retinal Foundation Models](https://arxiv.org/abs/2610.40954)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Andre Guarnier De Mitri, Giovani Decico Lucafo, Miller Matheus Lima Anacleto Rocha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in deep learning has substantially advanced automated grading of ophthalmologic pathologies, supported by large annotated datasets and improved representation learning. However, a significant gap remains between state-of-the-art performance and clinical scalability. In particular, foundation models have reshaped image-based medical screening and diagnosis. These large-scale architectures trained on extensive datasets learn rich, generalizable feature representations that can be adapted to a wide range of downstream tasks. In ophthalmology, RETFound, one of the most relevant foundation models for retinal images, performs strongly across classification, segmentation, and risk prediction tasks. Despite their effectiveness, foundation models are often computationally prohibitive, hindering their deployment in real-world clinical environments where hardware constraints and latency are critical. To bridge this gap, we introduce CAMEL (Cross-Architecture Masked Embedding Learning), a novel cross-architecture distillation framework that uses an asymmetric masking strategy during embedding learning to effectively transfer knowledge from massive teacher foundation models to compact, lightweight student models. Our experimental evaluation across four datasets shows that CAMEL preserves accuracy while drastically reducing computational complexity, enabling lightweight yet highly accurate models suitable for resource-limited clinical settings.

---


### 181. [QUAL: Quantile Alignment Improves Zero-Shot Time-Series Foundation Models](https://arxiv.org/abs/2610.41100)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junhyeok Kang, Sangjun Han, Jun Seo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models (TSFMs) provide zero-shot forecasts for unseen series, but their accuracy varies across datasets. Combining several models can reduce this variability, yet zero-shot deployment provides no target labels for selecting or weighting them. We find that a model pool is useful not only as a final ensemble, but also as a probability reference for transforming each member forecast. Aligning quantiles through this pool-relative reference improves every member forecast in aggregate. Motivated by this finding, we propose QUAL (Quantile alignment), a simple label-free framework for improving and combining diverse TSFMs. QUAL first produces aligned member forecasts, then applies Huber aggregation and rearrangement to obtain a robust combined forecast without training or model modification. On GIFT-Eval, quantile alignment reduces average member MASE and CRPS by 7.4% and 9.8%. The full framework remains robust when weak forecasters enter a candidate pool whose quality cannot be verified in advance. Code is available at this https URL.

---


### 182. [PP-Mark: Provable and Publicly Verifiable Watermarking for Generative AI](https://arxiv.org/abs/2610.41170)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hankyeong Ko, Taehoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative AI models now produce images indistinguishable from real data, making publicly verifiable provenance essential; however, existing watermarking methods become vulnerable to forgeries and adversarial optimization attacks once their detectors are made public. We propose PP-Mark, a provenance framework that anchors lightweight statistical detection to a zero-knowledge proof of the embedding process, ensuring that forged content cannot pass full verification by construction. We establish formal unforgeability under standard cryptographic assumptions and validate PP-Mark against representative baselines across two latent-diffusion models (SD2.1 and SDXL), demonstrating resistance to black-box imprint forgery, white-box optimization, and regeneration attacks while remaining practical for decentralized verification. Code is available at this https URL

---


### 183. [scAnyOmics: Foundation-Model Distillation for Any-to-Any Completion of Multi-omics Virtual Cells](https://arxiv.org/abs/2610.41399)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhaoqi Song, Ye Du, Yusuke Iwasawa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in single-cell technologies have enabled the profiling of multiple molecular modalities, including transcriptomics, proteomics, and chromatin accessibility, providing a more comprehensive understanding of cellular states. However, integrating heterogeneous modalities and predicting missing molecular information remain challenging, particularly when paired measurements are limited. Here, we introduce scAnyOmics, a generative framework that distills knowledge from a frozen single-cell foundation model into a multimodal student model. scAnyOmics integrates scRNA-seq, protein-marker measurements, and scATAC-seq into a shared representation, enabling cross-modal prediction and reconstruction of missing modalities. We assembled 690,880 cells from six publicly available studies, covering both paired and partially paired multi-omics measurements, to systematically evaluate its predictive performance. We further evaluated scAnyOmics on held-out donor data, where it outperformed baseline methods across multiple evaluation metrics. Beyond cross-modal reconstruction, we explored its applications in cell-type annotation, perturbation-response prediction, and biological age estimation. Overall, scAnyOmics provides a unified framework for integrating incomplete single-cell multi-omics data and transferring pretrained biological knowledge, supporting the development of virtual cell models across diverse cellular contexts and experimental platforms.

---


### 184. [Dynamical Memory Transformer: Selective Recurrent Memories with Constant Cost Attention](https://arxiv.org/abs/2610.41850)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yannis Bendi-Ouis, Xavier Hinaut  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformers retain an explicit history of the sequence, allowing attention to directly retrieve past representations. However, the size of the KV-Cache and the cost of a new token increase with the context length. State Space Models compress the past into a fixed-size recurrent state, at the cost of reduced addressability. We present the Dynamical Memory Transformer (DMT), a hybrid architecture that separates sequence encoding from information reading. The encoder uses several memory units, each implemented by a dynamical system with a complex diagonal recurrent matrix. An input-dependent leak rate controls their updates. The decoder then uses attention to read and combine their outputs, without going through the token history. The formulation of the recurrence allows an associative scan with O(T ) total work and O(log T ) parallel depth, with fixed dimensions. During autoregressive inference, the recurrent states and the convolution cache remain fixed in size. We compare DMT with Mamba and Transformer on cognitive and language modeling tasks, and show its strengths and limitations: DMT achieves the best results on several cognitive tasks and language modeling performance close to that of Transformer, but remains behind Mamba in language modeling. On selective copy, DMT also shows stronger length extrapolation than Mamba and Transformer. These results demonstrate that parallel dynamical memory units are a promising mechanism for retaining and using information over sequences.

---


### 185. [Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning](https://arxiv.org/abs/2610.41949)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhuguanyu Wu, Congjia Chen, Ruihao Gong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Few-step flow models generate samples through a handful of large denoising transitions. Applying GRPO to such models requires introducing stochasticity into the denoising transitions, and when a single transition spans a wide range of noise levels, the choice of the resulting stochastic policy becomes a major factor in optimization. Recent constructions constrain the policy to preserve the target flow coefficients, but this constraint admits a family of policies and offers no criterion for choosing among them. We introduce Geo-FSRL (Geometry-Optimized Few-Step Reinforcement Learning), built on a selection principle: at a fixed conditioning state and timestep pair, choose the admissible policy that minimizes the conditional KL divergence induced by any given nonzero velocity-output update. Within a coefficient-preserving family of isotropic Gaussian transitions, this criterion reduces to minimizing a single scalar geometry factor that determines the conditional KL for every velocity-output update. The same factor governs velocity-space Fisher information and conditional transition log-likelihood-ratio variance. We derive the unique closed-form optimizer within this family, shared across all nonzero update magnitudes and directions, with transition coefficients determined by both the source and target noise levels. Because the minimized geometry factor still varies across timesteps, we further adopt gradient-scale matching from prior work and derive closed-form policy-gradient and KL weights that normalize explicit score scales and reference-KL curvature. Geo-FSRL trains on the original few-step schedule and retains the deterministic solver at inference. Our method achieves higher final reward scores than Flow-GRPO and Flow-CPS on both image generation and video generation models under the 4-step setting. Code is available at this https URL

---


### 186. [Chronos-2: A foundation model for multivariate time series forecasting](https://arxiv.org/abs/2610.41956)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting with uncertainty quantification is critical in a variety of scientific applications ranging from epidemiology and economics to energy systems and earth sciences. Yet most forecasting models still need to be developed and trained separately for each domain-specific dataset. Time series foundation models (TSFMs) aim to remove this limitation and enable the application of the same model across domains through large-scale pretraining. However, most existing TSFMs treat each time series independently and therefore cannot model interactions among time series and external drivers. Here, we introduce Chronos-2, a foundation model for zero-shot forecasting that models the interactions between multivariate time series and heterogeneous covariates, which commonly arise in scientific applications. The model infers relationships among time series directly from historical context and generates probabilistic forecasts without task-specific treatment. Across various benchmarks, Chronos-2 achieves state-of-the-art accuracy on average by improving skill scores by 5.2 percentage points relative to the strongest baselines and increasing win rates by 10 percentage points. Chronos-2 is also computationally efficient, generating forecasts for 100 time series in under one second on a single mid-range GPU, 50x and 1000x faster end-to-end than the best task-specific point and probabilistic forecasters, respectively. In addition, we demonstrate its effectiveness in diverse scientific settings -- including infectious-disease forecasting, macroeconomic modeling, carbon-flux prediction, and runoff simulation -- where the model matches or surpasses specialized methods developed for each domain. These results show that a single pretrained model can capture structure shared across temporal systems.

---


### 187. [When Does Test-Time Search Help World Action Models? An Empirical Audit of Candidate Selection and Simulator Integrity](https://arxiv.org/abs/2610.41970)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jun Liu, Dajie Sun, Zhenglun Kong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World-action models increasingly apply test-time scaling, spending extra inference computation on candidate selection and adaptive allocation to improve control. Such gains are credible only when candidates carry exploitable signal, nominal compute savings become real speedup, and evaluation stays reliable. We audit all three on Cosmos Policy and RoboCasa with a premise-first, pre-registered methodology. On clean data, a learned value selector is 1.66 pp worse than random; a hindsight oracle gains only 1.40 pp, with an episode-level interval spanning zero; and 82% of states show identical candidate outcomes, leaving little selection headroom. Token pruning cuts per-forward FLOPs by up to 47% but yields at most a measured 1.15$\times$ end-to-end speedup on the deployed path (1.25$\times$ on a decode-excluded path), short of a 1.5$\times$ target, and our adaptive-allocation experiment is inconclusive under a power gate. We further identify and fix a silent rendering corruption whose rate rises sharply along compute-heavy planning paths while leaving the official direct-policy result unaffected, and release a detector, fix, and scripts. These findings show why test-time scaling should be audited as a chain of premises (decision signal, realized efficiency, evaluationintegrity) rather than by success rate alone. Conclusions are scoped to the tested configuration.

---


### 188. [ID2Pattern: Pretraining Generalizable Identity Behavior Patterns for Transaction Risk Foundation Models](https://arxiv.org/abs/2610.41988)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ze Zhao, Haoyu Jiang, Weiyu Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale behavioral pretraining offers a promising route to generalizable representations in online payment systems. However, high-cardinality identity fields such as card, device, and account IDs, though rich in behavioral signals, remain underexploited. Their continually growing vocabularies and limited semantic meaning make existing vocabulary-based and semantics-based encodings ill-suited. Their generalizable signal lies not in specific values, but in the identity behavior patterns they exhibit across a transaction sequence. Building on this insight, we propose ID2Pattern, a pretraining framework that brings these patterns into transaction foundation models. ID2Pattern first encodes identity fields with a Local Anonymous ID (LAID) tokenizer, which captures how each identity appears and recurs within the sequence, independent of its specific value. It then pretrains a multi-scale pattern codebook on unlabeled sequences, which abstracts LAID sequences into discrete behavior patterns for downstream prediction. Experiments on an industrial dataset with over 100M sequences and six public datasets show that ID2Pattern consistently outperforms strong baselines, improving industrial by 4.13% and public datasets by 8.83% on average. Notably, ID2Pattern remains equally effective even when all identity values are unseen during training, highlighting its potential to generalize to new users and markets.

---


> [!TIP]
> 当前位于：**151-188**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-188**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
