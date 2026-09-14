# 🧠 大模型相关研究 | 2026年09月14日

> 本类共 **153** 篇论文：已确认 **145** 篇，待复核 **8** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-153](./part-04.md)

---

### 51. [MOSAIC: Query-Aware Exploration Policy Adaptation for GraphRAG](https://arxiv.org/abs/2609.11065)

**<font color=#1a73e8>作者：</font>** EunKyeong Lee, Kyeong-Jin Oh, Jinwon Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph Retrieval-Augmented Generation (GraphRAG) can connect evidence distributed across a corpus graph, but most systems use largely shared exploration procedures across queries. This creates a structural mismatch: direct facts may need compact local neighborhoods, comparisons need balanced coverage of multiple targets, and mediated questions may require deeper paths through weakly related connectors. We present Mosaic, a training-free framework that formulates GraphRAG retrieval as a per-query control problem. An LLM analyzer converts query-specific evidence requirements into a bounded policy over seed selection, graph traversal, stopping, and evidence selection, while the corpus graph, indexes, scoring functions, grounding procedure, and answer generator remain shared.
On GraphRAG-Bench, Mosaic achieves query-weighted Answer Correctness of 76.97 on Medical and 64.33 on Novel, improving over the strongest previously reported overall results by 5.13 and 4.43 points. On Medical, it reaches 95.1 Evidence Recall and 86.1 Context Relevancy. Controlled comparisons on an identical graph and generator show that no fixed narrow, medium, or wide policy is consistently optimal; Mosaic improves by 9.96 points over the strongest canonical fixed policy. Relative to Fixed Wide, it evaluates 81.9% fewer paths and retains 47.2% fewer evidence items. Transfer experiments on HotpotQA, MuSiQue, and 2WikiMultiHopQA further show that the policy interface can be applied without benchmark-specific retriever training.

---


### 52. [When Noise Fabricates Bias: The Fragility of LLM-as-a-Judge Bias Measurement under Noisy Text](https://arxiv.org/abs/2609.11067)

**<font color=#1a73e8>作者：</font>** DongHyun Ryu, Jaehyeok Lee, YeongJun Hwang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as judges to measure social bias in text, yet the passages they judge are often noisy, containing typos, informal spelling, and broken punctuation. The consequences of such surface noise for social bias measurement remain unclear. To investigate this question, we apply five realistic noise conditions at multiple intensity levels to 3,822 stereotype-related responses and compare the resulting bias judgments with those on the original text. We find that such surface noise does not degrade bias measurement symmetrically: it is far more likely to turn neutral judgments into biased ones than biased judgments into neutral ones, by up to a 120x margin. We further observe two non-obvious effects across four LLM judges: in the most fragile judge the distortion is at its purest at mild, realistic noise levels, where erasure is scarcest, and as judges grow robust it attenuates toward parity rather than reversing. Bias measured on noisy text is therefore systematically overestimated, most in the categories that matter most for fairness.

---


### 53. [Beyond Solver Verdicts: Generative Reward Models for Autoformalization](https://arxiv.org/abs/2609.11085)

**<font color=#1a73e8>作者：</font>** Vikash Singh, Debargha Ganguly, Aman Goel 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neurosymbolic systems rely on mathematical solvers to guarantee reasoning correctness, yet solvers are fundamentally blind to whether a formal translation maintains strict reference-equivalence to a designated formalization. We formalize this vulnerability as Verdict-Preserving-Unfaithfulness (VPU): a failure mode where an incorrect encoding executes successfully and matches the expected verdict. We theoretically prove that structural, verdict-only verification heuristics are mathematically bounded to chance-level detection on these deceptively valid traces. To resolve this, we introduce Generative Verification (GenV), which distills an offline Z3-equivalence oracle into a reference-free, continuous reference-equivalence score by repurposing the language model's native vocabulary space. Mechanistic analysis via decision-projected logit lenses and sparse autoencoders shows this generative readout natively extracts precise spatial error coordinates without explicit localization training. Empirically, our oracle-mined verifier (GenV+HN) achieves 0.961 AUROC in reference-equivalence verification, generalizes zero-shot across unseen translators and divergent formal styles, and yields an 11.3-point downstream accuracy gain in agentic test-time compute allocation.

---


### 54. [ProMediConv: Benchmarking Proactive Conversational Agents in Legal Dispute Mediation](https://arxiv.org/abs/2609.11101)

**<font color=#1a73e8>作者：</font>** Zesheng Wei, Mengfan Li, Wenhao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dispute mediation is essential for maintaining social harmony and resilience, yet developing skilled mediators is costly and time-consuming. Existing LLM-based mediation research remains limited by unrealistic task formulations, low-fidelity datasets, and coarse evaluation metrics that obscure turn-by-turn dynamics. To address these gaps, we introduce ProMediConv, a novel benchmarking framework that models mediation as a proactive, multi-stage, and party-aware dialogue process incorporating 11 mediation strategies and four party behavior pattern (BP) states. Using 972 complete real-world cases, we construct a high-fidelity mediation dataset with utterance-level annotations of strategies and BP states. Furthermore, to better assess agent impact, we propose MAD (Mean Attribute Difference), a fine-grained metric that captures BP shifts throughout the dialogue. Leveraging this framework, we establish a comprehensive benchmark by evaluating diverse models alongside our tailored baseline ProMediAgent. Extensive empirical analyses reveal critical behavioral phenomena and underscore the persistent challenges current models face in dynamic, multi-party mediation. Ultimately, ProMediConv provides a rigorous foundation and a vital quantitative standard for advancing AI-assisted conflict resolution. Our dataset and codebase are accessible at this https URL.

---


### 55. [But How Would AI Agents Run a Town's Economy?](https://arxiv.org/abs/2609.11108)

**<font color=#1a73e8>作者：</font>** Sajal Regmi, Siddhartha Pudasaini, Chetan Phakami Pun  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We placed 100 memory-equipped large language model (LLM) agents in charge of a closed, money-conserving spatial economy on real Pokhara Lakeside geography (earning wages, running businesses, setting prices) and ran this multi-agent simulation for up to 26 simulated weeks, well past the 1-2 weeks typical of agent-society studies. Across 91 validated runs (2.44M agent decisions, 21.5B tokens), the money stops moving, in a specific and measurable way. A 12x tourist demand shock raises business revenue 4.62x ($p<0.001$), which we decompose exactly into a 1.50x extensive margin (more businesses trading) and a 3.07x intensive margin (more revenue each). Monetary transmission stops there. Wages move 1.03x ($p=0.42$); 0.3% of 3,981 menu items are ever repriced ($p=0.47$). A randomized cash transfer (NPR 5,000 to 20 of 100 agents) shows the same pattern from the opposite direction: 96.7% is still held 311 pulses later, marginal propensity to consume 3-4% by two independent measures, indistinguishable from zero. The wealth distribution is consequently near-frozen at the horizon this literature uses ($\rho=0.964$ over 2 simulated weeks), but not frozen. $\rho$ falls to 0.832 at 12 weeks and 0.752 at 26, a horizon-dependence no short study can see. Matched ablations show which knob actually matters. Swapping the backing LLM moves every outcome we measure ($p=0.0039$); deleting agents' memory moves none of them detectably. A purely social tool fails 94-97% of the time across two model families, compared with ~96% success on economic tools, with no measurable shift away from it. Every headline number is verified twice, by a live validator and by an offline recomputation that reconciles each agent's wealth against its own signed transaction history, and we release the full run corpus for reanalysis.

---


### 56. [How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding](https://arxiv.org/abs/2609.11109)

**<font color=#1a73e8>作者：</font>** Jeongyeon Kim, John Mitchell  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The utility of AI in multi-coder qualitative coding has been widely discussed, yet little empirical evidence exists to delineate the contexts in which it performs reliably. We address this gap by quantifying the effectiveness of multi-agent LLM coding across varied qualitative datasets, revealing key contextual and structural factors that mediate coding outcomes. We developed a literature-informed baseline pipeline that enables AI agents to independently code, debate, and reconcile disagreements. Results revealed that coding accuracy depends on factors such as codebook length, qualitative data similarity, and agent disagreement. Notably, intense and unresolved debates between agents led to higher accuracy. Our analysis showed that while LLMs emulate many human discussion behaviors, they lack adaptive responsiveness to context. From these findings, we offer design recommendations for building automated coding systems. Our open-source AI discussion dataset and methodological framework lay the groundwork for advancing the design of AI-mediated automated thematic analysis.

---


### 57. [Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and Evaluation](https://arxiv.org/abs/2609.11115)

