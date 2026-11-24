# 🧠 大模型相关研究 | 2026年11月25日

> 本类共 **486** 篇论文：已确认 **458** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-486](./part-10.md)

---

### 251. [Which Loopholes Get Found? Predicting Reward Hacking of LLM Judges Before RL Training](https://arxiv.org/abs/2611.29651)

**<font color=#1a73e8>作者：</font>** Xuanyi Lyu, Yuezhou Zhao, Qing Qin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A policy trained against an LLM judge can learn to exploit its loopholes. Static probes show that such judges accept degenerate answers like a lone "{" or "Thought process:", but not which flaw a policy will find. In GRPO the first loophole to be exploited can be predicted before training from each pattern's exposure, the product of the starting policy's propensity to produce it and the judge's false-positive rate (FPR). To test exposure causally, we seed the patterns into fine-tuning at three doses in a Latin square. Across 36 GRPO runs with seven judges, the first exploited pattern had the highest exposure in all 12 runs with exploitation and the highest FPR in only 6. Predictions recorded before training held in three of four runs with one pattern masked by rule. When only two patterns were seeded, at 3% to 3.8% of the fine-tuning data and chosen so that exposure disagreed with FPR alone or propensity alone, exposure named the first exploited pattern and its onset window in all six runs. Exploitation occurred only on hard prompts, where an accepted exploit gets a large group-normalized advantage. Auditing exposure before RL therefore identifies the loophole a policy will likely exploit first.

---


### 252. [How Reliable is AI-Generated Audio Description? A Multilingual Expert Evaluation](https://arxiv.org/abs/2611.29658)

**<font color=#1a73e8>作者：</font>** Annette Rios, Lukas Fischer, Sarah Ebling  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio description (AD) makes visual media, such as video, accessible to blind or low-vision (BLV) audiences, but the high cost of professional production limits coverage. Due to recent advances in AI, numerous approaches to automatically generate intermediate AD scripts and/or final AD audios have been proposed. We present an expert evaluation of AI-generated AD scripts for movies in Italian and German that compares two AI systems, a GPT-4o- and a Qwen-based pipeline, against human-authored descriptions. Professional audio describers rated description quality and annotated errors using a detailed error taxonomy that includes content, character, fluency and coherence errors. The results show that while GPT-4o outperforms the Qwen models, both AI systems still fall short of human professional quality: the generated descriptions show substantially higher error rates and lower quality ratings. Based on the error annotations, we identify two key areas that require improvement: 1) character references, which includes both issues with identification and coherent naming, and 2) content errors and hallucinations, where the AD misrepresents or invents events. These error types are particularly critical, as they directly affect the viewer's ability to follow the narrative.

---


### 253. [Exact on Paper: Which LLM Serving Shortcuts Flip Graded Answers, Measured Against the Noise of Reordering the Same Requests](https://arxiv.org/abs/2611.29663)

**<font color=#1a73e8>作者：</font>** Sharven Rane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Teams enable serving features such as prefix caching, chunked prefill and speculative decoding after checking that benchmark accuracy is unchanged, because the engine documents them as exact. Accuracy is an aggregate, so a feature can hold it while flipping which requests are answered correctly. We serve one 4B instruction model in vLLM under nine single feature configurations and five replicas of a reference configuration, grade 3,380 requests from five benchmarks in every run, and compare each candidate with a restart floor (fresh process) and a scheduling floor (same requests in a different order). With default kernels every configuration keeps accuracy within one point, and the seven exact features flip the graded outcome of 1.47% (95% CI 1.13 to 1.85) to 1.78% (1.39 to 2.20) of requests, none above the scheduling floor of 1.72%, while the FP8 KV cache flips 3.36% (2.80 to 3.96), as many as FP8 weights. With batch invariant kernels all seven exact features, speculative decoding included, reproduce the reference text on every request, while the FP8 KV cache still flips 3.91% (3.28 to 4.53) of graded outcomes. A gate that compares against a single replica pair rejected an unchanged configuration, so we recommend certifying a serving change under batch invariant kernels, where the floor is zero, or against a scheduling floor measured from at least three replicas.

---


### 254. [Position-Skipped Distillation of Sparse-Attention Indexers: Train Short, Serve Long](https://arxiv.org/abs/2611.29664)

**<font color=#1a73e8>作者：</font>** Fu Dai, Haodi Quan, Kamal Taha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Top-k sparse attention relies on an indexer, a lightweight per-layer module that ranks cached tokens so attention covers only the k highest-scoring ones. Indexers are usually distilled from dense attention at the full serving length, so every training step pays for long-context dense attention. We show that when an indexer is distilled on short sequences, its failure to generalise to longer contexts is driven mainly by rotary positional encoding (RoPE), not by degraded content matching. We propose position-skipped distillation: the indexer and the frozen teacher see short sequences whose position IDs contain a randomly placed gap, so neither ever processes more than the short training length. On DeepSeek-V2-Lite and Qwen3-30B-A3B, an indexer distilled on 8K tokens this way matches a 32K-distilled indexer to within about 0.5 perplexity up to 32K, and on DeepSeek-V2-Lite matches a 64K-distilled indexer at 64K with roughly 6x less training compute per token. On Llama-3.1-8B it trails the stronger 32K run by 0.6 perplexity, and at 64K simple position compression is often as good, so the main gain is training cost rather than quality. We also quantise indexer keys to 3-4 bits without retraining and score them with a fused integer kernel: at 4 bits, perplexity changes by at most 0.05 and the scan is 1.6-2.2x faster than half precision. In a current serving engine, the indexer speeds up decoding only for long contexts with multiple concurrent streams.

---


### 255. [But Can You Draw It Live? The Emergence of AI Duidus for Adjudicating Suspected Generative AI Use in Digital Art Commission Communities](https://arxiv.org/abs/2611.29684)

**<font color=#1a73e8>作者：</font>** Elise Chenxinran Shen, Dashiel Carrera, Michelle Annett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI poses new challenges for digital art commission communities, where a commission's value often depends on human labor and authorship. We examine a novel community-developed dispute resolution mechanism called an AI duidu, or livestreamed drawing bet, used when an artist is suspected of using generative AI. In an AI duidu, an accuser challenges an artist to create a new artwork live, and community members vote on whether the artist created the disputed artwork without AI assistance. Often, both parties stake money with an intermediary, who releases it after the vote. Through interviews with 17 accusers, accused artists, or intermediaries, we examined how the AI duidu emerged and how participants perceived its effectiveness and risks. We found that AI duidus shift authorship verification from the artwork itself to the artist, using livestreamed creative labor, community adjudication, and wagering to establish provenance and negotiate community norms surrounding AI use.

---


### 256. [Do More Roles or Larger Models Improve LLM Fact-Checking? A Controlled Study on Fixed Evidence](https://arxiv.org/abs/2611.29687)

**<font color=#1a73e8>作者：</font>** Martin Pavlíček, Martin Kotyrba, Eva Volná 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A fact-checking system can spend more computation on a claim by using a larger model, by asking the same model several times, or by a multi-role Tribunal: two roles propose quoted findings, code checks the quotations, an auditor that does not see the proposed relation judges each one, and code derives the verdict or abstains. We compare these options on identical fixed evidence, without retrieval: 300 AVeriTeC claims, each with its annotated question--answer items mixed with items written for other claims, read by judges of four open-weights models from three families, a vote of five, and six assignments of models to the Tribunal's roles. The 9B judge was right on 186 claims and the 27B judge of the same family on 156; the larger judges declined to decide far more often and were no more accurate when they decided. The vote reached 196 and the 9B judge with its verdict replaced by Tribunal certificates 195, at a similar cost; the Tribunal alone reached 153 to 164, because it abstained on almost half of the claims. A hearing's outcome followed the auditor's model and was nearly indifferent to the proposers'. A larger auditor, or one of another family, made certificates neither more often correct (77% to 81%) nor more independent of the judge. As a replacement, certificates improved every judge by 3 to 10 points and overturned four to five in a hundred of its correct verdicts. With the annotated evidence withheld, judges and Tribunal still decided on 7% to 14% of the claims.

---


### 257. [Grammar Sparsity Sets How Transformers Learn Random Languages](https://arxiv.org/abs/2611.29692)

**<font color=#1a73e8>作者：</font>** Edgar Andres Hernandez Moreno, Francesco Cagnetta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study language acquisition by transformers trained on the Random Language Model: a synthetic hierarchical grammar with random production rules, whose sparsity is controlled by a single parameter and whose conditional entropies are known exactly. On depth-two grammars, we find that sparsity sets both the order and the speed of learning. Dense grammars are learnt one level at a time: a token is predicted from its sibling after $t\propto V$ steps and from the full context only after $t\propto V^{3}$, so the two stages are separated by a plateau that widens with $V$. Sparse grammars are learnt all at once, at $t\propto\sqrt V$, with a smaller exponent than even the first stage of a dense one. The exponents $1$ and $1/2$ already appear at depth one, where we derive them for a linear model trained with Adam.

