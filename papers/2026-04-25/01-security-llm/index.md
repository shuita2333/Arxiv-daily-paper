# 🔐 大模型安全相关研究 | 2026年04月25日

> 本类共 **13** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Sensitivity Uncertainty Alignment in Large Language Models](https://arxiv.org/abs/2604.20903)

**<font color=#1a73e8>作者：</font>** Prakul Sunil Hiremath, Harshit R. Hiremath  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose Sensitivity-Uncertainty Alignment (SUA), a framework for analyzing failures of large language models under adversarial and ambiguous inputs. We argue that adversarial sensitivity and ambiguity reflect a common issue: misalignment between prediction instability and model uncertainty. A reliable model should express higher uncertainty when its predictions are unstable; failure to do so leads to miscalibration.
We define a scalar score, SUA_theta(x), capturing the difference between distributional sensitivity and predictive entropy. We show that minimizing its positive part bounds worst-case perturbed risk and relates to calibration error. We also formalize ambiguity collapse, where models produce overconfident outputs despite multiple valid interpretations.
We introduce SUA-TR, a training method combining consistency regularization and entropy alignment, along with an abstention rule for safer inference. Across tasks including question answering and classification, SUA better identifies model failures than entropy or self-consistency alone.
The framework is model-agnostic and provides a basis for improving reliability in evolving language models.

---


### 2. [Omission Constraints Decay While Commission Constraints Persist in Long-Context LLM Agents](https://arxiv.org/abs/2604.20911)

**<font color=#1a73e8>作者：</font>** Yeran Gamage  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents deployed in production operate under operator-defined behavioral policies (system-prompt instructions such as prohibitions on credential disclosure, data exfiltration, and unauthorized output) that safety evaluations assume hold throughout a conversation. Prohibition-type constraints decay under context pressure while requirement-type constraints persist; we term this asymmetry Security-Recall Divergence (SRD). In a 4,416-trial three-arm causal study across 12 models and 8 providers at six conversation depths, omission compliance falls from 73% at turn 5 to 33% at turn 16 while commission compliance holds at 100% (Mistral Large 3, $p < 10^{-33}$). In the two models with token-matched padding controls, schema semantic content accounts for 62-100% of the dilution effect. Re-injecting constraints before the per-model Safe Turn Depth (STD) restores compliance without retraining. Production security policies consist of prohibitions such as never revealing credentials, never executing untrusted code, and never forwarding user data. Commission-type audit signals remain healthy while omission constraints have already failed, leaving the failure invisible to standard monitoring.

---


### 3. [SafeRedirect: Defeating Internal Safety Collapse via Task-Completion Redirection in Frontier LLMs](https://arxiv.org/abs/2604.20930)

**<font color=#1a73e8>作者：</font>** Chao Pan, Yu Wu, Xin Yao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Internal Safety Collapse (ISC) is a failure mode in which frontier LLMs, when executing legitimate professional tasks whose correct completion structurally requires harmful content, spontaneously generate that content with safety failure rates exceeding 95%. Existing input-level defenses achieve a 100% failure rate against ISC, and standard system prompt defenses provide only partial mitigation. We propose SafeRedirect, a system-level override that defeats ISC by redirecting the model's task-completion drive rather than suppressing it. SafeRedirect grants explicit permission to fail the task, prescribes a deterministic hard-stop output, and instructs the model to preserve harmful placeholders unresolved. Evaluated on seven frontier LLMs across three AI/ML-related ISC task types in the single-turn setting, SafeRedirect reduces average unsafe generation rates from 71.2% to 8.0%, compared to 55.0% for the strongest viable baseline. Multi-model ablation reveals that failure permission and condition specificity are universally critical, while the importance of other components varies across models. Cross-attack evaluation confirms state-of-the-art defense against ISC with generalization performance at least on par with the baseline on other attack families. Code is available at this https URL.

---


### 4. [Adaptive Defense Orchestration for RAG: A Sentinel-Strategist Architecture against Multi-Vector Attacks](https://arxiv.org/abs/2604.20932)

**<font color=#1a73e8>作者：</font>** Pranav Pallerla, Wilson Naik Bhukya, Bharath Vemula 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) systems are increasingly deployed in sensitive domains such as healthcare and law, where they rely on private, domain-specific knowledge. This capability introduces significant security risks, including membership inference, data poisoning, and unintended content leakage. A straightforward mitigation is to enable all relevant defenses simultaneously, but doing so incurs a substantial utility cost. In our experiments, an always-on defense stack reduces contextual recall by more than 40%, indicating that retrieval degradation is the primary failure mode. To mitigate this trade-off in RAG systems, we propose the Sentinel-Strategist architecture, a context-aware framework for risk analysis and defense selection. A Sentinel detects anomalous retrieval behavior, after which a Strategist selectively deploys only the defenses warranted by the query context. Evaluated across three benchmark datasets and five orchestration models, ADO is shown to eliminate MBA-style membership inference leakage while substantially recovering retrieval utility relative to a fully static defense stack, approaching undefended baseline levels. Under data poisoning, the strongest ADO variants reduce attack success to near zero while restoring contextual recall to more than 75% of the undefended baseline, although robustness remains sensitive to model choice. Overall, these findings show that adaptive, query-aware defense can substantially reduce the security-utility trade-off in RAG systems.

---


### 5. [Breaking Bad: Interpretability-Based Safety Audits of State-of-the-Art LLMs](https://arxiv.org/abs/2604.20945)

**<font color=#1a73e8>作者：</font>** Krishiv Agarwal, Ramneet Kaur, Colin Samplawski 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Effective safety auditing of large language models (LLMs) demands tools that go beyond black-box probing and systematically uncover vulnerabilities rooted in model internals. We present a comprehensive, interpretability-driven jailbreaking audit of eight SOTA open-source LLMs: Llama-3.1-8B, Llama-3.3-70B-4bt, GPT-oss- 20B, GPT-oss-120B, Qwen3-0.6B, Qwen3-32B, Phi4-3.8B, and Phi4-14B. Leveraging interpretability-based approaches -- Universal Steering (US) and Representation Engineering (RepE) -- we introduce an adaptive two-stage grid search algorithm to identify optimal activation-steering coefficients for unsafe behavioral concepts. Our evaluation, conducted on a curated set of harmful queries and a standardized LLM-based judging protocol, reveals stark contrasts in model robustness. The Llama-3 models are highly vulnerable, with up to 91\% (US) and 83\% (RepE) jailbroken responses on Llama-3.3-70B-4bt, while GPT-oss-120B remains robust to attacks via both interpretability approaches. Qwen and Phi models show mixed results, with the smaller Qwen3-0.6B and Phi4-3.8B mostly exhibiting lower jailbreaking rates, while their larger counterparts are more susceptible. Our results establish interpretability-based steering as a powerful tool for systematic safety audits, but also highlight its dual-use risks and the need for better internal defenses in LLM deployment.

---


### 6. [Breaking MCP with Function Hijacking Attacks: Novel Threats for Function Calling and Agentic Models](https://arxiv.org/abs/2604.20994)

**<font color=#1a73e8>作者：</font>** Yannis Belkhiter, Giulio Zizzo, Sergio Maffeis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growth of agentic AI has drawn significant attention to function calling Large Language Models (LLMs), which are designed to extend the capabilities of AI-powered system by invoking external functions. Injection and jailbreaking attacks have been extensively explored to showcase the vulnerabilities of LLMs to user prompt manipulation. The expanded capabilities of agentic models introduce further vulnerabilities via their function calling interface. Recent work in LLM security showed that function calling can be abused, leading to data tampering and theft, causing disruptive behavior such as endless loops, or causing LLMs to produce harmful content in the style of jailbreaking attacks. This paper introduces a novel function hijacking attack (FHA) that manipulates the tool selection process of agentic models to force the invocation of a specific, attacker-chosen function. While existing attacks focus on semantic preference of the model for function-calling tasks, we show that FHA is largely agnostic to the context semantics and robust to the function sets, making it applicable across diverse domains. We further demonstrate that FHA can be trained to produce universal adversarial functions, enabling a single attacked function to hijack tool selection across multiple queries and payload configurations. We conducted experiments on 5 different models, including instructed and reasoning variants, reaching 70% to 100% ASR over the established BFCL dataset. Our findings further demonstrate the need for strong guardrails and security modules for agentic systems.

---


### 7. [Behavioral Consistency and Transparency Analysis on Large Language Model API Gateways](https://arxiv.org/abs/2604.21083)

**<font color=#1a73e8>作者：</font>** Guanjie Lin, Yinxin Wan, Shichao Pei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party Large Language Model (LLM) API gateways are rapidly emerging as unified access points to models offered by multiple vendors. However, the internal routing, caching, and billing policies of these gateways are largely undisclosed, leaving users with limited visibility into whether requests are served by the advertised models, whether responses remain faithful to upstream APIs, or whether invoices accurately reflect public pricing policies. To address this gap, we introduce GateScope, a lightweight black-box measurement framework for evaluating behavioral consistency and operational transparency in commercial LLM gateways. GateScope is designed to detect key misbehaviors, including model downgrading or switching, silent truncation, billing inaccuracies, and instability in latency by auditing gateways along four critical dimensions: response content analysis, multi-turn conversation performance, billing accuracy, and latency characteristics. Our measurements across 10 real-world commercial LLM API gateways reveal frequent gaps between expected and actual behaviors, including silent model substitutions, degraded memory retention, deviations from announced pricing, and substantial variation in latency stability across platforms.

---


### 8. [Adaptive Instruction Composition for Automated LLM Red-Teaming](https://arxiv.org/abs/2604.21159)

**<font color=#1a73e8>作者：</font>** Jesse Zymet, Andy Luo, Swapnil Shinde 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many approaches to LLM red-teaming leverage an attacker LLM to discover jailbreaks against a target. Several of them task the attacker with identifying effective strategies through trial and error, resulting in a semantically limited range of successes. Another approach discovers diverse attacks by combining crowdsourced harmful queries and tactics into instructions for the attacker, but does so at random, limiting effectiveness. This article introduces a novel framework, Adaptive Instruction Composition, that combines crowdsourced texts according to an adaptive mechanism trained to jointly optimize effectiveness with diversity. We use reinforcement learning to balance exploration with exploitation in a combinatorial space of instructions to guide the attacker toward diverse generations tailored to target vulnerabilities. We demonstrate that our approach substantially outperforms random combination on a set of effectiveness and diversity metrics, even under model transfer. Further, we show that it surpasses a host of recent adaptive approaches on Harmbench. We employ a lightweight neural contextual bandit that adapts to contrastive embedding inputs, and provide ablations suggesting that the contrastive pretraining enables the network to rapidly generalize and scale to the massive space as it learns.

---


### 9. [CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents](https://arxiv.org/abs/2604.21308)

**<font color=#1a73e8>作者：</font>** Wenjie Fu, Xiaoting Qin, Jue Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Enterprise LLM agents can dramatically improve workplace productivity, but their core capability, retrieving and using internal context to act on a user's behalf, also creates new risks for sensitive information leakage. We introduce CI-Work, a Contextual Integrity (CI)-grounded benchmark that simulates enterprise workflows across five information-flow directions and evaluates whether agents can convey essential content while withholding sensitive context in dense retrieval settings. Our evaluation of frontier models reveals that privacy failures are prevalent (violation rates range from 15.8%-50.9%, with leakage reaching up to 26.7%) and uncovers a counterintuitive trade-off critical for industrial deployment: higher task utility often correlates with increased privacy violations. Moreover, the massive scale of enterprise data and potential user behavior further amplify this vulnerability. Simply increasing model size or reasoning depth fails to address the problem. We conclude that safeguarding enterprise workflows requires a paradigm shift, moving beyond model-centric scaling toward context-centric architectures.

---


### 10. [A Sociotechnical, Practitioner-Centered Approach to Technology Adoption in Cybersecurity Operations: An LLM Case](https://arxiv.org/abs/2604.21679)

**<font color=#1a73e8>作者：</font>** Francis Hahn, Mohd Mamoon, Alexandru G. Bardas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Technology for security operations centers (SOCs) has a storied history of slow adoption due to concerns about trust and reliability. These concerns are amplified with artificial intelligence, particularly large language models (LLMs), which exhibit issues such as hallucinations and inconsistent outputs. To assess whether LLM-based tools can improve SOC efficiency, we embedded two PhD researchers within a multinational company SOC for six months of ethnographic fieldwork. We identified recurring challenges, such as repetitive tasks, fragmented/unclear data, and tooling bottlenecks, and collaborated directly with practitioners to develop LLM companion tools aligned with their operational needs. Iterative refinement reduced workflow disruption and improved interpretability, leading from skepticism to sustained adoption. Ethnographic analysis indicates that this shift was enabled by our sociotechnical co-creation process consistent with Nonaka's SECI model. This framework explains the common challenges in traditional SOC technology adoption, including workflow misalignment, rigidity against evolving threats and internal requirements, and stagnation over time. Our findings show that the co-creation approach can overcome these old barriers and create a new paradigm for creating usable technology for cybersecurity operations.

---


### 11. [Stealthy Backdoor Attacks against LLMs Based on Natural Style Triggers](https://arxiv.org/abs/2604.21700)

**<font color=#1a73e8>作者：</font>** Jiali Wei, Ming Fan, Guoheng Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growing application of large language models (LLMs) in safety-critical domains has raised urgent concerns about their security. Many recent studies have demonstrated the feasibility of backdoor attacks against LLMs. However, existing methods suffer from three key shortcomings: explicit trigger patterns that compromise naturalness, unreliable injection of attacker-specified payloads in long-form generation, and incompletely specified threat models that obscure how backdoors are delivered and activated in practice. To address these gaps, we present BadStyle, a complete backdoor attack framework and pipeline. BadStyle leverages an LLM as a poisoned sample generator to construct natural and stealthy poisoned samples that carry imperceptible style-level triggers while preserving semantics and fluency. To stabilize payload injection during fine-tuning, we design an auxiliary target loss that reinforces the attacker-specified target content in responses to poisoned inputs and penalizes its emergence in benign responses. We further ground the attack in a realistic threat model and systematically evaluate BadStyle under both prompt-induced and PEFT-based injection strategies. Extensive experiments across seven victim LLMs, including LLaMA, Phi, DeepSeek, and GPT series, demonstrate that BadStyle achieves high attack success rates (ASRs) while maintaining strong stealthiness. The proposed auxiliary target loss substantially improves the stability of backdoor activation, yielding an average ASR improvement of around 30% across style-level triggers. Even in downstream deployment scenarios unknown during injection, the implanted backdoor remains effective. Moreover, BadStyle consistently evades representative input-level defenses and bypasses output-level defenses through simple camouflage.

---


### 12. [Black-Box Skill Stealing Attack from Proprietary LLM Agents: An Empirical Study](https://arxiv.org/abs/2604.21829)

**<font color=#1a73e8>作者：</font>** Zihan Wang, Rui Zhang, Yu Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on skills to encapsulate reusable capabilities via progressively disclosed instructions. High-quality skills inject expert knowledge into general-purpose models, improving performance on specialized tasks. This quality and ease of dissemination drive the emergence of a skill economy: free skill marketplaces already report 90368 published skills, while paid marketplaces report more than 2000 listings and over $100,000 in creator earnings. Yet this growing marketplace also creates a new attack surface, as adversaries can interact with public agent to extract hidden proprietary skill content. We present the first empirical study of black-box skill stealing against LLM agent systems. To study this threat, we first derive an attack taxonomy from prior prompt-stealing methods and build an automated stealing prompt generation agent. This agent starts from model-generated seed prompts, expands them through scenario rationalization and structure injection, and enforces diversity via embedding filtering. This process yields a reproducible pipeline for evaluating agent systems. We evaluate such attacks across 3 commercial agent architectures and 5 LLMs. Our results show that agent skills can be extracted with only 3 interactions, posing a serious copyright risk. To mitigate this threat, we design defenses across three stages of the agent pipeline: input, inference, and output. Although these defenses achieve strong results, the attack remains inexpensive and readily automatable, allowing an adversary to launch repeated attempts with different variants; only one successful attempt is sufficient to compromise the protected skill. Overall, our findings suggest that these copyright risks are largely overlooked across proprietary agent ecosystems. We therefore advocate for more robust defense strategies that provide stronger protection guarantees.

---


### 13. [Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models](https://arxiv.org/abs/2604.21860)

**<font color=#1a73e8>作者：</font>** Naheed Rayhan, Sohely Jahan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly integrated into sensitive workflows, raising the stakes for adversarial robustness and safety. This paper introduces Transient Turn Injection(TTI), a new multi-turn attack technique that systematically exploits stateless moderation by distributing adversarial intent across isolated interactions. TTI leverages automated attacker agents powered by large language models to iteratively test and evade policy enforcement in both commercial and open-source LLMs, marking a departure from conventional jailbreak approaches that typically depend on maintaining persistent conversational context. Our extensive evaluation across state-of-the-art models-including those from OpenAI, Anthropic, Google Gemini, Meta, and prominent open-source alternatives-uncovers significant variations in resilience to TTI attacks, with only select architectures exhibiting substantial inherent robustness. Our automated blackbox evaluation framework also uncovers previously unknown model specific vulnerabilities and attack surface patterns, especially within medical and high stakes domains. We further compare TTI against established adversarial prompting methods and detail practical mitigation strategies, such as session level context aggregation and deep alignment approaches. Our study underscores the urgent need for holistic, context aware defenses and continuous adversarial testing to future proof LLM deployments against evolving multi-turn threats.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