**<font color=#1a73e8>作者：</font>** Koutian Wu, Junjie Zhou, Ergan Shang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmark researchers and developers of large language models (LLMs) and other AI systems need to find relevant evaluations, locate their benchmark datasets and code, and understand the settings behind reported scores. We present Benchmark Radar, a living database and search engine for retrieval and discovery of AI benchmarks, covering LLM evaluation, agentic and tool-use benchmarks, coding, reasoning, safety, and domain-specific evaluations. The system combines daily discovery of benchmark papers, repositories, datasets, and releases with a searchable benchmark catalog, mentions in model cards and technical reports, and score histories. It retains source identities and citations so readers can inspect candidate benchmarks and their evaluation evidence. Daily discovery draws on 37 sources: 13 direct connectors and 24 first-party research and engineering feeds. The catalog contains 1,283 source records drawn from 4 benchmark catalogs and 12,916 numeric observations on 790 records. We describe collection and retrieval, audit the full catalog, and examine benchmark saturation, adoption trends, and the limits of score comparisons. A worked example walks through a complete prior-art search, showing how to query the catalog and inspect benchmark evidence when designing a new evaluation. We release the web dashboard with a benchmark leaderboard, a Pareto frontier view of score against measured use, saturation and trend views, daily feeds, downloadable evidence, a command-line interface (CLI) for offline queries, and reproducible analysis.

---


### 58. [Overview of the NLPCC 2026 Shared Task 11: Agent-Based Experiment Reproduction from Scientific Papers](https://arxiv.org/abs/2609.11117)

**<font color=#1a73e8>作者：</font>** Hanhua Hong, Yizhi Li, Luu Gia Huy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reproducibility is essential to scientific progress, yet the growing volume and complexity of scientific publications make exhaustive manual verification increasingly impractical. Although recent advances in large language model (LLM) agents enable automated experiment reproduction, existing evaluations largely focus on final repositories and are typically limited to machine learning (ML). We introduce AgentActionBench, a process-oriented benchmark for evaluating agent-based experiment reproduction across ML and AI4Science domains. Our framework uses an MCP-based Action Recorder to capture agents' behaviour throughout the reproduction process and evaluates the resulting traces with paper-specific rubrics. AgentActionBench contains 150 papers, including 120 ML papers and 30 AI4Science papers. A human-annotated subset covering 10% of the benchmark provides validation data, while model-assisted augmentation expands the full benchmark to more than 10,000 rubric items. Experimental results show that current systems remain limited, with execution as the primary bottleneck. Meanwhile, the strong Pearson and Spearman correlations between model-generated and human-annotated rubrics validate the reliability of our scalable rubric-generation approach.

---


### 59. [Beyond Benchmarks: Using VLMs to Reveal Systematic Classification Failures Under Real World Conditions](https://arxiv.org/abs/2609.11126)

**<font color=#1a73e8>作者：</font>** Dieuwertje Alblas, Alma M. Liezenga, Jan Erik van Woerden 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Verification and validation (V&V) of classification models is crucial to enable a wide range of sensor processing applications. Currently, the V&V process relies on time-consuming manual inspection of erroneous samples to find meaningful patterns. This work explores the use of Vision Language Models (VLMs) to speed up this laborious process. VLMs are trained to embed images into a semantically meaningful vector representation, from which human-interpretable systematic errors can be distilled. Deploying such VLM-based methods in a defence context introduces two major challenges: (1) the defence domain is underrepresented in the training data of VLMs, and (2) surroundings and context are less diverse than for other domains. This study provides an initial assessment of the suitability of VLM-based methods for V&V of defence applications. We propose a VLM-based error slice detection (ESD) method that independently groups and labels systematic errors made by a classification model. We demonstrate that this method is able to identify operationally-relevant artificially added perturbations in a non-military dataset. In a military context, our method clusters and describes images based on their surroundings, but also exhibits overlap between cluster descriptions. We further investigate the difference in embedding variation between our military and non-military dataset, which remains a topic of interest. Although the results do not yet warrant fully automated V&V through VLM-based ESD, they show that VLMs could be used to accelerate V&V processes in the future.

---


### 60. [Rubric-Aligned Disentangled Evaluation of Human Simultaneous Interpreting](https://arxiv.org/abs/2609.11131)

**<font color=#1a73e8>作者：</font>** Ziyu Zhang, Satoshi Nakamura  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human simultaneous interpreting (SI) is commonly assessed with analytic rubrics separating meaning transfer, delivery quality, and temporal synchrony, yet no automatic metric is designed for rubric-aligned segment-level SI evaluation. We construct a professionally annotated corpus of 1,101 SI segments with scores for meaning transfer (LQ), delivery quality (EXP), and perceived latency (LAT). We show that structured LLM prompting and scalar supervision collapse rubric dimensions, yielding near-zero correlation with human ratings and strong cross-dimension coupling. To isolate supervision structure under identical backbone capacity, we introduce dual regression heads on a LoRA-adapted COMET-KIWI encoder. On a held-out talk-level test set, the model achieves Pearson correlations of 0.388 (LQ) and 0.301 (EXP), improving over frozen COMET-KIWI. Given low absolute rater agreement, we interpret results relative to human consistency and target stable ranking signals for formative assessment.

---


### 61. [Phase-Decoupled, Model-Calibrated Power Control for Disaggregated LLM Serving](https://arxiv.org/abs/2609.11133)

**<font color=#1a73e8>作者：</font>** Jae Gon Kim, Donghoon Yoo, Hanyul Ryu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Datacenter GPU power is the binding constraint on LLM serving capacity, and production serving has shifted to prefill/decode (PD) disaggregation. Deploying NVIDIA's Max-Q inference profile on a disaggregated B200 system, we found its realized gain modest (+8.6% tokens/J), model-dependent, and carrying a mean end-to-end latency cost (+5.2%) that throughput-only evaluation does not surface; the profile also applies one setting to prefill and decode GPUs that operate in opposite hardware regimes. We hypothesize that the optimal power setting is a property of the deployed (model, quantization, engine, hardware) combination rather than of the GPU class, that each lane warrants its own profile, and that converting SLO headroom into energy safely requires latency-gated calibration under a runtime SLO guard rather than a fixed recipe. We present a phase-decoupled, model-calibrated controller: the prefill lane runs under an SM-clock window whose floor is a latency guarantee by construction, and the decode lane under a power cap placed by automatic calibration just above a measured throughput/latency cliff. Because a disaggregated decode lane draws flat, memory-bound power, the cap binds continuously, the reactive-overshoot weakness that led POLCA to reject capping is absent, and the GPU's own power manager retains throughput under the cap. On an 8x B200 node serving Qwen3-Coder-480B (FP8) under agentic load, our balanced mode delivers +20.4% tokens/J at +3.5% mean e2e versus +8.6% at +5.2% for Max-Q, a Pareto improvement on both axes. On Qwen3-235B-A22B (NVFP4) every operating mode meets the ITL-p99 SLO in every repetition; both vendor profiles miss it. A decode-actuator A/B shows the calibrated cap beats static clock locks, and a three-day sustained run saves 32.3% of a lane pair's electricity. Both models are MoE; a dense model recovers roughly 5x less, so we scope our claims to MoE serving.

---


### 62. [Bidirectional Multimodal Fusion of Sky Images and Time-Series for Solar Forecasting with Large Language Models](https://arxiv.org/abs/2609.11135)

**<font color=#1a73e8>作者：</font>** Ken Chen, Maneesha Perera, Wei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Short-term photovoltaic (PV) power and global horizontal irradiance (GHI) forecasts are essential for effective dispatch, reserve scheduling, and grid operations. At these forecasting horizons, errors are predominantly driven by cloud induced ramps: relying solely on historical numerical data may struggle to anticipate an incoming cloud, making ground-based sky images a crucial complementary physical signal. Furthermore, forecast performance is highly sensitive to location and local observing conditions, creating a strong need for site-specific data that are often scarce. Recently, large language models (LLMs) have demonstrated competitive performance and high data efficiency in time-series forecasting. Despite their success, existing LLM-based forecasting methods remain predominantly unimodal, relying primarily on historical numerical time-series data. Effectively incorporating sky imagery into an LLM-based forecasting framework remains under-explored and an open challenge. In this paper, we propose SolCloudLLM, an LLM-based multimodal forecasting framework. SolCloudLLM aligns sky-image patches with time-series patches and fuses their corresponding representations through bidirectional multimodal fusion, yielding a unified representation that is subsequently mapped into the embedding space of an LLM. Extensive experiments on the SIRTA and SKIPP'D datasets demonstrate that SolCloudLLM consistently outperforms the best baseline methods in MSE across all forecasting horizons, achieving a maximum relative MSE reduction of 25.4%. Stratified analysis further indicates that the benefits of multimodal fusion are concentrated primarily under cloudy conditions. Notably, SolCloudLLM achieves the best performance in nearly all few-shot settings, whereas other deep learning baselines experience substantial performance degradation and are frequently outperformed by the non-learning physical method.

---


### 63. [The Machines Are Calling: Measuring Automated and Synthetic Voices in Unwanted Inbound Calls](https://arxiv.org/abs/2609.11137)