---


### 258. [HandiVid: A High-Quality Dataset for Hand-Driven Interactive Video Generation](https://arxiv.org/abs/2611.29693)

**<font color=#1a73e8>作者：</font>** Chaoyang Zhang, Shaohao Rui, Xiaofeng Mao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hand-driven egocentric interactive video generation aims to generate dynamic scenes with realistic interaction responses conditioned on hand movements and camera motion. However, existing egocentric video datasets struggle to provide scene diversity, meaningful hand-object interactions, and reliable motion annotations simultaneously. To address these limitations, we introduce HandiVid, a high-quality dataset comprising 200K curated and annotated egocentric interaction video clips for hand-driven interactive video generation. We develop a unified data processing pipeline that integrates public datasets, online videos and synthetic videos. Through video quality assessment, hand detection filtering, and multi-stage interaction validation using vision-language models (VLMs), we select high-quality video clips with meaningful hand-object interactions. Since 3D hand reconstruction relies on initial hand detections, we integrate SAM 3 into the hand detection pipeline to reduce missed detections and improve the completeness of 3D hand annotations. Each video clip is provided with high-quality hand renderings, camera trajectories, and interaction descriptions. Comprehensive dataset analysis and downstream video generation experiments demonstrate the effectiveness of HandiVid in terms of data diversity, annotation quality, and controllable video generation.

---


### 259. [Fin-RSI: A Unified Library of Financial Skills, Checks, and Self-Improvement for LLM Agents](https://arxiv.org/abs/2611.29716)

**<font color=#1a73e8>作者：</font>** Wanghao Ye, Shwai He, Sihan Chen 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) become more capable, financial agents need tools they can readily discover and use. Yet financial software is fragmented across libraries with different interfaces and conventions, making it difficult to build reliable agent workflows. We present Fin-RSI, a unified Python library of financial skills, checks, and self-improvement designed for LLM agents. It brings together tools for market analysis, forecasting, portfolio construction, and trading research through shared interfaces across models and agent frameworks. Agents can find suitable tools from natural-language requests, reuse tested implementations, and improve generated programs through checking and feedback. Developers can extend the library with new tools without rebuilding integrations for each model. Across 20 open-weight models on six trading-position tasks, tool discovery increased the proportion of episodes producing valid programs from 9.7% to 29.2%; for models with at least 14 billion parameters, it rose from 23.6% to 64.6%. We release the library and benchmark as a shared resource for the community and plan to expand its tools and task coverage as financial agents evolve.

---


### 260. [LAF-ECG: Multi-Resolution Lead-Aware Fusion of Time-Series and Language Foundation Models for ECG Classification](https://arxiv.org/abs/2611.29721)

**<font color=#1a73e8>作者：</font>** Kiana Taktehrani, Maryam Hosseini, Amir Keynia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated electrocardiogram (ECG) interpretation has advanced substantially with deep learning, yet many methods remain task-specific and label-dependent. Large language models (LLMs) and time-series foundation models (TSFMs) offer complementary pretrained representations, but integrating them is challenging because of mismatched feature spaces and the lead- and scale-dependent structure of ECG signals. We propose LAF-ECG (Lead-Aware Foundation Fusion for ECG), a dual-foundation framework that extends MedTsLLM with a lead-aware interface to a frozen TSFM backbone while retaining its reprogramming pathway. The proposed framework captures multi-resolution temporal context, fuses temporal and language-aligned ECG representations through adaptive residual integration, and employs branch-specific supervision with cross-branch alignment. LAF-ECG achieves 71.10% accuracy and 62.43% macro-F1 on PTB-XL, and 89.73% accuracy and 65.94% macro-F1 on Chapman-Shaoxing, outperforming MedTsLLM on both datasets. These results highlight the value of preserving lead-specific temporal structure when combining temporal and language foundation representations for ECG classification. The code is publicly available at this https URL.

---


### 261. [Reasoning Beyond Imitation: Observation Conditioned Distillation for Video LLMs](https://arxiv.org/abs/2611.29728)

**<font color=#1a73e8>作者：</font>** Junzhou Chen, Jindong Wang, Gang Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning distillation offers a promising approach to transfer temporal reasoning capabilities of powerful Video-LLMs to open-source student models. However, teacher and student Video-LLMs may construct different temporal observations from the same video due to the adoption of distinct video sampling pipelines. A reasoning trajectory valid under the teacher's observations may rely on evidence inaccessible to the student and thus cannot be directly executed based on the student's observations. We formalize this as a conditional target mismatch, thereby revealing the Reasoning Acquisition-Execution Gap. To bridge this gap, we propose an acquisition-to-execution framework that first distills teacher trajectories into a student reasoning prior and then further optimizes the execution capability of this prior across multiple observations. We further introduce Execution-Aware Reference Regularization, which retains the existing prior when it is executable under current observations, while allowing a greater degree of adaptive adjustment when it is not. Experiments across multiple Video-LLM backbones and six video reasoning benchmarks show that explicitly optimizing observation-conditioned execution consistently outperforms supervised distillation and standard RL-based optimization, with gains extending to held-out out-of-domain benchmarks.

---


### 262. [Reinforcement Learning from LLM-Generated (Suboptimal) Demonstrations](https://arxiv.org/abs/2611.29732)

**<font color=#1a73e8>作者：</font>** Anurag Kadkol, Lawson L.S. Wong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has achieved substantial progress across many domains, but training an agent \textit{tabula rasa} remains highly sample-inefficient. A common remedy is to initialize the agent using a neural network pretrained on demonstrations. However, collecting demonstrations is expensive, and the demonstrations themselves can be suboptimal. In this work, we use a large language model (LLM) to generate an advice policy that produces demonstration data with effectively no human cost. We use this data to warmstart a DQN agent, and use the advice policy itself to guide exploration during training. Because LLM-generated advice is often suboptimal, we further introduce a value warmstart method that initializes the agent to recognize promising states from the advice policy's behavior, without directly copying its actions. To characterize the robustness of this method, we systematically perturb individual sub-skills of an LLM-generated advice policy for a long-horizon, sparse-reward task. Degraded advice still meaningfully accelerates learning relative to unaided baselines. These results suggest that LLM-generated advice, though suboptimal, can be a cheap alternative to costly human demonstrations.

---


### 263. [Why Units Die in the Layer After a Frozen Random Encoder, and What the Number of Live Units Measures](https://arxiv.org/abs/2611.29752)

**<font color=#1a73e8>作者：</font>** Scott M. Norton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement-learning agents can learn Atari games through a convolutional encoder whose random weights are never trained. They reach expert play in Pong and, without random action repeats, in Breakout, but training takes far longer and few ReLU units in the layer after the encoder stay alive. A dead unit outputs zero for every input and cannot learn. In earlier work we took the number of live units to measure the game's complexity. Here we ask why units die and correct that conclusion. We find that more units die as the layer's inputs lie farther from zero relative to how much they vary. We call this ratio the offset. Earlier work showed this in sparse autoencoders at the start of training. We saw it after training in agents, image classifiers, a reservoir computer and sparse autoencoders on GPT-2. A random encoder leaves the offset of its input roughly unchanged, and a formula predicted its median offset within 25 percent in all 44 cases. So a game with a bright, mostly unchanging screen gives the next layer a large offset. In Pong, subtracting the average screen raised the number of live units from between 3 and 6 of 64 to between 59 and 63, so the number alone cannot show a game's complexity. On unaltered screens none of the agents reached a training score of 18 in 50 million steps. With the subtraction all did within 5 million, about as fast as a trained encoder on unaltered screens. In Breakout the subtraction left more units alive, but average training scores did not clearly improve, and a large gap to a trained encoder remained. So we do not treat their number as something to raise for its own sake. The evidence is from small networks and three games, and in agents and image classifiers changing the offset also changed the size of the inputs. We suggest measuring the offset before training a layer on a fixed front end and, if it is large, trying to subtract the mean input.

---


### 264. [DictaRashi: A State-of-the-Art OCR Model For Rashi Script](https://arxiv.org/abs/2611.29760)