**<font color=#1a73e8>作者：</font>** Xingyu Shen, Tommy Duong, Muduo Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In February 2024 the U.S. Federal Communications Commission (FCC) placed AI-generated voices under the Telephone Consumer Protection Act (TCPA). Yet no peer-reviewed measurement says how much unwanted call traffic is placed by a machine, or how much of that machine speech is synthesized rather than played from a recording. We report both with a disclosed pipeline. An interactive voice honeypot (language-model personas on real U.S. numbers, the caller recorded on its own track) recorded 10,987 calls over 66 days; 11 days on which our stack answered silently are set aside. Three instruments read each opening: an audio fingerprint that finds the same recording played on other calls, a commercial synthetic-speech detector on the caller's first ten seconds, and blinded listeners who check what it flags. Of the 7,233 calls our persona greeted on normal days, 13.8% open with a recording we also heard on another call, and 13.1% with fresh audio the detector labels synthetic. A further 9.9% open with a caller who never spoke after our greeting, 54.2% with fresh audio the detector labels human, and 9.0% could not be scored. Machine-voiced openings are therefore at least 26.9%, a further tenth of calls are silent connections we read as machine-placed, and replays of a recording make up 45% of the detector's own rate (29.3% of 6,192 scored openings). The same waveform played on two calls lands on opposite sides of the detector's threshold 13.6% of the time, and eleven listeners confirm 54.4% of what it flags. Synthetic openings concentrate in lead-generation spam (33.8%), not fraud (21.1%); 0.44% disclose automation. Prevalence tracks how long a bait number has circulated (59% against 19% in the same weeks): seeding history, not calendar time, explains the trend. Campaigns outlast their numbers: one recorded compliance notice opens calls in six campaigns, and one synthetic voice serves nine.

---


### 64. [Can LLMs Normalize Databases? A Benchmark and Multi-Agent Framework for Schema Normalization](https://arxiv.org/abs/2609.11141)

**<font color=#1a73e8>作者：</font>** Dong-Jae Koh, Huisu Kim, SeongHwan Yoon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used to generate structured outputs, but their reliability remains unclear when those outputs must satisfy database-level constraints. We study this issue through database normalization, involving reasoning about functional dependencies, lossless join decompositions, and inter-table constraints. We introduce a Database Normalization Benchmark (DNBENCH), comprising 3,275 samples for evaluating LLM-driven database normalization from 1NF to BCNF. DNBENCH uses a three-axis protocol to measure semantic equivalence, structural accuracy, and logical validity. Across Single, Complex, and Real World levels, DNBENCH uncovers recurring failures in dependency inference, schema decomposition, and inter-table constraint reconstruction. We further propose Multi-Agent Reasoning for Schemas (MARS), which separates evidence extraction, violation diagnosis, and decomposition planning from schema generation and verification. MARS improves the DNB-SCORE by 82.0% over the single-prompt baseline. All artifacts will be released upon acceptance.

---


### 65. [Same Day, Same Story; One Day Ahead, a Different Signal: The Dual Validity of Financial Sentiment](https://arxiv.org/abs/2609.11144)

**<font color=#1a73e8>作者：</font>** AS Aravinthkakshan, Laven Srivastava, Harsh Nandwani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial NLP has a standard workflow: validate a sentiment tool against human labels, then trust it to extract market signal. This assumes the two evaluations measure the same thing. We test that assumption in a setting where both can be measured at once: a corpus of securities class actions (2002-2025) linking 70,500 X messages to abnormal stock returns, with a single-annotator human labelled gold sample. Running five instruments (VADER, Loughran-McDonald, FinBERT, Twitter-RoBERTa, and an LLM annotator) through one identical pipeline, we find that the relationship between construct and predictive validity depends on the sampling convention and score representation. Under conventional method-specific sampling, human agreement aligns more closely with graded same-day associations than with one-day leads. On a fixed-n panel, however, agreement has similar graded rank correlations at both horizons, while the coarse ordering remains weak. Benchmark agreement therefore establishes semantic validity but does not by itself determine predictive rankings. In a conversation that is 17.6% spam, message volume predicts neither market damage nor settlement size.

---


### 66. [The Oligarch Barely Steers Model Collapse in Multi-Model Ecosystems](https://arxiv.org/abs/2609.11146)

**<font color=#1a73e8>作者：</font>** Yangze Liu, Zhongyi Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-generated text is flowing back into the training corpora of the next generation of models. Recursive training on it drives model collapse, and recent work extends the setting to many models feeding one another -- but almost always with the market split evenly, while real generative AI is an oligopoly. Concentration raises two worries: fewer, more uniform sources may make collapse faster, and later models may be dragged toward the oligarch's output. We test both in controlled ecosystems: 13 open 1--4B models form natural ecosystems of 3 to 13 players, plus an injected probe that pushes the top share to 90%; each generation, every model's output is mixed into a shared pool by market share and every model is retrained on that pool from clean base weights, for five generations. Yet within the range we test, neither worry materializes; what emerges instead is an invariance. Making the split more unequal barely changes the speed of collapse. Destinations move even less: the share and identity knobs shift five-generation endpoints by only a few percent of the drift common to all arms -- the ecosystems collapse to nearly the same place. An extreme share paired with the strongest injected bias still does not guarantee steering, and the topic shifts it does produce leave only a faint trace on the ruler that measures collapse. What sets the speed is who supplies the pool and how readily those suppliers are carried along: with every share held fixed, swapping the members of a K=3 ecosystem changes five-generation drift by 2.8x; a share-weighted index of each member's susceptibility explains the speed differences across nineteen arms with R^2 = 0.68; and replacing half the pool with human text roughly halves drift without changing its course. Within the tested range, concentration sets neither the destination nor the pace of collapse; the pace follows whose text fills the pool.

---


### 67. [A Fragility Spectrum for Recursive Language-Model Training](https://arxiv.org/abs/2609.11149)

**<font color=#1a73e8>作者：</font>** Yangze Liu, Zhongyi Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model-generated text is finding its way back into training corpora, and there is plenty of evidence that training on such data over and over collapses output diversity. Prior work has studied the phenomenon itself: which protocols and which data mixtures cause collapse. But different models behave very differently under the same process. We fix one recursive contamination protocol and let 13 publicly released checkpoints form an ecosystem that shares a common corpus for five generations. The unique 4-gram outcome after five generations ranges from 0.187 to 0.940 across checkpoints, a roughly five-fold spread: some models are barely touched, others degenerate into repetitive fragments. Changing the composition of the shared pool or mixing in human text keeps the Spearman correlation of the ordering at 0.91--0.97, and changing the random seed keeps it at 0.93--0.98. Whether a model collapses easily under recursive training is, then, a property of the checkpoint itself, and one that has gone largely unexamined. Parameter scale alone does not explain it, since a three-size ladder within one family is not monotonic in size, and none of the static indicators we tested predicts it either. What does work is cheap: let a model iterate on its own output for two or three generations, and its fragility in the larger ecosystem can be inferred from that alone. Collapse speed also responds to intervention. Tightening top-p, which cuts the low-probability tail at generation time, nearly stops collapse within three generations and stabilizes six checkpoints spanning the whole spectrum together, while data-side filtering slows collapse without stopping it.

---


### 68. [LILA: Calibration-Free Structured Pruning of Large Language Models via Latent Spectral Geometry](https://arxiv.org/abs/2609.11163)

**<font color=#1a73e8>作者：</font>** Sankar Behera, Dhruv Singh, Anshika Agnihotri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured pruning of large language models (LLMs) offers hardware-efficient compression, yet existing methods require calibration data, gradient computation, or large auxiliary policy networks at pruning time. LILA (\emph{Latent-Informed Layer Analysis}) scores neuron importance via the Kolmogorov--Smirnov (KS) distance between empirical singular value distributions of the full and neuron-ablated feed-forward network (FFN) weight matrix, providing a closed-form spectral rule requiring no training, calibration data, or auxiliary network. Without any fine-tuning, LILA surpasses PruneNet (45M-parameter RL policy) by 1.57~pp in zero-shot accuracy on LLaMA-2-7B at 25\% sparsity, and outperforms WikiText-2-calibrated SliceGPT by up to 6.0~pp across all sparsity levels, while preserving the original architecture. After one epoch of LoRA recovery fine-tuning, LILA achieves highly competitive performance, matching the heavily calibrated SliceGPT baseline to within a 0.48~pp margin across LLaMA-2-7B and Phi-2, despite using zero calibration data. A Neural Tangent Kernel analysis confirms a 22$\times$ reduction in functional distortion versus random pruning, providing theoretical grounding for the spectral importance criterion. Finally, extending LILA to dynamically allocate sparsity budgets via KS-scores yields state-of-the-art generative preservation at moderate compression, while uncovering fundamental single-layer architectural bottlenecks at higher compression regimes.

---


### 69. [SemVerBench: Benchmarking LLM Comprehension of Version-Constraint Resolution Semantics](https://arxiv.org/abs/2609.11180)

**<font color=#1a73e8>作者：</font>** Qibai Chen, Zeming Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) coding agents constantly decide whether a version satisfies a constraint such as ^1.2.3 or >=2.0,<3, yet their grasp of version-constraint semantics has never been measured directly. We introduce SemVerBench, the first benchmark of LLM version-constraint resolution semantics across three ecosystems (npm, PEP 440, Cargo): 240 machine-checkable items with unique answers, built author-neutrally from four balanced sources (each ecosystem's official test suite plus three frontier LLM proposers) and labeled by a non-circular two-implementation oracle. Evaluating six frontier models, we find systematic, predictable per-mechanism blind spots: a partial-comparator carry rule (>1.2 means >=1.3.0) traps every model on Cargo (near 60%), and although standard PEP 440 prefix matching is universal, on zero-pad/post-release corner cases GPT-5.1 collapses (0/26) while Claude stays at 97-100% (verified on a 67-item oracle-validated set). Opus significantly outperforms all other models, and Sonnet outperforms the OpenAI models (McNemar). The failures look more like an activation/application gap than a knowledge gap: injecting the rule or a light correct hint recovers most errors, whereas interval decomposition does not, and models are at ceiling on the basic forms of the same rules. An author-stratified analysis finds no statistically significant self-favoritism. Because the task is verifiable and a free, 100%-correct resolver exists, tool delegation reaches ~100%: coding agents should delegate version resolution to a resolver rather than reason about versions in-head.

---


### 70. [Can LLMs Follow Medical Expert Logic? A Benchmark for Hierarchical Logical Consistency in Risk-of-Bias Assessment](https://arxiv.org/abs/2609.11185)

**<font color=#1a73e8>作者：</font>** Jiayu Huang, Zichen Tang, Qianhui Ling 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evidence-based medicine demands strict logical consistency, yet current evaluations of large language models (LLMs) prioritize superficial label matching over genuine reasoning. We introduce LogiMed-RoB, a benchmark grounded in Cochrane Risk of Bias (RoB) 2.0 expert logic, comprising 860 randomized controlled trials (RCTs) and 14,820 queries. It evaluates models under the Hierarchical Logical Consistency (HLC) framework across four dimensions: Atomic Consistency, Domain Consistency, Aggregation Consistency, and Evidential Faithfulness. Experiments on 10 state-of-the-art LLMs reveal a catastrophic Error Compounding Effect: despite the top model reaching 98.88% Atomic Consistency, its end-to-end consistency collapses to 45.13%, with several open-weight architectures plummeting to nearly 0%. We further uncover a systematic evidence-reasoning gap: even when models retrieve high-quality evidence, they fail to deduce correct outcomes in 18.63-40.05% of cases, while Blind Guess Rates reach 48.28%. LogiMed-RoB demonstrates that high outcome accuracy can conceal critical reasoning flaws, underscoring the necessity of white-box logical verification for clinical deployment.

---


### 71. [Agentic Share-of-Search: A Multi-Agent AI System for Competitive Decision-Making in LLM-Mediated E-Commerce](https://arxiv.org/abs/2609.11190)

**<font color=#1a73e8>作者：</font>** Spandan Ghose Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI shopping assistants increasingly redirect consumer discovery, creating an urgent need for tools that support seller-side competitive decision-making. We present a multi-agent AI system that automates competitive visibility measurement and root cause diagnosis in LLM-mediated ecommerce. The system introduces Agentic Share-of-Search (ASoS) as the decision target, deploys query agents across leading AI platforms, and uses a ReAct-based diagnostic agent to recommend prioritized merchandising interventions. A 100-trial ablation study, presented as a feasibility evaluation of this prototype, shows the agent recovers the ablated signal in 39% of trials (95% CI: 30.0% - 48.8%, 5.5x over chance), rising to 63.9% among high-correlation ablations.

---


### 72. [FlexComp: One Model for Every Ratio in Context Compression](https://arxiv.org/abs/2609.11192)

**<font color=#1a73e8>作者：</font>** Kaiyan Zhao, Zhongtao Miao, Akiko Aizawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Soft context compression condenses a context into a few memory tokens that a frozen LLM consumes in place of the raw text, but existing compressors fix the compression ratio at training and inference: each deployed ratio requires a separately trained model, and the chosen ratio is applied uniformly to all inputs, whose actual needs vary drastically. We propose FlexComp, a method-agnostic framework that decouples the ratio from both training and deployment: Matryoshka-style training samples the memory budget $K$ per instance, turning one model into an any-ratio compressor, and the budget is then chosen per input by: (1) confidence-based cascade routing or (2) a lightweight learned $K$ predictor. Across ICAE, 500xCompressor, and SAC on MRQA, a single FlexComp model matches separately trained fixed-ratio specialists with minimal degradation. Cascade routing preserves over 98% of the mildest ratio's accuracy at up to 266x average compression; the $K$ predictor, in a single compression-decoding pass, reaches 158-236x within 0.7 F1 of the mildest ratio. At serving-scale batch sizes, the $K$ predictor cuts context KV cache by 50% and improves decoding throughput by 47%.

---


### 73. [An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning](https://arxiv.org/abs/2609.11199)

**<font color=#1a73e8>作者：</font>** Muhammad Fahad Bashir, Muhammad Afzal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the existing digital mental health tools specifically developed for Western settings, Pakistani students are exposed to a uniquely compounded stress situation in their university that includes academic, financial, familial, and relational stressors, which have become a serious concern for academic and psychological development of students in Pakistani universities. This paper introduces a new, AI-driven and culturally sensitive stress detection and wellness support system that is tailored to the context of Pakistani university students. The system is based on a machine learning model called Random Forest which is trained using a validated student stress data set of 1100 responses on 20 features from psychological, physiological, academic, environmental and social aspects, with an accuracy of 89.09% and a macro F1-score of 0.89, in three stress severity levels. The classification outputs are passed on to an open-source large language model through OpenRouter API, where an appropriately crafted system prompt, culturally aware, gives the model a conversation about wellness, in English, Urdu and Roman Urdu. The second most predictive stress factor in this population identified by feature importance analysis was teacher-student relationship, which is a culturally important stress factor highlighting the need for region-aware mental health systems. Future research will involve primary data collection from students at various academic levels of Pakistani Universities with the validated DASS-21 instrument focusing on the students who are moving from FSc to undergraduate studies, which is a time of being psychologically vulnerable which is under-researched.

---


### 74. [REVA: Reusable Evidence View Aggregation for Context-Efficient RAG Serving](https://arxiv.org/abs/2609.11209)

**<font color=#1a73e8>作者：</font>** Tuan Nguyen, Qiran Hu, Banruo Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) improves knowledge-intensive large language model (LLM) applications by conditioning generation on retrieved documents, but longer contexts increase latency, key-value (KV) cache memory, and token cost. Post-retrieval compression can reduce this cost, yet existing compressors often operate independently for each query, rely on auxiliary models or rewriting, and introduce online overhead that can offset the benefit of shorter prompts. We revisit RAG compression from a data-mining perspective by aggregating historical query--document--model interactions into reusable evidence views. We first show that modern compressors have unstable gains over simple truncation and can add substantial inference-time latency. We then propose Reusable Evidence View Aggregation (REVA), a framework that mines the target generator's historical attention traces into a document-keyed, budget-agnostic score store. REVA maps token-level attention to readable word units, aggregates importance across repeated document accesses, and renders budget-specific plain-text views that preserve document order and the standard RAG interface. Across four representative benchmarks and modern LLMs, REVA improves generation quality by 1.0--5.8 points over existing advances, while reducing compression overhead by a factor of 5.3 to 15.6, adding less than 40 ms of latency.

---


### 75. [Legible Failures: Detecting and Repairing In-Context Binding Errors](https://arxiv.org/abs/2609.11216)

**<font color=#1a73e8>作者：</font>** Manas Venkata Sai Ravulapalli, Samrath Singh Chadha, Abhinav M. Hari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A wrong answer does not show whether the model lacked the needed information or held it and failed to use it. On an entity-obligation binding task, a language model can emit an incorrect prompt-supplied binding while a linear probe can recover the correct one from its frozen hidden state. We measure how often this occurs across 16 public checkpoints, each evaluated with three seeds. We fit a probe on a training fold, select its layer on a validation fold, and report results on a disjoint test fold. On the trials each model gets wrong, probe accuracy exceeds the strict present-obligation baseline, 1/K = 0.125, by +0.196 (95% CI [+0.101, +0.296], bootstrapped over models). A query-entity counterfactual rules out token presence and recency. A score built from the sign of probe-output disagreement improves failure detection over the model's own confidence by +0.079 AUROC (95% CI [+0.036, +0.126]). Raw probe confidence gives no measurable improvement over model confidence. Steering the residual stream toward the probe-decoded binding, with no gold label, raises accuracy on all eight models tested by a mean of +0.168 (95% CI [+0.066, +0.280]). Where recent studies report that probe-detected errors are resistant to interventions, we find that in-context binding is a setting in which probes are actionable.