**<font color=#1a73e8>作者：</font>** Ometz Shmidman, Yonah Taurog, Aryeh Sanders 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We release DictaRashi, a Tesseract OCR model for scanned Hebrew books printed in the so-called "Rashi" font. We trained DictaRashi on over one million manually corrected lines of text from over 100 different books of Rabbinic and post-Rabbinic literature. On a held-out set of 1,120 manually transcribed lines from scanned Rashi-script pages, DictaRashi reaches a character error rate (CER) of 0.86% and a word error rate (WER) of 3.38%, setting a new state-of-the-art for publicly-available Tesseract models. We provide a full comparison of our results to those of the 31 other publicly available Hebrew Tesseract models; the best of those models achieves a 2.98% CER and 11.86% WER. We further demonstrate that DictaRashi outperforms the current frontier LLMs on this OCR task. We release the test set of Rashi-script documents so that it may be used as a benchmark for future work in this area. We are pleased to release the model and test set to the community under a CC BY NC 4.0 license.

---


### 265. [probly: Uncertainty-Aware Machine Learning](https://arxiv.org/abs/2611.29762)

**<font color=#1a73e8>作者：</font>** Paul Hofman, Clemens Damke, Timo Löhr 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As machine learning systems are increasingly deployed in real-world applications, the question of how to represent and quantify uncertainty has moved from a methodological side issue to a central concern. In practice, however, making a model uncertainty-aware is still surprisingly difficult: relevant tools tend to be scattered across libraries, each tied to a particular framework and a particular approach to modeling uncertainty, and the choice of representation, quantification, and evaluation is typically left to the user without much guidance. In this paper, we present probly, a Python package that addresses these issues in a single, modular framework. probly offers (i) lightweight transformations that turn existing models into uncertainty-aware ones, currently supporting PyTorch, scikit-learn, and Flax, (ii) several representations, including second-order distributions, credal sets, and conformal prediction, (iii) the corresponding quantification measures, and (iv) a number of evaluation protocols, which can be combined more or less arbitrarily. Using probly, we conduct a benchmark study on three standard tasks --- selective prediction, out-of-distribution detection, and active learning. In addition, and unlike existing benchmarks, we evaluate suitable methods on first-order data, i.e., datasets for which the target itself is a distribution over outcomes. We further illustrate the flexibility of the package on a number of less standard case studies, including large language models, graph neural networks, and data streams. The package is publicly available at this https URL.

---


### 266. [Sánchez, Feijóo, or Abascal? Speaker Attribution and Ideological Congruence in LLM Personas Reading Posts on X of the Leaders of the Three Main Parties of the 29N General Election in Spain](https://arxiv.org/abs/2611.29765)

**<font color=#1a73e8>作者：</font>** Víctor Yeste, Candida Maria Greco, Paolo Rosso 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Source cues are central to political communication, yet reception studies with large language model (LLM) personas as synthetic audiences have not tested whether personas respond to who speaks and not only to what is said. With Spain's general election of 29 November 2026 in mind, we run a speaker-attribution experiment using 1,075 anonymised X posts by the leaders of PSOE, PP and VOX on four topics (the economy and employment, household costs, immigration and corruption) and 791 distinct value-grounded, LLM-generated personas. Each post was assigned to 300 topic-selected persona profiles, 150 grounded in the Inglehart-Welzel cultural map and 150 in Moral Foundations Theory, under four conditions: no author, Sánchez, Feijóo or Abascal, yielding 322,470 complete persona-post quartets. Naming any leader lowered support for identical text, with the penalty for Abascal nearly twice as large as those for Sánchez and Feijóo. The penalty follows the persona's elicited left-right self-placement (ideological congruence): left personas spare Sánchez and right personas spare Feijóo, although ideology was never in the message-evaluation prompt. Corruption posts were penalised under every name, whereas on other topics the ideologically closest leader generally produced little or no penalty. The leader order matches public opinion in 48 CIS barometers (2022-2026) in all three groups and the sign of all twelve differences, but fits barometers before the model's 2024 knowledge cutoff better than recent ones. Our findings demonstrate that LLM personas evaluate political speakers through systematic, value-congruent priors: however, while they replicate human candidate rank-orders across survey barometers, this alignment is ordinal rather than quantitative, highlighting their utility for controlled source-effect experiments though not as substitutes for empirical public opinion surveys.

---


### 267. [S1Arena-MM: Which Multimodal Decisions Can Be Left to System 1?](https://arxiv.org/abs/2611.29773)

**<font color=#1a73e8>作者：</font>** Lang Lin, Tianyu Chen, Yi Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perception systems often make discrete decisions: flag a hateful meme, predict whether a pedestrian will cross, detect a spoofed voice, or select the next move in a game. System-1 models, such as OneJev and Jev-Omni, read the media and return probabilities over the options in a single forward pass, while multimodal large language models (MLLMs) generate text. Which multimodal decisions can System-1 models handle, and where do MLLMs perform better? We introduce S1Arena-MM, a benchmark that gives every model the same decision requests and scores the probabilities it returns. It contains 51,060 questions across 94 tasks with image, video, and audio input, drawn from 94 public datasets and three program-generated ones. It also includes 102 closed-loop game environments that a model plays from screenshots; in real-time mode, the game continues while the model decides. We evaluate 33 open models: 12 System-1 models and 21 MLLMs read at the answer token. On static decisions, the best System-1 model leads the best MLLM by 4.9 percentage points on images and is within one point of it on video and audio. Post-training for decisions mainly improves the probabilities: on video, a System-1 model has a lower Brier score than the MLLM that it is post-trained from in 10 of 12 pairs. With up to 2,048 thought tokens per question, the most accurate MLLMs pass the best System-1 models only slightly, and thinking raises the Brier score of most MLLMs. Closed loops separate the models: three System-1 models built on a 27B MLLM reach 22.0-33.3% progression in BALROG, and no other model exceeds 9.7% with thinking off. In real-time GameWorld, latencies of up to 1.1 s per decision cause no measurable loss of progress for System-1 models. Code and data: this https URL.

---


### 268. [ComplexIF: A Challenging Multi-Turn, Multi-Constraint Instruction-Following Benchmark](https://arxiv.org/abs/2611.29775)

**<font color=#1a73e8>作者：</font>** Zhichao Xu, Bingsen Chen, Yawei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As frontier LLMs saturate existing instruction-following benchmarks, measuring further progress requires harder tests that remain faithful to real use. In practice, users often combine several constraints, add them at different turns of a conversation, and expect all of them to hold in the assistant's response. We introduce ComplexIF, a challenging benchmark for this setting, together with the automatic pipeline that generates it. The pipeline expands seed requests into multi-turn conversations, weaves constraints into their turns, and keeps only tasks that a strong model can solve, so difficulty can be raised by adding constraints or turns while every task stays solvable. ComplexIF's two splits test complementary sides of instruction following: a verifiable split of format constraints, checked by programs, and a rubric split of semantic instructions, such as a tone or an audience, checked with an LLM judge. Across 14 proprietary and open-weight models, even the strongest satisfies every constraint on fewer than half of the verifiable tasks, and no model leads on both splits.

---


### 269. [Beyond Language Optimization: Enhancing Visual Representations for Radiology Report Generation](https://arxiv.org/abs/2611.29783)

**<font color=#1a73e8>作者：</font>** Rui Zuo, Qinyue Tong, Ziqian Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate chest X-ray radiology report generation (RRG) requires recognizing clinically relevant abnormalities and accurately describing them. Although Group Relative Policy Optimization (GRPO) improves the clinical accuracy of generated reports, our analyses suggest limited improvements in visual representations for abnormality recognition. To address this limitation, we propose a selective regional visual distillation framework that enhances visual representations of challenging abnormalities while preserving existing visual capabilities. Specifically, we train a region-aware teacher with targeted supervision on challenging anatomical regions to acquire complementary visual knowledge. Rather than transferring all teacher features, we verify their utility through regional feature replacement and select only those that improve the original student's performance. We further introduce a Spatially Gated Residual Adapter (SGRA) to distill these verified features while minimizing interference with the student's existing visual representations. Experiments on MIMIC-CXR and IU-Xray demonstrate improved clinical report accuracy and region-level abnormality recognition across different multimodal large language model backbones, while largely preserving performance on non-target findings.

---


### 270. [Dimension Is Free, Horizon Is Not: When Evolution Strategies Rival Policy Gradients for LLM Fine-Tuning](https://arxiv.org/abs/2611.29795)