---


### 76. [AI Soccer Analyst: Stage-Aware and Verifiable Human-AI Collaboration for Soccer Data Analysis](https://arxiv.org/abs/2609.11224)

**<font color=#1a73e8>作者：</font>** Calvin Yeung, Keisuke Fujii  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Sports data analysts translate domain questions into insights by combining computation with sport-specific domain expertise. Large language models ease programming, but prompt-to-report workflows may obscure decisions and evidence. We present AI Soccer Analyst, a mixed-initiative system with revisable stages: Data Understanding, Problem Definition, Structured Planning, Execution, Evidence-Grounded Reporting, and Interaction and Refinement. A formative study with five analysts first informed design goals for automation, verifiability, human control, and accessibility. Subsequently, a task-based evaluation with 16 participants combined system logs, retained artifacts, ratings, and open responses; 33 of 48 tasks met the operational completion criteria. Exploratory tests supported favorable participant perceptions of completed-task output quality, task achievement, reliability, and verifiability after Holm correction. Interaction records showed domain knowledge emerging through clarification, planning, and refinement. These findings position stage-aware human-AI collaboration as a practical approach for producing inspectable, revisable, and verifiable analyses while retaining domain-expert involvement in consequential decisions.

---


### 77. [A Voice-Interactive Multi-Agent System for Smart Operating Rooms: Architecture Design and Key Technologies](https://arxiv.org/abs/2609.11231)

**<font color=#1a73e8>作者：</font>** Tianxiang Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents SurgicalRoomAgent, a voice-interactive multi-agent system for smart operating rooms based on large language models (LLMs). The system achieves natural language understanding, device control, intraoperative recording, and surgical report generation through a layered architecture comprising a voice interaction pipeline (wake, ASR, turn detection, agent reasoning, TTS) and an agent core (skill registry, task planner, device manager). Three key technologies are investigated: (1) KV Cache prefix warming for low-latency inference, reducing recomputation overhead from approximately 500 ms to tens of milliseconds via byte-level Longest Common Prefix reuse; (2) streaming partial JSON parsing with early parallel task execution, reducing end-to-end latency by approximately 30%; and (3) progressive skill prompt disclosure, which dynamically filters system prompts based on user role, connected devices, and surgical phase to maximize information density within limited context windows. The system is implemented using the Qwen3-27B model with this http URL inference engines. Experimental analysis demonstrates effective operation within a 16,384-token context limit and multi-device parallel control response times meeting OR real-time requirements.

---


### 78. [NovGauge: A Fine-Grained Benchmark for Diagnosing LLMs' Capability in Paper Novelty Assessment](https://arxiv.org/abs/2609.11234)

**<font color=#1a73e8>作者：</font>** Guoqiang Zhang, Kexin Tan, Ming Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in peer review at major AI conferences, yet novelty remains a persistent weak point. Existing benchmarks assess novelty as a single holistic score, making it difficult to diagnose which dimension a model misjudges or whether its evidence is faithful. We present NovGauge, a human-anchored benchmark for fine-grained novelty assessment diagnosis. The benchmark contains 619 paper pairs and 50 multi-paper sets, drawn from two expert sources: ICLR reviewer overlap claims and survey co-citations. Instances are independently labeled along three dimensions: task, problem, and method, capturing application goals, technical challenges, and solution approaches. We propose a cascading diagnostic pipeline that verifies per-dimension correctness, evidence grounding, and logical support. Evaluation of 18 LLMs shows hallucination rates ranging from 0% to 39% across dimensions, and among non-hallucinated correct-positive judgments, over 70% cite evidence fails to logically support the stated reason. The best-performing model, GPT-5.5, achieves 43-72% Verified F1 across dimensions, while most models retain less than half of their raw F1 after faithfulness verification. These results suggest that current LLMs remain far from reliable scientific novelty assessment, particularly when correctness is conditioned on faithful evidence grounding.

---


### 79. [HALDETECT at ImageEval 2026 Shared Tasks: Answer-First Contrastive Grounding with QLoRA](https://arxiv.org/abs/2609.11236)

**<font color=#1a73e8>作者：</font>** Syed Mohaiminul Hoque, Md Sakhawat Hossain  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large multimodal models tend to hallucinate visual detail fluently, which limits their deployment for fine-grained interpretation. We present HALDETECT, our system for the English hallucination-detection track (Task 1b) of ImageEval 2026, in which a system must identify, from an image and three culturally plausible statements, the single visually grounded one. We frame the item as one contrastive decision, emit the answer before its explanation, and structure reasoning around colour/texture, shape/form, and context. Our best submitted adapter fine-tunes Qwen2.5-VL-7B-Instruct with 4-bit QLoRA while freezing the vision encoder and reaches Contrastive Instability (CI) 0.035 on the 1,000-item test set; we placed third of eight teams. Development experiments show that answer order can matter more than model scale and that adaptation beats prompting alone. Retrospective paired analysis of the released gold labels confirms the QLoRA gain over the best prompt but not the small gap between the devtest-selected and best-test adapters, and reseeding all four training sizes shows that the apparent data-scaling curve does not survive a seed change. The 35 residual errors are culturally plausible function, material, and recognition distinctions; naive adapter voting does not help.

---


### 80. [From Evaluation to Enhancement: Benchmarking and Improving Think-with-Video Reasoning for Video Generative Models](https://arxiv.org/abs/2609.11242)

**<font color=#1a73e8>作者：</font>** Meng Luo, Yicheng Liu, Jiahao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation has advanced to produce visually compelling and temporally coherent results. Yet, whether these models can genuinely think with video--executing symbolic rules, respecting physical laws, and pursuing intentional goals--remains an open question. Existing benchmarks only partially address this, often conflating visual quality with cognitive correctness. We introduce VWG-Bench (Video World Generalist Benchmark), a comprehensive benchmark spanning 9 reasoning dimensions and 38 fine-grained tasks. To enable precise diagnosis, we design a three-level VLM-as-Judge protocol that independently assesses video-level fluency, task-level rule adherence, and sample-level goal realization. Evaluations of leading models reveal a striking gap: while models achieve strong rendering scores, they consistently fail on logic-heavy and rule-constrained tasks. To address this, we propose Vid-PRE (Video Prompt Reasoner and Enhancer), a model-agnostic prompt rewriter that offloads the cognitive burden of reasoning to a dedicated VLM. Trained via reinforcement learning with purely text-based rewards, Vid-PRE produces concise, constraint-aware prompts without the instability of video-level reward signals. Experiments show that Vid-PRE yields substantial reasoning improvements across multiple generators without architectural modifications. Together, VWG-Bench and Vid-PRE offer a rigorous diagnostic lens and a scalable path toward true think-with-video capabilities. All data and code are publicly available at this https URL.

---


### 81. [OmniHallu: Unified Hallucination Detection for Cross-Modal Comprehension and Generation in Multimodal Large Language Models](https://arxiv.org/abs/2609.11244)

**<font color=#1a73e8>作者：</font>** Jianjiang Yang, Peihang Li, Shanqing Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) have achieved remarkable progress across diverse tasks, they suffer from hallucinations where generated outputs contradict or misrepresent input semantics. Existing research typically addresses hallucination detection within a single modality or task type, limiting generalizability. We introduce OmniHallu, a unified hallucination detection framework spanning both comprehension and generation tasks across image, video, and audio modalities. We contribute OmniHallu-Bench, a 10,000-sample benchmark with claim-level human annotations covering six cross-modal tasks: image-to-text (I2T), video-to-text (V2T), audio-to-text (A2T), text-to-image (T2I), text-to-video (T2V), and text-to-audio (T2A). Our multi-agent architecture decomposes model outputs into atomic claims, verifies them through modality-specific experts, and aggregates evidence via structured reasoning. We further propose a preference-optimized trainable verifier that approximates the multi-agent decision boundary, reducing expert calls by 66% with minimal performance loss. Extensive experiments reveal a consistent modality-dependent performance gradient and provide fine-grained insights into cross-modal hallucination patterns.

---


### 82. [MUtE: A Dual Framework for Concept Erasure and Counterfactual Interventions](https://arxiv.org/abs/2609.11253)