**<font color=#1a73e8>作者：</font>** Qiyao Liang, Kajetan Schweighofer, Xin Qiu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Policy gradient (PG) methods such as GRPO dominate LLM fine-tuning, yet recent work showed that Evolution Strategies (ES) also scale to fine-tuning models with billions of parameters. Which method needs fewer samples, and on which tasks, remains unclear. We view the two methods as estimators of the same gradient that differ in where they explore. Because ES perturbs parameters, its noise grows with the number of parameters, and because PG samples actions, its noise grows with the number of generated tokens. Only noise along the directions that change the reward slows learning. The cost of ES then depends on the effective dimension, the number of independent skills a task requires rather than its parameter count, while the cost of PG depends on the effective horizon, which counts only the tokens that share both credit and weights with the reward-carrying ones. We train both methods on a synthetic task where the number of skills and the effective horizon can be varied separately. PG is cheaper when the horizon is short, ES becomes cheaper once it is long enough, and this crossover moves to longer horizons as the number of skills grows. We then measure the effective horizons of 20 NLP, math reasoning, and agentic tasks and compare the two methods with Qwen2.5-7B. PG leads on short-horizon tasks, the two tie on the moderate-horizon math ones, and no task has a horizon in the regime where the theory predicts an ES advantage. Terminal-Bench has a far longer horizon. There, in a preliminary comparison with Qwen3.5-4B, ES without any credit assignment reaches a higher success rate than the PG checkpoint released with Tmax, as the theory predicts. ES should thus have the advantage on long-horizon tasks with few independent skills and a nonvanishing reward signal. Current benchmarks are only at the onset of this regime, so ES should become more competitive as agentic tasks grow longer.

---


### 271. [FORGETMENOT: Auditing Memory Driven Privacy Risks in Commercial AI Agents](https://arxiv.org/abs/2611.29804)

**<font color=#1a73e8>作者：</font>** Ismat Jarin, Tu Le, Athina Markopoulou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Commercial AI agents increasingly incorporate long-term memory (both persistent and chat-history) to enable more accurate and personalized responses, raises significant privacy and policy concerns. Yet little is known about user privacy risks associated with memory behavior, in particular, about memory storage, disclosure, transparency and deletion control. To bridge this gap, we propose FORGETMENOT, an auditing framework for analyzing the privacy risks of long term memory in commercial AI agents. Using our framework, we collect around 3800 multi-turn sessions comprising around 6M tokens across five popular AI agents. Our results show that agents store a wide range of personal attributes, including demographics, health, and sensitive details. Furthermore, user visible memory reveals substantially less (around 20% on average) attributes than the agents store in practice, exposing a significant transparency gap. Our stealth memory injection (SMI) technique further increases the amount of personal and sensitive attribute stored in memory, raising it by 25% and 15% for Copilot and Claude, respectively. We further observed memory deletion control is unreliable, as all five agents exhibit non-zero post deletion leakage, including health and self-harm related attributes. Finally, we demonstrate the feasibility of memory disclosure to a 3rd-party email recipient as a proof-of-concept, as Gemini shows 31.9% leakage rate. Together, our findings reveal notable privacy risks in commercial agents memory. Finally, we discuss both design implications and regulatory recommendations to protect users memory privacy in commercial agents.

---


### 272. [Latent-Predisposition Personas for Heterogeneous and Reliable LLM Survey Simulation](https://arxiv.org/abs/2611.29805)

**<font color=#1a73e8>作者：</font>** Geonwoo Bang, Dongho Kim, Moohong Min  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM personas are used to simulate survey publics, which should reproduce not only answer distributions but also within-person coherence and stability. Drawing on mass belief systems research, we show that persona-conditioned LLMs produce over-constrained publics. Across three model families and three U.S. surveys, opinions on unrelated issues are 1.6-4.6 times as correlated as among humans, and party identification explains 2.5-7.6 times as much answer variance. Common remedies (temperature, diversity instructions, backstories) weaken these correlations by making answers more random. On Qwen, their ten-day test-retest reliability falls to 33-59% of the human level, and when made consistent they lose correlation fit. We propose Latent-Predisposition Personas (LPP), whose persons differ stably, not randomly. Each persona receives political engagement, value priorities, and party-relative issue deviations that grow as engagement falls. Answers are sharpened and calibrated to toplines and party crosstabs. At selected operating points, LPP is never significantly worse than any baseline and far more reliable. At matched human-level reliability, it has the lowest correlation error in all six model-survey combinations, also at a lower target. Errors still exceed those between human samples, and gains on framing effects and a frontier closed model are partial.

---


### 273. [Hierarchical Reasoning Action Head for Tiny Vision-Language-Action Models](https://arxiv.org/abs/2611.29813)

**<font color=#1a73e8>作者：</font>** Aditya Makineni, Amitesh Sahoo, Qing Tian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time onboard robot control calls for a lightweight vision-language-action (VLA) model, yet shrinking the backbone leaves less capacity for deliberation at inference time. Chain-of-thought decoding, dual-system architectures, and larger backbones can restore deliberation but reintroduce the latency and memory costs that motivated going small. Recurrent action heads offer a lighter alternative by iterating in latent space before committing to an action, but existing designs refine a single undifferentiated state that must simultaneously encode slowly evolving task context and rapidly changing motor commands. We propose the Hierarchical Reasoning Action Head (HR-AH), which maintains two latent states updated at different frequencies: a low-level state that updates fast, grounded in action tokens and proprioception, and a high-level state that updates slowly, grounded in visual understanding and the instruction-informed low-level state. The two states exchange information through nested reasoning cycles. Because all iteration occurs in the compact head after a single backbone pass, HR-AH adds hierarchical reasoning without increasing the backbone size. With a 22.5M-parameter head, 3-4.3x smaller than those of RD-VLA and VLA-Adapter on the same backbone, HR-AH reaches 97.0% success rate on LIBERO and a 4.40 average chain length on CALVIN ABC->D, at the lowest latency among compared methods. We show that this hierarchy improves performance over a parameter-matched single-state head, and that routing distinct modalities to each level yields further gains in both accuracy and inference cost.

---


### 274. [Model Immunization Cannot Reliably Protect Models from Harmful Adaptation](https://arxiv.org/abs/2611.29815)

**<font color=#1a73e8>作者：</font>** Tong Li, Chenru Wang, Chris Thomas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient fine-tuning techniques have substantially reduced the cost of adapting open-weight models, enabling malicious actors to readily fine-tune them toward harmful capabilities. In response, model immunization modifies a pretrained checkpoint to resist subsequent adaptation toward designated harmful capabilities while preserving its utility and adaptability for benign tasks. Furthermore, a few immunization methods have sought to keep their protection robust to some changes in the attacker's adaptation. However, fine-tuning offers attackers many more low-cost options, and we observe that existing methods still substantially overfit to the attacker configuration they are optimized against. Such overfitting stays hidden when immunization is evaluated under, or near, this configuration, so the reported protection may give a false sense of security. To rigorously evaluate model immunization, we conduct experiments, varying one component of this configuration at a time: the harmful data, the adaptation strategy, or the model initialization. Across four immunization methods on text-to-image generation and image classification, with additional results on language models, these variations substantially degrade the protection, and in many cases the immunized model relearns the harmful capability nearly as well as the un-immunized model. Existing immunization therefore cannot reliably protect models, leaving them vulnerable to harmful adaptation.

---


### 275. [Memphis: A Case Study in Seeding an Agent Task from a Model's Real-World Attempt](https://arxiv.org/abs/2611.29824)

**<font color=#1a73e8>作者：</font>** Ibrahim A. Ahmed, Ahmed Sameh Khalil  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent benchmarks are usually made harder by scaling up the data their tasks are built from, yet models that do well on them still fail at real work. We propose building simulated tasks from a model's own attempt at an open-ended task in the real world, so that the model's failures in the simulation resemble its failures in reality. As a case study, we had GPT-6.1 Sol manage two human workers in Cairo over chat for five shifts, with a budget of 7,000 Egyptian pounds, to build as many USB desk lamps as it could. It built two. From the real-world attempt's transcript, we build Memphis, an evaluation in a model-simulated world. Memphis is hard: GPT-6.1 Sol delivers 1.0 lamp per trial on average and repeats its real-world mistakes, buying too few stands and giving up the search for them. With a one-page hint on where to buy parts and who can wire them, it delivers 9.2. Claude Opus 5.5 delivers 2.2 without the hint and 4.6 with it. We release the task, the trials, the audits, and a redacted record of the real-world evaluation.

---


### 276. [Who Makes the Decision? Auditing an Agentic LLM Pipeline for Illicit Cryptocurrency Transaction Monitoring](https://arxiv.org/abs/2611.29829)