**<font color=#1a73e8>作者：</font>** Antoine Saillenfest  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Erasing concept-specific information from representations has been proven useful for mitigating bias or interpreting model decisions. The joint objective is to transform the original representations such that the target concept becomes unpredictable, while maximally preserving concept-unrelated information. In this work, we revisit the optimal bounds of concept erasure to derive a novel class of erasure functions that naturally induce a deterministic, dual counterfactual mapping. Bridging the gap between theoretical optimality and practical representation learning, we design an implementation that imposes a translational bias on counterfactual trajectories - a constraint that aligns with how many concepts geometrically manifest in modern language models. Our framework enables seamless navigation between concept erasure and counterfactual generation. We empirically demonstrate its efficacy in improving downstream algorithmic fairness and generating counterfactual texts.

---


### 83. [Off-Target Effects of Response-Style Alignment in a Korean 27B Language Model](https://arxiv.org/abs/2609.11291)

**<font color=#1a73e8>作者：</font>** Hyojung Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We post-train Qwen3.8-27B for Korean response style -- verbosity, list and markdown usage, discourse structure and register -- and measure two behaviours the objective never targets: abstention on ambiguous social questions in KoBBQ, where the benchmark-correct answer is UNKNOWN, and unprompted disclosure in securities guidance. Both move, and the changes are expressed primarily through the model's emission policy: how often it answers and how much it says.
Matched target-form controls show that answer propensity depends on the training target, not the prompt set or recipe alone. Holding prompts, recipe, data volume and serving fixed and changing only the target text, three style seeds give positive answer-rate point estimates (mean +0.82 pp) and three neutral seeds negative ones (mean -1.53 pp); the observed seed ranges do not overlap and the means differ by 2.34 pp. A length-matched arm lies between them, and a fourth arm that stays short while preserving hedging is unstable across seeds, so which feature of the form is responsible is unresolved.
For absolute stereotyped exposure the decomposition into an answer-propensity term and a conditional-composition term is an algebraic identity, not a finding; its empirical content is where the movement went. Across the trained checkpoints the changes are dominated by answer propensity while the composition term stays small, and because that term is evaluated on treatment-dependent answered subsets we do not read it as evidence about latent preference.
Two measurement results follow. A between-arm contrast in conditional stereotyped share does not identify a change in conditional content preference when answer status is treatment-dependent. And agreement between two rule detectors for the same construct runs from 0.44 to 0.99 depending on which checkpoint produced the text -- observable without any reference labels.

---


### 84. [Memory Compression for High-Fanout Agent Sandboxes](https://arxiv.org/abs/2609.11294)

**<font color=#1a73e8>作者：</font>** Mengming Li, Ceyu XU, Qijun Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-fanout agent workloads create a growing memory bottleneck because a single task may spawn many concurrent sandbox sessions. Yet these sandboxes are far from independent: they originate from a shared template and execute related trajectories, exposing substantial template-relative and cross-sandbox memory redundancy. Conventional memory compression is poorly matched to this setting in three fundamental dimensions: how to compress, because they fail to exploit similarity across non-identical sandbox pages; what to compress, because they control page-fault overhead through conservative page selection; and when to compress, because compression is either triggered by memory pressure or performed without awareness of agent execution phases.
We present AgentZip, the first memory compression system designed specifically for AI-agent sandboxes. AgentZip introduces compression mechanisms that exploit both the template-relative and cross-sandbox redundancy. It broadens the compression scope to any page with a profitable representation and shifts overhead control from compression-time page selection to restore-time prefetching. It further aligns expensive compression with LLM waiting periods to avoid interfering with foreground tool execution. Across LLM training and inference workloads, AgentZip reduces sandbox-owned memory by up to 8.7x, compared with 2.1x for the Linux configuration. Restore prefetching and agent-execution-aware scheduling reduce the slowdown of aggressive compression from as high as 3.1x to 1.40x while retaining nearly all of its memory-saving benefit.

---


### 85. [Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models](https://arxiv.org/abs/2609.11310)

**<font color=#1a73e8>作者：</font>** Gautam Rajendrakumar Gare, Siyi Li, Hewei Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address few-shot object detection with vision-language models (VLMs) in out-of-domain settings such as aerial, industrial, and medical imagery, using only ten annotated images for supervision. Existing adaptation methods are discrete prompt optimization and LoRA fine-tuning. We revisit a third option: soft prompting, where a small number of continuous prompt tokens are optimized while the pretrained backbone remains frozen.
We identify two key design choices. First, placing prompt tokens at the cross-modal boundary between visual and text tokens outperforms other placements (10.0 vs. 8.4 mAP). Second, initializing prompts from the empty space token outperforms semantic and random initialization.
With these choices, one to three learned tokens (7,168 parameters on average) match the best LoRA configuration on Roboflow20-VL (14.2 mAP, 10-shot) while training over 20,000x fewer parameters. Soft prompting remains harder to optimize, exhibiting higher variance across random seeds. Unlike LoRA, however, it causes no forgetting: the LoRA rank matching our accuracy reduces NaturalBench VQA accuracy by 35% relative, rising to 56% at the largest rank, whereas soft prompting leaves pretrained performance unchanged.
The learned tokens behave like prompts rather than weights. They transfer to a newer model without retraining (+0.8 mAP on Qwen3.5-9B) and can be verbalized into readable prompts competitive with prompt-search methods (matching DetPO and outperforming GEPA).
The approach also extends beyond detection. On RoboCasa manipulation tasks, the frozen $\pi_{0.5}$ vision-language-action policy benefits from soft prompting, matching the LoRA baseline on two of three tasks when tokens are placed at the gradient bottleneck. These results suggest modern VLMs already encode much of what is needed for specialized domains; the challenge is learning how to ask.

---


### 86. [A Dynamic Fusion Large Language Model for Traffic Flow Prediction](https://arxiv.org/abs/2609.11314)

**<font color=#1a73e8>作者：</font>** Xue Qiu, Jianli Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic flow prediction is a core supporting technology for intelligent transportation systems. It uses historical data to infer future traffic dynamics in specific areas, thereby helping to alleviate congestion and improve resource allocation efficiency. Traditional neural networks struggle to break through accuracy limits due to their reliance on singular feature modeling, while large language models (LLMs) suffer from insufficient capture of spatial topological information and mining spatiotemporal correlation. This study proposes a Dynamic Fusion Large Language Model (DF-LLM) for traffic flow prediction. The model incorporates three core components: spatiotemporal embedding module, spatiotemporal fusion module, and LLM backbone. The spatiotemporal embedding module enables synergistic representation of multi-scale spatiotemporal features. The spatiotemporal fusion module integrates spatial topology and dynamic dependencies via graph convolution. The LLM backbone adopts a differentiated parameter adaptation strategy to balance training efficiency and traffic data adaptability. Additionally, it introduces a context aggregation attention module to strengthens global dependencies. More importantly, the LLM backbone takes the residual connections to mitigate the gradient vanishing in deep networks. Experiments show that DF-LLM has achieved better performance by comparing the metrics on all the four datasets.

---


### 87. [Routing by Reasoning Need: Trajectory-Aware Decoding Control for Diffusion Vision-Language Models](https://arxiv.org/abs/2609.11315)

**<font color=#1a73e8>作者：</font>** Yixiang Liu, Zhongxing Xu, Zhonghua Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion vision-language models generate answers through iterative refinement, exposing intermediate answer trajectories that can be inspected and controlled at inference time. However, this controllability creates a reasoning-need mismatch, where a universal generation length is applied to questions with different reasoning demands. Visually closed questions may be harmed by continued refinement after a stable answer has formed, whereas reasoning-sensitive questions may be harmed by premature commitment. We formulate this problem as reasoning-budget mismatch and study it in LLaDA-V. Rather than choosing a universal generation length, our training-free controller routes each example to early commitment, baseline preservation, or reasoning-supportive decoding using trajectory signals from answer closure, commitment evidence, and representation revision pressure, without using ground-truth answers. Across answer-focused, mixed-reasoning, and CoT-sensitive benchmarks, routed control improves robustness over fixed long decoding, pure short decoding, and single-rule interventions. The gains are not explained by shorter outputs alone. Answer-closed examples often benefit from commitment, whereas CoT-sensitive examples require preserving or supporting intermediate reasoning. Taken together, these results suggest diffusion VLM decoding should route inference-time control by the state suggested by the observed trajectory instead of relying on a universal decoding length.

---


### 88. [Magenta: Closing the Loop Between Mathematical Reasoning and Lean Verification](https://arxiv.org/abs/2609.11319)

**<font color=#1a73e8>作者：</font>** Joshua Ong Jun Leang, Haonan Li, Zheng Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most of mathematical knowledge has been communicated through so-called informal use of mathematics and natural language. With large language models (LLMs) being highly adept in using natural language, they achieve strong performance, yet not perfect, in informal mathematical reasoning. Restraining LLMs to informal reasoning misses out on the opportunity to use the discrete verification abilities that machines offer through machine-checkable proofs. In this paper, we bridge the gap between informal and formal reasoning by integrating Lean signals into the informal reasoning process. We introduce Magenta, a training-free agentic pipeline that, given only a natural-language problem, produces an answer, expresses it as a Lean 4 statement, and constructs a machine-checked proof. A statement judge verifies whether the formalisation preserves the original problem, while an error-attribution judge routes failed attempts either to mathematical re-derivation or local Lean repair. Magenta achieves 100% accuracy across all evaluated olympiad benchmarks, including AIME 2025, AIME 2026, and HMMT February 2026. When paired with the open-weight K2-Horizon-7B reasoner, it solves all six IMO 2026 problems. Our analysis shows that statement adjudication is essential for preventing false certificates and that feedback-guided correction outperforms independent resampling on difficult problems.