**<font color=#1a73e8>作者：</font>** Vaishnavi Chaughule, Yuchen Zhang, Mohammed Ahnaf Tajwar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic pipelines that combine graph detectors, deterministic rules, retrieval-augmented generation and an LLM judge are being proposed to monitor illicit cryptocurrency flows and to write regulation-citing justifications for analysts. They are evaluated on end-to-end accuracy or on the quality of those justifications, and neither shows which component made a decision. We audit such a pipeline on the Elliptic++ Bitcoin dataset with decision-source attribution, a trace-level protocol with three layers: per-case actual causation, interventional Shapley credit, and mediation of upstream risk scores. A deterministic wallet-score override carries about 94% of the credit for flags, and a verification gate cancels most of the judge's own flags, which fall on licit transactions. Testing the judge alone over 76 evidence bundles, four backbones and two prompts, we find that it follows an injected risk score on the anonymous transaction features it is given, although stronger models decide correctly when the facts are explicit; that a context too short for the system prompt leaves it with no verdict at all; and that it cites regulatory clauses that do not apply, which a substring-based citation check accepts. Hiding the score does not fix the judge, because evidence gathered with the score visible still encodes it. For illicit-activity monitoring, an LLM's justification should therefore not be read as evidence of which component flagged a transaction.

---


### 277. [The Temporal Residual: Fast and Effective Retrofitting of Latent Feedback into Pretrained Language Models](https://arxiv.org/abs/2611.29843)

**<font color=#1a73e8>作者：</font>** Ziyang Cai, Xingyu Zhu, Sanjeev Arora  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A transformer language model computes a deep hidden state for every token but uses it only to sample that token. Existing latent-feedback designs, which feed hidden states back across tokens, are mostly built in during pretraining and gain little when added to a pretrained model. We introduce the temporal residual, a second residual stream that every sublayer reads and writes and that is carried from each token to the next. It adds 2,752 parameters to a 4.2B-parameter model and starts exactly at the pretrained network. Retrofitted onto Qwen3.5-4B-Base with 5B tokens of training, it beats a standard model trained on the same data by 7, 13 and 5 points on AIME 2024, AIME 2025 and AMC 2023, writes shorter solutions, and stays ahead at matched training compute. The separate stream matters: prior designs that feed state into the existing stream recover at most 40% of the gain when retrofitted. Validation loss can mislead: the recipe with the lowest loss gains nothing at decoding. Trained with filler tokens in place of reasoning, the model reasons in its hidden state: its GSM8K accuracy with no visible reasoning rises from 21% to 40%, and falls back when the carried state is zeroed.

---


### 278. [GlobalHRBench: Does Changing the Question Language Change the Legal Answer?](https://arxiv.org/abs/2611.29852)

**<font color=#1a73e8>作者：</font>** Yuding Wang, Yuhang Yao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language matters when deploying LLM agents across borders, especially in law, where the governing rules must hold across working languages. Does changing the language of a legal question change answer accuracy? We introduce GlobalHRBench, pairing 240 employment-law problems across eight jurisdictions and eight languages while fixing facts, applicable law and required conclusions. We evaluate nine models on all 1,920 prompts in independent, closed-book, single-answer trials, scoring legal correctness, completeness and answer-language compliance. GPT-6.1 Sol leads at 76.2% strict passes, with a 5.8% relative best-to-worst language decline, compared with 42.2% for DeepSeek V4.1 Flash. Kimi K3.1 Pro and Claude Sonnet 5.5 reverse order between English and Chinese. A four-model study on 16 paired families compares closed-book answers with governing evidence, added cross-jurisdiction distractors and removal of a governing passage. Governing evidence corrects legal errors and shortens reasoning on recovered answers, yet recognizing an evidence gap does not ensure correct application of the rules that remain. These findings motivate multilingual training for accurate, efficient and evidence-supported answers, and deployment evaluation in the user's working language.

---


### 279. [Semantic repeatability and reproducibility of GPT-5 and Gemini 3 Flash on H5N1 One Health questions](https://arxiv.org/abs/2611.29859)

**<font color=#1a73e8>作者：</font>** Luizza Dalla Pria, Amelia l. Nelson, Renata Ivanek  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Highly pathogenic avian influenza A(H5N1) has re-emerged as a One Health concern since 2024, and the public is increasingly consulting large-language-model (LLM) chatbots for health information during outbreaks. Before a chatbot's accuracy can be meaningfully assessed, its consistency must first be understood, so that any single response can be trusted as a fair representative of the model's behavior. We characterized the semantic repeatability and reproducibility of GPT-5 (OpenAI) and Gemini 3 Flash (Google) on 15 H5N1 One Health questions sourced from social media discourse by adopting and extending a centroid-based evaluation framework. Each question was submitted 30 times and reformulated using five Chain-of-Thought (CoT) variants with 30 runs each, yielding 5,400 responses. Pairwise cosine similarity was computed on MPNet embeddings, with sensitivity analyses across three additional transformers. Statistical inference combined standard nonparametric tests (paired Wilcoxon and Friedman with Holm--Bonferroni correction) with inter-embedding agreement statistics (ICC(2,k) and Cronbach's $\alpha$) introduced here as a methodological addition. Both models produced high mean consistency (0.93--0.97, rescaled to {[}0, 1{]}). GPT-5 showed reproducibility significantly higher than repeatability (W = 3.0, p = 0.0003), whereas for Gemini 3 Flash the two metrics were statistically indistinguishable (W = 42.0, p = 0.33). Differential Diagnosis ranked among the top two CoT framings for consistency in both models. The tested chatbots behave as semantically stable sources on H5N1 One Health questions, and the developed consistency evaluation framework is portable to other domains.

---


### 280. [Escriba-OCR: A 1B Vision-Language Model for Error-Preserving Transcription of Handwritten Portuguese Essays](https://arxiv.org/abs/2611.29874)

**<font color=#1a73e8>作者：</font>** Tardelli Ronan Coelho Stekel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Feedback tools and research on learner writing need transcriptions of handwritten essays that keep exactly what the student wrote: misspellings, line breaks, struck-through words and insertions. Vision-language models (VLMs) read handwriting well, but they also tend to rewrite it into correct language. We measure this on BRESSAY, 1,000 handwritten Brazilian Portuguese essays, with a benchmark that adds error preservation, invented errors, edit-markup precision and recall and line structure to the character error rate (CER) and uses paired bootstrap confidence intervals. We restrict the study to open-weight models that schools can run on their own hardware. Of 22 open baselines, the best, Qwen3-VL 235B-A22B, reaches 5.6% CER on the 199 test pages; none reproduces the edit markup reliably, and every VLM replaces 39-78% of the words absent from a Portuguese dictionary with dictionary words. We fine-tune LightOnOCR-3-1B on the 647 training pages in 85 minutes on one GPU. The resulting Escriba-OCR-1B reaches 2.06% CER, 3.5 points below the best baseline (95% CI [-4.2, -2.9]); under the ICDAR 2024 competition metric it reaches 2.1% CER, below the best published page-level results (2.2-2.4%). It recovers 67% of insertions and 77% of illegible deletions, and reproduces the line structure of 97% of the pages, but still normalises 60% of likely misspellings. Three seeds agree within 0.04 CER points, and quantised to 4 bits the model runs on an ordinary CPU at about one minute per page. On 40 letters of another corpus it matches its base model (without that model's appended comments) but misreads unseen words more often; weight interpolation recovers half the gap. A teacher's review finds that 45% of the judgeable apparent corrections are errors in the BRESSAY ground truth, so dictionary-based scores likely understate preservation. We release the model, the benchmark code and the review data.

---


### 281. [Towards Agentic Video Corpus Moment Retrieval](https://arxiv.org/abs/2611.29877)

**<font color=#1a73e8>作者：</font>** Chenwei Xu, Shang Wu, Zhenyu Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video corpus moment retrieval (VCMR) requires finding the video and time interval that match a text query in a corpus of videos. We present RELAY, a training-free framework for VCMR that shares memory across queries. RELAY processes a batch of queries in three stages: search with a query bank, ranking with video notes, and localization with video prompt caching. In the search stage, an embedding model scores each video by its best-matching frame. The query bank penalizes videos that score highly for many other queries in the batch. In the ranking stage, a vision-language model (VLM) writes notes on each candidate video's scenes, people, objects, and actions once. Then, a large language model (LLM) reranks the candidates from these notes. In the localization stage, a VLM predicts the time interval of the moment in the top-ranked video. When multiple queries select the same video, prompt caching lets the VLM reuse its frames. On the three VERIFIED benchmarks, RELAY outperforms the trained baselines in video retrieval R@1 without training. Without any labeled moment, its predicted intervals are shorter than the annotated ones. In VCMR, it achieves similar performance to VideoSearch-R1 on one benchmark and trails it at IoU 0.5 on the other two. Human annotators also mark shorter moments than the original annotations of the benchmarks. A single margin, calibrated on a few labeled queries, widens the predicted interval to the annotation convention of the benchmarks. With it, RELAY outperforms the trained baselines in VCMR at IoU 0.5.

---


### 282. [Training-Free Interventions for Hallucination in Large Language Models](https://arxiv.org/abs/2611.29909)