---


### 89. [E-CONAN (Entailment, CONtradition And Neutral) Benchmarks: Arabic Textual Entailment and Natural Inference Datasets](https://arxiv.org/abs/2609.11334)

**<font color=#1a73e8>作者：</font>** Khloud AL Jallad, Nada Ghneim, Ghaida Rebdawi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural Language Inference processes pairs of sentences to extract their semantic relations. NLI has been a hot research topic, integrated as a main component in other NLP applications. Despite significant advancements in textual inference across various languages all around the world, Arabic language still suffers from limited resources in this domain. To address this gap, this paper introduces E-CONAN benchmarks that are composed of sentences pairs from various sources: (1) automatically-translated pairs, (2) human-validated machine-translated pairs, (3) hand-crafted pairs from teaching Arabic as foreign language books, and (4) headlines pairs from different news channels containing rumors. E-CONAN contains two benchmark datasets, E-CONAN-2, a 2-way dataset (RTE) and E-CONAN-3, a 3-way dataset (NLI). Additionally, we have used E-CONAN benchmarks to evaluate 9 state-of-the-art multilingual pretrained models using zero-shot classification. Models were evaluated across the ArNLI, XNLI, and E-CONAN datasets. Results show that E-CONAN is a potentially valuable resource for evaluating model generalization and even for fine-tuning pre-trained models. Its diverse composition, derived from a combination of sources, offers a broader and more robust assessment compared to XNLI and ArNLI. In addition, we have evaluated 5 LLMs on E-CONAN-3 dataset. Moreover, we incorporated MARBERT as a representative Arabic-specific baseline and conducted performance evaluation comparison to demonstrate how Arabic-specific models scale against cross-lingual and LLM-based approaches on the E-CONAN benchmarks. Furthermore, we conducted detailed qualitative and quantitative error analysis to analyze frequent error patterns. E-CONAN benchmarks will be publicly available, we hope that it will enrich research community in Arabic textual entailment and natural language inference.

---


### 90. [On the Impact of Anonymization on the Performance of Large Language Models](https://arxiv.org/abs/2609.11335)

**<font color=#1a73e8>作者：</font>** Tobias Deußer, Max Hahnbück, Lorenz Sparrenberg 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models are increasingly deployed in sensitive domains, anonymizing input data to protect personally identifiable information has become a critical practice. However, the impact of this anonymization on model utility is not well understood. This paper presents a systematic empirical study of the trade-off between privacy and performance. We evaluate five prominent language models across eleven diverse benchmarks, comparing their performance on original versus pseudonymized inputs. Our results reveal that while anonymization generally degrades performance, the effect is highly nuanced. We find that more capable models, such as Qwen2.5-72B and GPT-4o mini, suffer the largest performance drops, suggesting a stronger reliance on specific entity information. The impact is also task-dependent: performance on TruthfulQA improves with anonymization, while retrieval-focused tasks like RGB experience a catastrophic decline. Further experiments show that reversible anonymization techniques that preserve entity uniqueness significantly outperform irreversible ones like redaction, and that explicitly prompting models about anonymization offers no discernible benefit. We conclude that anonymization is not a one-size-fits-all solution and must be co-designed with the model and task in mind to balance privacy and utility effectively. Our findings provide a crucial baseline for developing more robust, privacy-aware AI systems.

---


### 91. [SEAR: Segment-Evidence-Aware Routing for Weak-to-Strong Multilingual Speech MCQ](https://arxiv.org/abs/2609.11355)

**<font color=#1a73e8>作者：</font>** Huy Hoang Le, Long-Bao Nguyen, Minh Tri Dao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes our system for Task~2 of the second Multilingual Conversational Speech Language Model (MLC-SLM) Challenge. We adapt Qwen3-Omni-30B-A3B-Instruct with a segment-evidence-aware data and post-training pipeline. A language model converts timestamped ASR into coherent event spans, which are expanded by a boundary margin and cropped from the original recording. We then synthesize complementary semantic MCQs with Qwen3.6-27B and acoustic MCQs with Gemini~3.1 Flash-Lite, followed by structural, grounding, answer-consistency, and target-model trainability checks, yielding 359,825 verified MCQs across 21 language and accent variants. A text-only probe partitions the data into weak, text-answerable items used for supervised fine-tuning and strong, audio-dependent items used for reinforcement learning with Group Sequence Policy Optimization (GSPO), stabilized by debiased advantages, sequence-level importance correction, and dynamic filtering. Our system obtains 90.92% accuracy on the final official evaluation set.

---


### 92. [R4Tun: LLM-guided adaptive segmental tunnel lining segmentation in point clouds](https://arxiv.org/abs/2609.11360)

**<font color=#1a73e8>作者：</font>** Xinghui Tao, Zehao Ye, Guangming Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated inspection of segmental tunnel linings requires adaptive segmentation from 3D point clouds, yet expert-tuned pipelines often degrade when tunnel conditions vary. This paper presents R4Tun, a large language model (LLM)-driven adaptation framework that extends an expert-designed pipeline (SAM4Tun) with bounded parameter tuning informed by structured context: memory ($m$), state ($s$), and knowledge ($k$). Evaluated on 30 selected Seg2Tunnel subsets (13 regular, 17 complex) across three LLMs, the full $m+s+k$ design raised mean Intersection-over-Union (mIoU) from 0.18 to 0.43--0.48 and overall accuracy (OA) from 0.42 to 0.59--0.65 relative to the static SAM4Tun baseline, with the near-reference regular (staggered) subsets reaching mIoU 0.784--0.796 across LLMs. Across 270 (30 tunnels $\times$ 3 different LLMs $\times$ 3 context settings) runs, the LLMs showed similar parameter-adjustment trends (with overlapping 95\% CIs on mean gains) and consistently adjusted a shared set of critical parameters. These results support R4Tun as a controlled, label-free, cross-LLM adaptation mechanism in the tested SAM4Tun--Seg2Tunnel setting, demonstrating consistent accuracy gains; we position R4Tun as a mechanism contribution rather than a deployable final-inspection system, in which each bounded parameter change is auditable via logged rationales.

---


### 93. [Portable Semantics, Private Dialects: Reuse and Negative Transfer in Latent Communication Between Language-Model Cells](https://arxiv.org/abs/2609.11365)

**<font color=#1a73e8>作者：</font>** Narcis Marincat  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In shared-genome language-model societies, restricted evidence visibility favors reusable, value-indexed latent packet interfaces, whereas the sole high-performing globally visible model in the parent study learned an episode-entangled code. This companion study asks whether independently trained societies share one packet language, where strict zero-shot transfer fails, and whether inherited interface state helps or harms later learning. First, a leakage-controlled causal interoperability audit over all 30 ordered pairs of six independently trained restricted societies -- under sealed held-out structure and a preregistered raw/orthogonal/linear/nonlinear alignment ladder -- shows the six semantically similar interfaces do not form one raw language: one same-initialization pair is exactly interoperable in both directions, a second shows asymmetric partial compatibility, and all 26 cross-initialization directions fail every frozen alignment rung. Second, within the tested decomposition and a single sealed source formulation, a source-span control localizes strict zero-shot failure to interpretation and execution of the new operator instructions. Third, in a matched adaptation factorial, the globally trained communication interface acts as a severe negative-transfer prior: reinitializing only the packet reader, writer, and mouth raises final depth-three accuracy from 0.169 to 0.857. Fourth, across two restricted checkpoints and two independently frozen target streams each, inherited interfaces never exceeded fresh-interface controls by the preregistered 0.10 margin. All primary conclusions are bounded to a near-transfer 17-state setting; the negative-transfer factorial concerns one globally visible parent-cohort checkpoint, while an appendix adds a post hoc tagged-global twin case study.

---


### 94. [Beyond Confidence: Stability-Aware Test-Time Adaptation for LLM Reasoning](https://arxiv.org/abs/2609.11393)

**<font color=#1a73e8>作者：</font>** Bincheng Gu, Min Gao, Zongwei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation has emerged as a lightweight alternative to costly post-training for improving the reasoning capabilities of Large Language Models (LLMs) on downstream tasks. Predictive entropy provides a model-derived signal for such adaptation, guiding models toward higher-confidence reasoning states without external verifiers or reward models. However, higher confidence does not necessarily imply correctness, as LLMs may remain highly confident along incorrect reasoning trajectories. We observe that high-confidence reasoning is more likely to be correct when confidence remains stable under local perturbations. Based on this observation, we propose Test-Time Adaptation via Stability-Aware Confidence Optimization (TASCO), a framework that incorporates local stability into confidence-based test-time adaptation while keeping the LLM frozen. TASCO operationalizes local stability by optimizing a lightweight task-level prefix under two alternative perturbation strategies: Random Perturbation promotes distributional stability across trajectories induced by nearby perturbed prefixes, whereas Sharpness-Aware Perturbation targets worst-case local sensitivity. Experiments demonstrate that TASCO improves reasoning accuracy and token efficiency across diverse LLMs and reasoning benchmarks, while behavioral analyses show that it maintains stable confidence under local perturbations without prematurely concentrating the model's predictive distribution.

---


### 95. [TransClean: A Benchmark for Detecting and Extracting Clean Translations from Large Language Model Outputs](https://arxiv.org/abs/2609.11399)

**<font color=#1a73e8>作者：</font>** Shenbin Qian, Yves Scherrer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for machine translation, yet their outputs often contain additional text beyond the translation itself, such as language labels, explanations or bilingual repetitions, which we term translation noise. Despite its prevalence, this problem lacks dedicated benchmarks and systematic study. We analyze over 790,000 translation outputs from 12 LLMs across 22 language pairs (LPs) and identify 12 recurring noise patterns, which we group into formatting and content noise. Building on the observed patterns, we construct TransClean, a controlled benchmark of 9,900 pairs of noisy and clean translation outputs, comprising 8,800 synthetically generated instances and 1,100 manually curated authentic instances. We evaluate two extraction approaches on the TransClean benchmark: 1) a span-based extraction method leveraging translation quality estimation models for span detection, and 2) an LLM-based extraction method that prompts an LLM to isolate the translation. Our benchmark and analysis provide the first systematic framework to evaluate and improve the cleanliness of LLM translation outputs.

---


### 96. [SWRouter: Similarity-Contractive Window Routing for Multi-Turn Large Language Model Conversations](https://arxiv.org/abs/2609.11414)

**<font color=#1a73e8>作者：</font>** Yu Wang, Yuchen Li, Rui Kong 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit complementary strengths, motivating routing methods that dispatch each query to the most suitable model. Although existing routers are effective in single-turn settings, they do not directly transfer to multi-turn dialogue, where routing performance critically depends on how historical context is segmented, retained, and incorporated into the current prompt. This introduces two fundamental challenges: preventing information loss and information confusion during context construction, and evaluating routing quality without conflating model selection with prompt construction quality. In this paper, we propose SWRouter, a Similarity-Contractive Window Router for multi-turn large language model routing. SWRouter combines a similarity-based context segmentation mechanism for prompt construction with a dual-metric evaluation framework that decouples construction accuracy from router performance. Experiments on multi-turn dialogue benchmarks demonstrate that SWRouter consistently surpasses strong baselines, achieving a 16.26% improvement in evaluation accuracy over the best individual large language model and an additional 8.22% gain over the Conv-ID Context baseline. Our results highlight that multi-turn large language model routing requires a joint design of context construction and evaluation, rather than a direct extension of single-turn routing methods.

---


### 97. [LLMs as Post-hoc Auditors of Physiological Plausibility in Symbolic Regression: A Clinician-Evaluated Case Study](https://arxiv.org/abs/2609.11431)

**<font color=#1a73e8>作者：</font>** Jorge López-Varela, J. Ignacio Hidalgo, José-Manuel Muñoz 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Genetic Programming and its variants, such as grammatical evolution, are widely used in Symbolic Regression to derive mathematical expressions from multivariate data. In addition to predictive accuracy, models are appreciated for their potential to provide interpretability, offering explicit equations that relate input variables to outcomes. However, achieving interpretability and plausibility remains challenging, as evolved models may be complex or scientifically inconsistent. In this study, we explore whether Large Language Models, can assist in improving the explainability of Symbolic Regression models generated by evolutionary computation methods. Building upon our previous work on estimating body fat percentage using grammar-based Genetic Programming , we investigate the use of LLMs as post-processing tools to analyze and rank evolved expressions according to their interpretability and medical plausibility. Four symbolic expressions are analysed by three LLMs over three repeated runs, and the resulting interpretations and rankings are assessed by a panel of three clinicians. Across the three LLMs, comparative model-ranking outputs received more favorable clinician assessments than isolated term-level interpretations. However, the LLMs also produced physiologically and mathematically questionable explanations, indicating that they are better suited to comparative auditing under expert oversight than to autonomous validation.\blfootnote{The present work is an extended version of a paper submitted into a journal.

---


### 98. [Cross-Lingual Clinical Annotation Projection as Constrained Text Generation: A Six-Language Study](https://arxiv.org/abs/2609.11450)

**<font color=#1a73e8>作者：</font>** Álvaro Rey-Blanes, Francisco J. Moreno-Barea, Francisco J. Veredas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: To determine whether cross-lingual clinical annotation projection can be formulated as a text-preserving, document-level generative task that produces verifiable character-level annotations for multilingual clinical corpus construction, and to characterize its robustness and computational trade-offs relative to candidate-based projection pipelines. Methods: We developed a constrained LLM projection workflow that inserts entity tags directly into immutable target-language text, followed by deterministic validation and character-offset reconstruction. We evaluated it alongside supervised candidate-span projection and hybrid ML-LLM refinement for transferring Spanish Disease, Symptom, and Procedure annotations into six languages. Evaluation used MultiClinAI gold standard with strict span matching and character-overlap F1 Results: Direct LLM projection achieved the strongest and most consistent performance. GLM 5.2 obtained a mean Strict F1 of 0.9201 across 18 language-entity combinations, while locally deployable Gemma4:31B achieved 0.9133. The best LLM configuration improved Strict F1 over the previous state of the art in all 18 settings, by 0.0564-0.1512, yielding 55,416 grounded mentions with reconstructed offsets. Conclusions: Direct LLM-based projection enables high-quality multilingual clinical annotation transfer and provides a practical approach for extending clinical NLP resources to languages with fewer annotated datasets and language-specific tools. Combined with local inference and deterministic validation, it can substantially reduce expert time and cost for multilingual clinical corpus construction.

---


### 99. [RouteRepair: Instance-Level Failure Diagnosis and Targeted Repair in LLM-Based Automated Heuristic Design for Routing Optimization](https://arxiv.org/abs/2609.11452)

**<font color=#1a73e8>作者：</font>** Binghao Ji, Di Huang, Jiahui Fang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient routing optimization is essential to freight transportation, urban logistics, and shared mobility, where high-quality heuristics are often required under limited computational budgets. Recent large language model (LLM)-based automated heuristic design methods can generate effective routing rules, but aggregate evaluation may mask recurrent failures on particular instance structures. To address this limitation, this study develops RouteRepair, which diagnoses parent-specific weaknesses from instance-level performance and applies targeted modifications to the corresponding heuristic components while protecting behavior that already performs well. Routing evidence, solver behavior, and program context are combined to define bounded repair objectives, and each intervention is validated through matched parent-child evaluation of failure recovery and collateral degradation. Experiments on the traveling salesman problem (TSP) and capacitated vehicle routing problem (CVRP) span constructive search, guided local search, and ant colony optimization. RouteRepair-GLS reduces the mean TSP optimality gap from 1.7476% to 0.7587%, while the constructive CVRP heuristic lowers average route cost by 1.91% relative to the savings heuristic; the generated ACO priors also outperform matched hand-designed priors. These results show that failure-aware, evidence-constrained refinement can improve routing heuristics on difficult instances while preserving performance on cases they already solve well.

---


### 100. [BruNet: A Cross-Domain Transfer Framework for Bruise Segmentation](https://arxiv.org/abs/2609.11463)

**<font color=#1a73e8>作者：</font>** Qiming Wang, Richard J. Motley, Ebube E. Obi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmenting bruises is a challenging task in medical imaging due to limited data and annotations, diffuse boundaries, and highly variable appearance. In this work, we propose BruNet, a segmentation framework that combines a ViT-based visual encoder (a self-supervised DINOv3 or a pretrained LingBot-Vision backbone) with a SAM-based mask decoder. BruNet is trained on the HAM10000 skin lesion dataset and evaluated on a separate bruise dataset without additional fine-tuning. Although a small number of prior studies have explored machine learning and computer vision for bruise analysis, existing work has primarily focused on detection, classification, or colour analysis rather than pixel-level localisation. To the best of our knowledge, this is the first study to address automatic bruise segmentation. Our results show that BruNet outperforms CNN-based models, state-of-the-art segmentation models, ChatGPT-4o/5-assisted SAM2 zero-shot baselines, and the medical-oriented MedSAM model, demonstrating strong cross-domain generalisation to bruise segmentation.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-153](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