**<font color=#1a73e8>作者：</font>** Can Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A frozen language model can give a wrong answer because a fact is unavailable, a reliable passage is ignored, or an unsupported claim survives generation. We review 116 works on inference-time hallucination intervention and its foundations. We trace the development from retrieval and controllable generation to methods that act on input evidence, token scores, internal representations, completed claims, or the decision to answer. For each family we compare its source of evidence, model access, preparation cost, and the task on which a correction can be established. For activation steering, we distinguish estimating a subspace from applying a state-dependent edit and separate interventions on the prompt from those on the generated prefix. Published comparisons show why faithfulness to a source, factual correctness, informativeness, and answer coverage must be measured separately. Applications in time-sensitive question answering, document synthesis, and visual grounding identify when source authority, evidence availability, or capability preservation limits a reported gain.

---


### 283. [SpectralRoute: Adaptive Spectral Routing for Training-Free Open-Vocabulary Hyperspectral Segmentation](https://arxiv.org/abs/2611.29919)

**<font color=#1a73e8>作者：</font>** Qingmei Li, Xiaoya Fan, Juepeng Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation enables the recognition of arbitrary categories through natural language descriptions and has recently been extended from natural images to remote sensing. However, existing approaches primarily focus on three-channel optical imagery or limited-band multispectral data, while pretrained vision-language models (VLMs) struggle to directly exploit the rich spectral information of hyperspectral imagery (HSI) without additional adaptation. More importantly, different land-cover categories rely on distinct spectral cues, which may be weakened by uniform fusion. To address these challenges, we propose SpectralRoute, a training-free framework for open-vocabulary hyperspectral segmentation. Specifically, we construct complementary spectral views from HSI and enrich category descriptions with external spectral knowledge, enabling frozen vision-language models to extract diverse spectral-semantic responses. We then introduce a class-adaptive spectral routing mechanism that selectively amplifies discriminative spectral responses for each category, overcoming the limitations of uniform fusion. Furthermore, physical spectral priors are incorporated to refine predictions for visually similar land-cover categories. Experiments on three hyperspectral benchmarks demonstrate that SpectralRoute consistently outperforms state-of-the-art methods without additional training.

---


### 284. [Reward Blindness: A Theoretical Framework for Diagnosing Reinforcement Learning Reward Limitations in Text-to-SQL](https://arxiv.org/abs/2611.29930)

**<font color=#1a73e8>作者：</font>** Lakshmi Muraleedharan Nair, Shiqi Huang, Fangyu Lo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL systems let users without programming expertise query relational databases in natural language. Reinforcement learning has become the dominant way to train such systems, yet progress is still judged by a single number, execution accuracy, which counts correct queries but says nothing about which kinds of semantic error survive training. This paper develops a theoretical framework that examines text-to-SQL from the perspective of reward design. We introduce Reward Error Sensitivity, a measure of how strongly a reward function separates queries that contain a given error type from queries that do not, and prove a Reward Blindness theorem: when this sensitivity is zero, policy-gradient training carries no systematic signal for removing that error. Using fourteen published finegrained error signals for four text-to-SQL systems on the BIRD benchmark, we build error profiles and estimate sensitivities for common reward designs. Predicate and result-level errors are the most frequent, firing on up to 27 percent of queries, while structurally deep errors such as suboptimal joins persist at 5 to 12 percent. Each reward family has a distinct and predictable set of blind spots, and inexpensive database-level checks that need no language model calls detect 45 to 60 percent of semantic errors. Controlled training simulations confirm that executiononly reward leaves output-preserving errors untouched, whereas a signal-grounded reward removes them even when the detectors are noisy.

---


### 285. [LODESTONE: Linking System Events to Threat Intelligence for Evidence-Grounded Cyber Attack Investigation](https://arxiv.org/abs/2611.29932)

**<font color=#1a73e8>作者：</font>** Liangyi Huang, Zichen Liu, Fei Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> System provenance graphs help reconstruct attacks through causal dependencies, but these connections alone do not explain how events accomplish an adversary's goal. Cyber threat intelligence (CTI) provides the necessary security knowledge, yet linking it to execution evidence requires bridging differences in meaning and granularity between events and attack relations amid scarce labels and sparse relevant evidence. We present LODESTONE, a cross-graph alignment system that links observed system events to CTI attack relations to support evidence-grounded attack reports. LODESTONE uses a novel CTI-driven training-data engine and an expert-verified benchmark of edge-level correspondences and reference attack reports. The engine pairs real CTI knowledge graphs with provenance graphs from isolated executions. A large language model (LLM) agent recursively improves correspondences by checking execution evidence and repairing retrieval, parsing, and reproduction failures; experts independently verify benchmark correspondences. LODESTONE combines text cross-encoder and directed-graph relevance scores to extract compact alert-centered subgraphs, retrieves article-level knowledge graphs through node- and edge-level dual-softmax assignment, and uses a fine-tuned 4B-parameter LLM to align event combinations with CTI attack steps. We evaluate LODESTONE on 27 expert-verified attack cases amid continuous benign activity from real applications, using 713 CTI articles. LLM judgments aligned with multiple human experts yield an attack-step description score of 82%, and attack identification reaches 91%, versus 73% and 32% using the same generator with provenance alone. Baseline pipelines and coding agents achieve description scores of at most 57%. Human-verified correspondences further demonstrate advantages in balancing attack-edge coverage with subgraph size, CTI retrieval, and cross-graph alignment.

---


### 286. [Benchmarking VLM Medical Hallucination across 5 Modalities](https://arxiv.org/abs/2611.29934)

**<font color=#1a73e8>作者：</font>** Zhixing Cao, Yusen Peng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hallucinations in Vision-Language Models (VLMs) within the medical domain remain a difficult and not well-understood problem, and it is still unclear where these models break down. Although several benchmarks targeting medical hallucination have been introduced, they often lack broad coverage across different medical imaging modalities. We introduce Multi-Med, a medical hallucination benchmark containing 1,000 image-question pairs spanning five distinct modalities. Using this benchmark, we perform an in-depth experimental study of 10 widely used VLMs across five modalities and four question categories. Our findings indicate that model performance differs substantially depending on the imaging modality and question type, and that the differences among the best-performing models are not statistically significant.

---


### 287. [SAEPO: Sparse-Autoencoder-Guided Credit Assignment for Policy Optimization](https://arxiv.org/abs/2611.29936)

**<font color=#1a73e8>作者：</font>** Yusong Zhao, Zihao Zhao, Zirui Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has demonstrated strong performance in improving large language model (LLM) reasoning, yet its credit-assignment signal remains coarse. Outcome verifiers provide scalable supervision by judging whether a completed response is correct, but they do not directly indicate which intermediate reasoning tokens contribute to success or failure. As a result, policy optimization can be inefficient, especially when training base models directly from sparse outcome feedback. In this paper, we introduce SAEPO, a Sparse AutoEncoder-guided token-level credit assignment method for outcome-supervised Policy Optimization. Rather than treating correctness only as a rollout-level (sequence-level) signal, SAEPO uses a pretrained sparse autoencoder (SAE) to build token-level semantic representations within reasoning trajectories; it scores each token based on the SAE concepts (e.g., penalizing wrong "final-answer" tokens but rewarding correct "reasoning-process" tokens), learned in an unsupervised manner, to achieve fine-grained credit assignment. SAEPO is a plug-in advantage-shaping module compatible with various policy optimization algorithms. We instantiate SAEPO with both GRPO and GSPO, covering token-ratio and sequence-ratio policy-gradient objectives, and evaluate SAEPO across three LLM backbones on six math and two code benchmarks. Empirical results show that SAEPO improves both the math and code benchmark averages over the matched baselines, with gains of up to 6.63% and 5.57%, respectively. On Qwen3-1.7B-Base, training curves also show faster early accuracy growth. Feature and token-level analyses suggest that the SAE-derived signal favors question-relevant concepts and reasoning tokens.

---


### 288. [The Answer Is Not the State: Trajectory-Level Corrigibility in Diffusion Language Models](https://arxiv.org/abs/2611.29937)

**<font color=#1a73e8>作者：</font>** Junchi Liao, Wentao Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models generate tokens at many positions on a shared canvas, making unfinished responses appear revisable. We find a counterexample: after the final answer is reopened, previously generated rationale can reconstruct the old decision despite newly available evidence. We isolate this effect by comparing reopening the answer alone with reopening both rationale and answer, and by exchanging rationales between paired trajectories. On a 150-question source-disjoint benchmark, reopening both regions makes decisions follow the evidence currently present--whether correct or deliberately corrupted--across Dream, LLaDA, and iLLaDA. On a new 100-question free-form short-answer evaluation, the same effect remains strong in LLaDA and iLLaDA but is negligible in Dream. Coherent transplanted rationales steer rebuilt decisions, while token-level attribution improves which positions to reopen without producing a compact repair. Corrigibility therefore depends on retained rationale state, not answer openness alone.

---


### 289. [When 1+1 $\neq$ 2: Benchmarking Civil-Time Reasoning in Large Language Models](https://arxiv.org/abs/2611.29972)

**<font color=#1a73e8>作者：</font>** Melika Shirian, Kianoosh Vadaei, Arshia Hemmat 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Calendar arithmetic is non-linear. When 1:59 AM + 1 minute occurs during daylight saving spring-forward, the result is 3:00 AM, not 2:00 AM, as the hour is skipped. We introduce CivilTime-Bench, a benchmark for civil-time reasoning covering daylight saving transitions, non-hour offsets, date-line crossings, and ISO week boundaries. With 60,011 training and 10,500 evaluation examples under strict output-contract evaluation, we benchmark seven LLMs (six instruction-tuned models and Llama-3.1-8B base) and find: zero-shot exact match varies substantially across models, contract-aware prompting often improves format compliance but yields inconsistent accuracy gains, few-shot in-context learning provides model-dependent improvements, and fine-tuning achieves 74.6--86.6% EM on synthetic evaluation but only 36.6--45.2% on HumanTime-500 for models with valid results on both splits, highlighting substantial limitations in generalization. We release the benchmark and code.

---


### 290. [Language models seek help despite guaranteed score losses in question answering](https://arxiv.org/abs/2611.29981)

**<font color=#1a73e8>作者：</font>** Jiahao You, Ziye Jia, Chao Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> At the highest waiting cost in a multiple-choice question-answering task, all 7 tested open-weight language models still consult an expert even though a correct expert answer earns fewer points than an incorrect independent answer. Pooling over expert accuracy and fixed-fee combinations gives help-seeking rates of 20.8% to 94.1% across models. We test 2,291 questions across 54 combinations of expert accuracy and consultation costs, comparing observed decisions with an expected-score baseline based on independently measured and calibrated model confidence. Help-seeking rates vary across conditions with the same expected consultation score. Fine-tuning reduces decision regret by 59% to 87% on held-out questions within the training range but increases inconsistency at matched expected consultation scores. In a separate task, external routing improves scores by 0.180 to 0.273 points per question with candidate answers held fixed.

---


### 291. [How Relations Impose Embedding-Space Structure](https://arxiv.org/abs/2611.29986)

**<font color=#1a73e8>作者：</font>** Lachlan Cowley, Jey Han Lau, Yulia Otmakhova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are known to encode simple relations, such as synonymy, in the geometry of their representations. It is unclear whether they also encode complex patterns of relationships such as those that drive analogy. We present a simple method, with no learned parameters, based on comparing the internal structural arrangements between disparate domains, to test this. Using our method we find over multiple models that representations are arranged consistently to encode complex relationship similarities. Models align distant representation clouds so that facets of meaning are easily comparable under simple mappings. Our work extends mechanistic accounts of representation space to the relative arrangement of representations that may be only weakly related to one another, showing that representation geometry is far richer than previously thought. Code and data: this https URL

---


### 292. [SHAKTI: Evidence-Grounded Conversational AI for Nutrition and Health](https://arxiv.org/abs/2611.29988)

**<font color=#1a73e8>作者：</font>** Chaitanya Pallerla, Dongyi Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) answer many diet and health questions but can state unsupported claims and cite sources that do not support them. We present SHAKTI (Smart Health Advisor for Knowledge-based Tailored Interventions), a conversational assistant that answers only from retrieved scholarly papers and exact food-composition data, and evaluate it with retrieval, generation, grounding, efficiency and contextawareness metrics. We indexed 484,368,086 OpenAlex works, searched exactly on a GPU for evaluation (10,065 NFCorpus, BioASQ, SciFact and PubMedQA questions) and through a compressed 230-million-abstract index in deployment. On 1,000 stratified questions, we compared single-shot, multi-hop, corrective and deep-research retrieval-augmented generation (RAG) with Claude Sonnet. SHAKTI adds conversational query rewriting, USDA FoodData Central lookups, source-link checks and online verification of quotes and numbers. It was tested in 36 scripted conversational turns, a 248-question memory-depth test and a 38-question load test. Claims were checked by a Claude Opus judge against exactly the text the system saw. MedCPT reranking of hybrid retrieval gave the best MRR (0.21) and MAP@100 (0.14). Across existing RAG methods, faithfulness was 0.95-0.96, claim hallucination 0.5-0.8% and context precision up to 0.98; the deep-research agent answered 73.2% of BioASQ questions correctly. In conversation, SHAKTI reached a context-awareness score of 97.1%, faithfulness 95.5%, 1.9% unsupported claims, no contradicted claims and 229/229 working source links; it resolved references to the first question after 16 unrelated questions. An answer cost 14,716 tokens (US$0.06) with a median latency of 24 s. Large-scale retrieval with agentic evidence selection and mechanical verification yields auditable, low-hallucination nutrition answers.

---


### 293. [Antiphony: A Dual-Process Agent for Deepfake Video Detection with Real-Video Calibration](https://arxiv.org/abs/2611.29999)

**<font color=#1a73e8>作者：</font>** Xinyu Yan, Yurong Hao, Zherui Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable video deepfake detection requires generalization to unseen generators while limiting false alarms on authentic footage. Although existing detectors capture diverse visual cues, they may produce overconfident errors under generator shift, limiting the reliability of confidence-based fusion. Threshold calibration is further complicated by shifts in authentic capture domains and the lack of future-generator examples. To address these challenges, we present Antiphony, a framework that combines calibrated fusion of four visual experts with selective investigation. Authentic videos serve as a shared reference for score fusion and threshold calibration, enabling threshold updates without target deepfakes. For this expert-fusion stage, we establish finite-sample false-alarm control when the scoring procedure is fixed independently of calibration and authentic samples are exchangeable. To refine decisions near the calibrated threshold, a tool-using multimodal investigator examines these videos and contributes an additional fusion score. We train the investigator on generator-held-out predictions and counterfactual expert outputs, to improve robustness to unreliable expert evidence. Across six benchmark protocols, Antiphony achieves a mean benchmark score of 88.3%, exceeding the strongest evaluated MLLM and conventional detector baselines by 14.7 and 11.5 points, respectively. It also outperforms ARGUS by 20.2 points on average and by 3.6 balanced-accuracy points on FaceVid's 20 unseen generators.

---


### 294. [Training Dynamics of Large State-Transition Models](https://arxiv.org/abs/2611.30005)

**<font color=#1a73e8>作者：</font>** Yee Man Choi, Fengchi Wang, Ruiquan Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Next-token prediction relies on learned token embeddings whose dimension $d$ is much smaller than the vocabulary size $V$. Existing analyses of training dynamics either fix the embeddings with $d\ge V$ or train them only in restricted settings. It remains unclear whether jointly training the embeddings by gradient-based methods from random initialization leads to accurate prediction when $d<V$. In this paper, we study this question in the simplest setting where it is already nontrivial, namely next-token prediction with a one-token context, which we refer to as a state-transition model. The model consists of an input embedding and an output embedding, either untied or tied, and is trained from Gaussian initialization by perturbed gradient descent with weight decay on the population cross-entropy loss. We consider ground-truth transition laws whose centered log-probability table has low rank and bounded entries, and measure the prediction quality by the relative prediction gain (RPG). It is zero for the uniform predictor and one for the optimal predictor. For the untied model, we show that when $d=\Omega(\sqrt V)$, with probability at least $1-e^{-cd}$ for some constant $c$, the RPG is above $7/8$ at every iterate in the final $1-1/d$ fraction of training iterations. For the tied model trained on a subset of states, we prove that the RPG on the observed states is $1-O(V/d^2)$, and under a coverage condition on the ground truth and a bound on the learned embeddings, we further prove a prediction guarantee on the unseen states. Our analysis is based on the bounded trace of the Hessian of the softmax cross-entropy loss, which implies that the approximate second-order stationary points reached by training have high prediction gain. Numerical experiments with practical parameter choices illustrate the persistent training gain and the transfer of the tied model.

---


### 295. [MORSE: Optimizing Streaming Memory Design via Open-World Auto-Research](https://arxiv.org/abs/2611.30011)

**<font color=#1a73e8>作者：</font>** Ce Zhang, Jianshu Zhang, Jinxi He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A streaming video system must decide in a single pass what evidence to retain under bounded frame storage, before it knows which details a future question will require. Recent recursive self-improvement methods automate the design of the harness that stores and retrieves this evidence. They revise the harness in response to failures, but the editor must still devise each repair from its prior knowledge and a predefined set of tools. A failure that recurs across videos, however, may point to a problem that prior work has already addressed. We introduce MORSE (Memory Optimization with Recursive Self-Evolvement), an open-world auto-research framework that uses recurring failures to guide an online search for solutions. Its editor groups failures in training traces by cause, then searches papers, model cards, and code for methods it can adapt or pretrained perception models it can use. When the editor introduces a new perceptual capability, it can also revise how the harness stores and retrieves the resulting evidence for a frozen video-language model. On held-out validation streams, MORSE first selects revisions that improve answer quality, then seeks faster revisions that preserve those gains within a specified tolerance. Across three streaming video benchmarks, MORSE consistently achieves the highest answer accuracy within each frozen-backbone comparison. On OVO-Bench, our Qwen3-VL-8B harness answers queries in 0.30 seconds on average while achieving 75.1% accuracy, 3.1 percentage points ahead of the next-best evaluated harness using the same frozen backbone.

---


### 296. [3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets](https://arxiv.org/abs/2611.30013)

**<font color=#1a73e8>作者：</font>** Bohan Zeng, Kaixin Zhu, Yifan Yang 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Animating arbitrary 3D assets from instructions requires both structural inference and motion control, yet existing motion benchmarks mostly cover conventional human or animal skeletons with simple instructions. We introduce DivDynBench, which evaluates rigging and motion generation across six morphology categories, with instructions requiring multi-phase part coordination and explicit timing, angle, repetition, and trajectory constraints. With large language models, we systematically compare three common paradigms: specialized motion generation, video generation followed by motion recovery, and direct agent-driven generation. We analyze their control capabilities, cross-morphology adaptability, and generation costs. Guided by this comparison, we propose an Agentic Motion Framework in which an agent writes compact parametric skeleton and motion programs, and a deterministic executor performs rigging, kinematic solving, and geometric correction. Compact parameter control reduces generation overhead and improves rigging reliability and motion-control accuracy, providing practical guidance for deploying complex 3D motion generation.

---


### 297. [OWE-Bench: A long-horizon benchmark for measuring real-world engineering](https://arxiv.org/abs/2611.30017)

**<font color=#1a73e8>作者：</font>** Jacob Cole, Martin Dimakis, Victor Barres 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present OWE-Bench (OpenWorldEngineer-Bench), a benchmark of 26 long-horizon engineering tasks written by domain experts in software engineering, physical engineering, machine learning, and scientific computing. Tasks range from optimizing kernels and designing an aircraft, to identifying the faults responsible for an earthquake. Each task requires significant domain knowledge and engineering work, with models averaging hundreds of millions of tokens per task. Solutions are scored on practical measures such as speed, cost and accuracy, both on provided cases the agent could test against and on hidden cases that an engineer would expect from the task description. The best-performing frontier model so far, Claude Fable 5.2, scores 54.6% and averages 211 million tokens per task. We highlight two findings. First, when models are given more time, they use more test-time compute and achieve higher scores. Models also scale differently with test-time compute: GPT-6 Astra achieves higher scores at shorter time limits and at equal token use, while Claude Fable 5.2 uses more tokens at longer limits to achieve the highest overall score. Second, each model scores lower on hidden cases than on the provided cases, by an average of 18 points, which we call the deployment gap. Models also fail to predict the deployment gap, overestimating their performance on hidden test cases by an average of 21 points. We hope that OWE-Bench grounds progress toward agents whose engineering solutions perform as well in deployment as they do in testing.

---


### 298. [Fast 4-bit KV-Cache Decoding on Hopper GPUs: Why Existing Kernels Are Slow and How to Fix Them](https://arxiv.org/abs/2611.30027)

**<font color=#1a73e8>作者：</font>** Jian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A 4-bit KV cache reads about half the bytes of FP8, but Hopper GPUs have no FP4 hardware and little instruction-issue capacity per byte of memory bandwidth, so 4-bit values must be decoded in software. On H200, vLLM's NVFP4 KV path (FlashInfer's decode) reaches 10-20% of memory bandwidth and is up to 1.7x slower than FP8. NVBit instruction counts show two causes: the kernels behind vLLM's 4-bit paths (FlashInfer NVFP4, Triton UltraQuant) execute 2-6x Hopper's issue budget per byte and serialize loading, decoding and matrix multiplies. Our Hopper-native decode kernel overlaps a TMA producer warp with two compute warpgroups, lays the cache out at write time so decoded values feed the tensor cores from registers, and swaps the matrix operands so small query groups need no padding. On H200 it reaches 67-75% of peak bandwidth at batch 32-128 and at all 11 shapes is 1.12-1.49x faster than the faster of XQA and FlashAttention-4's proposed native FP8. Inside vLLM, with an accuracy recipe (K mean removal and rotation, 4 BF16 sink tokens, BF16 layer 0), it decodes 1.12-1.64x faster per step on Llama-3.1-8B than vLLM's FlashInfer FP8 path at batch 8 and above (1.04-1.24x over FlashAttention-4's FP8), is level at batch 1, and holds 1.63x as many tokens. On one H200 under a reasoning-like request stream, the highest rate at which 99% of requests meet the latency targets is 1.23-1.32x FP8's on Llama-3.1-8B and 1.67-2.20x on Qwen2.5-72B, as the cache becomes the limit; prefill-heavy streams are worse (7% slower prefill). On five 7B-32B models, repeated runs show no significant accuracy difference from BF16 KV. In Qwen2-family models, whose reasoning variants collapse under FP8 KV, layer 0's key mean is almost entirely the key-projection bias identified by prior work, seen through RoPE and computable from the weights alone; keeping that layer in BF16 restores FP8 KV and, with K mean removal, 4-bit KV.

---


### 299. [TRAE: Trustworthy Automated ESG Annotation via Multi-Agent Consensus and Confidence Assessment](https://arxiv.org/abs/2611.30035)

**<font color=#1a73e8>作者：</font>** Jaeyoung Lee, Misuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> With the growing demand for ESG disclosure and evaluation, constructing high-quality datasets for automatically extracting ESG-related information from large-scale documents has become essential. However, ESG annotation remains challenging due to strong context dependence, ambiguous label boundaries, and the need for domain expertise, resulting in high annotation cost and limited scalability. To address these challenges, we propose TRAE (TRustworthy Automated ESG annotation), a multi-agent framework for scalable and reliable ESG data construction. Unlike direct LLM-based annotation, TRAE evaluates annotation reliability by modeling agreement, confidence, and reasoning consistency among multiple agents through a structured multi-step reasoning process. Experimental results demonstrate that TRAE improves annotation performance compared with existing automated annotation strategies. Furthermore, TRAE supports a hybrid human-AI annotation strategy that assigns expert labeling only to uncertain samples, reducing annotation cost while preserving data quality. Using TRAE, we construct a high-quality ESG dataset containing approximately 20,000 instances with complete reasoning traces, intermediate agent outputs, and reliability information to enhance transparency and reproducibility. Overall, this work provides a practical and scalable framework for trustworthy ESG data construction. The code and data are publicly available at: this https URL.

---


### 300. [Teaching How to Reason, Beyond What to Answer: Evidence-Faithful On-Policy Distillation for streaming video understanding](https://arxiv.org/abs/2611.30040)

**<font color=#1a73e8>作者：</font>** Mengnan Liu, Sanping Zhou, Kun Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Moment Retrieval (MR) aims to localize the temporal segment in a video that corresponds to a given textual description. However, a textual query often provides only a sparse semantic description of the target event, whereas the video contains rich and fine-grained visual variations. This mismatch creates an inherent gap between textual semantics and visual content, making a single textual input insufficient for precise cross-modal alignment. As a result, when multiple temporally adjacent or semantically similar segments exist, the model may struggle to distinguish the target moment from confusing candidates. To address this challenge, we propose a Multi-Perspective Auxiliary Representation (MPAR) framework, which aims to bridge this alignment gap by enriching a single textual input with complementary visual cues from multiple perspectives. Specifically, MPAR consists of three key components: (1) Auxiliary Representation Initialization (ARI) constructs multiple learnable representation slots from the original query, preserving the query intent while preparing flexible carriers for subsequent visual cue injection; (2) Visual-Induced Semantic Structuring (VISS) injects target-specific visual attributes into each representation while preserving semantic coherence with the original query; and (3) Multi-Perspective Semantic Aligner (MPSA) aligns each auxiliary representation with corresponding video regions to enhance discriminative localization. By constructing multi-perspective auxiliary representations and guiding the model to attend to relevant visual regions across these representations, our model achieves more accurate moment localization. Extensive experiments on MR benchmarks demonstrate that our MPAR outperforms state-of-the-art methods, validating the effectiveness of MPAR.

---


> [!TIP]
> 当前位于：**251-300**（第 6/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-486](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
